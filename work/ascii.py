#!/usr/bin/env python3
"""ASCII-art rendering of a page region.
Usage: python3 work/ascii.py <book> <x0> <x1> <y0> <y1> [dpi=600] [cols=110] [rows=0]
"""
import sys, os, cv2
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from render import pdf_for

book=int(sys.argv[1]); x0,x1,y0,y1=map(int,sys.argv[2:6])
dpi=int(sys.argv[6]) if len(sys.argv)>6 else 600
cols=int(sys.argv[7]) if len(sys.argv)>7 else 110
rows=int(sys.argv[8]) if len(sys.argv)>8 else 0
import pymupdf
os.makedirs("work/hi",exist_ok=True)
f,p=pdf_for(book)[0]
out=f"work/hi/b{book:03d}_{dpi}.png"
if not os.path.exists(out):
    d=pymupdf.open(f); d[p-1].get_pixmap(dpi=dpi).save(out); d.close()
s=dpi/150.0
img=cv2.imread(out)
crop=img[int(y0*s):int(y1*s), int(x0*s):int(x1*s)]
g=cv2.cvtColor(crop,cv2.COLOR_BGR2GRAY)
h,w=g.shape
if not rows:
    rows=max(3,int(h/(w/cols)/2.1))
g=cv2.resize(g,(cols, rows), interpolation=cv2.INTER_AREA)
_,bw=cv2.threshold(g,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
for r in bw:
    print("".join("#" if v<140 else ("+" if v<205 else ".") for v in r))
