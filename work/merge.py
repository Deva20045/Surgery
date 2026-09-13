#!/usr/bin/env python3
"""Merge data/chNN.json chapter files into pulse-surgery-complete.html.

- Base HTML: whatever is at workspace root `pulse-surgery-complete.html`.
- Detects chapters already embedded, appends any data/chNN.json with a higher
  chapter number (ascending), flips CHAPTERS live flags, rewrites
  data/chapters_live.json.
- Idempotent: running twice changes nothing.

Usage: python3 work/merge.py [pulse-surgery-complete.html]
"""
import glob, json, os, re, sys

OUT = sys.argv[1] if len(sys.argv) > 1 else "pulse-surgery-complete.html"
if not os.path.exists(OUT):
    sys.exit("no base HTML found: pulse-surgery-complete.html")

def compact(obj):
    return json.dumps(obj, ensure_ascii=False, separators=(",", ":"))

h = open(OUT, encoding="utf-8").read()

# ---- locate the three arrays -------------------------------------------
q_start = h.find("const QUESTIONS = [")
u_decl = h.find("const UNITS = [")
c_decl = h.find("const CHAPTERS = [")
assert -1 not in (q_start, u_decl, c_decl), "array anchors not found"
q_end = h.rfind("];", q_start, u_decl)          # index of ']' closing QUESTIONS
u_end = h.rfind("];", u_decl, c_decl)           # index of ']' closing UNITS
assert q_end > q_start and u_end > u_decl

# ---- chapters already embedded ------------------------------------------
emb = sorted(set(int(x) for x in re.findall(r"SURG-C(\d+)-\d+", h[q_start:u_end])))
print(f"base: {OUT}  embedded chapters: {emb}")

# ---- new chapter data ----------------------------------------------------
news = []
for f in sorted(glob.glob("data/ch[0-9]*.json"),
                key=lambda p: int(re.search(r"ch(\d+)", p).group(1))):
    ch = int(re.search(r"ch(\d+)", f).group(1))
    if not re.fullmatch(r"data/ch\d+\.json", f):  # skip part files chNN_a.json etc.
        continue
    if ch in emb or ch <= max(emb, default=0):
        continue
    d = json.load(open(f, encoding="utf-8"))
    news.append((ch, d))
    print(f"merging ch{ch}: {len(d['questions'])} qs, {len(d['units'])} units")

def empty_before(anchor, end_idx, text):
    start = text.find(anchor) + len(anchor)
    return text[start:end_idx].strip() == ""

q_empty = empty_before("const QUESTIONS = [", q_end, h)
u_empty = empty_before("const UNITS = [", u_end, h)
q_add = ((("" if q_empty else ",") + ",".join(compact(q) for _, d in news for q in d["questions"])) if news else "")
u_add = ((("" if u_empty else ",") + ",".join(compact(u) for _, d in news for u in d["units"])) if news else "")

# splice: do UNITS first (later offset), then QUESTIONS, then CHAPTERS flags
h2 = h[:u_end] + u_add + h[u_end:]
q_end2 = q_end
h2 = h2[:q_end2] + q_add + h2[q_end2:]

# ---- CHAPTERS live flags -------------------------------------------------
live_set = set(emb) | {ch for ch, _ in news}
c_s = h2.find("const CHAPTERS = [")
c_e = h2.find("];", c_s)
block = h2[c_s:c_e]
def fix(m):
    n = int(m.group(1))
    body = m.group(0)
    if n in live_set and "live:true" not in body:
        if "live:false" in body:
            body = body.replace("live:false", "live:true")
        else:
            body = body[:-1] + ",live:true}"
    return body
block2 = re.sub(r"\{n:(\d+),[^{}]*\}", fix, block)
h2 = h2[:c_s] + block2 + h2[c_e:]

open(OUT, "w", encoding="utf-8").write(h2)

# ---- bookkeeping -----------------------------------------------------------
os.makedirs("data", exist_ok=True)
json.dump(sorted(live_set), open("data/chapters_live.json", "w"))
nq = len(set(re.findall(r'"id":"SURG-C\d+-\d+"', h2)))
nu = len(set(re.findall(r'"id":"SURG-U\d+', h2)))
print(f"written {OUT}: ~{nq} question ids, ~{nu} unit ids, live={sorted(live_set)}")
