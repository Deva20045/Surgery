#!/usr/bin/env python3
"""Print the block layout of a page region (word-merged bounding boxes) + OCR each block.
Usage: python3 work/layout.py <book> [y0] [y1] [dpi=200]
"""
import sys, os, cv2, numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from render import pdf_for
import pymupdf
from rapidocr_onnxruntime import RapidOCR
book=int(sys.argv[1]); y0=float(sys.argv[2]); y1=float(sys.argv[3]); dpi=int(sys.argv[4]) if len(sys.argv)>4 else 200
f,p=pdf_for(book)[0]
doc=pymupdf.open(f); pg=doc[p-1]
k=72.0/150.0
W=pg.rect.width/72.0*150.0  # page width in 150-dpi pixel units
pix=pg.get_pixmap(dpi=dpi, clip=pymupdf.Rect(0,y0*k,W*k,y1*k))
arr=np.frombuffer(pix.samples,dtype=np.uint8).reshape(pix.height,pix.width,pix.n)
doc.close()
g=cv2.cvtColor(cv2.cvtColor(arr,cv2.COLOR_RGB2BGR),cv2.COLOR_BGR2GRAY)
bw=cv2.adaptiveThreshold(g,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,41,15)
kx=int(0.10*dpi)  # merge words within ~0.1 inch
kernel=cv2.getStructuringElement(cv2.MORPH_RECT,(kx,3))
d=cv2.dilate(bw,kernel,iterations=1)
d=cv2.dilate(d,cv2.getStructuringElement(cv2.MORPH_RECT,(3,5)),iterations=1)
n,lab,stats,cent=cv2.connectedComponentsWithStats(d,8)
sc=150.0/dpi
items=[]
for i in range(1,n):
    x,y,w,h,a=stats[i]
    if a< 40*(dpi/150.0)**2: continue
    items.append((y*sc+y0, x*sc, (x+w)*sc, (y+h)*sc+y0))
items.sort()
ocr=RapidOCR()
for (ty,tx0,tx1,by) in items:
    sub=arr[int((ty-y0)/sc):int((by-y0)/sc), int(tx0/sc):int(tx1/sc)]
    if sub.size==0: continue
    h,w=sub.shape[:2]
    if h>0:
        big=cv2.resize(sub,None,fx=3,fy=3,interpolation=cv2.INTER_CUBIC)
        res,_=ocr(big)
        txt=" | ".join(t for _b,t,_s in (res or []))
    else: txt=""
    print(f"y{int(ty):4d}-{int(by):4d} x{int(tx0):4d}-{int(tx1):4d} :: {txt}")
