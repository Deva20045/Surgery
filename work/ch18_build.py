#!/usr/bin/env python3
"""Build data/ch18.json for PULSE Surgery ch18 (Adrenal Glands and Neuroendocrine Tumors, book p117-125)."""
import json

Q = []
def q(page, sec, text, opts, ans, exp):
    Q.append({"id": f"SURG-C18-{len(Q)+1:03d}", "sec": sec, "page": page,
              "q": text, "opts": opts, "ans": ans, "exp": exp})

# ---------------- p117 · ADRENAL INCIDENTALOMA: CAUSES ----------------
S1 = "Adrenal Incidentaloma: Causes"
q(117, S1, "Adrenal incidentaloma refers to:",
  ["Incidental diagnosis of adrenal lesions", "Symptomatic adrenal mass detected clinically",
   "Adrenal lesion detected only at autopsy", "Adrenal enlargement due to chronic steroid use"], 0,
  "Adrenal incidentaloma = incidental diagnosis of adrenal lesions. (Book p117)")
q(117, S1, "The m/c cause of an adrenal incidentaloma is:",
  ["Non-functional tumors", "Metastases", "Functional tumors", "Adrenal cyst"], 0,
  "Causes of adrenal incidentaloma: non-functional tumors (m/c). (Book p117)")
q(117, S1, "Adrenal metastases detected as an incidentaloma can arise from all of the following EXCEPT:",
  ["Thyroid carcinoma", "Breast cancer", "Lung cancer", "Renal cancer"], 0,
  "Metastases causing adrenal incidentaloma: breast cancer, lung cancer, renal cancer. (Book p117)")
q(117, S1, "Functional tumors that can present as an adrenal incidentaloma include:",
  ["Cushing's syndrome", "Conn's syndrome", "Addison's disease", "Congenital adrenal hyperplasia"], 0,
  "Functional tumors listed as a cause: Cushing's syndrome. (Book p117)")
q(117, S1, "Adrenocortical carcinoma as a cause of adrenal incidentaloma is listed under:",
  ["Functional tumors", "Non-functional tumors", "Metastases", "Cystic lesions"], 0,
  "Causes: functional tumors - Cushing's syndrome, carcinoma. (Book p117)")
q(117, S1, "Benign adrenal tumors on NCCT characteristically show attenuation of:",
  ["<= 10 HU", ">= 20 HU", "30-40 HU", "> 50 HU"], 0,
  "Benign adrenal tumors on NCCT: <= 10 HU. (Book p117)")
q(117, S1, "The imaging shown in the book for an incidentally detected adrenal lesion is:",
  ["NCCT showing incidentaloma", "CECT showing incidentaloma", "MRI showing incidentaloma",
   "Ultrasound showing incidentaloma"], 0,
  "Book image: NCCT showing an incidentaloma. (Book p117)")

# ---------------- p117 · ADRENAL INCIDENTALOMA: EVALUATION ----------------
S2 = "Adrenal Incidentaloma: Evaluation"
q(117, S2, "Serum cortisol estimation in an adrenal incidentaloma is done to evaluate for:",
  ["Cushing's syndrome", "Pheochromocytoma", "Adrenocortical carcinoma", "Primary aldosteronism"], 0,
  "Evaluation of functional tumors: serum cortisol (Cushing's). (Book p117)")
q(117, S2, "Plasma free metanephrines are estimated in an adrenal incidentaloma to rule out:",
  ["Pheochromocytoma", "Cushing's syndrome", "Adrenocortical carcinoma", "Conn's syndrome"], 0,
  "Plasma free metanephrines - evaluation for pheochromocytoma. (Book p117)")
q(117, S2, "Serum DHEA is estimated in the evaluation of an adrenal incidentaloma to detect:",
  ["Adrenocortical carcinoma", "Pheochromocytoma", "Cushing's syndrome", "Myelolipoma"], 0,
  "Serum DHEA - marker for adrenocortical carcinoma. (Book p117)")
q(117, S2, "The dexamethasone suppression test in the evaluation of an adrenal incidentaloma assesses:",
  ["Cortisol excess (Cushing's)", "Catecholamine excess", "Androgen excess", "Aldosterone excess"], 0,
  "Dexamethasone suppression test & urinary cortisol - Cushing's evaluation. (Book p117)")
q(117, S2, "24 hour urinary cortisol is done in an adrenal incidentaloma as part of evaluation of:",
  ["Cushing's syndrome", "Pheochromocytoma", "Neuroblastoma", "Carcinoid syndrome"], 0,
  "Urinary cortisol - evaluation of Cushing's syndrome. (Book p117)")
q(117, S2, "On imaging, radiological features suggesting adrenal malignancy include:",
  ["Diameter >= 4 cm and > 10 HU density", "Diameter < 4 cm and < 10 HU density",
   "Diameter >= 4 cm but < 10 HU density", "Diameter < 2 cm with calcification"], 0,
  "Radiological suspicion of malignancy: diameter >= 4 cm and > 10 HU density. (Book p117)")
q(117, S2, "CECT is performed in an adrenal incidentaloma to assess:",
  ["Washout", "Calcification", "Fat content", "Septations"], 0,
  "CECT: washout - characterisation of the adrenal lesion. (Book p117)")
q(117, S2, "FDG PET suggests adrenal malignancy when it shows:",
  ["Positive uptake", "No uptake", "Photopenic defect", "Rim calcification"], 0,
  "FDG PET: positive uptake suggests malignancy. (Book p117)")
q(117, S2, "FNAC of an adrenal mass is performed:",
  ["Only after ruling out pheochromocytoma", "As the first investigation of every incidentaloma",
   "Only in lesions < 1 cm", "Never, in any adrenal lesion"], 0,
  "FNAC is done only after ruling out pheochromocytoma. (Book p117)")

# ---------------- p118 · MANAGEMENT OF UNILATERAL ADRENAL MASS ----------------
S3 = "Management of Unilateral Adrenal Mass"
q(118, S3, "The management algorithm for a unilateral adrenal mass begins with assessing:",
  ["Radiological suspicion of malignancy", "Size of the mass alone", "Patient's age",
   "Laterality of the mass"], 0,
  "Algorithm: unilateral adrenal mass - radiological suspicion of malignancy? (Book p118)")
q(118, S3, "A unilateral adrenal mass with radiological suspicion of malignancy and local invasion is treated by:",
  ["Open adrenalectomy", "Laparoscopic adrenalectomy", "No surgery", "Chemotherapy alone"], 0,
  "Local invasion (with suspicion of malignancy) - open adrenalectomy. (Book p118)")
q(118, S3, "Open adrenalectomy is preferred over the laparoscopic route when there is:",
  ["Local invasion", "A functional tumor < 4 cm", "A non-functional cyst", "Bilateral disease"], 0,
  "Open adrenalectomy is used when local invasion is present. (Book p118)")
q(118, S3, "In a unilateral adrenal mass without suspicion of malignancy, a diameter <= 6 cm is treated by:",
  ["Laparoscopic adrenalectomy", "Open adrenalectomy", "Observation only", "Radiotherapy"], 0,
  "Diameter <= 6 cm - laparoscopic adrenalectomy. (Book p118)")
q(118, S3, "For adrenal masses that do not fit the standard criteria (e.g. large but no invasion), the book advises:",
  ["Individualised surgical approach", "No surgery for all such patients",
   "Bilateral adrenalectomy", "Radiofrequency ablation in all"], 0,
  "Individualised surgical approach for masses outside standard criteria. (Book p118)")
q(118, S3, "Non-functional adrenal tumors < 4 cm or clearly benign are managed by:",
  ["No surgery, CT/MRI every 3-6 months", "Immediate adrenalectomy", "Annual X-ray alone",
   "FNAC and radiotherapy"], 0,
  "Non-functional tumors < 4 cm / benign: no surgery, CT or MRI every 3-6 months. (Book p118)")
q(118, S3, "The follow-up interval advised for small non-functional adrenal tumors is:",
  ["Every 3-6 months", "Every 2 years", "Every 5 years", "Only if symptomatic"], 0,
  "Follow up: CT/MRI every 3-6 months. (Book p118)")
q(118, S3, "Non-functional adrenal tumors >= 4 cm (or with features of malignancy / significant growth) are treated by:",
  ["Adrenalectomy", "Observation", "Chemotherapy", "Radiotherapy"], 0,
  "Non-functional tumors >= 4 cm / features of malignancy / significant growth: adrenalectomy. (Book p118)")

# ---------------- p118 · PHEOCHROMOCYTOMA BASICS & PARAGANGLIOMA ----------------
S4 = "Pheochromocytoma: Basics & Paraganglioma"
q(118, S4, "Pheochromocytoma is a tumor of the:",
  ["Adrenal medulla", "Adrenal cortex", "Sympathetic ganglion only", "Carotid body"], 0,
  "Pheochromocytoma = tumor of the adrenal medulla. (Book p118)")
q(118, S4, "The incidence of pheochromocytoma shows:",
  ["Males = females", "Male predominance 3:1", "Female predominance 3:1", "Seen only in children"], 0,
  "Incidence of pheochromocytoma: M = F. (Book p118)")
q(118, S4, "Paragangliomas are:",
  ["Extra-adrenal tumors", "Cortical adenomas", "Pituitary tumors", "Thyroid C-cell tumors"], 0,
  "Paraganglioma: extra-adrenal tumors. (Book p118)")
q(118, S4, "The m/c site of a sympathetic chain paraganglioma is the:",
  ["Organ of Zuckerkandl", "Carotid body", "Glomus jugulare", "Adrenal cortex"], 0,
  "Sympathetic chain paraganglioma - organ of Zuckerkandl (m/c site). (Book p118)")
q(118, S4, "A parasympathetic chain paraganglioma classically arises from the:",
  ["Carotid body", "Organ of Zuckerkandl", "Adrenal medulla", "Coeliac plexus"], 0,
  "Parasympathetic chain paraganglioma: carotid body. (Book p118)")
q(118, S4, "Carotid body tumors arise from the:",
  ["Parasympathetic chain", "Sympathetic chain", "Adrenal medulla", "Vagus nerve nucleus"], 0,
  "Carotid body = parasympathetic chain paraganglioma. (Book p118)")
q(118, S4, "According to the rule of 10 for pheochromocytoma, the proportion that is familial is:",
  ["10%", "1%", "25%", "50%"], 0,
  "Rule of 10: 10% familial. (Book p118)")
q(118, S4, "All of the following are part of the 'rule of 10' for pheochromocytoma EXCEPT:",
  ["10% are calcified", "10% bilateral", "10% malignant", "10% extra-adrenal"], 0,
  "Rule of 10: familial, bilateral, malignant, extra-adrenal, children - calcification is not part of it. (Book p118)")
q(118, S4, "The proportion of pheochromocytomas occurring in children is:",
  ["10%", "1%", "30%", "50%"], 0,
  "Rule of 10: 10% occur in children. (Book p118)")
q(118, S4, "The m/c syndrome associated with familial pheochromocytomas is:",
  ["MEN 2A syndrome", "MEN 1 syndrome", "MEN 2B syndrome", "Von Hippel-Lindau disease"], 0,
  "Syndrome associated with familial pheochromocytomas: MEN 2A syndrome (m/c). (Book p118)")

# ---------------- p119 · FAMILIAL PHEOCHROMOCYTOMA SYNDROMES ----------------
S5 = "Familial Pheochromocytoma Syndromes"
q(119, S5, "The gene involved in MEN 2A is:",
  ["RET", "NF1", "VHL", "SDHB"], 0,
  "MEN 2A: RET gene. (Book p119)")
q(119, S5, "The triad of medullary thyroid carcinoma, pheochromocytoma and parathyroid hyperplasia occurs in:",
  ["MEN 2A", "MEN 2B", "MEN 1", "Von Hippel-Lindau disease"], 0,
  "MEN 2A (RET): medullary thyroid carcinoma, pheochromocytoma, parathyroid hyperplasia. (Book p119)")
q(119, S5, "Parathyroid hyperplasia with pheochromocytoma is characteristic of:",
  ["MEN 2A", "MEN 2B", "VHL disease", "NF1"], 0,
  "Parathyroid hyperplasia is part of MEN 2A. (Book p119)")
q(119, S5, "The gene involved in MEN 2B is:",
  ["RET", "NF1", "SDHD", "VHL"], 0,
  "MEN 2B: RET gene. (Book p119)")
q(119, S5, "Marfanoid habitus with pheochromocytoma is characteristic of:",
  ["MEN 2B", "MEN 2A", "NF1", "Familial paraganglioma type 3"], 0,
  "MEN 2B: pheochromocytoma, medullary thyroid carcinoma, marfanoid habitus, mucocutaneous ganglioneuromas. (Book p119)")
q(119, S5, "Mucocutaneous ganglioneuromas are a feature of:",
  ["MEN 2B", "MEN 2A", "VHL disease", "Carney triad"], 0,
  "Mucocutaneous ganglioneuromas: MEN 2B. (Book p119)")
q(119, S5, "The NF1 gene product is:",
  ["Neurofibromin", "Succinate dehydrogenase", "Ret proto-oncogene", "VHL protein"], 0,
  "NF1 - neurofibromin. (Book p119)")
q(119, S5, "Cafe-au-lait spots, neurofibromas and optic nerve glioma with pheochromocytoma suggest:",
  ["Neurofibromatosis type 1", "MEN 2B", "VHL disease", "Tuberous sclerosis"], 0,
  "NF1: neurofibromas, cafe-au-lait spots, optic nerve glioma, pheochromocytoma. (Book p119)")
q(119, S5, "Optic nerve glioma with pheochromocytoma is associated with:",
  ["NF1", "MEN 2A", "MEN 2B", "VHL disease"], 0,
  "Optic nerve glioma: NF1. (Book p119)")
q(119, S5, "The gene involved in Von Hippel-Lindau disease is:",
  ["VHL", "RET", "NF1", "SDHB"], 0,
  "Von Hippel-Lindau (VHL) disease: VHL gene. (Book p119)")
q(119, S5, "Hemangioblastoma with pheochromocytoma suggests:",
  ["Von Hippel-Lindau disease", "MEN 2A", "NF1", "Familial paraganglioma type 1"], 0,
  "VHL: pheochromocytoma, renal cell carcinoma, paraganglioma, hemangioblastoma, pancreatic endocrine neoplasm. (Book p119)")
q(119, S5, "Renal cell carcinoma with pheochromocytoma is characteristic of:",
  ["Von Hippel-Lindau disease", "MEN 2A", "MEN 2B", "NF1"], 0,
  "Renal cell carcinoma: VHL disease. (Book p119)")
q(119, S5, "Pancreatic endocrine neoplasm with pheochromocytoma is seen in:",
  ["Von Hippel-Lindau disease", "MEN 2B", "NF1", "Familial paraganglioma type 4"], 0,
  "Pancreatic endocrine neoplasm: VHL disease. (Book p119)")
q(119, S5, "Familial paraganglioma type 1 is caused by mutation of:",
  ["SDHD", "SDHB", "SDHC", "RET"], 0,
  "Familial paraganglioma 1: SDHD - pheochromocytoma, paraganglioma. (Book p119)")
q(119, S5, "Familial paraganglioma type 3 is associated with mutation of:",
  ["SDHC", "SDHD", "SDHB", "NF1"], 0,
  "Familial paraganglioma 3: SDHC - paraganglioma. (Book p119)")
q(119, S5, "Familial paraganglioma type 4 is associated with mutation of:",
  ["SDHB", "SDHD", "SDHC", "RET"], 0,
  "Familial paraganglioma 4: SDHB - pheochromocytoma, paraganglioma. (Book p119)")
q(119, S5, "SDHB stands for:",
  ["Succinate dehydrogenase complex, subunit B", "Succinate dehydrogenase complex, subunit C",
   "Succinate dehydrogenase complex, subunit D", "Sodium dehydrogenase binding protein"], 0,
  "SDHB - succinate dehydrogenase complex, subunit B. (Book p119)")
q(119, S5, "SDHC stands for:",
  ["Succinate dehydrogenase complex, subunit C", "Succinate dehydrogenase complex, subunit B",
   "Succinate dehydrogenase complex, subunit D", "Sodium-dependent catecholamine channel"], 0,
  "SDHC - succinate dehydrogenase complex, subunit C. (Book p119)")
q(119, S5, "SDHD stands for:",
  ["Succinate dehydrogenase complex, subunit D", "Succinate dehydrogenase complex, subunit B",
   "Succinate dehydrogenase complex, subunit C", "Somatostatin-dependent hormone"], 0,
  "SDHD - succinate dehydrogenase complex, subunit D. (Book p119)")

# ---------------- p119-120 · HISTOPATHOLOGY & IHC ----------------
S6 = "Histopathology & IHC of Pheochromocytoma"
q(119, S6, "The gross appearance of pheochromocytoma is:",
  ["Tan brown colour", "Pearly white", "Jet black", "Grey-white and firm"], 0,
  "Gross appearance: tan brown colour. (Book p119)")
q(119, S6, "The tan brown colour of pheochromocytoma on cutting is due to the:",
  ["Chromaffin reaction", "Melanin pigment", "Hemosiderin deposition", "Bile staining"], 0,
  "Tan brown colour is due to the chromaffin reaction. (Book p119)")
q(119, S6, "Gross features of pheochromocytoma include necrosis and:",
  ["Hemorrhage", "Calcification", "Cavitation", "Cartilage formation"], 0,
  "Gross: necrosis and hemorrhage. (Book p119)")
q(120, S6, "The classic microscopic pattern of pheochromocytoma is:",
  ["Zellballen pattern", "Indian filing", "Glandular acinar pattern", "Storiform pattern"], 0,
  "Microscopy: Zellballen pattern. (Book p120)")
q(120, S6, "'Salt and pepper' nuclei on microscopy are characteristic of:",
  ["Pheochromocytoma", "Follicular carcinoma thyroid", "Adrenocortical carcinoma", "Carcinoid tumor"], 0,
  "Microscopy: Zellballen pattern with salt & pepper nuclei. (Book p120)")
q(120, S6, "On IHC, pheochromocytoma is positive for:",
  ["Synaptophysin", "Thyroglobulin", "Calcitonin", "PSA"], 0,
  "IHC positive for synaptophysin, neuron specific enolase and chromogranin. (Book p120)")
q(120, S6, "Neuron specific enolase positivity on IHC is seen in:",
  ["Pheochromocytoma", "Adrenocortical carcinoma", "Renal cell carcinoma", "Seminoma"], 0,
  "IHC: neuron specific enolase positive. (Book p120)")
q(120, S6, "Chromogranin positivity on IHC is seen in:",
  ["Pheochromocytoma", "Adrenocortical carcinoma", "Wilms' tumor", "Hepatoblastoma"], 0,
  "IHC: chromogranin positive. (Book p120)")

# ---------------- p120 · MALIGNANT PHEOCHROMOCYTOMA & SECRETORY PROFILE ----------------
S7 = "Malignant Pheochromocytoma & Secretory Profile"
q(120, S7, "The confirmatory sign of malignant pheochromocytoma is:",
  ["Metastases", "Capsular invasion alone", "Pleomorphism alone", "Necrosis alone"], 0,
  "Malignant pheochromocytoma: metastases is the confirmatory sign. (Book p120)")
q(120, S7, "The PASS score used for malignant pheochromocytoma includes the proliferation marker:",
  ["Ki-67", "CEA", "CA 19-9", "PSA"], 0,
  "PASS score: Ki-67 (proliferation marker), vascular invasion, capsular invasion. (Book p120)")
q(120, S7, "Vascular invasion and capsular invasion are components of the:",
  ["PASS score for malignant pheochromocytoma", "Gleason score", "Child-Pugh score", "Ranson's criteria"], 0,
  "PASS score includes vascular invasion and capsular invasion. (Book p120)")
q(120, S7, "An adrenal pheochromocytoma predominantly secretes:",
  ["Noradrenaline > adrenaline", "Adrenaline > noradrenaline", "Dopamine only", "Serotonin only"], 0,
  "Adrenal pheochromocytoma: noradrenaline > adrenaline. (Book p120)")
q(120, S7, "Paragangliomas characteristically secrete:",
  ["Noradrenaline", "Adrenaline", "Dopamine", "Serotonin"], 0,
  "Paraganglioma: noradrenaline. (Book p120)")
q(120, S7, "Dopamine secretion is characteristic of:",
  ["Malignant pheochromocytoma", "Benign adrenal adenoma", "Paraganglioma", "Neuroblastoma"], 0,
  "Malignant pheochromocytoma: dopamine. (Book p120)")

# ---------------- p120 · CLINICAL FEATURES ----------------
S8 = "Clinical Features of Pheochromocytoma"
q(120, S8, "The m/c symptom of pheochromocytoma is:",
  ["Headache", "Weight loss", "Sweating", "Palpitations"], 0,
  "Clinical features: headache is the m/c symptom. (Book p120)")
q(120, S8, "The m/c sign of pheochromocytoma is:",
  ["Hypertension", "Tachycardia", "Pallor", "Fever"], 0,
  "Headache is due to hypertension, which is the m/c sign. (Book p120)")
q(120, S8, "The classical triad of pheochromocytoma (headache, palpitations and the third symptom) is completed by:",
  ["Sweating", "Weight gain", "Polyuria", "Constipation"], 0,
  "Features: headache, sweating, palpitations, weight loss. (Book p120)")
q(120, S8, "Palpitations in pheochromocytoma are due to:",
  ["Catecholamine excess", "Anaemia", "Thyrotoxicosis", "Hypoglycaemia"], 0,
  "Palpitations are a feature of catecholamine excess in pheochromocytoma. (Book p120)")
q(120, S8, "Weight loss is a recognised feature of:",
  ["Pheochromocytoma", "Adrenocortical adenoma", "Myelolipoma", "Adrenal cyst"], 0,
  "Features: headache, sweating, palpitations and weight loss. (Book p120)")

# ---------------- p120 · INVESTIGATIONS ----------------
S9 = "Investigations of Pheochromocytoma"
q(120, S9, "The screening test for pheochromocytoma is:",
  ["24 hour urinary VMA", "Plasma free metanephrines", "MRI abdomen", "Gallium dotatate scan"], 0,
  "Screening test: 24 hour urinary VMA (vanillyl mandelic acid). (Book p120)")
q(120, S9, "VMA stands for:",
  ["Vanillyl mandelic acid", "Vanillyl monoamine", "Vasoactive monoamine", "Volatile mandelic acid"], 0,
  "VMA = vanillyl mandelic acid - 24 hour urinary screening test. (Book p120)")
q(120, S9, "The most sensitive test for pheochromocytoma is:",
  ["Plasma free metanephrines", "24 hour urinary VMA", "Urinary 5-HIAA", "Serum chromogranin A"], 0,
  "Most sensitive: plasma free metanephrines. (Book p120)")
q(120, S9, "The investigation of choice for localising a pheochromocytoma is:",
  ["MRI", "CT scan", "X-ray abdomen", "Ultrasound"], 0,
  "IOC for pheochromocytoma: MRI. (Book p120)")
q(120, S9, "The 'light bulb sign' or 'Swiss cheese appearance' of pheochromocytoma is seen on:",
  ["MRI", "CT scan", "Plain X-ray", "Bone scan"], 0,
  "MRI: light bulb sign / Swiss cheese appearance. (Book p120)")
q(120, S9, "Extra-adrenal pheochromocytoma and metastases are best localised by:",
  ["Gallium dotatate scan", "Plain CT alone", "Intravenous urography", "Bone scan"], 0,
  "Extra-adrenal pheochromocytoma / metastases: gallium dotatate scan. (Book p120)")
q(120, S9, "Pheochromocytoma commonly metastasises to the:",
  ["Bones and liver", "Brain and spleen", "Kidneys and pancreas", "Skin and thyroid"], 0,
  "Pheochromocytoma commonly metastasises to bones and liver. (Book p120)")

# ---------------- p121 · MANAGEMENT OF PHEOCHROMOCYTOMA ----------------
S10 = "Management of Pheochromocytoma"
q(121, S10, "Medical management of pheochromocytoma is started with:",
  ["Alpha blocker", "Beta blocker", "Calcium channel blocker", "ACE inhibitor"], 0,
  "Medical management: alpha blockade first. (Book p121)")
q(121, S10, "A beta blocker is added in the medical management of pheochromocytoma if there is:",
  ["Tachycardia", "Bradycardia", "Hypotension", "Bronchospasm"], 0,
  "If tachycardia is present, add a beta blocker. (Book p121)")
q(121, S10, "If a beta blocker is given before an alpha blocker in pheochromocytoma, it causes:",
  ["Unopposed alpha action leading to vasospasm and hypertensive crisis",
   "Unopposed beta action causing severe bradycardia",
   "Complete catecholamine depletion", "Acute Addisonian crisis"], 0,
  "Beta blocker before alpha blocker: unopposed alpha action -> vasospasm, hypertensive crisis. (Book p121)")
q(121, S10, "Definitive management of pheochromocytoma is:",
  ["Laparoscopic or open adrenalectomy", "Lifelong alpha blockade only", "Radiotherapy", "Chemotherapy"], 0,
  "Surgery: laparoscopic or open adrenalectomy. (Book p121)")
q(121, S10, "Sudden hypotension during adrenalectomy for pheochromocytoma occurs when:",
  ["The adrenal vein is clipped", "The peritoneum is opened", "The tumour capsule is incised",
   "The patient is intubated"], 0,
  "Adrenal vein clipped: sudden hypotension. (Book p121)")
q(121, S10, "Hypotension after clipping of the adrenal vein is prevented by:",
  ["Administering large amounts of IV fluids +/- vasopressors",
   "Giving a beta blocker bolus", "Clamping the inferior vena cava", "Induced hypothermia"], 0,
  "Prevention: administering large amount of IV fluids +/- vasopressors. (Book p121)")

# ---------------- p121 · PHEOCHROMOCYTOMA IN PREGNANCY ----------------
S11 = "Pheochromocytoma in Pregnancy"
q(121, S11, "Pheochromocytoma presenting in the 1st or 2nd trimester of pregnancy is managed by:",
  ["Alpha blocker followed by surgery", "Immediate delivery followed by surgery",
   "Beta blocker alone till term", "Surgery in the postpartum period only"], 0,
  "1st and 2nd trimester: alpha blocker then surgery. (Book p121)")
q(121, S11, "Pheochromocytoma presenting in the 3rd trimester of pregnancy is managed by:",
  ["Alpha blocker, early delivery, then surgery", "Surgery alone, ignoring the pregnancy",
   "Alpha blocker alone till term, no surgery", "Termination of pregnancy followed by radiotherapy"], 0,
  "3rd trimester: alpha blocker -> early delivery -> surgery. (Book p121)")

# ---------------- p121 · NEUROBLASTOMA: FEATURES & PRESENTATION ----------------
S12 = "Neuroblastoma: Features & Presentation"
q(121, S12, "The m/c abdominal malignancy in a child is:",
  ["Neuroblastoma", "Wilms' tumor", "Hepatoblastoma", "Rhabdomyosarcoma"], 0,
  "M/c abdominal malignancy in a child: neuroblastoma (more than Wilms' tumor). (Book p121)")
q(121, S12, "Neuroblastoma arises from:",
  ["Adrenal medulla > sympathetic chain", "Adrenal cortex", "Renal pelvis", "Liver"], 0,
  "Arises from: adrenal medulla > sympathetic chain. (Book p121)")
q(121, S12, "N-myc amplification is associated with:",
  ["Neuroblastoma", "Wilms' tumor", "Hepatoblastoma", "Pheochromocytoma"], 0,
  "Features: N-myc amplification present. (Book p121)")
q(121, S12, "Neuroblastoma may occur as:",
  ["Sporadic or familial", "Only sporadic", "Only familial", "Only radiation-induced"], 0,
  "Neuroblastoma: sporadic or familial. (Book p121)")
q(121, S12, "The m/c age of presentation of neuroblastoma is:",
  ["5 years", "1 year", "15 years", "25 years"], 0,
  "Presentation: m/c age is 5 years. (Book p121)")
q(121, S12, "The m/c presenting feature of neuroblastoma is:",
  ["Abdominal mass crossing the midline", "Hematuria", "Jaundice", "Bone pain"], 0,
  "M/c symptom: abdominal mass that crosses the midline. (Book p121)")
q(121, S12, "The proportion of neuroblastoma patients presenting with metastases at diagnosis is:",
  ["50-70%", "Less than 5%", "10-20%", "Almost 100%"], 0,
  "50-70% present with metastasis at diagnosis. (Book p121)")
q(121, S12, "'Raccoon eyes' in neuroblastoma refers to:",
  ["Orbital metastasis with swollen eyes and bruising", "Periorbital oedema due to nephrotic syndrome",
   "Allergic shiners", "Basal skull fracture"], 0,
  "Raccoon eyes: swollen eyes with bruising due to orbital metastases. (Book p121)")
q(121, S12, "'Blueberry muffin' lesions are atypical metastases seen in:",
  ["Neuroblastoma", "Wilms' tumor", "Retinoblastoma", "Hepatoblastoma"], 0,
  "Blueberry muffin lesions: atypical metastases of neuroblastoma. (Book p121)")

# ---------------- p122 · NEUROBLASTOMA: INVESTIGATIONS & PROGNOSIS ----------------
S13 = "Neuroblastoma: Investigations & Prognosis"
q(122, S13, "The investigation of choice for neuroblastoma is:",
  ["MRI", "CT scan", "Plain X-ray", "Ultrasound"], 0,
  "Investigations: MRI (> CT) is the IOC. (Book p122)")
q(122, S13, "MIBG scan in neuroblastoma is used to detect:",
  ["Metastases", "Calcification", "Cystic degeneration", "Vascular invasion"], 0,
  "Mets: MIBG scan. (Book p122)")
q(122, S13, "Wilms' tumor is differentiated from neuroblastoma because it arises from the:",
  ["Kidney", "Adrenal medulla", "Sympathetic chain", "Liver"], 0,
  "Rule out Wilms' tumor: origin is the kidney. (Book p122)")
q(122, S13, "Unlike neuroblastoma, the abdominal mass of Wilms' tumor:",
  ["Does not cross the midline", "Always crosses the midline", "Is always calcified", "Is always cystic"], 0,
  "Wilms' tumor: abdominal mass does not cross the midline. (Book p122)")
q(122, S13, "Histopathology of neuroblastoma shows:",
  ["Small round blue cells", "Spindle cells", "Clear cells", "Signet ring cells"], 0,
  "Histopathology: small round blue cells. (Book p122)")
q(122, S13, "Small round blue cell tumors include all of the following EXCEPT:",
  ["Squamous cell carcinoma", "Neuroblastoma", "Medulloblastoma", "Ewing's sarcoma / PNET"], 0,
  "Small round blue cell tumors: neuroblastoma, retinoblastoma, hepatoblastoma, medulloblastoma, nephroblastoma, rhabdomyosarcoma, Ewing's sarcoma/PNET, lymphoma. (Book p122)")
q(122, S13, "Medulloblastoma belongs to the group of:",
  ["Small round blue cell tumors", "Germ cell tumors", "Neuroendocrine tumors", "Mesenchymal tumors"], 0,
  "Small round blue cell tumors include medulloblastoma. (Book p122)")
q(122, S13, "Favourable prognostic stage in neuroblastoma is:",
  ["Stage 4S", "Stage 3", "Stage 4", "Stage 3 and 4"], 0,
  "Favourable stage: 1, 2A, 2B, 4S; unfavourable: 3 and 4. (Book p122)")
q(122, S13, "The favourable age group in neuroblastoma prognosis is:",
  ["< 18 months", "> 18 months", "> 5 years", "> 10 years"], 0,
  "Age: < 18 months is favourable, > 18 months unfavourable. (Book p122)")
q(122, S13, "N-myc amplification in neuroblastoma indicates:",
  ["Unfavourable prognosis", "Favourable prognosis", "Spontaneous regression", "Benign behaviour"], 0,
  "N-myc amplified = non-favourable prognosis. (Book p122)")

# ---------------- p122 · NEUROBLASTOMA: MANAGEMENT ----------------
S14 = "Neuroblastoma: Management"
q(122, S14, "Chemotherapy for neuroblastoma uses:",
  ["Etoposide + cisplatin", "Vincristine + methotrexate", "5-FU + leucovorin", "Bleomycin + dacarbazine"], 0,
  "Chemotherapy: etoposide + cisplatin, plus surgery. (Book p122)")
q(122, S14, "Neuroblastoma with metastases is managed by:",
  ["Aggressive management (good survival chance)", "Only palliative care", "No treatment",
   "Radiotherapy alone"], 0,
  "Mets: aggressive management - good survival chance. (Book p122)")

# ---------------- p122-123 · CARCINOID TUMORS: ORIGIN & SITES ----------------
S15 = "Carcinoid Tumors: Origin & Sites"
q(122, S15, "Carcinoid tumors arise from:",
  ["Neuroendocrine cells", "Squamous epithelium", "Smooth muscle", "Adipose tissue"], 0,
  "Carcinoid tumors arise from the neuroendocrine cells. (Book p122)")
q(122, S15, "The new term for carcinoid tumors is:",
  ["Neuroendocrine tumors", "Adenocarcinoid tumors", "Argentaffinomas", "Chromaffin tumors"], 0,
  "New term: neuroendocrine tumors. (Book p122)")
q(123, S15, "The m/c site of carcinoid tumors is the:",
  ["Appendix", "Rectum", "Lung", "Stomach"], 0,
  "Site distribution: appendix is the m/c site (40%). (Book p123)")
q(123, S15, "After the appendix, the next m/c site of carcinoid tumors is the:",
  ["Small bowel", "Colon", "Duodenum", "Lung"], 0,
  "Distribution: appendix (m/c, 40%) followed by small bowel (25%). (Book p123)")
q(123, S15, "Foregut carcinoids include those arising in the:",
  ["Lungs and stomach", "Appendix and caecum", "Colon and rectum", "Rectum and anal canal"], 0,
  "Foregut: lungs, stomach; midgut: small intestine, appendix; hindgut: colon, rectum. (Book p123)")
q(123, S15, "Hindgut carcinoids arise from the:",
  ["Colon and rectum", "Stomach and duodenum", "Lungs", "Appendix"], 0,
  "Hindgut: colon and rectum. (Book p123)")
q(123, S15, "The m/c site of metastases in carcinoid tumors is the:",
  ["Bones", "Brain", "Spleen", "Kidneys"], 0,
  "Carcinoid tumors: m/c metastasis to bones. (Book p123)")
q(123, S15, "Serotonin produced by carcinoid tumors is metabolised in the:",
  ["Liver", "Kidney", "Lung", "Spleen"], 0,
  "Serotonin is metabolised in the liver. (Book p123)")
q(123, S15, "Chromogranin A positivity is seen in:",
  ["Carcinoid tumors", "Adrenocortical carcinoma", "Squamous cell carcinoma", "Wilms' tumor"], 0,
  "Others: chromogranin A positive. (Book p123)")

# ---------------- p123 · CARCINOID SYNDROME: FEATURES & INVESTIGATIONS ----------------
S16 = "Carcinoid Syndrome: Features & Investigations"
q(123, S16, "Carcinoid syndrome occurs in what proportion of patients with carcinoid tumors?",
  ["10%", "50%", "90%", "1%"], 0,
  "Carcinoid syndrome: 10% of cases, when liver metastases are present. (Book p123)")
q(123, S16, "Carcinoid syndrome develops when the tumor has:",
  ["Liver metastases", "Bone metastases", "Nodal metastases only", "Peritoneal seedlings only"], 0,
  "Carcinoid syndrome occurs if liver metastases are present (hormones escape hepatic metabolism). (Book p123)")
q(123, S16, "The m/c symptom of carcinoid syndrome is:",
  ["Cutaneous flushing", "Diarrhea", "Bronchospasm", "Palpitations"], 0,
  "Clinical features: cutaneous flushing is the m/c symptom. (Book p123)")
q(123, S16, "The m/c symptom of abdominal carcinoids is:",
  ["Pain", "Flushing", "Jaundice", "Hematuria"], 0,
  "Pain is the m/c symptom of abdominal carcinoids. (Book p123)")
q(123, S16, "Diarrhea in carcinoid syndrome is due to:",
  ["Serotonin", "Gastrin", "Vasoactive intestinal peptide only", "Histamine from the stomach"], 0,
  "Diarrhea is a feature of carcinoid syndrome (serotonin mediated). (Book p123)")
q(123, S16, "Bronchospasm and weight loss are recognised features of:",
  ["Carcinoid syndrome", "Cushing's syndrome", "Conn's syndrome", "Addison's disease"], 0,
  "Features: flushing, pain, diarrhea, weight loss, bronchospasm, right sided valve lesions. (Book p123)")
q(123, S16, "Right sided valvular lesions in carcinoid syndrome most often involve the:",
  ["Tricuspid valve", "Mitral valve", "Aortic valve", "Pulmonary vein"], 0,
  "Right sided valvular lesions: tricuspid valve is the m/c. (Book p123)")
q(123, S16, "The urinary investigation for carcinoid syndrome is:",
  ["5-HIAA (hydroxy indole acetic acid)", "VMA", "Catecholamines", "Metanephrines"], 0,
  "Urine: 5-HIAA (hydroxy indole acetic acid). (Book p123)")
q(123, S16, "Urinary 5-HIAA is the metabolite of:",
  ["Serotonin", "Adrenaline", "Dopamine", "Histamine"], 0,
  "5-HIAA is the metabolite of serotonin. (Book p123)")
q(123, S16, "The blood investigation used for carcinoid tumors is:",
  ["Chromogranin A", "Serum cortisol", "Plasma metanephrines", "Serum calcitonin"], 0,
  "Blood: chromogranin A. (Book p123)")

# ---------------- p124 · CARCINOID: LOCALISATION & SURGICAL MANAGEMENT ----------------
S17 = "Carcinoid: Localisation & Surgical Management"
q(124, S17, "CT scan in carcinoid tumors is done to:",
  ["Localise the lesion", "Assess valvular lesions", "Measure serotonin levels", "Detect bone marrow uptake"], 0,
  "CT scan: to localise the lesion. (Book p124)")
q(124, S17, "Serotonin / somatostatin receptor scintigraphy in carcinoid is used for:",
  ["Localisation of the tumor and its metastases", "Measuring urinary 5-HIAA",
   "Assessing cardiac valves", "Staging of liver function"], 0,
  "Serotonin/somatostatin receptor scintigraphy localises tumor and metastases. (Book p124)")
q(124, S17, "A Dotatate PET scan in carcinoid disease is used to:",
  ["Localise metastases", "Replace histopathology", "Measure Ki-67", "Assess valvular disease"], 0,
  "Dotatate PET scan localises metastases. (Book p124)")
q(124, S17, "A high Ki-67 in a neuroendocrine tumor indicates:",
  ["Malignancy / metastases", "Benign behavior", "Good prognosis", "Response to octreotide"], 0,
  "High Ki-67: malignancy / metastases. (Book p124)")
q(124, S17, "In localised carcinoid disease, the surgical approach is:",
  ["Radical resection", "Palliative resection", "No resection", "Biopsy only"], 0,
  "Localised disease: radical resection. (Book p124)")
q(124, S17, "The aim of surgery in localised carcinoid disease is:",
  ["R0 - microscopic freedom from disease", "R1 - leaving microscopic disease",
   "Debulking only for symptom relief", "Cytoreduction to < 50%"], 0,
  "Aim in localised disease: R0 (microscopic freedom from disease). (Book p124)")
q(124, S17, "In regional carcinoid disease, the resection includes:",
  ["Primary tumor and nodes along the mesentery", "Primary tumor alone",
   "Liver metastases only", "Only the mesenteric nodes"], 0,
  "Regional disease: resection of primary and nodes along the mesentery. (Book p124)")
q(124, S17, "In distant / metastatic carcinoid disease, the intent of surgery is:",
  ["Palliative", "Curative in all cases", "Diagnostic only", "Never indicated"], 0,
  "Distant disease: palliative intent. (Book p124)")
q(124, S17, "Palliative resection in carcinoid disease is done to avoid:",
  ["Obstructive complications", "Hypertensive crisis", "Bone pain", "Valvular regurgitation"], 0,
  "Palliative resection: to avoid obstructive complications (R1). (Book p124)")
q(124, S17, "No resection is advised in carcinoid disease when the tumor is:",
  ["Irresectable or the patient has comorbidities", "Localised", "Regional", "Less than 1 cm in the appendix"], 0,
  "No resection: due to irresectability or comorbidities. (Book p124)")
q(124, S17, "Octreotide is used in carcinoid disease:",
  ["For metastases - it controls symptoms", "To cure localised disease", "As a screening test",
   "To prevent bone metastases"], 0,
  "Octreotide: for metastases - controls symptoms. (Book p124)")

# ---------------- p124-125 · APPENDICEAL & GASTRIC CARCINOIDS ----------------
S18 = "Appendiceal & Gastric Carcinoids"
q(124, S18, "Appendiceal carcinoids are m/c located at the:",
  ["Tip of the appendix", "Base of the appendix", "Mid appendix only", "Mesenteric border"], 0,
  "Appendiceal carcinoid: m/c at the tip of the appendix. (Book p124)")
q(124, S18, "An appendiceal carcinoid can present as:",
  ["Appendicitis", "Carcinoid syndrome", "Intussusception", "Upper GI bleed"], 0,
  "Appendiceal carcinoid can present as appendicitis. (Book p124)")
q(124, S18, "Appendiceal carcinoid < 1 cm has an excellent prognosis and is treated by:",
  ["Appendicectomy", "Right hemicolectomy", "Chemotherapy", "Observation alone"], 0,
  "< 1 cm (excellent prognosis): appendicectomy. (Book p124)")
q(124, S18, "For appendiceal carcinoids of 1-2 cm, further management is based on:",
  ["Mitotic figures and Ki-67", "Patient's age only", "Serum chromogranin A only",
   "Size of the appendix"], 0,
  "1-2 cm: management based on mitotic figures and Ki-67. (Book p124)")
q(124, S18, "Right hemicolectomy for appendiceal carcinoid is indicated for all of the following EXCEPT:",
  ["Tumor at the tip measuring 0.5 cm", "Tumor >= 2 cm", "Tumor close to the base",
   "Infiltration of the mesoappendix"], 0,
  "Right hemicolectomy: tumor >= 2 cm, close to the base, or infiltrating the mesoappendix. (Book p124)")
q(124, S18, "Infiltration of the mesoappendix by an appendiceal carcinoid warrants:",
  ["Right hemicolectomy", "Simple appendicectomy", "Observation", "Radiotherapy"], 0,
  "Infiltration of the mesoappendix: right hemicolectomy. (Book p124)")
q(125, S18, "Type 1 gastric carcinoids are seen in:",
  ["Chronic atrophic gastritis with hypergastrinemia", "Gastrinoma in MEN 1",
   "Sporadic ECLomas unrelated to hypergastrinemia", "Small cell neuroendocrine carcinoma"], 0,
  "Type 1: ECLomas in chronic atrophic gastritis with hypergastrinemia - benign, non-functional, well differentiated. (Book p125)")
q(125, S18, "Type 2 gastric carcinoids are associated with:",
  ["Gastrinoma in MEN 1", "Chronic atrophic gastritis", "Pernicious anaemia",
   "Small cell carcinoma"], 0,
  "Type 2: ECLomas with hypergastrinemia as a result of gastrinoma in MEN 1. (Book p125)")
q(125, S18, "Type 3 gastric carcinoids are:",
  ["Sporadic ECLomas not related to hypergastrinemia", "Associated with MEN 1",
   "Associated with atrophic gastritis", "Always benign"], 0,
  "Type 3: sporadic ECLomas, not related to hypergastrinemia - low grade malignant. (Book p125)")
q(125, S18, "Type 4 gastric carcinoid is:",
  ["High grade malignant neuroendocrine carcinoma with poor prognosis",
   "A benign non-functional tumor", "Always associated with MEN 1",
   "Associated with chronic atrophic gastritis"], 0,
  "Type 4: intermediate or small cell type, high grade malignant (neuroendocrine carcinoma), causative factor unknown, poor prognosis. (Book p125)")
q(125, S18, "ECL in the gastric carcinoid classification stands for:",
  ["Enterochromaffin-like", "Enterochromaffin cell lymphoma", "Endocrine cell lesion",
   "Eosinophilic crypt lesion"], 0,
  "ECL: enterochromaffin-like; MEN: multiple endocrine neoplasia. (Book p125)")

# ---------------- p125 · ADRENOCORTICAL CARCINOMA ----------------
S19 = "Adrenocortical Carcinoma"
q(125, S19, "Adrenocortical carcinoma is seen in children and in the:",
  ["4th to 5th decade", "1st decade only", "7th decade", "9th decade"], 0,
  "Adrenocortical carcinoma: children and 4th to 5th decade. (Book p125)")
q(125, S19, "Adrenocortical carcinomas are:",
  ["Non-functional >> functional (aggressive)", "Functional >> non-functional",
   "Always functional", "Always non-functional and benign"], 0,
  "Features: non-functional >> functional (aggressive). (Book p125)")
q(125, S19, "The m/c functional presentation of adrenocortical carcinoma is:",
  ["Cushing's syndrome", "Conn's syndrome", "Pheochromocytoma", "Addison's disease"], 0,
  "Cushing's syndrome is the m/c functional presentation. (Book p125)")
q(125, S19, "The investigation of choice for adrenocortical carcinoma is:",
  ["MRI > CECT", "CECT > MRI", "Plain X-ray", "Ultrasound only"], 0,
  "Investigations: IOC is MRI (> CECT). (Book p125)")
q(125, S19, "The McFarlane classification of adrenocortical carcinoma is based on:",
  ["Size", "Depth of invasion", "Nodal status", "Hormone secretion"], 0,
  "McFarlane classification: based on size. (Book p125)")

# ---------------- units ----------------
def sec_ids(*labels):
    return [x["id"] for x in Q if x["sec"] in labels]
def first_page(label):
    for x in Q:
        if x["sec"] == label:
            return x["page"]
    return 0

UNIT_DEFS = [
    (S1, "Adrenal incidentaloma = an adrenal lesion found while imaging for something else; non-functional tumours are the commonest cause, followed by metastases (breast, lung, kidney) and functional lesions (Cushing's, carcinoma). The NCCT density is the great splitter: benign lesions are lipid-rich and read <= 10 HU."),
    (S2, "Work every incidentaloma twice: is it functional (serum cortisol, urinary cortisol, dexamethasone suppression; plasma free metanephrines for pheochromocytoma; serum DHEA for cortical carcinoma) and is it malignant (>= 4 cm, > 10 HU, CECT washout, FDG PET uptake). FNAC only after pheochromocytoma is excluded - needling one can be fatal."),
    (S3, "Unilateral adrenal mass: suspicion of malignancy with local invasion goes straight to open adrenalectomy; <= 6 cm without invasion is laparoscopic; odd cases get an individualised plan. Non-functional and < 4 cm/benign: no surgery, just CT or MRI every 3-6 months; >= 4 cm, malignant features or significant growth - adrenalectomy."),
    (S4, "Pheochromocytoma is an adrenal-medulla tumour (M = F) and the classic 'rule of 10' applies: 10% familial, bilateral, malignant, extra-adrenal and in children. Paraganglioma is the extra-adrenal counterpart - sympathetic chain (organ of Zuckerkandl, the commonest site) or parasympathetic chain (carotid body)."),
    (S5, "Know the familial syndromes by their gene and their signature partner lesions: MEN 2A (RET) triad = MTC + pheochromocytoma + parathyroid hyperplasia; MEN 2B (RET) = marfanoid habitus and mucocutaneous ganglioneuromas; NF1 (neurofibromin) = neurofibromas, cafe-au-lait spots, optic glioma; VHL = RCC, hemangioblastoma, pancreatic endocrine tumour; SDHD/SDHB/SDHC = familial paragangliomas 1/4/3."),
    (S6, "Cut surface is tan-brown because of the chromaffin reaction, with necrosis and haemorrhage; microscopy shows the Zellballen (cell-ball) nests with salt-and-pepper chromatin. IHC is neuroendocrine: synaptophysin, neuron-specific enolase and chromogranin."),
    (S7, "Malignancy is proven only by metastases - histology alone cannot call it. The PASS score weighs Ki-67 proliferation, vascular invasion and capsular invasion. Secretory fingerprint: adrenal tumours noradrenaline > adrenaline, paragangliomas noradrenaline, malignant lesions dopamine."),
    (S8, "Episodic headache is the commonest symptom and hypertension the commonest sign; add sweating, palpitations and weight loss. The classic triad is episodic headache, sweating and palpitations in a hypertensive young patient."),
    (S9, "Screen with 24-hour urinary VMA (vanillyl mandelic acid); plasma free metanephrines is the most sensitive test; MRI is the investigation of choice and gives the light-bulb/Swiss-cheese appearance; gallium dotatate scan for extra-adrenal disease and metastases (bones and liver are the usual targets)."),
    (S10, "Never block beta first: alpha blockade (phenoxybenzamine) comes first, then a beta blocker only if tachycardia - otherwise unopposed alpha action causes vasospasm and hypertensive crisis. Definitive treatment is laparoscopic or open adrenalectomy; clipping the adrenal vein causes sudden hypotension, prevented by generous IV fluids +/- vasopressors."),
    (S11, "In pregnancy, alpha blockade then surgery in the 1st or 2nd trimester; in the 3rd trimester, alpha blockade, early delivery, then surgery."),
    (S12, "Neuroblastoma is the commonest abdominal malignancy of childhood (more than Wilms'), arising from the adrenal medulla more often than the sympathetic chain, with N-myc amplification, sporadic or familial. Around 5 years of age it presents as an abdominal mass crossing the midline; 50-70% already have metastases, with the tell-tale raccoon eyes and blueberry muffin skin nodules."),
    (S13, "MRI beats CT as the IOC and MIBG scintigraphy picks up metastases; exclude Wilms' tumour (renal origin, does not cross the midline, may calcify). Biopsy shows small round blue cells - the family that also includes retinoblastoma, hepatoblastoma, medulloblastoma, nephroblastoma, rhabdomyosarcoma, Ewing's/PNET and lymphoma. Good prognosis: stage 1, 2A, 2B or 4S, age < 18 months, N-myc not amplified."),
    (S14, "Treatment is etoposide plus cisplatin chemotherapy together with surgery; even metastatic disease is treated aggressively because survival is genuinely good."),
    (S15, "Carcinoid tumours - now called neuroendocrine tumours - arise from neuroendocrine cells, most often in the appendix, then small bowel, rectum and lung; foregut (lung, stomach), midgut (small intestine, appendix) and hindgut (colon, rectum) behave differently, bone is the commonest metastatic site, and serotonin they make is normally destroyed by the liver."),
    (S16, "Carcinoid syndrome needs liver metastases - only then do hormones bypass hepatic metabolism; it affects about 10%. Flushing is the commonest symptom (pain for abdominal primaries), with diarrhoea, weight loss, bronchospasm and right-sided tricuspid valve disease. Test urine for 5-HIAA (the serotonin metabolite) and blood for chromogranin A."),
    (S17, "Localise with CT, somatostatin-receptor scintigraphy or Dotatate PET; high Ki-67 means malignancy/metastases. Localised disease gets radical R0 resection, regional disease resection of primary plus mesenteric nodes, distant disease only palliative resection to prevent obstruction; irresectable disease or comorbid patients are palliated with octreotide, which controls symptoms."),
    (S18, "Appendix: usually the tip, may mimic appendicitis; < 1 cm = appendicectomy (excellent prognosis), 1-2 cm is decided by mitotic figures and Ki-67, and right hemicolectomy for >= 2 cm, base involvement or mesoappendix infiltration. Gastric carcinoids: type 1 atrophic gastritis/hypergastrinaemia, type 2 gastrinoma in MEN 1, type 3 sporadic ECLoma, type 4 high-grade small-cell type with poor prognosis."),
    (S19, "Adrenocortical carcinoma hits children and the 4th-5th decade, is usually non-functional and therefore aggressive, and when functional it presents as Cushing's. MRI beats CECT as the IOC, and the McFarlane classification stages it by size."),
]

UNITS = []
for i, (title, guide) in enumerate(UNIT_DEFS, 1):
    UNITS.append({"id": f"SURG-U18-{i}", "ch": 18, "n": i, "title": title,
                  "sec": f"{title} · p{first_page(title)}",
                  "qs": sec_ids(title), "guide": guide})

covered = [i for u in UNITS for i in u["qs"]]
assert covered == [x["id"] for x in Q], "units must cover questions in order"

data = {"questions": Q, "units": UNITS}
with open("data/ch18.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
print(f"ch18: {len(Q)} questions, {len(UNITS)} units")
