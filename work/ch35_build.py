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

# ------------------------------------------------------------------ p257
S9 = "Treatment of Localised HCC"
q(257, S9, "Curative resection for HCC is offered to patients with:",
  ["Child-Pugh A and an adequate future liver remnant",
   "Child-Pugh B disease with an adequate remnant",
   "Child-Pugh C disease",
   "Any Child class if the tumour is small"], 0,
  "The localized branch: Child-Pugh A with adequate FLR (>25%) goes to resection. (Book p257)")
q(257, S9, "A patient with Child-Pugh B or C disease, or an inadequate future liver remnant, is considered for:",
  ["Liver transplantation", "Immediate resection",
   "Radiofrequency ablation as first choice", "Best supportive care only"], 0,
  "Child-Pugh B/C and inadequate FLR (<25%) make the patient a candidate for transplant. (Book p257)")
q(257, S9, "FLR expands to:",
  ["Functional liver reserve", "Focal liver remnant",
   "Fibrotic liver reserve", "Functional lobar resection"], 0,
  "FLR: functional liver reserve. (Book p257)")
q(257, S9, "The future liver remnant is assessed using:",
  ["Fibroscan", "Endoscopic ultrasound", "Plain X-ray", "MRCP"], 0,
  "FLR is assessed using Fibroscan. (Book p257)")
q(257, S9, "Resection can be done when the future liver remnant is:",
  ["More than 25%", "More than 10%", "More than 50%", "More than 75%"], 0,
  ">25% — resection can be done. (Book p257)")
q(257, S9, "Which procedure is listed for triggering hypertrophy of the other lobe before resection?",
  ["Portal vein embolisation", "Trans-arterial chemoembolisation",
   "Radiofrequency ablation", "Percutaneous ethanol injection"], 0,
  "Portal vein embolisation triggers hypertrophy of the other lobe. (Book p257)")
q(257, S9, "The Nimura technique / ALPPS is listed in the management of HCC under:",
  ["Measures used when the future liver remnant is inadequate",
   "Palliative therapy for metastatic disease",
   "Treatment of haemangioma",
   "Staging laparoscopy"], 0,
  "Nimura technique/ALPPS appears in the branch dealing with an inadequate FLR. (Book p257)")

S10 = "Milan Criteria, Ablation and Palliative Therapy"
q(257, S10, "The Milan criteria for liver transplantation in HCC are:",
  ["A single tumour <5 cm or up to 3 tumours each <3 cm, with no metastasis",
   "Any number of tumours provided each is <5 cm",
   "A single tumour <10 cm",
   "Any tumour without vascular invasion"], 0,
  "Milan criteria: single tumor <5 cm OR 1-3 tumors <3 cm, with no metastasis. (Book p257)")
q(257, S10, "Radiofrequency ablation is listed for HCC lesions of size:",
  ["Less than 3 cm", "More than 3 cm", "More than 5 cm", "Any size"], 0,
  "RFA: <3 cm. (Book p257)")
q(257, S10, "Microwave ablation is listed for lesions:",
  ["More than 3 cm", "Less than 3 cm", "Less than 1 cm", "Only in the left lobe"], 0,
  "Microwave ablation: >3 cm. (Book p257)")
q(257, S10, "Which of the following is listed among the local ablative/trans-arterial options when transplantation is not possible?",
  ["Percutaneous ethanol injection", "Systemic chemotherapy alone",
   "External beam radiotherapy", "Cryotherapy of the whole liver"], 0,
  "The listed options are RFA, microwave ablation, percutaneous ethanol injection, TACE and TARE. (Book p257)")
q(257, S10, "Trans-arterial radioembolisation (TARE) uses:",
  ["Yttrium spheres", "Iodine-131 seeds", "Iridium wires", "Gold grains"], 0,
  "Trans-arterial radioembolisation/TARE — yttrium spheres are used. (Book p257)")
q(257, S10, "Trans-arterial chemoembolisation is abbreviated as:",
  ["TACE", "TARE", "TAE", "TEA"], 0,
  "Trans-arterial chemoembolisation = TACE. (Book p257)")
q(257, S10, "The first-line systemic agent listed for advanced/metastatic HCC is:",
  ["Sorafenib, a tyrosine kinase inhibitor", "Bevacizumab",
   "5-fluorouracil", "Cetuximab"], 0,
  "Palliative treatment for advanced/metastatic disease: sorafenib (tyrosine kinase inhibitor). (Book p257)")
q(257, S10, "Which immunotherapy drugs are listed for advanced HCC?",
  ["Pembrolizumab / nivolumab", "Bevacizumab alone",
   "Trastuzumab and pertuzumab", "Rituximab"], 0,
  "The second palliative option listed is pembrolizumab/nivolumab. (Book p257)")

S11 = "Prognostic Indicators and the Fibrolamellar Variant"
q(257, S11, "Which of the following is NOT listed as a prognostic indicator for HCC?",
  ["LI-RADS", "CLIP", "Okuda", "BCLC (Barcelona Clinic Score)"], 0,
  "Prognostic indicators listed: CLIP, Okuda and BCLC. (Book p257)")
q(257, S11, "The most common prognostic factor in HCC is:",
  ["The stage of the disease", "The AFP level alone",
   "The patient's age", "The size of the spleen"], 0,
  "m/c prognostic factor in HCC: stage of disease. (Book p257)")
q(257, S11, "The most common site of metastasis from HCC is the:",
  ["Lungs", "Bone", "Brain", "Adrenals"], 0,
  "m/c site of metastasis: lungs. (Book p257)")
q(257, S11, "The fibrolamellar variant of HCC occurs in:",
  ["Young patients with a non-cirrhotic liver",
   "Elderly cirrhotic patients",
   "Only in women",
   "Only in patients with hepatitis B"], 0,
  "Fibrolamellar variant: young patients, non-cirrhotic liver, male = female. (Book p257)")
q(257, S11, "The prognosis of the fibrolamellar variant is:",
  ["Good", "Very poor", "The same as conventional HCC", "Invariably fatal within 6 months"], 0,
  "Fibrolamellar variant: good prognosis. (Book p257)")
q(257, S11, "In the fibrolamellar variant of HCC the AFP is:",
  ["Not raised", "Markedly raised", "Raised only in children", "Used to monitor treatment"], 0,
  "AFP is not raised in the fibrolamellar variant (neurotensin B is the marker that rises). (Book p257)")

# ------------------------------------------------------------------ p258
S12 = "Principles of Liver Resection"
q(258, S12, "The principles of liver resection listed include:",
  ["Trendelenburg position with fluid restriction",
   "Reverse Trendelenburg position with aggressive fluid loading",
   "Prone positioning",
   "Intra-operative normovolaemic haemodilution only"], 0,
  "Principle of liver resection: Trendelenburg position + fluid restriction (to keep venous pressure low). (Book p258)")
q(258, S12, "The three most critical factors in liver resection are:",
  ["Amount of liver resected, blood loss and the condition of the liver (Child-Pugh score)",
   "Age, sex and tumour size",
   "Portal pressure, bile duct diameter and platelet count",
   "Anaesthesia time, incision length and drain use"], 0,
  "The 3 most critical factors: amount of liver resected, blood loss and condition (Child-Pugh score). (Book p258)")
q(258, S12, "A future liver remnant of more than 50% is associated with:",
  ["Less mortality", "Increased mortality",
   "No change in mortality", "A guaranteed cure"], 0,
  "FLR >50%: less mortality. (Book p258)")
q(258, S12, "Mortality rises when the future liver remnant falls below:",
  ["20-25%", "50%", "40%", "10%"], 0,
  "FLR <20-25%: ↑ mortality. (Book p258)")
q(258, S12, "All of the following are listed complications of liver resection EXCEPT:",
  ["Retrograde ejaculation", "Hepatic dysfunction", "Bile leak", "Ascites"], 0,
  "Complications listed: hepatic dysfunction, bile leak, ascites and infections. (Book p258)")

S13 = "Colorectal Liver Metastases"
q(258, S13, "The most common site of metastasis from colorectal cancer is the:",
  ["Liver", "Lung", "Bone", "Peritoneum"], 0,
  "Liver is the m/c site for colorectal cancer metastases. (Book p258)")
q(258, S13, "Approximately what proportion of colorectal cancers show liver metastases?",
  ["60%", "6%", "20%", "90%"], 0,
  "60% of colorectal cancers show liver metastases. (Book p258)")
q(258, S13, "Liver metastases detected less than 1 year after the primary are termed:",
  ["Synchronous", "Metachronous", "Solitary", "Satellite"], 0,
  "Types: synchronous (<1 yr) and metachronous (>1 yr). (Book p258)")
q(258, S13, "Metastases detected more than 1 year after treatment of the primary are:",
  ["Metachronous", "Synchronous", "Recurrent", "De novo"], 0,
  "Metachronous: >1 year. (Book p258)")
q(258, S13, "The investigation of choice for colorectal liver metastases shows:",
  ["Hypodense lesions on triple phase CT", "Hyperdense lesions on triple phase CT",
   "Calcified lesions on plain X-ray", "Hot spots on a sulphur colloid scan"], 0,
  "Investigation: triple phase CT (IOC) → hypodense lesions. (Book p258)")
q(258, S13, "Bevacizumab, used in colorectal liver metastases, is a monoclonal antibody against:",
  ["VEGF", "EGFR", "HER2", "CD20"], 0,
  "Immunotherapy: bevacizumab — a monoclonal antibody against VEGF. (Book p258)")
q(258, S13, "Surgical resection of colorectal liver metastases is advised when:",
  ["The future liver remnant is adequate and resection is possible, as it improves survival",
   "There are more than ten lesions",
   "There is extrahepatic disease even if resection is possible",
   "The primary tumour is still in situ"], 0,
  "Surgical resection is done if adequate FLR plus resection is possible — and it increases survival. (Book p258)")

# ------------------------------------------------------------------ p259
S14 = "Hepatoblastoma"
q(259, S14, "Hepatoblastoma typically presents at what age?",
  ["Less than 3 years", "10-20 years", "40-50 years", "Over 60 years"], 0,
  "Hepatoblastoma: <3 yrs of age. (Book p259)")
q(259, S14, "Which of the following is NOT listed as a clinical feature of hepatoblastoma?",
  ["Jaundice as an early sign", "Hepatomegaly", "Anaemia", "Lung metastasis at diagnosis in about 50%"], 0,
  "Clinical features: <3 yrs, hepatomegaly, anaemia, lung metastasis at diagnosis (50%) and jaundice — jaundice is a LATE sign. (Book p259)")
q(259, S14, "At diagnosis, roughly what proportion of hepatoblastoma patients have lung metastases?",
  ["50%", "5%", "10%", "90%"], 0,
  "Lung metastasis at diagnosis: 50%. (Book p259)")
q(259, S14, "The investigation of choice for hepatoblastoma is:",
  ["Triple phase CT (CECT)", "Ultrasound alone", "MRCP", "Liver biopsy alone"], 0,
  "IOC: triple phase CT (CECT). (Book p259)")
q(259, S14, "The sequence of treatment in hepatoblastoma is:",
  ["Surgery followed by chemotherapy", "Chemotherapy followed by surgery",
   "Radiotherapy alone", "Chemotherapy alone"], 0,
  "Management: surgery → chemotherapy. (Book p259)")
q(259, S14, "The correct statement about hepatoblastoma with metastases is that:",
  ["Aggressive treatment is given even if metastases are present",
   "Treatment is palliative only once metastases appear",
   "Metastases exclude surgery",
   "Only the lung lesion is treated"], 0,
  "The page emphasises aggressive treatment even if metastasis is present. (Book p259)")

S15 = "Intrahepatic Cholangiocarcinoma"
q(259, S15, "The incidence of intrahepatic cholangiocarcinoma is about:",
  ["10%", "1%", "30%", "50%"], 0,
  "Incidence: 10%. (Book p259)")
q(259, S15, "Intrahepatic cholangiocarcinoma is the:",
  ["Second most common primary hepatic neoplasm",
   "Most common primary hepatic neoplasm",
   "Third most common primary hepatic neoplasm",
   "Rarest primary hepatic neoplasm"], 0,
  "It is the 2nd m/c primary hepatic neoplasm (after HCC). (Book p259)")
q(259, S15, "Which of the following is a risk factor for intrahepatic cholangiocarcinoma?",
  ["Primary sclerosing cholangitis", "Oral contraceptive pills",
   "Hepatitis A infection", "Haemochromatosis"], 0,
  "Risk factors: primary sclerosing cholangitis (PSC), hepatolithiasis and choledochal cyst. (Book p259)")
q(259, S15, "Which risk factor is shared by intrahepatic cholangiocarcinoma and gallbladder disease through stone formation within the ducts?",
  ["Hepatolithiasis", "Alcoholic cirrhosis", "Wilson disease", "Alpha-1 antitrypsin deficiency"], 0,
  "Hepatolithiasis is listed as a risk factor for intrahepatic cholangiocarcinoma. (Book p259)")
q(259, S15, "Compared with HCC, jaundice in intrahepatic cholangiocarcinoma appears:",
  ["Early", "Late", "Never", "Only after lung metastasis"], 0,
  "Clinical features: jaundice (early sign) and hepatomegaly. (Book p259)")
q(259, S15, "The tumour marker picture in intrahepatic cholangiocarcinoma is:",
  ["Normal AFP with a markedly raised CA 19-9",
   "Raised AFP with a normal CA 19-9",
   "Raised AFP and raised CA 19-9",
   "Normal AFP and normal CA 19-9"], 0,
  "Investigation: IOC triple phase CT, AFP normal and S. CA 19-9 ↑↑. (Book p259)")
q(259, S15, "A 60-year-old with primary sclerosing cholangitis develops a hepatic mass with early jaundice, a normal AFP and a markedly raised CA 19-9. The diagnosis is:",
  ["Intrahepatic cholangiocarcinoma", "Hepatocellular carcinoma",
   "Hepatoblastoma", "Liver metastasis"], 0,
  "PSC is a risk factor, jaundice is early, AFP is normal and CA 19-9 is markedly raised — intrahepatic cholangiocarcinoma. (Book p259)")

# ------------------------------------------------------------------ units
def sec_ids(*labels):
    return [x["id"] for x in Q if x["sec"] in labels]


def first_page(label):
    for x in Q:
        if x["sec"] == label:
            return x["page"]
    return 0


UNIT_DEFS = [
    (S1, "Triple phase CT is the entry ticket to every liver mass, and LI-RADS turns its appearance into a shared language: LR-1 is certainly benign, LR-5 is certainly HCC, and LR-3 in the middle is where follow-up or biopsy earns its keep."),
    (S2, "Haemangiomas are simply a tangle of vessels, common in women and found by accident. Non-contrast hypodense with peripheral nodular arterial enhancement is the signature; leave them alone unless they are big enough to bleed, hurt or consume clotting factors."),
    (S3, "FNH is the great mimicker that needs no operation: a young woman, a central stellate scar fed by a dilated arteriole, bile ductules and Kupffer cells that light up the sulphur colloid scan, and a completely normal AFP. Observe it."),
    (S4, "Adenoma is FNH's dangerous twin — OCP-related, symptomatic, and the commonest non-traumatic cause of haemoperitoneum when it ruptures. Fat and haemorrhage shape its CT appearance, and the absence of Kupffer cells means a cold sulphur colloid scan."),
    (S5, "The Bordeaux classification decides an adenoma's behaviour: inflammatory tumours bleed most, HNF-1α tumours present young and multiple, and β-catenin tumours — the anabolic-steroid, exon-3 mutated group — carry the malignant risk."),
    (S6, "HCC follows its risk factors: HBV above HCV, then alcohol, NAFLD, aflatoxin and diabetes. Thorotrast is the historical curiosity worth remembering because it also predisposes to cholangiocarcinoma and renal cell carcinoma."),
    (S7, "HCC declares itself on the phases — hypodense, then hyperdense, then early washout — and declares itself systemically through hypoglycaemia, Cushing's syndrome or gynaecomastia, none of which needs a metastasis to explain it."),
    (S8, "Markers matter when the scan is equivocal: AFP, PIVKA (the abnormal prothrombin induced by vitamin K antagonism), glypican and HepPar-1 — and neurotensin B, which rises specifically in the fibrolamellar variant."),
    (S9, "Resection is a question of reserve rather than courage: Child-Pugh A with an FLR above 25% measured on Fibroscan goes to theatre, and when the remnant is short you can make it grow with portal vein embolisation or an ALPPS-type strategy."),
    (S10, "For everyone else there is a ladder: transplant within Milan criteria, and when no donor appears, RFA under 3 cm, microwave over 3 cm, ethanol injection, TACE or TARE with yttrium spheres — and sorafenib or pembrolizumab/nivolumab once the disease is advanced."),
    (S11, "Prognosis is still driven by stage, scored variously by CLIP, Okuda or BCLC, and the lung is where HCC most often lands. The fibrolamellar variant is the welcome exception: a young patient, a non-cirrhotic liver, a normal AFP and a genuinely good outlook."),
    (S12, "Cutting liver is as much physiology as anatomy: head down, fluids restricted, and three things watched — how much liver is taken, how much blood is lost and how good the liver was to begin with. Below a 20-25% remnant, mortality climbs."),
    (S13, "The liver is where colorectal cancer goes, and it goes there in about 60% of patients. Synchronous lesions within a year and metachronous ones after it are both worth resecting when the remnant allows, usually alongside bevacizumab against VEGF."),
    (S14, "Hepatoblastoma is the tumour of the under-threes: hepatomegaly, anaemia, half of them already seeded to lung at diagnosis and jaundice only late. Even with metastases the page insists on aggressive surgery followed by chemotherapy."),
    (S15, "Intrahepatic cholangiocarcinoma closes the chapter as the second commonest primary liver cancer, born of PSC, stones or a choledochal cyst. Unlike HCC it jaundices early, keeps AFP normal and sends CA 19-9 soaring."),
]

UNITS = []
for i, (title, guide) in enumerate(UNIT_DEFS, 1):
    UNITS.append({
        "id": f"SURG-U35-{i}",
        "ch": 35,
        "n": i,
        "title": title,
        "sec": f"{title} · p{first_page(title)}",
        "qs": sec_ids(title),
        "guide": guide,
    })

covered = [i for u in UNITS for i in u["qs"]]
assert covered == [x["id"] for x in Q], "units must cover questions in order"
assert len(set(covered)) == len(covered), "duplicate question in units"

data = {"questions": Q, "units": UNITS}
with open("data/ch35.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
print(f"ch35: {len(Q)} questions, {len(UNITS)} units")
