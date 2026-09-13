#!/usr/bin/env python3
"""Build data/ch12.json for PULSE Surgery ch12 (Breast : Part 4, book p68-74)."""
import json

Q = []
def q(page, sec, text, opts, ans, exp):
    Q.append({"id": f"SURG-C12-{len(Q)+1:03d}", "sec": sec, "page": page,
              "q": text, "opts": opts, "ans": ans, "exp": exp})

# ---------------- p68 · CHEMOTHERAPY INDICATIONS & NACT ----------------
q(68, "Chemotherapy Indications & NACT", "Which of the following is NOT a listed indication for chemotherapy in breast cancer?",
  ["T1 tumor with ER, PR +ve and low recurrence risk", "+ve lymph nodes", "Locally advanced breast cancers", "Her 2 neu +ve tumors"], 0,
  "Indications for chemotherapy: 1. +ve lymph nodes; 2. Locally advanced breast cancers; 3. ER, PR -ve tumors; 4. Her 2 neu +ve tumors; 5. metastasis. (Book p68)")
q(68, "Chemotherapy Indications & NACT", "Chemotherapy is indicated for breast tumors that are:",
  ["ER, PR -ve", "ER, PR +ve", "ER +ve only", "PR +ve only"], 0,
  "Indication #3 for chemotherapy: ER, PR -ve tumors. (Book p68)")
q(68, "Chemotherapy Indications & NACT", "Which is NOT an indication for neoadjuvant chemotherapy (NACT)?",
  ["Small tumor with no desire for breast conservation", "Locally advanced breast cancer (LABC)", "Triple negative breast cancer (TNBC)", "Large tumor with patient desiring BCS"], 0,
  "NACT indications: 1. LABC; 2. TNBC; 3. HER 2 Neu +ve; 4. Large tumors with patient desiring Breast conservation Sx (BCS). (Book p68)")
q(68, "Chemotherapy Indications & NACT", "NACT is indicated for large tumors when the patient desires:",
  ["Breast conservation surgery (BCS)", "Mastectomy", "Radiotherapy alone", "Hormonal therapy alone"], 0,
  "NACT indication #4: Large tumors with patient desiring Breast conservation Sx (BCS). (Book p68)")
q(68, "Chemotherapy Indications & NACT", "Which is an advantage of NACT?",
  ["Downstage/downsize the tumour", "Increase micrometastasis", "Replace the need for surgery", "Remove the need for RT after BCS"], 0,
  "Advantages of NACT: Downstage/downsize the tumour; ↓ micrometastasis; in vivo chemosensitivity indicator (RECIST criteria). (Book p68)")
q(68, "Chemotherapy Indications & NACT", "NACT decreases which of the following?",
  ["Micrometastasis", "Tumor size only", "Lymph node yield", "RECIST score"], 0,
  "Advantages of NACT include ↓ micrometastasis. (Book p68)")
q(68, "Chemotherapy Indications & NACT", "The in vivo chemosensitivity indicator during NACT is assessed by:",
  ["RECIST criteria", "TNM staging", "Van Nuys index", "Karnofsky score"], 0,
  "In vivo chemosensitivity indicator: RECIST criteria (Response evaluation criteria in solid tumors). (Book p68)")

# ---------------- p68 · RECIST CRITERIA ----------------
q(68, "RECIST Criteria", "RECIST stands for:",
  ["Response Evaluation Criteria In Solid Tumors", "Response Estimation Criteria In Soft Tissues", "Recurrence Evaluation Criteria In Solid Tumors", "Response Evaluation Criteria In Skin Tumors"], 0,
  "RECIST criteria = Response evaluation criteria in solid tumors. (Book p68)")
q(68, "RECIST Criteria", "On RECIST, Complete Response (CR) means:",
  ["Disappearance of all lesions & pathological lymph nodes", "≥30% decrease in single largest diameter", "No PR or PD", "≥20% increase in SLD"], 0,
  "CR: Disappearance of all lesions & pathological lymph nodes. (Book p68)")
q(68, "RECIST Criteria", "Which breast cancer subtype has the highest pathological CR (pCR) rates?",
  ["TNBC", "ER +ve lobular cancer", "Her 2 neu -ve luminal A", "LCIS"], 0,
  "pCR: TNBC have highest pCR rates. (Book p68)")
q(68, "RECIST Criteria", "Partial Response (PR) on RECIST requires at least what change in the single largest diameter (SLD)?",
  ["≥30% decrease", "≥20% decrease", "≥50% decrease", "Any decrease"], 0,
  "PR: ≥30% ↓ in single largest diameter (SLD), no new lesions, no progression of non target lesions. (Book p68)")
q(68, "RECIST Criteria", "Which is required for a Partial Response (PR) on RECIST?",
  ["No new lesions and no progression of non target lesions", "Disappearance of all lymph nodes", "≥20% increase in SLD", "New lesions <1 cm"], 0,
  "PR: ≥30% ↓ SLD; No new lesions; No progression of non target lesions. (Book p68)")
q(68, "RECIST Criteria", "Stable Disease (SD) on RECIST is defined as:",
  ["No PR or PD", "Disappearance of target lesions", "≥30% ↓ in SLD", "≥20% ↑ in SLD"], 0,
  "SD: No PR or PD. (Book p68)")
q(68, "RECIST Criteria", "Progressive Disease (PD) on RECIST includes ≥20% increase in SLD, progression of non target lesions, or:",
  ["New lesions", "≥30% decrease in SLD", "Stable non target lesions", "Disappearance of lesions"], 0,
  "PD: ≥20% ↑ SLD (or) Progression of non target lesions (or) New lesions. (Book p68)")

# ---------------- p69 · CHEMOPORT & REGIMENS ----------------
q(69, "Chemoport & Regimens", "A chemoport is placed:",
  ["Below the clavicle", "Above the clavicle", "In the femoral vein", "In the internal jugular vein"], 0,
  "Chemoport: Placed below the clavicle; used to deliver chemo drugs; prevents thrombophlebitis. (Book p69)")
q(69, "Chemoport & Regimens", "On X-ray, the chemoport tip lies in:",
  ["SVC just above right atrium", "Right ventricle", "Left atrium", "Subclavian vein"], 0,
  "X Ray chemoport: Tip lies in SVC just above right atrium. (Book p69)")
q(69, "Chemoport & Regimens", "A chemoport prevents which complication of chemotherapy delivery?",
  ["Thrombophlebitis", "Peripheral neuropathy", "Osteoporosis", "Hot flashes"], 0,
  "Chemoport prevents thrombophlebitis. (Book p69)")
q(69, "Chemoport & Regimens", "In the CAF/CMF regimens (now not used), F stands for:",
  ["5-Fluorouracil", "Flutamide", "Folinic acid", "Fulvestrant"], 0,
  "CAF/CMF (not used): C cyclophosphamide, A Adriamycin, F 5-Fluorouracil, m methotrexate. (Book p69)")
q(69, "Chemoport & Regimens", "In CMF, the letter m stands for:",
  ["Methotrexate", "Mitomycin", "Melphalan", "Methoxy psoralen"], 0,
  "m: methotrexate. (Book p69)")
q(69, "Chemoport & Regimens", "In CAF, the letter A stands for:",
  ["Adriamycin", "Anastrozole", "Abemaciclib", "Atezolizumab"], 0,
  "A: Adriamycin. (Book p69)")
q(69, "Chemoport & Regimens", "The currently used regimen for Her 2 neu -ve breast cancer is:",
  ["4 cycles AC/EC then 4 cycles T", "6 cycles TCH + P", "CAF for 6 cycles", "CMF for 1 year"], 0,
  "Her 2 neu -ve: Currently used = 4 cycles AC/EC then 4 cycles T. (Book p69)")
q(69, "Chemoport & Regimens", "In the AC/EC regimen, E stands for:",
  ["Epirubicin", "Etoposide", "Erlotinib", "Everolimus"], 0,
  "E: Epirubicin. (Book p69)")
q(69, "Chemoport & Regimens", "The T in '4 cycles T' refers to:",
  ["Taxanes (Paclitaxel/Docetaxel)", "Tamoxifen", "Trastuzumab", "Topotecan"], 0,
  "T: Taxanes (Paclitaxel/Docetaxel). (Book p69)")
q(69, "Chemoport & Regimens", "The side effect of Paclitaxel is:",
  ["Peripheral neuropathy", "Endometrial hyperplasia", "Osteoporosis", "DVT"], 0,
  "S/E of Paclitaxel: Peripheral neuropathy. (Book p69)")
q(69, "Chemoport & Regimens", "The regimen for Her 2 neu +ve breast cancer is:",
  ["6 cycles TCH + P", "4 cycles AC/EC then 4 cycles T", "CAF/CMF", "Tamoxifen for 5 years"], 0,
  "Her 2 neu +ve: 6 cycles TCH + P. (Book p69)")
q(69, "Chemoport & Regimens", "In TCH + P, the C stands for:",
  ["Carboplatin", "Cyclophosphamide", "Cisplatin", "Capecitabine"], 0,
  "TCH + P: T Taxanes, C Carboplatin, H Herceptin, P Pertuzumab. (Book p69)")
q(69, "Chemoport & Regimens", "Which two drugs in TCH + P are the anti-Her 2 neu agents?",
  ["Herceptin and Pertuzumab", "Taxanes and Carboplatin", "Herceptin and Tamoxifen", "Pertuzumab and Paclitaxel"], 0,
  "H: Herceptin + P: Pertuzumab = Anti-Her 2 neu. (Book p69)")

# ---------------- p69 · AVOIDING CHEMO & MOLECULAR TESTS ----------------
q(69, "Avoiding Chemo & Molecular Tests", "Chemotherapy is avoided in breast cancer patients with:",
  ["Poor performance status (Karnofsky/ECOG score)", "TNBC subtype", "Her 2 neu +ve disease", "+ve lymph nodes"], 0,
  "Avoid chemotherapy in: 1. Poor performance status (Karnofsky/ECOG score); 2. Low-risk molecular profile. (Book p69)")
q(69, "Avoiding Chemo & Molecular Tests", "In T1/T2, N0/N1, M0 with ER ± and Her 2 neu -ve disease, molecular testing is done to indicate:",
  ["Risk of recurrence", "Risk of lymphedema", "RT dose", "Need for SLNB"], 0,
  "For T1/T2, N0/N1, M0, ER±, Her2 neu- patients: Do molecular testing (indicates risk of recurrence). (Book p69)")
q(69, "Avoiding Chemo & Molecular Tests", "If molecular testing shows LOW risk of recurrence, the plan is:",
  ["Avoid chemo", "Give chemo", "Give RT only", "Mastectomy"], 0,
  "Molecular testing: Low → Avoid chemo; High → Chemo given. (Book p69)")
q(69, "Avoiding Chemo & Molecular Tests", "Oncotype Dx is a:",
  ["21 gene assay", "70 gene assay", "12 gene assay", "50 gene assay"], 0,
  "Oncotype Dx: 21 gene assay. (Book p69)")
q(69, "Avoiding Chemo & Molecular Tests", "Mammaprint is a:",
  ["70 gene assay", "21 gene assay", "12 gene assay", "50 gene assay"], 0,
  "Mammaprint: 70 gene assay. (Book p69)")
q(69, "Avoiding Chemo & Molecular Tests", "Endopredict is a:",
  ["12 gene assay", "21 gene assay", "70 gene assay", "50 gene assay"], 0,
  "Endopredict: 12 gene assay. (Book p69)")
q(69, "Avoiding Chemo & Molecular Tests", "PAM 50 is a:",
  ["50 gene assay", "21 gene assay", "70 gene assay", "12 gene assay"], 0,
  "PAM 50: 50 gene assay. (Book p69)")
q(69, "Avoiding Chemo & Molecular Tests", "The Indian molecular test for recurrence risk in breast cancer is:",
  ["CAN assist", "Oncotype Dx", "Mammaprint", "Endopredict"], 0,
  "CAN assist: Indian test. (Book p69)")

# ---------------- p70 · RADIOTHERAPY: WBI VS APBI ----------------
q(70, "Radiotherapy: WBI vs APBI", "Which is NOT a listed indication for radiotherapy in breast cancer?",
  ["T1 tumor <2 cm with clear margins and N0", "+ve lymph nodes", "Tumor >5 cm (> T3)", "After BCS"], 0,
  "RT indications: 1. +ve lymph nodes; 2. Tumor >5 cm (> T3); 3. Locally advanced breast carcinoma (LABC); 4. After BCS. (Book p70)")
q(70, "Radiotherapy: WBI vs APBI", "Whole breast irradiation (WBI) targets the breast and which lymph nodes?",
  ["Axilla, infra & supraclavicular, internal mammary", "Axilla only", "Internal mammary only", "Supraclavicular only"], 0,
  "WBI target sites: Breast + Lymph nodes: Axilla, infra & supraclavicular, internal mammary. (Book p70)")
q(70, "Radiotherapy: WBI vs APBI", "The duration and dose of WBI is:",
  ["25 days: 50-54 Gy", "5 days: 30-34 Gy", "10 days: 40 Gy", "30 days: 60-70 Gy"], 0,
  "WBI duration: 25 days: 50-54 Gy. (Book p70)")
q(70, "Radiotherapy: WBI vs APBI", "Accelerated partial breast irradiation (APBI) is delivered over:",
  ["5 days: 30-34 Gy", "25 days: 50-54 Gy", "15 days: 45 Gy", "3 days: 20 Gy"], 0,
  "APBI duration: 5 days: 30-34 Gy. (Book p70)")
q(70, "Radiotherapy: WBI vs APBI", "The target site of APBI is:",
  ["Partial breast", "Whole breast + axilla", "Internal mammary chain", "Chest wall"], 0,
  "APBI target: Partial breast. (Book p70)")
q(70, "Radiotherapy: WBI vs APBI", "Which is NOT an indication of APBI?",
  ["Age <50 years", "T1 tumor", "ER, PR (+)", "-ve lymphovascular invasion"], 0,
  "APBI indications: 1. T1; 2. ER, PR (+); 3. -ve lymphovascular invasion; 4. Unifocal; 5. -ve margins; 6. ≥50 years. (Book p70)")
q(70, "Radiotherapy: WBI vs APBI", "In APBI, the electrodes are placed in:",
  ["The tumor cavity", "The axilla", "The skin surface", "The internal mammary chain"], 0,
  "APBI: Electrodes placed in cavity. (Book p70)")

# ---------------- p70 · HORMONAL THERAPY ----------------
q(70, "Hormonal Therapy", "Hormonal therapy in breast cancer is indicated when:",
  ["Either or both ER/PR +ve", "Only when both ER and PR are +ve", "Only in metastatic disease", "Only after chemotherapy"], 0,
  "Hormonal therapy indication: Either or both ER/PR +ve. (Book p70)")
q(70, "Hormonal Therapy", "The drug for pre-menopausal women is:",
  ["Tamoxifen (SERM)", "Letrozole", "Anastrozole", "Olaparib"], 0,
  "Pre-menopausal: Selective estrogen receptor modulator (SERM): Tamoxifen. (Book p70)")
q(70, "Hormonal Therapy", "Tamoxifen belongs to which drug class?",
  ["Selective estrogen receptor modulator (SERM)", "Aromatase inhibitor", "LHRH analogue", "CDK 4/6 inhibitor"], 0,
  "Tamoxifen = SERM. (Book p70)")
q(70, "Hormonal Therapy", "The drugs for post-menopausal women are:",
  ["Aromatase inhibitors: Letrozole, Anastrozole", "Tamoxifen only", "Fulvestrant only", "Zoladex only"], 0,
  "Post-menopausal: Aromatase inhibitors: Letrozole, Anastrozole. (Book p70)")
q(70, "Hormonal Therapy", "The standard duration of tamoxifen is:",
  ["5 years (extended upto 10 years in some cases)", "1 year", "2 years", "Lifetime"], 0,
  "Tamoxifen duration: 5 years; in some cases extended upto 10 years. (Book p70)")
q(70, "Hormonal Therapy", "The duration of aromatase inhibitor therapy is:",
  ["5-10 years", "1-2 years", "6 months", "20 years"], 0,
  "Aromatase inhibitors duration: 5-10 years. (Book p70)")
q(70, "Hormonal Therapy", "The most common side effect of tamoxifen is:",
  ["Hot flashes", "Osteoporosis", "Peripheral neuropathy", "Cardiotoxicity"], 0,
  "Tamoxifen side effects: Hot flashes (m/c), endometrial hyperplasia, DVT. (Book p70)")
q(70, "Hormonal Therapy", "Besides hot flashes, tamoxifen causes:",
  ["Endometrial hyperplasia and DVT", "Osteoporosis", "Cataract", "Pulmonary fibrosis"], 0,
  "Tamoxifen S/E: Hot flashes (m/c); Endometrial hyperplasia; DVT. (Book p70)")
q(70, "Hormonal Therapy", "The most common side effect of aromatase inhibitors is:",
  ["Osteoporosis", "Endometrial hyperplasia", "DVT", "Hot flashes"], 0,
  "Aromatase inhibitors: Osteoporosis (m/c). (Book p70)")
q(70, "Hormonal Therapy", "Before starting aromatase inhibitors, which baseline test is done?",
  ["DEXA scan", "Mammogram", "Pelvic USG", "LFT"], 0,
  "Before starting aromatase inhibitors, baseline DEXA scan done. If low, start vit D3, Ca2+ & bisphosphonate. (Book p70)")
q(70, "Hormonal Therapy", "If the DEXA scan is low before starting aromatase inhibitors, start:",
  ["Vit D3, Ca2+ & bisphosphonate", "Tamoxifen", "Estrogen supplements", "RT"], 0,
  "If DEXA low: start vit D3, Ca2+ & bisphosphonate. (Book p70)")
q(70, "Hormonal Therapy", "When planning pregnancy while on tamoxifen, tamoxifen must be completely taken for how many years (out of 5)?",
  ["2 years", "1 year", "4 years", "5 years without break"], 0,
  "Tamoxifen has to be completely taken for 2 years (out of 5 years) before pausing for pregnancy. (Book p70)")
q(70, "Hormonal Therapy", "If a patient on tamoxifen wants to conceive after 2 years (no distant mets/contraindication), tamoxifen must be stopped:",
  ["3 months prior to conception", "1 week prior", "1 year prior", "It need not be stopped"], 0,
  "Tamoxifen has to be stopped 3 months prior to conception. (Book p70)")

# ---------------- p71 · PROGNOSTIC FACTORS ----------------
q(71, "Prognostic Factors", "The most important prognostic factor in breast cancer is:",
  ["Axillary LN status", "Tumor size", "Grade", "Age"], 0,
  "Most important prognostic factor: Axillary LN status. (Book p71)")
q(71, "Prognostic Factors", "In metastatic breast cancer, the most important prognostic factor is:",
  ["ER, PR status", "Axillary LN status", "Ki-67 index", "Tumor size"], 0,
  "In metastatic breast cancer: ER, PR status. (Book p71)")
q(71, "Prognostic Factors", "Which is a poor prognostic DISEASE factor?",
  ["High Ki-67 index", "Older age", "Post-menopausal status", "Absence of DCIS component"], 0,
  "Disease factors: ↑ size, ↑ stage, axillary LN involvement, ↑ grade, aggressive histopathological variant, lymphovascular invasion, extensive DCIS component, high Ki-67 index. (Book p71)")
q(71, "Prognostic Factors", "Which histopathological variant of breast cancer is aggressive?",
  ["Metaplastic carcinoma", "Tubular carcinoma", "Papillary DCIS", "Fibroadenoma"], 0,
  "Histopathological variant: metaplastic carcinoma is aggressive. (Book p71)")
q(71, "Prognostic Factors", "Poor prognostic disease factors include Her2/neu positive and which subtype?",
  ["Triple negative", "Luminal A", "LCIS", "Lobular in situ"], 0,
  "Aggressive biology: Her2/neu positive and triple negative. (Book p71)")
q(71, "Prognostic Factors", "Which is a poor prognostic PATIENT factor?",
  ["Younger age", "Older age", "Male sex", "Absence of family history"], 0,
  "Patient factors: Younger age, premenopausal women, BRCA-associated tumour, family history, prior history, obesity/sedentary lifestyle, failure to complete intended treatment. (Book p71)")
q(71, "Prognostic Factors", "BRCA-associated tumours and lobular histology are listed under:",
  ["Poor prognostic patient factors / bilateral cancer features", "Good prognostic factors", "RECIST criteria", "APBI indications"], 0,
  "Patient factors include BRCA-associated tumour; bilateral breast carcinoma is usually BRCA (+) with lobular histology. (Book p71)")

# ---------------- p71 · FOLLOW UP & TREATMENT SUMMARY ----------------
q(71, "Follow up & Treatment Summary", "In follow-up, clinical visits in the first 2 years are:",
  ["Every 3 months", "Every 6 months", "Every year", "Every month"], 0,
  "Clinical visits: Every 3 months for first 2 years; every 6 months b/w 2-5 years; every year after 5 years. (Book p71)")
q(71, "Follow up & Treatment Summary", "Between 2-5 years, follow-up visits are:",
  ["Every 6 months", "Every 3 months", "Every 2 years", "Monthly"], 0,
  "Every 6 months b/w 2-5 years. (Book p71)")
q(71, "Follow up & Treatment Summary", "After 5 years, follow-up visits are:",
  ["Every year", "Every 3 months", "Every 6 months", "Only if symptomatic"], 0,
  "Every year after 5 years. (Book p71)")
q(71, "Follow up & Treatment Summary", "Mammogram/USG in follow-up is done:",
  ["Once a year", "Every 3 months", "Every 2 years", "Once in 5 years"], 0,
  "Mammogram/USG: Once a year. (Book p71)")
q(71, "Follow up & Treatment Summary", "A patient on tamoxifen needs which investigation in follow-up?",
  ["USG pelvis (endometrial thickness)", "DEXA scan yearly", "CT chest", "Serum CEA"], 0,
  "Patient on tamoxifen: USG pelvis (Endometrial thickness). (Book p71)")
q(71, "Follow up & Treatment Summary", "The serum marker for breast cancer is:",
  ["S. Ca 15-3", "CEA", "CA 19-9", "AFP"], 0,
  "Serum marker: S. Ca 15-3. (Book p71)")
q(71, "Follow up & Treatment Summary", "In early breast cancer (T1, T2/N0, N1/M0), if N0 the nodal procedure is:",
  ["SLNB", "Full axillary clearance", "No nodal surgery", "Radiotherapy to axilla"], 0,
  "Sx: 1. BCS; 2. If N0 → SLNB; 3. If BCS C/I → mastectomy. (Book p71)")
q(71, "Follow up & Treatment Summary", "In early breast cancer, BCS is contraindicated; the surgical alternative is:",
  ["Mastectomy", "SLNB", "RT alone", "Observation"], 0,
  "If BCS C/I → mastectomy. (Book p71)")
q(71, "Follow up & Treatment Summary", "In early breast cancer, radiotherapy (RT) is indicated after:",
  ["BCS and in LN +ve disease", "Mastectomy for T1N0", "SLNB alone", "Hormonal therapy only"], 0,
  "RT indications in summary: BCS; LN +ve. (Book p71)")
q(71, "Follow up & Treatment Summary", "Hormonal therapy in the early breast cancer summary is given when:",
  ["ER, PR +ve", "ER, PR -ve", "Her 2 neu +ve", "Always"], 0,
  "Hormonal: ER, PR +ve. (Book p71)")
q(71, "Follow up & Treatment Summary", "In early breast cancer with ER, PR ± and LOW risk on molecular tests:",
  ["Avoid chemo", "Give chemo", "Give trastuzumab", "Give RT only"], 0,
  "T1, T2/N0, N1/M0 & ER, PR ± → molecular tests: Low risk → Avoid chemo; High risk → Give chemo. (Book p71)")
q(71, "Follow up & Treatment Summary", "Which subtypes receive chemotherapy regardless of molecular testing?",
  ["TNBC and Her 2 neu +ve", "ER +ve low risk", "LCIS", "T1N0 lobular"], 0,
  "TNBC, Her 2 neu +ve → Chemo. (Book p71)")

# ---------------- p72 · LABC & METASTATIC DISEASE ----------------
q(72, "LABC & Metastatic Disease", "Criteria for LABC include T3N1M0 and:",
  ["Any T4, any N2, any N3 (M0)", "T1N0M0", "Only T2N1", "Any M1"], 0,
  "LABC criteria: T3N1M0, Any T4, Any N2, Any N3 → M0. (Book p72)")
q(72, "LABC & Metastatic Disease", "Peau d' orange corresponds to which T stage?",
  ["T4b", "T1", "T2", "T3"], 0,
  "Peau d' orange = T4b (shown with LABC). (Book p72)")
q(72, "LABC & Metastatic Disease", "The management sequence of LABC is:",
  ["NACT → Sx (BCS/mastectomy) → RT", "Sx → NACT → RT", "RT → Sx → NACT", "HT → Sx → RT"], 0,
  "Mx of LABC: NACT → Sx (BCS/mastectomy) → RT. (Book p72)")
q(72, "LABC & Metastatic Disease", "In LABC that is ER, PR +ve, what is added to treatment?",
  ["Hormonal therapy", "Olaparib", "Lapatinib", "Bisphosphonates"], 0,
  "ER, PR +ve → Hormonal therapy. (Book p72)")
q(72, "LABC & Metastatic Disease", "In Her 2 neu +ve LABC, the targeted drug and its duration is:",
  ["Trastuzumab for 1 year", "Lapatinib for 6 months", "TDM1 for 2 years", "Pertuzumab for 5 years"], 0,
  "Her 2 neu +ve → Trastuzumab (For 1 year). (Book p72)")
q(72, "LABC & Metastatic Disease", "Metastatic breast cancer is defined by:",
  ["M1", "T4", "N3", "Any T with LVI"], 0,
  "Metastatic breast cancer: Criteria: M1. (Book p72)")
q(72, "LABC & Metastatic Disease", "The aim of treatment in metastatic breast cancer is:",
  ["Palliative", "Curative", "Prophylactic", "Neoadjuvant"], 0,
  "Mx of metastatic disease: Palliative. (Book p72)")
q(72, "LABC & Metastatic Disease", "In metastatic breast cancer, Olaparib is used if:",
  ["BRCA +ve", "ER +ve", "Her 2 neu +ve", "PD-L1 +ve"], 0,
  "Olaparib is used if BRCA +ve. (Book p72)")

# ---------------- p72 · METASTATIC SUBTYPE-DIRECTED THERAPY ----------------
q(72, "Metastatic Subtype-directed Therapy", "In ER, PR +ve / Her 2 neu -ve metastatic disease, hormonal therapy is combined with:",
  ["CDK 4/6 inhibitors (Palbociclib, Ribociclib, Abemaciclib)", "Pembrolizumab", "Trastuzumab", "Methotrexate"], 0,
  "ER, PR +ve Her2-: Hormonal therapy + CD 4/6 (-) inhibitors: Palbociclib, Ribociclib, Abemaciclib. (Book p72)")
q(72, "Metastatic Subtype-directed Therapy", "If resistance develops in ER/PR +ve metastatic disease, the options are:",
  ["Chemo, Zoladex (LHRH analogues), Fulvestrant (HT)", "Lapatinib", "TDM1", "Pembrolizumab"], 0,
  "If resistance develops: Chemo; Zoladex (LHRH analogues); Fulvestrant (HT). (Book p72)")
q(72, "Metastatic Subtype-directed Therapy", "Fulvestrant works as:",
  ["Hormonal therapy (HT)", "CDK 4/6 inhibitor", "Anti-Her 2 neu", "Chemotherapy"], 0,
  "Fulvestrant (HT). (Book p72)")
q(72, "Metastatic Subtype-directed Therapy", "In metastatic TNBC, chemo is combined with:",
  ["Pembrolizumab and Atezolizumab (PD-L1)", "Palbociclib", "Trastuzumab", "Tamoxifen"], 0,
  "TNBC: Chemo + Pembrolizumab/Atezolizumab (PDL1). (Book p72)")
q(72, "Metastatic Subtype-directed Therapy", "In metastatic Her 2 neu +ve disease, chemo is combined with:",
  ["Trastuzumab", "Lapatinib first line", "Fulvestrant", "Ribociclib"], 0,
  "Her 2 neu +: Chemo + Trastuzumab. (Book p72)")
q(72, "Metastatic Subtype-directed Therapy", "If resistance develops in Her 2 neu +ve metastatic disease, the ORAL anti-Her 2 drug that crosses the blood-brain barrier (brain mets) is:",
  ["Lapatinib", "TDM1", "Pertuzumab", "Trastuzumab"], 0,
  "Lapatinib (Oral anti Her 2 neu) - Rx of brain mets (Cross blood brain barrier). (Book p72)")
q(72, "Metastatic Subtype-directed Therapy", "The IV anti-Her 2 neu agent used after resistance is:",
  ["TDM1", "Lapatinib", "Palbociclib", "Olaparib"], 0,
  "TDM1 (IV anti Her 2 neu). (Book p72)")

# ---------------- p72-73 · PREGNANCY ASSOCIATED BREAST CANCER ----------------
q(72, "Pregnancy Associated Breast Cancer", "Pregnancy associated breast cancer is breast cancer occurring:",
  ["During pregnancy or within 1 year of delivery", "Only during pregnancy", "Within 5 years of delivery", "During lactation only"], 0,
  "Criteria: Breast cancer during pregnancy / within 1 year of delivery. (Book p72)")
q(72, "Pregnancy Associated Breast Cancer", "Pregnancy associated breast cancers are typically:",
  ["ER, PR -ve and aggressive", "ER, PR +ve and indolent", "Her 2 neu +ve only", "LCIS"], 0,
  "Features: ER, PR -ve; Aggressive tumors. (Book p72)")
q(72, "Pregnancy Associated Breast Cancer", "Diagnosis of pregnancy associated breast cancer is by:",
  ["Core biopsy", "FNAC only", "PET scan", "Mammogram"], 0,
  "Diagnosis: Core biopsy. (Book p72)")
q(72, "Pregnancy Associated Breast Cancer", "The investigation of choice (IOC) in pregnancy is:",
  ["USG", "Mammogram", "CT", "PET"], 0,
  "Ix: USG (IOC). (Book p72)")
q(73, "Pregnancy Associated Breast Cancer", "In the 1st trimester, the surgery of choice is:",
  ["Mastectomy", "BCS with immediate RT", "SLNB only", "No surgery ever"], 0,
  "Sx: Mastectomy in 1st trimester; BCS in 2nd/3rd trimester → RT after delivery. (Book p73)")
q(73, "Pregnancy Associated Breast Cancer", "BCS in pregnancy is done in the 2nd/3rd trimester; RT is given:",
  ["After delivery", "Immediately in 2nd trimester", "During 3rd trimester", "Never"], 0,
  "BCS in 2nd/3rd trimester → RT after delivery. (Book p73)")
q(73, "Pregnancy Associated Breast Cancer", "Chemotherapy in pregnancy is:",
  ["C/I in 1st trimester; safe in 2nd/3rd trimester", "Safe in all trimesters", "C/I in all trimesters", "Safe only in 1st trimester"], 0,
  "Chemo: C/I in 1st trimester; Safe in 2nd/3rd trimester. (Book p73)")
q(73, "Pregnancy Associated Breast Cancer", "Hormonal therapy and RT during pregnancy are:",
  ["C/I in all trimesters", "Safe in 2nd trimester", "Safe in 3rd trimester", "C/I only in 1st trimester"], 0,
  "HT & RT: C/I in all trimesters. (Book p73)")

# ---------------- p73 · BILATERAL & MALE BREAST CARCINOMA ----------------
q(73, "Bilateral & Male Breast Carcinoma", "Bilateral breast carcinoma is usually:",
  ["BRCA (+) with lobular histology", "BRCA negative with ductal histology", "Unrelated to genetics", "Always comedo type"], 0,
  "Features: Usually BRCA (+); Lobular histology. (Book p73)")
q(73, "Bilateral & Male Breast Carcinoma", "If bilateral breast cancers are diagnosed at the same time:",
  ["Both are staged separately", "They are staged as one cancer", "Only the larger one is staged", "Staging is not needed"], 0,
  "Dx: If diagnosed at the same time → Both staged separately. (Book p73)")
q(73, "Bilateral & Male Breast Carcinoma", "Treatment of bilateral breast carcinoma is governed by:",
  ["The more advanced/aggressive cancer", "The smaller cancer", "Always bilateral mastectomy only", "LCIS protocol"], 0,
  "Treatment: Governed by more advance/aggressive cancer. (Book p73)")
q(73, "Bilateral & Male Breast Carcinoma", "The most important BRCA risk factor for male breast cancer is:",
  ["BRCA 2 > BRCA 1", "BRCA 1 only", "No BRCA link", "BRCA 2 only in females"], 0,
  "Risk factors: 1. BRCA 2 > 1; 2. Obesity; 3. Klinefelter syndrome; 4. Alcohol intake; 5. Liver cirrhosis. (Book p73)")
q(73, "Bilateral & Male Breast Carcinoma", "Which syndrome is a risk factor for male breast cancer?",
  ["Klinefelter syndrome", "Turner syndrome", "Down syndrome", "Marfan syndrome"], 0,
  "Risk factor #3: Klinefelter syndrome. (Book p73)")
q(73, "Bilateral & Male Breast Carcinoma", "Besides BRCA2, risk factors for male breast cancer include:",
  ["Obesity, alcohol intake and liver cirrhosis", "Smoking only", "Early puberty", "High testosterone"], 0,
  "Obesity, alcohol intake, liver cirrhosis (with Klinefelter). (Book p73)")
q(73, "Bilateral & Male Breast Carcinoma", "The clinical feature of male breast cancer is:",
  ["Hard mass/lump", "Diffuse tenderness", "Skin rash", "Galactorrhea only"], 0,
  "C/F: Hard mass/lump. (Book p73)")
q(73, "Bilateral & Male Breast Carcinoma", "Diagnosis of male breast cancer is by:",
  ["Biopsy", "USG only", "Serum PSA", "Clinical exam alone"], 0,
  "Diagnosis: Biopsy. (Book p73)")
q(73, "Bilateral & Male Breast Carcinoma", "Mx & prognosis of male breast cancer is:",
  ["Same as female breast cancer", "Worse with no treatment options", "Better and needs no therapy", "Only palliative"], 0,
  "Mx & prognosis: Same as female breast cancer. (Book p73)")

# ---------------- p73-74 · DCIS & VAN NUYS ----------------
q(73, "DCIS & Van Nuys", "Ductal carcinoma in situ (DCIS) is:",
  ["Non invasive", "Invasive by definition", "Always metastatic", "A lobular lesion"], 0,
  "DCIS: Non invasive. (Book p73)")
q(73, "DCIS & Van Nuys", "The most common type of DCIS is:",
  ["Papillary", "Comedo", "Solid", "Cribriform"], 0,
  "Types: Papillary (m/c), Cribriform, Solid, Comedo. (Book p73)")
q(73, "DCIS & Van Nuys", "Papillary, cribriform and solid DCIS types are typically:",
  ["ER, PR (+) with microcalcification (+)", "ER, PR -ve with no calcification", "Necrotic and aggressive", "Invasive"], 0,
  "Papillary/Cribriform/Solid: ER, PR (+); microcalcification (+). (Book p73)")
q(73, "DCIS & Van Nuys", "The most aggressive type of DCIS is:",
  ["Comedo (with necrosis)", "Papillary", "Cribriform", "Solid"], 0,
  "Comedo: With necrosis = most aggressive. (Book p73)")
q(73, "DCIS & Van Nuys", "Comedo DCIS is typically:",
  ["ER, PR -ve and presents as a lump", "ER, PR +ve with microcalcification only", "Non palpable always", "Bilateral always"], 0,
  "Comedo: ER, PR -ve; Presents as a lump. (Book p73)")
q(73, "DCIS & Van Nuys", "On mammogram, DCIS classically shows:",
  ["Clustered microcalcifications", "A spiculated mass", "Architectural distortion only", "A cyst"], 0,
  "Clustered microcalcifications on mammogram. (Book p73)")
q(74, "DCIS & Van Nuys", "Diagnosis of DCIS is by:",
  ["Image guided core biopsy", "Clinical exam", "Serum Ca 15-3", "USG alone"], 0,
  "Diagnosis: Image guided core biopsy. (Book p74)")
q(74, "DCIS & Van Nuys", "Surgical options for DCIS are:",
  ["Simple mastectomy or BCS + RT", "Radical mastectomy always", "SLNB only", "No surgery"], 0,
  "Mx: Sx → Simple mastectomy OR BCS → RT. (Book p74)")
q(74, "DCIS & Van Nuys", "BCS is contraindicated in DCIS when:",
  ["Extensive microcalcification (+)", "Microcalcification is focal", "Tumor is papillary", "Patient is ER +ve"], 0,
  "BCS is C/I if extensive microcalcification (+). (Book p74)")
q(74, "DCIS & Van Nuys", "The role of chemotherapy in DCIS is:",
  ["No role", "First line", "After RT", "Only in comedo type"], 0,
  "No role of chemo. (Book p74)")
q(74, "DCIS & Van Nuys", "Hormonal therapy in DCIS is given when:",
  ["ER, PR +ve", "Always", "Never", "Only after mastectomy"], 0,
  "HT: ER, PR +ve. (Book p74)")
q(74, "DCIS & Van Nuys", "Parameters of the Van Nuys prognostic index are:",
  ["Size, margins, grade & necrosis, age", "ER, PR, Her2, Ki-67", "T stage, N stage, M stage, grade", "Age, sex, BMI, smoking"], 0,
  "Van Nuys parameters: Size; Margins; Grade & necrosis; Age. (Book p74)")
q(74, "DCIS & Van Nuys", "Which is NOT included in the Van Nuys prognostic index?",
  ["ER, PR status", "Size", "Margins", "Age"], 0,
  "ER, PR status not included. (Book p74)")
q(74, "DCIS & Van Nuys", "A LOW Van Nuys score means:",
  ["RT can be avoided", "RT is mandatory", "Mastectomy is mandatory", "Chemo is given"], 0,
  "Low score → RT can be avoided. (Book p74)")
q(74, "DCIS & Van Nuys", "An INTERMEDIATE Van Nuys score is managed with:",
  ["RT given", "No treatment", "Mastectomy", "Chemo"], 0,
  "Intermediate → RT given. (Book p74)")
q(74, "DCIS & Van Nuys", "A HIGH Van Nuys score is managed with:",
  ["Mastectomy", "RT alone", "Observation", "HT alone"], 0,
  "High score → Mastectomy. (Book p74)")

# ---------------- p74 · LCIS ----------------
q(74, "LCIS", "LCIS is now classified as:",
  ["A risk factor for Ca breast (1%/year risk of conversion)", "An invasive cancer", "A metastatic lesion", "A benign cyst"], 0,
  "LCIS now classified as risk factor for Ca breast (1%/year risk of conversion). (Book p74)")
q(74, "LCIS", "The annual risk of conversion of LCIS to invasive cancer is:",
  ["1%/year", "10%/year", "0.1%/year", "25%/year"], 0,
  "1%/year risk of conversion. (Book p74)")
q(74, "LCIS", "Features of LCIS include:",
  ["B/L, multicentric and ER, PR +ve", "Unilateral and ER -ve", "Comedo necrosis", "Microcalcifications only"], 0,
  "Features: B/L, multicentric; ER, PR +ve. (Book p74)")
q(74, "LCIS", "LCIS is usually diagnosed:",
  ["As an incidental diagnosis", "By a palpable lump", "By nipple discharge", "By peau d' orange"], 0,
  "Dx: Usually an incidental diagnosis. (Book p74)")
q(74, "LCIS", "Management of LCIS is:",
  ["Patient is kept under surveillance", "Mastectomy always", "Chemotherapy", "RT"], 0,
  "Mx: Patient is kept under surveillance. (Book p74)")
q(74, "LCIS", "LCIS can progress to:",
  ["Invasive ductal and invasive lobular carcinoma", "Only DCIS", "Fibroadenoma", "Phyllodes"], 0,
  "Progression: LCIS → Invasive ductal / Invasive lobular. (Book p74)")
q(74, "LCIS", "Invasive lobular carcinoma is characteristically:",
  ["B/L multicentric with E cadherin mutation (+)", "Unilateral unifocal", "E cadherin intact", "Treated with BCS always"], 0,
  "Invasive lobular: B/L multicentric (BCS is C/D); E cadherin mutation (+). (Book p74)")
q(74, "LCIS", "In invasive lobular carcinoma, BCS is:",
  ["Contraindicated (B/L multicentric)", "The treatment of choice", "Done with RT", "Done in 1st trimester"], 0,
  "B/L multicentric (BCS is C/D). (Book p74)")
q(74, "LCIS", "The HPE pattern of invasive lobular cancer is:",
  ["Indian or single file pattern", "Cribriform pattern", "Comedo necrosis", "Papillary fronds"], 0,
  "HPE of invasive lobular cancer: Indian or single file pattern. (Book p74)")
q(74, "LCIS", "CDH gene mutation with ↓/loss of E-cadherin leads to invasive lobular carcinoma and:",
  ["Diffuse gastric cancer", "Colon cancer", "Hepatocellular carcinoma", "Renal cell carcinoma"], 0,
  "CDH gene mutation → ↓/loss of E-cadherin → Invasive lobular Ca + Diffuse gastric Ca. (Book p74)")

# ---------------- units ----------------
def sec_ids(*labels):
    return [x["id"] for x in Q if x["sec"] in labels]

def first_page(label):
    for x in Q:
        if x["sec"] == label:
            return x["page"]
    return 0

UNIT_DEFS = [
    ("Chemotherapy Indications & NACT", ("Chemotherapy Indications & NACT",),
     "Chemo is for +ve nodes, locally advanced disease, ER/PR -ve, Her2 +ve and metastasis; NACT is for LABC, TNBC, HER2 +ve and large tumors wanting BCS - it downstages, cuts micrometastasis and gives an in vivo chemosensitivity readout."),
    ("RECIST Criteria", ("RECIST Criteria",),
     "RECIST grades response in solid tumors: CR wipes out all lesions and pathological nodes, pCR is highest in TNBC, PR needs ≥30% fall in single largest diameter with no new/progressing lesions, SD is neither PR nor PD, and PD is ≥20% rise, progression or new lesions."),
    ("Chemoport & Regimens", ("Chemoport & Regimens",),
     "The chemoport sits below the clavicle with its tip in the SVC just above the right atrium, sparing veins from thrombophlebitis. Old CAF/CMF is retired; Her2 -ve gets 4 cycles AC/EC then 4 cycles T (paclitaxel causes peripheral neuropathy), Her2 +ve gets 6 cycles TCH + P with Herceptin and Pertuzumab as the anti-Her2 duo."),
    ("Avoiding Chemo & Molecular Tests", ("Avoiding Chemo & Molecular Tests",),
     "Skip chemo in poor performance status and low-risk molecular profiles (T1/T2, N0/N1, M0, ER±, Her2 -ve). The assays: Oncotype Dx 21 genes, Mammaprint 70, Endopredict 12, PAM 50 fifty, and CAN assist is the Indian test; low risk avoids chemo, high risk gets it."),
    ("Radiotherapy: WBI vs APBI", ("Radiotherapy: WBI vs APBI",),
     "RT follows BCS always and covers +ve nodes, >5 cm tumors and LABC. WBI bathes breast plus axillary, infra/supraclavicular and internal mammary nodes over 25 days (50-54 Gy); APBI shrinks this to partial breast, 5 days (30-34 Gy) with cavity electrodes, for T1, ER/PR +, no LVI, unifocal, -ve margins, ≥50 years."),
    ("Hormonal Therapy", ("Hormonal Therapy",),
     "Either ER or PR +ve qualifies. Pre-menopausal women take tamoxifen (SERM) 5 years (up to 10) with hot flashes, endometrial hyperplasia and DVT; post-menopausal get letrozole/anastrozole 5-10 years with osteoporosis - baseline DEXA first, vit D3/Ca/bisphosphonate if low. Pause for pregnancy only after 2 full years, stopping 3 months before conception."),
    ("Prognostic Factors", ("Prognostic Factors",),
     "Axillary LN status is the single most important prognosticator, replaced by ER/PR status in metastatic disease. Poor disease factors: bigger, higher stage/grade, nodal spread, metaplastic variant, LVI, extensive DCIS, high Ki-67; poor patient factors: young, premenopausal, BRCA, family/prior history, obesity and unfinished treatment."),
    ("Follow up & Treatment Summary", ("Follow up & Treatment Summary",),
     "Review 3-monthly for 2 years, 6-monthly to 5 years, yearly after; physical exam every visit, mammogram/USG yearly, pelvic USG for tamoxifen endometrium, and S. Ca 15-3 as marker. Early cancer: BCS with SLNB if N0 (mastectomy if BCS C/I), RT after BCS or with +ve nodes, HT if ER/PR +ve, chemo only for high-risk molecular or TNBC/Her2 +ve."),
    ("LABC & Metastatic Disease", ("LABC & Metastatic Disease",),
     "LABC = T3N1M0 or any T4/N2/N3 (peau d' orange is T4b), treated NACT → surgery → RT, plus HT if ER/PR +ve and a year of trastuzumab if Her2 +ve. Metastatic (M1) disease is palliative; BRCA +ve tumors get Olaparib."),
    ("Metastatic Subtype-directed Therapy", ("Metastatic Subtype-directed Therapy",),
     "ER/PR +ve Her2- metastases: hormonal therapy plus CDK4/6 inhibitors (palbociclib, ribociclib, abemaciclib), switching to chemo, Zoladex or fulvestrant on resistance. TNBC adds pembrolizumab/atezolizumab (PD-L1); Her2 +ve adds trastuzumab, then lapatinib orally for brain mets or IV TDM1 when resistance appears."),
    ("Pregnancy Associated Breast Cancer", ("Pregnancy Associated Breast Cancer",),
     "Cancer during pregnancy or within a year of delivery - ER/PR -ve, aggressive, diagnosed by core biopsy with USG as IOC. Mastectomy in 1st trimester, BCS in 2nd/3rd with RT after delivery; chemo C/I in 1st but safe later; HT and RT C/I in all trimesters."),
    ("Bilateral & Male Breast Carcinoma", ("Bilateral & Male Breast Carcinoma",),
     "Bilateral disease is usually BRCA (+) lobular, staged separately when synchronous and treated per the more aggressive side. Male cancer rides on BRCA2 > BRCA1, obesity, Klinefelter, alcohol and cirrhosis, presents as a hard lump, is biopsied and managed exactly like female breast cancer."),
    ("DCIS & Van Nuys", ("DCIS & Van Nuys",),
     "DCIS is non invasive: papillary (m/c), cribriform and solid are ER/PR + with clustered microcalcifications, while comedo with necrosis is the aggressive ER/PR -ve lump-former. Image-guided core biopsy diagnoses; simple mastectomy or BCS + RT treats (BCS C/I if extensive calcification), chemo has no role, HT if ER/PR +ve. Van Nuys scores size, margins, grade & necrosis, age (not ER/PR): low avoids RT, intermediate gets RT, high gets mastectomy."),
    ("LCIS", ("LCIS",),
     "LCIS is now a risk marker (1%/year conversion), B/L multicentric, ER/PR +ve, found incidentally and kept under surveillance. It progresses to invasive ductal or lobular cancer; invasive lobular is B/L multicentric (BCS C/D) with E-cadherin loss, Indian/single-file cells, and CDH mutation also drives diffuse gastric cancer."),
]

UNITS = []
for i, (title, labels, guide) in enumerate(UNIT_DEFS, 1):
    UNITS.append({"id": f"SURG-U12-{i}", "ch": 12, "n": i, "title": title,
                  "sec": f"{labels[0]} · p{first_page(labels[0])}",
                  "qs": sec_ids(*labels), "guide": guide})

covered = [i for u in UNITS for i in u["qs"]]
assert covered == [x["id"] for x in Q], "units must cover questions in order"

data = {"questions": Q, "units": UNITS}
with open("data/ch12.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
print(f"ch12: {len(Q)} questions, {len(UNITS)} units")
