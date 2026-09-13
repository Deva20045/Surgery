#!/usr/bin/env python3
"""Build data/ch9.json for PULSE Surgery ch9 (Breast : Part 1, book p49-54)."""
import json

Q = []
def q(page, sec, text, opts, ans, exp):
    Q.append({"id": f"SURG-C9-{len(Q)+1:03d}", "sec": sec, "page": page,
              "q": text, "opts": opts, "ans": ans, "exp": exp})

# ---------------- p49 · SURGICAL ANATOMY ----------------
q(49, "Surgical Anatomy", "The breast is embryologically a:",
  ["Modified sweat gland", "Modified sebaceous gland", "Modified salivary gland", "Modified lymphoid organ"], 0,
  "Surgical anatomy: modified sweat gland. (Book p49)")
q(49, "Surgical Anatomy", "The axillary tail of Spence:",
  ["Extends upto axilla and can be mistaken for a lump", "Extends to the sternum", "Is always absent", "Contains no glandular tissue"], 0,
  "Axillary tail of Spence: Extends upto axilla; Can be mistaken for a lump. (Book p49)")
q(49, "Surgical Anatomy", "The vertical extent of the breast is from the:",
  ["2nd to 6th rib", "1st to 4th rib", "3rd to 8th rib", "4th to 9th rib"], 0,
  "Extent: 2nd to 6th rib. (Book p49)")
q(49, "Surgical Anatomy", "The horizontal extent of the breast is from the:",
  ["Midline to anterior/mid-axillary line", "Midline to posterior axillary line", "Sternum to scapula", "Clavicle to xiphisternum"], 0,
  "Extent: Midline to Anterior/Mid-axillary line. (Book p49)")
q(49, "Surgical Anatomy", "The number of lactiferous ducts and where they open are:",
  ["9-12 ducts opening at the nipple", "2-4 ducts opening at the areola", "20-25 ducts opening at the skin", "1 duct opening at the nipple"], 0,
  "Lactiferous ducts (9-12): Open at the nipple. (Book p49)")
q(49, "Surgical Anatomy", "The suspensory ligaments of Cooper run from the:",
  ["Pectoralis fascia to the skin", "Skin to the ribs", "Nipple to the areola", "Fascia to the sternum"], 0,
  "Suspensory ligaments of Cooper: Pectoralis fascia -> Skin. (Book p49)")
q(49, "Surgical Anatomy", "The function of Cooper's ligaments is to:",
  ["Maintain the shape of the breast", "Drain lymph", "Secrete milk", "Supply blood"], 0,
  "Suspensory ligaments of Cooper: Maintains the shape of the breast. (Book p49)")
q(49, "Surgical Anatomy", "The breast lies over which muscle and its fascia?",
  ["Pectoralis major", "Latissimus dorsi", "Serratus anterior", "Rectus abdominis"], 0,
  "Breast rests on Pectoralis major / Pectoralis fascia. (Book p49)")

# ---------------- p49 · CLINICAL SIGNS ----------------
q(49, "Clinical Signs", "Dimpling of breast skin is due to involvement of which structure in malignancy?",
  ["Ligament of Cooper", "Lactiferous duct", "Subdermal lymphatics", "Pectoralis major"], 0,
  "Dimpling: Due to involvement of ligament of Cooper in malignancy. (Book p49)")
q(49, "Clinical Signs", "Dimpling in breast cancer is:",
  ["Not a sign of skin involvement", "A definite sign of skin involvement", "A sign of chest wall fixation", "A sign of mastitis"], 0,
  "Dimpling: Not a sign of skin involvement in breast cancer. (Book p49)")
q(49, "Clinical Signs", "Retraction of nipple in breast cancer is:",
  ["Not a sign of skin involvement", "A sign of skin involvement", "Always benign", "Seen only in duct ectasia"], 0,
  "Retraction of nipple: Not a sign of skin involvement in breast cancer. (Book p49)")
q(49, "Clinical Signs", "A slit-like nipple retraction is characteristic of:",
  ["Duct ectasia", "Cancer", "Abscess", "Fibroadenoma"], 0,
  "Types of nipple retraction: Slit like (Duct ectasia). (Book p49)")
q(49, "Clinical Signs", "A circumferential nipple retraction is characteristic of:",
  ["Cancer", "Duct ectasia", "Trauma", "Congenital inversion"], 0,
  "Types of nipple retraction: Circumferential (cancer). (Book p49)")
q(49, "Clinical Signs", "Peau d'orange (PDO) gives which appearance?",
  ["Orange peel appearance", "Blue discoloration", "Shiny smooth skin", "Ulceration"], 0,
  "Peau d'orange: Orange peel appearance. (Book p49)")
q(49, "Clinical Signs", "Peau d'orange is caused by involvement of which structures in cancer?",
  ["Sub dermal/superficial lymphatics", "Cooper's ligaments", "Deep fascia", "Lactiferous ducts"], 0,
  "PDO: Involvement of sub dermal/superficial lymphatics in cancer. (Book p49)")
q(49, "Clinical Signs", "If more than 1/3rd of the breast is involved by peau d'orange, the diagnosis is:",
  ["Inflammatory breast cancer", "Duct ectasia", "Fat necrosis", "Phyllodes tumor"], 0,
  "If > 1/3rd of breast involved -> Inflammatory breast cancer. (Book p49)")

# ---------------- p50 · LYMPHATIC DRAINAGE ----------------
q(50, "Lymphatic Drainage", "What percentage of breast lymphatic drainage goes to axillary lymph nodes?",
  ["85-90%", "10-15%", "50-60%", "100%"], 0,
  "Lymphatic drainage: 85-90% Axillary Lymph nodes (LN). (Book p50)")
q(50, "Lymphatic Drainage", "What percentage of breast lymph drains to internal mammary lymph nodes?",
  ["10-15%", "85-90%", "25-30%", "5%"], 0,
  "Lymphatic drainage: 10-15% Internal mammary LN. (Book p50)")
q(50, "Lymphatic Drainage", "The clinical examination groups of axillary lymph nodes are:",
  ["Anterior, Central, Apical, Lateral, Posterior", "Level I, II, III", "Superficial and deep", "Medial and lateral"], 0,
  "Clinical Examination: Anterior, Central, Apical, Lateral, Posterior. (Book p50)")
q(50, "Lymphatic Drainage", "The surgical division of axillary nodes is based on their relation to the:",
  ["Pectoralis minor", "Pectoralis major", "Latissimus dorsi", "Subclavian vein"], 0,
  "Surgical division levels I-III are mapped on the Pectoralis minor. (Book p50)")
q(50, "Lymphatic Drainage", "Level I axillary nodes lie which side of the pectoralis minor?",
  ["Lateral", "Medial", "Posterior", "Deep"], 0,
  "Surgical division: Lateral = Level I. (Book p50)")
q(50, "Lymphatic Drainage", "Level III axillary nodes lie which side of the pectoralis minor?",
  ["Medial", "Lateral", "Superficial", "Within"], 0,
  "Surgical division: Medial = Level III. (Book p50)")
q(50, "Lymphatic Drainage", "Rotter's lymph nodes are present between the:",
  ["Pectoralis major and minor", "Skin and fascia", "Breast and ribs", "Axilla and neck"], 0,
  "Rotter's lymph nodes: Present b/w pectoralis major and minor. (Book p50)")
q(50, "Lymphatic Drainage", "The sentinel lymph node is:",
  ["The first draining LN from any cancer", "The largest axillary node", "The apical node", "A internal mammary node"], 0,
  "Sentinel lymph node -> First draining LN from any cancer. (Book p50)")

# ---------------- p50 · FUNCTIONAL UNIT & TRIPLE ASSESSMENT ----------------
q(50, "Functional Unit & Assessment", "The functional unit of the breast where most cancers arise is the:",
  ["Terminal duct lobular unit (TDLU)", "Lactiferous sinus", "Cooper's ligament", "Areolar gland"], 0,
  "Terminal duct lobular unit (TDLU): most cancers arise here. (Book p50)")
q(50, "Functional Unit & Assessment", "The stroma present between TDLUs gives rise to:",
  ["Fibroadenoma and phyllodes tumor", "Duct papilloma", "DCIS", "Fat necrosis"], 0,
  "Stroma present b/w TDLUs give rise to: Fibro adenoma; Phyllodes tumor. (Book p50)")
q(50, "Functional Unit & Assessment", "The triple assessment of a breast lump is:",
  ["Clinical examination -> Radiological investigation -> Histopathological investigation", "USG -> MRI -> PET", "FNAC -> core biopsy -> excision", "Inspection -> palpation -> auscultation"], 0,
  "Triple Assessment: Clinical examination -> Radiological investigation -> Histopathological investigation. (Book p50)")
q(50, "Functional Unit & Assessment", "The best method of breast examination is the:",
  ["Dial clock method", "Vertical strip method", "Circular spiral method", "Quadrant method only"], 0,
  "Breast examination: Best method: Dial clock method. (Book p50)")

# ---------------- p51 · RADIOLOGICAL: INITIAL & BIRADS ----------------
q(51, "Radiological: Initial & BIRADS", "The initial investigation for a breast lump in a woman <40 years (glands > fat) is:",
  ["USG", "Mammogram", "MRI", "PET"], 0,
  "Initial investigation: <40 years (Glands > Fat) -> USG. (Book p51)")
q(51, "Radiological: Initial & BIRADS", "The initial investigation for a breast lump in a woman >40 years (fat > glands) is:",
  ["Mammogram", "USG", "MRI", "FNAC"], 0,
  "Initial investigation: >40 years (Fat > Glands) -> Mammogram. (Book p51)")
q(51, "Radiological: Initial & BIRADS", "Mammography is not sensitive in ages < 40 years because:",
  ["Both lesions and normal glandular tissue are hyperintense", "Fat replaces glands", "Radiation is too high", "Breasts are too small"], 0,
  "Mammography not sensitive in ages < 40 yrs: Both lesions and normal glandular tissue are hyperintense. (Book p51)")
q(51, "Radiological: Initial & BIRADS", "BIRADS stands for:",
  ["Breast Imaging Reporting and Data Systems", "Breast Infection Risk and Data Scores", "Biopsy Imaging Rating and Diagnosis System", "Breast Index of Radiological Abnormality Degrees"], 0,
  "BIRADS: Breast Imaging Reporting and Data Systems. (Book p51)")
q(51, "Radiological: Initial & BIRADS", "BIRADS 0 category means:",
  ["Needs additional imaging - recall for additional imaging", "Negative", "Benign", "Suspicious"], 0,
  "BIRADS 0: Needs additional imaging; Recall for additional imaging; n/a. (Book p51)")
q(51, "Radiological: Initial & BIRADS", "BIRADS 1 (negative) and 2 (benign) are managed by:",
  ["Routine screening in 1 year; likelihood essentially 0%", "Biopsy", "6 month follow up", "Surgical excision"], 0,
  "BIRADS 1 & 2: Routine screening in 1 year; Essentially 0%. (Book p51)")
q(51, "Radiological: Initial & BIRADS", "BIRADS 3 (probably benign) is managed by:",
  ["Short term follow up (6 months); likelihood 0-3%", "Routine screening in 5 years", "Immediate biopsy", "Surgical excision"], 0,
  "BIRADS 3: Probably benign; Short term follow up (6 months); 0 - 3%. (Book p51)")
q(51, "Radiological: Initial & BIRADS", "BIRADS 4 (suspicious) is managed by:",
  ["Tissue diagnosis (biopsy)", "6 month follow up", "Routine screening", "Surgical excision"], 0,
  "BIRADS 4: Suspicious; Tissue Diagnosis (Biopsy). (Book p51)")
q(51, "Radiological: Initial & BIRADS", "The likelihood of cancer for BIRADS 4a, 4b and 4c respectively is:",
  ["2-10%, 10-50%, 50-95%", "0-3%, 3-10%, 10-50%", "10-20%, 20-40%, 40-60%", "5%, 15%, 25%"], 0,
  "BIRADS 4: 4a 2-10%; 4b 10-50%; 4c 50-95%. (Book p51)")
q(51, "Radiological: Initial & BIRADS", "BIRADS 5 (highly s/o malignancy) carries a likelihood of cancer of:",
  ["95%", "50%", "75%", "100%"], 0,
  "BIRADS 5: Highly s/o malignancy; Tissue Diagnosis (Biopsy); 95%. (Book p51)")
q(51, "Radiological: Initial & BIRADS", "BIRADS 6 (known biopsy proven) is managed by:",
  ["Surgical excision", "Repeat biopsy", "6 month follow up", "Routine screening"], 0,
  "BIRADS 6: Known biopsy proven; Surgical excision; n/a. (Book p51)")

# ---------------- p51 · ASBRS SCREENING GUIDELINES ----------------
q(51, "ASBRS Screening Guidelines", "As per ASBRS, formal risk assessment for breast cancer (Eg: Gail Index) begins at age:",
  ["≥25 yrs", "≥20 yrs", "≥30 yrs", "≥40 yrs"], 0,
  "ASBRS: 1. >25yrs -> Formal risk assessment for breast cancer (Eg: Gail Index). (Book p51)")
q(51, "ASBRS Screening Guidelines", "For average risk women, yearly screening mammography begins at:",
  ["40 yrs", "30 yrs", "45 yrs", "50 yrs"], 0,
  "ASBRS: 2. Average risk -> Begin yearly screening mammography at 40yrs. (Book p51)")
q(51, "ASBRS Screening Guidelines", "Screening mammography is ceased when life expectancy is less than:",
  ["10 yrs", "5 yrs", "15 yrs", "20 yrs"], 0,
  "ASBRS: 3. Life expectancy < 10yrs -> Cease screening mammography. (Book p51)")
q(51, "ASBRS Screening Guidelines", "Higher than average risk women receive:",
  ["Yearly screening mammography + supplemental imaging", "Only clinical examination", "Mammography every 3 years", "USG only"], 0,
  "ASBRS: 4. Higher than average risk: Yearly screening mammography + Supplemental imaging. (Book p51)")
q(51, "ASBRS Screening Guidelines", "Women with hereditary susceptibility (E.g. BRCA) or prior chest wall radiation (b/w 10-30 yrs) should have:",
  ["Annual MRI from 25 yrs and 3D mammography from 30 yrs", "3D mammogram from 35 yrs only", "USG from 40 yrs", "MRI from 40 yrs"], 0,
  "Hereditary susceptibility/prior chest wall radiation: a. Annual MRI from 25yrs; b. 3D mammography from 30 yrs. (Book p51)")
q(51, "ASBRS Screening Guidelines", "Women with predicted lifetime risk > 20% or a strong family history should have:",
  ["3D mammogram from 35 yrs; MRI if mammogram not showing relevant features", "Annual MRI from 25 yrs", "No screening", "USG yearly"], 0,
  "Predicted lifetime risk > 20%/Strong family history: a. 3D mammogram from 35yrs; b. If mammogram not showing relevant features -> MRI. (Book p51)")

# ---------------- p52 · MAMMOGRAPHY ----------------
q(52, "Mammography", "Mammography is essentially a:",
  ["X-ray of breast", "Ultrasound of breast", "MRI of breast", "CT of breast"], 0,
  "Mammography: ~ X-ray of breast. (Book p52)")
q(52, "Mammography", "The radiation dose of mammography is:",
  ["0.1 to 0.2 cGy (low radiation exposure)", "1-2 Gy", "10-20 cGy", "5 Gy"], 0,
  "Mammography: 0.1 to 0.2 cGy (Low radiation exposure). (Book p52)")
q(52, "Mammography", "The two views of mammography are:",
  ["Craniocaudal (CC) and mediolateral oblique (MLO)", "AP and lateral", "Oblique and axial", "CC and tangential"], 0,
  "Two views: Craniocaudal (CC); Mediolateral oblique (MLO). (Book p52)")
q(52, "Mammography", "Which mammographic view visualises the axilla and shows maximum breast tissue?",
  ["Mediolateral oblique (MLO)", "Craniocaudal (CC)", "Tangential", "True lateral"], 0,
  "MLO: Axilla visualised; Maximum breast tissue seen. (Book p52)")
q(52, "Mammography", "The latest mammography technique used in dense breasts for better pictures is:",
  ["3D Full Field Digital Tomosynthesis", "2D screen-film", "Xeroradiography", "Thermography"], 0,
  "Latest technique: 3D Full Field Digital Tomosynthesis -> used in dense breasts (Better pictures). (Book p52)")
q(52, "Mammography", "Benign breast lesions on mammography characteristically show:",
  ["Macro calcifications (popcorn calcification)", "Microcalcifications", "Spiculated margins", "Rounded nodes"], 0,
  "Benign lesion shows macro calcifications: Popcorn calcification (macrocalcification). (Book p52)")
q(52, "Mammography", "A calcified fibroadenoma on mammography shows which calcification and BIRADS category?",
  ["Popcorn calcification, BIRADS-2", "Microcalcification, BIRADS-4", "Spiculated, BIRADS-5", "No calcification, BIRADS-0"], 0,
  "Fibroadenoma: BIRADS-2 (CC); Popcorn calcification (macrocalcification). (Book p52)")
q(52, "Mammography", "A malignant lesion on the MLO view characteristically shows:",
  ["Spiculated margins", "Smooth round margins", "Popcorn calcification", "Preserved fatty hilum"], 0,
  "Malignant lesion: MLO shows spiculated margins. (Book p52)")
q(52, "Mammography", "Normal lymph nodes on mammography appear:",
  ["Kidney shaped with preserved fatty hilum", "Rounded with loss of fatty hilum", "Spiculated", "Calcified"], 0,
  "Normal lymph nodes: Kidney shaped (Preserved fatty hilum). (Book p52)")
q(52, "Mammography", "Malignant lymph nodes on mammography appear:",
  ["Rounded with loss of fatty hilum", "Kidney shaped with preserved hilum", "Elongated", "Invisible"], 0,
  "Malignant lymph nodes: Rounded (Loss of fatty hilum). (Book p52)")

# ---------------- p53 · BREAST ULTRASOUND ----------------
q(53, "Breast Ultrasound", "Advantages of breast ultrasound include all of the following EXCEPT:",
  ["Detects microcalcifications best", "No radiation exposure", "Best investigation to differentiate solid and cystic lesions", "Preferred in pregnancy"], 0,
  "USG advantages: No radiation exposure; Best to differentiate solid and cystic lesions; Preferred in pregnancy; Better in <40 years; Can detect ductal lesions. (Book p53)")
q(53, "Breast Ultrasound", "Breast ultrasound is better in which age group?",
  ["<40 years", ">40 years", ">60 years", "Any age equally"], 0,
  "USG: Better in <40 years. (Book p53)")
q(53, "Breast Ultrasound", "Breast ultrasound can detect ductal lesions such as:",
  ["Ductal papilloma", "Fibroadenoma", "Fat necrosis", "Phyllodes tumor"], 0,
  "USG: Can detect ductal lesions (Eg: Ductal papilloma). (Book p53)")
q(53, "Breast Ultrasound", "On ultrasound, a benign lesion is typically:",
  ["Wider than taller", "Taller than wider", "Rounded with lost hilum", "Spiculated"], 0,
  "USG findings: Lesion: Benign = Wider than taller. (Book p53)")
q(53, "Breast Ultrasound", "On ultrasound, a malignant lesion is typically:",
  ["Taller than wider", "Wider than taller", "Anechoic with posterior enhancement", "Kidney shaped"], 0,
  "USG findings: Lesion: Malignant = Taller than wider. (Book p53)")
q(53, "Breast Ultrasound", "On ultrasound, benign and malignant calcifications respectively are:",
  ["Macrocalcification and microcalcifications", "Microcalcifications and macrocalcification", "Both macro", "Both micro"], 0,
  "USG findings: Calcifications: Benign = Macrocalcification; Malignant = Microcalcifications. (Book p53)")
q(53, "Breast Ultrasound", "On ultrasound, benign and malignant lymph nodes respectively show:",
  ["Preserved hilum and rounded", "Rounded and preserved hilum", "Kidney shaped and kidney shaped", "Loss of hilum in both"], 0,
  "USG findings: LN: Benign = Preserved hilum; Malignant = Rounded. (Book p53)")
q(53, "Breast Ultrasound", "Intracapsular breast implant rupture on ultrasound shows the:",
  ["Stepladder pattern", "Snowstorm appearance", "Popcorn pattern", "Linguini's sign"], 0,
  "Breast implant rupture: Intracapsular -> Stepladder pattern. (Book p53)")
q(53, "Breast Ultrasound", "Extracapsular breast implant rupture on ultrasound shows the:",
  ["Snowstorm appearance", "Stepladder pattern", "Target sign", "Halo sign"], 0,
  "Breast implant rupture: Extracapsular -> Snowstorm appearance. (Book p53)")

# ---------------- p53 · MRI ----------------
q(53, "MRI", "The investigation of choice (IOC) for breast implants is:",
  ["MRI", "USG", "Mammogram", "CT"], 0,
  "MRI indications: i. Breast implants (+): IOC. (Book p53)")
q(53, "MRI", "Intracapsular rupture of a breast implant on MRI shows:",
  ["Linguini's sign", "Stepladder pattern", "Snowstorm appearance", "Popcorn sign"], 0,
  "Intracapsular rupture of implant: Linguini's sign. (Book p53)")
q(53, "MRI", "The IOC to identify multicentric/multifocal breast lesions is:",
  ["MRI", "USG", "Mammogram", "FNAC"], 0,
  "MRI indications: ii. To identify multicentric/multifocal lesions: IOC. (Book p53)")
q(53, "MRI", "Multifocal breast lesions are:",
  ["Multiple lesions in same quadrant; breast conservation Sx (+)", "Multiple lesions in different quadrants", "Lesions >5cm apart", "Breast conservation Sx (-)"], 0,
  "Multifocal: Multiple lesions in same quadrants; Breast conservation Sx (+). (Book p53)")
q(53, "MRI", "Multicentric breast lesions are:",
  ["Multiple lesions in different quadrants />5cm apart; breast conservation Sx (-)", "Multiple lesions in same quadrant", "Breast conservation Sx (+)", "Always unilateral single"], 0,
  "Multicentric: Multiple lesions in different quadrants />5cm apart; Breast conservation Sx (-). (Book p53)")
q(53, "MRI", "MRI breast is used as a screening tool for:",
  ["High risk patients", "All women >40", "Men", "Post-menopausal only"], 0,
  "MRI indications: iii. Screening tool for high risk patients. (Book p53)")
q(53, "MRI", "MRI breast is indicated when USG is inconclusive for:",
  ["Ductal lesions", "Cysts", "Fibroadenoma", "Fat necrosis"], 0,
  "MRI indications: iv. When USG is inconclusive for ductal lesions. (Book p53)")
q(53, "MRI", "MRI is sensitive for detecting:",
  ["Ductal Carcinoma In-situ (DCIS)", "Microcalcifications on USG", "Popcorn calcification", "Fatty hilum"], 0,
  "MRI indications: v. Sensitive for Ductal Carcinoma In-situ (DCIS). (Book p53)")
q(53, "MRI", "MRI breast is used to detect:",
  ["Local/scar recurrence", "Bone metastases only", "Liver metastases only", "Sentinel nodes"], 0,
  "MRI indications: vi. Used to detect local/scar recurrence. (Book p53)")

# ---------------- p54 · HISTOPATHOLOGICAL INVESTIGATION ----------------
q(54, "Histopathological Investigation", "FNAC of the breast uses which needle gauge?",
  ["23-30 G needle", "14 G needle", "8-11 G probe", "18 G needle"], 0,
  "FNAC: 23-30 G needle used. (Book p54)")
q(54, "Histopathological Investigation", "FNAC for breast lesions is:",
  ["Not used anymore", "The IOC", "The gold standard", "Preferred over core biopsy"], 0,
  "FNAC: Not used anymore for breast lesions. (Book p54)")
q(54, "Histopathological Investigation", "A key disadvantage of FNAC is:",
  ["High false negative", "High radiation", "Needs general anaesthesia", "Cannot be done outpatient"], 0,
  "FNAC disadvantages: i. High false negative. (Book p54)")
q(54, "Histopathological Investigation", "FNAC cannot differentiate in-situ from invasive cancers because:",
  ["Basement membrane breach is not appreciated", "Cells are destroyed", "Stains fail", "Needle is too thick"], 0,
  "FNAC: Cannot differentiate between in-situ and invasive cancers (Basement membrane breach not appreciated). (Book p54)")
q(54, "Histopathological Investigation", "Which IHC markers cannot be assessed on FNAC?",
  ["ER, PR, HER2 Neu, Ki-67", "CA 15-3 only", "CEA only", "AFP only"], 0,
  "FNAC: Immunohistochemistry (IHC) markers cannot be assessed (ER, PR, HER2 Neu, Ki-67). (Book p54)")
q(54, "Histopathological Investigation", "The IOC for a breast lump (incisional biopsy category) is:",
  ["Core needle biopsy / Tru-cut biopsy", "FNAC", "Punch biopsy", "Excisional biopsy"], 0,
  "Core needle biopsy / Tru-cut biopsy: IOC for breast lumps. (Book p54)")
q(54, "Histopathological Investigation", "Core needle/Tru-cut biopsy:",
  ["Removes a piece of tissue", "Removes the whole lump", "Only aspirates cells", "Uses vacuum"], 0,
  "Core needle biopsy: Removes a piece of tissue. (Book p54)")
q(54, "Histopathological Investigation", "As per the recent update, core needle biopsy uses which needle?",
  ["14 G needles", "23-30 G needles", "8-11 G probes", "18 G needles"], 0,
  "Core needle biopsy: 14 G needles used (Recent update). (Book p54)")
q(54, "Histopathological Investigation", "Punch biopsy of the breast region is used for:",
  ["Skin lesions / Paget's disease", "Deep lumps", "Cysts", "Fibroadenoma"], 0,
  "Punch biopsy: Used for skin lesions / Paget's disease. (Book p54)")
q(54, "Histopathological Investigation", "Vacuum Assisted Breast Biopsy (VABB) uses:",
  ["8-11 G probe attached to vacuum", "14 G needle", "23 G needle", "Scalpel"], 0,
  "VABB: 8-11 G probe attached to vacuum. (Book p54)")
q(54, "Histopathological Investigation", "VABB is used for:",
  ["Scarless fibroadenoma surgery", "Mastectomy", "Sentinel node biopsy", "DCIS treatment"], 0,
  "VABB: Used for scarless fibroadenoma surgery. (Book p54)")
q(54, "Histopathological Investigation", "The gold standard investigation with 100% chance of detection is:",
  ["Excisional biopsy", "FNAC", "Core biopsy", "Mammography"], 0,
  "Excisional Biopsy: Gold standard investigation (100% chance of detection). (Book p54)")

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
    ("Surgical Anatomy of the Breast", ("Surgical Anatomy",),
     "The breast is a modified sweat gland spanning the 2nd-6th ribs from midline to the anterior/mid-axillary line, with an axillary tail of Spence that mimics a lump. 9-12 lactiferous ducts open at the nipple, and Cooper's ligaments from pectoralis fascia to skin hold its shape."),
    ("Clinical Signs: Dimpling, Nipple Retraction & Peau d'Orange", ("Clinical Signs",),
     "Dimpling means Cooper's ligament involvement and nipple retraction is slit-like in duct ectasia but circumferential in cancer - neither is a sign of skin involvement. Peau d'orange is subdermal lymphatic block giving an orange peel look; beyond a third of the breast it declares inflammatory breast cancer."),
    ("Lymphatic Drainage & Axillary Levels", ("Lymphatic Drainage",),
     "85-90% of lymph flows to axillary nodes (clinically anterior, central, apical, lateral, posterior; surgically levels I-III around pectoralis minor) and 10-15% to internal mammary nodes. Rotter's nodes sit between the pectoralis muscles, and the sentinel node is the first draining node of any cancer."),
    ("Functional Unit & Triple Assessment", ("Functional Unit & Assessment",),
     "Most cancers arise in the terminal duct lobular unit while the stroma between TDLUs breeds fibroadenoma and phyllodes. Every lump passes through triple assessment - clinical (dial clock method), radiological then histopathological."),
    ("Initial Radiological Investigation & BIRADS", ("Radiological: Initial & BIRADS",),
     "Under 40 (glands > fat) start with USG; over 40 (fat > glands) with mammography, which fails below 40 because lesions and glandular tissue are both hyperintense. BIRADS runs from 0 (recall) through 1-2 (routine yearly, ~0%), 3 (6-month follow-up, 0-3%), 4a-c (biopsy, 2-95%) and 5 (biopsy, 95%) to 6 (surgical excision)."),
    ("ASBRS Breast Cancer Screening Guidelines", ("ASBRS Screening Guidelines",),
     "Formal risk assessment (Gail Index) from 25, yearly mammography from 40 for average risk, cease when life expectancy is under 10 years. High-risk women add supplemental imaging: BRCA or chest radiation get annual MRI from 25 and 3D mammography from 30; lifetime risk >20% or strong family history get 3D mammogram from 35 with MRI if mammography is silent."),
    ("Mammography: Views, Dose & Findings", ("Mammography",),
     "A 0.1-0.2 cGy X-ray in CC and MLO views - MLO catches the axilla and most tissue - now upgraded to 3D full field digital tomosynthesis for dense breasts. Benign lesions show popcorn macrocalcifications (fibroadenoma BIRADS-2), malignancy shows spiculated margins, and nodes turn from kidney-shaped with fatty hilum to rounded without it."),
    ("Breast Ultrasound", ("Breast Ultrasound",),
     "Radiation-free, best for solid vs cystic, preferred in pregnancy and under-40s, and able to catch ductal papillomas. Benign lesions lie wider than taller with macrocalcifications and preserved hilum; malignant ones stand taller than wider with microcalcifications and rounded nodes. Implant rupture: stepladder inside the capsule, snowstorm outside."),
    ("MRI Breast", ("MRI",),
     "MRI is IOC for implants (linguini's sign marks intracapsular rupture) and for mapping multicentric/multifocal disease - multifocal in one quadrant allows conservation, multicentric across quadrants or >5 cm apart forbids it. It screens high-risk patients, resolves inconclusive ductal USG, catches DCIS and detects local/scar recurrence."),
    ("Histopathological Investigation: FNAC to Excision", ("Histopathological Investigation",),
     "FNAC (23-30 G) is retired for breast: high false negatives, no in-situ vs invasive call, no IHC (ER, PR, HER2 Neu, Ki-67). Tru-cut/core (14 G) is IOC and takes a tissue piece, punch biopsy samples skin/Paget's, VABB (8-11 G vacuum probe) removes fibroadenomas scarlessly, and excisional biopsy remains the 100% gold standard."),
]

UNITS = []
for i, (title, labels, guide) in enumerate(UNIT_DEFS, 1):
    UNITS.append({"id": f"SURG-U9-{i}", "ch": 9, "n": i, "title": title,
                  "sec": f"{labels[0]} \u00b7 p{first_page(labels[0])}",
                  "qs": sec_ids(*labels), "guide": guide})

covered = [i for u in UNITS for i in u["qs"]]
assert covered == [x["id"] for x in Q], "units must cover questions in order"

data = {"questions": Q, "units": UNITS}
with open("data/ch9.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
print(f"ch9: {len(Q)} questions, {len(UNITS)} units")
