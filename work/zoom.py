#!/usr/bin/env python3
import os, sys, cv2
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from render import pdf_for
from rapidocr_onnxruntime import RapidOCR
book=int(sys.argv[1]); x0,x1,y0,y1=map(int,sys.argv[2:6]); dpi=int(sys.argv[6]) if len(sys.argv)>6 else 500
import pymupdf
os.makedirs("work/hi",exist_ok=True)
f,p=pdf_for(book)[0]
out=f"work/hi/b{book:03d}_{dpi}.png"
if not os.path.exists(out):
    d=pymupdf.open(f); d[p-1].get_pixmap(dpi=dpi).save(out); d.close()
s=dpi/150.0
img=cv2.imread(out)
crop=img[int(y0*s):int(y1*s), int(x0*s):int(x1*s)]
ocr=RapidOCR()
for scale in (2,4,6,8):
    for mode in ('cubic','lanczos'):
        inter=cv2.INTER_CUBIC if mode=='cubic' else cv2.INTER_LANCZOS4
        g=cv2.cvtColor(crop,cv2.COLOR_BGR2GRAY)
        g=cv2.resize(g,None,fx=scale,fy=scale,interpolation=inter)
        for pre in ('plain','sharp','otsu','adapt'):
            im=g
            if pre=='sharp':
                k=np.array([[0,-1,0],[-1,5,-1],[0,-1,0]]) if False else None
                import numpy as np
                k=np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
                im=cv2.filter2D(g,-1,k)
            elif pre=='otsu':
                _,im=cv2.threshold(g,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
            elif pre=='adapt':
                im=cv2.adaptiveThreshold(g,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,31,10)
            im=cv2.cvtColor(im,cv2.COLOR_GRAY2BGR)
            res,_=ocr(im)
            txt=" | ".join(t for _b,t,_s in (res or []))
            print(f"[{scale}x {mode} {pre}] {txt}")
