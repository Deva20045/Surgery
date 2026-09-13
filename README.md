# PULSE · Surgery — Marrow Edition 8 Companion

Single-file quiz app (`pulse-surgery-complete.html`) being extended chapter-by-chapter,
line-by-line from the Marrow Surgery Edition 8 book (2 volumes, **72 chapters**, book pages 1-550).

**Live: 2/72 chapters** — see PROGRESS.md for the build tracker.

## Repo layout
```
pulse-surgery-complete.html   ← the deliverable app (open in any browser)
index.html                    ← redirect -> pulse-surgery-complete.html
data/chNN.json                ← per-chapter source data {questions, units}
data/chapters_live.json       ← list of chapters merged into the app
work/render.py                ← render book pages from source PDFs to PNG
work/validate.py              ← schema validator for data/chNN.json
work/merge.py                 ← merge data into the HTML (idempotent)
work/integrity.py             ← post-merge integrity check (node-backed)
PROGRESS.md                   ← memory / single source of truth for continuation
Surgery Vol. 1-*.pdf, Surgery Vol. 2_part_*.pdf   ← scanned source PDFs (no text layer)
```

## ▶ Play
Open `index.html` (or `pulse-surgery-complete.html`) in any browser.

## Continue work (new session)
1. Say **"continue"** in the Arena session — the agent reads PROGRESS.md (single source of truth).
2. Source PDFs are stored in this repo root — no re-upload needed.
3. Pipeline per chapter: `work/render.py` → read pages as images → write `data/chNN.json`
   → `work/validate.py` → `work/merge.py` → `work/integrity.py` → commit + push.

## Schema contract (see PROGRESS.md for full detail)
- Question: `{id:"SURG-C{ch}-{nnn}", sec, page, q, opts[4], ans, exp}` — exp ends `(Book pX)`.
- Unit: `{id:"SURG-U{ch}-{n}", ch, n, title, sec:"<Heading> · p<page>", qs:[...], guide}`.
- Units cover every question exactly once, strictly in book order.

## Checks before shipping a chapter
```bash
python3 work/validate.py data/chNN.json
python3 work/merge.py pulse-surgery-complete.html
python3 work/integrity.py
```
