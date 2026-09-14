#!/usr/bin/env python3
"""Render ONLY a clipped region of a page at high dpi, then OCR / ASCII it.
Usage: python3 work/zoom2.py <book> <x0> <y0> <x1> <y1> [mode=ocr|ascii] [dpi=900] [extra]
coords in 150-dpi page space.
"""
import sys, os, cv2, numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from render import pdf_for
import pymupdf

book = int(sys.argv[1]); x0, y0, x1, y1 = map(float, sys.argv[2:6])
mode = sys.argv[6] if len(sys.argv) > 6 else "ocr"
dpi = int(sys.argv[7]) if len(sys.argv) > 7 else 900
extra = int(sys.argv[8]) if len(sys.argv) > 8 else 0
f, p = pdf_for(book)[0]
doc = pymupdf.open(f)
pg = doc[p-1]
# page size at 150 dpi
w150, h150 = pg.rect.width/72*150, pg.rect.height/72*150
sc = dpi/150.0
k = 72.0/150.0  # our coords are in 150-dpi pixel space; PDF rect is in points
clip = pymupdf.Rect(x0*k, y0*k, x1*k, y1*k)
pix = pg.get_pixmap(dpi=dpi, clip=clip)
arr = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width, pix.n)
doc.close()
img = cv2.cvtColor(arr, cv2.COLOR_RGB2BGR) if pix.n >= 3 else arr
if mode == "ascii":
    cols = extra or 160
    g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    h, w = g.shape
    rows = max(3, int(h/(w/cols)/2.1))
    g2 = cv2.resize(g, (cols, rows), interpolation=cv2.INTER_AREA)
    _, bw = cv2.threshold(g2, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    for r in bw:
        print("".join("#" if v < 140 else ("+" if v < 205 else ".") for v in r))
else:
    from rapidocr_onnxruntime import RapidOCR
    ocr = RapidOCR()
    g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    for tag, im in (("gray", g), ("inv", 255-g)):
        for sc2 in (2, 3):
            big = cv2.resize(im, None, fx=sc2, fy=sc2, interpolation=cv2.INTER_CUBIC)
            res, _ = ocr(cv2.cvtColor(big, cv2.COLOR_GRAY2BGR))
            print(f"[{tag} x{sc2}] " + " | ".join(t for _b, t, _s in (res or [])))
