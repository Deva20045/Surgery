#!/usr/bin/env python3
"""OCR a rectangular region of a rendered page at high dpi, several preprocessings.
Usage: python3 work/region.py <book> <x0> <x1> <y0> <y1> [dpi=300]
coords are in the 150-dpi work/pages/bNNN.png space; they get rescaled.
"""
import os, sys
import cv2, numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from render import pdf_for

BASE_DPI = 150

def get(book, dpi):
    import pymupdf
    os.makedirs("work/hi", exist_ok=True)
    f, p = pdf_for(book)[0]
    out = f"work/hi/b{book:03d}_{dpi}.png"
    if not os.path.exists(out):
        doc = pymupdf.open(f)
        doc[p-1].get_pixmap(dpi=dpi).save(out)
        doc.close()
    return out

def main():
    book = int(sys.argv[1]); x0,x1,y0,y1 = map(int, sys.argv[2:6])
    dpi = int(sys.argv[6]) if len(sys.argv) > 6 else 300
    s = dpi / BASE_DPI
    img = cv2.imread(get(book, dpi))
    crop = img[int(y0*s):int(y1*s), int(x0*s):int(x1*s)]
    from rapidocr_onnxruntime import RapidOCR
    ocr = RapidOCR()
    variants = {}
    g = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
    variants['raw'] = crop
    variants['gray3'] = cv2.cvtColor(cv2.resize(g, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC), cv2.COLOR_GRAY2BGR)
    variants['blur'] = cv2.cvtColor(cv2.medianBlur(cv2.resize(g, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC),3), cv2.COLOR_GRAY2BGR)
    _, bw = cv2.threshold(g, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    variants['otsu'] = cv2.cvtColor(cv2.resize(bw, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC), cv2.COLOR_GRAY2BGR)
    for name, im in variants.items():
        res, _ = ocr(im)
        txt = " | ".join(t for _b, t, _s in (res or []))
        print(f"[{name}] {txt}")

main()
