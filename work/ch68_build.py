#!/usr/bin/env python3
"""Build data/ch68.json — Skin Tumors and Soft Tissue Sarcomas (pp529-534)."""
import json

Q = []


def q(page, sec, text, correct, wrongs, note=None):
    opts = [correct] + list(wrongs)
    assert len(opts) == 4
    Q.append({
        "id": f"SURG-C68-{len(Q)+1:03d}",
        "sec": sec,
        "page": page,
        "q": text,
        "opts": opts,
        "ans": 0,
        "exp": (note or correct) + f" (Book p{page})",
    })


# ------------------------------------------------------------- p529
S1 = "Basal Cell Carcinoma: Features and Risk Factors"
q(529, S1, "Basal cell carcinoma is also known as:", "Rodent ulcer", ["Marjolin's ulcer", "Ackerman tumor", "Bowen's disease"])
q(529, S1, "Characteristic behaviour of basal cell carcinoma:", "Locally invasive without lymph node or distant metastasis", ["Early lymph node spread", "Early haematogenous spread", "Multicentric metastasis"])
q(529, S1, "M/c site of basal cell carcinoma:", "Face, above the line joining the angle of mouth to the ear lobule", ["Below the line joining angle of mouth to ear lobule", "Scalp", "Trunk"])
q(529, S1, "Population at highest risk for basal cell carcinoma:", "White population", ["Dark skinned population", "Asian population", "All equally"])
q(529, S1, "Radiation risk factor for basal cell carcinoma:", "UV rays", ["Gamma rays only", "Microwaves", "Infrared rays"])
q(529, S1, "Chromosome involved in Gorlin syndrome:", "Chromosome 9", ["Chromosome 17", "Chromosome 5", "Chromosome 22"])

S2 = "BCC Types, Clinical Features and Management"
q(529, S2, "M/c localized type of basal cell carcinoma:", "Nodular", ["Nodulocystic", "Pigmented", "Superficial"])
q(529, S2, "Localized types of BCC include all EXCEPT:", "Multifocal", ["Nodular", "Nodulocystic", "Pigmented"])
q(529, S2, "Generalized types of basal cell carcinoma:", "Superficial and multifocal", ["Nodular and pigmented", "Morphoeic", "Nodulocystic"])
q(529, S2, "Most aggressive type of basal cell carcinoma:", "Infiltrative morphoeic type", ["Nodular", "Superficial", "Pigmented"])
q(529, S2, "Classical ulcer of basal cell carcinoma:", "Rolled out, pearly white edges", ["Everted cauliflower edges", "Undermined edges", "Punched out edges"])
q(529, S2, "Biopsy finding in basal cell carcinoma:", "Pallisading pattern", ["Keratin pearls", "Swiss cheese pattern", "Melanocytic nests"])
q(529, S2, "Standard management of basal cell carcinoma:", "Wide local excision with rhomboid/Limberg flap", ["Radiotherapy alone", "Cryotherapy alone", "Observation"])
q(529, S2, "Flap used for BCC close to the tip of the nose:", "Bilobed flap", ["Rhomboid flap", "Bipedicled flap", "Free fibular flap"])
q(529, S2, "Flap used for BCC involving the eyelid region:", "Bipedicled flap", ["Bilobed flap", "Limberg flap", "PMMC flap"])

# ------------------------------------------------------------- p530
S3 = "High Risk BCC and Moh's Micrographic Surgery"
q(530, S3, "Size defining a high risk basal cell carcinoma:", ">2 cm", [">0.5 cm", ">1 cm", ">5 cm"])
q(530, S3, "High risk features of BCC include all EXCEPT:", "First presentation of a 5 mm lesion on the trunk", ["Size >2 cm", "Sites where infiltration can lead to cranial extension", "Recurrent lesions and immunosuppression"])
q(530, S3, "Moh's micrographic surgery involves:", "Layer by layer removal of the lesion with microscopic examination", ["En bloc excision with 2 cm margin", "Radiotherapy in fractions", "Cryotherapy in cycles"])
q(530, S3, "Moh's micrographic surgery is m/c done for:", "Basal cell carcinoma", ["Malignant melanoma", "Soft tissue sarcoma", "Squamous cell carcinoma"])
q(530, S3, "Indications for Moh's micrographic surgery:", "Recurrent cases and lesions close to vital structures or nerves", ["Small primary trunk lesions", "Metastatic disease", "Benign naevi"])
q(530, S3, "Advantages of Moh's micrographic surgery:", "Less tissue removed and better cosmesis", ["Shorter operating time", "No need for anaesthesia", "No recurrence ever"])
q(530, S3, "Disadvantage of Moh's micrographic surgery:", "Time consuming", ["Poor cosmesis", "High recurrence", "Excess tissue loss"])

S4 = "Malignant Melanoma: Risk Factors and Superficial Spreading Type"
q(530, S4, "Malignant melanoma is a tumour of:", "Melanocytes", ["Keratinocytes", "Basal cells", "Fibroblasts"])
q(530, S4, "Risk factors for malignant melanoma:", "UV radiation, white population and familial atypical mole melanoma syndrome", ["Betel quid chewing", "EBV infection", "Chronic lymphedema"])
q(530, S4, "Familial atypical mole melanoma syndrome also increases the risk of:", "Pancreatic cancer", ["Gastric cancer", "Thyroid cancer", "Renal cancer"])
q(530, S4, "Sequence of growth phases in malignant melanoma:", "Horizontal phase followed by vertical invasion", ["Vertical followed by horizontal", "Only vertical", "Only horizontal"])
q(530, S4, "M/c type of malignant melanoma:", "Superficial spreading", ["Nodular", "Acral", "Lentigo maligna"])
q(530, S4, "Growth phase of superficial spreading melanoma:", "Prolonged horizontal phase", ["Rapid vertical phase", "No growth phase", "Only vertical phase"])
q(530, S4, "M/c melanoma arising in a pre-existing mole:", "Superficial spreading melanoma", ["Nodular melanoma", "Acral melanoma", "Desmoplastic melanoma"])
q(530, S4, "Risk factors for superficial spreading melanoma:", "Young individuals and sun exposure", ["Elderly patients and dark skin", "Chronic lymphedema", "Radiation in childhood"])

# ------------------------------------------------------------- p531
S5 = "Types of Malignant Melanoma"
q(531, S5, "Lentigo maligna is also known as:", "Hutchinson's melanotic freckle", ["Hutchinson's sign", "Ackerman tumor", "Bowen's disease"])
q(531, S5, "Lentigo maligna is:", "An in-situ melanoma seen in elderly patients with the best prognosis", ["An invasive melanoma in young patients", "The worst prognosis melanoma", "A melanoma of the palm"])
q(531, S5, "M/c melanoma in dark skinned individuals:", "Acral melanoma", ["Superficial spreading melanoma", "Lentigo maligna", "Desmoplastic melanoma"])
q(531, S5, "Site of acral melanoma:", "Palm and sole", ["Face", "Trunk", "Scalp"])
q(531, S5, "Growth phase and prognosis of acral melanoma:", "Rapid vertical phase with poor prognosis", ["Prolonged horizontal phase with good prognosis", "No vertical phase", "Best prognosis"])
q(531, S5, "Hutchinson's SIGN refers to:", "Pigmentation of the nail fold in subungual melanoma", ["A melanotic freckle of the face", "Pigmented palm creases", "A halo naevus"])
q(531, S5, "Melanoma with the WORST prognosis:", "Nodular melanoma", ["Lentigo maligna", "Superficial spreading melanoma", "Acral melanoma"])
q(531, S5, "Growth phase of nodular melanoma:", "Rapid vertical phase", ["Prolonged horizontal phase", "In-situ only", "Static"])
q(531, S5, "Amelanotic melanoma is:", "A variant that lacks pigment and is detected late", ["A heavily pigmented melanoma", "An in-situ melanoma with good prognosis", "A benign naevus"])
q(531, S5, "Site of desmoplastic melanoma:", "Head and neck region", ["Palm and sole", "Trunk", "Lower limb"])
q(531, S5, "Consequences of perineural invasion in desmoplastic melanoma:", "Painful lesion with locoregional recurrence", ["Painless lesion with no recurrence", "Early distant metastasis only", "Spontaneous regression"])

S6 = "ABCDE Changes and Investigations"
q(531, S6, "'A' in the ABCDE changes of melanoma:", "Asymmetry", ["Atrophy", "Anaemia", "Adhesion"])
q(531, S6, "'B' in the ABCDE changes of melanoma:", "Irregular border", ["Bleeding", "Blackness", "Blistering"])
q(531, S6, "'C' in the ABCDE changes of melanoma:", "Colour change", ["Consistency", "Crusting", "Contraction"])
q(531, S6, "Diameter in the ABCDE changes suggesting malignancy:", ">6 mm", [">2 mm", ">10 mm", ">20 mm"])
q(531, S6, "'E' in the ABCDE changes of melanoma:", "Evolution", ["Erythema", "Erosion", "Elevation only"])
q(531, S6, "IHC markers for malignant melanoma:", "S-100, Melan-A and HMB 45", ["cKit, p63, SMA", "CK7, CK20", "TTF-1, napsin"])
q(531, S6, "A brown colour on melanoma IHC indicates:", "A positive result", ["A negative result", "An inconclusive result", "Artefact"])

# ------------------------------------------------------------- p532
S7 = "Staging of Malignant Melanoma"
q(532, S7, "Staging of malignant melanoma is based on:", "Depth of invasion", ["Tumour width", "Pigment content", "Patient age"])
q(532, S7, "Clarke's classification is based on:", "The structure invaded", ["The size in mm", "Number of mitoses", "Lymph node status"])
q(532, S7, "Clarke's stage I involves:", "Epidermis", ["Papillary dermis", "Reticular dermis", "Subcutaneous tissue"])
q(532, S7, "Clarke's stage II involves:", "Papillary dermis", ["Epidermis", "Dermal papillae", "Reticular dermis"])
q(532, S7, "Clarke's stage III involves:", "Dermal papillae", ["Papillary dermis", "Reticular dermis", "Subcutaneous tissue"])
q(532, S7, "Clarke's stage IV involves:", "Reticular dermis", ["Dermal papillae", "Subcutaneous tissue", "Epidermis"])
q(532, S7, "Clarke's stage V involves:", "Subcutaneous tissue", ["Reticular dermis", "Muscle", "Bone"])
q(532, S7, "Breslow classification is based on:", "Size (thickness) of the lesion", ["Structure invaded", "Mitotic count", "Ulceration"])
q(532, S7, "Breslow stage I:", "≤0.75 mm", ["0.76-1.5 mm", "1.5-4 mm", ">4 mm"])
q(532, S7, "Breslow stage II:", "0.76-1.5 mm", ["≤0.75 mm", "1.5-4 mm", ">4 mm"])
q(532, S7, "Breslow stage III:", "1.5 mm - 4 mm", ["≤0.75 mm", "0.76-1.5 mm", ">4 mm"])
q(532, S7, "Breslow stage IV:", ">4 mm", ["1.5-4 mm", "0.76-1.5 mm", "≤0.75 mm"])
q(532, S7, "Routes of spread of malignant melanoma:", "Both lymph node and haematogenous", ["Lymph node only", "Haematogenous only", "Direct spread only"])

S8 = "Management of Malignant Melanoma"
q(532, S8, "Management of the primary tumour in localised melanoma:", "Wide local excision using NCCN margin criteria", ["Moh's surgery always", "Radiotherapy", "Cryotherapy"])
q(532, S8, "NCCN margin for a melanoma <0.5 mm thick:", "0.5 cm", ["1 cm", "2 cm", "5 cm"])
q(532, S8, "NCCN margin for a melanoma 0.5-1 mm thick:", "0.5-1 cm", ["1-2 cm", "2 cm", "0.2 cm"])
q(532, S8, "NCCN margin for a melanoma 1 mm-2 mm thick:", "1-2 cm", ["0.5 cm", "2 cm", "5 cm"])
q(532, S8, "NCCN margin for a melanoma >2 mm thick:", "2 cm", ["1 cm", "0.5 cm", "5 cm"])
q(532, S8, "Management when there is NO gross lymph node involvement:", "Sentinel lymph node biopsy", ["Lymph node clearance", "Radiotherapy", "No nodal assessment"])
q(532, S8, "Management when gross lymph node involvement is present:", "Lymph node clearance", ["Sentinel lymph node biopsy", "Observation", "Chemotherapy alone"])
q(532, S8, "Dabrafenib acts as a:", "BRAF inhibitor", ["MAPK pathway inhibitor", "Check point inhibitor", "PDL-1 inhibitor"])
q(532, S8, "Trametinib acts:", "Against the MAPK pathway", ["As a BRAF inhibitor", "As a check point inhibitor", "As an alkylating agent"])
q(532, S8, "Ipilimumab is a:", "Check point inhibitor", ["BRAF inhibitor", "MAPK inhibitor", "Topoisomerase inhibitor"])

# ------------------------------------------------------------- p533
S9 = "Melanoma Prognosis and Squamous Cell Carcinoma of Skin"
q(533, S9, "Isolated limb perfusion chemotherapy is used in:", "Locally advanced malignant melanoma", ["In-situ melanoma", "Basal cell carcinoma", "Desmoid tumor"])
q(533, S9, "Most important OVERALL prognostic factor in malignant melanoma:", "Lymph node status", ["Depth of invasion", "Tumour site", "Patient age"])
q(533, S9, "Most important prognostic factor in node negative / early malignant melanoma:", "Depth", ["Lymph node status", "Ulceration", "Pigmentation"])
q(533, S9, "Precursor lesions of cutaneous squamous cell carcinoma:", "Cutaneous horn and keratoacanthoma", ["Lentigo maligna and naevus", "Dermatofibroma and lipoma", "Seborrheic keratosis only"])
q(533, S9, "A sebaceous horn consists of:", "Solidified keratin, a complication of a sebaceous cyst", ["Calcified fat", "Fibrous tissue", "Melanin deposits"])
q(533, S9, "Marjolin's ulcer is seen in:", "Long standing varicose ulcers and burn scars", ["Acute traumatic wounds", "Diabetic foot ulcers only", "Pressure sores only"])
q(533, S9, "Edges of a Marjolin's ulcer:", "Raised, everted cauliflower edges", ["Rolled out pearly edges", "Undermined edges", "Punched out edges"])
q(533, S9, "Why are lymph nodes rarely involved in Marjolin's ulcer:", "Scarring of the lymphatics", ["Absence of tumour cells", "Slow growth only", "Immune protection"])
q(533, S9, "Investigation for Marjolin's ulcer:", "Biopsy", ["FNAC", "CT", "USG"])
q(533, S9, "Management of Marjolin's ulcer:", "Wide local excision", ["Radiotherapy alone", "Skin graft alone", "Observation"])

S10 = "Soft Tissue Sarcomas: Types and Etiology"
q(533, S10, "Usual route of spread of soft tissue sarcomas:", "Haematogenous", ["Lymphatic", "Transcoelomic", "Perineural"])
q(533, S10, "M/c soft tissue sarcoma overall and in the retroperitoneum:", "Liposarcoma", ["Rhabdomyosarcoma", "Angiosarcoma", "Synovial sarcoma"])
q(533, S10, "M/c soft tissue sarcoma in children:", "Rhabdomyosarcoma", ["Liposarcoma", "Synovial sarcoma", "Angiosarcoma"])
q(533, S10, "M/c sites of rhabdomyosarcoma in children:", "Genitourinary and head and neck region", ["Retroperitoneum and thigh", "Chest wall only", "Bone"])
q(533, S10, "Viral infection associated with a soft tissue sarcoma:", "Kaposi sarcoma", ["Liposarcoma", "Synovial sarcoma", "Desmoid tumor"])
q(533, S10, "Sarcoma arising in long standing lymphedema:", "Stewart-Treves syndrome (angio/lymphangiosarcoma)", ["Kaposi sarcoma", "Liposarcoma", "Rhabdomyosarcoma"])
q(533, S10, "Etiological factors for soft tissue sarcoma include all EXCEPT:", "Betel quid chewing", ["Radiation exposure", "Chemical exposure", "Immunosuppression"])
q(533, S10, "Syndrome associated with desmoid tumor:", "Gardner's syndrome", ["Li-Fraumeni syndrome", "Gorlin syndrome", "NF-1"])
q(533, S10, "Gorlin syndrome is associated with:", "Sarcomas plus basal cell carcinoma", ["Desmoid tumor", "Retinoblastoma", "Rhabdomyosarcoma only"])
q(533, S10, "Syndromes associated with soft tissue sarcoma include all EXCEPT:", "Plummer-Vinson syndrome", ["Retinoblastoma", "Li-Fraumeni syndrome", "NF-1"])

# ------------------------------------------------------------- p534
S11 = "Soft Tissue Sarcoma: Features, Spread and Investigations"
q(534, S11, "Typical presentation of a soft tissue sarcoma:", "A painless mass/swelling with rapid increase in size", ["A painful ulcer", "A pigmented macule", "A pulsatile mass"])
q(534, S11, "When does a soft tissue sarcoma become painful:", "With nerve infiltration", ["When small", "Always at onset", "Only after radiotherapy"])
q(534, S11, "M/c site of metastasis from a LIMB soft tissue sarcoma:", "Lungs", ["Liver", "Bone", "Brain"])
q(534, S11, "M/c site of metastasis from a RETROPERITONEAL soft tissue sarcoma:", "Liver", ["Lungs", "Bone", "Brain"])
q(534, S11, "Lymph node spread in soft tissue sarcomas is:", "Uncommon", ["The commonest route", "Universal", "Seen in all liposarcomas"])
q(534, S11, "The mnemonic MARCES denotes sarcomas that:", "Spread to lymph nodes and require LN clearance", ["Never metastasise", "Are radioresistant", "Occur only in children"])
q(534, S11, "Sarcomas spreading to lymph nodes include all EXCEPT:", "Liposarcoma", ["Malignant fibrous histiocytoma", "Angiosarcoma and rhabdomyosarcoma", "Clear cell, epithelial and synovial sarcoma"])
q(534, S11, "Investigation of choice for a soft tissue sarcoma:", "Core needle biopsy", ["FNAC", "Excision biopsy", "Incisional biopsy of the centre"])
q(534, S11, "Most important prognostic factor in soft tissue sarcoma:", "Grade, based on mitotic figures", ["Tumour size", "Patient age", "Site"])

S12 = "Management of Soft Tissue Sarcoma and Desmoid Tumor"
q(534, S12, "Surgical management of soft tissue sarcoma:", "Wide local excision / compartmental excision", ["Enucleation", "Moh's surgery", "Debulking only"])
q(534, S12, "Chemotherapy regimen for soft tissue sarcoma:", "Methotrexate plus Adriamycin", ["Cisplatin plus 5-FU", "Dabrafenib plus trametinib", "Bleomycin alone"])
q(534, S12, "Role of radiotherapy in soft tissue sarcoma:", "Markedly reduces loco-regional recurrence", ["Cures distant metastasis", "Replaces surgery", "Has no role"])
q(534, S12, "Typical site of a desmoid tumor:", "Soft tissue over the anterior abdominal wall, over a scar", ["Retroperitoneum only", "Thigh", "Head and neck"])
q(534, S12, "Syndromic association of desmoid tumor:", "Gardner's syndrome", ["Gorlin syndrome", "Li-Fraumeni syndrome", "NF-1"])
q(534, S12, "Behaviour of a desmoid tumor:", "Locally invasive but does not metastasize", ["Metastasises early to lung", "Spreads to lymph nodes", "Regresses spontaneously always"])
q(534, S12, "Management of a desmoid tumor:", "Wide local excision and tamoxifen", ["Radiotherapy alone", "Methotrexate alone", "Observation only"])

UNIT_DEFS = [
    (S1, "Basal cell carcinoma — the rodent ulcer — is locally invasive but never metastasises to nodes or distant sites, and favours the face above the line joining the angle of mouth to the ear lobule. Risks: white skin, UV rays and Gorlin syndrome on chromosome 9."),
    (S2, "BCC types: localized (nodular m/c, nodulocystic, pigmented), generalized (superficial, multifocal) and infiltrative morphoeic, the most aggressive. The ulcer has rolled out pearly white edges and biopsy shows a pallisading pattern. Treat by wide local excision with a rhomboid/Limberg flap, a bilobed flap near the nasal tip and a bipedicled flap at the eyelid."),
    (S3, "High risk BCC: >2 cm, sites where infiltration can extend intracranially, recurrent lesions and post-immunosuppression. Moh's micrographic surgery removes the lesion layer by layer with microscopic checks, is done m/c for BCC, and suits recurrent lesions or those near vital structures and nerves — less tissue removed and better cosmesis, but time consuming."),
    (S4, "Malignant melanoma arises from melanocytes, driven by UV radiation, white skin and familial atypical mole melanoma syndrome (which also raises pancreatic cancer risk). Growth is horizontal then vertical. Superficial spreading is the m/c type, with a prolonged horizontal phase, commonest melanoma in a pre-existing mole, in young sun-exposed individuals."),
    (S5, "Lentigo maligna (Hutchinson's melanotic freckle) is an in-situ melanoma of the elderly with the best prognosis. Acral melanoma is commonest in dark skin, on palm and sole, with a rapid vertical phase and poor prognosis — Hutchinson's sign marks subungual melanoma. Nodular melanoma has a rapid vertical phase and the worst prognosis; the amelanotic variant lacks pigment and is found late. Desmoplastic melanoma sits in the head and neck with perineural invasion causing pain and locoregional recurrence."),
    (S6, "Malignant transformation is flagged by ABCDE: Asymmetry, irregular Border, Colour change, Diameter >6 mm and Evolution. Biopsy plus IHC with S-100, Melan-A and HMB 45 — a brown colour signals positivity."),
    (S7, "Staging depends on depth. Clarke's uses structure: I epidermis, II papillary dermis, III dermal papillae, IV reticular dermis, V subcutaneous tissue. Breslow uses thickness: I ≤0.75 mm, II 0.76-1.5 mm, III 1.5-4 mm, IV >4 mm. Melanoma spreads both by lymph nodes and haematogenously."),
    (S8, "Localised disease: wide local excision by NCCN margins — <0.5 mm → 0.5 cm, 0.5-1 mm → 0.5-1 cm, 1-2 mm → 1-2 cm, >2 mm → 2 cm. Without gross nodes do a sentinel lymph node biopsy; with gross nodes do clearance. Metastatic disease uses dabrafenib (BRAF inhibitor), trametinib (MAPK pathway) and ipilimumab (checkpoint inhibitor)."),
    (S9, "Isolated limb perfusion chemotherapy treats locally advanced melanoma. Lymph node status is the most important prognostic factor overall, depth in node negative/early disease. Cutaneous SCC follows a cutaneous horn or keratoacanthoma; a sebaceous horn is solidified keratin complicating a sebaceous cyst. Marjolin's ulcer arises in long standing varicose ulcers and burn scars, has raised everted cauliflower edges, rarely involves nodes because lymphatics are scarred, is diagnosed by biopsy and excised widely."),
    (S10, "Soft tissue sarcomas spread haematogenously. Liposarcoma is m/c overall and in the retroperitoneum; rhabdomyosarcoma in children, in genitourinary and head and neck sites. Causes: radiation, chemicals, immunosuppression, viral infection (Kaposi sarcoma) and long standing lymphedema (Stewart-Treves angio/lymphangiosarcoma). Syndromes: retinoblastoma, Li-Fraumeni, NF-1, Gardner's (desmoid tumor) and Gorlin (sarcomas plus BCC)."),
    (S11, "A sarcoma is a painless rapidly enlarging mass that becomes painful with nerve infiltration. Haematogenous spread dominates — limb sarcomas to lungs, retroperitoneal to liver — while nodal spread is uncommon except MARCES: Malignant fibrous histiocytoma, Angiosarcoma, Rhabdomyosarcoma, Clear cell, Epithelial and Synovial sarcoma, which need LN clearance. Diagnose by core needle biopsy; grade based on mitotic figures is the most important prognostic factor."),
    (S12, "Treat sarcomas by wide local or compartmental excision, chemotherapy with methotrexate and adriamycin, and radiotherapy to cut loco-regional recurrence. Desmoid tumor is a soft tissue sarcoma of the anterior abdominal wall over a scar, linked to Gardner's syndrome, locally invasive but non-metastasising, managed by wide local excision and tamoxifen."),
]

first_page = {}
for x in Q:
    first_page.setdefault(x["sec"], x["page"])

UNITS = []
for i, (title, guide) in enumerate(UNIT_DEFS, 1):
    UNITS.append({
        "id": f"SURG-U68-{i}",
        "ch": 68,
        "n": i,
        "title": title,
        "sec": f"{title} · p{first_page[title]}",
        "qs": [x["id"] for x in Q if x["sec"] == title],
        "guide": guide,
    })

covered = [x for u in UNITS for x in u["qs"]]
assert covered == [x["id"] for x in Q]
with open("data/ch68.json", "w", encoding="utf-8") as f:
    json.dump({"questions": Q, "units": UNITS}, f, ensure_ascii=False, indent=1)
print(f"ch68: {len(Q)} questions, {len(UNITS)} units")
