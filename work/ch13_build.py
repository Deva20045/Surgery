#!/usr/bin/env python3
"""Build data/ch13.json for PULSE Surgery ch13 (Breast : Part 5, book p75-81)."""
import json

Q = []
def q(page, sec, text, opts, ans, exp):
    Q.append({"id": f"SURG-C13-{len(Q)+1:03d}", "sec": sec, "page": page,
              "q": text, "opts": opts, "ans": ans, "exp": exp})

# ---------------- p75 · BREAST ABSCESS: LACTATIONAL ----------------
q(75, "Breast Abscess: Lactational", "Which is more common?",
  ["Lactational breast abscess > Non lactational", "Non lactational > Lactational", "Both equal", "Lactational only in males"], 0,
  "Breast abscess: Lactational > Non lactational. (Book p75)")
q(75, "Breast Abscess: Lactational", "The most common organism in lactational breast abscess is:",
  ["S. aureus", "E. coli", "Streptococcus pyogenes", "Pseudomonas"], 0,
  "Organism: S. aureus (m/c). (Book p75)")
q(75, "Breast Abscess: Lactational", "The source of infection in lactational breast abscess is:",
  ["Oropharynx of the child", "Skin of the mother", "Blood stream", "Lymphatics"], 0,
  "Source: Oropharynx of the child. (Book p75)")
q(75, "Breast Abscess: Lactational", "The entry point of organisms in lactational breast abscess is:",
  ["Cracked nipple", "Blocked duct", "Sebaceous cyst", "Axillary tail"], 0,
  "Entry point: Cracked nipple. (Book p75)")
q(75, "Breast Abscess: Lactational", "Symptoms of breast abscess include:",
  ["Pain, swelling and fever", "Painless lump", "Nipple retraction only", "Skin dimpling only"], 0,
  "Symptoms: Pain, Swelling, Fever. (Book p75)")
q(75, "Breast Abscess: Lactational", "The LATE sign of breast abscess is:",
  ["Fluctuation", "Redness", "Warmth", "Tenderness"], 0,
  "Signs: Signs of inflammation (+); Fluctuation (Late sign). (Book p75)")
q(75, "Breast Abscess: Lactational", "Fluctuation is a late sign in which group of abscesses?",
  ["Breast, parotid, ischiorectal, palmar & plantar", "Dental, peritonsillar, submandibular", "Liver, splenic, renal", "Psoas and iliac"], 0,
  "Fluctuation is a late sign in: Breast, parotid, ischiorectal abscess, palmar & plantar abscess. (Book p75)")
q(75, "Breast Abscess: Lactational", "Investigation of choice for breast abscess is:",
  ["USG", "Mammogram", "FNAC", "CT"], 0,
  "Ix: USG (IOC). (Book p75)")
q(75, "Breast Abscess: Lactational", "Antibiotics used for lactational breast abscess are:",
  ["Amoxicillin + Clavulanic acid or Cloxacillin", "Vancomycin only", "Metronidazole only", "Linezolid only"], 0,
  "Rx: Antibiotics: Amoxicillin + Clavulanic acid or Cloxacillin. (Book p75)")
q(75, "Breast Abscess: Lactational", "Regarding breast milk during lactational abscess treatment:",
  ["Breast milk to be expressed", "Breast feeding must stop forever", "Milk must be suppressed with drugs", "Only contralateral feeding allowed"], 0,
  "Rx: Breast milk to be expressed. (Book p75)")
q(75, "Breast Abscess: Lactational", "If pus is present, after 2 failed attempts of USG guided aspiration with a still recurrent abscess, the next step is:",
  ["Incision & drainage with blade no. 11", "Continue aspiration for 10 more attempts", "Mastectomy", "Antibiotics alone"], 0,
  "If pus + → 2 attempts of USG guided aspiration; if abscess still recurrent → Incision & drainage (Blade no. 11). (Book p75)")

# ---------------- p75 · RECURRENT NON-LACTATIONAL ABSCESSES ----------------
q(75, "Recurrent Non-lactational Abscesses", "A recurrent non-lactational abscess with caseating granulomas, AFB +ve and GeneXpert +ve is treated with:",
  ["ATT", "Steroids", "Mastectomy", "Antibiotics alone"], 0,
  "Tuberculosis: HPE caseating granulomas, AFB +ve, Gene expert +ve → Rx ATT. (Book p75)")
q(75, "Recurrent Non-lactational Abscesses", "Idiopathic granulomatous mastitis shows on HPE:",
  ["Non caseating granulomas", "Caseating granulomas", "Carcinoma", "Normal tissue"], 0,
  "Idiopathic granulomatous mastitis: Non caseating granulomas; AFB -ve; Gene expert -ve. (Book p75)")
q(75, "Recurrent Non-lactational Abscesses", "Idiopathic granulomatous mastitis is a diagnosis of exclusion treated with:",
  ["Steroids", "ATT", "Antibiotics", "Surgery always"], 0,
  "Rx: Diagnosis of exclusion; Rx: Steroids. (Book p75)")
q(75, "Recurrent Non-lactational Abscesses", "In the recurrent non-lactational abscess table, inflammatory cancer shows on HPE:",
  ["Carcinoma", "Caseating granulomas", "Non caseating granulomas", "Fat necrosis"], 0,
  "Inflammatory cancer: HPE carcinoma → Rx of cancer. (Book p75)")
q(75, "Recurrent Non-lactational Abscesses", "AFB stain and GeneXpert are negative in:",
  ["Idiopathic granulomatous mastitis", "Tuberculous abscess", "Both TB and cancer", "Neither"], 0,
  "Idiopathic granulomatous mastitis: AFB -ve, Gene expert for TB -ve (TB is +ve for both). (Book p75)")

# ---------------- p76 · ANDI & FIBROADENOMA ----------------
q(76, "ANDI & Fibroadenoma", "ANDI stands for:",
  ["Aberrations of Normal Development & Involution", "Abnormal Nodular Disease of Involution", "Aberrations of Neoplastic Development & Involution", "Atypical Normal Duct Involution"], 0,
  "ANDI: Aberrations of Normal Development & Involution. (Book p76)")
q(76, "ANDI & Fibroadenoma", "The most common benign breast condition in age 15-25 is:",
  ["Fibroadenoma", "Fibrocystic disease", "Duct ectasia", "Papilloma"], 0,
  "Age 15-25: Fibroadenoma. (Book p76)")
q(76, "ANDI & Fibroadenoma", "In age 25-40, the most common benign condition is:",
  ["Fibrocystic disease/Fibroadenosis", "Fibroadenoma", "Duct ectasia", "Phyllodes"], 0,
  "Age 25-40: Fibrocystic disease/Fibroadenosis. (Book p76)")
q(76, "ANDI & Fibroadenoma", "Above 40 years, the common benign conditions are:",
  ["Fibrocystic disease > Duct ectasia", "Fibroadenoma > cyst", "Papilloma > ectasia", "Phyllodes > fibroadenoma"], 0,
  ">40: Fibrocystic disease > Duct ectasia. (Book p76)")
q(76, "ANDI & Fibroadenoma", "The most common cause of breast lump is:",
  ["Fibroadenoma", "Fibrocystic disease", "Cancer", "Abscess"], 0,
  "Fibroadenoma: m/c cause of breast lump. (Book p76)")
q(76, "ANDI & Fibroadenoma", "Fibroadenoma typically occurs at age:",
  ["15-25", "35-45", "45-55", ">60"], 0,
  "Age: 15-25. (Book p76)")
q(76, "ANDI & Fibroadenoma", "Clinical features of fibroadenoma are:",
  ["Firm, painless, lobulated, mobile", "Hard, fixed, painful", "Soft, tender, fluctuant", "Cystic and transilluminant"], 0,
  "Clinical features: Firm, Painless, Lobulated, Mobile (Breast mouse). (Book p76)")
q(76, "ANDI & Fibroadenoma", "The 'Breast mouse' refers to:",
  ["Fibroadenoma (mobile)", "Phyllodes", "Lipoma", "DCIS"], 0,
  "Mobile (Breast mouse) = fibroadenoma. (Book p76)")
q(76, "ANDI & Fibroadenoma", "On mammogram, fibroadenoma shows:",
  ["Popcorn calcification", "Clustered microcalcifications", "Spiculated mass", "Architectural distortion"], 0,
  "Mammogram showing popcorn calcification in fibroadenoma. (Book p76)")
q(76, "ANDI & Fibroadenoma", "USG (IOC) features of fibroadenoma are:",
  ["Smooth well defined, wider than taller, no increase in vascularity", "Irregular, taller than wide, vascular", "Cystic with debris", "Shadowing lesion"], 0,
  "USG Breast (IOC): Smooth, well defined tumor; Wider than taller; No ↑ in vascularity. (Book p76)")
q(76, "ANDI & Fibroadenoma", "The usual BIRADS score of fibroadenoma is:",
  ["BIRADS II", "BIRADS I", "BIRADS IVb", "BIRADS V"], 0,
  "Staging: BIRADS II (m/c). (Book p76)")
q(76, "ANDI & Fibroadenoma", "Complex/Atypical fibroadenoma is graded:",
  ["BIRADS III/IVa", "BIRADS I", "BIRADS II", "BIRADS V"], 0,
  "Complex/Atypical fibroadenoma: BIRADS III/IVa. (Book p76)")
q(76, "ANDI & Fibroadenoma", "BIRADS IVa fibroadenoma requires:",
  ["Biopsy", "Observation", "MRI only", "Mastectomy"], 0,
  "BIRADS IVa → Biopsy required. (Book p76)")

# ---------------- p76 · FIBROADENOMA: RX ----------------
q(76, "Fibroadenoma: Staging & Rx", "Which is NOT an indication for surgery in fibroadenoma?",
  ["Stable 1 cm lesion with no symptoms or anxiety", "Increase in size/rapid increase", "Family H/o breast cancer", "Giant fibroadenoma (>4-5 cm)"], 0,
  "Indications for Sx: ↑ size/rapid ↑ size; Family H/o Breast cancer; Painful fibroadenoma; Giant (>4-5 cm); If patient desires. (Book p76)")
q(76, "Fibroadenoma: Staging & Rx", "A giant fibroadenoma is defined as size greater than:",
  ["4-5 cm", "1 cm", "2 cm", "10 cm"], 0,
  "Giant Fibroadenoma (>4-5 cm). (Book p76)")
q(76, "Fibroadenoma: Staging & Rx", "In open excision of fibroadenoma, the incision is:",
  ["Periareolar", "Radial only", "Transverse axillary", "Circumareolar skin excision"], 0,
  "Older methods: Open Sx - Incision: Periareolar. (Book p76)")
q(76, "Fibroadenoma: Staging & Rx", "Closure after open fibroadenoma excision is with:",
  ["Subcuticular sutures with 3-0 monocryl", "Interrupted prolene 1-0", "Staplers", "Secondary intention"], 0,
  "Closure: Subcuticular sutures with 3-0 monocryl. (Book p76)")
q(76, "Fibroadenoma: Staging & Rx", "The latest methods of fibroadenoma removal are:",
  ["Vacuum assisted/scarless breast Sx", "Halstead radical Sx", "Simple mastectomy", "RT ablation"], 0,
  "Latest methods: Vacuum assisted/scarless breast Sx. (Book p76)")

# ---------------- p77 · PHYLLODES TUMOR ----------------
q(77, "Phyllodes Tumor", "Phyllodes tumor is also known as:",
  ["Cystosarcoma phyllodes", "Cystosarcoma mammae", "Sarcoma botryoides", "Adenosarcoma"], 0,
  "AKA Cystosarcoma phyllodes. (Book p77)")
q(77, "Phyllodes Tumor", "Phyllodes tumor is a:",
  ["Stromal tumor", "Epithelial tumor", "Lymphoid tumor", "Vascular tumor"], 0,
  "Stromal tumor. (Book p77)")
q(77, "Phyllodes Tumor", "Phyllodes tumor typically occurs in which decade?",
  ["4th/5th decade", "2nd decade", "6th/7th decade", "Childhood"], 0,
  "Age: 4th/5th decade. (Book p77)")
q(77, "Phyllodes Tumor", "Clinical features of phyllodes include:",
  ["Rapid increase in breast size with firm/hard variegated consistency", "Slow painful lump", "Nipple discharge only", "Skin puckering"], 0,
  "Clinical features: Rapid ↑ size of breast; Firm/hard with variegated consistency. (Book p77)")
q(77, "Phyllodes Tumor", "Spread to lymph nodes in phyllodes is:",
  ["<10%", ">50%", "Always", "30-40%"], 0,
  "<10% Spread to Lymph nodes. (Book p77)")
q(77, "Phyllodes Tumor", "Malignant phyllodes metastasizes to:",
  ["Lungs", "Liver first", "Bone only", "Brain only"], 0,
  "If malignant → metastasize to lungs. (Book p77)")
q(77, "Phyllodes Tumor", "To confirm diagnosis of phyllodes, core biopsy is based on:",
  ["Mitotic figures (benign/borderline/malignant)", "ER status", "Calcification", "Cyst size"], 0,
  "Core biopsy (To confirm Dx): Based on mitotic figures: Benign, Borderline, malignant. (Book p77)")
q(77, "Phyllodes Tumor", "First line treatment of phyllodes is:",
  ["Surgery: wide local excision/lumpectomy", "Chemotherapy", "RT alone", "Hormonal therapy"], 0,
  "Rx: Surgery (1st line): Wide local excision/Lumpectomy. (Book p77)")
q(77, "Phyllodes Tumor", "Simple mastectomy in phyllodes is done for:",
  ["Large tumors, malignant phyllodes post Sx (RT given), recurrent phyllodes", "All phyllodes", "Only benign small phyllodes", "Never"], 0,
  "Simple mastectomy for: Large tumors; malignant phyllodes Post Sx → RT given; Recurrent phyllodes. (Book p77)")
q(77, "Phyllodes Tumor", "Role of chemotherapy in phyllodes is:",
  ["No role", "First line", "Adjuvant always", "Only borderline"], 0,
  "No role of chemotherapy. (Book p77)")

# ---------------- p77-78 · FIBROADENOSIS / FIBROCYSTIC DISEASE ----------------
q(77, "Fibroadenosis & Cysts", "Incidence of fibroadenosis/fibrocystic disease is:",
  ["Age >25 years till menopause", "Age 15-25", "Post menopause only", "Any age equally"], 0,
  "Incidence: Age >25 years till menopause. (Book p77)")
q(77, "Fibroadenosis & Cysts", "The most common cause of cyclical mastalgia is:",
  ["Fibroadenosis", "Fibroadenoma", "Duct ectasia", "Cancer"], 0,
  "Cyclical mastalgia: m/c cause is Fibroadenosis. (Book p77)")
q(77, "Fibroadenosis & Cysts", "In cyclical mastalgia, pain is maximal:",
  ["Before menstrual cycle", "During menstrual cycle", "After menopause", "At ovulation only"], 0,
  "Before menstrual cycle: max pain; During menstrual cycle: Pain reduces. (Book p77)")
q(77, "Fibroadenosis & Cysts", "Tender nodularities/lumps in fibrocystic disease are assessed by:",
  ["Cardiff Lucknow Nodularity Score", "VAS only", "BIRADS", "Van Nuys score"], 0,
  "Assessed by Cardiff Lucknow Nodularity Score. (Book p77)")
q(78, "Fibroadenosis & Cysts", "USG in fibrocystic disease shows:",
  ["Cysts", "Solid masses", "Microcalcifications", "Duct dilatation only"], 0,
  "Ix: USG: Cysts seen. (Book p78)")
q(78, "Fibroadenosis & Cysts", "A simple cyst on USG is:",
  ["Smooth walled with no solid component; BIRADS 2; observation", "Solid components in wall; BIRADS 4", "Infective floating debris", "Septated with vegetations"], 0,
  "Simple cyst: Smooth walled, No solid component; BIRADS 2; Observation. (Book p78)")
q(78, "Fibroadenosis & Cysts", "A complex cyst (solid components in cyst wall) has BIRADS score 4 and needs:",
  ["Core biopsy to rule out cancer", "Observation", "Antibiotics", "Aspiration only"], 0,
  "Complex cyst: Solid components in cyst wall; BIRADS 4; Core biopsy to rule out cancer. (Book p78)")
q(78, "Fibroadenosis & Cysts", "A complicated cyst shows:",
  ["Infective intracystic floating debris; position changes with posture; if infected → antibiotics", "Smooth wall only", "Solid mural nodule", "Popcorn calcification"], 0,
  "Complicated cyst: Infective intracystic floating debris within the cyst; Position changes with posture; If infected: Antibiotics. (Book p78)")

# ---------------- p78 · MASTALGIA RX ----------------
q(78, "Mastalgia Rx", "Lifestyle/pain measures in fibrocystic disease include:",
  ["Reassurance with VAS breast pain chart, avoid caffeine/stress/sugar, tight sports brassiere", "Immediate biopsy", "Empiric antibiotics", "Mastectomy"], 0,
  "Reassure with VAS breast pain chart; Avoid caffeine, stress, sugar; Adequate support: Tight sports brassiere during the day. (Book p78)")
q(78, "Mastalgia Rx", "Flax seed 30 g daily is rich in:",
  ["Omega 3 fatty acids", "γ-linolenic acid", "Vitamin E", "Phytoestrogens only"], 0,
  "Flax seed 30g daily: Rich sources of Omega 3 fatty acids; oil of evening primrose: γ-linolenic acid. (Book p78)")
q(78, "Mastalgia Rx", "Oil of evening primrose is a rich source of:",
  ["γ-linolenic acid", "Omega 3", "Omega 6 only", "Vitamin D"], 0,
  "Oil of evening primrose: Rich in γ-linolenic acid. (Book p78)")
q(78, "Mastalgia Rx", "Topical NSAID creams for mastalgia include diclofenac/piroxicam applied:",
  ["4 times/day", "Once daily", "Once weekly", "Only at night"], 0,
  "Topical NSAID cream (Diclofenac/Piroxicam: 4 times/day). (Book p78)")
q(78, "Mastalgia Rx", "Systemic medication is considered when pain score is ≥3 on a VAS of:",
  ["0-10", "0-5", "0-100", "1-3"], 0,
  "Consider systemic medication if pain score ≥3 on a VAS of 0-10. (Book p78)")
q(78, "Mastalgia Rx", "Tamoxifen dose for mastalgia is:",
  ["10 mg daily for 3-6 months", "20 mg twice daily", "5 mg weekly", "40 mg daily"], 0,
  "Tamoxifen: 10mg daily, 3-6 months. (Book p78)")
q(78, "Mastalgia Rx", "Which systemic drug for mastalgia is NOT preferred?",
  ["Danazol", "Tamoxifen", "Ormeloxifene", "Topical NSAID"], 0,
  "Danazol (Not preferred): 50-300mg daily, 3-6 months. (Book p78)")
q(78, "Mastalgia Rx", "Ormeloxifene (Centchroman) dose and role is:",
  ["30 mg twice a week; treats cyclical & non cyclical mastalgia and nodularity", "10 mg daily only for pain", "300 mg daily", "Only pre-operative"], 0,
  "Ormeloxifene (Centchroman): 30 mg twice a week; 3-6 months in both cyclical & non cyclical mastalgia to treat nodularity. (Book p78)")

# ---------------- p78-79 · NON-CYCLICAL MASTALGIA: MONDOR'S & TIETZE'S ----------------
q(78, "Mondor's & Tietze's", "Mondor's disease is:",
  ["Thrombophlebitis of chest veins (lateral thoracic vein m/c)", "Costochondritis", "Duct ectasia", "Fat necrosis"], 0,
  "Mondor's disease: Thrombophlebitis of chest veins: Lateral thoracic vein (m/c). (Book p78)")
q(79, "Mondor's & Tietze's", "Clinical feature of Mondor's disease is:",
  ["Non cyclical mastalgia", "Cyclical mastalgia", "Bloody nipple discharge", "Fever with pus"], 0,
  "Clinical features: Non cyclical mastalgia. (Book p79)")
q(79, "Mondor's & Tietze's", "Risk of Mondor's disease is increased in:",
  ["Smokers", "Diabetics", "Hypertensives", "Vegetarians"], 0,
  "Risk factors: ↑ Risk in smokers. (Book p79)")
q(79, "Mondor's & Tietze's", "Cancer risk in Mondor's disease is:",
  ["No risk of cancer", "High", "Moderate", "Only with BRCA"], 0,
  "No risk of cancer. (Book p79)")
q(79, "Mondor's & Tietze's", "Treatment of Mondor's disease is:",
  ["Painkillers", "Anticoagulation", "Excision of vein", "Antibiotics"], 0,
  "Rx: Painkillers. (Book p79)")
q(79, "Mondor's & Tietze's", "Tietze's syndrome is also known as:",
  ["Costochondritis", "Mondor's cord", "Zuska disease", "Poland syndrome"], 0,
  "Tietze's syndrome AKA costochondritis. (Book p79)")
q(79, "Mondor's & Tietze's", "Tietze's syndrome presents with non cyclical mastalgia and:",
  ["Trigger point at costochondral junction", "Trigger point at sternum only", "Nipple retraction", "Axillary nodes"], 0,
  "Clinical features: Non cyclical mastalgia; Trigger point at costochondral junction. (Book p79)")
q(79, "Mondor's & Tietze's", "Management of Tietze's syndrome is:",
  ["Anti-inflammatory agents and intralesional steroid", "Surgery", "Antibiotics", "RT"], 0,
  "Mx: Anti-inflammatory agents; Intralesional steroid. (Book p79)")
q(79, "Mondor's & Tietze's", "Which statement about Mondor's & Tietze's syndrome is correct?",
  ["They are not a part of ANDI", "They are core ANDI conditions", "They are premalignant", "They occur only in men"], 0,
  "Note: mondor's & Tietze's syndrome are not a part of ANDI. (Book p79)")

# ---------------- p79 · NIPPLE DISCHARGE ----------------
q(79, "Nipple Discharge", "Which nipple discharge is suspicious?",
  ["Spontaneous & not expressed discharge", "Only on expression", "During lactation", "After exercise"], 0,
  "Spontaneous & not expressed discharge: Suspicious. (Book p79)")
q(79, "Nipple Discharge", "IOC for nipple discharge is USG; which tests are NOT sensitive?",
  ["Mammography and nipple discharge cytology", "USG and MRI", "Core biopsy and FNAC", "PET and CT"], 0,
  "Ix: USG (IOC); Mammography is not sensitive; Nipple discharge cytology is not sensitive. (Book p79)")
q(79, "Nipple Discharge", "Physiological causes of serous discharge are:",
  ["Puberty and pregnancy", "Lactation only", "Cancer", "Duct ectasia"], 0,
  "Serous: Physiological = Puberty, Pregnancy; Pathological = Cancer, Duct ectasia. (Book p79)")
q(79, "Nipple Discharge", "Pathological causes of serous discharge include:",
  ["Cancer and duct ectasia", "Puberty", "Pregnancy", "Lactation"], 0,
  "Serous pathological: Cancer, Duct ectasia. (Book p79)")
q(79, "Nipple Discharge", "Milky discharge with high prolactin is seen in prolactinoma and hypothyroidism; treatment is:",
  ["Cabergoline/Bromocriptine", "Tamoxifen", "Surgery", "RT"], 0,
  "↑ prolactin (Prolactinoma, hypothyroidism): Mx: Cabergoline/Bromocriptine. (Book p79)")
q(79, "Nipple Discharge", "Green/bluish nipple discharge from multiple ducts is due to:",
  ["Duct ectasia (m/c)", "Cancer", "Papilloma", "TB"], 0,
  "Green/Bluish: Duct ectasia (m/c), multiple ducts. (Book p79)")
q(79, "Nipple Discharge", "Benign causes of bloody nipple discharge include:",
  ["Duct papilloma (single duct), lactation due to cracked nipple, baby bites", "Only cancer", "Duct ectasia", "Mondor's disease"], 0,
  "Bloody: Duct papilloma (Single duct); Lactation (D/t cracked nipple); Baby bites the nipple; Pathological: Cancer. (Book p79)")

# ---------------- p80 · DUCT PAPILLOMA & DUCT ECTASIA ----------------
q(80, "Duct Papilloma & Duct Ectasia", "The most common cause of bloody nipple discharge from a SINGLE duct is:",
  ["Duct papilloma", "Duct ectasia", "Cancer", "Cracked nipple"], 0,
  "Duct papilloma: m/c cause of bloody nipple discharge from a single duct. (Book p80)")
q(80, "Duct Papilloma & Duct Ectasia", "Duct ectasia is the most common cause of:",
  ["Pathological nipple discharge", "Bloody single-duct discharge", "Cyclical mastalgia", "Popcorn calcification"], 0,
  "Duct ectasia: Pathological nipple discharge. (Book p80)")
q(80, "Duct Papilloma & Duct Ectasia", "Risk factors for duct ectasia are:",
  [">45 years (premenopausal) and smokers", "<25 years", "Male sex", "BRCA only"], 0,
  "Duct ectasia risk: >45 years (Premenopausal); Smokers. (Book p80)")
q(80, "Duct Papilloma & Duct Ectasia", "10% of duct papilloma cases are associated with:",
  ["Papillary DCIS", "Invasive lobular cancer", "LCIS", "Phyllodes"], 0,
  "Risk factors: 10% cases a/w papillary DCIS. (Book p80)")
q(80, "Duct Papilloma & Duct Ectasia", "Clinical feature of duct papilloma is a U/L periareolar nodule that on press gives:",
  ["Bloody discharge", "Milky discharge", "Green discharge", "Serous discharge"], 0,
  "U/L Periareolar nodule → press → Bloody discharge. (Book p80)")
q(80, "Duct Papilloma & Duct Ectasia", "In duct ectasia, stasis of secretion in dilated ducts causes periductal mastitis also called:",
  ["Zuska disease", "Mondor's disease", "Tietze's syndrome", "Peau d' orange"], 0,
  "Dilated ducts → Stasis of secretion → Periductal mastitis (Zuska disease). (Book p80)")
q(80, "Duct Papilloma & Duct Ectasia", "Duct ectasia can present with greenish/bluish discharge (multiple ducts) or:",
  ["Periareolar abscess or sinuses (aerobic + anaerobic)", "Bloody single duct discharge", "Popcorn calcification", "Nipple adenoma"], 0,
  "Periductal mastitis → Greenish or bluish discharge (multiple ducts) OR Periareolar abscess or sinuses (aerobic + anaerobic). (Book p80)")
q(80, "Duct Papilloma & Duct Ectasia", "USG in duct papilloma shows papillomatous growth within dilated ducts; if USG is inconclusive, do:",
  ["MRI", "CT", "PET", "Repeat USG in 6 months"], 0,
  "USG inconclusive → MRI. (Book p80)")
q(80, "Duct Papilloma & Duct Ectasia", "IOC for duct ectasia is:",
  ["USG", "MRI", "Ductogram", "CT"], 0,
  "Duct ectasia Ix: USG (IOC). (Book p80)")
q(80, "Duct Papilloma & Duct Ectasia", "Treatment of duct papilloma is:",
  ["Microdochectomy (removal of duct + papilla)", "Antibiotics", "Major duct excision", "Observation"], 0,
  "Mx: Microdochectomy (Removal of duct + papilla). (Book p80)")
q(80, "Duct Papilloma & Duct Ectasia", "In duct ectasia, if antibiotics fail, the surgery is:",
  ["Major duct excision: Hadfield procedure/Cone excision of ducts", "Microdochectomy", "Simple mastectomy", "Incision & drainage"], 0,
  "Antibiotics → Fails → major duct excision: Hadfield procedure/Cone excision of ducts. (Book p80)")
q(80, "Duct Papilloma & Duct Ectasia", "Relative risk of cancer with solitary papilloma is:",
  ["1.5-2 times", "3 times", "5 times", "No risk"], 0,
  "Solitary papilloma: RR of cancer: 1.5-2 times. (Book p80)")
q(80, "Duct Papilloma & Duct Ectasia", "Papillomatosis (B/L ≥5 papillomas) carries a relative cancer risk of:",
  ["3 times", "1.5-2 times", "10 times", "1 time"], 0,
  "Papillomatosis: B/L ≥5 papillomas & RR of cancer: 3 times. (Book p80)")
q(80, "Duct Papilloma & Duct Ectasia", "Juvenile papillomatosis is also called:",
  ["Swiss cheese disease", "Zuska disease", "Mondor's disease", "Breast mouse"], 0,
  "Juvenile papillomatosis (Swiss cheese disease): multiple papillomas in a young female with palpable nodules. (Book p80)")

# ---------------- p80-81 · PAGET'S VS ECZEMA ----------------
q(80, "Paget's vs Eczema", "Paget's disease of nipple is typically:",
  ["Unilateral (U/L)", "Bilateral (B/L)", "Central only", "Absent in women"], 0,
  "Site: Paget's U/L; Eczema B/L. (Book p80)")
q(80, "Paget's vs Eczema", "Eczema of the nipple is typically:",
  ["Bilateral", "Unilateral", "With destruction of NAC", "With an underlying lump"], 0,
  "Eczema: B/L. (Book p80)")
q(80, "Paget's vs Eczema", "Itching in Paget's disease and eczema is:",
  ["Present in both", "Absent in both", "Only in Paget's", "Only in eczema"], 0,
  "Itching: Present (both). (Book p80)")
q(80, "Paget's vs Eczema", "Destruction of the nipple areolar complex is seen in:",
  ["Paget's disease", "Eczema", "Both", "Neither"], 0,
  "Nipple areolar complex: Destruction (+) in Paget's; No destruction in eczema. (Book p80)")
q(80, "Paget's vs Eczema", "In Paget's disease, what percentage have an underlying lump?",
  [">70% (DCIS > invasive ductal cancer)", "<10%", "50% always invasive lobular", "Never"], 0,
  ">70% have an underlying lump (DCIS > Invasive ductal cancer). (Book p80)")
q(80, "Paget's vs Eczema", "Diagnosis of Paget's disease rests on Paget cells which are usually:",
  ["ER & PR -ve, CEA +ve", "ER & PR +ve, CEA -ve", "ER +ve only", "Her 2 -ve always"], 0,
  "Dx: Paget cells; Usually ER & PR -ve, CEA +ve. (Book p80)")
q(81, "Paget's vs Eczema", "On HPE, Paget cells are:",
  ["Large cells with clear cytoplasm, prominent nuclei in the epidermis", "Small blue cells in dermis", "Granulomas", "Signet ring cells in stroma"], 0,
  "Paget cells: Large cells with clear cytoplasm, prominent nuclei in the epidermis. (Book p81)")
q(80, "Paget's vs Eczema", "Management of Paget's disease is:",
  ["Mx of the underlying lump", "Topical steroids", "Antibiotics", "Observation"], 0,
  "Mx: Mx of lump (Paget's); Topical Steroids (eczema). (Book p80)")
q(80, "Paget's vs Eczema", "Eczema of the nipple is treated with:",
  ["Topical steroids", "Mastectomy", "RT", "Antibiotics"], 0,
  "Eczema: Topical Steroids. (Book p80)")

# ---------------- p81 · GYNECOMASTIA ----------------
q(81, "Gynecomastia", "Gynecomastia is:",
  ["Enlargement of male breast (U/L or B/L)", "Enlargement of female breast", "Male breast cancer", "Accessory nipple"], 0,
  "Gynecomastia: Enlargement of male breast; U/L or B/L. (Book p81)")
q(81, "Gynecomastia", "Physiological causes of gynecomastia are:",
  ["Newborn, puberty, senile", "Only drugs", "Liver disease", "Klinefelter only"], 0,
  "Physiological: 1. Newborn; 2. Puberty; 3. Senile. (Book p81)")
q(81, "Gynecomastia", "In the DISCKO mnemonic for drug-induced gynecomastia, D and I stand for:",
  ["Digoxin and Isoniazid", "Diazepam and Insulin", "Digoxin and Ibuprofen", "Danazol and Isoniazid"], 0,
  "DISCKO: D - Digoxin; I - Isoniazid. (Book p81)")
q(81, "Gynecomastia", "In DISCKO, the S drugs are:",
  ["Steroids and Spironolactone", "Sertraline and Statins", "Spironolactone only", "Salbutamol"], 0,
  "S - Steroids, Spironolactone. (Book p81)")
q(81, "Gynecomastia", "In DISCKO, C and K stand for:",
  ["Cimetidine and Ketoconazole", "Clofazimine and Ketamine", "Captopril and Ketoconazole", "Cimetidine and Clonidine"], 0,
  "C - Cimetidine; K - Ketoconazole. (Book p81)")
q(81, "Gynecomastia", "In DISCKO, O stands for:",
  ["Oestrogen", "Omeprazole", "Ondansetron", "Oxytocin"], 0,
  "O - Oestrogen. (Book p81)")
q(81, "Gynecomastia", "Which pathological cause of gynecomastia increases the risk of male breast cancer?",
  ["Klinefelter syndrome", "Liver disease", "Mumps orchitis", "Idiopathic"], 0,
  "Klinefelter syndrome (↑ Risk of male breast cancer). (Book p81)")
q(81, "Gynecomastia", "Paraneoplastic gynecomastia is seen in:",
  ["HCC, RCC, testicular cancer", "Lung and colon cancer", "Prostate cancer", "Melanoma"], 0,
  "Paraneoplastic conditions in HCC, RCC, Testicular cancer. (Book p81)")
q(81, "Gynecomastia", "Lepromatous and which orchitis cause gynecomastia?",
  ["Mumps orchitis", "TB orchitis", "Filarial orchitis", "E. coli orchitis"], 0,
  "Lepromatous / mumps orchitis. (Book p81)")
q(81, "Gynecomastia", "IOC in gynecomastia is USG showing:",
  ["Disc of breast tissue", "Cyst", "Solid mass", "Lymph node"], 0,
  "IOC: USG (Disc of breast tissue). (Book p81)")
q(81, "Gynecomastia", "Treatment of gynecomastia is:",
  ["Liposuction + gland excision", "Tamoxifen only", "Observation always", "Mastectomy with nodes"], 0,
  "Mx: Liposuction + Gland excision. (Book p81)")

# ---------------- p81 · POLYMASTIA, AMASTIA & POLYTHELIA ----------------
q(81, "Polymastia, Amastia & Polythelia", "Polymastia is:",
  ["Accessory breast tissue", "Absent breast", "Accessory nipple", "Male breast enlargement"], 0,
  "Polymastia: Accessory breast tissue. (Book p81)")
q(81, "Polymastia, Amastia & Polythelia", "The most common site of polymastia is:",
  ["Axilla", "Abdomen", "Back", "Groin"], 0,
  "Site: Axilla (m/c). (Book p81)")
q(81, "Polymastia, Amastia & Polythelia", "Polymastia becomes prominent during:",
  ["Puberty/pregnancy", "Old age", "Exercise", "Infection"], 0,
  "Prominent during puberty/pregnancy. (Book p81)")
q(81, "Polymastia, Amastia & Polythelia", "Polymastia is excised when:",
  ["Pain (+)/cosmetic reasons", "Always at birth", "Only if malignant", "Never"], 0,
  "Mx: if pain(+)/cosmetic reasons → Excision. (Book p81)")
q(81, "Polymastia, Amastia & Polythelia", "Amastia is seen in:",
  ["Poland syndrome", "Turner syndrome", "Klinefelter syndrome", "Marfan syndrome"], 0,
  "Amastia: Seen in Poland syndrome. (Book p81)")
q(81, "Polymastia, Amastia & Polythelia", "In Poland syndrome, which structures do not develop?",
  ["P. major & breast tissue", "Latissimus dorsi", "Serratus anterior", "Pectoralis minor only"], 0,
  "P. major & breast tissue do not develop. (Book p81)")
q(81, "Polymastia, Amastia & Polythelia", "Polythelia is:",
  ["Accessory nipple", "Accessory breast", "Absent nipple", "Inverted nipple"], 0,
  "Polythelia: Accessory nipple. (Book p81)")

# ---------------- units ----------------
def sec_ids(*labels):
    return [x["id"] for x in Q if x["sec"] in labels]

def first_page(label):
    for x in Q:
        if x["sec"] == label:
            return x["page"]
    return 0

UNIT_DEFS = [
    ("Breast Abscess: Lactational", ("Breast Abscess: Lactational",),
     "Lactational beats non-lactational: S. aureus from the child's oropharynx enters through a cracked nipple giving pain, swelling, fever; fluctuation is a LATE sign (as in parotid, ischiorectal, palmar/plantar abscesses). USG is IOC; amoxicillin-clavulanate or cloxacillin, express milk, two USG-guided aspirations, then I&D with a no. 11 blade if it recurs."),
    ("Recurrent Non-lactational Abscesses", ("Recurrent Non-lactational Abscesses",),
     "Three culprits: TB (caseating granulomas, AFB/GeneXpert +ve → ATT), idiopathic granulomatous mastitis (non-caseating, both negative, diagnosis of exclusion → steroids) and inflammatory cancer (carcinoma on HPE → treat the cancer)."),
    ("ANDI & Fibroadenoma", ("ANDI & Fibroadenoma",),
     "ANDI = Aberrations of Normal Development & Involution: 15-25 fibroadenoma, 25-40 fibrocystic disease, >40 fibrocystic > duct ectasia. The fibroadenoma is the m/c breast lump, a firm painless lobulated mobile 'breast mouse' of 15-25 with popcorn calcification, USG smooth wider-than-taller avascular, BIRADS II (complex III/IVa, IVa needs biopsy)."),
    ("Fibroadenoma: Staging & Rx", ("Fibroadenoma: Staging & Rx",),
     "Excise when growing fast, family history, painful, giant >4-5 cm or the patient wishes; open surgery uses a periareolar incision closed subcuticularly with 3-0 monocryl, while the latest vacuum-assisted scarless breast surgery leaves no mark."),
    ("Phyllodes Tumor", ("Phyllodes Tumor",),
     "Cystosarcoma phyllodes is a stromal tumor of the 4th/5th decade growing rapidly into a firm variegated mass; nodes <10% but malignant forms fly to lungs. Core biopsy grades benign/borderline/malignant by mitotic figures; wide local excision first, simple mastectomy for large/malignant (post-op RT)/recurrent, and chemo has no role."),
    ("Fibroadenosis & Cysts", ("Fibroadenosis & Cysts",),
     "From 25 to menopause, fibroadenosis is the m/c cause of cyclical mastalgia (worst pre-menstrually, easing with the cycle) with nodularity scored by the Cardiff Lucknow score. USG cysts: simple (smooth, no solid part, BIRADS 2, observe), complex (mural solid parts, BIRADS 4, core biopsy), complicated (floating infective debris shifting with posture, antibiotics if infected)."),
    ("Mastalgia Rx", ("Mastalgia Rx",),
     "Start with reassurance via a VAS pain chart, cutting caffeine/stress/sugar and a tight sports bra; add flax seed (omega-3) or evening primrose oil (γ-linolenic) and topical NSAIDs 4×/day. At VAS ≥3 go systemic: tamoxifen 10 mg daily, danazol (not preferred) or ormeloxifene 30 mg twice weekly which also settles nodularity."),
    ("Mondor's & Tietze's", ("Mondor's & Tietze's",),
     "Mondor's is thrombophlebitis of chest wall veins (lateral thoracic m/c) in smokers - non-cyclical pain, no cancer risk, painkillers. Tietze's (costochondritis) triggers at the costochondral junction, treated with anti-inflammatories and intralesional steroid. Neither belongs to ANDI."),
    ("Nipple Discharge", ("Nipple Discharge",),
     "Spontaneous unexpressed discharge is suspicious; USG is IOC because mammography and discharge cytology are not sensitive. Serous: puberty/pregnancy vs cancer/ectasia; milky: lactation vs prolactinoma/hypothyroid (cabergoline/bromocriptine); green-bluish: ectasia; bloody: papilloma, cracked nipple, baby bites - or cancer."),
    ("Duct Papilloma & Duct Ectasia", ("Duct Papilloma & Duct Ectasia",),
     "Papilloma = m/c bloody single-duct discharge from a pressable periareolar nodule (10% a/w papillary DCIS; USG papillomatous growth, MRI if unsure; microdochectomy). Ectasia hits >45 smokers: stasis → Zuska periductal mastitis, green-bluish multi-duct discharge or periareolar abscess/sinuses; antibiotics, then Hadfield major duct excision. Solitary RR 1.5-2×, papillomatosis (≥5, B/L) 3×, juvenile = Swiss cheese disease."),
    ("Paget's vs Eczema", ("Paget's vs Eczema",),
     "Both itch, but Paget's is unilateral with nipple-areolar destruction and >70% hide an underlying lump (DCIS > invasive ductal); its Paget cells - large, clear cytoplasm, prominent nuclei in epidermis, ER/PR -ve, CEA +ve - demand treatment of the lump, while bilateral non-destructive eczema takes topical steroids."),
    ("Gynecomastia", ("Gynecomastia",),
     "Male breast enlargement, U/L or B/L: physiological at newborn, puberty, senile; pathological via DISCKO drugs (digoxin, isoniazid, steroids/spironolactone, cimetidine, ketoconazole, oestrogen), idiopathic, Klinefelter (raises male cancer risk), liver disease, paraneoplastic HCC/RCC/testicular and lepromatous/mumps orchitis. USG shows the breast disc; liposuction + gland excision cures."),
    ("Polymastia, Amastia & Polythelia", ("Polymastia, Amastia & Polythelia",),
     "Polymastia is accessory breast tissue, axilla m/c, swelling at puberty/pregnancy, excised for pain or cosmetics; amastia (absent breast with missing pectoralis major) marks Poland syndrome; polythelia is simply an accessory nipple."),
]

UNITS = []
for i, (title, labels, guide) in enumerate(UNIT_DEFS, 1):
    UNITS.append({"id": f"SURG-U13-{i}", "ch": 13, "n": i, "title": title,
                  "sec": f"{labels[0]} · p{first_page(labels[0])}",
                  "qs": sec_ids(*labels), "guide": guide})

covered = [i for u in UNITS for i in u["qs"]]
assert covered == [x["id"] for x in Q], "units must cover questions in order"

data = {"questions": Q, "units": UNITS}
with open("data/ch13.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
print(f"ch13: {len(Q)} questions, {len(UNITS)} units")
