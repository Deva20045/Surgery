#!/usr/bin/env python3
"""Validator for PULSE Surgery chapter data files.

Schema (must match exactly — mirrors the ORTHO app contract):
- Question: {id:"SURG-C{ch}-{nnn}" sequential per chapter from 001, sec, page(book),
             q, opts[4], ans(idx 0-3), exp ends "(Book pX)"}
- Unit: {id:"SURG-U{ch}-{n}" sequential per chapter from 1, ch, n, title,
         sec:"<Heading> · p<page>", qs:[ids contiguous & ordered],
         guide: vivid 2-3 sentence prose}
- Units must cover every question exactly once, in order.

Usage: python3 work/validate.py data/chNN.json [more.json ...]
"""
import json, re, sys

PAGE_MAP = {  # book start-end pages per chapter (TOC-verified)
    1: (1, 5), 2: (6, 9), 3: (10, 17), 4: (18, 24), 5: (25, 27), 6: (28, 36),
    7: (37, 43), 8: (44, 48), 9: (49, 54), 10: (55, 60), 11: (61, 67), 12: (68, 74),
    13: (75, 81), 14: (82, 89), 15: (90, 101), 16: (102, 110), 17: (111, 116),
    18: (117, 125), 19: (126, 134), 20: (135, 144), 21: (145, 149), 22: (150, 156),
    23: (157, 160), 24: (161, 169), 25: (170, 178), 26: (179, 183), 27: (184, 190),
    28: (191, 196), 29: (197, 207), 30: (208, 217), 31: (218, 226), 32: (227, 232),
    33: (233, 244), 34: (245, 252), 35: (253, 259), 36: (260, 264), 37: (265, 275),
    38: (276, 284), 39: (285, 296), 40: (297, 306), 41: (307, 312), 42: (313, 317),
    43: (318, 326), 44: (327, 338), 45: (339, 352), 46: (353, 359), 47: (360, 364),
    48: (365, 370), 49: (371, 376), 50: (377, 385), 51: (386, 392), 52: (393, 398),
    53: (399, 409), 54: (410, 416), 55: (417, 425), 56: (426, 434), 57: (435, 443),
    58: (444, 450), 59: (451, 459), 60: (460, 469), 61: (470, 475), 62: (476, 485),
    63: (486, 493), 64: (494, 502), 65: (503, 508), 66: (509, 519), 67: (520, 528),
    68: (529, 534), 69: (535, 543), 70: (544, 546), 71: (547, 549), 72: (550, 558),
}

def fail(msg):
    print("  FAIL:", msg)
    sys.exit(1)

def validate(path):
    print(f"== {path}")
    d = json.load(open(path, encoding="utf-8"))
    qs, units = d["questions"], d["units"]
    if not qs:
        fail("no questions")
    m = re.match(r"SURG-C(\d+)-(\d+)", qs[0]["id"])
    ch = int(m.group(1))
    lo, hi = PAGE_MAP.get(ch, (1, 558))

    # ---- questions ----
    for i, q in enumerate(qs, 1):
        if q["id"] != f"SURG-C{ch}-{i:03d}":
            fail(f"question order/id: got {q['id']} expected SURG-C{ch}-{i:03d}")
        if len(q["opts"]) != 4:
            fail(f"{q['id']}: opts != 4")
        if not (isinstance(q["ans"], int) and 0 <= q["ans"] <= 3):
            fail(f"{q['id']}: bad ans")
        if not (lo <= q["page"] <= hi):
            fail(f"{q['id']}: page {q['page']} outside chapter range {lo}-{hi}")
        if not q["exp"].rstrip().endswith(f"(Book p{q['page']})"):
            fail(f"{q['id']}: exp must end '(Book p{q['page']})' -> ...{q['exp'][-20:]}")
        if not q["q"].strip() or any(not str(o).strip() for o in q["opts"]):
            fail(f"{q['id']}: empty text")
    print(f"  questions OK: {len(qs)} (C{ch}-001 .. C{ch}-{len(qs):03d})")

    # ---- units ----
    covered = []
    for i, u in enumerate(units, 1):
        if u["id"] != f"SURG-U{ch}-{i}":
            fail(f"unit order/id: got {u['id']} expected SURG-U{ch}-{i}")
        if u["ch"] != ch or u["n"] != i:
            fail(f"{u['id']}: ch/n mismatch")
        if not re.match(r".+ · p\d+$", u["sec"]):
            fail(f"{u['id']}: sec format '{u['sec']}'")
        if not u["qs"] or not u["guide"].strip():
            fail(f"{u['id']}: empty qs/guide")
        covered += u["qs"]
    # units cover every question exactly once, in order
    if covered != [q["id"] for q in qs]:
        want, got = set(q["id"] for q in qs), set(covered)
        missing = [x for x in (q["id"] for q in qs) if x not in got]
        dupes = [x for x in covered if covered.count(x) > 1]
        extra = [x for x in covered if x not in want]
        fail(f"coverage mismatch. missing={missing[:5]} dupes={sorted(set(dupes))[:5]} extra={extra[:5]}")
    print(f"  units OK: {len(units)} cover all {len(qs)} questions in order")
    print(f"  PASS ✓  ({path})")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(1)
    for p in sys.argv[1:]:
        validate(p)
