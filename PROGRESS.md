# PULSE Surgery — progress tracker

## Goal
Build `pulse-surgery-complete.html` (single-file quiz app, clone of the PULSE Ortho app)
line-by-line from the **Marrow Surgery Edition 8** scanned book (2 volumes, 72 chapters,
book pages 1-550) until ALL 72 chapters are live. Same style, same schema, same pipeline
as the ORTHO repo. No quality compromise: line-by-line questions, first line → last line,
strict book order, 4 options each, book page cited in every explanation.

## Sources (8 scanned PDFs, stored at repo root — NO text layer, read pages as images)
| File | Pages | **Offset formula (book page)** | Book pages covered |
|---|---|---|---|
| `Surgery Vol. 1-1-90.pdf` (v1a) | 90 | pdf 1-8 = unnumbered front matter; **pdf 9-18 → book = pdf − 8 (p1-p9)**; **pdf 19-90 → book = pdf − 9 (p10-p81)** | 1-81 |
| `Surgery Vol. 1-91-168.pdf` (v1b) | 78 | **book = pdf + 81** | 82-159 |
| `Surgery Vol. 1-168-237.pdf` (v1c) | 70 | **book = pdf + 158** (p1 duplicates v1b p78 = book p159) | 159-228 |
| `Surgery Vol. 1-238-316.pdf` (v1d) | 79 | **book = pdf + 228** (pdf 79 = blank unnumbered page after p306) | 229-306 |
| `Surgery Vol. 2_part_1.pdf` (v2a) | 82 | pdf 1-9 = unnumbered front matter; **book = pdf + 297** | 307-378 |
| `Surgery Vol. 2_part_2.pdf` (v2b) | 75 | **book = pdf + 377** | 379-452 |
| `Surgery Vol. 2_part_3.pdf` (v2c) | 71 | **book = pdf + 452** | 453-523 |
| `Surgery Vol. 2_part_4.pdf` (v2d) | 35 | **book = pdf + 523** (content to ~p556, back cover at end) | 524-558 |

**Quirk: the book itself prints page "9" twice** — v1a pdf 17 AND pdf 18 both carry header "9"
(Surgical Blades & Energy Sources). So v1a's offset flips from −8 to −9 after that duplicate.
Verified against printed headers: v1a pdf9=p1 … pdf17=p9, pdf18=p9(dup), pdf19=p10 … pdf30=p21,
pdf40=p31, pdf50=p41, pdf60=p51, pdf70=p61, pdf80=p71, pdf88=p79, pdf89=p80, pdf90=p81;
v1b pdf1=p82 / pdf78=p159; v1c pdf1=p159 / pdf70=p228; v1d pdf1=p229 / pdf78=p306;
v2a pdf10=p307 / pdf81=p377; v2b pdf1=p379 / pdf75=p452; v2c pdf1=p453 / pdf71=p523;
v2d pdf1=p524 / pdf27=p550 / pdf33=p556.
All files except v1a are provably sequential (last header − first header = page count − 1);
the only other duplicated page in the set is book p159 (v1b pdf78 = v1c pdf1, split overlap).

Book: "Surgery, Marrow Edition 8" (Vol 1: Patient Safety → Pancreatic Tumour;
Vol 2: Testicular Disorders → Surgical Instruments). Author: Dr. Rohan Khandelwal (MS General Surgery).

## Schema (must match exactly — identical to ORTHO app contract)
- Question: `{id:"SURG-C{ch}-{nnn}" sequential per chapter from 001, sec, page(book), q, opts[4], ans(idx 0-3), exp ends "(Book pX)"}`
- Unit: `{id:"SURG-U{ch}-{n}" sequential per chapter from 1, ch, n, title, sec:"<Heading> · p<page>", qs:[ids contiguous & ordered], guide: vivid 2-3 sentence prose}`
- Units must cover every question exactly once, in order.
- Deliverable format inside HTML: `const QUESTIONS = [{...}]`, `const UNITS = [{...}]` (compact JSON, natural key order), `const CHAPTERS = [{n,t,p,live:true}]`.

## Chapter page map (72 chapters, book pages; end = next start − 1)
**Vol 1** — Embryology/GI: ch1 Patient Safety, OT Zones and Surgery Positions 1-5 (v1a p9-13) ·
ch2 Surgical Blades and Energy Sources 6-9 (v1a p14-18, incl. duplicate p9) · ch3 Surgical Drains, Knots and Sutures 10-17 (v1a p19-26) ·
ch4 Post-operative Fever and Wound Infection 18-24 (v1a p27-33) · ch5 Day Care Surgery 25-27 (v1a p34-36) ·
ch6 Surgical Nutrition 28-36 (v1a p37-45) · ch7 Shock Part 1 37-43 (v1a p46-52) · ch8 Shock Part 2 44-48 (v1a p53-57) ·
**Breast:** ch9 49-54 (v1a p58-63) · ch10 55-60 (v1a p64-69) · ch11 61-67 (v1a p70-76) · ch12 68-74 (v1a p77-83) · ch13 75-81 (v1a p84-90) ·
**Endocrine:** ch14 Thyroid Part 1 82-89 (v1b p1-8) · ch15 Thyroid Part 2 90-101 (v1b p9-20) · ch16 Thyroid Part 3 102-110 (v1b p21-29) ·
ch17 Parathyroid 111-116 (v1b p30-35) · ch18 Adrenal Glands and Neuroendocrine Tumors 117-125 (v1b p36-44) ·
**GI/Abdominal:** ch19 Esophagus Part 1 126-134 (v1b p45-53) · ch20 Esophagus Part 2 135-144 (v1b p54-63) · ch21 Esophagus Part 3 145-149 (v1b p64-68) ·
ch22 Stomach Part 1 150-156 (v1b p69-75) · ch23 Stomach Part 2 157-160 (v1b p76-78 + v1c p1-2) · ch24 Stomach Part 3 161-169 (v1c p3-11) ·
ch25 Upper GI Haemorrhage 170-178 (v1c p12-20) · ch26 Bariatric Surgery 179-183 (v1c p21-25) · ch27 Bowel Obstruction Part 1 184-190 (v1c p26-32) ·
ch28 Bowel Obstruction Part 2 191-196 (v1c p33-38) · ch29 Benign Conditions of Small and Large Bowel 197-207 (v1c p39-49) · ch30 Appendix 208-217 (v1c p50-59) ·
ch31 Colorectal Polyps and Cancer Part 1 218-226 (v1c p60-68) · ch32 Colorectal Polyps and Cancer Part 2 227-232 (v1c p69-70 + v1d p1-4) ·
ch33 Rectum and Anal Canal 233-244 (v1d p5-16) · ch34 Liver Part 1 245-252 (v1d p17-24) · ch35 Liver Part 2 253-259 (v1d p25-31) ·
ch36 Spleen 260-264 (v1d p32-36) · ch37 Gall Bladder and Bile Ducts Part 1 265-275 (v1d p37-47) · ch38 Gall Bladder and Bile Ducts Part 2 276-284 (v1d p48-56) ·
ch39 Benign Pancreatic Conditions 285-296 (v1d p57-68) · ch40 Pancreatic Tumour 297-306 (v1d p69-78) ·
**Vol 2** — **Urology:** ch41 Testicular Disorders Part 1 307-312 (v2a p10-15) · ch42 Testicular Disorders Part 2 313-317 (v2a p16-20) ·
ch43 Urethral and Penile Disorders 318-326 (v2a p21-29) · ch44 Kidney Part 1 327-338 (v2a p30-41) · ch45 Kidney Part 2 339-352 (v2a p42-55) ·
ch46 Bladder 353-359 (v2a p56-62) · ch47 Prostate Part 1 360-364 (v2a p63-67) · ch48 Prostate Part 2 365-370 (v2a p68-73) ·
**Speciality:** ch49 Minimally Invasive Surgery 371-376 (v2a p74-79) · ch50 Transplant Surgery 377-385 (v2a p80-88) ·
ch51 Plastic Surgery Part 1 386-392 (v2b p7-13) · ch52 Plastic Surgery Part 2 393-398 (v2b p14-19) · ch53 Neurosurgery 399-409 (v2b p20-30) ·
**Trauma:** ch54 Basics of Trauma Management 410-416 (v2b p31-37) · ch55 Abdominal Trauma 417-425 (v2b p38-46) · ch56 Thoracic Trauma 426-434 (v2b p47-55) ·
ch57 Head Trauma 435-443 (v2b p56-64) · ch58 Thermal Injuries 444-450 (v2b p65-73) ·
**Hernia:** ch59 Hernia Part 1 451-459 (v2b p74-75 + v2c p1-7) · ch60 Hernia Part 2 460-469 (v2c p8-17) ·
**Vascular:** ch61 Venous Thrombosis 470-475 (v2c p18-23) · ch62 Varicose Veins 476-485 (v2c p24-33) · ch63 Arterial System Part 1 486-493 (v2c p34-41) ·
ch64 Arterial System Part 2 494-502 (v2c p42-50) · ch65 Lymphatic System 503-508 (v2c p51-56) ·
**Faciomaxillary:** ch66 Oral Cancers 509-519 (v2c p57-67) · ch67 Salivary Glands 520-528 (v2c p68-71 + v2d p1-5) ·
**Miscellaneous:** ch68 Skin and Soft Tissue Sarcomas 529-534 (v2d p6-11) · ch69 Thorax and Mediastinum 535-543 (v2d p12-20) ·
ch70 Common Surgical Swellings 544-546 (v2d p21-23) · ch71 Common Ulcers 547-549 (v2d p24-26) · ch72 Surgical Instruments 550-558 (v2d p27-35)

## Pipeline per chapter
1. `python3 work/render.py <book_a> <book_b> 100` (renders `work/pages/bNNN.png` using the offset table above; use 150 dpi for dense/handwritten pages)
2. read_file the pages (batches), transcribe every line mentally — strict book order
3. write `data/chNN_a.json` / `_b.json` / `_c.json` (last part holds "units"), assemble to `data/chNN.json`
4. `python3 work/validate.py data/chNN.json`
5. `python3 work/merge.py pulse-surgery-complete.html` (idempotent; appends chapters > max embedded, flips live flags, rewrites data/chapters_live.json)
6. `python3 work/integrity.py` (node-backed check of ids/coverage/live flags)
7. commit + push (per chapter, so progress is never lost)

## How to CONTINUE in a new session (user says "continue")
1. Clone the repo, read this PROGRESS.md — it is the single source of truth.
2. Source PDFs are already in the repo root (no re-upload needed).
3. Find the NEXT chapter in the Status table, run the pipeline above.
4. Commit + push data/work/docs after each chapter (NEVER the .html — local-only rule).

## Status — ALL 72 chapters (tracked from day one; "Soon" until merged)
- [x] ch1 Patient Safety, OT Zones and Surgery Positions — p1-5 — **DONE (79 qs, 12 units)** 2026-09-13
- [x] ch2 Surgical Blades and Energy Sources — p6-9 — **DONE (79 qs, 11 units)** 2026-09-13
- [x] ch3 Surgical Drains, Knots and Sutures — p10-17 — **DONE (151 qs, 16 units)** 2026-09-13
- [x] ch4 Post-operative Fever and Wound Infection — p18-24 — **DONE (131 qs, 15 units)** 2026-09-13
- [x] ch5 Day Care Surgery — p25-27 — **DONE (64 qs, 7 units)** 2026-09-13
- [x] ch6 Surgical Nutrition — p28-36 — **DONE (147 qs, 16 units)** 2026-09-13
- [x] ch7 Shock : Part 1 — p37-43 — **DONE (126 qs, 12 units)** 2026-09-13
- [x] ch8 Shock : Part 2 — p44-48 — **DONE (81 qs, 11 units)** 2026-09-13
- [x] ch9 Breast : Part 1 — p49-54 — **DONE (85 qs, 10 units)** 2026-09-13
- [x] ch10 Breast : Part 2 — p55-60 — **DONE (96 qs, 11 units)** 2026-09-13
- [x] ch11 Breast : Part 3 — p61-67 — **DONE (90 qs, 11 units)** 2026-09-13
- [x] ch12 Breast : Part 4 — p68-74 — **DONE (132 qs, 14 units)** 2026-09-13
- [x] ch13 Breast : Part 5 — p75-81 — **DONE (117 qs, 13 units)** 2026-09-13
- [x] ch14 Thyroid : Part 1 — p82-89 — **DONE (104 qs, 13 units)** 2026-09-13
- [x] ch15 Thyroid : Part 2 — p90-101 — **DONE (128 qs, 20 units)** 2026-09-13
- [x] ch16 Thyroid : Part 3 — p102-110 — **DONE (107 qs, 14 units)** 2026-09-13
- [x] ch17 Parathyroid — p111-116 — **DONE (77 qs, 13 units)** 2026-09-13
- [ ] ch18 Adrenal Glands and Neuroendocrine Tumors — p117-125 — Soon
- [ ] ch19 Esophagus : Part 1 — p126-134 — Soon
- [ ] ch20 Esophagus : Part 2 — p135-144 — Soon
- [ ] ch21 Esophagus : Part 3 — p145-149 — Soon
- [ ] ch22 Stomach : Part 1 — p150-156 — Soon
- [ ] ch23 Stomach : Part 2 — p157-160 — Soon
- [ ] ch24 Stomach : Part 3 — p161-169 — Soon
- [ ] ch25 Upper GI Haemorrhage — p170-178 — Soon
- [ ] ch26 Bariatric Surgery — p179-183 — Soon
- [ ] ch27 Bowel Obstruction : Part 1 — p184-190 — Soon
- [ ] ch28 Bowel Obstruction : Part 2 — p191-196 — Soon
- [ ] ch29 Benign Conditions of Small and Large Bowel — p197-207 — Soon
- [ ] ch30 Appendix — p208-217 — Soon
- [ ] ch31 Colorectal Polyps and Cancer : Part 1 — p218-226 — Soon
- [ ] ch32 Colorectal Polyps and Cancer : Part 2 — p227-232 — Soon
- [ ] ch33 Rectum and Anal Canal — p233-244 — Soon
- [ ] ch34 Liver : Part 1 — p245-252 — Soon
- [ ] ch35 Liver : Part 2 — p253-259 — Soon
- [ ] ch36 Spleen — p260-264 — Soon
- [ ] ch37 Gall Bladder and Bile Ducts : Part 1 — p265-275 — Soon
- [ ] ch38 Gall Bladder and Bile Ducts : Part 2 — p276-284 — Soon
- [ ] ch39 Benign Pancreatic Conditions — p285-296 — Soon
- [ ] ch40 Pancreatic Tumour — p297-306 — Soon
- [ ] ch41 Testicular Disorders : Part 1 — p307-312 — Soon
- [ ] ch42 Testicular Disorders : Part 2 — p313-317 — Soon
- [ ] ch43 Urethral and Penile Disorders — p318-326 — Soon
- [ ] ch44 Kidney : Part 1 — p327-338 — Soon
- [ ] ch45 Kidney : Part 2 — p339-352 — Soon
- [ ] ch46 Bladder — p353-359 — Soon
- [ ] ch47 Prostate : Part 1 — p360-364 — Soon
- [ ] ch48 Prostate : Part 2 — p365-370 — Soon
- [ ] ch49 Minimally Invasive Surgery — p371-376 — Soon
- [ ] ch50 Transplant Surgery — p377-385 — Soon
- [ ] ch51 Plastic surgery : Part 1 — p386-392 — Soon
- [ ] ch52 Plastic surgery : Part 2 — p393-398 — Soon
- [ ] ch53 Neurosurgery — p399-409 — Soon
- [ ] ch54 Basics of Trauma Management — p410-416 — Soon
- [ ] ch55 Abdominal Trauma — p417-425 — Soon
- [ ] ch56 Thoracic trauma — p426-434 — Soon
- [ ] ch57 Head Trauma — p435-443 — Soon
- [ ] ch58 Thermal Injuries — p444-450 — Soon
- [ ] ch59 Hernia : Part 1 — p451-459 — Soon
- [ ] ch60 Hernia : Part 2 — p460-469 — Soon
- [ ] ch61 Venous Thrombosis — p470-475 — Soon
- [ ] ch62 Varicose Veins — p476-485 — Soon
- [ ] ch63 Arterial System : Part 1 — p486-493 — Soon
- [ ] ch64 Arterial System : Part 2 — p494-502 — Soon
- [ ] ch65 Lymphatic System — p503-508 — Soon
- [ ] ch66 Oral cancers — p509-519 — Soon
- [ ] ch67 Salivary Glands — p520-528 — Soon
- [ ] ch68 Skin and Soft Tissue Sarcomas — p529-534 — Soon
- [ ] ch69 Thorax and Mediastinum — p535-543 — Soon
- [ ] ch70 Common Surgical Swellings — p544-546 — Soon
- [ ] ch71 Common Ulcers — p547-549 — Soon
- [ ] ch72 Surgical Instruments — p550-558 — Soon

## Session rule (set 2026-09-13 — KEEP until user changes it)
- Work chapter-wise in **batches of 3** (ch3-5, ch6-8, …). After each batch, **pop up the
  updated `pulse-surgery-complete.html`** to the user for preview/testing.
- ~~LOCAL-ONLY html~~ **RULE CHANGED 2026-09-13:** user wants the live GitHub Pages
  site kept in sync — commit + push `pulse-surgery-complete.html` together with
  `data/`, `work/`, `PROGRESS.md`, `README.md` after each batch (via arena branch + PR).
- Merge + integrity still run locally every batch so the preview HTML is always verified.
- After each batch, also refresh the download copy at workspace root:
  `cp pulse-surgery-complete.html /home/user/pulse-surgery-complete.html`
  (mirrors the Ortho session layout — user downloads it from the Workspace panel).

## Totals / live link
- Local HTML: **17/72 chapters live** · Questions: 1794 · Units: 219
- GitHub HTML: **synced at 17/72** (pushed 2026-09-13 after ch17)
- NEXT: ch18 Adrenal Glands and Neuroendocrine Tumors — p117-125 (v1b pdf 36-44)
- Deliverable: `pulse-surgery-complete.html` (repo root) · `index.html` redirects to it.
- LIVE LINK: https://deva20045.github.io/Surgery/ (GitHub Pages already enabled,
  deploys from main; site rebuilds ~1 min after every push to main).
- Git: push per chapter to `main` of https://github.com/Deva20045/SURGERY.
