#!/usr/bin/env python3
"""Render only a clip at high dpi, then OCR it through several colour/contrast variants.
Best weapon for handwriting lines RapidOCR garbles.
Usage: python3 work/chan.py <book> <x0> <y0> <x1> <y1> [dpi=900]
"""
import sys, os, cv2, numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from render import pdf_for
import pymupdf
from rapidocr_onnxruntime import RapidOCR

book = int(sys.argv[1]); x0, y0, x1, y1 = map(float, sys.argv[2:6])
dpi = int(sys.argv[7]) if len(sys.argv) > 7 else 900
f, p = pdf_for(book)[0]
doc = pymupdf.open(f); pg = doc[p-1]
k = 72.0/150.0
pix = pg.get_pixmap(dpi=dpi, clip=pymupdf.Rect(x0*k, y0*k, x1*k, y1*k))
arr = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width, pix.n)
doc.close()
img = cv2.cvtColor(arr, cv2.COLOR_RGB2BGR)
b, g, r = cv2.split(img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8)).apply(gray)
V = {'gray': gray, 'inv': 255-gray, 'R': r, 'G': g, 'B': b,
     'R-B': cv2.subtract(r, b), 'B-R': cv2.subtract(b, r),
     'otsu': otsu, 'clahe': clahe}
ocr = RapidOCR()
seen = {}
for tag, im in V.items():
    for sc in (2, 3):
        big = cv2.resize(im, None, fx=sc, fy=sc, interpolation=cv2.INTER_CUBIC)
        res, _ = ocr(cv2.cvtColor(big, cv2.COLOR_GRAY2BGR))
        txt = " | ".join(t for _x, t, _s in (res or []))
        if txt and txt not in seen:
            seen[txt] = 1
            print(f"[{tag} x{sc}] {txt}")
