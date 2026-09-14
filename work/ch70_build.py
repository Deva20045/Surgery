#!/usr/bin/env python3
"""Build data/ch70.json — Common Surgical Swellings (pp544-546)."""
import json

Q = []


def q(page, sec, text, correct, wrongs, note=None):
    opts = [correct] + list(wrongs)
    assert len(opts) == 4
    Q.append({
        "id": f"SURG-C70-{len(Q)+1:03d}",
        "sec": sec,
        "page": page,
        "q": text,
        "opts": opts,
        "ans": 0,
        "exp": (note or correct) + f" (Book p{page})",
    })


# --------------------------------------------------------- p544
S1 = "Sebaceous Cyst"
q(544, S1, "A sebaceous cyst arises from:", "A blocked hair follicle duct", ["A blocked sweat gland", "Trapped epithelium along fusion lines", "Encapsulated fat"])
q(544, S1, "Sites where a sebaceous cyst can NEVER occur:", "Palms and soles, as they have no hair follicles", ["Scalp", "Scrotum", "Face"])
q(544, S1, "Characteristic skin sign of a sebaceous cyst:", "Skin cannot be pinched over the swelling, as it arises from skin", ["Skin can be pinched freely", "Skin is ulcerated", "Skin is pigmented"])
q(544, S1, "Characteristic central feature of a sebaceous cyst:", "A whitish centre — the punctum", ["A black eschar", "A pearly nodule", "A sinus opening"])
q(544, S1, "Discharge from a sebaceous cyst:", "Whitish discharge", ["Serous discharge", "Blood stained discharge", "No discharge ever"])
q(544, S1, "Multiple sebaceous cysts are m/c seen in the:", "Scrotum and scalp", ["Palms and soles", "Axilla and groin", "Back and abdomen"])
q(544, S1, "Sebaceous horn is formed when:", "Secretions harden to form a horn like structure", ["The cyst becomes infected", "The cyst turns malignant", "The cyst calcifies into bone"])
q(544, S1, "Management of a sebaceous cyst:", "Excision of the cyst", ["Incision and drainage", "Aspiration", "Observation only"])

S2 = "Dermoid Cyst"
q(544, S2, "Pathophysiology of a dermoid cyst:", "Epithelial tissue trapped along the lines of embryonic fusion", ["Blocked hair follicle duct", "Encapsulated fat", "Lymphatic sequestration"])
q(544, S2, "Classic sites of a dermoid cyst:", "Outer canthus of the eye and post auricular region", ["Palms and soles", "Scrotum and scalp", "Nape of the neck"])
q(544, S2, "Key clinical difference of a dermoid cyst from a sebaceous cyst:", "Skin CAN be pinched over the swelling", ["Skin cannot be pinched", "It has a punctum", "It is non-fluctuant"])
q(544, S2, "Fluctuation in a dermoid cyst:", "Present — it is a cystic swelling", ["Absent", "Only pseudofluctuation", "Pulsatile"])
q(544, S2, "Why must X-ray/CT be done before excising a dermoid cyst:", "To rule out intracranial extension", ["To assess bone density", "To detect calcification only", "To stage malignancy"])
q(544, S2, "Management of a dermoid cyst:", "Surgical excision", ["Aspiration", "Sclerotherapy", "Observation"])
q(544, S2, "An implantation dermoid occurs due to:", "Injury — m/c after ear piercing", ["Embryonic fusion failure", "Blocked duct", "Infection"])
q(544, S2, "Management of an implantation dermoid:", "Surgical excision", ["Antibiotics", "Aspiration", "Observation"])

# --------------------------------------------------------- p545
S3 = "Lipoma"
q(545, S3, "A lipoma is:", "An encapsulated collection of fat", ["A blocked hair follicle", "Trapped epithelium", "A collection of lymph"])
q(545, S3, "M/c swelling in the body:", "Lipoma", ["Sebaceous cyst", "Dermoid cyst", "Branchial cyst"])
q(545, S3, "Skin sign of a lipoma:", "Skin can be pinched over the swelling, as it arises from subcutaneous tissue", ["Skin cannot be pinched", "Punctum present", "Skin ulcerated"])
q(545, S3, "Pseudofluctuation in lipoma means:", "The swelling expands only in one axis", ["The swelling expands in all axes", "There is no expansion", "The swelling pulsates"])
q(545, S3, "Sign classically positive in lipoma:", "Slip sign", ["Punctum sign", "Stemmer sign", "Hutchinson's sign"])
q(545, S3, "Dercum's disease is:", "Multiple lipomas / lipomatosis, a benign condition managed by observation", ["Malignant transformation of a lipoma", "Multiple sebaceous cysts", "Multiple dermoid cysts"])
q(545, S3, "Indication for excising a lipoma:", "If symptomatic (painful) or large", ["All lipomas always", "Only if multiple", "Never"])
q(545, S3, "Lipoma sites with high potential for sarcomatous change:", "Retroperitoneum, thigh and between the shoulder blades", ["Forearm, calf and scalp", "Face and neck", "Palms and soles"])

S4 = "Tubercular Cervical Lymphadenopathy"
q(545, S4, "Cervical lymphadenopathy means:", "Cervical lymph node enlargement due to pathological or reactive causes", ["Only malignant node enlargement", "Salivary gland swelling", "Thyroid enlargement"])
q(545, S4, "M/c pathological cause of cervical lymphadenopathy in India:", "Tuberculosis", ["Metastatic carcinoma", "Lymphoma", "Reactive hyperplasia"])
q(545, S4, "First step in the pathophysiology of tubercular cervical lymphadenopathy:", "Tubercular bacilli infect the cervical lymph nodes causing caseous necrosis", ["Immediate abscess rupture", "Fascial adherence first", "Sinus formation first"])
q(545, S4, "Periadenitis in tubercular lymphadenopathy leads to:", "Matting of lymph nodes", ["Discrete mobile nodes", "Node regression", "Calcification only"])
q(545, S4, "Third stage of tubercular cervical lymphadenopathy:", "Lymph nodes coalesce and become adherent to the deep fascia", ["Nodes remain discrete", "Immediate sinus formation", "Caseation resolves"])
q(545, S4, "Collar stud abscess is:", "A cold abscess with no signs of inflammation, formed as pus tracks through the deep fascia", ["A hot abscess with pus points", "A carbuncle", "A sebaceous cyst"])

# --------------------------------------------------------- p546
S5 = "Diagnosis of Cold Abscess and Carbuncle"
q(546, S5, "Clinical findings of tubercular cervical lymphadenopathy:", "A cold abscess in the cervical region with a fluctuant swelling", ["A hot tender abscess with pus points", "A pulsatile swelling", "A transilluminant midline swelling"])
q(546, S5, "Confirmatory test for a cold abscess:", "Antigravity aspiration followed by Ziehl-Neelsen staining", ["Aspiration from below with Gram stain", "Excision biopsy always", "Blood culture"])
q(546, S5, "Why is aspiration done in an antigravity direction:", "If aspirated from below, a sinus tract can form", ["It gives more pus", "It is less painful", "It avoids nerve injury"])
q(546, S5, "Management of tubercular cervical lymphadenopathy:", "Anti-tubercular therapy", ["Surgical excision of all nodes", "Incision and drainage", "Radiotherapy"])
q(546, S5, "A carbuncle is:", "Multiple small abscesses coalescing to form a large abscess", ["A single sterile cyst", "A cold abscess", "An encapsulated fat collection"])
q(546, S5, "Carbuncle is m/c seen in:", "Diabetics", ["Children", "Pregnant women", "Athletes"])
q(546, S5, "Characteristic surface finding of a carbuncle:", "Multiple pus points", ["A single punctum", "Pearly edges", "Transillumination"])
q(546, S5, "M/c site of a carbuncle:", "Nape of the neck", ["Scrotum", "Palm", "Sole"])
q(546, S5, "Management of a carbuncle:", "Drainage with a cruciate incision to drain all the abscesses", ["Simple aspiration", "Single linear stab incision", "Antibiotics alone always"])

S6 = "Branchial Cyst and Branchial Sinus/Fistula"
q(546, S6, "Embryological basis of the branchial cyst:", "Fusion of the 2nd arch with the 6th arch forms the cervical sinus, which persists instead of obliterating", ["Failure of the thyroglossal duct to close", "Sequestration of lymphatic tissue", "Trapped epithelium along fusion lines"])
q(546, S6, "Site of a branchial cyst:", "Neck, at the anterior border of sternocleidomastoid, at the junction between the upper and middle 1/3rd", ["Posterior border of SCM in the lower 1/3rd", "Midline of the neck", "Supraclavicular fossa"])
q(546, S6, "Clinical features of a branchial cyst:", "Fluctuant cystic swelling, transillumination positive", ["Bony hard swelling", "Pulsatile swelling", "Non-fluctuant fixed mass"])
q(546, S6, "Management of a branchial cyst:", "FNAC followed by surgical excision", ["Incision and drainage", "Sclerotherapy", "Observation"])
q(546, S6, "Branchial sinus/fistula is formed by:", "Failure of fusion of the 2nd and 6th arch", ["Persistence of the cervical sinus", "Thyroglossal duct persistence", "Trauma"])
q(546, S6, "Site of a branchial sinus/fistula:", "Anterior border of SCM, between the middle and lower 1/3rd", ["Between upper and middle 1/3rd", "Posterior triangle", "Midline"])
q(546, S6, "Management of a branchial sinus/fistula:", "Excision", ["Sclerotherapy", "Cauterisation", "Observation"])

UNIT_DEFS = [
    (S1, "A sebaceous cyst is a blocked hair follicle duct, so it can appear anywhere except palms and soles. The skin cannot be pinched over it, there is whitish discharge and the characteristic punctum; sometimes it hurts. It may become inflamed and infected, appear multiply on the scrotum and scalp, or harden into a sebaceous horn. Treat by excision of the cyst."),
    (S2, "A dermoid cyst forms from epithelial tissue trapped along lines of embryonic fusion, classically at the outer canthus of the eye and post auricular region, fluctuant, and — unlike a sebaceous cyst — the skin CAN be pinched over it. Always X-ray/CT before surgery to rule out intracranial extension, then excise. An implantation dermoid follows injury, m/c after ear piercing, and is also excised."),
    (S3, "Lipoma is an encapsulated collection of fat and the m/c swelling in the body. Skin pinches easily over it because it arises from subcutaneous tissue; it shows pseudofluctuation (expanding in one axis only) and a positive slip sign. Dercum's disease is multiple lipomatosis, benign and observed. Excise if painful or large, and watch closely lipomas of the retroperitoneum, thigh and between the shoulder blades for sarcomatous change."),
    (S4, "Tuberculosis is the m/c pathological cause of cervical lymphadenopathy in India. Bacilli infect the nodes causing caseous necrosis, periadenitis mats them together, they coalesce and adhere to the deep fascia, and pus finally tracks through the fascia as a collar stud abscess — a cold abscess without signs of inflammation."),
    (S5, "The cold abscess is a fluctuant cervical swelling confirmed by ANTIGRAVITY aspiration with Ziehl-Neelsen staining — aspirating from below risks a sinus tract — and treated with anti-tubercular therapy. A carbuncle is multiple small abscesses coalescing, m/c in diabetics, showing multiple pus points, m/c on the nape of the neck, drained through a cruciate incision."),
    (S6, "A branchial cyst arises when the cervical sinus, formed by fusion of the 2nd and 6th arches, persists; it presents at the anterior border of SCM between the upper and middle thirds, fluctuant and transilluminant, treated by FNAC then excision. A branchial sinus/fistula comes from FAILURE of fusion of the 2nd and 6th arches, lies at the anterior border of SCM between the middle and lower thirds, and is excised."),
]

first_page = {}
for x in Q:
    first_page.setdefault(x["sec"], x["page"])

UNITS = []
for i, (title, guide) in enumerate(UNIT_DEFS, 1):
    UNITS.append({
        "id": f"SURG-U70-{i}",
        "ch": 70,
        "n": i,
        "title": title,
        "sec": f"{title} · p{first_page[title]}",
        "qs": [x["id"] for x in Q if x["sec"] == title],
        "guide": guide,
    })

covered = [x for u in UNITS for x in u["qs"]]
assert covered == [x["id"] for x in Q]
with open("data/ch70.json", "w", encoding="utf-8") as f:
    json.dump({"questions": Q, "units": UNITS}, f, ensure_ascii=False, indent=1)
print(f"ch70: {len(Q)} questions, {len(UNITS)} units")
