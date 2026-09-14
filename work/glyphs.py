#!/usr/bin/env python3
"""Print each glyph of a region separately as ASCII art (column-gap segmentation).
Usage: python3 work/glyphs.py <book> <x0> <y0> <x1> <y1> [dpi=900] [cols_per_glyph=24] [target_h=48]
"""
import sys, os, cv2, numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from render import pdf_for
import pymupdf
book=int(sys.argv[1]); x0,y0,x1,y1=map(float,sys.argv[2:6])
dpi=int(sys.argv[7]) if len(sys.argv)>7 else 900
cg=int(sys.argv[8]) if len(sys.argv)>8 else 24
th=int(sys.argv[9]) if len(sys.argv)>9 else 48
f,p=pdf_for(book)[0]
doc=pymupdf.open(f); pg=doc[p-1]
k=72.0/150.0
pix=pg.get_pixmap(dpi=dpi, clip=pymupdf.Rect(x0*k,y0*k,x1*k,y1*k))
arr=np.frombuffer(pix.samples,dtype=np.uint8).reshape(pix.height,pix.width,pix.n)
doc.close()
img=cv2.cvtColor(arr,cv2.COLOR_RGB2BGR)
g=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
H,W=g.shape
sc=th/H
g=cv2.resize(g,(max(1,int(W*sc)),th),interpolation=cv2.INTER_AREA)
_,bw=cv2.threshold(g,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
colprof=(bw>0).sum(axis=0)
cols=np.nonzero(colprof>0)[0]
if len(cols)==0: print("empty"); sys.exit()
gapth=max(1,int(0.008*bw.shape[1]))
segs=[];start=cols[0];prev=cols[0]
for c in cols[1:]:
    if c-prev>gapth:
        segs.append((start,prev)); start=c
    prev=c
segs.append((start,prev))
scale=(x1-x0)/bw.shape[1]
print(f"{len(segs)} glyph group(s)")
for i,(a,b) in enumerate(segs):
    sub=bw[:, a:b+1]
    ys=np.nonzero(sub.any(axis=1))[0]
    sub=sub[ys.min():ys.max()+1]
    h,w=sub.shape
    rows=max(3,int(h/(w/cg)/2.1))
    r2=cv2.resize(sub.astype(np.uint8),(cg,rows),interpolation=cv2.INTER_AREA)
    print(f"--- glyph {i} page-x {x0+a*scale:.0f}..{x0+b*scale:.0f} ---")
    for r in r2:
        print("  "+"".join("#" if v>110 else "." for v in r))
