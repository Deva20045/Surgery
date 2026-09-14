#!/bin/bash
for p in "$@"; do
  echo "=============== BOOK PAGE $p ==============="
  echo "---- RAW (detection order) ----"
  sed -n '/^### raw$/,/^### geo$/p' work/ocr/b$p.txt | sed '1d;$d'
  echo "---- GEO (rows) ----"
  sed -n '/^### geo$/,/^### raw$/p' work/ocr/b$p.txt | sed '1d;$d'
done
