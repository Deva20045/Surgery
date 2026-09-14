#!/usr/bin/env python3
"""Build data/ch35.json — ch35 Liver: Part 2 (Marrow Surgery Ed 8, book p253-259)."""
import json

Q = []


def q(page, sec, text, opts, ans, exp):
    Q.append({
        "id": f"SURG-C35-{len(Q)+1:03d}",
        "sec": sec,
        "page": page,
        "q": text,
        "opts": opts,
        "ans": ans,
        "exp": exp,
    })


# ------------------------------------------------------------------ p253
S1 = "LI-RADS and the Common Liver Tumours"
q(253, S1, "The investigation of choice for liver tumours, on which LI-RADS is based, is:",
  ["Triple phase CT", "Ultrasound abdomen", "Plain CT abdomen", "PET-CT"], 0,
  "The investigation of choice is triple phase CT and LI-RADS scoring is based on it. (Book p253)")
q(253, S1, "LI-RADS scoring is applied to:",
  ["All liver tumours", "Only HCC", "Only metastases", "Only benign lesions"], 0,
  "LI-RADS scoring is done for all liver tumours. (Book p253)")
q(253, S1, "An LR-1 lesion is:",
  ["100% benign", "Probably benign", "Probably HCC", "100% definite HCC"], 0,
  "LR-1: 100% benign. (Book p253)")
q(253, S1, "An LR-2 lesion is:",
  ["Probably benign and followed up", "100% benign",
   "Intermediate probability of HCC", "Definitely HCC"], 0,
  "LR-2: probably benign (follow up done). (Book p253)")
q(253, S1, "An LR-3 lesion indicates:",
  ["Intermediate probability for HCC — follow up or biopsy",
   "A definitely benign lesion",
   "Probably HCC needing resection",
   "100% definite HCC"], 0,
  "LR-3: intermediate probability for HCC (follow up/biopsy). (Book p253)")
q(253, S1, "LR-4 means:",
  ["Probably HCC", "Probably benign", "100% definite HCC", "100% benign"], 0,
  "LR-4: probably HCC. (Book p253)")
q(253, S1, "LR-5 means:",
  ["100% definite HCC", "Probably HCC", "Intermediate probability", "100% benign"], 0,
  "LR-5: 100% definite HCC. (Book p253)")
q(253, S1, "The most common benign tumour of the liver is:",
  ["Haemangioma", "Focal nodular hyperplasia", "Hepatic adenoma", "Simple cyst"], 0,
  "One liners: m/c benign tumor — haemangioma. (Book p253)")
q(253, S1, "The second most common benign tumour of the liver is:",
  ["Focal nodular hyperplasia (FNH)", "Hepatic adenoma",
   "Haemangioma", "Nodular regenerative hyperplasia"], 0,
  "The one-liners list FNH (focal nodular hyperplasia) as the second m/c benign tumour. (Book p253)")
q(253, S1, "The most common malignant tumour of the liver is:",
  ["Metastasis / secondaries to the liver", "Hepatocellular carcinoma",
   "Cholangiocarcinoma", "Hepatoblastoma"], 0,
  "m/c malignant tumor: metastasis / secondaries to liver (HCC is the m/c PRIMARY malignant tumour). (Book p253)")
q(253, S1, "The most common primary malignant tumour of the liver is:",
  ["Hepatocellular carcinoma", "Metastasis", "Cholangiocarcinoma", "Angiosarcoma"], 0,
  "m/c primary malignant tumor: hepatocellular carcinoma (HCC). (Book p253)")

S2 = "Liver Haemangioma"
q(253, S2, "A liver haemangioma is:",
  ["A collection of blood vessels", "A proliferation of hepatocytes",
   "A bile duct hamartoma", "A nest of Kupffer cells"], 0,
  "Liver haemangiomas are a collection of blood vessels. (Book p253)")
q(253, S2, "Liver haemangiomas are more common in:",
  ["Females", "Males", "Both equally", "Children only"], 0,
  "Clinical features: female > male. (Book p253)")
q(253, S2, "Most liver haemangiomas are:",
  ["Asymptomatic and diagnosed incidentally", "Present with rupture",
   "Present with jaundice", "Present with fever"], 0,
  "Commonly asymptomatic → incidental diagnosis. (Book p253)")
q(253, S2, "Kasabach-Merritt syndrome (consumption coagulopathy) is a complication of:",
  ["Very large haemangiomas", "Small peripheral haemangiomas",
   "Focal nodular hyperplasia", "Hepatic adenoma"], 0,
  "In very large haemangiomas: Kasabach-Merritt syndrome — consumption coagulopathy. (Book p253)")
q(253, S2, "Large haemangiomas may present with:",
  ["Bleeding and pain", "Jaundice and ascites", "Portal hypertension", "Hypoglycaemia"], 0,
  "Large haemangiomas → bleeding + pain. (Book p253)")
q(253, S2, "On a non-contrast triple phase CT a haemangioma is:",
  ["Hypodense", "Hyperdense", "Isointense", "Calcified"], 0,
  "Non-contrast phase: hypodense. (Book p253)")
q(253, S2, "The characteristic arterial phase appearance of a hepatic haemangioma is:",
  ["Peripheral nodular enhancement", "Central stellate scar",
   "Early washout", "Uniform hyperdensity"], 0,
  "Arterial phase: peripheral nodular enhancement. (Book p253)")
q(254, S2, "An asymptomatic hepatic haemangioma is managed by:",
  ["Conservative management", "Angioembolisation", "Resection", "Chemotherapy"], 0,
  "Asymptomatic: conservative management. (Book p254)")
q(254, S2, "A large symptomatic haemangioma is treated by:",
  ["Angioembolisation", "Observation", "Radiotherapy", "Liver transplantation"], 0,
  "Large + symptomatic: angioembolisation. (Book p254)")

S3 = "Focal Nodular Hyperplasia"
q(254, S3, "FNH is more common in:",
  ["Females", "Males", "Both equally", "Only in children"], 0,
  "FNH: female > male. (Book p254)")
q(254, S3, "FNH is usually:",
  ["Asymptomatic and an incidental diagnosis", "Present with rupture",
   "Present with jaundice", "Present with hypoglycaemia"], 0,
  "FNH clinical features: female > male, asymptomatic, incidental diagnosis. (Book p254)")
q(254, S3, "The imaging hallmark of FNH on triple phase CT is:",
  ["A central stellate scar", "Peripheral nodular enhancement",
   "A water-lily sign", "A double line sign"], 0,
  "Central stellate scar: a dilated arteriole with branches. (Book p254)")
q(254, S3, "The central stellate scar of FNH is also a feature of which renal tumour?",
  ["Oncocytoma", "Clear cell carcinoma", "Angiomyolipoma", "Wilms tumour"], 0,
  "The page notes the central stellate scar is also seen in oncocytoma of the kidney. (Book p254)")
q(254, S3, "On histopathology FNH contains hepatocytes and:",
  ["Atypical bile duct structures with Kupffer cells",
   "Sheets of hepatocytes with no bile ducts",
   "Mucin producing glands",
   "Caseating granulomas"], 0,
  "HPE of FNH: hepatocytes, atypical bile duct structures and Kupffer cells. (Book p254)")
q(254, S3, "Because FNH contains Kupffer cells and is usually unencapsulated it:",
  ["Shows a 'hot-spot' on a sulphur colloid scan",
   "Shows no uptake on a sulphur colloid scan",
   "Is always hot on a PET scan",
   "Is calcified on plain X-ray"], 0,
  "Kupffer cells (and the usually unencapsulated nature) → 'hot-spot' on a sulphur colloid scan. (Book p254)")
q(254, S3, "Alpha-fetoprotein in FNH is:",
  ["Normal", "Greatly raised", "Mildly raised", "Undetectable only in children"], 0,
  "α-fetoprotein (AFP) is normal in FNH — and this differentiates FNH from HCC. (Book p254)")
q(254, S3, "A 32-year-old woman on no medication has an asymptomatic 4 cm liver lesion with a central stellate scar and a normal AFP. The correct management is:",
  ["Observation", "Resection because of the cancer risk",
   "Angioembolisation", "Liver transplantation"], 0,
  "This is FNH: observation is the recommended management. (Book p254)")

S4 = "Hepatic Adenoma"
q(254, S4, "Hepatic adenoma is described as a benign tumour with what risk of cancer?",
  ["10%", "1%", "25%", "50%"], 0,
  "Hepatic adenoma: benign tumor with a 10% risk of cancer. (Book p254)")
q(254, S4, "The strongest association of hepatic adenoma is with:",
  ["Oral contraceptive pills", "Anabolic steroids", "Alcohol", " smoking"], 0,
  "Strongest association with oral contraceptive pills (OCPs). (Book p254)")
q(254, S4, "Unlike FNH, a hepatic adenoma is usually:",
  ["Symptomatic with hepatomegaly", "Asymptomatic and incidental",
   "Only seen in males", "Associated with a raised AFP"], 0,
  "Usually symptomatic: hepatomegaly (+). (Book p254)")
q(254, S4, "Spontaneous rupture of a hepatic adenoma causes haemoperitoneum, which is the most common:",
  ["Non-traumatic cause of haemoperitoneum", "Cause of haemoperitoneum overall",
   "Cause of upper GI bleeding", "Cause of retroperitoneal bleeding"], 0,
  "Spontaneous rupture → haemoperitoneum (m/c non-traumatic cause). (Book p254)")
q(255, S4, "On triple phase CT, fat within an adenoma makes the lesion:",
  ["Hypodense", "Hyperdense", "Isointense", "Calcified"], 0,
  "Fat content → hypodense. (Book p255)")
q(255, S4, "Intratumoral haemorrhage within an adenoma appears:",
  ["Hyperdense", "Hypodense", "Isointense", "As a fluid level only on MRI"], 0,
  "Intratumoral hemorrhage → hyperdense. (Book p255)")
q(255, S4, "On histopathology an adenoma shows sheets of hepatocytes with:",
  ["No bile duct structures and no Kupffer cells",
   "Atypical bile duct structures and Kupffer cells",
   "A central stellate scar",
   "Psammoma bodies"], 0,
  "HPE: sheets of hepatocytes, no bile duct structures and no Kupffer cells. (Book p255)")
q(255, S4, "The absence of Kupffer cells in an adenoma means it shows:",
  ["No 'hot-spot' on a technetium/sulphur colloid scan",
   "A 'hot-spot' on a sulphur colloid scan",
   "A central scar",
   "Intense uptake on PET"], 0,
  "No Kupffer cells → no 'hot-spot' on a technetium/sulphur colloid scan — the opposite of FNH. (Book p255)")
q(255, S4, "According to this chapter, a hepatic adenoma larger than 5 cm is managed by:",
  ["Close observation", "Immediate resection",
   "Angioembolisation", "Liver transplantation"], 0,
  "The chapter states: >5 cm — close observation. (Book p255)")
q(255, S4, "According to this chapter, a hepatic adenoma smaller than 5 cm is managed by:",
  ["Resection because of the risk of HCC", "Close observation",
   "Angioembolisation", "Ablation"], 0,
  "The chapter states: <5 cm — resection (d/t risk of HCC). (Book p255)")

S5 = "Bordeaux Classification of Hepatic Adenoma"
q(255, S5, "Which subtype of hepatic adenoma carries the maximum risk of bleeding?",
  ["Inflammatory adenoma", "HNF-1 alpha mutated adenoma",
   "β-catenin mutated adenoma", "Unclassified adenoma"], 0,
  "Inflammatory adenoma: maximum risk of bleeding. (Book p255)")
q(255, S5, "The HNF-1 alpha mutated adenoma is typically seen in:",
  ["Young patients, often with multiple lesions", "Elderly men",
   "Patients on anabolic steroids", "Patients with cirrhosis"], 0,
  "HNF-1 alpha mutated: young patient, multiple lesions. (Book p255)")
q(255, S5, "Which subtype of hepatic adenoma carries the maximum risk of cancer?",
  ["β-catenin mutated adenoma", "Inflammatory adenoma",
   "HNF-1 alpha mutated adenoma", "Unclassified adenoma"], 0,
  "β-catenin mutated: maximum risk of cancer. (Book p255)")
q(255, S5, "Anabolic steroid associated adenomas and exon-3 mutations are additional features of the:",
  ["β-catenin mutated adenoma", "Inflammatory adenoma",
   "HNF-1 alpha mutated adenoma", "Hepatocellular carcinoma"], 0,
  "The Bordeaux list adds that β-catenin mutated adenomas are seen in patients on anabolic steroids and show an exon-3 mutation. (Book p255)")

S6 = "Hepatocellular Carcinoma: Risk Factors"
q(255, S6, "The most important risk factor for HCC, ranked above the others in this chapter, is:",
  ["HBV", "HCV", "Alcohol", "Aflatoxin"], 0,
  "Risk factors are listed beginning HBV > HCV. (Book p255)")
q(255, S6, "Which of the following is NOT listed as a risk factor for HCC?",
  ["Primary sclerosing cholangitis", "Alcohol", "Obesity (NAFLD)", "Aflatoxin"], 0,
  "Risk factors listed: HBV > HCV, alcohol, obesity (NAFLD), Thorotrast exposure, aflatoxin and diabetes mellitus. (Book p255)")
q(255, S6, "Thorotrast exposure increases the risk of all of the following EXCEPT:",
  ["Hepatoblastoma", "HCC", "Cholangiocarcinoma", "Renal cell carcinoma"], 0,
  "Thorotrast exposure (an old contrast medium) increases the risk of HCC, cholangiocarcinoma and renal cell carcinoma. (Book p255)")
q(255, S6, "Thorotrast, listed as a risk factor for HCC, was:",
  ["A contrast medium", "An oral hypoglycaemic agent",
   "A herbal remedy", "A chemotherapeutic drug"], 0,
  "Thorotrast exposure (contrast medium) is listed among the risk factors. (Book p255)")

# ------------------------------------------------------------------ p256
S7 = "Paraneoplastic Syndromes and Diagnosis of HCC"
q(256, S7, "A paraneoplastic syndrome is defined as a syndrome:",
  ["Not explained by direct spread or metastasis",
   "Caused by direct invasion of a neighbouring organ",
   "Caused only by the mass effect of the tumour",
   "Occurring only after treatment"], 0,
  "Paraneoplastic syndrome: a syndrome not explained by direct spread or metastasis. (Book p256)")
q(256, S7, "The most common paraneoplastic syndrome associated with HCC is:",
  ["Hypoglycaemia", "Cushing's syndrome", "Gynaecomastia", "Hypercalcaemia"], 0,
  "Hypoglycaemia is the m/c paraneoplastic syndrome of HCC. (Book p256)")
q(256, S7, "Which of the following is NOT listed as a paraneoplastic syndrome of HCC?",
  ["Hypercalcaemia", "Hypoglycaemia", "Cushing's syndrome", "Gynaecomastia"], 0,
  "The listed paraneoplastic syndromes are hypoglycaemia (m/c), Cushing's syndrome and gynaecomastia. (Book p256)")
q(256, S7, "On triple phase CT, HCC in the non-contrast phase is:",
  ["Hypodense", "Hyperdense", "Isointense", "Calcified"], 0,
  "CT phases: HCC — non-contrast hypodense, arterial hyperdense, venous early washout. (Book p256)")
q(256, S7, "On triple phase CT, HCC in the arterial phase is:",
  ["Hyperdense", "Hypodense", "Isointense", "Indistinguishable from a cyst"], 0,
  "Arterial phase: hyperdense — the tumour is supplied by the hepatic artery. (Book p256)")
q(256, S7, "The venous phase behaviour that characterises HCC is:",
  ["Early washout", "Continued filling-in",
   "Peripheral nodular enhancement", "No change in density"], 0,
  "Venous phase: early washout — the hallmark that separates HCC from other lesions. (Book p256)")
q(256, S7, "Metastases in the liver on triple phase CT are:",
  ["Hypodense", "Hyperdense in the arterial phase",
   "Hyperdense in the venous phase", "Isointense throughout"], 0,
  "Metastasis is listed as hypodense, in contrast to the arterial hyperdensity and early washout of HCC. (Book p256)")
q(256, S7, "The CT finding in HCC is described as:",
  ["Classical and diagnostic", "Non-specific", "Only useful for staging", "Inferior to ultrasound"], 0,
  "CT finding is classical and diagnostic, and the triple phase CT helps differentiate HCC from metastasis. (Book p256)")
q(256, S7, "The scores listed for assessing liver function in a patient with HCC include all of the following EXCEPT:",
  ["LI-RADS", "Child-Turcotte-Pugh score", "MELD score", "PELD score"], 0,
  "Scores for assessing liver function: Child-Turcotte-Pugh, MELD and PELD. LI-RADS is the imaging scoring system. (Book p256)")

S8 = "Tumour Markers in HCC"
q(256, S8, "PIVKA, listed as a tumour marker in HCC, expands to:",
  ["Protein induced in vitamin K antagonism (abnormal prothrombin)",
   "Prothrombin-induced vascular kinase activity",
   "Plasma inhibitor of vitamin K absorption",
   "Proliferative index of vitamin K activity"], 0,
  "The marker is described as protein induced in vitamin K antagonism (PIVKA), i.e. abnormal prothrombin. (Book p256)")
q(256, S8, "Which tumour marker is specifically noted to be raised in the fibrolamellar variant of HCC?",
  ["Neurotensin B", "Alpha-fetoprotein", "CA 19-9", "CEA"], 0,
  "Neurotensin B is raised in the fibrolamellar variant. (Book p256)")
q(256, S8, "Which of the following is NOT listed as a tumour marker for HCC?",
  ["CA 19-9", "AFP", "Glypican", "HepPar-1"], 0,
  "Tumour markers listed: AFP, PIVKA (prothrombin), glypican, HepPar-1 and neurotensin B. (Book p256)")
