#!/usr/bin/env python3
"""Re-OCR a small region of an already-OCR'd page (for garbled / rotated bits).

Usage:
    python3 work/crop.py <book> <i|i,j,k|all> [pad=25] [rot=auto|0|90|270] [scale=3]

`i` is the 0-based index of a box in work/ocr/box/bNNN.json (boxes are printed
with their index by `--list`).  Use `all` to sweep every box (slow but thorough)
or a range like `3-9`.
"""
import json
import os
import sys

import cv2

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from render import pdf_for  # noqa: E402

PAGES_DIR = "work/pages"
BOX_DIR = "work/text/box"


def load(book):
    tag = f"b{book:03d}"
    items = json.load(open(f"{BOX_DIR}/{tag}.json", encoding="utf-8"))
    return tag, items


def parse(sel, n):
    if sel == "all":
        return list(range(n))
    out = []
    for part in sel.split(","):
        if "-" in part:
            a, b = part.split("-")
            out += list(range(int(a), int(b) + 1))
        else:
            out.append(int(part))
    return out


def main(argv):
    if len(argv) < 3:
        print(__doc__)
        sys.exit(1)
    book = int(argv[1])
    sel = argv[2]
    pad = int(argv[3]) if len(argv) > 3 else 25
    rot = argv[4] if len(argv) > 4 else "auto"
    scale = float(argv[5]) if len(argv) > 5 else 3.0
    tag, items = load(book)
    png = None
    for cand in (f"{PAGES_DIR}/{tag}.png", f"{PAGES_DIR}/{tag}a.png"):
        if os.path.exists(cand):
            png = cand
            break
    if png is None:
        import pymupdf
        png = f"{PAGES_DIR}/{tag}.png"
        os.makedirs(PAGES_DIR, exist_ok=True)
        f, p = pdf_for(book)[0]
        doc = pymupdf.open(f)
        doc[p - 1].get_pixmap(dpi=200).save(png)
        doc.close()
    img = cv2.imread(png)
    H, W = img.shape[:2]
    if len(argv) > 2 and sel == "list":
        for i, it in enumerate(items):
            print(f"{i:3d} y{it['yc']:6.0f} x[{it['x0']:5.0f},{it['x1']:5.0f}] {it['t'][:70]}")
        return
    from rapidocr_onnxruntime import RapidOCR
    ocr = RapidOCR()
    idxs = parse(sel, len(items))
    for i in idxs:
        it = items[i]
        # NOTE: box coords came from the OCR run on `png`; if png was re-rendered
        # at a different dpi the coords are scaled accordingly.
        sx = W / json.load(open(f"{BOX_DIR}/{tag}.json", encoding="utf-8"))[0].get("_w", W) if False else 1
        x0 = max(0, int(it["x0"] * sx) - pad)
        x1 = min(W, int(it["x1"] * sx) + pad)
        y0 = max(0, int(it["yc"] * sx) - 45 - pad)
        y1 = min(H, int(it["yc"] * sx) + 45 + pad)
        crop = img[y0:y1, x0:x1]
        rots = {"0": [None], "90": [cv2.ROTATE_90_CLOCKWISE],
                "270": [cv2.ROTATE_90_COUNTERCLOCKWISE],
                "auto": [None, cv2.ROTATE_90_CLOCKWISE,
                         cv2.ROTATE_90_COUNTERCLOCKWISE, cv2.ROTATE_180]}[rot]
        print(f"--- #{i} {it['t'][:60]!r} ---")
        best = []
        for r in rots:
            im = crop if r is None else cv2.rotate(crop, r)
            im = cv2.resize(im, None, fx=scale, fy=scale, interpolation=cv2.INTER_CUBIC)
            im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            im = cv2.cvtColor(im, cv2.COLOR_GRAY2BGR)
            res, _ = ocr(im)
            txt = " / ".join(t for _b, t, _s in (res or []))
            best.append((len(txt), txt))
            print(f"    rot {r if r is None else 'x'}: {txt}")
        if rot == "auto":
            print(f"  >> best: {max(best)[1][:200]}")


if __name__ == "__main__":
    os.environ.setdefault("OMP_NUM_THREADS", "2")
    main(sys.argv)
