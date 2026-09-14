#!/usr/bin/env python3
"""Render + OCR book pages and print them in COLUMN-AWARE reading order.

The Marrow Surgery note pages are frequently laid out in two (sometimes three)
columns. Row-based geometric ordering merges the columns together and makes
transcription error-prone, so this helper:

  1. renders the book page to PNG (reusing render.pdf_for),
  2. runs RapidOCR (offline, PP-OCRv4),
  3. caches the raw boxes to work/ocr/box/bNNN.json,
  4. detects vertical gutters (x ranges covered by no box) and splits the page
     into columns,
  5. prints each column top-to-bottom, columns left-to-right.

Usage:
    python3 work/ocrbox.py <book_a> <book_b> [dpi=150] [--force]
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from render import pdf_for  # noqa: E402

PAGES_DIR = "work/pages"
BOX_DIR = "work/ocr/box"


def render(book, dpi, force=False):
    os.makedirs(PAGES_DIR, exist_ok=True)
    import pymupdf
    out = []
    locs = pdf_for(book) or []
    for i, (f, pdf) in enumerate(locs):
        name = f"{PAGES_DIR}/b{book:03d}{chr(97 + i) if len(locs) > 1 else ''}.png"
        if os.path.exists(name) and not force:
            out.append(name)
            continue
        doc = pymupdf.open(f)
        doc[pdf - 1].get_pixmap(dpi=dpi).save(name)
        doc.close()
        out.append(name)
    return out


def boxes(png, ocr, cache, force):
    if os.path.exists(cache) and not force:
        return json.load(open(cache, encoding="utf-8"))
    res, _ = ocr(png)
    items = []
    for box, text, _score in (res or []):
        xs = [p[0] for p in box]
        ys = [p[1] for p in box]
        items.append({"x0": min(xs), "x1": max(xs),
                      "yc": (min(ys) + max(ys)) / 2, "t": text})
    os.makedirs(os.path.dirname(cache), exist_ok=True)
    json.dump(items, open(cache, "w", encoding="utf-8"), ensure_ascii=False)
    return items


def split_columns(items, page_w):
    """Return list of (x0, x1, [items]) columns, separated by empty gutters."""
    if not items:
        return []
    # occupancy histogram over x (16 px bins)
    bw = 16
    nb = int(page_w // bw) + 2
    occ = [0] * nb
    for it in items:
        for b in range(int(it["x0"] // bw), int(it["x1"] // bw) + 1):
            if 0 <= b < nb:
                occ[b] += 1
    # find gutters: runs of empty bins at least 5 bins (80 px) wide
    gaps, run = [], None
    for b in range(nb):
        if occ[b] == 0:
            run = b if run is None else run
        else:
            if run is not None and b - run >= 5:
                gaps.append((run * bw, b * bw))
            run = None
    if run is not None and nb - run >= 5:
        gaps.append((run * bw, nb * bw))
    # only keep gutters that actually separate content (ignore page margins)
    cuts = []
    for g0, g1 in gaps:
        left = [i for i in items if i["x1"] <= g0 + 4]
        right = [i for i in items if i["x0"] >= g1 - 4]
        if len(left) >= 6 and len(right) >= 6:
            cuts.append((g0 + g1) / 2)
    bounds = [0] + cuts + [page_w * 2]
    cols = []
    for i in range(len(bounds) - 1):
        lo, hi = bounds[i], bounds[i + 1]
        sel = [it for it in items if lo - 4 <= (it["x0"] + it["x1"]) / 2 < hi + 4]
        if sel:
            cols.append((min(i2["x0"] for i2 in sel), max(i2["x1"] for i2 in sel), sel))
    cols.sort(key=lambda c: c[0])
    return cols


def clusters_of(row, gap=50.0):
    """Split one y-row into horizontal clusters (separate columns / table cells)."""
    row = sorted(row, key=lambda z: z["x0"])
    out, cur = [], [row[0]]
    for it in row[1:]:
        if it["x0"] - cur[-1]["x1"] > gap:
            out.append(cur)
            cur = [it]
        else:
            cur.append(it)
    out.append(cur)
    return out


def rows_of(items):
    """Group items into rows (by y-centre); each row is split into x-clusters and
    every cluster printed on its own line, indented to show its column."""
    hs = sorted(it["x1"] - it["x0"] for it in items)
    med_h = hs[len(hs) // 2] if hs else 20
    ys = sorted((it for it in items), key=lambda i2: i2["yc"])
    gaps = [ys[i + 1]["yc"] - ys[i]["yc"] for i in range(len(ys) - 1)]
    gaps = [g for g in gaps if g > 2]
    med_gap = sorted(gaps)[len(gaps) // 2] if gaps else med_h
    tol = max(6.0, med_gap * 0.6)
    out, cur, cur_y = [], [], None
    for it in ys:
        if cur_y is None or abs(it["yc"] - cur_y) <= tol:
            cur.append(it)
            cur_y = it["yc"] if cur_y is None else cur_y
        else:
            out.append(cur)
            cur, cur_y = [it], it["yc"]
    if cur:
        out.append(cur)
    lines = []
    for r in out:
        for cl in clusters_of(r):
            txt = " ".join(i2["t"] for i2 in cl)
            lines.append(" " * int(min(cl[0]["x0"], 900) / 55) + txt)
    return lines


def main(argv):
    args = [a for a in argv[1:] if not a.startswith("--")]
    force = "--force" in argv[1:]
    if len(args) < 2:
        print(__doc__)
        sys.exit(1)
    a, b = int(args[0]), int(args[1])
    dpi = int(args[2]) if len(args) > 2 else 150
    from rapidocr_onnxruntime import RapidOCR
    ocr = RapidOCR()
    import pymupdf
    for book in range(a, b + 1):
        pngs = render(book, dpi, force)
        for png in pngs:
            tag = os.path.basename(png)[:-4]
            cache = f"{BOX_DIR}/{tag}.json"
            items = boxes(png, ocr, cache, force)
            import cv2
            w = cv2.imread(png).shape[1]
            cols = split_columns(items, w)
            print(f"\n===== {tag} ({len(items)} boxes, {len(cols)} column(s)) =====")
            if len(cols) <= 1:
                for line in rows_of(items):
                    print(line)
            else:
                blocks = [rows_of(c[2]) for c in cols]
                for i, blk in enumerate(blocks, 1):
                    print(f"--- col{i} ---")
                    for line in blk:
                        print(line)


if __name__ == "__main__":
    os.environ.setdefault("OMP_NUM_THREADS", "2")
    main(sys.argv)
