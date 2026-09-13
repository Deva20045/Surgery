#!/usr/bin/env python3
"""Build data/ch11.json for PULSE Surgery ch11 (Breast : Part 3, book p61-67)."""
import json

Q = []
def q(page, sec, text, opts, ans, exp):
    Q.append({"id": f"SURG-C11-{len(Q)+1:03d}", "sec": sec, "page": page,
              "q": text, "opts": opts, "ans": ans, "exp": exp})

# ---------------- p61 · TREATMENT MODALITIES & BCS VS MASTECTOMY ----------------
q(61, "Treatment Modalities & BCS vs Mastectomy", "Which of the following is NOT one of the four listed treatment modalities for breast cancer?",
  ["Immunotherapy", "Surgery", "Chemotherapy", "Radiotherapy (RT)"], 0,
  "Treatment modalities for breast cancer: 1. Surgery; 2. Chemotherapy; 3. Radiotherapy (RT); 4. Hormonal therapy (HT). Immunotherapy is not listed. (Book p61)")
q(61, "Treatment Modalities & BCS vs Mastectomy", "Surgical management of breast cancer is divided into surgery for:",
  ["Breast and lymph nodes", "Breast only", "Lymph nodes only", "Chest wall and breast"], 0,
  "Surgical mx of breast cancer: Sx for breast + Sx for lymph nodes. (Book p61)")
q(61, "Treatment Modalities & BCS vs Mastectomy", "Surgery for the breast is divided into which two operations?",
  ["BCS and mastectomy", "BCS and SLNB", "Mastectomy and axillary clearance", "Oncoplasty and TRAM"], 0,
  "Sx for breast: BCS vs mastectomy. (Book p61)")
q(61, "Treatment Modalities & BCS vs Mastectomy", "Overall survival after BCS compared with mastectomy is:",
  ["Same", "Better with BCS", "Better with mastectomy", "Depends on tumor size"], 0,
  "BCS vs mastectomy table: Overall survival = Same. (Book p61)")
q(61, "Treatment Modalities & BCS vs Mastectomy", "Local recurrence rate after BCS is:",
  ["3-4%", "1%", "10%", "15%"], 0,
  "Local recurrence: BCS = 3-4% (Hence RT is mandatory). (Book p61)")
q(61, "Treatment Modalities & BCS vs Mastectomy", "Why is radiotherapy mandatory after BCS?",
  ["Local recurrence is 3-4%", "Overall survival is worse", "To prevent lymphedema", "To sterilize the contralateral breast"], 0,
  "BCS local recurrence 3-4%, hence RT is mandatory. (Book p61)")
q(61, "Treatment Modalities & BCS vs Mastectomy", "Local recurrence rate after mastectomy is:",
  ["1%", "3-4%", "5-15%", "10%"], 0,
  "Local recurrence: mastectomy = 1%. (Book p61)")

# ---------------- p61 · ONCOPLASTY ----------------
q(61, "Oncoplasty", "Oncoplasty combines the principles of cancer surgery with:",
  ["Plastic surgery", "Vascular surgery", "Radiation oncology", "Endocrine surgery"], 0,
  "Oncoplasty: Principles of cancer Sx + Plastic Sx. (Book p61)")
q(61, "Oncoplasty", "Volume displacement oncoplasty is used for what breast volume resection?",
  ["10-15%", "<5%", "≥15%", "≥25%"], 0,
  "Volume displacement: 10-15% breast volume resection. (Book p61)")
q(61, "Oncoplasty", "Volume replacement oncoplasty is indicated when breast volume resection is:",
  ["≥15%", "10-15%", "5-10%", "<5%"], 0,
  "Volume replacement: ≥15% breast volume resection. (Book p61)")
q(61, "Oncoplasty", "BCS with round block technique and BCS with periareolar incision are examples of:",
  ["Volume displacement", "Volume replacement", "Skin sparing mastectomy", "TRAM flap"], 0,
  "BCS with round block technique / periareolar incision = Volume displacement. (Book p61)")
q(61, "Oncoplasty", "Importing tissue (e.g. a flap) to fill a defect after ≥15% breast volume resection is:",
  ["Volume replacement", "Volume displacement", "Round block technique", "Nipple sparing mastectomy"], 0,
  "≥15% resection needs volume replacement (flap shown in images). (Book p61)")

# ---------------- p62 · CONTRAINDICATIONS FOR BCS ----------------
q(62, "Contraindications for BCS", "The absolute contraindication for RT (and hence BCS) is:",
  ["Pregnancy", "Prior RT to chest wall", "SLE", "Rheumatoid arthritis"], 0,
  "Absolute C/I for RT: 1. Pregnancy. (Book p62)")
q(62, "Contraindications for BCS", "The absolute technical contraindication for BCS is:",
  ["Multicentric tumors", "Multifocal tumors", "Large tumor : breast ratio", "LABC"], 0,
  "Absolute technical C/I: 1. Multicentric tumors. (Book p62)")
q(62, "Contraindications for BCS", "Relative contraindications for RT include prior RT to chest wall and:",
  ["Collagen vascular diseases (SLE, RA)", "Pregnancy", "Multicentric tumors", "Diffuse microcalcifications"], 0,
  "Relative C/I for RT: 2. Prior RT to chest wall; 3. Collagen vascular diseases (SLE, RA). (Book p62)")
q(62, "Contraindications for BCS", "Multifocal tumors, diffuse microcalcifications/DCIS in entire breast, LABC and large tumor : breast ratio are:",
  ["Relative technical contraindications", "Absolute technical contraindications", "Absolute C/I for RT", "Not contraindications"], 0,
  "Relative technical C/1: multifocal tumors; diffuse microcalcifications/DCIS in entire breast; LABC; large tumor : breast ratio. (Book p62)")
q(62, "Contraindications for BCS", "Multicentric tumors means tumors in:",
  ["Different quadrants", "Same quadrant", "Only the UOQ", "Subareolar region"], 0,
  "Diagram: multicentric = tumors in different quadrants (absolute technical C/I). (Book p62)")
q(62, "Contraindications for BCS", "Multifocal tumors means tumors in:",
  ["Same quadrant", "Different quadrants", "Both breasts", "Only lateral half"], 0,
  "Diagram: multifocal = multiple tumors clustered in one quadrant (relative technical C/I). (Book p62)")
q(62, "Contraindications for BCS", "BCS can still be done in LABC / large tumor : breast ratio after:",
  ["Neo adjuvant chemo", "Radiotherapy", "Mastectomy", "SLNB"], 0,
  "BCS can be done post neo adjuvant chemo (LABC, large tumor : breast ratio). (Book p62)")
q(62, "Contraindications for BCS", "BCS amounts to lumpectomy with what margin?",
  ["1 mm", "1 cm", "2 cm", "5 mm"], 0,
  "BCS = Lumpectomy with 1 mm margin. (Book p62)")

# ---------------- p63 · MASTECTOMY TYPES ----------------
q(63, "Mastectomy Types", "Mastectomy means:",
  ["Removal of entire breast", "Removal of tumor with 1 mm margin", "Removal of one quadrant", "Removal of axillary nodes"], 0,
  "Mastectomy: Removal of entire breast. (Book p63)")
q(63, "Mastectomy Types", "The incision used for radical mastectomy is:",
  ["Halstead", "Elliptical Stewart", "Periareolar", "Round block"], 0,
  "Radical mastectomy incision: Halstead. (Book p63)")
q(63, "Mastectomy Types", "The incision used for modified radical mastectomy (MRM) is:",
  ["Elliptical Stewart", "Halstead", "Vertical midline", "Transverse"], 0,
  "MRM incision: Elliptical Stewart. (Book p63)")
q(63, "Mastectomy Types", "Structures removed in radical mastectomy include breast, NAC, level 1-3 axillary nodes and:",
  ["Pectoralis major & minor", "Pectoral fascia only", "Latissimus dorsi", "Serratus anterior"], 0,
  "Radical mastectomy removes: Breast; NAC; Pectoralis major & minor; Level 1,2,3 axillary lymph nodes. (Book p63)")
q(63, "Mastectomy Types", "In MRM, instead of the pectoral muscles, what is removed?",
  ["Pectoral fascia", "Pectoralis major", "Pectoralis minor", "Clavipectoral fascia and serratus"], 0,
  "MRM removes breast, NAC, pectoral fascia, level 1,2,3 axillary lymph nodes (± p. minor). (Book p63)")
q(63, "Mastectomy Types", "In MRM, when the pectoralis minor is retracted the procedure is called:",
  ["Auchincloss", "Patey", "Scanlon", "Halstead"], 0,
  "± P. minor: Retracted → Auchincloss. (Book p63)")
q(63, "Mastectomy Types", "In MRM, when the pectoralis minor is cut the procedures are:",
  ["Patey and Scanlon", "Auchincloss and Madden", "Halstead and Stewart", "Patey and Halstead"], 0,
  "± P. minor: Cut → Patey, Scanlon. (Book p63)")
q(63, "Mastectomy Types", "In simple mastectomy:",
  ["Lymph nodes are not removed", "Level 1-3 nodes are removed", "Pectoralis minor is cut", "NAC is preserved"], 0,
  "Simple mastectomy: Breast, NAC, pectoral fascia; lymph nodes NOT removed. (Book p63)")
q(63, "Mastectomy Types", "NAC removed in all mastectomies stands for:",
  ["Nipple areola complex", "Nodal axillary complex", "Nipple axillary canal", "Neuro areolar complex"], 0,
  "NAC = Nipple areola complex (removed in radical, MRM and simple mastectomy). (Book p63)")
q(63, "Mastectomy Types", "The two conservation-type mastectomies illustrated are:",
  ["Nipple sparing and skin sparing mastectomy", "Radical and simple", "Patey and Scanlon", "TRAM and DIEP"], 0,
  "Images: Nipple sparing mastectomy; Skin sparing mastectomy. (Book p63)")

# ---------------- p63 · AXILLARY CLEARANCE BOUNDARIES ----------------
q(63, "Axillary Clearance Boundaries", "The medial boundary of axillary clearance is:",
  ["Halstead ligament", "Axillary vein", "Angular vein", "Thoraco-dorsal pedicle"], 0,
  "Medial boundary: Halstead ligament. (Book p63)")
q(63, "Axillary Clearance Boundaries", "The superior boundary of axillary clearance is:",
  ["Axillary vein", "Halstead ligament", "Angular vein", "Long thoracic nerve"], 0,
  "Superior boundary: Axillary vein. (Book p63)")
q(63, "Axillary Clearance Boundaries", "The lateral boundary of axillary clearance is:",
  ["Thoraco-dorsal pedicle", "Axillary vein", "Halstead ligament", "Angular vein"], 0,
  "Lateral boundary: Thoraco-dorsal pedicle. (Book p63)")
q(63, "Axillary Clearance Boundaries", "The inferior boundary of axillary clearance is:",
  ["Angular vein", "Axillary vein", "Halstead ligament", "Thoraco-dorsal pedicle"], 0,
  "Inferior boundary: Angular vein. (Book p63)")
q(63, "Axillary Clearance Boundaries", "During axillary clearance the long thoracic nerve is:",
  ["Saved and is not a boundary", "A medial boundary", "Removed with the nodes", "The superior boundary"], 0,
  "Long thoracic nerve: Saved; Not a boundary. (Book p63)")
q(63, "Axillary Clearance Boundaries", "Minimum number of lymph nodes removed in axillary clearance:",
  ["10", "4", "6", "20"], 0,
  "Minimum 10 lymph nodes removed in axillary clearance. (Book p63)")

# ---------------- p64 · COMPLICATIONS OF MASTECTOMY ----------------
q(64, "Complications of Mastectomy", "Bleeding after mastectomy is classified as:",
  ["Primary, reactionary and secondary", "Early and late", "Arterial and venous", "Capillary only"], 0,
  "Bleeding: Primary, Reactionary, Secondary. (Book p64)")
q(64, "Complications of Mastectomy", "The most commonly (m/c) injured nerve in mastectomy/axillary clearance is:",
  ["Intercostobrachial nerve", "Long thoracic nerve", "Thoracodorsal pedicle", "Medial pectoral nerve"], 0,
  "Injury to nerves: Intercostobrachial nerve (m/c). (Book p64)")
q(64, "Complications of Mastectomy", "Intercostobrachial nerve injury causes:",
  ["Numbness & ↓ sensation in axilla", "Winging of scapula", "Latissimus dorsi wasting", "Pectoralis major paralysis"], 0,
  "Intercostobrachial nerve (m/c) → Numbness & ↓ sensation in axilla. (Book p64)")
q(64, "Complications of Mastectomy", "Winging of scapula after axillary clearance is due to injury of:",
  ["Long thoracic nerve / Nerve to Santorini / Nerve of Bell", "Intercostobrachial nerve", "Thoracodorsal pedicle", "Lateral pectoral nerve"], 0,
  "Long thoracic nerve / Nerve to Santorini / Nerve of Bell → winging of scapula. (Book p64)")
q(64, "Complications of Mastectomy", "Injury to the thoracodorsal pedicle affects:",
  ["Latissimus dorsi", "Serratus anterior", "Pectoralis major", "Teres major"], 0,
  "Thoracodorsal pedicle → Affects Latissimus dorsi. (Book p64)")
q(64, "Complications of Mastectomy", "Injury to the lateral & medial pectoral nerves affects:",
  ["P. major / minor", "Latissimus dorsi", "Serratus anterior", "Deltoid"], 0,
  "Lateral & medial pectoral nerves → affects P. major/minor. (Book p64)")
q(64, "Complications of Mastectomy", "Flap necrosis after mastectomy occurs due to:",
  ["Compromised blood supply", "Seroma", "Nerve injury", "Early drain removal"], 0,
  "Flap necrosis (d/t compromised blood supply). (Book p64)")
q(64, "Complications of Mastectomy", "The m/c complication of mastectomy is:",
  ["Seroma formation", "Winging of scapula", "Flap necrosis", "Lymphedema"], 0,
  "Seroma formation: m/c complication. (Book p64)")
q(64, "Complications of Mastectomy", "A seroma is:",
  ["Fluid accumulation beneath the flap", "Pus in the axilla", "Blood in the pleural cavity", "CSF leak"], 0,
  "Seroma: Fluid accumulation beneath the flap. (Book p64)")
q(64, "Complications of Mastectomy", "Seroma after mastectomy is prevented by:",
  ["Romovac suction drain", "Pressure dressing alone", "Prophylactic antibiotics", "Early arm exercise"], 0,
  "Prevention: Romovac suction drain. (Book p64)")
q(64, "Complications of Mastectomy", "The Romovac suction drain is removed when output is:",
  ["< 40 cc/day for a consecutive days", "< 100 cc/day once", "< 500 cc/day", "Immediately after surgery"], 0,
  "Removed when output < 40 cc/day for a consecutive days. (Book p64)")
q(64, "Complications of Mastectomy", "Treatment of seroma includes all EXCEPT:",
  ["Do not put the drain again", "Aspirate under aseptic conditions", "Pressure dressing", "Re-insert the Romovac drain"], 0,
  "Rx of seroma: Aspirate under aseptic conditions; Pressure dressing; Do not put the drain again. (Book p64)")

# ---------------- p64-65 · LYMPHEDEMA ----------------
q(64, "Lymphedema & Stewart-Treves", "Post mastectomy/axillary clearance lymphedema is the:",
  ["m/c cause of upper limb lymphedema", "rarest cause of limb swelling", "m/c cause of lower limb lymphedema", "cause of breast swelling"], 0,
  "m/c cause of upper limb lymphedema. (Book p64)")
q(64, "Lymphedema & Stewart-Treves", "Post mastectomy lymphedema typically develops:",
  ["Few weeks-months after Sx", "On the operating table", "After 10 years only", "Only after RT"], 0,
  "Develops few weeks-months after Sx. (Book p64)")
q(64, "Lymphedema & Stewart-Treves", "Incidence of lymphedema after lymph node clearance is:",
  ["5-15%", "50%", "1%", "80%"], 0,
  "Lymph node clearance (5-15%). (Book p64)")
q(64, "Lymphedema & Stewart-Treves", "Factors which ↑ incidence of lymphedema include removal of lymph nodes above the:",
  ["Axillary vein", "Angular vein", "Cephalic vein", "Basilic vein"], 0,
  "↑ incidence: Removal of lymph nodes above axillary vein; RT to axilla after lymph node clearance. (Book p64)")
q(64, "Lymphedema & Stewart-Treves", "Which factor ↓ the incidence of lymphedema?",
  ["Sentinel lymph node biopsy", "Axillary clearance", "RT to axilla", "Removal of nodes above axillary vein"], 0,
  "Factors which ↓ incidence: Sentinel lymph node biopsy. (Book p64)")
q(65, "Lymphedema & Stewart-Treves", "Management of lymphedema includes:",
  ["Skin care, lymphedema massages, stockings, exercise", "Immediate amputation", "Routine re-operation", "High dose diuretics only"], 0,
  "Mx: Skin care; Lymphedema massages; Stockings; Exercise. (Book p65)")
q(65, "Lymphedema & Stewart-Treves", "Long standing lymphedema for 8-10 years can lead to:",
  ["2° cancer / Angiosarcoma (Stewart-Treves syndrome)", "Fibroadenoma", "Duct ectasia", "Fat necrosis"], 0,
  "Long standing lymphedema for 8-10 years → 2° cancer/Angiosarcoma → Stewart-Treves syndrome. (Book p65)")
q(65, "Lymphedema & Stewart-Treves", "Stewart-Treves syndrome presents with:",
  ["Reddish/bluish skin nodules", "Painless jaundice", "White patches on arm", "Bony swellings"], 0,
  "Reddish/bluish skin nodules in long standing lymphedema = Stewart-Treves syndrome. (Book p65)")

# ---------------- p65 · LOCAL RECURRENCE, PHANTOM BREAST & RECONSTRUCTION ----------------
q(65, "Local Recurrence, Phantom Breast & Reconstruction", "First step in investigating a local recurrence is:",
  ["Repeat biopsy to confirm diagnosis", "Start chemotherapy", "Mastectomy", "PET-CT"], 0,
  "Ix: Repeat biopsy to confirm diagnosis. (Book p65)")
q(65, "Local Recurrence, Phantom Breast & Reconstruction", "On repeat biopsy of a local recurrence, IHC markers can show change in expression in:",
  ["10-15%", "50%", "1%", "90%"], 0,
  "IHC markers (10-15% can show change in IHC expression). (Book p65)")
q(65, "Local Recurrence, Phantom Breast & Reconstruction", "Extensive local recurrences covering the chest wall like armour are called:",
  ["Cancer en cuirasse", "Cancer en plaque", "Peau d'orange", "Mastitis carcinomatosa"], 0,
  "Extensive local recurrences → Covers chest wall like armour: Cancer en cuirasse. (Book p65)")
q(65, "Local Recurrence, Phantom Breast & Reconstruction", "In phantom breast syndrome the patient:",
  ["Feels as if breast is still present", "Develops fever", "Loses sensation over the scar", "Gets bilateral gynaecomastia"], 0,
  "Phantom breast syndrome: Patient feels as if breast is still present. (Book p65)")
q(65, "Local Recurrence, Phantom Breast & Reconstruction", "Phantom breast syndrome occurs due to:",
  ["ICBN entrapment", "Seroma", "Hypertrophic scar", "Rib metastasis"], 0,
  "D/t ICBN entrapment; Pain (+). (Book p65)")
q(65, "Local Recurrence, Phantom Breast & Reconstruction", "Reconstructive surgery after mastectomy uses which flaps?",
  ["TRAM & DIEP (Latissimus dorsi also)", "Groin flap only", "Deltopectoral flap only", "Free fibula flap"], 0,
  "Reconstructive Sx: TRAM & DIEP; Latissimus dorsi flap can also be used. (Book p65)")
q(65, "Local Recurrence, Phantom Breast & Reconstruction", "TRAM flap stands for:",
  ["Transverse rectus abdominus myocutaneous flap", "Transverse rectus artery muscle flap", "Total rectus abdominis muscle flap", "Thoracic rectus anterior myocutaneous flap"], 0,
  "TRAM = Transverse rectus abdominus myocutaneous flap. (Book p65)")
q(65, "Local Recurrence, Phantom Breast & Reconstruction", "In TRAM flap which tissues are removed?",
  ["Skin, fat, muscle", "Skin & fat only", "Fat only", "Muscle only"], 0,
  "TRAM: Elliptical incision; Skin, fat, muscle removed. (Book p65)")
q(65, "Local Recurrence, Phantom Breast & Reconstruction", "TRAM flap carries ↑ risk of incisional hernia because:",
  ["Muscle is removed", "Skin is removed", "Fat is removed", "It uses a prosthesis"], 0,
  "↑ Risk of incisional hernia (d/t removal of muscle). (Book p65)")
q(65, "Local Recurrence, Phantom Breast & Reconstruction", "DIEP flap stands for:",
  ["Deep inferior epigastric artery perforator flap", "Deep iliac epigastric perforator flap", "Direct inferior epigastric pedicle flap", "Deep internal epigastric artery flap"], 0,
  "DIEP = Deep inferior epigastric artery perforator flap. (Book p65)")
q(65, "Local Recurrence, Phantom Breast & Reconstruction", "DIEP is the best flap because:",
  ["Less abdominal complications (muscle not removed)", "It removes muscle", "No incision is needed", "It uses the latissimus dorsi"], 0,
  "DIEP: Skin & fat removed; Best flap: Less abdominal complications (as muscle is not removed). (Book p65)")

# ---------------- p66 · SURGICAL MX OF LYMPH NODES & SLNB ----------------
q(66, "Lymph Node Mx & SLNB Basics", "In the surgical management flowchart, a patient with an enlarged lymph node first undergoes:",
  ["Biopsy LN for cancer", "Direct axillary clearance", "SLNB", "Radiotherapy"], 0,
  "Patient with enlarged lymph node → Biopsy LN for cancer. (Book p66)")
q(66, "Lymph Node Mx & SLNB Basics", "If the LN biopsy for cancer is positive (+ve), the next step is:",
  ["Axillary clearance", "SLNB", "Observation", "Hormonal therapy"], 0,
  "+ve → Axillary clearance. (Book p66)")
q(66, "Lymph Node Mx & SLNB Basics", "If the LN biopsy for cancer is negative (−ve), the next step is:",
  ["SLNB", "Axillary clearance", "Mastectomy", "RT"], 0,
  "−ve → SLNB. (Book p66)")
q(66, "Lymph Node Mx & SLNB Basics", "The concept of sentinel lymph node was described by:",
  ["Cabana in penile cancer", "Halstead in breast cancer", "Patey in penile cancer", "Stewart in melanoma"], 0,
  "Concept described by: Cabana in penile cancer. (Book p66)")
q(66, "Lymph Node Mx & SLNB Basics", "The sentinel LN is:",
  ["First draining lymph node from cancer", "Largest axillary node", "Any level III node", "The internal mammary node"], 0,
  "Sentinel LN: First draining lymph node from cancer. (Book p66)")
q(66, "Lymph Node Mx & SLNB Basics", "The sentinel lymph node is most commonly present in:",
  ["Level I of axilla", "Level III of axilla", "Supraclavicular fossa", "Internal mammary chain"], 0,
  "Most commonly present in level I of axilla. (Book p66)")
q(66, "Lymph Node Mx & SLNB Basics", "The m/c nerve injured during SLNB is:",
  ["ICBN", "Long thoracic nerve", "Thoracodorsal nerve", "Vagus nerve"], 0,
  "m/c nerve injured: ICBN. (Book p66)")
q(66, "Lymph Node Mx & SLNB Basics", "SLNB is used in all the following cancers EXCEPT:",
  ["Glioblastoma", "Malignant melanoma", "Penile cancer", "Vulvar carcinoma"], 0,
  "Cancers where SLNB is used: Malignant melanoma; Breast cancer; Penile cancer; Vulvar carcinoma; Head & neck cancer. (Book p66)")

# ---------------- p66 · BLUE DYE TECHNIQUE ----------------
q(66, "Blue Dye Technique", "In the blue dye technique, the dye is injected where and in what volume?",
  ["1-1.5 cc methylene blue/isosulfan blue, subcutaneous periareolar", "10 cc methylene blue intravenous", "5 cc isosulfan blue intramuscular", "1-1.5 cc indigo carmine subdermal over the tumor"], 0,
  "1-1.5 cc methylene blue/isosulfan blue injected in subcutaneous plane in periareolar region. (Book p66)")
q(66, "Blue Dye Technique", "After localising the blue lymph nodes, the next step is:",
  ["Frozen section in normal container", "Direct mastectomy", "Core biopsy of breast", "Gamma camera scan"], 0,
  "Localise blue lymph nodes → Frozen section in normal container. (Book p66)")
q(66, "Blue Dye Technique", "If frozen section of the sentinel node is cancer −ve:",
  ["Axillary clearance not needed (hence ↓ incidence of lymphedema)", "Axillary clearance is mandatory", "RT to axilla is mandatory", "Repeat SLNB"], 0,
  "Cancer −ve → Axillary clearance not needed (Hence ↓ incidence of lymphedema). (Book p66)")
q(66, "Blue Dye Technique", "If frozen section of the sentinel node is cancer +ve, the management is:",
  ["Axillary clearance", "Observation", "Pressure dressing", "Repeat frozen section"], 0,
  "Cancer +ve → Mx: Axillary clearance. (Book p66)")
q(66, "Blue Dye Technique", "The m/c complication of the blue dye technique is:",
  ["Skin tattooing", "Anaphylaxis", "Skin necrosis", "Bluish discolouration of urine"], 0,
  "Complications: Skin tattooing (m/c). (Book p66)")
q(66, "Blue Dye Technique", "Which of the following is a listed complication of the blue dye technique?",
  ["Anaphylaxis", "Winging of scapula", "Seroma", "Phantom breast"], 0,
  "Complications: Skin tattooing (m/c), Anaphylaxis, Bluish discolouration of urine, Skin necrosis. (Book p66)")
q(66, "Blue Dye Technique", "A harmless listed complication of methylene/isosulfan blue seen in the urine is:",
  ["Bluish discolouration of urine", "Hematuria", "Proteinuria", "Chyluria"], 0,
  "Bluish discolouration of urine is a listed complication. (Book p66)")

# ---------------- p67 · RADIONUCLEOTIDE, ICG & SENTIMAG ----------------
q(67, "Radionucleotide, ICG & Sentimag", "In the radionucleotide technique, what is injected in the periareolar region?",
  ["Tc99 tagged sulphur colloid", "Methylene blue", "Ferric oxide", "Indocyanine green"], 0,
  "Tc99 tagged sulphur colloid injected in periareolar region. (Book p67)")
q(67, "Radionucleotide, ICG & Sentimag", "Hot nodes (radioactive) in the radionucleotide technique are identified on:",
  ["Gamma camera", "MRI", "PET-CT", "USG"], 0,
  "Hot nodes (Radioactive) identified on gamma camera. (Book p67)")
q(67, "Radionucleotide, ICG & Sentimag", "The best technique for SLNB is:",
  ["Combination of blue dye + radionucleotide", "Blue dye alone", "Palpation alone", "ICG alone"], 0,
  "Best technique: Combination of blue dye + radionucleotide. (Book p67)")
q(67, "Radionucleotide, ICG & Sentimag", "In the indocyanine green (ICG) technique, what is injected?",
  ["ICG + blue dye", "ICG + ferric oxide", "Tc99 + blue dye", "Methylene blue + ferric oxide"], 0,
  "ICG + Blue dye injected → Green lymph nodes under filter. (Book p67)")
q(67, "Radionucleotide, ICG & Sentimag", "The advantage of the ICG technique is:",
  ["No radiation exposure", "Zero cost", "No injection needed", "Nodes seen with naked eye without filter"], 0,
  "Advantages: No radiation exposure. (Book p67)")
q(67, "Radionucleotide, ICG & Sentimag", "The Sentimag technique uses which compound?",
  ["Ferric oxide compound", "Tc99 colloid", "Isosulfan blue", "Gadolinium"], 0,
  "Sentimag technique: Ferric oxide compound used. (Book p67)")
q(67, "Radionucleotide, ICG & Sentimag", "In the Sentimag technique the lymph node is detected on:",
  ["Magnetic scanner", "Gamma camera", "X-ray", "Thermal camera"], 0,
  "LN detected on magnetic scanner. (Book p67)")
q(67, "Radionucleotide, ICG & Sentimag", "The advantage of the Sentimag technique is:",
  ["Zero radiation exposure", "No equipment needed", "It stains nodes blue", "It is painful"], 0,
  "Advantages: Zero radiation exposure. (Book p67)")

# ---------------- UNITS ----------------
def sec_ids(*labels):
    ids = [x["id"] for x in Q if x["sec"] in labels]
    assert ids, labels
    return ids

def first_page(label):
    for x in Q:
        if x["sec"] == label:
            return x["page"]

UNIT_DEFS = [
    ("Treatment Modalities & BCS vs Mastectomy", ("Treatment Modalities & BCS vs Mastectomy",),
     "Four weapons against breast cancer: surgery, chemotherapy, RT and HT. Surgery tackles breast and lymph nodes; for the breast, BCS and mastectomy give the SAME overall survival, but BCS recurs locally 3-4% (hence RT mandatory) versus 1% after mastectomy."),
    ("Oncoplasty: Volume Displacement & Replacement", ("Oncoplasty",),
     "Oncoplasty fuses cancer surgery with plastic surgery: 10-15% breast volume resections are closed by volume displacement (round block, periareolar incisions), while ≥15% resections need volume replacement with imported tissue."),
    ("Contraindications for BCS", ("Contraindications for BCS",),
     "Absolute bars: pregnancy (RT) and multicentric tumors (technical, different quadrants). Relative: prior chest wall RT and collagen vascular disease (SLE, RA) for RT; multifocal (same quadrant) tumors, diffuse microcalcifications/DCIS, LABC and large tumor:breast ratio technically - the last two become BCS-eligible after neo adjuvant chemo. BCS = lumpectomy with a 1 mm margin."),
    ("Mastectomy Types", ("Mastectomy Types",),
     "Radical (Halstead) takes breast, NAC, pectoralis major & minor and level 1-3 nodes; MRM (elliptical Stewart) spares the muscles taking pectoral fascia, ± pectoralis minor retracted (Auchincloss) or cut (Patey, Scanlon); simple mastectomy removes no nodes. Nipple and skin sparing versions conserve the envelope."),
    ("Boundaries of Axillary Clearance", ("Axillary Clearance Boundaries",),
     "Halstead ligament medially, axillary vein above, thoraco-dorsal pedicle laterally and angular vein below; the long thoracic nerve is saved, not a boundary, and at least 10 nodes must come out."),
    ("Complications: Nerves, Seroma & Flap", ("Complications of Mastectomy",),
     "Bleeding runs primary, reactionary, secondary. The intercostobrachial nerve (m/c) loses axillary sensation; long thoracic (Santorini/Bell) wings the scapula; thoracodorsal hits latissimus dorsi; pectoral nerves hit p. major/minor. Seroma, the m/c complication, is prevented by a Romovac drain pulled at <40 cc/day and treated by aseptic aspiration + pressure dressing, never re-inserting the drain."),
    ("Lymphedema & Stewart-Treves", ("Lymphedema & Stewart-Treves",),
     "Post-mastectomy lymphedema is the m/c cause of upper limb lymphedema, appearing weeks-months later in 5-15% after clearance - worse if nodes above the axillary vein go or axillary RT follows, less with SLNB. Manage with skin care, massage, stockings, exercise; 8-10 years of swelling can breed angiosarcoma (reddish/bluish nodules) = Stewart-Treves syndrome."),
    ("Local Recurrence, Phantom Breast & Reconstruction", ("Local Recurrence, Phantom Breast & Reconstruction",),
     "Recurrences need repeat biopsy (10-15% change IHC expression) and armour-like spread is cancer en cuirasse; ICBN entrapment causes painful phantom breast. Reconstruction: TRAM takes skin-fat-muscle (incisional hernia risk) while DIEP, the best flap, takes skin-fat only; latissimus dorsi also serves."),
    ("Surgical Mx of Lymph Nodes & SLNB Basics", ("Lymph Node Mx & SLNB Basics",),
     "Enlarged nodes get biopsy: positive → axillary clearance, negative → SLNB. Cabana described the sentinel node in penile cancer; it is the first draining node, usually level I, and SLNB (m/c nerve injured ICBN) serves melanoma, breast, penile, vulvar and head & neck cancers."),
    ("Blue Dye Technique", ("Blue Dye Technique",),
     "1-1.5 cc methylene/isosulfan blue injected subcutaneously periareolarly stains the sentinel node for frozen section: negative spares axillary clearance (less lymphedema), positive mandates it. Watch for skin tattooing (m/c), anaphylaxis, bluish urine and skin necrosis."),
    ("Radionucleotide, ICG & Sentimag Techniques", ("Radionucleotide, ICG & Sentimag",),
     "Tc99 sulphur colloid marks hot nodes on gamma camera and combined blue dye + radionucleotide is the best technique; ICG + blue dye shows green nodes under a filter with no radiation, and Sentimag's ferric oxide is read by a magnetic scanner with zero radiation."),
]

UNITS = []
for i, (title, labels, guide) in enumerate(UNIT_DEFS, 1):
    UNITS.append({"id": f"SURG-U11-{i}", "ch": 11, "n": i, "title": title,
                  "sec": f"{labels[0]} · p{first_page(labels[0])}",
                  "qs": sec_ids(*labels), "guide": guide})

covered = [i for u in UNITS for i in u["qs"]]
assert covered == [x["id"] for x in Q], "units must cover questions in order"

data = {"questions": Q, "units": UNITS}
with open("data/ch11.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
print(f"ch11: {len(Q)} questions, {len(UNITS)} units")
