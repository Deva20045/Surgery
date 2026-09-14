#!/usr/bin/env python3
"""OCR helper for the scanned Marrow Surgery PDFs.

The source PDFs have NO text layer, so pages are rendered to PNG (PyMuPDF) and
run through RapidOCR (PP-OCRv4, ONNX - fully offline, models ship in the wheel).

Usage:
    python3 work/ocr.py <book_a> <book_b> [dpi=150]      # render + OCR -> work/ocr/bNNN.txt
    python3 work/ocr.py <book_a> <book_b> --force        # re-do even if txt exists

Reading order: boxes are grouped into rows by their y-centre (tolerance scales
with median line height) and each row is sorted left-to-right, which restores
the natural top-to-bottom order of these note pages (incl. 2-column pages).
"""
import os
import subprocess
import sys

# reuse the verified book-page -> (pdf, pdf_page) mapping from render.py
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from render import pdf_for  # noqa: E402

OUT_DIR = "work/ocr"
PAGES_DIR = "work/pages"


def render(book, dpi, force=False):
    """Render one book page to PNG (all variants, e.g. the duplicated p9)."""
    os.makedirs(PAGES_DIR, exist_ok=True)
    import pymupdf
    out = []
    for i, (f, pdf) in enumerate(pdf_for(book) or []):
        name = f"{PAGES_DIR}/b{book:03d}{chr(97 + i) if len(pdf_for(book)) > 1 else ''}.png"
        if os.path.exists(name) and not force:
            out.append(name)
            continue
        doc = pymupdf.open(f)
        doc[pdf - 1].get_pixmap(dpi=dpi).save(name)
        doc.close()
        out.append(name)
    return out


def order_lines(res):
    """Sort OCR boxes into reading order: rows by y-centre, then x."""
    if not res:
        return []
    items = []
    for box, text, _score in res:
        xs = [p[0] for p in box]
        ys = [p[1] for p in box]
        items.append(((min(ys) + max(ys)) / 2, min(xs), text))
    heights = sorted(max(p[0] for p in r[0]) - min(p[0] for p in r[0]) for r in res)
    med_h = heights[len(heights) // 2] if heights else 20
    tol = max(6.0, med_h * 0.6)
    items.sort(key=lambda t: (t[0], t[1]))
    rows, cur, cur_y = [], [], None
    for y, x, text in items:
        if cur_y is None or abs(y - cur_y) <= tol:
            cur.append((x, text))
            cur_y = y if cur_y is None else cur_y
        else:
            rows.append(cur)
            cur, cur_y = [(x, text)], y
    if cur:
        rows.append(cur)
    return ["  ".join(t for _, t in sorted(row, key=lambda r: r[0])) for row in rows]


def main(argv):
    args = [a for a in argv[1:] if not a.startswith("--")]
    force = "--force" in argv[1:]
    if len(args) < 2:
        print(__doc__)
        sys.exit(1)
    a, b = int(args[0]), int(args[1])
    dpi = int(args[2]) if len(args) > 2 else 150
    os.makedirs(OUT_DIR, exist_ok=True)
    from rapidocr_onnxruntime import RapidOCR
    ocr = RapidOCR()
    for book in range(a, b + 1):
        txt_path = f"{OUT_DIR}/b{book:03d}.txt"
        if os.path.exists(txt_path) and not force:
            print(f"b{book:03d}: cached")
            continue
        pngs = render(book, dpi, force)
        chunks = []
        for png in pngs:
            res, _ = ocr(png)
            # 1) detection order (PP-OCR emits boxes roughly in reading order)
            chunks.append("### raw")
            chunks += [r[1] for r in (res or [])]
            # 2) geometric order (rows by y-centre, then x) - cross-check
            chunks.append("### geo")
            chunks += order_lines(res)
        with open(txt_path, "w", encoding="utf-8") as fh:
            fh.write("\n".join(chunks) + "\n")
        print(f"b{book:03d}: {len(chunks)} lines -> {txt_path}")


if __name__ == "__main__":
    # keep numpy/blas from oversubscribing the box
    os.environ.setdefault("OMP_NUM_THREADS", "2")
    main(sys.argv)
