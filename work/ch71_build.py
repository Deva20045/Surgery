#!/usr/bin/env python3
"""Build data/ch71.json — Common Ulcers (pp547-549)."""
import json

Q = []


def q(page, sec, text, correct, wrongs, note=None):
    opts = [correct] + list(wrongs)
    assert len(opts) == 4
    Q.append({
        "id": f"SURG-C71-{len(Q)+1:03d}",
        "sec": sec,
        "page": page,
        "q": text,
        "opts": opts,
        "ans": 0,
        "exp": (note or correct) + f" (Book p{page})",
    })


# --------------------------------------------------------- p547
S1 = "Ulcers: Definition and Comparison of Types"
q(547, S1, "An ulcer is:", "A breach in the continuity of epithelium/mucosa", ["A raised skin lesion", "A fluid filled cavity", "A fibrous scar"])
q(547, S1, "Site of a venous ulcer:", "Gaiter area", ["Dorsum/lateral side of the foot", "Sole/base of great toe", "Heel only"])
q(547, S1, "Site of an arterial ulcer:", "Dorsum / lateral side", ["Gaiter area", "Sole/base of great toe", "Medial malleolus"])
q(547, S1, "Site of trophic and diabetic ulcers:", "Sole / base of the great toe", ["Gaiter area", "Dorsum of foot", "Lateral malleolus"])
q(547, S1, "Arterial pulsations in a venous ulcer:", "Normal", ["Absent", "Bounding", "Irregular"])
q(547, S1, "Arterial pulsations in an arterial ulcer:", "Absent", ["Normal", "Bounding", "Increased"])
q(547, S1, "Arterial pulsations in a trophic ulcer:", "Normal", ["Absent", "Always bounding", "Undetectable"])
q(547, S1, "Arterial pulsations in a diabetic ulcer:", "May be absent", ["Always normal", "Always bounding", "Always present"])
q(547, S1, "Ulcer type in which dilated veins are present:", "Venous ulcer", ["Arterial ulcer", "Trophic ulcer", "Diabetic ulcer"])
q(547, S1, "Sensations in a venous ulcer:", "Normal", ["Painful", "Decreased", "Absent"])
q(547, S1, "Sensations in an arterial ulcer:", "Painful", ["Normal", "Decreased", "Absent"])
q(547, S1, "Sensations in trophic and diabetic ulcers:", "Decreased sensations", ["Painful", "Normal", "Hyperaesthetic"])
q(547, S1, "Margin of a venous ulcer:", "Sloping", ["Punched out", "Undermined", "Rolled out"])
q(547, S1, "Margin of arterial, trophic and diabetic ulcers:", "Punched out", ["Sloping", "Undermined", "Everted"])

S2 = "Varicose Ulcer and Marjolin's Ulcer"
q(547, S2, "M/c site of a varicose ulcer:", "Medial malleolus", ["Lateral malleolus", "Dorsum of foot", "Sole"])
q(547, S2, "Depth and granulation tissue in a varicose ulcer:", "Shallow ulcer with pale granulation tissue", ["Deep ulcer with healthy granulation", "Deep ulcer with no granulation", "Shallow ulcer with exuberant granulation"])
q(547, S2, "Cause of the pigmented margin in a varicose ulcer:", "Hemosiderin deposition", ["Melanin deposition", "Bilirubin deposition", "Iron therapy"])
q(547, S2, "Healing behaviour of a varicose ulcer:", "Non-healing ulcer", ["Heals rapidly", "Heals without treatment", "Always heals in a week"])
q(547, S2, "Marjolin's ulcer is a:", "Squamous cell cancer", ["Basal cell carcinoma", "Melanoma", "Sarcoma"])
q(547, S2, "Risk factors for Marjolin's ulcer:", "Long standing venous ulcer and burn scars", ["Acute trauma", "Arterial insufficiency", "Diabetes alone"])
q(547, S2, "Margin of a Marjolin's ulcer:", "Raised, everted margins", ["Sloping margins", "Punched out margins", "Undermined margins"])
q(547, S2, "Management of Marjolin's ulcer:", "Wide local excision", ["Radiotherapy", "Skin graft alone", "Compression therapy"])
q(547, S2, "Why is radiotherapy contraindicated in Marjolin's ulcer:", "Because of scarring and recurrence", ["Because of bleeding risk", "Because it causes metastasis", "Because of poor tumour control alone"])

# --------------------------------------------------------- p548
S3 = "Arterial, Trophic and Diabetic Ulcers"
q(548, S3, "Limb features accompanying an arterial ulcer:", "Loss of muscle mass and hair with shiny skin", ["Dilated veins and pigmentation", "Increased hair growth", "Warm oedematous limb"])
q(548, S3, "Risk factors for a trophic ulcer:", "Paralyzed patients and diabetics", ["Young athletes", "Pregnant women", "Smokers only"])
q(548, S3, "Predisposing factors for a diabetic ulcer:", "Microangiopathy (arterial disease) and raised glucose", ["Venous hypertension", "Lymphatic obstruction", "Pressure alone"])
q(548, S3, "Stage 1 diabetic ulcer:", "Inflammation but no breach", ["Superficial ulcer", "Deep ulcer", "Ulcer with osteomyelitis"])
q(548, S3, "Stage 2 diabetic ulcer:", "Superficial ulcer", ["Inflammation without breach", "Deep ulcer", "Ulcer with osteomyelitis"])
q(548, S3, "Stage 3 diabetic ulcer:", "Deep ulcer", ["Superficial ulcer", "Inflammation only", "Ulcer with osteomyelitis"])
q(548, S3, "Stage 4 diabetic ulcer:", "Ulcer plus osteomyelitis", ["Deep ulcer without bone involvement", "Superficial ulcer", "Inflammation only"])
q(548, S3, "Management of a stage 1 diabetic ulcer:", "Antibiotics, diabetic control and off loading", ["Debridement and VAC dressing", "Amputation", "Observation"])
q(548, S3, "Management of stage 2 and 3 diabetic ulcers:", "Antibiotics, diabetic control, off loading plus debridement and VAC dressings", ["Amputation", "Off loading alone", "Compression bandaging"])
q(548, S3, "Management of a stage 4 diabetic ulcer:", "Amputation", ["VAC dressing alone", "Antibiotics alone", "Off loading"])
q(548, S3, "Negative pressure used in VAC dressing:", "-125 mmHg", ["-25 mmHg", "-250 mmHg", "+125 mmHg"])

# --------------------------------------------------------- p549
S4 = "Ulcer Edges"
q(549, S4, "A SLOPING ulcer edge is seen in:", "Healing and venous ulcers", ["Arterial and neuropathic ulcers", "Tubercular ulcers", "Basal cell carcinoma"])
q(549, S4, "A PUNCHED OUT ulcer edge is seen in all EXCEPT:", "Tuberculosis", ["Arterial ulcers", "Neuropathic ulcers and bed sores", "Syphilis"])
q(549, S4, "An UNDERMINED ulcer edge is characteristic of:", "Tuberculosis", ["Syphilis", "Basal cell carcinoma", "Squamous cell carcinoma"])
q(549, S4, "A ROLLED OUT, pearly white ulcer edge indicates:", "Basal cell carcinoma (rodent ulcer)", ["Squamous cell carcinoma", "Tubercular ulcer", "Venous ulcer"])
q(549, S4, "A RAISED, everted, cauliflower ulcer edge indicates:", "Squamous cell carcinoma", ["Basal cell carcinoma", "Tubercular ulcer", "Arterial ulcer"])
q(549, S4, "Bed sores typically show which ulcer edge:", "Punched out", ["Sloping", "Undermined", "Everted"])
q(549, S4, "Syphilitic ulcers typically show which edge:", "Punched out", ["Sloping", "Undermined", "Rolled out pearly"])

UNIT_DEFS = [
    (S1, "An ulcer is a breach in epithelial or mucosal continuity. Compare the four: venous ulcers sit in the gaiter area with normal pulsations, dilated veins, normal sensation and sloping margins; arterial ulcers on the dorsum/lateral side with absent pulsations, painful, punched out; trophic ulcers on the sole or base of the great toe with normal pulsations, reduced sensation and punched out margins; diabetic ulcers in the same site with possibly absent pulsations, reduced sensation and punched out margins."),
    (S2, "A varicose ulcer sits m/c at the medial malleolus, shallow, with pale granulation tissue, a hemosiderin-pigmented margin, and does not heal. Marjolin's ulcer is a squamous cell cancer developing in a long standing venous ulcer or burn scar, with raised everted margins, treated by wide local excision — radiotherapy is contraindicated because of scarring and recurrence."),
    (S3, "Arterial ulcers come with loss of muscle mass and hair and shiny skin. Trophic ulcers afflict paralyzed patients and diabetics. Diabetic ulcers stem from microangiopathy and hyperglycaemia and are staged: 1 inflammation without breach, 2 superficial ulcer, 3 deep ulcer, 4 ulcer with osteomyelitis. Stage 1 needs antibiotics, diabetic control and off loading; stages 2-3 add debridement and VAC dressings at -125 mmHg; stage 4 requires amputation."),
    (S4, "Read the edge: sloping means healing or venous; punched out means arterial, neuropathic, bed sores or syphilis; undermined means tuberculosis; rolled out and pearly white means basal cell carcinoma (rodent ulcer); raised, everted and cauliflower-like means squamous cell carcinoma."),
]

first_page = {}
for x in Q:
    first_page.setdefault(x["sec"], x["page"])

UNITS = []
for i, (title, guide) in enumerate(UNIT_DEFS, 1):
    UNITS.append({
        "id": f"SURG-U71-{i}",
        "ch": 71,
        "n": i,
        "title": title,
        "sec": f"{title} · p{first_page[title]}",
        "qs": [x["id"] for x in Q if x["sec"] == title],
        "guide": guide,
    })

covered = [x for u in UNITS for x in u["qs"]]
assert covered == [x["id"] for x in Q]
with open("data/ch71.json", "w", encoding="utf-8") as f:
    json.dump({"questions": Q, "units": UNITS}, f, ensure_ascii=False, indent=1)
print(f"ch71: {len(Q)} questions, {len(UNITS)} units")
