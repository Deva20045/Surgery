#!/usr/bin/env python3
"""Save a high-dpi clip of a book page to work/inspect/ for visual checking.
Usage: python3 work/clip.py <book> <x0> <y0> <x1> <y1> <out.png> [dpi=400]
coords in 150-dpi page space.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from render import pdf_for
import pymupdf

book = int(sys.argv[1]); x0, y0, x1, y1 = map(float, sys.argv[2:6])
out = sys.argv[6]
dpi = int(sys.argv[7]) if len(sys.argv) > 7 else 400
f, p = pdf_for(book)[0]
doc = pymupdf.open(f)
pg = doc[p - 1]
k = 72.0 / 150.0
clip = pymupdf.Rect(x0 * k, y0 * k, x1 * k, y1 * k)
pix = pg.get_pixmap(dpi=dpi, clip=clip)
os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
pix.save(out)
print(out, pix.width, pix.height)
doc.close()
