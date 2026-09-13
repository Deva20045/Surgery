#!/usr/bin/env python3
"""Build data/ch15.json for PULSE Surgery ch15 (Thyroid : Part 2, book p90-101)."""
import json

Q = []
def q(page, sec, text, opts, ans, exp):
    Q.append({"id": f"SURG-C15-{len(Q)+1:03d}", "sec": sec, "page": page,
              "q": text, "opts": opts, "ans": ans, "exp": exp})

# ---------------- p90 · THYROID CANCERS: IOC & SYNDROMES ----------------
q(90, "Thyroid Cancers: IOC & Syndromes", "The IOC (investigation of choice) for thyroid cancers is:",
  ["FNAC", "USG neck", "CT neck", "TFT"], 0,
  "IOC: FNAC. (Book p90)")
q(90, "Thyroid Cancers: IOC & Syndromes", "Medullary thyroid cancer is associated with which syndrome and gene?",
  ["MEN2 / RET", "MEN1 / Menin", "Cowden / PTEN", "Werner / WRN"], 0,
  "Medullary: MEN2 syndrome; Gene: RET. (Book p90)")
q(90, "Thyroid Cancers: IOC & Syndromes", "Cowden syndrome (↑ risk of breast & thyroid cancer, benign GI polyps) is associated with which histology and gene?",
  ["Follicular / PTEN (Ch 10)", "Papillary / AP (Ch 5)", "Medullary / RET", "Papillary / PRKAR1A"], 0,
  "Follicular: Cowden syndrome (↑ breast & thyroid cancer risk, GI polyps benign) - PTEN gene: Ch 10. (Book p90)")
q(90, "Thyroid Cancers: IOC & Syndromes", "Werner/adult progeroid syndrome (follicular cancer association) involves which gene?",
  ["WRN", "RET", "PTEN", "PRKAR1A"], 0,
  "Werner/Adult progeroid syndrome: WRN gene. (Book p90)")
q(90, "Thyroid Cancers: IOC & Syndromes", "Familial adenomatous polyposis (≥100 polyps, 100% colorectal cancer risk) is associated with which thyroid histology?",
  ["Papillary", "Follicular", "Medullary", "Anaplastic"], 0,
  "Papillary associations: FAP (≥100 polyps, 100% colorectal cancer risk), Cowden, Carney complex, familial non-medullary & familial papillary syndromes. (Book p90)")
q(90, "Thyroid Cancers: IOC & Syndromes", "Carney complex is also known as:",
  ["Batman's syndrome", "Sipple syndrome", "Wermer syndrome", "MEN3 syndrome"], 0,
  "Carney complex/Batman's syndrome - papillary association. (Book p90)")
q(90, "Thyroid Cancers: IOC & Syndromes", "The AP gene (FAP) is on which chromosome, and PRKAR1A links to which histology?",
  ["Ch 5 / papillary", "Ch 10 / follicular", "Ch 11 / medullary", "Ch 12 / anaplastic"], 0,
  "Papillary genes: AP gene Ch 5, PTEN, PRKAR1A. (Book p90)")

# ---------------- p90 · TNM STAGING ----------------
q(90, "TNM Staging", "T1 thyroid tumor size is:",
  ["≤ 2 cm", "≤ 1 cm", "> 2 but ≤ 4 cm", "> 4 cm"], 0,
  "T1: Tumor ≤ 2cm (T1a ≤ 1cm; T1b > 1cm but ≤ 2cm). (Book p90)")
q(90, "TNM Staging", "T1b thyroid tumor is:",
  ["Tumor > 1 cm but ≤ 2 cm", "Tumor ≤ 1 cm", "Tumor > 2 but ≤ 4 cm", "Tumor > 4 cm"], 0,
  "T1b: Tumor > 1cm but ≤ 2cm. (Book p90)")
q(90, "TNM Staging", "T2 thyroid tumor is:",
  ["Tumor > 2 cm but ≤ 4 cm", "Tumor ≤ 2 cm", "Tumor > 4 cm limited to thyroid", "Any size invading strap muscles"], 0,
  "T2: Tumor > 2cm but ≤ 4cm. (Book p90)")
q(90, "TNM Staging", "T3a thyroid tumor is:",
  ["Tumor > 4 cm limited to thyroid", "Tumor > 4 cm with strap muscle invasion", "Gross extrathyroidal extension", "Tumor ≤ 4 cm"], 0,
  "T3a: Tumor > 4cm limited to thyroid. (Book p90)")
q(90, "TNM Staging", "T3b (recent update) is a tumor of:",
  ["Any size invading only strap muscles", "Any size invading trachea", "> 4 cm limited to thyroid", "Any size with major neck structure invasion"], 0,
  "T3b: Tumor of any size invading ONLY strap muscles (recent update). (Book p90)")
q(90, "TNM Staging", "T4 thyroid tumor denotes:",
  ["Gross extrathyroidal extension into major neck structures", "Strap muscle invasion only", "Tumor > 4 cm limited to thyroid", "Substernal extension only"], 0,
  "T4: Gross extrathyroidal extension into major neck structures. (Book p90)")
q(90, "TNM Staging", "N1 in thyroid cancer means:",
  ["Metastasis to regional nodes", "No regional LN metastasis", "Regional LN can't be assessed", "Distant metastasis"], 0,
  "N1: Metastasis to regional nodes (N0 none; Nx can't be assessed). (Book p90)")
q(90, "TNM Staging", "M1 in thyroid cancer means:",
  ["Distant metastasis (+)", "No distant metastasis", "Regional nodes (+)", "Tumor can't be assessed"], 0,
  "M0: No distant metastasis; M1: Distant metastasis (+). (Book p90)")

# ---------------- p91 · DTC & UPDATES ----------------
q(91, "DTC & Updates", "Differentiated thyroid cancer (DTC) includes:",
  ["Papillary, follicular & Hurthle cell cancers", "Papillary & anaplastic only", "Medullary & follicular", "Anaplastic & Hurthle cell"], 0,
  "DTC: Papillary, follicular, Hurthle cell - arise from thyroid epithelial cells & take up iodine. (Book p91)")
q(91, "DTC & Updates", "DTC diagnosed at <55 years carries:",
  ["Good prognosis", "Bad prognosis", "No prognostic meaning", "Worse prognosis than >55"], 0,
  "Updates: DTC Dx by age - <55 yrs good prognosis; >55 yrs bad prognosis. (Book p91)")
q(91, "DTC & Updates", "Which cancer (previously staged T4) is now staged the same as DTC?",
  ["Anaplastic cancer", "Medullary cancer", "Thyroid lymphoma", "Hurthle cell cancer"], 0,
  "Anaplastic cancer (previously T4): staged same as DTC. (Book p91)")

# ---------------- p91 · PTC: RISK FACTORS & GENETICS ----------------
q(91, "PTC: Risk Factors & Genetics", "The most common thyroid cancer is:",
  ["Papillary", "Follicular", "Medullary", "Anaplastic"], 0,
  "PTC: m/c thyroid cancer with BEST prognosis. (Book p91)")
q(91, "PTC: Risk Factors & Genetics", "Which is NOT a listed risk factor for PTC?",
  ["Iodine deficiency", "Radiation exposure", "Family history", "Obesity"], 0,
  "Risk factors: 1. Radiation exposure; 2. Family history; 3. Obesity (iodine deficiency is FTC's). (Book p91)")
q(91, "PTC: Risk Factors & Genetics", "Radiation exposure risk includes all EXCEPT:",
  ["Radioiodine ablation therapy at old age", "Nuclear fall out", "Post radiotherapy of head & neck", "Radioiodine ablation therapy at young age"], 0,
  "Radiation: nuclear fall out, post radiotherapy head & neck, radioiodine ablation at YOUNG age. (Book p91)")
q(91, "PTC: Risk Factors & Genetics", "PTC genes exposed to radiation are:",
  ["More aggressive", "Less aggressive", "Unchanged", "Radioresistant"], 0,
  "PTC genes exposed to radiation are more aggressive. (Book p91)")
q(91, "PTC: Risk Factors & Genetics", "The most common (m/c) mutation in PTC is:",
  ["BRAF", "GDNF", "RET/PTC", "P53"], 0,
  "Genetics: mutation of BRAF (m/c), GDNF, RET/PTC. (Book p91)")
q(91, "PTC: Risk Factors & Genetics", "GDNF stands for:",
  ["Glial derived neurotrophic factor", "Glandular derived neoplastic factor", "Glial derived neoplastic factor", "Gonadal derived neurotrophic factor"], 0,
  "GDNF: Glial derived neurotrophic factor. (Book p91)")
q(91, "PTC: Risk Factors & Genetics", "The female:male ratio and decade for PTC are:",
  ["3:1, 3rd-5th decade", "1:3, 3rd-5th decade", "3:1, 6th-7th decade", "2:1, 5th-7th decade"], 0,
  "Incidence: Female:male = 3:1; 3rd-5th decade. (Book p91)")

# ---------------- p91-92 · PTC: CLINICAL FEATURES & SPREAD ----------------
q(91, "PTC: Clinical Features & Spread", "The most common presentation of PTC is:",
  ["Thyroid swelling", "Hoarseness", "Stridor", "Weight loss"], 0,
  "Thyroid swelling: m/c presentation; B/L multicentric → Rx: total thyroidectomy. (Book p91)")
q(92, "PTC: Clinical Features & Spread", "The FIRST lymphatic spread of PTC is to:",
  ["Level 6 lymph nodes (central compartment/delphian)", "Level 3 nodes", "Mediastinal nodes", "Retropharyngeal nodes"], 0,
  "Lymphatic: Level 6 lymph nodes 1st (central compartment/delphian lymph nodes). (Book p92)")
q(92, "PTC: Clinical Features & Spread", "The most common site of haematogenous spread in PTC is:",
  ["Lungs", "Liver", "Bone", "Brain"], 0,
  "Haematogenous: Lungs (m/c). (Book p92)")
q(92, "PTC: Clinical Features & Spread", "Lateral aberrant thyroid is:",
  ["Level 6 LN enlargement (d/t PTC) with non-palpable thyroid", "Ectopic lateral thyroid tissue", "A lateral thyroglossal cyst", "Metastatic follicular carcinoma"], 0,
  "Lateral aberrant thyroid: level 6 LN enlargement (d/t PTC) & non-palpable thyroid. (Book p92)")
q(92, "PTC: Clinical Features & Spread", "A thyroid incidentaloma is:",
  ["Incidental Dx, size < 1 cm", "Always malignant", "Size > 2 cm", "A palpable nodule"], 0,
  "Thyroid incidentaloma: incidental Dx; size < 1cm. (Book p92)")

# ---------------- p92 · PTC: DIAGNOSIS & HISTOLOGY ----------------
q(92, "PTC: Diagnosis & Histology", "The IOC for diagnosing PTC is:",
  ["FNAC", "Core biopsy", "CT", "Thyroglobulin"], 0,
  "Ix: FNAC = IOC. (Book p92)")
q(92, "PTC: Diagnosis & Histology", "'Orphan Annie eyed'/coffee bean nuclei on H&E indicate:",
  ["Papillary thyroid carcinoma", "Follicular carcinoma", "Medullary carcinoma", "Anaplastic carcinoma"], 0,
  "Orphan Annie eyed/coffee bean nuclei - PTC. (Book p92)")
q(92, "PTC: Diagnosis & Histology", "Pseudo (intranuclear) inclusions are a feature of:",
  ["PTC", "FTC", "MTC", "Lymphoma"], 0,
  "Pseudo (intranuclear) inclusions - PTC. (Book p92)")
q(92, "PTC: Diagnosis & Histology", "Psammoma bodies are:",
  ["Foci of dystrophic calcification", "Foci of amyloid", "Intranuclear inclusions", "Colloid-filled follicles"], 0,
  "Psammoma bodies: foci of dystrophic calcification. (Book p92)")
q(92, "PTC: Diagnosis & Histology", "Psammoma bodies are seen in all EXCEPT:",
  ["Follicular thyroid carcinoma", "PTC", "Serous cystadenoma of ovary", "Meningioma"], 0,
  "Psammoma bodies: PTC, serous cystadenoma of ovary, papillary RCC, meningioma. (Book p92)")

# ---------------- p93 · PTC: SURGICAL OPTIONS ----------------
q(93, "PTC: Surgical Options", "Hemithyroidectomy criteria include all of the following EXCEPT:",
  ["Extrathyroidal spread", "Low risk", "U/L", "1-4 cm"], 0,
  "Hemithyroidectomy: ALL of - low risk, U/L, 1-4 cm, NO extrathyroidal spread. (Book p93)")
q(93, "PTC: Surgical Options", "Minimum total thyroidectomy is indicated for all EXCEPT:",
  ["Unilateral low-risk 2 cm tumor", "Radiation induced DTC", "Familial non-medullary thyroid cancer", "Multifocal B/L DTC"], 0,
  "Minimum total thyroidectomy: radiation induced DTC, familial non-medullary TC, multifocal B/L DTC, extrathyroid extension. (Book p93)")
q(93, "PTC: Surgical Options", "Prophylactic central neck dissection (total thyroidectomy + CND) is done for:",
  ["T3, T4 tumors", "T1a tumors", "Benign nodules", "Incidentaloma only"], 0,
  "Total thyroidectomy + CND (level 6 LN removal): T3, T4 (prophylactic CND done); level 6 LN (+). (Book p93)")
q(93, "PTC: Surgical Options", "Total thyroidectomy + CND + modified radical neck dissection (U/L or B/L) is for:",
  ["PTC involving level 6 + other neck LN", "T1 tumors", "Prophylactic cases", "FTC adenoma"], 0,
  "Total + CND + MRND (U/L/B/L): PTC involving level 6 + other neck LN. (Book p93)")

# ---------------- p93-94 · WHOLE BODY IODINE SCAN & RIA ----------------
q(93, "Whole Body Iodine Scan & RIA", "The prerequisite TSH level for a whole body iodine scan is:",
  ["TSH > 30 (to enhance iodine uptake)", "TSH < 0.1", "TSH 5-10", "Normal TSH"], 0,
  "Prerequisite: TSH > 30 to enhance iodine uptake. (Book p93)")
q(93, "Whole Body Iodine Scan & RIA", "In the traditional method of raising TSH, thyroxine is not supplemented for 4-6 weeks; the disadvantage is:",
  ["Patient suffers hypothyroidism for 4-6 weeks", "Risk of thyrotoxicosis", "False positive scans", "Hypertensive crisis"], 0,
  "Traditional: wait 4-6 weeks post Sx, don't supplement thyroxine - patient suffers hypothyroidism 4-6 weeks. (Book p93)")
q(93, "Whole Body Iodine Scan & RIA", "The alternative to thyroxine withdrawal for raising TSH is:",
  ["Recombinant TSH injections", "High-dose thyroxine", "Pentagastrin", "ACTH infusion"], 0,
  "Recombinant TSH injections avoid withdrawal hypothyroidism. (Book p93)")
q(94, "Whole Body Iodine Scan & RIA", "A positive whole body iodine scan (residual disease/mets) is treated with:",
  ["Radioiodine ablation (RIA)", "TSH suppression only", "External beam RT", "Chemotherapy"], 0,
  "(+) scan → Rx: Radioiodine ablation (RIA). (Book p94)")
q(94, "Whole Body Iodine Scan & RIA", "RIA uses I-131 which acts via:",
  ["β rays", "α rays", "γ rays", "Auger electrons"], 0,
  "I131 acts via β rays. (Book p94)")
q(94, "Whole Body Iodine Scan & RIA", "The half life of I-131 is:",
  ["7-8 days", "7-8 hours", "70 days", "48 hours"], 0,
  "I131 ½ life: 7-8 days. (Book p94)")
q(94, "Whole Body Iodine Scan & RIA", "Indications for RIA include all EXCEPT:",
  ["Normal thyroglobulin with negative scan", "Residual disease", "Metastases", "Persistently high thyroglobulin after Sx"], 0,
  "RIA indications: residual disease, metastases, +ve lymph nodes, persistently high thyroglobulin after Sx. (Book p94)")
q(94, "Whole Body Iodine Scan & RIA", "A negative scan is managed with TSH suppression to the lower limit of normal using:",
  ["Thyroxine", "Propylthiouracil", "Carbimazole", "Radioiodine"], 0,
  "(-) scan → TSH suppression to lower limit of N: thyroxine (↓ recurrence of PTC). (Book p94)")
q(94, "Whole Body Iodine Scan & RIA", "Life-long follow-up of DTC uses USG neck plus which tumor marker, checked 6-monthly?",
  ["S. thyroglobulin", "Calcitonin", "CEA", "CA-125"], 0,
  "Life-long follow-up: USG neck + S. thyroglobulin (tumor marker for DTC) 6-monthly. (Book p94)")
q(94, "Whole Body Iodine Scan & RIA", "S. thyroglobulin is NOT a reliable marker if:",
  ["Anti-Tg antibodies are (+)", "TSH is suppressed", "Patient is on thyroxine", "Scan is negative"], 0,
  "Not reliable if anti-Tg antibodies (+). (Book p94)")

# ---------------- p94 · RADIOIODINE RESISTANT DTC & LINDSEY TUMOR ----------------
q(94, "Radioiodine Resistant DTC & Lindsey Tumor", "Immunotherapy (targeted therapy) for radioiodine-resistant DTC includes:",
  ["Sorafenib, lenvatinib", "Dabrafenib", "Vandetinib", "Doxorubicin"], 0,
  "RAI-resistant DTC: 1. Immunotherapy sorafenib, lenvatinib; 2. EBRT; 3. Chemo doxorubicin. (Book p94)")
q(94, "Radioiodine Resistant DTC & Lindsey Tumor", "The chemotherapy drug for radioiodine-resistant DTC is:",
  ["Doxorubicin", "Cisplatin", "Methotrexate", "5-FU"], 0,
  "Chemotherapy: doxorubicin. (Book p94)")
q(94, "Radioiodine Resistant DTC & Lindsey Tumor", "Lindsey tumor is:",
  ["Follicular variety of papillary with similar prognosis as PTC", "A variant of FTC with poor prognosis", "Medullary cancer in MEN2", "Anaplastic cancer post-radiation"], 0,
  "Lindsey tumor: follicular variety of papillary; similar prognosis as PTC. (Book p94)")

# ---------------- p94-95 · FTC: BASICS, FEATURES & SPREAD ----------------
q(94, "FTC: Basics, Features & Spread", "The second most common thyroid cancer is:",
  ["Follicular", "Papillary", "Medullary", "Hurthle cell"], 0,
  "FTC: 2nd m/c thyroid cancer; m/c cancer in iodine deficient areas. (Book p94)")
q(94, "FTC: Basics, Features & Spread", "FTC genetics shows upregulation of miRNA:",
  ["197, 346", "17-92", "21, 155", "197 only"], 0,
  "Genetics: upregulation of miRNA-197, 346; mutation of PTEN & BAX gene. (Book p94)")
q(94, "FTC: Basics, Features & Spread", "The genes mutated in FTC are:",
  ["PTEN & BAX", "BRAF & RET", "P53 & B-catenin", "K-RAS & WRN"], 0,
  "Mutation of PTEN & BAX gene. (Book p94)")
q(95, "FTC: Basics, Features & Spread", "The risk factor for FTC is:",
  ["Long standing multinodular goitre", "Radiation", "Hashimoto's thyroiditis", "Obesity"], 0,
  "Risk factor: long standing multinodular goitre; Females > males. (Book p95)")
q(95, "FTC: Basics, Features & Spread", "Pressure symptoms in FTC: trachea causes stridor and RLN causes:",
  ["Hoarseness", "Stridor", "Dysphagia", "Ptosis"], 0,
  "Pressure: trachea → stridor; RLN → hoarseness. (Book p95)")
q(95, "FTC: Basics, Features & Spread", "Haematogenous spread of FTC classically produces:",
  ["Pulsatile bony mets (highly vascular, osteolytic > osteoblastic)", "Sclerotic bony mets", "Liver mets first", "Brain mets first"], 0,
  "Haematogenous: pulsatile bony mets - highly vascular; osteolytic > osteoblastic. (Book p95)")

# ---------------- p95-96 · FTC: DX/MX & HURTHLE CELL CARCINOMA ----------------
q(95, "FTC: Dx, Mx & Hurthle Cell Carcinoma", "FNAC in FTC reports:",
  ["Follicular neoplasm (Thy 3)", "Papillary carcinoma", "Benign colloid", "Anaplastic"], 0,
  "FNAC: follicular neoplasm (Thy 3). (Book p95)")
q(95, "FTC: Dx, Mx & Hurthle Cell Carcinoma", "FNAC cannot differentiate:",
  ["Follicular adenoma vs carcinoma", "PTC vs FTC", "MTC vs lymphoma", "Benign vs colloid"], 0,
  "Cannot differentiate follicular adenoma vs carcinoma on FNAC. (Book p95)")
q(95, "FTC: Dx, Mx & Hurthle Cell Carcinoma", "The adenoma vs carcinoma distinction is made by:",
  ["Hemithyroidectomy → frozen section", "FNAC repeat", "Iodine scan", "Serum thyroglobulin"], 0,
  "Hemithyroidectomy → frozen section: cancer → mx same as PTC; adenoma → no mx. (Book p95)")
q(95, "FTC: Dx, Mx & Hurthle Cell Carcinoma", "FTC prognosis compared to PTC is:",
  ["Slightly poorer", "Better", "Identical", "Worst of all"], 0,
  "Prognosis: slightly poorer than PTC. (Book p95)")
q(95, "FTC: Dx, Mx & Hurthle Cell Carcinoma", "Hurthle cell carcinoma presents in which decade and the cells are rich in:",
  ["6th-7th decade, mitochondria", "3rd-5th decade, mitochondria", "6th-7th decade, amyloid", "5th-7th decade, colloid"], 0,
  "Hurthle cell carcinoma: 6th-7th decade; oxyphilic Hurthle cells rich in mitochondria. (Book p95)")
q(95, "FTC: Dx, Mx & Hurthle Cell Carcinoma", "Compared to other DTC, Hurthle cell carcinoma is:",
  ["Less radioactive avid & more aggressive", "More radioactive avid", "Less aggressive", "Always benign"], 0,
  "More aggressive than FTC; LESS radioactive avid than other DTC; mx same as PTC; prognosis poorer than FTC. (Book p95)")
q(96, "FTC: Dx, Mx & Hurthle Cell Carcinoma", "Hurthle cells are seen in all EXCEPT:",
  ["Riedel thyroiditis", "Hurthle cell carcinoma", "Hashimoto thyroiditis", "Thyroid lymphoma"], 0,
  "Hurthle cells seen in: Hurthle cell carcinoma, Hashimoto thyroiditis, thyroid lymphoma. (Book p96)")

# ---------------- p96 · PROGNOSTIC SCORES ----------------
q(96, "Prognostic Scores (AGES/AMES/MACIS)", "The AGES system comprises:",
  ["Age, histologic grade, extrathyroidal invasion, size", "Age, metastases, extrathyroidal spread, size", "Metastases, age, completeness of resection, invasion, size", "Age, grade, nodes, size"], 0,
  "AGES: Age, histologic Grade, Extrathyroidal invasion, Size. (Book p96)")
q(96, "Prognostic Scores (AGES/AMES/MACIS)", "The AMES system comprises:",
  ["Age, metastases, extrathyroidal spread, size of tumors", "Age, grade, extension, size", "Metastases, age, completeness, invasion, size", "Age, nodes, mets, size"], 0,
  "AMES: Age, Metastases, Extrathyroidal spread, Size of tumors. (Book p96)")
q(96, "Prognostic Scores (AGES/AMES/MACIS)", "The 'C' (completeness of original surgical resection - post op criteria) belongs to:",
  ["MACIS", "AGES", "AMES", "TNM"], 0,
  "MACIS: Metastases, Age, Completeness of original surgical resection (post op criteria), extrathyroidal invasion, size of original lesion. (Book p96)")

# ---------------- p96-97 · ANAPLASTIC CARCINOMA ----------------
q(96, "Anaplastic Carcinoma", "The least common thyroid cancer with the worst prognosis is:",
  ["Anaplastic", "Papillary", "Follicular", "Medullary"], 0,
  "Anaplastic: least common type; WORST prognosis. (Book p96)")
q(96, "Anaplastic Carcinoma", "Anaplastic carcinoma incidence peaks in:",
  ["5th-7th decade", "3rd-5th decade", "Childhood", "6th-7th decade"], 0,
  "Incidence: 5th-7th decade. (Book p96)")
q(96, "Anaplastic Carcinoma", "Anaplastic genetics shows:",
  ["miRNA 17-92 upregulation; mutation in p53 & B-catenin", "BRAF mutation", "RET/PTC", "PTEN & BAX"], 0,
  "Genetics: miRNA 17-92 upregulation; mutation in p53 & B-catenin. (Book p96)")
q(96, "Anaplastic Carcinoma", "Anaplastic neck swelling is characteristically:",
  ["Rapid ↑ in size, hard in consistency", "Soft and mobile", "Slow growing and cystic", "Tender and warm"], 0,
  "Neck swelling: rapid ↑ in size, hard in consistency; H/o multinodular goitre (follicular > anaplastic). (Book p96)")
q(96, "Anaplastic Carcinoma", "The important differential diagnosis of anaplastic carcinoma is:",
  ["Riedel thyroiditis (fibrosis of thyroid gland)", "Hashimoto thyroiditis", "Thyroid lymphoma", "De Quervain's"], 0,
  "D/D: Riedel thyroiditis (fibrosis of thyroid gland). (Book p96)")
q(96, "Anaplastic Carcinoma", "Spread of anaplastic carcinoma is predominantly:",
  ["Distant metastases: lungs (m/c)", "Lymphatic only", "Local only", "Bone only"], 0,
  "Spread: distant metastases - lungs (m/c). (Book p96)")
q(96, "Anaplastic Carcinoma", "FNAC in anaplastic carcinoma is often inconclusive; next step is:",
  ["USG guided core biopsy", "Repeat FNAC", "Iodine scan", "Empirical surgery"], 0,
  "FNAC inconclusive → USG guided core biopsy. (Book p96)")
q(97, "Anaplastic Carcinoma", "Staging of anaplastic carcinoma is:",
  ["Same as DTC", "Same as MTC", "Separate system", "Same as lymphoma"], 0,
  "Staging is same as DTC. (Book p97)")
q(97, "Anaplastic Carcinoma", "Localised anaplastic disease is managed aggressively with:",
  ["Total thyroidectomy + CND + modified radical neck dissection", "Hemithyroidectomy", "RIA alone", "Thyroxine suppression"], 0,
  "Localised: aggressive mx - Sx total thyroidectomy + CND + MRND. (Book p97)")
q(97, "Anaplastic Carcinoma", "In advanced anaplastic disease, isthmusectomy is done to:",
  ["↓ pressure over trachea", "Cure the disease", "Enable RIA", "Prevent hypocalcemia"], 0,
  "Advanced/metastatic: tumor debulking; isthmusectomy (↓ pressure over trachea); TKI dabrafenib (immunotherapy); chemotherapy. (Book p97)")
q(97, "Anaplastic Carcinoma", "The tyrosine kinase inhibitor named for advanced anaplastic cancer is:",
  ["Dabrafenib", "Sorafenib", "Vandetinib", "Lenvatinib"], 0,
  "Tyrosine kinase inhibitors: dabrafenib (immunotherapy). (Book p97)")

# ---------------- p97 · THYROID LYMPHOMA ----------------
q(97, "Thyroid Lymphoma", "The most common type of thyroid lymphoma is:",
  ["Diffuse large B cell lymphoma (DLBCL)", "Small blue cell lymphoma", "Hodgkin lymphoma", "Burkitt lymphoma"], 0,
  "Types: DLBCL (m/c); small blue cell. (Book p97)")
q(97, "Thyroid Lymphoma", "The risk factor for thyroid lymphoma is:",
  ["Long standing Hashimoto/lymphocytic thyroiditis", "Radiation", "Iodine deficiency", "MEN2"], 0,
  "Risk factor: long standing Hashimoto/lymphocytic thyroiditis; 5th-7th decade; rare. (Book p97)")
q(97, "Thyroid Lymphoma", "B symptoms of lymphoma include all EXCEPT:",
  ["Hypertension", "Weight loss", "Night sweats", "Fever"], 0,
  "B symptoms: weight loss, fever, night sweats, itching; thyroid swelling m/c. (Book p97)")
q(97, "Thyroid Lymphoma", "The investigation of choice for thyroid lymphoma is:",
  ["Core/trucut biopsy", "FNAC", "USG", "TFT"], 0,
  "Core/trucut biopsy (FNAC cannot characterize a lymphoma). (Book p97)")
q(97, "Thyroid Lymphoma", "The 1st line Rx of thyroid lymphoma is:",
  ["Chemotherapy (R-CHOP)", "Surgery", "RIA", "Thyroxine"], 0,
  "Chemotherapy 1st line Rx: R-CHOP. (Book p97)")
q(97, "Thyroid Lymphoma", "In R-CHOP, 'R' is rituximab which is a monoclonal antibody against:",
  ["CD20", "CD3", "CD5", "HER2"], 0,
  "R: rituximab (monoclonal antibody against CD20). (Book p97)")
q(97, "Thyroid Lymphoma", "In R-CHOP, 'H' and 'O' stand for:",
  ["Hydroxydaunorubicin; oncovin/vincristine", "Hydrocortisone; oxaliplatin", "Hydroxyurea; oncovin", "Hydroxydaunorubicin; oxaliplatin"], 0,
  "H: hydroxydaunorubicin; O: oncovin/vincristine; C cyclophosphamide; P prednisolone. (Book p97)")
q(97, "Thyroid Lymphoma", "Surgery in thyroid lymphoma is indicated:",
  ["Only in residual/recurrent disease", "As 1st line", "Never", "For diagnosis only"], 0,
  "Sx indication: only in residual/recurrent disease. (Book p97)")

# ---------------- p98 · MTC: ORIGIN, SECRETIONS & TYPES ----------------
q(98, "MTC: Origin, Secretions & Types", "Medullary thyroid carcinoma arises from:",
  ["Parafollicular/C cells", "Follicular cells", "Epithelial cells", "Lymphocytes"], 0,
  "Arises from parafollicular/C cells (neural crest → ultimobranchial bodies → C cells). (Book p98)")
q(98, "MTC: Origin, Secretions & Types", "MTC secretes all EXCEPT:",
  ["Thyroxine", "Calcitonin", "CEA", "Chromogranin A"], 0,
  "Secrete: calcitonin, CEA, chromogranin A. (Book p98)")
q(98, "MTC: Origin, Secretions & Types", "In MTC, a sign of dedifferentiation (more aggressive) is:",
  ["CEA (carcinoembryonic antigen)", "Calcitonin", "Chromogranin A", "Thyroglobulin"], 0,
  "CEA: sign of dedifferentiation (more aggressive). (Book p98)")
q(98, "MTC: Origin, Secretions & Types", "Chromogranin A is also released in:",
  ["Carcinoid tumors", "Insulinoma", "Pheochromocytoma only", "Gastrinoma"], 0,
  "Chromogranin A also released in carcinoid tumors. (Book p98)")
q(98, "MTC: Origin, Secretions & Types", "The more common (m/c) type of MTC is:",
  ["Sporadic (4th-6th decade)", "Familial (3rd-4th decade)", "MEN2B associated", "Juvenile"], 0,
  "Sporadic: m/c, 4th-6th decade, less aggressive; familial: MEN2 syndromes, more aggressive, multifocal. (Book p98)")
q(98, "MTC: Origin, Secretions & Types", "The most aggressive MTC is associated with:",
  ["MEN 2B", "MEN 1", "MEN 2A", "MEN 4"], 0,
  "MEN 2B: most aggressive. (Book p98)")
q(98, "MTC: Origin, Secretions & Types", "Diarrhoea in MTC is due to:",
  ["Serotonin", "ACTH", "Histamine", "Calcitonin"], 0,
  "Diarrhoea: serotonin. (Book p98)")
q(98, "MTC: Origin, Secretions & Types", "Cushing syndrome in MTC is due to:",
  ["ACTH", "Serotonin", "Histamine", "VIP"], 0,
  "Cushing syndrome: ACTH. (Book p98)")
q(98, "MTC: Origin, Secretions & Types", "Flushing in MTC is due to:",
  ["Histamine", "Serotonin", "ACTH", "Calcitonin"], 0,
  "Flushing: histamine. (Book p98)")

# ---------------- p98-99 · MTC: DX, SPREAD & MX ----------------
q(98, "MTC: Dx, Spread & Mx", "H&E of MTC classically shows:",
  ["Amyloid rich stroma", "Orphan Annie nuclei", "Follicles", "Psammoma bodies"], 0,
  "Amyloid rich stroma. (Book p98)")
q(98, "MTC: Dx, Spread & Mx", "Haematogenous spread of MTC is most commonly to:",
  ["Liver", "Lungs", "Bone", "Brain"], 0,
  "Lymphatic: level 6 LNs; haematogenous: liver (m/c). (Book p98)")
q(99, "MTC: Dx, Spread & Mx", "The 1st line Mx of MTC is:",
  ["Surgery", "RIA", "Chemotherapy", "Radiotherapy"], 0,
  "Sx: 1st line Mx. (Book p99)")
q(99, "MTC: Dx, Spread & Mx", "Tumor localized to thyroid in MTC is treated with:",
  ["Total thyroidectomy + CND", "Hemithyroidectomy", "Total + CND + B/L MRND", "RIA"], 0,
  "Localized to thyroid: total thyroidectomy + CND. (Book p99)")
q(99, "MTC: Dx, Spread & Mx", "Tumor involving thyroid + level 6 + other LN in MTC needs:",
  ["Total thyroidectomy + CND + MRND on B/L sides", "Total + CND only", "Hemithyroidectomy", "Debulking only"], 0,
  "Thyroid + level 6 & other LN: total + CND + MRND on B/L sides. (Book p99)")
q(99, "MTC: Dx, Spread & Mx", "Whole body iodine scan/RIA in MTC has:",
  ["No role (cells do not take up iodine)", "A major role", "A diagnostic role", "A follow-up role"], 0,
  "No role in MTC - cells do not take up iodine. (Book p99)")
q(99, "MTC: Dx, Spread & Mx", "Before treating MTC, always rule out which MEN2 association that must be managed FIRST?",
  ["Pheochromocytoma", "Hyperparathyroidism", "Prolactinoma", "Insulinoma"], 0,
  "Rule out pheochromocytoma (managed FIRST, then MTC); hyperparathyroidism managed together. (Book p99)")
q(99, "MTC: Dx, Spread & Mx", "Tyrosine kinase inhibitors for advanced MTC are:",
  ["Vandetinib, carbozantinib", "Sorafenib, lenvatinib", "Dabrafenib", "Imatinib"], 0,
  "Advanced: tumor debulking, radiotherapy, TKI vandetinib, carbozantinib. (Book p99)")
q(99, "MTC: Dx, Spread & Mx", "Follow-up markers of MTC are:",
  ["Calcitonin & CEA", "Thyroglobulin", "TSH", "CA-125"], 0,
  "Follow up: calcitonin & CEA. (Book p99)")

# ---------------- p99 · SUMMARY OF THYROID CANCERS ----------------
q(99, "Summary of Thyroid Cancers", "Match the genetics: follicular thyroid carcinoma shows:",
  ["K-RAS, PI3K", "BRAF, RET-PTC", "RET, MEN II", "P53"], 0,
  "Follicular: K-RAS, PI3K (papillary BRAF/RET-PTC; medullary RET/MEN II; anaplastic P53). (Book p99)")
q(99, "Summary of Thyroid Cancers", "The metastasis pattern of medullary and anaplastic cancers is:",
  ["Both (lymphatic + haematogenous)", "Lymphatic only", "Haematogenous only", "No spread"], 0,
  "Papillary lymphatic; follicular haematogenous (bony mets); medullary & anaplastic BOTH. (Book p99)")
q(99, "Summary of Thyroid Cancers", "The origin of anaplastic carcinoma is:",
  ["Follicular cells", "Parafollicular cells", "C cells", "Lymphocytes"], 0,
  "Anaplastic origin: follicular cells (medullary: parafollicular cells). (Book p99)")
q(99, "Summary of Thyroid Cancers", "Risk factors for papillary cancer include radiation, thyroglossal cyst and:",
  ["Hashimoto's thyroiditis", "MNG", "Iodine deficiency", "MEN2"], 0,
  "Papillary risk: radiation, thyroglossal cyst, Hashimoto's thyroiditis; follicular: iodine deficiency, MNG. (Book p99)")
q(99, "Summary of Thyroid Cancers", "On H&E, medullary carcinoma shows:",
  ["Amyloid", "Orphan Annie eye & psammoma", "Follicles", "Nothing specific"], 0,
  "H&E: papillary - Orphan Annie eye, psammoma; follicular - follicles; medullary - amyloid. (Book p99)")

# ---------------- p100 · MEN 1 SYNDROME ----------------
q(100, "MEN 1 Syndrome", "MEN 1 (Wermer syndrome) is due to mutation of:",
  ["Menin gene on Ch 11", "RET on Ch 10", "CDKN1B on Ch 12", "PTEN on Ch 10"], 0,
  "MEN1 (Wermer): menin gene on Ch 11. (Book p100)")
q(100, "MEN 1 Syndrome", "The most common pituitary adenoma in MEN1 is:",
  ["Prolactinoma", "Somatotroph adenoma", "Corticotroph adenoma", "Non-functional"], 0,
  "3 Ps: pituitary adenomas (prolactinoma m/c). (Book p100)")
q(100, "MEN 1 Syndrome", "The most common abnormality in MEN1 (95% cases) is:",
  ["Parathyroid adenoma >> hyperplasia", "Parathyroid hyperplasia >> adenoma", "Parathyroid carcinoma", "Normal parathyroid"], 0,
  "Parathyroid abnormalities (m/c: 95% cases): adenoma >> hyperplasia. (Book p100)")
q(100, "MEN 1 Syndrome", "The most common pancreatic endocrine tumor overall vs in MEN1 are respectively:",
  ["Insulinoma; gastrinoma", "Gastrinoma; insulinoma", "PPoma; insulinoma", "VIPoma; gastrinoma"], 0,
  "Pancreatic: m/c overall insulinoma; in MEN1 gastrinoma; non-functional PPoma. (Book p100)")
q(100, "MEN 1 Syndrome", "The non-functional pancreatic tumor seen in MEN1 is:",
  ["PPoma", "Insulinoma", "Gastrinoma", "VIPoma"], 0,
  "Non functional pancreatic tumor: PPoma. (Book p100)")
q(100, "MEN 1 Syndrome", "Other tumors seen in MEN1 include:",
  ["Collagenomas, adrenocortical & thymic tumors", "Pheochromocytoma", "Mucosal neuromas", "Renal tumors"], 0,
  "Also collagenomas, adrenocortical tumors, thymic tumors. (Book p100)")

# ---------------- p100 · MEN 2 SYNDROME ----------------
q(100, "MEN 2 Syndrome", "MEN 2 syndrome is due to:",
  ["RET proto-oncogene on Ch 10", "Menin on Ch 11", "CDKN1B on Ch 12", "WRN on Ch 8"], 0,
  "RET proto-oncogene on Ch 10. (Book p100)")
q(100, "MEN 2 Syndrome", "The MEN2 type with MTC only carries exon mutation:",
  ["618", "634", "918", "768"], 0,
  "Types: MTC only (exon 618), MEN 2A, MEN 2B. (Book p100)")
q(100, "MEN 2 Syndrome", "MEN 2A (Sipple syndrome) features include all EXCEPT:",
  ["Mucosal neuromas", "MTC (m/c)", "Parathyroid abnormalities (adenoma > hyperplasia)", "Pheochromocytoma"], 0,
  "2A: MTC m/c, parathyroid (adenoma > hyperplasia), pheochromocytoma, megacolon/Hirschsprung (2A > 2B); exon 634. (Book p100)")
q(100, "MEN 2 Syndrome", "The '5 Ms' (MTC m/c most aggressive, marfanoid, mucosal neuromas, medullated corneal fibres, megacolon) describe:",
  ["MEN 2B (MEN3 syndrome), exon 918", "MEN 2A, exon 634", "MEN 1", "MEN 4"], 0,
  "MEN 2B (MEN3): 5 Ms; exon 918; medullated corneal fibres cause visual problems. (Book p100)")
q(100, "MEN 2 Syndrome", "Megacolon/Hirschsprung disease is more common in:",
  ["MEN 2A > 2B", "MEN 2B > 2A", "MEN 1", "Equal in both"], 0,
  "Megacolon/Hirschsprung disease: MEN 2A > 2B. (Book p100)")

# ---------------- p101 · RET TESTING & MEN 4 ----------------
q(101, "RET Testing & MEN 4", "Who should undergo RET testing?",
  ["1st degree relatives of MTC/MEN2 patients", "All thyroid patients", "Only symptomatic patients", "Only MEN1 families"], 0,
  "1st degree relatives should undergo RET testing. (Book p101)")
q(101, "RET Testing & MEN 4", "Low risk RET mutations (exons 768, 790) need prophylactic thyroidectomy:",
  ["Upto 20 years", "Upto 5-6 years", "Before 1 year", "At birth"], 0,
  "Low: 768, 790 → upto 20 years. (Book p101)")
q(101, "RET Testing & MEN 4", "Medium risk RET mutations (exons 618, 634) need prophylactic thyroidectomy:",
  ["Upto 5-6 years", "Upto 20 years", "Before 1 year", "After 30 years"], 0,
  "Medium: 618, 634 → upto 5-6 years. (Book p101)")
q(101, "RET Testing & MEN 4", "High risk RET mutation (exon 918) needs prophylactic thyroidectomy:",
  ["Before 1 year", "Upto 5-6 years", "Upto 20 years", "Only if symptomatic"], 0,
  "High: 918 → before 1 year. (Book p101)")
q(101, "RET Testing & MEN 4", "If tumor is +ve, the pentagastrin stimulation test shows:",
  ["↑↑ calcitonin", "↓ calcitonin", "↑ TSH", "↑ thyroglobulin"], 0,
  "If tumor +ve → pentagastrin stimulation test → ↑↑ calcitonin. (Book p101)")
q(101, "RET Testing & MEN 4", "MEN 4 syndrome is due to:",
  ["CDKN1B gene on Ch 12", "RET on Ch 10", "Menin on Ch 11", "PTEN on Ch 10"], 0,
  "MEN4: CDKN1B gene on Ch 12. (Book p101)")
q(101, "RET Testing & MEN 4", "Features of MEN4 include pituitary, parathyroid adenomas plus:",
  ["Renal, adrenocortical & reproductive organ tumors", "Pheochromocytoma & MTC", "Mucosal neuromas", "Pancreatic tumors only"], 0,
  "MEN4: pituitary adenomas, parathyroid adenomas, renal tumors, adrenocortical tumors, reproductive organ tumors. (Book p101)")

# ---------------- units ----------------
def sec_ids(*labels):
    return [x["id"] for x in Q if x["sec"] in labels]

def first_page(label):
    for x in Q:
        if x["sec"] == label:
            return x["page"]
    return 0

UNIT_DEFS = [
    ("Thyroid Cancers: IOC & Syndromes", ("Thyroid Cancers: IOC & Syndromes",),
     "IOC for thyroid cancers is FNAC. Syndrome links: medullary → MEN2/RET; follicular → Cowden (PTEN Ch10, ↑ breast & thyroid cancer, benign GI polyps) & Werner (WRN); papillary → FAP (AP Ch5, ≥100 polyps, 100% colorectal risk), Cowden, Carney/Batman's, PRKAR1A."),
    ("TNM Staging", ("TNM Staging",),
     "T1 ≤2cm (1a ≤1cm, 1b >1-≤2cm); T2 >2-≤4cm; T3a >4cm limited to thyroid; T3b any size invading ONLY strap muscles (recent update); T4 gross extension into major neck structures. N1 regional nodes; M1 distant mets."),
    ("DTC & Updates", ("DTC & Updates",),
     "DTC = papillary + follicular + Hurthle cell: arise from epithelial cells and take up iodine. New rule: age cutoff 55 - younger good prognosis, older bad; anaplastic (previously T4) now staged like DTC."),
    ("PTC: Risk Factors & Genetics", ("PTC: Risk Factors & Genetics",),
     "PTC = m/c thyroid cancer with best prognosis. Risks: radiation (fallout, head-neck RT, RAI at young age - more aggressive tumors), family history, obesity. Genetics BRAF (m/c), GDNF, RET/PTC. F:M 3:1, 3rd-5th decade."),
    ("PTC: Clinical Features & Spread", ("PTC: Clinical Features & Spread",),
     "Presents as thyroid swelling, B/L multicentric → total thyroidectomy. Lymphatic first to level 6 (central/delphian), haematogenous to lungs. Lateral aberrant thyroid = level 6 LN mets with non-palpable gland; incidentaloma <1cm."),
    ("PTC: Diagnosis & Histology", ("PTC: Diagnosis & Histology",),
     "FNAC is IOC. Histology: Orphan Annie eyed/coffee bean nuclei, pseudo intranuclear inclusions, psammoma bodies (dystrophic calcification - also in serous cystadenoma ovary, papillary RCC, meningioma)."),
    ("PTC: Surgical Options", ("PTC: Surgical Options",),
     "Hemithyroidectomy when ALL: low risk, U/L, 1-4 cm, no extrathyroidal spread. Minimum total for radiation-induced, familial non-medullary, multifocal B/L, extrathyroid extension. Add CND for T3/T4 or level 6 (+); add MRND when level 6 + other neck nodes."),
    ("Whole Body Iodine Scan & RIA", ("Whole Body Iodine Scan & RIA",),
     "Post-Sx scan needs TSH >30 (withdraw thyroxine 4-6 wks - patient hypothyroid - or recombinant TSH). (+) scan → RIA with I131 (β rays, t½ 7-8 d) for residual/mets/+ve nodes/high Tg; (-) → thyroxine TSH suppression + life-long 6-monthly USG & thyroglobulin (unreliable if anti-Tg Ab +)."),
    ("Radioiodine Resistant DTC & Lindsey Tumor", ("Radioiodine Resistant DTC & Lindsey Tumor",),
     "RAI-resistant DTC: sorafenib/lenvatinib, EBRT, doxorubicin. Lindsey tumor = follicular variety of papillary, prognosis like PTC."),
    ("FTC: Basics, Features & Spread", ("FTC: Basics, Features & Spread",),
     "2nd m/c; m/c in iodine deficiency; risk long-standing MNG; females > males. miRNA 197/346, PTEN & BAX. Rapid neck swelling, pressure symptoms; pulsatile vascular osteolytic bony mets; lymphatic to level 6."),
    ("FTC: Dx, Mx & Hurthle Cell Carcinoma", ("FTC: Dx, Mx & Hurthle Cell Carcinoma",),
     "FNAC gives follicular neoplasm (Thy 3) but can't split adenoma vs carcinoma - hemithyroidectomy + frozen section decides. Prognosis slightly poorer than PTC. Hurthle cell: 6th-7th decade, mitochondria-rich oxyphilic cells, less RAI-avid, more aggressive, poorer than FTC; Hurthle cells also in Hashimoto's & thyroid lymphoma."),
    ("Prognostic Scores (AGES/AMES/MACIS)", ("Prognostic Scores (AGES/AMES/MACIS)",),
     "Well-differentiated TC scores: AGES = age, grade, extrathyroidal invasion, size; AMES = age, metastases, extrathyroidal spread, size; MACIS = metastases, age, completeness of original resection (post-op criteria), invasion, size."),
    ("Anaplastic Carcinoma", ("Anaplastic Carcinoma",),
     "Least common, worst prognosis; 5th-7th decade; miRNA 17-92, p53 & B-catenin. Rapid hard neck swelling on MNG background, pressure symptoms; D/D Riedel thyroiditis; spreads to lungs; FNAC inconclusive → core biopsy. Localised: total + CND + MRND; advanced: debulking, isthmusectomy for tracheal pressure, dabrafenib, chemo."),
    ("Thyroid Lymphoma", ("Thyroid Lymphoma",),
     "Rare, 5th-7th decade, on long-standing Hashimoto's. DLBCL m/c; thyroid swelling + B symptoms (weight loss, fever, night sweats, itching). Core/trucut biopsy (FNAC can't characterize). Chemo R-CHOP 1st line (rituximab anti-CD20, cyclophosphamide, hydroxydaunorubicin, oncovin/vincristine, prednisolone); surgery only for residual/recurrent."),
    ("MTC: Origin, Secretions & Types", ("MTC: Origin, Secretions & Types",),
     "From parafollicular/C cells (neural crest → ultimobranchial bodies). Secretes calcitonin, CEA (dedifferentiation marker), chromogranin A. Sporadic m/c (4th-6th decade); familial = MEN2 (2B most aggressive, multifocal). Atypical symptoms: diarrhoea (serotonin), Cushing (ACTH), flushing (histamine)."),
    ("MTC: Dx, Spread & Mx", ("MTC: Dx, Spread & Mx",),
     "FNAC + amyloid-rich stroma; lymphatic level 6, haematogenous liver. Sx 1st line: total + CND (add MRND as nodal spread widens). No RIA role. Rule out pheochromocytoma FIRST & treat hyperparathyroidism together. Advanced: debulking, RT, vandetinib/carbozantinib; follow-up calcitonin + CEA."),
    ("Summary of Thyroid Cancers", ("Summary of Thyroid Cancers",),
     "Papillary: m/c, best, BRAF/RET-PTC, lymphatic, Orphan Annie + psammoma. Follicular: iodine deficiency/MNG, K-RAS/PI3K, bony mets, follicles. Medullary: parafollicular, RET/MEN2, both routes, amyloid. Anaplastic: L/C, worst, P53, both routes."),
    ("MEN 1 Syndrome", ("MEN 1 Syndrome",),
     "Wermer syndrome, menin on Ch 11. 3 Ps: pituitary (prolactinoma m/c), parathyroid (95%, adenoma >> hyperplasia), pancreatic (overall insulinoma, in MEN1 gastrinoma, non-functional PPoma); plus collagenomas, adrenocortical & thymic tumors."),
    ("MEN 2 Syndrome", ("MEN 2 Syndrome",),
     "RET on Ch 10. MTC-only exon 618; 2A (Sipple) exon 634: MTC, parathyroid, pheochromocytoma, megacolon/Hirschsprung (2A > 2B); 2B (MEN3) exon 918: 5 Ms - MTC most aggressive, marfanoid, mucosal neuromas, medullated corneal fibres, megacolon."),
    ("RET Testing & MEN 4", ("RET Testing & MEN 4",),
     "1st-degree relatives get RET testing: low (768/790) prophylactic thyroidectomy upto 20 yrs; medium (618/634) upto 5-6 yrs; high (918) before 1 yr. Tumor +ve → pentagastrin stimulation → ↑↑ calcitonin. MEN4 = CDKN1B on Ch 12: pituitary, parathyroid, renal, adrenocortical, reproductive organ tumors."),
]

UNITS = []
for i, (title, labels, guide) in enumerate(UNIT_DEFS, 1):
    UNITS.append({"id": f"SURG-U15-{i}", "ch": 15, "n": i, "title": title,
                  "sec": f"{labels[0]} · p{first_page(labels[0])}",
                  "qs": sec_ids(*labels), "guide": guide})

covered = [i for u in UNITS for i in u["qs"]]
assert covered == [x["id"] for x in Q], "units must cover questions in order"

data = {"questions": Q, "units": UNITS}
with open("data/ch15.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
print(f"ch15: {len(Q)} questions, {len(UNITS)} units")
