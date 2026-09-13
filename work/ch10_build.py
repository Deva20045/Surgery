#!/usr/bin/env python3
"""Build data/ch10.json for PULSE Surgery ch10 (Breast : Part 2, book p55-60)."""
import json

Q = []
def q(page, sec, text, opts, ans, exp):
    Q.append({"id": f"SURG-C10-{len(Q)+1:03d}", "sec": sec, "page": page,
              "q": text, "opts": opts, "ans": ans, "exp": exp})

# ---------------- p55 · RISK FACTORS ----------------
q(55, "Risk Factors", "Which of the following is NOT a listed risk factor for breast cancer?",
  ["Breastfeeding ≥1 year", "Early menarche", "Late menopause", "Nulliparity"], 0,
  "Risk factors: ↑ Age, Early menarche, Late menopause, Nulliparity... (breastfeeding ≥1 year is protective). (Book p55)")
q(55, "Risk Factors", "Obesity raises breast cancer risk because of peripheral conversion of fat to estrogen by:",
  ["Aromatase", "5-alpha reductase", "Cyclooxygenase", "Lipase"], 0,
  "Obesity: Peripheral conversion of fat --Aromatase--> Estrogen. (Book p55)")
q(55, "Risk Factors", "Maternal age at first live birth that increases breast cancer risk is:",
  ["≥ 30 yrs", "≤ 20 yrs", "21-25 yrs", "Any age"], 0,
  "Risk factor: Maternal age at first live birth (≥ 30 yrs). (Book p55)")
q(55, "Risk Factors", "Family history as a breast cancer risk factor includes:",
  ["Maternal & paternal sides", "Only maternal side", "Only paternal side", "Only siblings"], 0,
  "Family history: maternal & paternal. (Book p55)")
q(55, "Risk Factors", "Which therapy is a listed breast cancer risk factor?",
  ["Hormone replacement therapy", "Low dose OCPs", "Tamoxifen", "Insulin"], 0,
  "Risk factor: Hormone replacement therapy. (Book p55)")
q(55, "Risk Factors", "The hormonal risk factors early menarche and late menopause act by:",
  ["Increasing lifetime estrogen exposure", "Decreasing estrogen", "Raising prolactin", "Lowering FSH"], 0,
  "Risk factors: Early menarche and Late menopause (prolonged estrogen exposure). (Book p55)")
q(55, "Risk Factors", "Which lifestyle factors are listed breast cancer risks?",
  ["Alcohol and smoking", "Exercise", "Weight reduction", "Breastfeeding"], 0,
  "Risk factors: 6. Alcohol; 7. Smoking. (Book p55)")

# ---------------- p55 · DUPONT & PAGE CLASSIFICATION ----------------
q(55, "Dupont & Page Classification", "In the Dupont & Page classification, nonproliferative lesions, cysts, mild hyperplasia of the usual type and columnar cell change carry a relative risk of:",
  ["1 (No risk)", "1.3-1.9", "4-5", "9"], 0,
  "Dupont & Page: Nonproliferative lesions, Cysts, Mild hyperplasia of the usual type, Columnar cell change = 1 (No risk). (Book p55)")
q(55, "Dupont & Page Classification", "Proliferative lesions without atypia, sclerosing adenosis, moderate/florid ductal hyperplasia, radial scar, intraductal papilloma and complex fibroadenoma carry a relative risk of:",
  ["1.3-1.9", "1 (No risk)", "4-5", "9"], 0,
  "Dupont & Page: Proliferative lesions without atypia group = 1.3-1.9. (Book p55)")
q(55, "Dupont & Page Classification", "Atypical hyperplasia (atypical ductal/lobular hyperplasia) carries a relative risk of:",
  ["4-5", "1.3-1.9", "9", "1"], 0,
  "Dupont & Page: Atypical hyperplasia, Atypical ductal hyperplasia, Atypical lobular hyperplasia = 4-5. (Book p55)")
q(55, "Dupont & Page Classification", "Carcinoma in-situ carries a relative risk of:",
  ["9", "4-5", "1.3-1.9", "1"], 0,
  "Dupont & Page: Carcinoma in-situ = 9. (Book p55)")
q(55, "Dupont & Page Classification", "Which lesion sits in the 1.3-1.9 relative risk group?",
  ["Radial scar", "Atypical ductal hyperplasia", "Carcinoma in-situ", "Cysts"], 0,
  "1.3-1.9 group includes Radial scar (and sclerosing adenosis, intraductal papilloma...). (Book p55)")
q(55, "Dupont & Page Classification", "The Dupont & Page classification estimates breast cancer risk due to:",
  ["Pre-existing lesion in breast", "Family history", "Age alone", "Radiation exposure"], 0,
  "Dupont & Page classification: Risk of breast cancer d/t pre-existing lesion in breast. (Book p55)")

# ---------------- p56 · NOTES: SMOKERS, PROTECTIVE, OCP ----------------
q(56, "Notes: Smokers & Protective", "Breast conditions associated with increased risk in smokers include:",
  ["Breast cancer, duct ectasia and Mondor's disease", "Fibroadenoma and cysts", "Phyllodes tumor", "Fat necrosis only"], 0,
  "Breast conditions associated with ↑ risk in smokers: Breast cancer, Duct ectasia, Mondor's disease. (Book p56)")
q(56, "Notes: Smokers & Protective", "Protective factors against breast cancer include maternal age at first live birth of:",
  ["≤20 years", "≥30 years", "25-29 years", "Any age"], 0,
  "Protective factors: maternal age at first live birth: ≤20 years. (Book p56)")
q(56, "Notes: Smokers & Protective", "Breastfeeding is protective against breast cancer when continued for:",
  ["≥1 year", "≥1 month", "≥1 week", "≥5 years"], 0,
  "Protective factors: Breastfeeding ≥1 year. (Book p56)")
q(56, "Notes: Smokers & Protective", "Low dose OCPs:",
  ["Do not increase risk of breast cancer", "Double the risk", "Are protective", "Cause BRCA mutation"], 0,
  "Low dose OCP's do not ↑ risk of breast cancer. (Book p56)")

# ---------------- p56 · GENES ASSOCIATED ----------------
q(56, "Genes Associated", "What proportion of breast cancer is familial vs sporadic?",
  ["10% familial, 90% sporadic", "50% each", "30% familial, 70% sporadic", "90% familial"], 0,
  "Breast cancer: 10% Familial; 90% Sporadic. (Book p56)")
q(56, "Genes Associated", "The m/c gene mutated in breast cancer overall is:",
  ["p53", "BRCA1", "PIK3CA", "HER2"], 0,
  "m/c gene mutated in: Breast cancer: p53. (Book p56)")
q(56, "Genes Associated", "Familial breast cancer is most commonly associated with which gene?",
  ["BRCA 1", "p53", "PIK3CA", "APC"], 0,
  "Familial breast cancer: BRCA 1. (Book p56)")
q(56, "Genes Associated", "ER, PR +ve breast cancer is most commonly associated with mutation of:",
  ["PIK3CA", "p53", "BRCA2", "PTEN"], 0,
  "ER, PR +ve breast cancer: PIK3CA. (Book p56)")
q(56, "Genes Associated", "Triple negative breast cancer (TNBC)/HER 2 neu +ve breast cancer is associated with:",
  ["p53", "PIK3CA", "BRCA2", "CDH1"], 0,
  "Triple negative breast cancer (TNBC)/HER 2 neu +ve: p53. (Book p56)")

# ---------------- p56-57 · BRCA GENES & TESTING ----------------
q(56, "BRCA Genes & Testing", "BRCA genes give rise to which syndrome?",
  ["HBOC syndrome: Hereditary breast & ovarian cancer syndrome", "Li-Fraumeni syndrome", "Cowden syndrome", "Peutz-Jeghers syndrome"], 0,
  "BRCA genes: Give rise to HBOC syndrome: Hereditary breast & ovarian cancer syndrome. (Book p56)")
q(56, "BRCA Genes & Testing", "BRCA 1 and BRCA 2 lie on which chromosomes?",
  ["17q and 13q", "13q and 17q", "17p and 13p", "11q and 13q"], 0,
  "BRCA table: Chromosome: BRCA 1 = 17q; BRCA 2 = 13q. (Book p56)")
q(56, "BRCA Genes & Testing", "Aggression in BRCA 1 vs BRCA 2 cancers is:",
  ["BRCA 1 ↑, BRCA 2 ↓", "BRCA 1 ↓, BRCA 2 ↑", "Equal", "Both low"], 0,
  "BRCA table: Aggression: BRCA 1 ↑; BRCA 2 ↓. (Book p56)")
q(56, "BRCA Genes & Testing", "The m/c subtype and histology in BRCA 1 cancers are:",
  ["Basal (TNBC) and medullary", "Luminal and tubular", "Luminal and mucinous", "HER2 enriched and lobular"], 0,
  "BRCA 1: m/c subtype Basal (TNBC); m/c histology: medullary. (Book p56)")
q(56, "BRCA Genes & Testing", "The m/c subtype in BRCA 2 cancers is:",
  ["Luminal", "Basal (TNBC)", "Medullary", "Claudin low"], 0,
  "BRCA 2: m/c subtype Luminal. (Book p56)")
q(56, "BRCA Genes & Testing", "Risk of breast & ovarian cancer is higher with:",
  ["BRCA 1 > BRCA 2", "BRCA 2 > BRCA 1", "BRCA 1 = BRCA 2", "Neither"], 0,
  "Risk of: Breast & ovarian cancer: BRCA 1 > BRCA 2. (Book p56)")
q(56, "BRCA Genes & Testing", "Risk of pancreatic, prostate and male breast cancer is higher with:",
  ["BRCA 2 > BRCA 1", "BRCA 1 > BRCA 2", "BRCA 1 = BRCA 2", "Only p53"], 0,
  "Pancreatic, prostate, male breast cancer: BRCA 2 > BRCA 1. (Book p56)")
q(56, "BRCA Genes & Testing", "Risk of colorectal & peritoneal cancer between BRCA 1 and BRCA 2 is:",
  ["BRCA 1 = BRCA 2", "BRCA 1 > BRCA 2", "BRCA 2 > BRCA 1", "None"], 0,
  "Colorectal & peritoneal cancer: BRCA 1 = BRCA 2. (Book p56)")
q(56, "BRCA Genes & Testing", "Indications for BRCA testing for ALL patients include deleterious BRCA 1/2 gene mutation in a blood relative and:",
  ["Personal history of ovarian, fallopian tube, and/or primary peritoneal cancer", "Personal history of fibroadenoma", "Family history of lung cancer", "Age > 60 years"], 0,
  "For all patients: Deleterious BRCA 1/2 gene mutation in a blood relative; Personal history of ovarian, fallopian tube, and/or primary peritoneal cancer. (Book p56)")
q(57, "BRCA Genes & Testing", "For all patients WITH breast cancer, BRCA testing is indicated when ≥1 blood relative was diagnosed with breast cancer at:",
  ["≤45 years", "≤60 years", "≤70 years", "Any age"], 0,
  "For all patients with breast cancer: ≥1 blood relatives diagnosed with breast cancer at ≤45 years. (Book p57)")
q(57, "BRCA Genes & Testing", "Personal history of b/l breast cancer at what age indicates BRCA testing?",
  ["≤50 years", "≤45 years", "≤60 years", "≤40 years"], 0,
  "Personal history of b/l breast cancer at ≤50 years. (Book p57)")
q(57, "BRCA Genes & Testing", "Personal history of triple-negative breast cancer at what age indicates BRCA testing?",
  ["≤60 years", "≤45 years", "≤50 years", "≤30 years"], 0,
  "Personal history of triple-negative breast cancer at ≤60 years. (Book p57)")
q(57, "BRCA Genes & Testing", "Which personal history always indicates BRCA testing in a breast cancer patient?",
  ["Male breast cancer", "Fibroadenoma", "Duct ectasia", "Mastitis"], 0,
  "Personal history of male breast cancer. (Book p57)")
q(57, "BRCA Genes & Testing", "Lifestyle modifications in BRCA mutation include all of the following EXCEPT:",
  ["Start low dose OCPs", "Weight reduction", "Exercise regularly", "Cessate smoking & alcohol consumption"], 0,
  "Lifestyle modifications in BRCA mutation: Weight reduction; Exercise regularly; Cessate smoking & alcohol consumption; MRI breast screening from 25 yr of age. (Book p57)")
q(57, "BRCA Genes & Testing", "In BRCA mutation carriers, MRI breast screening starts from:",
  ["25 yr of age", "30 yr of age", "35 yr of age", "40 yr of age"], 0,
  "MRI breast screening from 25 yr of age. (Book p57)")

# ---------------- p57 · RISK REDUCTION STRATEGIES ----------------
q(57, "Risk Reduction Strategies", "B/L prophylactic mastectomy reduces breast cancer risk by:",
  ["95%", "50%", "47%", "90%"], 0,
  "B/L prophylactic mastectomy: 95% risk reduction. (Book p57)")
q(57, "Risk Reduction Strategies", "In B/L prophylactic mastectomy:",
  ["Skin & nipple are spared", "Nipple is always removed", "Skin is always removed", "Both breasts are left"], 0,
  "B/L prophylactic mastectomy: Skin & nipple spared. (Book p57)")
q(57, "Risk Reduction Strategies", "B/L salpingo oophorectomy is timed:",
  ["After completion of family (within 40 years of age)", "Before 30 years always", "After 60 years", "At diagnosis"], 0,
  "B/L salpingo oophorectomy: Time: After completion of family (within 40 years of age). (Book p57)")
q(57, "Risk Reduction Strategies", "B/L salpingo oophorectomy reduces ovarian cancer risk by:",
  ["↓ 90% risk (10% risk of fallopian tube/1° peritoneal cancer remains)", "↓ 50%", "↓ 47%", "100%"], 0,
  "Ovarian cancer: ↓ 90% risk (10% risk of fallopian tube/1° peritoneal cancer). (Book p57)")
q(57, "Risk Reduction Strategies", "B/L salpingo oophorectomy reduces breast cancer risk by:",
  ["↓ 50% risk", "↓ 90% risk", "↓ 47% risk", "↓ 95% risk"], 0,
  "Breast cancer: ↓ 50% risk. (Book p57)")
q(57, "Risk Reduction Strategies", "Tamoxifen, a SERM, reduces breast cancer risk by:",
  ["↓ 47%", "↓ 95%", "↓ 90%", "↓ 25%"], 0,
  "Tamoxifen: (SERM): ↓ 47% of breast cancer. (Book p57)")

# ---------------- p57 · BIOPSY & HISTOLOGICAL TYPES ----------------
q(57, "Biopsy & Histological Types", "The IOC biopsy for breast cancer is:",
  ["Core needle biopsy", "FNAC", "Punch biopsy", "Excisional biopsy"], 0,
  "Biopsy: IOC: Core needle biopsy. (Book p57)")
q(57, "Biopsy & Histological Types", "Core needle biopsy gives the type (ductal vs lobular) and the biology via:",
  ["IHC", "USG", "MRI", "PET"], 0,
  "Biopsy: Type ...; Biology: IHC. (Book p57)")
q(57, "Biopsy & Histological Types", "Within ductal carcinoma, the m/c form is:",
  ["Invasive", "In situ", "Both equal", "None"], 0,
  "Ductal carcinoma: In situ; Invasive (m/c). (Book p57)")
q(57, "Biopsy & Histological Types", "The histological type of breast cancer overall is:",
  ["Invasive ductal carcinoma", "Lobular carcinoma", "Tubular", "Mucinous"], 0,
  "Histological types: Breast cancer: Invasive ductal carcinoma. (Book p57)")
q(57, "Biopsy & Histological Types", "Ductal carcinoma is otherwise labelled:",
  ["NOS (Not otherwise specified)", "NOS (New onset syndrome)", "TIS", "LCIS"], 0,
  "Ductal carcinoma: NOS (Not otherwise specified). (Book p57)")
q(57, "Biopsy & Histological Types", "Which special histological type carries a good prognosis?",
  ["Tubular", "Medullary", "Basal like", "Invasive ductal"], 0,
  "Special types: 1. Tubular: Good prognosis. (Book p57)")
q(57, "Biopsy & Histological Types", "Medullary breast cancer is associated with:",
  ["BRCA 1", "BRCA 2", "p53 only", "PIK3CA"], 0,
  "Special types: 3. Medullary: A/w BRCA 1. (Book p57)")
q(57, "Biopsy & Histological Types", "The special types of breast cancer listed are:",
  ["Tubular, mucinous and medullary", "Papillary only", "Cribriform only", "Metaplastic only"], 0,
  "Special types: Tubular (good prognosis), Mucinous, Medullary (A/w BRCA 1). (Book p57)")

# ---------------- p58 · IHC ----------------
q(58, "IHC", "ER & PR are which kind of receptors on IHC?",
  ["Nuclear receptors", "Membranous markers", "Cytoplasmic markers", "Mitochondrial markers"], 0,
  "IHC: 1. ER & PR: Nuclear receptors. (Book p58)")
q(58, "IHC", "The Allred score range for ER/PR is:",
  ["0-8", "0-3", "1-10", "0-100"], 0,
  "Allred score: 0-8. (Book p58)")
q(58, "IHC", "Her 2 neu is which kind of marker?",
  ["Membranous marker", "Nuclear receptor", "Cytosolic enzyme", "Stromal marker"], 0,
  "2. Her 2 neu: Membranous marker. (Book p58)")
q(58, "IHC", "Her 2 neu grades 0 and 1+ are reported as:",
  ["- ve", "+ve", "Equivocal", "Amplified"], 0,
  "Grades: 0, 1+ -> - ve. (Book p58)")
q(58, "IHC", "A Her 2 neu grade of 2+ (equivocal) is resolved by the IOC test:",
  ["FISH (Fluorescent in situ hybridization)", "PCR of serum", "Repeat IHC on same slide", "CT scan"], 0,
  "2+: Equivocal -> IOC: FISH (Fluorescent in situ hybridization). (Book p58)")
q(58, "IHC", "On FISH for Her 2 neu, 'not amplified' and 'amplified' correspond to:",
  ["-ve and +ve respectively", "+ve and -ve", "Both -ve", "Both +ve"], 0,
  "FISH: Not amplified -> -ve; Amplified -> +ve. (Book p58)")
q(58, "IHC", "A Her 2 neu grade of 3+ is reported as:",
  ["+ve", "-ve", "Equivocal", "Indeterminate"], 0,
  "3+: +ve. (Book p58)")
q(58, "IHC", "The brown stain in IHC is due to:",
  ["DAB (3,3' Diaminobenzidine)", "Hematoxylin", "Eosin", "Fluorescein"], 0,
  "Brown stain d/t DAB (3,3' Diaminobenzidine). (Book p58)")
q(58, "IHC", "Ki67 is a marker of:",
  ["Proliferation index", "Hormone receptors", "Membrane amplification", "Apoptosis"], 0,
  "3. Ki67: Proliferation index marker. (Book p58)")

# ---------------- p58 · MOLECULAR CLASSIFICATION ----------------
q(58, "Molecular Classification", "The molecular classification of breast cancer is based on:",
  ["Gene expression profiling", "Tumor size", "Nodal status", "Age"], 0,
  "Molecular classification of breast cancer: Based on gene expression profiling. (Book p58)")
q(58, "Molecular Classification", "The m/c molecular subtype with the best prognosis is:",
  ["Luminal A", "Luminal B", "Basal like", "Claudin low"], 0,
  "Luminal A (m/c): Best prognosis. (Book p58)")
q(58, "Molecular Classification", "Luminal A tumors show which ER/PR/HER2/Ki-67/CK5-6 pattern?",
  ["+ + - ↓ -", "- - + Any -", "+ + + Any +", "- - - Any +"], 0,
  "Luminal A: ER +, PR +, HER2 -, Ki-67 ↓, Cytokeratin 5 and 6 -. (Book p58)")
q(58, "Molecular Classification", "Luminal B tumors show:",
  ["ER+, PR+ with HER2 - and Ki-67 ↑, or HER2 + with any Ki-67", "ER-, PR-, HER2+", "All negative with CK5/6+", "ER+ PR- HER2- always"], 0,
  "Luminal B: + + - ↑ -; or + + + Any -. (Book p58)")
q(58, "Molecular Classification", "HER2 enriched tumors are:",
  ["ER -, PR -, HER2 +, any Ki-67", "ER +, PR +, HER2 -", "Triple negative with CK5/6 +", "ER +, PR +, HER2 +"], 0,
  "HER2 enriched: - - + Any -. (Book p58)")
q(58, "Molecular Classification", "Basal like tumors are:",
  ["ER -, PR -, HER2 -, Ki-67 any (usually ↑), cytokeratin 5/6 +", "ER +, PR +, HER2 -", "HER2 +", "CK5/6 -"], 0,
  "Basal like: - - - Any (Usually ↑); Cytokeratin 5 and 6 +. (Book p58)")
q(58, "Molecular Classification", "Claudin low type tumors show:",
  ["ER -, PR -, HER2 -, any Ki-67, CK5/6 -", "ER +, PR +", "HER2 +", "CK5/6 +"], 0,
  "Claudin low type: - - - Any; CK5/6 -. (Book p58)")
q(58, "Molecular Classification", "Basal like/classical triple negative breast cancer is:",
  ["Most aggressive with high recurrence rate and worst prognosis", "Best prognosis", "Seen in elderly", "Low rate of mets"], 0,
  "Basal like/classical triple negative: most aggressive, high recurrence rate; Worst prognosis. (Book p58)")
q(58, "Molecular Classification", "Triple negative breast cancer typically affects which age group?",
  ["Young", "Elderly only", "Post-menopausal only", "Children"], 0,
  "TNBC: Age: Young. (Book p58)")
q(58, "Molecular Classification", "The 'TNBC paradox' is that triple negative breast cancer:",
  ["Responds best to chemo despite worst prognosis", "Never responds to chemo", "Responds to tamoxifen", "Is always curable by surgery"], 0,
  "TNBC paradox: Respond best to chemo. (Book p58)")
q(58, "Molecular Classification", "The positive cytokeratin marker of basal like/triple negative tumors is:",
  ["Cytokeratin 5/6 +ve", "Cytokeratin 7", "Cytokeratin 20", "Cytokeratin 5/6 -ve"], 0,
  "Basal like: Cytokeratin 5/6 +ve. (Book p58)")

# ---------------- p59 · TNM STAGING & 8th AJCC ----------------
q(59, "TNM Staging", "In TNM staging, T, N and M stand for:",
  ["Tumor size, Lymph node status, Distant mets", "Tumor type, Node count, Metastasis site", "Tumor grade, Necrosis, Mitoses", "Thickness, Nodes, Markers"], 0,
  "TNM staging: T: Tumor size; N: Lymph node status; M: Distant mets. (Book p59)")
q(59, "TNM Staging", "cTNM, pTNM and rTNM denote:",
  ["Clinical, Pathological, Recurrent", "Core, Punch, Radical", "Central, Peripheral, Regional", "Chemo, Radio, Surgical"], 0,
  "cTNM: Clinical; pTNM: Pathological; rTNM: Recurrent. (Book p59)")
q(59, "TNM Staging", "mTNM and yTNM denote:",
  ["Multiple tumors; after neoadjuvant therapy (Chemo/Radio prior to sx)", "Metastatic; young", "Male; year of diagnosis", "Microscopic; yearly"], 0,
  "mTNM: Multiple tumors; yTNM: After neoadjuvant therapy (Chemo/Radio prior to sx). (Book p59)")
q(59, "TNM Staging", "The quadrant with maximum glandular tissue and the m/c site for breast cancer is the:",
  ["Upper outer quadrant (UOQ)", "Upper inner quadrant (UIQ)", "Lower inner quadrant (LIQ)", "Lower outer quadrant (LOQ)"], 0,
  "Max glandular tissue: m/c site for cancer = UOQ. (Book p59)")
q(59, "TNM Staging", "The quadrant with the least incidence of breast cancer is the:",
  ["LIQ", "UOQ", "UIQ", "LOQ"], 0,
  "Least incidence of cancer: LIQ. (Book p59)")
q(59, "8th AJCC: T", "Tis (cancer in situ) includes:",
  ["DCIS and Paget's disease", "LCIS only", "Invasive ductal", "Tubular cancer"], 0,
  "Tis: Cancer in situ: DCIS; Paget's disease. (Book p59)")
q(59, "8th AJCC: T", "T1, T2 and T3 breast tumors are sized:",
  ["≤2 cm, 2-5 cm, >5 cm", "≤1 cm, 1-3 cm, >3 cm", "≤2 cm, 2-4 cm, >4 cm", "≤3 cm, 3-6 cm, >6 cm"], 0,
  "T1: ≤2 cm; T2: 2-5 cm; T3: >5 cm. (Book p59)")
q(59, "8th AJCC: T", "T4a breast cancer involves the:",
  ["Chest wall: serratus anterior, ribs, intercostal muscles", "Skin only", "Nipple only", "Pectoralis major"], 0,
  "T4a: Involvement of chest wall -> Serratus anterior, ribs, intercostal muscles. (Book p59)")
q(59, "8th AJCC: T", "T4b breast cancer involves the skin with:",
  ["Ulceration, direct infiltration, peau d'orange, satellite nodules", "Dimpling only", "Nipple retraction only", "Erythema only"], 0,
  "T4b: Involvement of skin -> Ulceration, direct infiltration, peau d'orange, satellite nodules. (Book p59)")
q(59, "8th AJCC: T", "T4c and T4d respectively are:",
  ["T4a + T4b; inflammatory cancer", "T4a only; Paget's", "T4b only; DCIS", "Tis + T1; lobular"], 0,
  "T4c: T4a + T4b; T4d: Inflammatory cancer. (Book p59)")
q(59, "8th AJCC: N", "N1 breast cancer denotes:",
  ["Palpable mobile ipsilateral axillary nodes", "Fixed ipsilateral axillary nodes", "No regional node metastasis", "Supraclavicular nodes"], 0,
  "N1: Palpable mobile ipsilateral axillary nodes. (Book p59)")
q(59, "8th AJCC: N", "N2a and N2b respectively denote:",
  ["Fixed ipsilateral axillary nodes; internal mammary LN in absence of axillary LN", "Mobile axillary nodes; supraclavicular nodes", "Infraclavicular nodes; internal mammary nodes", "No nodes; single node"], 0,
  "N2a: Fixed ipsilateral axillary nodes; N2b: Presence of internal mammary lymph node in absence of axillary lymph node (LN). (Book p59)")
q(59, "8th AJCC: N", "N3a, N3b and N3c respectively denote:",
  ["Ipsilateral infraclavicular LN; internal mammary + axillary LN; ipsilateral supraclavicular LN", "Axillary levels I-III", "Fixed axillary; mobile axillary; internal mammary", "Supraclavicular; infraclavicular; axillary"], 0,
  "N3a: Ipsilateral infraclavicular LN; N3b: Internal mammary + Axillary LN; N3c: Ipsilateral supraclavicular LN. (Book p59)")
q(59, "8th AJCC: M", "M0 and M1 denote:",
  ["No distant mets; distant mets", "Distant mets; no mets", "Micro mets; macro mets", "Bone only; visceral"], 0,
  "M0: No distant mets; M1: Distant mets. (Book p59)")
q(59, "Metastases Notes", "The m/c site of breast cancer metastasis is bones (lumbar vertebrae) because of:",
  ["Batson plexus of valveless veins", "Arterial embolism", "Lymphatic spread only", "Direct extension"], 0,
  "M/c site of mets: Bones: Lumbar vertebrae d/t Batson plexus of valveless veins. (Book p59)")
q(59, "Metastases Notes", "Breast cancer bone metastases are typically:",
  ["Osteolytic > Osteoblastic", "Osteoblastic > Osteolytic", "Purely sclerotic", "Mixed equal"], 0,
  "Breast: Osteolytic > Osteoblastic. (Book p59)")
q(59, "Metastases Notes", "In prostate cancer, bone (lumbar vertebrae) metastases are:",
  ["Osteoblastic > Osteolytic", "Osteolytic > Osteoblastic", "Always lytic", "Never in bone"], 0,
  "Note: Prostate cancer: m/c site of mets are bone (Lumbar vertebrae); Osteoblastic > Osteolytic. (Book p59)")

# ---------------- p60 · IMPORTANT POINTS & PET-CT ----------------
q(60, "Important Points", "As per the book, LCIS is:",
  ["A benign disease with a risk of cancer, no longer in situ cancer", "An invasive cancer", "A variant of DCIS", "A surgical emergency"], 0,
  "LCIS is a benign disease with a risk of cancer, no longer in situ cancer. (Book p60)")
q(60, "Important Points", "Pectoral muscle involvement is:",
  ["Not considered in T4a", "Considered in T4a", "Considered in T4b", "Considered in T1"], 0,
  "Pectoral muscle involvement: Not considered in T4a. (Book p60)")
q(60, "Important Points", "Dimpling & retraction are:",
  ["Not considered in T4b", "Considered in T4b", "Considered in T4d", "Considered in Tis"], 0,
  "Dimpling & retraction: Not considered in T4b. (Book p60)")
q(60, "Important Points", "Contralateral (C/L) lymph node involvement is considered metastatic when:",
  ["The other breast does not have cancer", "The other breast also has cancer", "Always", "Never"], 0,
  "C/L LN: Considered metastatic (When other breast does not have cancer). (Book p60)")
q(60, "PET-CT", "PET-CT is the IOC for:",
  ["Staging", "Initial diagnosis of a lump", "Screening average risk women", "Biopsy guidance"], 0,
  "PET-CT: IOC for staging. (Book p60)")
q(60, "PET-CT", "The dye used in PET-CT and its half-life are:",
  ["18 FDG (Fluorodeoxyglucose), T½ 110 mins", "99mTc, T½ 6 hours", "Iodine-131, T½ 8 days", "Gadolinium, T½ 90 mins"], 0,
  "Dye: 18 FDG (Fluorodeoxyglucose); T½: 110 mins. (Book p60)")
q(60, "PET-CT", "PET-CT is not sensitive for the brain; the IOC for brain metastases is:",
  ["MRI", "CT", "X-ray", "USG"], 0,
  "PET CT is not sensitive for brain; Brain mets: IOC -> MRI. (Book p60)")
q(60, "PET-CT", "For prostate cancer, the PET done is:",
  ["PSMA PET (Prostate specific membrane antigen PET)", "18 FDG PET", "DOTATATE PET", "Choline PET only"], 0,
  "Prostate: PSMA PET (Prostate specific membrane antigen PET) is done. (Book p60)")

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
    ("Risk Factors for Breast Cancer", ("Risk Factors",),
     "Estrogen exposure drives risk: rising age, early menarche, late menopause, nulliparity and first birth after 30, plus obesity (aromatase converts peripheral fat to estrogen), alcohol, smoking, maternal and paternal family history and HRT."),
    ("Dupont & Page Classification", ("Dupont & Page Classification",),
     "Pre-existing lesions stratify risk: nonproliferative lesions, cysts, mild hyperplasia and columnar cell change carry no risk (1); proliferative without atypia (sclerosing adenosis, radial scar, intraductal papilloma, complex fibroadenoma) 1.3-1.9; atypical hyperplasias 4-5; carcinoma in-situ 9."),
    ("Smokers, Protective Factors & OCPs", ("Notes: Smokers & Protective",),
     "Smokers face more breast cancer, duct ectasia and Mondor's disease, while first birth by 20 and breastfeeding beyond a year protect. Low dose OCPs do not raise risk."),
    ("Genes Associated with Breast Cancer", ("Genes Associated",),
     "Only 10% of breast cancer is familial. p53 is the commonest mutation overall and in TNBC/HER2-positive disease, BRCA1 rules familial cases, and PIK3CA marks ER/PR-positive tumors."),
    ("BRCA Genes & Testing Indications", ("BRCA Genes & Testing",),
     "BRCA1 (17q, aggressive, basal/medullary) and BRCA2 (13q, luminal) cause HBOC syndrome: breast-ovarian risk favours BRCA1, pancreatic/prostate/male breast favours BRCA2, colorectal/peritoneal equal. Test everyone with a deleterious family mutation or ovarian/fallopian/peritoneal history, and every breast cancer patient with a relative ≤45, bilateral disease ≤50, TNBC ≤60 or male breast cancer; carriers lose weight, exercise, quit smoking/alcohol and start MRI at 25."),
    ("Risk Reduction Strategies", ("Risk Reduction Strategies",),
     "Bilateral prophylactic mastectomy cuts risk 95% sparing skin and nipple; salpingo-oophorectomy after family completion (by 40) cuts ovarian risk 90% (leaving 10% fallopian/peritoneal) and breast risk 50%; tamoxifen (SERM) trims 47%."),
    ("Biopsy & Histological Types", ("Biopsy & Histological Types",),
     "Core needle biopsy is IOC, typing ductal (invasive m/c) vs lobular disease and feeding IHC for biology. Invasive ductal carcinoma (NOS) dominates; tubular, mucinous and medullary (BRCA1-linked) are the special types."),
    ("IHC: ER/PR, HER2 & Ki67", ("IHC",),
     "ER/PR are nuclear receptors scored by Allred 0-8; HER2 is membranous with 0/1+ negative, 3+ positive and 2+ equivocal sent to FISH (amplified = positive), the brown stain coming from DAB. Ki67 marks the proliferation index."),
    ("Molecular Classification & TNBC", ("Molecular Classification",),
     "Gene expression profiling splits breast cancer into luminal A (m/c, best prognosis, ER+PR+HER2-, low Ki67), luminal B, HER2-enriched, claudin-low and basal-like - triple negative, CK5/6 positive, young patients, most aggressive with the worst prognosis yet the TNBC paradox: it responds best to chemotherapy."),
    ("TNM & 8th AJCC Staging", ("TNM Staging", "8th AJCC: T", "8th AJCC: N", "8th AJCC: M"),
     "T sizes run ≤2/2-5/>5 cm after Tis (DCIS, Paget's); T4a is chest wall (serratus, ribs, intercostals - not pectoralis), T4b skin (ulceration, infiltration, peau d'orange, satellites - not dimpling), T4c both, T4d inflammatory. N1 mobile axillary, N2a fixed axillary, N2b internal mammary without axillary, N3a infraclavicular, N3b internal mammary + axillary, N3c supraclavicular; UOQ is the commonest site and LIQ the rarest."),
    ("Metastases, Important Points & PET-CT", ("Metastases Notes", "Important Points", "PET-CT"),
     "Breast spreads to lumbar vertebrae through Batson's valveless plexus with osteolytic > osteoblastic lesions (prostate reverses this). LCIS is now a benign risk lesion, and PET-CT with 18 FDG (T½ 110 min) is IOC for staging except in brain (MRI) and prostate (PSMA PET)."),
]

UNITS = []
for i, (title, labels, guide) in enumerate(UNIT_DEFS, 1):
    UNITS.append({"id": f"SURG-U10-{i}", "ch": 10, "n": i, "title": title,
                  "sec": f"{labels[0]} \u00b7 p{first_page(labels[0])}",
                  "qs": sec_ids(*labels), "guide": guide})

covered = [i for u in UNITS for i in u["qs"]]
assert covered == [x["id"] for x in Q], "units must cover questions in order"

data = {"questions": Q, "units": UNITS}
with open("data/ch10.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
print(f"ch10: {len(Q)} questions, {len(UNITS)} units")
