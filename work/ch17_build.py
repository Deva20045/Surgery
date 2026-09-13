#!/usr/bin/env python3
"""Build data/ch17.json for PULSE Surgery ch17 (Parathyroid, book p111-116)."""
import json

Q = []
def q(page, sec, text, opts, ans, exp):
    Q.append({"id": f"SURG-C17-{len(Q)+1:03d}", "sec": sec, "page": page,
              "q": text, "opts": opts, "ans": ans, "exp": exp})

# ---------------- p111 · SURGICAL ANATOMY & PHYSIOLOGY ----------------
S1 = "Surgical Anatomy & Physiology"
q(111, S1, "The superior parathyroid gland originates from:",
  ["4th pharyngeal pouch", "3rd pharyngeal pouch", "2nd pharyngeal pouch", "Ultimobranchial body"], 0,
  "Superior parathyroid: 4th pharyngeal pouch. (Book p111)")
q(111, S1, "The location of the superior parathyroid gland is:",
  ["Constant: posterior aspect of thyroid lobe", "Variable, anterior to the thyroid", "Constant: anterior aspect of thyroid lobe", "Always inside the thymus"], 0,
  "Superior parathyroid location constant: posterior aspect of thyroid lobe. (Book p111)")
q(111, S1, "The inferior parathyroid gland originates from:",
  ["3rd pharyngeal pouch", "4th pharyngeal pouch", "1st pharyngeal pouch", "Neural crest only"], 0,
  "Inferior parathyroid: 3rd pharyngeal pouch; location variable. (Book p111)")
q(111, S1, "The thymus is also derived from the 3rd pharyngeal pouch; therefore in parathyroid surgery the thymus is removed along with the:",
  ["Inferior parathyroid gland", "Superior parathyroid gland", "Thyroid isthmus", "Both superior glands"], 0,
  "Thymus also from 3rd pouch - removed along with inf. parathyroid gland in parathyroid Sx → ↑ yield. (Book p111)")
q(111, S1, "What percentage of people have 5 parathyroid glands?",
  ["5%", "1%", "10%", "25%"], 0,
  "5% have 5 parathyroid glands. (Book p111)")
q(111, S1, "Parathyroid glands are identified intraoperatively by the:",
  ["Sentinel pad of fat (golden yellow)", "Pearly white capsule", "Bluish cystic appearance", "Visible pulsatility"], 0,
  "Identification: sentinel pad of fat (golden yellow). (Book p111)")
q(111, S1, "On touch, the parathyroid gland:",
  ["Turns dusky", "Turns bright red", "Becomes pearly white", "Shrinks instantly"], 0,
  "Turns dusky on touch. (Book p111)")
q(111, S1, "The half-life of PTH and its function are:",
  ["T½ 5-7 mins; ↑ plasma Ca2+ concentration", "T½ 5-7 secs; ↓ plasma Ca2+", "T½ 30-60 mins; ↑ plasma K+", "T½ 24 hrs; ↓ plasma Ca2+"], 0,
  "Secretes parathyroid hormones (PTH), T 1/2: 5-7 mins; function: ↑ plasma Ca2+ concentration. (Book p111)")

# ---------------- p111-112 · CLINICAL FEATURES OF HYPERPARATHYROIDISM ----------------
S2 = "Clinical Features of Hyperparathyroidism"
q(111, S2, "The mnemonic for clinical features of hyperparathyroidism is:",
  ["Bones, stones, abdominal groans, psychiatric overtones", "Stones, bones, groans and moans only", "Pain, pallor, palpitations, perspiration", "Bones, stones, tetany and tremors"], 0,
  "Mnemonic: Bones, stones, abdominal groans, psychiatric overtones. (Book p111)")
q(111, S2, "Which fracture pattern is part of the 'bones' of hyperparathyroidism?",
  ["Pathological fracture", "Greenstick fracture", "March fracture", "Avulsion fracture"], 0,
  "Bones: pathological fracture, subperiosteal resorption, salt & pepper skull, brown tumors. (Book p111)")
q(111, S2, "Subperiosteal bone resorption in hyperparathyroidism is m/c in the:",
  ["Radial aspect", "Ulnar aspect", "Medial tibial aspect", "Femoral head"], 0,
  "Subperiosteal bone resorption: m/c in radial aspect. (Book p111)")
q(111, S2, "The 'salt & pepper' appearance of hyperparathyroidism is seen in the:",
  ["Skull", "Hand", "Pelvis", "Vertebrae"], 0,
  "Salt & pepper skull. (Book p111)")
q(111, S2, "Brown tumors of hyperparathyroidism are also known as:",
  ["Osteitis fibrosa cystica / von Recklinghausen disease of bone", "Osteitis deformans / Paget disease", "Osteogenesis imperfecta", "Fibrous dysplasia"], 0,
  "Brown tumors: osteitis fibrosa cystica / von Recklinghausen disease of bone. (Book p111)")
q(112, S2, "Renal stones in hyperparathyroidism are typically:",
  ["Recurrent & multiple", "Single & asymptomatic", "Always radiolucent", "Uric acid type only"], 0,
  "Stones: recurrent & multiple renal stones (m/c). (Book p112)")
q(112, S2, "The m/c renal stone in hyperparathyroidism, which is radiopaque, is:",
  ["Calcium oxalate", "Uric acid", "Cystine", "Struvite"], 0,
  "Calcium oxalate stone: renal stones (m/c) → radiopaque. (Book p112)")
q(112, S2, "The 'abdominal groans' of hyperparathyroidism include abdominal colic and:",
  ["Pancreatitis", "Appendicitis", "Cholecystitis", "Intussusception"], 0,
  "Abdominal groans: abdominal colic, pancreatitis. (Book p112)")

# ---------------- p112 · PRIMARY HYPERPARATHYROIDISM: CAUSES, RISK FACTORS & INVESTIGATION ----------------
S3 = "Primary Hyperparathyroidism: Causes, Risk Factors & Investigation"
q(112, S3, "The m/c cause of primary hyperparathyroidism is:",
  ["Adenoma", "Hyperplasia", "Carcinoma", "Ectopic PTH secretion"], 0,
  "Adenoma >> hyperplasia. (Book p112)")
q(112, S3, "In primary hyperparathyroidism, adenoma versus hyperplasia means:",
  ["Enlargement of 1 gland vs all 4 glands", "Enlargement of 2 vs 3 glands", "Cystic vs solid gland", "Toxic vs non-toxic gland"], 0,
  "Adenoma: enlargement of 1 gland; hyperplasia: enlargement of all 4 glands. (Book p112)")
q(112, S3, "Risk factors for primary hyperparathyroidism are radiation exposure and:",
  ["MEN syndrome (MEN1, 2A)", "MEN2B only", "Turner syndrome", "Down syndrome"], 0,
  "Risk factors: 1. Radiation exposure 2. MEN syndrome (MEN1, 2A). (Book p112)")
q(112, S3, "MEN-syndrome-associated hyperparathyroidism is a familial syndrome showing:",
  ["Multiglandular disease (adenoma > hyperplasia)", "Single-gland atrophy", "Parathyroid cancer only", "Ectopic glands only"], 0,
  "Familial syndrome; multiglandular disease (adenoma > hyperplasia). (Book p112)")
q(112, S3, "The biochemical profile of primary hyperparathyroidism is:",
  ["↑ PTH, ↑ S. Ca2+, ↓ S. phosphorous, ↑ calcitriol", "↓ PTH, ↑ S. Ca2+, ↑ S. phosphorous", "↑ PTH, ↓ S. Ca2+, ↑ S. phosphorous", "↓ PTH, ↓ S. Ca2+, ↓ calcitriol"], 0,
  "↑ PTH; ↑ S. Ca2+ (total & ionised); ↑ U. Ca2+ & phosphate; ↓ S. phosphorous; ↑ calcitriol. (Book p112)")
q(112, S3, "The IOC investigation for a parathyroid adenoma is:",
  ["Tc99m sestamibi scan", "USG neck alone", "4D CT", "MRI neck"], 0,
  "Tc99m sestamibi scan: IOC (USG neck also part of workup). (Book p112)")
q(112, S3, "Tc99 localises in a PTH adenoma because the adenoma is rich in:",
  ["Mitochondria", "Lysosomes", "Glycogen", "Melanin"], 0,
  "Tc99 localises in PTH adenoma (rich in mitochondria). (Book p112)")
q(112, S3, "A false positive on sestamibi scan is:",
  ["Warthin tumour", "Pleomorphic adenoma", "Branchial cyst", "Thyroglossal cyst"], 0,
  "False positive: Warthin tumour (rich in mitochondria). (Book p112)")
q(112, S3, "SPECT, the m/c type of sestamibi imaging, stands for:",
  ["Single Photon Emission CT", "Single Proton Emission Count", "Sequential Photon Energy CT", "Single Photon Energy Tomography"], 0,
  "Types: single isotope dual phase; dual isotope subtraction imaging; SPECT: Single Photon Emission CT (m/c). (Book p112)")

# ---------------- p113 · LOCALISATION OF ADENOMA & MX OF ADENOMA ----------------
S4 = "Localisation of Adenoma & Mx of Adenoma"
q(113, S4, "Concordant imaging on sestamibi scan & USG leads to:",
  ["Pre-op marking with USG → minimally invasive parathyroidectomy (MIP)", "4D CT → 4 gland exploration", "Open bilateral exploration directly", "Repeat sestamibi after 6 months"], 0,
  "Concordant imaging → pre-op marking with USG → minimally invasive parathyroidectomy (MIP). (Book p113)")
q(113, S4, "Discordant imaging on sestamibi scan & USG is followed by:",
  ["4D CT", "MRI neck", "PET scan", "No further imaging"], 0,
  "Discordant imaging → 4D CT → 4 gland exploration or pre-op marking with USG and MIP. (Book p113)")
q(113, S4, "Management of a parathyroid adenoma is:",
  ["Removal of adenomatous gland (MIP or open removal)", "Total thyroidectomy", "Calcium supplementation alone", "Radioiodine ablation"], 0,
  "Mx of adenoma: removal of adenomatous gland - minimally invasive parathyroidectomy (MIP) or open removal. (Book p113)")
q(113, S4, "Steps to ensure correct gland removal in MIP are pre-op marking with USG and the:",
  ["Miami protocol", "Rome protocol", "Tokyo protocol", "Paris protocol"], 0,
  "Steps: 1. Pre-op marking with USG 2. Miami protocol. (Book p113)")
q(113, S4, "In the Miami protocol, success is confirmed when the PTH level 10-15 mins after gland removal falls by:",
  ["> 50%", "> 5%", "> 90%", "No fall required"], 0,
  "Miami protocol: pre-op PTH level → 10-15 mins after gland removal → ↓ PTH by > 50%. (Book p113)")

# ---------------- p113-114 · MANAGEMENT OF HYPERPLASIA & THYMECTOMY ----------------
S5 = "Management of Hyperplasia & Thymectomy"
q(113, S5, "Minimally invasive surgery (MIS) for parathyroid hyperplasia is indicated in:",
  ["Multigland disease, familial syndromes, lithium induced", "Single sporadic adenoma only", "Parathyroid carcinoma", "Ectopic mediastinal adenoma"], 0,
  "MIS for hyperplasia: C/I - multigland disease, familial syndromes, lithium induced. (Book p113)")
q(113, S5, "In subtotal parathyroidectomy for hyperplasia:",
  ["3½ glands removed, ½ gland retained in neck", "All 4 glands removed with autotransplant", "2 glands removed", "1 gland removed"], 0,
  "3½ glands removed, ½ gland retained in neck; disadvantage: Sx difficult in recurrence d/t fibrosis. (Book p113)")
q(113, S5, "In total parathyroidectomy with autotransplantation, ½ gland is placed in the:",
  ["Brachioradialis of the non-dominant hand", "Sternocleidomastoid", "Rectus abdominis", "Quadriceps of the dominant leg"], 0,
  "4 glands removed; ½ gland autotransplanted in brachioradialis (of non-dominant hand); advantage: easy removal in recurrence. (Book p113)")
q(113, S5, "Thymectomy during parathyroid surgery is indicated for:",
  ["Involvement of lower PTH glands, 2° hyperparathyroidism, familial syndromes", "Superior gland adenoma only", "Hypercalcemic crisis", "Hungry bone syndrome"], 0,
  "Thymectomy indication: involvement of lower PTH gland, 2° hyperparathyroidism, familial syndromes. (Book p113)")
q(114, S5, "Why is the PTH gland NOT transplanted into the sternocleidomastoid?",
  ["Injury to gland during thyroidectomy", "Poor cosmetic result", "Risk of airway obstruction", "Inadequate blood supply"], 0,
  "Note: transplantation of PTH gland in sternocleidomastoid → injury to gland during thyroidectomy. (Book p114)")

# ---------------- p114 · SX IN ASYMPTOMATIC HYPERPARATHYROIDISM & COMPLICATIONS ----------------
S6 = "Sx in Asymptomatic Hyperparathyroidism & Complications"
q(114, S6, "Indications for Sx in asymptomatic hyperparathyroidism include serum calcium:",
  ["> 1 mg/dl above reference range", "> 4 mg/dl above reference", "Equal to reference", "Below reference"], 0,
  "S. calcium > 1 mg/dl above reference range. (Book p114)")
q(114, S6, "Which complication lists as an indication for Sx in asymptomatic hyperparathyroidism?",
  ["Nephrolithiasis", "Cholelithiasis", "Appendicitis", "Pancreatic cancer"], 0,
  "Complications: e.g. nephrolithiasis; life threatening hypercalcemic episode. (Book p114)")
q(114, S6, "Severe hypercalciuria indicating surgery in asymptomatic disease is:",
  ["> 400 mg/24 hrs", "> 100 mg/24 hrs", "> 50 mg/24 hrs", "> 1000 mg/24 hrs"], 0,
  "Severe hypercalciuria (> 400 mg/24 hrs). (Book p114)")
q(114, S6, "Other indications for Sx in asymptomatic hyperparathyroidism are:",
  ["↓ bone mass (osteoporosis) and age < 50 yrs", "↑ bone mass and age > 70 yrs", "Osteopetrosis at any age", "Age > 60 yrs only"], 0,
  "↓ bone mass: osteoporosis; age < 50 yrs. (Book p114)")
q(114, S6, "Residual hyperparathyroidism is defined as ↑ PTH:",
  ["Within 6 weeks", "6 months after normalisation", "1 year after surgery", "Immediately within 24 hrs"], 0,
  "Residual hyperPTH: ↑ PTH within 6 weeks. (Book p114)")
q(114, S6, "Recurrent hyperparathyroidism is defined as ↑ PTH:",
  ["6 months after normalisation", "Within 6 weeks", "Within 48 hours", "Without ever normalising"], 0,
  "Recurrent hyperPTH: ↑ PTH 6 months after normalisation. (Book p114)")
q(114, S6, "The Casanova test measures PTH in neck & arm veins; recurrence is positive when:",
  ["Arm vein PTH = 20 × neck vein PTH", "Neck vein PTH equals arm vein PTH", "PTH is undetectable in both", "Arm vein PTH = half of neck vein PTH"], 0,
  "Casanova test: measures PTH in neck & arm veins; arm vein PTH = 20 × neck vein PTH → recurrence +ve → removal of gland. (Book p114)")
q(114, S6, "Hungry bone syndrome after PTH gland removal is:",
  ["Ca2+ influx into bones → hypocalcemia", "Ca2+ efflux from bones → hypercalcemia", "Phosphate influx into brain", "Marrow suppression"], 0,
  "Hungry bone syndrome: post PTH gland removal → Ca2+ influx into bones → hypocalcemia. (Book p114)")

# ---------------- p114 · HYPERCALCEMIC CRISIS ----------------
S7 = "Hypercalcemic Crisis"
q(114, S7, "Hypercalcemic crisis is seen in:",
  ["1° hyperparathyroidism & hypercalcemia of malignancy", "Hypoparathyroidism", "Hungry bone syndrome", "Vit D deficiency"], 0,
  "Seen in 1° hyperparathyroidism & hypercalcemia of malignancy (paraneoplastic). (Book p114)")
q(114, S7, "Hypercalcemia of malignancy (paraneoplastic) in hypercalcemic crisis is classically seen with:",
  ["Squamous cell cancer, breast cancer, prostate cancer", "Colon cancer only", "Thyroid cancer", "GIST"], 0,
  "Hypercalcemia of malignancy (paraneoplastic syndrome): squamous cell cancer, breast cancer, prostate cancer. (Book p114)")
q(114, S7, "Hypercalcemic crisis is a medical emergency defined by Ca2+:",
  ["> 14 mg/dl", "> 10 mg/dl", "> 8 mg/dl", "> 20 mg/dl"], 0,
  "Ca2+ > 14 mg/dl. (Book p114)")
q(114, S7, "Symptoms of hypercalcemic crisis include all EXCEPT:",
  ["Hyperactivity", "Confusion", "Nausea & vomiting", "Abdominal pain"], 0,
  "Symptoms: confusion, nausea & vomiting, anuria, dehydration, abdominal pain. (Book p114)")
q(114, S7, "ECG changes in hypercalcemic crisis are:",
  ["↑ PR interval, ↓ QT interval, arrhythmia", "↓ PR interval, ↑ QT interval", "Peaked T waves only", "Widened QRS only"], 0,
  "ECG changes: ↑ PR interval, ↓ QT interval, arrhythmia. (Book p114)")
q(114, S7, "Ca2+ above what level causes cardiac arrest in hypercalcemic crisis?",
  ["> 16 mg/dl", "> 14 mg/dl", "> 12 mg/dl", "> 20 mg/dl"], 0,
  "Ca2+ > 16 mg/dl → cardiac arrest. (Book p114)")
q(114, S7, "The first step in management of hypercalcemic crisis is:",
  ["Aggressive IV fluid therapy", "IV calcium gluconate", "Calcitonin", "Dialysis"], 0,
  "Aggressive IV fluid therapy: first step. (Book p114)")
q(114, S7, "The diuretic used in hypercalcemic crisis management is:",
  ["Furosemide", "Thiazide", "Spironolactone", "Acetazolamide"], 0,
  "Diuretics: furosemide. (Book p114)")
q(114, S7, "Bisphosphonates in hypercalcemic crisis (if RFT & urine output normal) act on the:",
  ["Osteoclast", "Osteoblast", "Chondrocyte", "Fibroblast"], 0,
  "Bisphosphonates if RFT & urine output are normal; acts on osteoclast; calcitonin added if zoledronic acid/denosumab is given. (Book p114)")
q(114, S7, "Dialysis in hypercalcemic crisis is reserved for:",
  ["Failure of other methods", "First-line use", "Hypocalcemia", "Routine use"], 0,
  "Dialysis: if failure of other methods. (Book p114)")

# ---------------- p115 · SECONDARY HYPERPARATHYROIDISM ----------------
S8 = "Secondary Hyperparathyroidism"
q(115, S8, "Secondary hyperparathyroidism is associated with:",
  ["PTH hyperplasia", "PTH atrophy", "Parathyroid carcinoma", "Single adenoma"], 0,
  "Associated with PTH hyperplasia. (Book p115)")
q(115, S8, "The m/c cause of secondary hyperparathyroidism is:",
  ["Chronic renal failure", "Vit D excess", "Primary adenoma", "Lithium withdrawal"], 0,
  "Chronic renal failure (m/c). (Book p115)")
q(115, S8, "In chronic renal failure, secondary hyperparathyroidism develops because of:",
  ["Failure of hydroxylation of vit D → ↓ vit D3 / ↓ S. Ca2+ → PTH hyperplasia", "Excess calcitriol", "↑ S. Ca2+", "↑ phosphate excretion"], 0,
  "Failure of hydroxylation of vit D → ↓ vit D3 / ↓ S. Ca2+ → PTH hyperplasia; reversible cause of 2° hyperPTH. (Book p115)")
q(115, S8, "Other causes of secondary hyperparathyroidism include defective intestinal absorption, vit D3 deficiency and:",
  ["Lithium intake", "Calcium excess", "Thiazides", "Radiation"], 0,
  "Causes: defective intestinal absorption, lithium intake, vit D3 deficiency. (Book p115)")
q(115, S8, "Investigations in secondary hyperparathyroidism show:",
  ["N/↓ S. Ca, ↑ S. phosphorous, ↓ calcitriol, ↑ PTH", "↑ S. Ca, ↓ S. phosphorous", "Normal PTH", "↑ calcitriol"], 0,
  "N/↓ S. Ca (total & ionized); ↑ S. phosphorous; ↓ calcitriol; ↑ PTH. (Book p115)")
q(115, S8, "The mainstay of treatment of secondary hyperparathyroidism is:",
  ["Renal transplantation", "Parathyroidectomy first-line", "Calcium restriction", "Thyroidectomy"], 0,
  "Correction of chronic renal failure; renal transplantation: mainstay of Rx. (Book p115)")
q(115, S8, "The calcimimetic used in secondary hyperparathyroidism is:",
  ["Cinacalcet", "Calcitriol", "Calcium carbonate", "Furosemide"], 0,
  "Cinacalcet: calcimimetics - acts on Ca2+ sensing receptors; ↓ requirement of Sx. (Book p115)")
q(115, S8, "Which is TRUE for secondary hyperparathyroidism?",
  ["No localisation of gland is required; surgery = mx of hyperplasia", "Sestamibi localisation is mandatory", "Surgery removes only an adenoma", "Vit D3 is contraindicated"], 0,
  "No localisation of gland required; surgery: mx of hyperplasia; also vit D3 supplementation & low phosphate diet. (Book p115)")

# ---------------- p115 · TERTIARY HYPERPARATHYROIDISM ----------------
S9 = "Tertiary Hyperparathyroidism"
q(115, S9, "Tertiary hyperparathyroidism is:",
  ["Persistent autonomous hypercalcemic hyperPTH post kidney transplant", "HyperPTH before dialysis", "HypoPTH post transplant", "Ectopic PTH from the thymus"], 0,
  "Causes: persistent autonomous hypercalcemic hyperPTH post kidney transplant. (Book p115)")
q(115, S9, "Investigations in tertiary hyperparathyroidism show:",
  ["↑ PTH, ↑ S. Ca2+, ↓ S. phosphate; USG neck confirms nodular enlargement", "↓ PTH, ↓ S. Ca2+", "Normal USG neck", "↑ S. phosphate"], 0,
  "↑ PTH; ↑ S. Ca2+; ↓ S. phosphate; USG neck: confirms nodular enlargement. (Book p115)")
q(115, S9, "Treatment of tertiary hyperparathyroidism is:",
  ["Subtotal parathyroidectomy (mainstay) or embolisation of gland", "Total thyroidectomy", "Calcitonin only", "Observation only"], 0,
  "Subtotal parathyroidectomy (mainstay); embolisation of gland. (Book p115)")

# ---------------- p115 · MISCELLANEOUS: CALCIPHYLAXIS ----------------
S10 = "Miscellaneous: Calciphylaxis"
q(115, S10, "Calciphylaxis (hypercalcemic uremic arteriopathy) is seen in:",
  ["Chronic dialysis", "Acute asthma", "Primary hyperparathyroidism", "Pregnancy"], 0,
  "Seen in chronic dialysis; hypercalcemic uremic arteriopathy. (Book p115)")
q(115, S10, "Calciphylaxis causes Ca2+ deposition in skin, blood vessels & soft tissues leading to:",
  ["Gangrene, painful purpura, calcification in breast", "Osteoporosis", "Nephrolithiasis", "Pancreatitis"], 0,
  "Ca2+ deposition → a. gangrene b. painful purpura c. calcification in breast. (Book p115)")

# ---------------- p116 · PSEUDOHYPERPARATHYROIDISM ----------------
S11 = "Pseudohyperparathyroidism"
q(116, S11, "Pseudohyperparathyroidism (AKA hypercalcemia of malignancy) is a:",
  ["PTHrp mediated paraneoplastic syndrome", "PTH mediated endocrine state", "Calcitonin mediated syndrome", "Vit D mediated syndrome"], 0,
  "AKA hypercalcemia of malignancy; paraneoplastic syndrome; PTH related peptide (PTHrp) mediated. (Book p116)")
q(116, S11, "Pseudohyperparathyroidism is m/c seen in:",
  ["Squamous cell carcinoma of lung", "Renal cell carcinoma only", "Colon cancer", "Thyroid cancer"], 0,
  "Seen in squamous cell carcinoma of lung (m/c), breast cancer, prostate cancer. (Book p116)")
q(116, S11, "Investigations in pseudohyperparathyroidism show:",
  ["↑ S. Ca, normal S. phosphorous, N/↓ calcitriol & PTH, ↑ PTHrp", "↑ PTH", "↓ S. Ca", "↑ calcitriol"], 0,
  "↑ S. Ca; normal S. phosphorous; N/↓ calcitriol, PTH; ↑ PTHrp. (Book p116)")
q(116, S11, "Management of pseudohyperparathyroidism is:",
  ["Same as hypercalcemic crisis", "Subtotal parathyroidectomy", "Cinacalcet only", "Neck exploration"], 0,
  "Same as hypercalcemic crisis. (Book p116)")

# ---------------- p116 · PARATHYROID CANCER ----------------
S12 = "Parathyroid Cancer"
q(116, S12, "Risk factors for parathyroid cancer are:",
  ["Radiation exposure & HRPT2 gene", "Lithium intake", "Vit D deficiency", "MEN2B"], 0,
  "Risk factors: radiation exposure; HRPT2 gene. (Book p116)")
q(116, S12, "HPE of parathyroid cancer shows fibrous bands & vascular invasion; IHC shows inactivation of:",
  ["Parafibromin", "Thyroglobulin", "Calcitonin", "Menin"], 0,
  "HPE: fibrous bands & vascular invasion; IHC: inactivation of parafibromin. (Book p116)")
q(116, S12, "The m/c cause of death in parathyroid cancer is:",
  ["Hypercalcemic crisis (arrhythmia)", "Airway obstruction", "Haemorrhage", "Hypocalcemia"], 0,
  "Features of hypercalcemia; hypercalcemic crisis (arrhythmia): m/c cause of death. (Book p116)")
q(116, S12, "Management of parathyroid cancer is:",
  ["Surgery: R0 resection (microscopic clearance); octreotide & cinacalcet ↓ symptoms", "Radioiodine ablation", "FNAC ablation", "Observation"], 0,
  "Surgery: R0 resection (microscopic clearance); octreotide, cinacalcet → ↓ symptoms. (Book p116)")

# ---------------- p116 · HYPOPARATHYROIDISM & DIGEORGE SYNDROME ----------------
S13 = "Hypoparathyroidism & DiGeorge Syndrome"
q(116, S13, "The m/c cause of hypoparathyroidism is:",
  ["Iatrogenic", "DiGeorge syndrome", "Autoimmune", "Magnesium excess"], 0,
  "1. Iatrogenic (m/c) 2. DiGeorge syndrome. (Book p116)")
q(116, S13, "DiGeorge syndrome (mnemonic CATCH 22) is caused by:",
  ["Deletion of 22q11", "Trisomy 21", "Deletion of 11p", "RET mutation"], 0,
  "Deletion of 22q11. (Book p116)")
q(116, S13, "The 'H' in the CATCH 22 mnemonic of DiGeorge syndrome stands for:",
  ["Hypocalcemia", "Hypercalcemia", "Hypokalemia", "Hyperkalemia"], 0,
  "CATCH 22: Cardiac anomalies, Atypical facies, Thymic hypoplasia, Cleft lip & palate, Hypocalcemia; 22 = deletion 22q11. (Book p116)")

# ---------------- units ----------------
def sec_ids(*labels):
    return [x["id"] for x in Q if x["sec"] in labels]
def first_page(label):
    for x in Q:
        if x["sec"] == label:
            return x["page"]
    return 0

UNIT_DEFS = [
    (S1, "Superior parathyroid from 4th pouch (constant, posterior thyroid), inferior from 3rd pouch (variable) like the thymus - so thymus goes with the inferior gland to ↑ yield; 5% have 5 glands. Identify by the golden-yellow sentinel fat pad (turns dusky on touch); PTH (t½ 5-7 mins) raises plasma Ca2+."),
    (S2, "Bones, stones, abdominal groans, psychiatric overtones: pathological fractures, subperiosteal resorption m/c radial side, salt & pepper skull, brown tumor = osteitis fibrosa cystica (von Recklinghausen bone disease); recurrent multiple radiopaque calcium-oxalate renal stones; colic & pancreatitis."),
    (S3, "Adenoma (1 gland) >> hyperplasia (4 glands); risks radiation & MEN1/2A (familial, multiglandular). Biochem: ↑PTH, ↑S.Ca, ↑U.Ca/phosphate, ↓S.phosphate, ↑calcitriol. Sestamibi = IOC (Tc99 sticks to mitochondria-rich adenoma; Warthin tumor false +); SPECT = Single Photon Emission CT m/c."),
    (S4, "Concordant sestamibi+USG → USG-marked MIP; discordant → 4D CT → 4-gland exploration or USG-marked MIP. Adenoma mx = remove the gland (MIP/open); correct gland ensured by USG marking + Miami protocol (PTH ↓ >50% at 10-15 min post-removal)."),
    (S5, "Hyperplasia MIS for multigland/familial/lithium: subtotal 3½ removed (½ in neck, but recurrence Sx hard d/t fibrosis) or total + ½ autotransplant in non-dominant brachioradialis (easy re-excision). Thymectomy for lower-gland involvement, 2° hyperPTH, familial; never implant into sternocleidomastoid - thyroidectomy would injure it."),
    (S6, "Asymptomatic Sx if S.Ca >1 above reference, nephrolithiasis/life-threatening episode, hypercalciuria >400mg/24h, osteoporosis, age <50. Residual = ↑PTH within 6 wks; recurrent = ↑PTH 6 months after normal (Casanova neck/arm vein test, +ve → remove gland). Hungry bone: Ca2+ floods into bones → hypocalcemia."),
    (S7, "Emergency at Ca >14 (arrest >16) in 1° hyperPTH or malignancy (squamous lung, breast, prostate). Confusion, vomiting, anuria, dehydration, abdominal pain; ECG ↑PR ↓QT arrhythmia. Rx: aggressive IV fluids first, furosemide, bisphosphonates (osteoclast) + calcitonin, dialysis if all fail."),
    (S8, "2° = PTH hyperplasia from chronic renal failure (m/c: failed vit D hydroxylation → ↓D3/↓Ca), malabsorption, lithium, D3 deficiency. N/↓ Ca, ↑ phosphate, ↓ calcitriol, ↑ PTH. Rx: fix CRF (renal transplant mainstay), D3, low-phosphate diet, cinacalcet (calcimimetic on Ca-sensing receptor); no localisation needed, surgery treats hyperplasia."),
    (S9, "Tertiary = persistent autonomous hypercalcemic hyperPTH after kidney transplant: ↑PTH, ↑Ca, ↓ phosphate, nodular glands on USG. Rx subtotal parathyroidectomy (mainstay) or gland embolisation."),
    (S10, "Calciphylaxis in chronic dialysis: hypercalcemic uremic arteriopathy - Ca2+ deposits in skin/vessels/soft tissue → gangrene, painful purpura, breast calcification."),
    (S11, "Pseudohyperparathyroidism = hypercalcemia of malignancy, PTHrp-mediated paraneoplastic (squamous lung m/c, breast, prostate): ↑Ca, normal phosphate, N/↓ PTH & calcitriol, ↑PTHrp; treat like hypercalcemic crisis."),
    (S12, "Rare cancer: radiation & HRPT2 risks; HPE fibrous bands + vascular invasion, IHC parafibromin inactivation. Death m/c from hypercalcemic crisis arrhythmia; Rx R0 resection, octreotide/cinacalcet for symptoms."),
    (S13, "Hypoparathyroidism: iatrogenic m/c then DiGeorge (CATCH 22 = 22q11 deletion: Cardiac anomalies, Atypical facies, Thymic hypoplasia, Cleft lip/palate, Hypocalcemia)."),
]

UNITS = []
for i, (title, guide) in enumerate(UNIT_DEFS, 1):
    UNITS.append({"id": f"SURG-U17-{i}", "ch": 17, "n": i, "title": title,
                  "sec": f"{title} · p{first_page(title)}",
                  "qs": sec_ids(title), "guide": guide})

covered = [i for u in UNITS for i in u["qs"]]
assert covered == [x["id"] for x in Q], "units must cover questions in order"

data = {"questions": Q, "units": UNITS}
with open("data/ch17.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
print(f"ch17: {len(Q)} questions, {len(UNITS)} units")
