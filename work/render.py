#!/usr/bin/env python3
"""Render book pages from the source PDFs to PNGs for transcription.

Source mapping (from PROGRESS.md — verified against printed page headers):

  v1a "Surgery Vol. 1-1-90.pdf" (90 pages):
      pdf 1-8  = unnumbered front matter (cover, author, title, instructions, TOC x3, blank)
      pdf 9-18 = book p1-p9   (book = pdf - 8)
      pdf 18   = DUPLICATE book p9  (the book itself prints "9" twice: pdf 17 AND pdf 18)
      pdf 19-90= book p10-p81 (book = pdf - 9)
  v1b "Surgery Vol. 1-91-168.pdf" (78 pages): book = pdf + 81   -> book 82-159
  v1c "Surgery Vol. 1-168-237.pdf"(70 pages): book = pdf + 158  -> book 159-228 (p159 duplicates v1b p78)
  v1d "Surgery Vol. 1-238-316.pdf"(79 pages): book = pdf + 228  -> book 229-306 (pdf 79 = blank, unnumbered)
  v2a "Surgery Vol. 2_part_1.pdf" (82 pages): pdf 1-9 = unnumbered front matter (cover, author, title,
      instructions, TOC x3, blanks); book = pdf + 297 -> book 307-378
  v2b "Surgery Vol. 2_part_2.pdf" (75 pages): book = pdf + 377  -> book 379-452
  v2c "Surgery Vol. 2_part_3.pdf" (71 pages): book = pdf + 452  -> book 453-523
  v2d "Surgery Vol. 2_part_4.pdf" (35 pages): book = pdf + 523  -> book 524-558 (content ends ~p558; back cover included)

Every other file is provably sequential (last header - first header == page count - 1).
The duplicate book p9 in v1a is real (printed in the book), so render book 9 twice.

Usage: python3 work/render.py <book_page_a> <book_page_b> [dpi=100]
Output: work/pages/bNNN.png (NNN = zero-padded book page; for the duplicated p9 use b009a/b009b via -dup)
"""
import os, sys

def pdf_for(book):
    """Return list of (file, pdf_page) for a book page (usually one; book p9 has two)."""
    if 1 <= book <= 8:
        return [("Surgery Vol. 1-1-90.pdf", book + 8)]
    if book == 9:  # the book prints page 9 twice
        return [("Surgery Vol. 1-1-90.pdf", 17), ("Surgery Vol. 1-1-90.pdf", 18)]
    if 10 <= book <= 81:
        return [("Surgery Vol. 1-1-90.pdf", book + 9)]
    if 82 <= book <= 159:
        return [("Surgery Vol. 1-91-168.pdf", book - 81)]
    if 159 <= book <= 228:
        return [("Surgery Vol. 1-168-237.pdf", book - 158)]
    if 229 <= book <= 306:
        return [("Surgery Vol. 1-238-316.pdf", book - 228)]
    if 307 <= book <= 326:
        return [("Surgery Vol. 2_part_1.pdf", book - 297)]
    if 327 <= book <= 378:
        return [("Surgery Vol. 2_part_1.pdf", book - 296)]
    if 379 <= book <= 452:
        return [("Surgery Vol. 2_part_2.pdf", book - 377)]
    if 453 <= book <= 523:
        return [("Surgery Vol. 2_part_3.pdf", book - 452)]
    if 524 <= book <= 558:
        return [("Surgery Vol. 2_part_4.pdf", book - 523)]
    return None

def render(a, b, dpi=100):
    try:
        import fitz  # PyMuPDF
    except ImportError:
        os.system("pip3 install -q --break-system-packages pymupdf")
        import fitz
    os.makedirs("work/pages", exist_ok=True)
    for book in range(a, b + 1):
        locs = pdf_for(book)
        if not locs:
            print(f"!! b{book:03d}: book page out of range 1-558")
            continue
        for i, (f, pdf) in enumerate(locs):
            if not os.path.exists(f):
                print(f"!! b{book:03d}: file missing: {f}")
                continue
            doc = fitz.open(f)
            if pdf < 1 or pdf > doc.page_count:
                print(f"!! b{book:03d}: page {pdf} out of range in {f}")
                doc.close()
                continue
            pix = doc[pdf - 1].get_pixmap(dpi=dpi)
            out = f"work/pages/b{book:03d}{chr(97+i) if len(locs)>1 else ''}.png"
            pix.save(out)
            print(f"b{book:03d} <- {os.path.basename(f)} p{pdf} -> {out} ({pix.width}x{pix.height})")
            doc.close()

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(__doc__); sys.exit(1)
    render(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]) if len(sys.argv) > 3 else 100)
