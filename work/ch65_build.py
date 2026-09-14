#!/usr/bin/env python3
"""Build data/ch65.json — Lymphatic System (Marrow Surgery Ed 8, pp503-508)."""
import json

Q = []


def q(page, sec, text, correct, wrongs, note=None):
    opts = [correct] + list(wrongs)
    assert len(opts) == 4
    Q.append({
        "id": f"SURG-C65-{len(Q)+1:03d}",
        "sec": sec,
        "page": page,
        "q": text,
        "opts": opts,
        "ans": 0,
        "exp": (note or correct) + f" (Book p{page})",
    })


# ------------------------------------------------------------------ p503
S1 = "Embryology and Development of Lymphatics"
q(503, S1, "Development of the lymphatic system begins at:", "6-7 weeks of gestation", ["2-3 weeks of gestation", "10-12 weeks of gestation", "20 weeks of gestation"])
q(503, S1, "Number of cystic spaces from which lymphatics develop:", "4", ["2", "6", "8"])
q(503, S1, "Sites of the 4 cystic spaces:", "One on each side of the neck (jugular) and groin (inguinal lymph sacs)", ["Two in the thorax and two in the abdomen", "All four in the neck", "All four in the pelvis"])
q(503, S1, "Lower limb and abdominal lymphatics drain via:", "Cisterna chyli into the thoracic duct", ["Right lymphatic duct", "Jugular trunk", "Subclavian trunk directly"])
q(503, S1, "The thoracic duct opens into the:", "Left IJV at its confluence with the subclavian vein", ["Right IJV", "Right subclavian vein", "Superior vena cava directly"])
q(503, S1, "Node involved by GI/GU cancer via the thoracic duct:", "Left supraclavicular LN (Virchow's LN)", ["Right supraclavicular LN", "Axillary LN", "Inguinal LN"])
q(503, S1, "Virchow's node is the:", "Left supraclavicular lymph node", ["Right supraclavicular node", "Left axillary node", "Left inguinal node"])
q(503, S1, "Head, neck and arm lymphatics drain into the:", "Right IJV", ["Left IJV", "Cisterna chyli", "Thoracic duct"])

S2 = "Anatomy and Mechanism of Lymph Flow"
q(503, S2, "Initial lymphatics are:", "Endothelised capillaries", ["Muscular arterioles", "Fibrous cords", "Venous sinusoids"])
q(503, S2, "Initial lymphatics drain into:", "Terminal lymphatics and then lymph trunks", ["Veins directly", "Arterioles", "Lymph nodes only"])
q(503, S2, "Type of valves in terminal lymphatics:", "Bicuspid valves", ["Tricuspid valves", "Semilunar valves", "No valves"])
q(503, S2, "Segments of lymphatics partitioned by valves are called:", "Lymphangions", ["Lymphangiomas", "Lymphatic lacunae", "Lacteals"])
q(503, S2, "Property of lymphangions:", "Contractile — help movement of lymph", ["Passive and non-contractile", "Secretory", "Absorptive only"])
q(503, S2, "Mechanisms of lymph flow include all EXCEPT:", "Arterial systolic pressure pumping lymph", ["Muscular contraction pushing lymphatics", "Sequential contraction and relaxation of lymphangions", "Valves preventing reflux"])
q(503, S2, "Function of lymphatic valves:", "Prevent reflux", ["Increase capacitance", "Generate contraction", "Filter antigens"])

S3 = "Cystic Hygroma"
q(503, S3, "Cystic hygroma is composed of:", "Sequestered lymphatic tissue", ["Sequestered arterial tissue", "Fatty tissue", "Neural tissue"])
q(503, S3, "M/c site of cystic hygroma:", "Neck — posterior triangle", ["Anterior triangle of neck", "Axilla", "Inguinal region"])
q(503, S3, "Other sites of cystic hygroma:", "Axillary and inguinal regions", ["Thorax and abdomen only", "Scalp only", "Retroperitoneum only"])
q(503, S3, "Consistency of a cystic hygroma:", "Partially compressible (vascular) swelling", ["Hard and fixed", "Bony hard", "Rubbery and non-compressible"])
q(503, S3, "Cystic hygroma is fluctuant due to:", "Liquid lymph", ["Blood within", "Pus", "Air"])
q(503, S3, "Transillumination in cystic hygroma:", "Brilliantly transilluminant", ["Non-transilluminant", "Partially opaque", "Variable"])
q(503, S3, "Other brilliantly transilluminant swellings include all EXCEPT:", "Lipoma", ["Ranula (oral cavity)", "Hydrocele", "Epididymal cyst"])
q(503, S3, "On pre-natal USG, cystic hygroma is a:", "Soft marker for chromosomal abnormalities", ["Definitive sign of trisomy 21", "Normal variant", "Sign of fetal demise"])
q(503, S3, "Obstetric presentation of a large cystic hygroma:", "Obstructed labor", ["Preterm labor only", "Placenta praevia", "Oligohydramnios"])
q(503, S3, "Neonatal presentation of a large cystic hygroma:", "Respiratory distress", ["Jaundice", "Seizures", "Hypoglycaemia"])
q(503, S3, "A cystic hygroma may also present as being:", "Infected", ["Calcified", "Malignant", "Pulsatile"])

# ------------------------------------------------------------------ p504
S4 = "Cystic Hygroma: Management"
q(504, S4, "IOC for cystic hygroma:", "FNAC", ["Excision biopsy", "CT scan", "MRI"])
q(504, S4, "Definitive treatment of cystic hygroma:", "Surgery", ["Radiotherapy", "Chemotherapy", "Observation"])
q(504, S4, "Management of a LARGE cystic hygroma:", "Sclerotherapy to reduce size, then surgery", ["Immediate radical excision", "Radiotherapy first", "Aspiration alone"])
q(504, S4, "Nerve at risk during resection of a cystic hygroma:", "Spinal accessory nerve", ["Hypoglossal nerve", "Vagus nerve", "Phrenic nerve"])

S5 = "Acute Lymphangitis"
q(504, S5, "Acute lymphangitis is:", "Acute infection of lymphatics", ["Chronic fibrosis of lymphatics", "Malignancy of lymphatics", "Thrombosis of lymph nodes"])
q(504, S5, "Causative organisms of acute lymphangitis:", "Streptococcus / Staphylococcus", ["E. coli", "Wuchereria bancrofti", "Mycobacterium tuberculosis"])
q(504, S5, "Characteristic clinical sign of acute lymphangitis:", "Reddish streak", ["Blue discoloration", "Depigmented patch", "Hard nodule"])
q(504, S5, "Diagnosis of acute lymphangitis is:", "Clinical", ["Radiological", "Histological", "Serological"])
q(504, S5, "Treatment of acute lymphangitis:", "Antibiotics, limb elevation and pain control; drain if pus present", ["Amputation", "Sclerotherapy", "Radiotherapy"])
q(504, S5, "Management if pus is present in acute lymphangitis:", "Drain", ["Antibiotics alone", "Observe", "Compression only"])

S6 = "Lymphedema: Definition and Types"
q(504, S6, "Lymphedema is:", "Excessive interstitial fluid (ISF)", ["Excess intravascular fluid", "Excess intracellular fluid", "Excess pleural fluid"])
q(504, S6, "Pathology of lymphedema:", "Inability of the lymphatic system to clear the ISF compartment", ["Excess lymph production alone", "Venous obstruction alone", "Arterial insufficiency"])
q(504, S6, "Primary lymphedema is due to:", "Defective lymphatics/valves causing a clearing defect", ["Increased ISF production", "Post-surgical damage", "Infection"])
q(504, S6, "Secondary lymphedema is due to:", "↑ ISF production and damage to lymphatics", ["Defective valves from birth", "Genetic mutation only", "Arterial disease"])
q(504, S6, "Which type of lymphedema is commoner:", "Secondary", ["Primary", "Both equal", "Neither occurs"])
q(504, S6, "Secondary lymphedema follows inflammation that is:", "Secondary to post surgery and infection", ["Secondary to arterial thrombosis", "Secondary to venous reflux", "Congenital"])
q(504, S6, "Clinical features of lymphedema:", "Pain (dull or sharp), swelling of limb, and skin changes when chronic", ["Claudication and rest pain", "Fever with rigors", "Pulsatile swelling"])

# ------------------------------------------------------------------ p505
S7 = "Brunner's Classification of Lymphedema"
q(505, S7, "Brunner grade 0 is:", "Subclinical (latent)", ["Pitting edema", "Non-pitting edema", "Irreversible skin changes"])
q(505, S7, "Brunner grade 0 shows:", "Excess interstitial fluid and histological abnormalities but no clinically apparent lymphedema", ["Pitting edema on pressure", "Non-pitting edema", "Fibrosis and papillae"])
q(505, S7, "Brunner grade I is:", "Pitting edema", ["Subclinical", "Non-pitting edema", "Irreversible skin changes"])
q(505, S7, "Behaviour of Brunner grade I edema:", "Pits on pressure and largely or completely disappears on elevation and bed rest", ["Does not pit and does not reduce", "Associated with fibrosis", "Not clinically apparent"])
q(505, S7, "Brunner grade II is:", "Non-pitting edema", ["Pitting edema", "Subclinical", "Fibrosis with papillae"])
q(505, S7, "Brunner grade II edema:", "Does not pit and does not significantly reduce upon elevation; seen in long standing cases", ["Pits and disappears on elevation", "Is subclinical", "Always has papillae"])
q(505, S7, "Brunner grade III is characterised by:", "Irreversible skin changes — fibrosis and papillae", ["Pitting edema", "Non-pitting edema without skin change", "No clinical findings"])

S8 = "Complications and Chronic Skin Changes"
q(505, S8, "Complications of lymphedema:", "Infection, skin changes and cancer (Stewart-Treves syndrome)", ["Claudication and gangrene", "Deep vein thrombosis", "Aneurysm formation"])
q(505, S8, "Malignant complication of lymphedema:", "Stewart-Treves syndrome", ["Marjolin's ulcer", "Kaposi sarcoma", "Melanoma"])
q(505, S8, "Chronic skin changes of lymphedema include:", "Loss of ankle contour, squaring of toes and thickened skin over the dorsum", ["Shiny hairless skin with absent pulses", "Punched out ulcers", "Depigmented patches"])
q(505, S8, "Buffalo hump in lymphedema refers to:", "Swelling over the dorsum of the foot", ["Swelling of the neck", "Fat pad on the back", "Calf swelling"])
q(505, S8, "Thickened skin over the dorsum that cannot be pinched is:", "Stemmer sign", ["Homan's sign", "Branham sign", "Moses sign"])
q(505, S8, "Stewart-Treves syndrome develops in lymphedema that is:", "Long standing (8-10 years) and untreated", ["Acute (<1 month)", "Well treated", "Subclinical"])
q(505, S8, "Malignancy in Stewart-Treves syndrome:", "Angiosarcoma", ["Squamous cell carcinoma", "Adenocarcinoma", "Lymphoma"])
q(505, S8, "Classical setting of Stewart-Treves syndrome:", "Lymphedema post mastectomy", ["Post appendicectomy", "Post cholecystectomy", "Post thyroidectomy"])
q(505, S8, "Appearance of Stewart-Treves lesions:", "Bluish/reddish nodules", ["White plaques", "Punched out ulcers", "Depigmented macules"])

# ------------------------------------------------------------------ p506
S9 = "Stewart-Treves Syndrome and Investigations"
q(506, S9, "Presentation of Stewart-Treves syndrome:", "Bluish/reddish nodules in a lymphedematous limb", ["Painless ulcer on the sole", "Pulsatile swelling", "Cold pale limb"])
q(506, S9, "Investigation of choice for Stewart-Treves syndrome:", "Biopsy", ["FNAC", "CT scan", "Lymphangiography"])
q(506, S9, "Management of Stewart-Treves syndrome:", "Aggressive surgery (± amputation)", ["Observation", "Compression stockings", "Antibiotics"])
q(506, S9, "Gold standard for quantification of lymphedema:", "Water plethysmography", ["Limb volume measurement", "Lymphangiography", "CT scan"])
q(506, S9, "Water plethysmography measures:", "Amount of water displaced on limb immersion", ["Lymph flow rate", "Interstitial pressure", "Skin thickness"])
q(506, S9, "Water plethysmography — mild lymphedema:", "<20%", ["20-40%", ">40%", ">60%"])
q(506, S9, "Water plethysmography — moderate lymphedema:", "20-40%", ["<20%", ">40%", ">60%"])
q(506, S9, "Water plethysmography — severe lymphedema:", ">40%", ["<20%", "20-40%", "10-20%"])
q(506, S9, "Crude method of quantifying lymphedema:", "Limb volume measurement", ["Water plethysmography", "Lymphangiography", "CT"])
q(506, S9, "In lymphangiography, dye is injected into lymphatics through the:", "Web space", ["Antecubital vein", "Femoral artery", "Skin of the thigh"])
q(506, S9, "Dye used in lymphangiography:", "Indigo cyanine green (ICG)", ["Methylene blue", "Iodine contrast", "Patent blue V"])
q(506, S9, "Single axial CT finding in lymphedema:", "Reticular honeycomb pattern", ["Ground glass opacity", "Tree in bud pattern", "Target sign"])

S10 = "Primary Lymphedema"
q(506, S10, "Age of onset of lymphedema congenita:", "0-2 years", ["2-35 years", ">35 years", "At puberty"])
q(506, S10, "Sex distribution in lymphedema congenita:", "M > F", ["F > M", "Equal", "Only females"])
q(506, S10, "Extent of involvement in lymphedema congenita:", "Can involve multiple limbs, face and genitalia", ["Unilateral till the knee only", "Only one arm", "Only the face"])
q(506, S10, "Familial form of lymphedema congenita:", "Nonne-Milroy syndrome", ["Meig's disease", "Stewart-Treves syndrome", "Klippel-Trenaunay syndrome"])
q(506, S10, "M/c type of primary lymphedema:", "Lymphedema praecox", ["Lymphedema congenita", "Lymphedema tarda", "All equal"])
q(506, S10, "Age range of lymphedema praecox:", "2-35 years, peak at puberty", ["0-2 years", ">35 years", "50-70 years"])
q(506, S10, "Sex distribution in lymphedema praecox:", "F > M", ["M > F", "Equal", "Only males"])
q(506, S10, "Extent of involvement in lymphedema praecox:", "Usually unilateral till the knee", ["Multiple limbs, face and genitalia", "Bilateral above the knee", "Upper limbs only"])
q(506, S10, "Familial form of lymphedema praecox:", "Meig's disease", ["Nonne-Milroy syndrome", "Parkes-Weber syndrome", "Sturge-Weber syndrome"])
q(506, S10, "Age of onset of lymphedema tarda:", ">35 years", ["0-2 years", "2-35 years", "At puberty"])
q(506, S10, "Frequency of lymphedema tarda:", "Rare", ["M/c primary lymphedema", "Most frequent in children", "Universal after 35"])

S11 = "Secondary Lymphedema and Post Mastectomy Lymphedema"
q(506, S11, "M/c cause of UPPER limb secondary lymphedema:", "Post mastectomy lymphedema", ["Filariasis", "Trauma", "Infection"])
q(506, S11, "M/c cause of LOWER limb secondary lymphedema:", "Filariasis", ["Post mastectomy", "Trauma", "Radiotherapy"])
q(506, S11, "M/c cause of secondary lymphedema overall:", "Filariasis", ["Post mastectomy", "Surgery", "Infection"])
q(506, S11, "Incidence of post mastectomy lymphedema:", "2-10%", ["20-30%", "40-50%", "<1%"])
q(506, S11, "Procedure that DECREASES the incidence of post mastectomy lymphedema:", "Sentinel lymph node biopsy", ["Axillary lymph node clearance", "Radiotherapy to axilla", "Resection of nodes above the axillary vein"])
q(506, S11, "Factors that INCREASE post mastectomy lymphedema include all EXCEPT:", "Sentinel lymph node biopsy", ["LN removal", "Radiotherapy to axilla", "LN above axillary vein resected"])
q(506, S11, "Time of onset of post mastectomy lymphedema:", "Weeks to months after surgery", ["Immediately in the recovery room", "10 years after surgery", "Only before surgery"])

# ------------------------------------------------------------------ p507
S12 = "Elephantiasis and Lymphangioma"
q(507, S12, "Elephantiasis is secondary to filariasis due to:", "Wuchereria bancrofti", ["Brugia timori only", "Onchocerca volvulus", "Loa loa"])
q(507, S12, "Effect of filariasis on lymphatics:", "Destroys lymphatics irreversibly", ["Causes reversible dilatation", "Causes valve incompetence only", "Causes lymphatic hyperplasia"])
q(507, S12, "Microfilariae come into the peripheral blood:", "During the night", ["During the day", "Only after meals", "Only during fever"])
q(507, S12, "Treatment of filariasis:", "DEC (diethylcarbamazine)", ["Albendazole alone", "Ivermectin alone", "Praziquantel"])
q(507, S12, "Lymphangioma is a:", "Chronic skin change of lymphedema", ["Malignant tumour", "Congenital arterial malformation", "Venous malformation"])
q(507, S12, "Pathology of lymphangioma:", "Lymphatic channels thrombose and fibrose forming nodules", ["Lymphatic channels dilate without thrombosis", "Arterial channels fibrose", "Fat necrosis"])
q(507, S12, "Lymphangioma circumscriptum:", "Nodules <5 cm", ["Nodules >5 cm", "Reticular arrangement", "Diffuse plaques"])
q(507, S12, "Lymphangioma diffusum:", "Nodules >5 cm", ["Nodules <5 cm", "Reticular arrangement", "Solitary nodule"])
q(507, S12, "Lymphangioma ab igne:", "Reticular arrangement", ["Nodules <5 cm", "Nodules >5 cm", "Single plaque"])

S13 = "Conservative Management of Lymphedema"
q(507, S13, "Importance of skin care in lymphedema:", "Dry skin is more prone to infection", ["Moist skin causes ulceration", "Skin care prevents malignancy", "Skin care reduces limb volume"])
q(507, S13, "Therapy used to control swelling in lymphedema:", "Decongestive lymphedema therapy", ["Sclerotherapy", "Thrombolysis", "Anticoagulation"])
q(507, S13, "First phase of decongestive lymphedema therapy is:", "Short, intensive, supervised therapy", ["Lifelong self care", "Surgical", "Pharmacological"])
q(507, S13, "MLD stands for:", "Manual lymphatic drainage", ["Multi-layer drainage", "Mechanical lymph diversion", "Micro-lymphatic dilatation"])
q(507, S13, "Manual lymphatic drainage includes:", "Massages, pneumatic stockings and limb elevation", ["Antibiotics and analgesics", "Sclerotherapy", "Laser ablation"])
q(507, S13, "MLLB stands for:", "Multi-layer lymphedema bandaging", ["Multi-level lymph node biopsy", "Manual limb lymph bandaging", "Micro lymphatic bypass"])
q(507, S13, "Before applying MLLB, one must rule out:", "Arterial/venous disease using ABPI", ["Diabetes using HbA1c", "Infection using culture", "Malignancy using biopsy"])
q(507, S13, "Second phase of decongestive lymphedema therapy:", "Maintenance phase — self care regimen", ["Intensive supervised therapy", "Surgical resection", "Radiotherapy"])
q(507, S13, "Type of exercise recommended in lymphedema:", "Slow rhythmic isotonic movement such as swimming", ["Isometric exercises", "Heavy weight lifting", "Complete rest"])
q(507, S13, "Type of exercise to be AVOIDED in lymphedema:", "Isometric exercises", ["Swimming", "Slow rhythmic isotonic movement", "Walking"])

# ------------------------------------------------------------------ p508
S14 = "Surgical Management of Lymphedema"
q(508, S14, "Two broad categories of surgery for lymphedema:", "Reconstructive and resective", ["Ablative and endovascular", "Open and laparoscopic", "Palliative and curative"])
q(508, S14, "Reconstructive surgery for lymphedema:", "Lymphovenous anastomosis (Neubulowitz surgery)", ["Charles procedure", "Homans procedure", "Thompson's reduction"])
q(508, S14, "Lymphovenous anastomosis is performed as:", "Microsurgery", ["Open laparotomy", "Endoscopic surgery", "Percutaneous procedure"])
q(508, S14, "Resective surgery is indicated in:", "Advanced cases unresponsive to medical management", ["Early subclinical disease", "Grade 0 lymphedema", "All patients at diagnosis"])
q(508, S14, "Homans procedure involves:", "Wedge resection of skin + subcutaneous tissue", ["Removal of all tissue till fascia", "Burying a dermal flap", "Lymphovenous anastomosis"])
q(508, S14, "M/c complication of the Homans procedure:", "Skin necrosis", ["Pilonidal sinus", "Worst cosmetic outcome", "Nerve injury"])
q(508, S14, "Thompson's reduction involves:", "Raising a flap, clearing out subcutaneous tissue and burying the skin before closure", ["Wedge resection of skin", "Removing all tissue till fascia with STSG", "Microsurgical anastomosis"])
q(508, S14, "M/c complication of Thompson's reduction:", "Pilonidal sinus", ["Skin necrosis", "Worst cosmetic outcome", "Graft rejection"])
q(508, S14, "Charles procedure involves:", "Removal of all tissue till the fascia followed by split thickness skin grafting", ["Wedge resection only", "Burying a dermal flap", "Lymphovenous anastomosis"])
q(508, S14, "M/c complication of the Charles procedure:", "Worst cosmetic outcome", ["Pilonidal sinus", "Skin necrosis", "Recurrence of tumour"])
q(508, S14, "STSG in the Charles procedure stands for:", "Split thickness skin grafting", ["Subcutaneous tissue skin graft", "Skin tension suture graft", "Superficial tissue skin grafting"])
q(508, S14, "Layers illustrated in the lymphedema resection diagrams from superficial to deep:", "Skin, subcutaneous fat, deep fascia, bone", ["Bone, deep fascia, fat, skin", "Skin, muscle, bone", "Fascia, skin, fat, bone"])

UNIT_DEFS = [
    (S1, "Lymphatics sprout at 6-7 weeks from four cystic spaces — jugular sacs in each side of the neck and inguinal sacs in each groin. Lower limb and abdominal lymph climbs the cisterna chyli into the thoracic duct, which empties into the LEFT IJV at its confluence with the subclavian vein — which is exactly why GI/GU cancers seed Virchow's left supraclavicular node — while head, neck and arm lymph drains to the right IJV."),
    (S2, "Endothelised initial lymphatics feed terminal lymphatics with bicuspid valves, then lymph trunks. Valves carve the vessel into contractile lymphangions; lymph moves by muscular contraction, sequential lymphangion contraction-relaxation, and valves that forbid reflux."),
    (S3, "Cystic hygroma is sequestered lymphatic tissue, m/c in the posterior triangle of the neck (also axilla and groin). It is partially compressible, fluctuant from liquid lymph and BRILLIANTLY transilluminant — as are ranula, hydrocele and epididymal cyst. Antenatally it is a soft marker for chromosomal abnormalities; later it causes obstructed labor, respiratory distress or infection."),
    (S4, "FNAC is the IOC and surgery is the treatment; a large hygroma is first shrunk by sclerotherapy. The spinal accessory nerve is the one to protect during resection."),
    (S5, "Acute lymphangitis is streptococcal or staphylococcal infection of lymphatics, recognised clinically by pain and a reddish streak. Give antibiotics, elevate the limb, control pain, and drain if there is pus."),
    (S6, "Lymphedema is excess interstitial fluid because the lymphatics cannot clear the ISF compartment. Primary lymphedema has defective lymphatics or valves (a clearing defect); secondary — the commoner form — combines increased ISF production with damaged lymphatics after surgery or infection. Patients get dull or sharp pain, limb swelling, and skin changes when chronic."),
    (S7, "Brunner grades lymphedema: 0 subclinical/latent (excess ISF and histological change but nothing clinically apparent), I pitting edema that disappears with elevation and bed rest, II non-pitting edema that resists elevation in long standing cases, III edema with irreversible fibrosis and papillae."),
    (S8, "Lymphedema complicates with infection, skin changes and cancer. The chronic limb loses its ankle contour, squares its toes and thickens its dorsal skin so it cannot be pinched — Stemmer sign — with a buffalo hump over the foot. Eight to ten years of untreated lymphedema, classically post-mastectomy, can turn into angiosarcoma: Stewart-Treves syndrome, with bluish-reddish nodules."),
    (S9, "Stewart-Treves nodules are biopsied and treated with aggressive surgery, sometimes amputation. Quantify lymphedema with water plethysmography, the gold standard, measuring water displaced on immersion: <20% mild, 20-40% moderate, >40% severe. Limb volume measurement is the crude alternative, lymphangiography injects indigo cyanine green through the web space, and single axial CT shows a reticular honeycomb pattern."),
    (S10, "Primary lymphedema splits by age: congenita 0-2 years, M>F, may take multiple limbs, face and genitalia, familial as Nonne-Milroy syndrome; praecox 2-35 years peaking at puberty, F>M, usually unilateral till the knee, familial as Meig's disease and the m/c primary form; tarda, rare, after 35 years."),
    (S11, "Secondary lymphedema: post mastectomy in the upper limb, filariasis in the lower limb and overall. Post mastectomy lymphedema affects 2-10%, falls with sentinel lymph node biopsy and rises with node removal, axillary radiotherapy and resection of nodes above the axillary vein — appearing weeks to months after surgery."),
    (S12, "Elephantiasis follows Wuchereria bancrofti filariasis, which destroys lymphatics irreversibly; microfilariae surface in peripheral blood at night and DEC is the treatment. Lymphangioma is a chronic skin change in which lymphatic channels thrombose and fibrose into nodules: circumscriptum <5 cm, diffusum >5 cm, ab igne in a reticular arrangement."),
    (S13, "Conservative care means pain relief, skin care (dry skin invites infection) and decongestive lymphedema therapy — a short intensive supervised first phase of manual lymphatic drainage (massage, pneumatic stockings, limb elevation) and multi-layer lymphedema bandaging after ABPI excludes arterial or venous disease, then a maintenance self-care phase. Exercise should be slow rhythmic isotonic movement such as swimming; avoid isometric work."),
    (S14, "Surgery is reconstructive — microsurgical lymphovenous anastomosis (Neubulowitz) — or resective for advanced disease unresponsive to medical care. Homans wedge-resects skin and subcutaneous tissue (m/c complication skin necrosis); Thompson's reduction raises a flap, clears subcutaneous tissue and buries the skin (m/c complication pilonidal sinus); Charles removes everything down to fascia and covers with split thickness skin graft, giving the worst cosmetic outcome."),
]

first_page = {}
for x in Q:
    first_page.setdefault(x["sec"], x["page"])

UNITS = []
for i, (title, guide) in enumerate(UNIT_DEFS, 1):
    UNITS.append({
        "id": f"SURG-U65-{i}",
        "ch": 65,
        "n": i,
        "title": title,
        "sec": f"{title} · p{first_page[title]}",
        "qs": [x["id"] for x in Q if x["sec"] == title],
        "guide": guide,
    })

covered = [x for u in UNITS for x in u["qs"]]
assert covered == [x["id"] for x in Q]
assert len(set(covered)) == len(covered)
with open("data/ch65.json", "w", encoding="utf-8") as f:
    json.dump({"questions": Q, "units": UNITS}, f, ensure_ascii=False, indent=1)
print(f"ch65: {len(Q)} questions, {len(UNITS)} units")
