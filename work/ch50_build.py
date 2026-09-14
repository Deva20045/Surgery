#!/usr/bin/env python3
"""Build data/ch50.json — Transplant Surgery (Marrow Surgery Ed 8, pp377-385)."""
import json

Q = []

def q(page, sec, text, correct, wrongs, note=None):
    opts = [correct] + list(wrongs)
    assert len(opts) == 4
    Q.append({
        "id": f"SURG-C50-{len(Q)+1:03d}",
        "sec": sec,
        "page": page,
        "q": text,
        "opts": opts,
        "ans": 0,
        "exp": (note or correct) + f" (Book p{page})",
    })

# ------------------------------------------------------------------ p377
S1 = "Types of Grafts, Donors and Maastricht Classification"
q(377, S1, "Autograft is a graft from:", "Same person (Eg: Skin graft)", ["Identical twins", "Same species", "Different species"])
q(377, S1, "Isograft is a graft between:", "Identical twins", ["Same person", "Same species", "Different species"])
q(377, S1, "Allograft is a graft among:", "Same species", ["Same person", "Identical twins", "Different species"])
q(377, S1, "Xenograft is a graft between:", "Different species", ["Same person", "Identical twins", "Same species"])
q(377, S1, "A type of donor is:", "Living donors", ["Xeno donors", "Dead organs only", "Artificial donors"])
q(377, S1, "The other type of donor is:", "Dead donors", ["Living donors", "Twin donors", "Animal donors"])
q(377, S1, "Maastricht Class I presentation is:", "Dead on arrival", ["Unsuccessful resuscitation", "Anticipated cardiac arrest", "Cardiac arrest in brain dead donor"])
q(377, S1, "Maastricht Class I situation is:", "Uncontrolled", ["Controlled", "Anticipated", "Planned"])
q(377, S1, "Organs procurable in Maastricht Class I are:", "Heart valves, cornea", ["Kidney, heart valves, cornea", "All organs except heart", "All organs including heart"])
q(377, S1, "Maastricht Class II presentation is:", "Unsuccessful resuscitation", ["Dead on arrival", "Anticipated cardiac arrest", "Unexpected arrest in hospital"])
q(377, S1, "Maastricht Class II situation is:", "Uncontrolled", ["Controlled", "Elective", "Planned"])
q(377, S1, "Organs procurable in Maastricht Class II are:", "Kidney, heart valves, cornea", ["Heart valves, cornea only", "All organs except heart", "Heart only"])
q(377, S1, "Maastricht Class III presentation is:", "Anticipated cardiac arrest", ["Dead on arrival", "Unsuccessful resuscitation", "Unexpected arrest in hospital"])
q(377, S1, "Maastricht Class III situation is:", "Controlled", ["Uncontrolled", "Unwitnessed", "Out-of-hospital"])
q(377, S1, "Maastricht Class IV presentation is:", "Cardiac arrest in brain dead donor", ["Dead on arrival", "Anticipated cardiac arrest", "Unsuccessful resuscitation"])
q(377, S1, "Maastricht Class IV situation is:", "Controlled", ["Uncontrolled", "Unexpected", "Unwitnessed"])
q(377, S1, "Maastricht Class V presentation is:", "Unexpected cardiac arrest in a hospital patient", ["Dead on arrival", "Anticipated cardiac arrest", "Cardiac arrest in brain dead donor"])
q(377, S1, "Maastricht Class V situation is:", "Uncontrolled", ["Controlled", "Elective", "Planned"])
q(377, S1, "Organs procurable in Maastricht Class III–V are:", "All organs except heart", ["Heart valves, cornea only", "Kidney only", "Heart only"])

# ------------------------------------------------------------------ p377-378
S2 = "Storage, Cold Ischemia and Machine Perfusion"
q(377, S2, "Static cold storage uses:", "UW (University of Wisconsin) solution", ["Normal saline", "Ringer lactate", "Distilled water"])
q(377, S2, "UW solution is stored at:", "4°C", ["37°C", "−20°C", "25°C"])
q(377, S2, "A constituent of UW solution is:", "Hydroxyethyl starch (HES)", ["Hydroxyapatite", "Hetastarch-free saline", "Albumin only"])
q(377, S2, "UW solution contains:", "Lactobionic acid (As lactone)", ["Lactic acid only", "Citric acid", "Acetic acid"])
q(377, S2, "A constituent of UW solution is:", "Adenosine", ["Adrenaline", "ATPase", "Adenine only"])
q(377, S2, "UW solution contains:", "Allopurinol", ["Allopregnanolone", "Aspirin", "Amiodarone"])
q(377, S2, "UW solution contains glutathione in the:", "Reduced form", ["Oxidized form", "Gaseous form", "Solid form"])
q(377, S2, "UW solution is injected into the donor through:", "Aorta & portal vein", ["IVC & aorta", "Renal vein", "Carotid artery"])
q(377, S2, "UW solution flushes out blood and thereby:", "Prevents thrombosis", ["Causes thrombosis", "Increases clotting", "Lyses organs"])
q(377, S2, "UW solution cools organs and thereby:", "Decreases oxygen requirement", ["Increases oxygen requirement", "Stops perfusion", "Warms organs"])
q(377, S2, "UW solution replaces normal extracellular fluid with:", "Preservation fluid", ["Blood", "Bile", "Lymph"])
q(378, S2, "Safe maximum cold ischemia time for the kidney is:", "36 hours (max)", ["12–18 hours", "4–6 hours", "3–6 hours"])
q(378, S2, "The organ with maximum cold ischemia time is the:", "Kidney", ["Liver", "Heart", "Lung"])
q(378, S2, "Safe maximum cold ischemia time for the liver is:", "12–18 hours", ["36 hours", "4–6 hours", "3–8 hours"])
q(378, S2, "Safe maximum cold ischemia time for the pancreas is:", "<10–18 hours", ["36 hours", "4–6 hours", "3–6 hours"])
q(378, S2, "Safe maximum cold ischemia time for the small intestine is:", "4–6 hours", ["36 hours", "12–18 hours", "3–8 hours"])
q(378, S2, "Safe maximum cold ischemia time for the heart is:", "3–6 hours (Least)", ["36 hours", "12–18 hours", "3–8 hours"])
q(378, S2, "The organ with least cold ischemia time is the:", "Heart", ["Kidney", "Liver", "Lung"])
q(378, S2, "Safe maximum cold ischemia time for the lung is:", "3–8 hours", ["36 hours", "12–18 hours", "4–6 hours"])
q(378, S2, "Normothermic machine perfusion stores organs in:", "Normal temperature", ["4°C", "−20°C", "Iced saline"])
q(378, S2, "Organs for normothermic machine perfusion include:", "Heart, lung, liver, kidney", ["Only kidney", "Only cornea", "Heart valves only"])
q(378, S2, "An advantage of normothermic machine perfusion is a:", "More physiological state", ["Less physiological state", "Frozen state", "Dry state"])
q(378, S2, "Normothermic perfusion restores function ex-vivo and replenishes depleted:", "ATPs", ["Glucose", "Lipids", "Calcium"])
q(378, S2, "Normothermic perfusion allows utility of:", "Marginal donors", ["Only ideal donors", "No donors", "Animal donors"])
q(378, S2, "Normothermic perfusion gives:", "Early graft function", ["Delayed graft function", "No graft function", "Chronic rejection"])

# ------------------------------------------------------------------ p378-379
S3 = "Renal Transplantation: Indications, Donors and Technique"
q(378, S3, "The most common indication for renal transplant in adults is:", "Diabetic nephropathy", ["Glomerulonephritis", "Polycystic kidney", "Renal stones"])
q(378, S3, "The most common indication for renal transplant in children is:", "Glomerulonephritis", ["Diabetic nephropathy", "VUR only", "Hypertension"])
q(378, S3, "Extended donor criteria include a fit patient aged:", ">60 years", ["<60 years", ">80 years only", "<40 years"])
q(378, S3, "Extended criteria also include >50 yrs plus ≥2 of the following, including:", "Death d/t stroke", ["Death d/t trauma only", "No comorbidity", "Young age"])
q(378, S3, "Extended donor criteria include history of:", "Hypertension", ["Hypotension", "Diabetes only", "Asthma"])
q(378, S3, "Extended donor criteria include serum creatinine:", ">1.5 mg/dL", ["<1.0 mg/dL", "<0.5 mg/dL", ">10 mg/dL"])
q(378, S3, "Dual kidney transplantation uses a pair of marginal quality kidneys to provide:", "Adequate nephron mass", ["Inadequate mass", "Single nephron", "No function"])
q(378, S3, "Dual kidneys are transplanted to:", "One recipient", ["Two recipients", "Three recipients", "No recipient"])
q(378, S3, "Dual kidneys are placed in the:", "Same iliac fossa", ["Opposite fossae", "Renal fossa", "Thorax"])
q(378, S3, "Dual transplantation is used in:", "Extended criteria in patients (Donors)", ["Standard criteria only", "Living donors only", "Children only"])
q(378, S3, "Investigations in a donor include:", "ABO compatibility", ["Only age", "Only weight", "Only height"])
q(378, S3, "Donor workup includes:", "Rh compatibility", ["ABO only", "No blood grouping", "Only HLA"])
q(378, S3, "HLA compatibility loci are:", "A, B, DR", ["A, B only", "C, D only", "X, Y"])
q(378, S3, "The most important HLA locus is:", "DR", ["A", "B", "C"])
q(378, S3, "Donor workup includes:", "KFT compatibility", ["LFT only", "CBC only", "ECG only"])
q(378, S3, "On USG KUB, the preferred donor kidney is the:", "Left kidney", ["Right kidney", "Either equally", "Horseshoe kidney"])
q(378, S3, "The left kidney is preferred due to a:", "Longer renal vein", ["Shorter renal vein", "Longer artery", "Absent ureter"])
q(379, S3, "Renal transplant is heterotopic, placed in the:", "Iliac fossa", ["Renal fossa", "Pelvis midline", "Thorax"])
q(379, S3, "In a dead donor, a cusp of aorta can be:", "Taken", ["Never taken", "Ligated always", "Discarded"])
q(379, S3, "In a dead donor, the renal artery is anastomosed to the:", "External iliac artery", ["Internal iliac artery", "Aorta directly", "Renal artery stump"])
q(379, S3, "Dead-donor arterial anastomosis is:", "End-to-side anastomosis", ["End-to-end anastomosis", "Side-to-side", "No anastomosis"])
q(379, S3, "In a live donor, the renal artery is anastomosed to the:", "Internal iliac artery", ["External iliac artery", "Aorta", "Femoral artery"])
q(379, S3, "Live-donor arterial anastomosis is:", "End-to-end anastomosis", ["End-to-side anastomosis", "Side-to-side", "Patch graft"])
q(379, S3, "The renal vein is anastomosed to the:", "External iliac vein", ["Internal iliac vein", "IVC", "Portal vein"])
q(379, S3, "Renal vein anastomosis is:", "End-to-side anastomosis", ["End-to-end anastomosis", "Side-to-side", "Ligated"])
q(379, S3, "The donor ureter is anastomosed to the:", "Bladder", ["Ureter", "Renal pelvis", "Urethra"])
q(379, S3, "Vascular anastomoses use:", "Proline suture", ["Vicryl", "Catgut", "Silk"])
q(379, S3, "Ureteric anastomosis uses:", "Vicryl (PDS)", ["Proline", "Steel wire", "Nylon"])
q(379, S3, "Acute allograft dysfunction is a rise of serum creatinine >10% of baseline or:", ">30 μmol/L", [">300 μmol/L", ">3 μmol/L", ">130 μmol/L"])
q(379, S3, "A cause of early graft dysfunction is:", "Acute rejection", ["Chronic rejection", "Hyperacute rejection only", "No rejection"])
q(379, S3, "Early graft dysfunction may be due to:", "Calcineurin inhibitor toxicity", ["Antibiotic toxicity", "Vitamin deficiency", "Steroid excess only"])
q(379, S3, "A cause of early graft dysfunction is:", "Dehydration", ["Overhydration", "Hyperkalemia only", "Anaemia only"])
q(379, S3, "Early graft dysfunction may follow:", "Urinary tract infection or pyelonephritis", ["Pneumonia only", "Meningitis", "Cellulitis"])
q(379, S3, "A surgical cause of early graft dysfunction is:", "Ureteric obstruction", ["Ureteric reflux only", "Bladder stone", "Meatal stenosis"])
q(379, S3, "Early graft dysfunction may be due to:", "Renal vein or artery thrombosis", ["Renal cyst", "Renal stone", "Renal ptosis"])
q(379, S3, "A cause of early graft dysfunction is:", "Sepsis", ["Asepsis", "Allergy", "Asthma"])
q(379, S3, "5-year graft survival with a live donor is:", "90%", ["85%", "70%", "50%"])
q(379, S3, "5-year graft survival with a dead donor is:", "85%", ["90%", "95%", "60%"])
q(379, S3, "Graft survival improved due to:", "Immunosuppression", ["No drugs", "Only surgery", "Radiotherapy"])
q(379, S3, "Graft survival improved due to better:", "Surgical technique", ["No technique", "Blind surgery", "Open biopsy"])

# ------------------------------------------------------------------ p380
S4 = "Rejection, Banff, Infection, Malignancy and PTLD"
q(380, S4, "Hyperacute rejection is:", "On table rejection", ["Rejection after 6 months", "Rejection after a year", "Chronic rejection"])
q(380, S4, "Hyperacute rejection shows a:", "Dusky kidney", ["Pale kidney", "Enlarged liver", "Normal kidney"])
q(380, S4, "Hyperacute rejection causes:", "No urine", ["Polyuria", "Haematuria only", "Pyuria"])
q(380, S4, "Hyperacute rejection is due to:", "Pre-formed antibody", ["T-cells", "No immunity", "Drugs"])
q(380, S4, "The pre-formed antibody in hyperacute rejection is the:", "HLA antibody", ["ABO antibody only", "Rh antibody", "Platelet antibody"])
q(380, S4, "Hyperacute rejection is a:", "Type II hypersensitivity reaction", ["Type I reaction", "Type III reaction", "Type IV reaction"])
q(380, S4, "Histology of hyperacute rejection shows:", "Intravascular thrombosis", ["Glomerular sclerosis", "Tubular atrophy only", "Normal vessels"])
q(380, S4, "Acute T-cell rejection:", "Responds to immunosuppression", ["Never responds", "Needs re-transplant", "Is untreatable"])
q(380, S4, "Acute antibody-mediated rejection has:", "Less response to immunosuppression", ["Better response", "No treatment needed", "Spontaneous cure"])
q(380, S4, "Chronic rejection occurs after:", ">6 months", ["<1 week", "On table", "Within a day"])
q(380, S4, "The most common type of rejection is:", "Chronic", ["Hyperacute", "Acute", "No rejection"])
q(380, S4, "Chronic rejection is a:", "Type IV hypersensitivity", ["Type I hypersensitivity", "Type II hypersensitivity", "Type III hypersensitivity"])
q(380, S4, "Histology of chronic rejection shows:", "Glomerular sclerosis", ["Intravascular thrombosis", "Normal glomeruli", "Acute tubular necrosis"])
q(380, S4, "The histological classification of rejection is the:", "Banff classification", ["Milan criteria", "Child Pugh", "MELD score"])
q(380, S4, "Biopsy type for kidney and liver rejection is:", "Needle biopsy", ["Endoscopic mucosal biopsy", "Subendocardial biopsy", "Excision biopsy"])
q(380, S4, "Biopsy type for bowel rejection is:", "Endoscopic mucosal biopsy", ["Needle biopsy", "Subendocardial biopsy", "Skin biopsy"])
q(380, S4, "Biopsy type for heart rejection is:", "Subendocardial biopsy through jugular vein", ["Needle biopsy", "Endoscopic biopsy", "Open biopsy"])
q(380, S4, "The most common infection in the 1st month post-transplant is:", "Bacterial infections", ["Viral infections", "Fungal infections", "Parasitic infections"])
q(380, S4, "The most common infection overall post-transplant is:", "Viral infection", ["Bacterial infection", "Fungal infection", "Protozoal infection"])
q(380, S4, "The most common viral infection post-transplant is:", "Cytomegalovirus", ["BK virus", "EBV", "Hepatitis B"])
q(380, S4, "A viral infection post-transplant is:", "BK virus", ["Staphylococcus", "E. coli", "Candida"])
q(380, S4, "The most common malignancy post-transplant is:", "Skin cancer", ["Breast cancer", "Hematological cancer", "Lung cancer"])
q(380, S4, "Post-transplant skin cancer is commonly:", "Squamous cell carcinoma", ["Basal cell carcinoma", "Melanoma", "Merkel cell"])
q(380, S4, "The 2nd most common malignancy post-transplant is:", "Hematological", ["Skin", "Breast", "Colon"])
q(380, S4, "Post renal transplant, breast cancer may occur as a:", "Malignancy", ["Infection", "Rejection", "Vascular event"])
q(380, S4, "Post transplant lympho-proliferative disorders (PTLD) are due to:", "EBV", ["CMV", "BK virus", "HBV"])
q(380, S4, "PTLD has a:", "High mortality rate", ["Low mortality rate", "No mortality", "Benign course"])
q(380, S4, "CNS involvement in PTLD means:", "Poor prognosis", ["Good prognosis", "No significance", "Cure"])
q(380, S4, "PTLD involves:", "B-cell mediated immunity", ["T-cell immunity only", "No immunity", "NK cells only"])
q(380, S4, "PTLD presents like infectious mononucleosis with:", "Fever + lymphadenopathy", ["Jaundice + ascites", "Chest pain + cough", "Haematuria + pain"])

# ------------------------------------------------------------------ p381
S5 = "Vascular Events, Pancreatic and Liver Transplant Assessment"
q(381, S5, "Renal vein thrombosis is the:", "Most common vascular complication", ["Least common complication", "Rare event", "Benign finding"])
q(381, S5, "Renal vein thrombosis leads to:", "Decreased graft function", ["Increased graft function", "No change", "Polyuria"])
q(381, S5, "Renal vein thrombosis is managed with:", "Anticoagulants", ["Balloon dilatation", "Re-transplantation", "Observation"])
q(381, S5, "Renal artery stenosis has:", "Gradual onset", ["Sudden onset", "On-table onset", "No onset"])
q(381, S5, "Renal artery stenosis causes:", "Hypertension", ["Hypotension", "No BP change", "Bradycardia"])
q(381, S5, "Renal artery stenosis decreases:", "Graft function", ["Blood pressure", "Creatinine", "Proteinuria"])
q(381, S5, "Renal artery stenosis is managed with:", "Balloon dilatation", ["Anticoagulants", "Re-transplantation", "Nephrectomy"])
q(381, S5, "Investigation for post-transplant vascular events is:", "CT angiography", ["USG KUB", "Plain X-ray", "ECG"])
q(381, S5, "Diabetic nephropathy needs:", "Combined kidney + pancreas transplantation (Tx)", ["Kidney alone always", "Pancreas alone always", "No transplant"])
q(381, S5, "Bladder anastomosis of pancreatic transplant monitors function with:", "Insulin", ["Glucagon", "Somatostatin", "Bile"])
q(381, S5, "Bladder drainage also monitors:", "Amylase", ["Lipase only", "Trypsin only", "Bilirubin"])
q(381, S5, "Complications of bladder anastomosis begin in:", "3–4 yrs", ["3–4 days", "3–4 weeks", "10 years"])
q(381, S5, "On complications, bladder anastomosis is converted to:", "Enteric anastomosis", ["Gastric anastomosis", "No anastomosis", "Skin anastomosis"])
q(381, S5, "Enteric anastomosis is the:", "Better procedure", ["Worse procedure", "Obsolete procedure", "Experimental procedure"])
q(381, S5, "The disadvantage of enteric anastomosis is:", "Difficult monitoring", ["Easy monitoring", "No complications", "Early failure"])
q(381, S5, "The most common cause for liver transplant in adults is:", "Cirrhosis (D/t hep B, hep C, alcohol induced)", ["Acute liver failure", "HCC only", "Biliary atresia"])
q(381, S5, "The most common cause for liver transplant in children is:", "Extrahepatic biliary atresia", ["Cirrhosis", "Hepatitis B", "Autoimmune hepatitis"])
q(381, S5, "In liver transplantation, HLA matching is:", "Not important", ["Most important", "Mandatory", "The only criterion"])
q(381, S5, "In liver transplant, hyperacute rejection is:", "Not seen", ["Common", "Universal", "The m/c type"])
q(381, S5, "Child Pugh Class A score is:", "5–6", ["7–9", "10–15", "0–4"])
q(381, S5, "Child Pugh Class B score is:", "7–9", ["5–6", "10–15", "16–20"])
q(381, S5, "Child Pugh Class C score is:", "10–15", ["5–6", "7–9", "0–5"])
q(381, S5, "Liver transplantation is indicated for Child Pugh classes:", "B and C (Tx)", ["A only", "A and B", "None"])
q(381, S5, "MELD stands for:", "Model for end stage liver disease", ["Malignant end stage lung disease", "Metabolic end liver disorder", "Model for early lung disease"])
q(381, S5, "MELD score is used in:", "Adults", ["Children", "Neonates", "Animals"])
q(381, S5, "PELD stands for:", "Pediatric end stage liver disease", ["Adult end stage liver disease", "Pulmonary end stage disease", "Pancreatic end stage disease"])
q(381, S5, "Milan criteria are an indicator for transplantation in:", "Hepatocellular carcinoma", ["Cholangiocarcinoma", "Cirrhosis", "Biliary atresia"])
q(381, S5, "Milan criteria: single tumour <5 cm plus no mets indicates:", "Liver transplantation", ["No transplantation", "Only chemotherapy", "Only resection"])
q(381, S5, "Milan criteria: 1–3 tumours <3 cm plus no mets indicates:", "Liver transplantation", ["Palliative care only", "No surgery", "Only TACE"])

# ------------------------------------------------------------------ p382-383
S6 = "Liver Transplant: King Criteria, Types, Sequence and Complications"
q(382, S6, "King's college criteria are an indicator for treatment in:", "Acute liver failure", ["Chronic liver failure", "HCC", "Cirrhosis"])
q(382, S6, "Non-acetaminophen acute liver failure needs transplant if prothrombin time is:", ">100 s", [">50 sec", ">18 sec", ">10 s"])
q(382, S6, "Alternatively, any 3 of the listed criteria including:", "Non-A, non-B viral hepatitis", ["Hepatitis A", "Hepatitis E", "Alcoholic hepatitis"])
q(382, S6, "A King's criterion is jaundice to encephalopathy:", ">7 days", ["<7 days", ">7 hours", "<24 hours"])
q(382, S6, "A King's criterion is age:", "<10 years or >40 years", ["20–30 years", ">60 years only", "<5 years only"])
q(382, S6, "A King's criterion is prothrombin time:", ">50 sec", [">100 s", "<50 sec", ">18 sec"])
q(382, S6, "A King's criterion is serum bilirubin:", ">18 mg/dL", [">1.8 mg/dL", "<18 mg/dL", ">180 mg/dL"])
q(382, S6, "A type of liver transplant is:", "Dead donor", ["Xeno donor", "No donor", "Skin donor"])
q(382, S6, "A type of liver transplant is:", "Live donor", ["Dead donor only", "No donor", "Cadaver skin"])
q(382, S6, "Split and reduced liver transplant divides the liver into segments:", "IV to VIII & II, III", ["I to III & IV", "V to VI only", "No segments"])
q(382, S6, "Segments IV to VIII are transplanted to an:", "Adult", ["Child", "Infant", "Animal"])
q(382, S6, "Segments II, III are transplanted to a:", "Child", ["Adult", "Elderly", "Donor"])
q(382, S6, "Extended donor criteria for liver include:", "Advanced donor age", ["Young age", "No disease", "Ideal organs"])
q(382, S6, "Extended liver donor criteria include:", "Organ dysfunction", ["Normal organs", "No infection", "Young donor"])
q(382, S6, "Extended liver donor criteria include infections like:", "Hepatitis", ["UTI", "Pneumonia", "Skin infection"])
q(382, S6, "Auxiliary liver transplant is a piggy back transplant in:", "Fulminant liver failure", ["Chronic failure", "HCC", "Cirrhosis"])
q(382, S6, "In auxiliary transplant, the diseased liver is:", "Not removed", ["Removed", "Resected partially", "Biopsied only"])
q(382, S6, "Domino liver transplant transplants the liver of a patient with systemic disease to another patient, Eg:", "Amyloidosis, HIV", ["Cirrhosis, HCC", "Biliary atresia", "Hepatitis"])
q(382, S6, "In the paired exchange programme, donors A/B and recipients A'/B':", "Do not match one another", ["Match each other", "Need no matching", "Are identical twins"])
q(382, S6, "Hence in paired exchange, each donor:", "Matches the other, so transplant pair exchanged", ["Donates to self", "Is rejected", "Waits for a cadaver"])
q(383, S6, "First anastomosis in liver transplant sequence is the:", "Suprahepatic IVC", ["Infrahepatic IVC", "Portal vein", "Bile duct"])
q(383, S6, "Second in liver transplant sequence is the:", "Infrahepatic IVC", ["Suprahepatic IVC", "Hepatic artery", "Bile duct"])
q(383, S6, "Third in liver transplant sequence is the:", "Portal vein", ["Hepatic artery", "Bile duct", "Suprahepatic IVC"])
q(383, S6, "Fourth in liver transplant sequence is the:", "Hepatic artery", ["Portal vein", "Bile duct", "IVC"])
q(383, S6, "Vascular anastomoses in liver transplant use:", "Proline suture", ["PDS", "Vicryl", "Catgut"])
q(383, S6, "Fifth in liver transplant sequence is the:", "Bile duct", ["Portal vein", "Hepatic artery", "IVC"])
q(383, S6, "Bile duct anastomosis uses:", "PDS (monofilament absorbable sutures)", ["Proline", "Silk", "Steel"])
q(383, S6, "In liver transplant there is:", "No hyperacute rejection", ["Hyperacute rejection always", "Chronic rejection only", "No rejection at all"])
q(383, S6, "Acute liver rejection is:", "Reduced by effective immunosuppression", ["Increased by immunosuppression", "Untreatable", "Always fatal"])
q(383, S6, "The most common liver rejection is:", "Chronic", ["Hyperacute", "Acute", "No rejection"])
q(383, S6, "Chronic liver rejection occurs:", "After 6 months", ["On table", "Within a week", "Within a day"])
q(383, S6, "Biopsy of chronic liver rejection shows:", "Vanishing duct syndrome", ["Glomerular sclerosis", "Intravascular thrombosis", "Normal ducts"])
q(383, S6, "The most common vascular complication after liver transplant is:", "Hepatic artery thrombosis", ["Portal vein thrombosis", "IVC thrombosis", "Biliary stricture"])
q(383, S6, "Hepatic artery thrombosis presents as:", "Acute rejection/acute liver failure", ["Chronic rejection", "Bile leak only", "No symptoms"])
q(383, S6, "Hepatic artery thrombosis is managed with:", "Anticoagulants", ["Balloon dilatation", "Observation", "Steroids"])
q(383, S6, "Failure to respond in hepatic artery thrombosis needs:", "Re-transplantation", ["Only antibiotics", "Discharge", "No treatment"])
q(383, S6, "A biliary complication after liver transplant is:", "Biliary stricture", ["Bile duct dilatation", "Gallstones", "No complication"])
q(383, S6, "Recurrence of disease after liver transplant includes:", "Hepatitis B and C", ["Hepatitis A only", "No recurrence", "Malaria"])
q(383, S6, "Recurrent disease after liver transplant includes:", "1° biliary cholangitis", ["Acute appendicitis", "Pneumonia", "UTI"])
q(383, S6, "Recurrence after liver transplant includes:", "Sclerosing cholangitis", ["Sclerosing pancreatitis", "Normal ducts", "No disease"])
q(383, S6, "Recurrent disease includes:", "Autoimmune hepatitis", ["Alcoholic hepatitis", "Drug hepatitis only", "Ischemic hepatitis"])
q(383, S6, "Recurrence includes:", "Non-alcoholic fatty liver disease", ["Alcoholic liver only", "No fat", "Viral hepatitis only"])
q(383, S6, "Recurrent disease includes:", "Budd-chiari syndrome", ["Budd-chiari never recurs", "Portal hypertension only", "Splenomegaly only"])
q(383, S6, "Recurrence after liver transplant includes:", "Malignant tumours", ["No tumours", "Benign tumours only", "Cysts only"])
q(383, S6, "Infections, malignancy and PTLD after liver transplant are:", "Same as renal Tx", ["Never seen", "Different always", "Fatal always"])

# ------------------------------------------------------------------ p383-385
S7 = "Heart, Lung, Small Bowel Transplantation and GVHD"
q(383, S7, "A heart transplant criterion is:", "Impaired left ventricular systolic function", ["Normal LV function", "Right ventricular failure only", "Normal heart"])
q(383, S7, "Heart transplant needs NYHA class:", "III", ["I", "II", "IV only"])
q(383, S7, "Heart transplant patients are:", "Receiving optimal medical therapy", ["Drug naive", "Untreated", "On no drugs"])
q(383, S7, "Heart transplant criteria include resynchronisation pacing or:", "Implantable defibrillator device", ["Pacemaker removal", "No device", "Stent only"])
q(383, S7, "Heart transplant is for patients with:", "Poor prognosis", ["Good prognosis", "No symptoms", "Mild disease"])
q(384, S7, "First anastomosis in heart transplant sequence is the:", "Left atrium", ["Right atrium", "Pulmonary artery", "Aorta"])
q(384, S7, "Second in heart transplant sequence is the:", "Right atrium", ["Left atrium", "Aorta", "Pulmonary vein"])
q(384, S7, "Third in heart transplant sequence is the:", "Pulmonary artery", ["Aorta", "Left atrium", "Right atrium"])
q(384, S7, "Fourth in heart transplant sequence is the:", "Aorta", ["Pulmonary artery", "Left atrium", "IVC"])
q(384, S7, "Heart rejection is monitored by:", "Subendocardial biopsy through jugular route", ["Needle biopsy", "Endoscopic biopsy", "Open biopsy"])
q(384, S7, "Lung donor investigations need a:", "Clear chest radiograph", ["Abnormal radiograph", "CT only", "No imaging"])
q(384, S7, "Lung donors need negative gram stain of:", "Bronchial/purulent secretion", ["Blood", "Urine", "Sputum only"])
q(384, S7, "Lung donors need arterial O2 tension:", ">300 mmHg", ["<300 mmHg", ">100 mmHg", "<100 mmHg"])
q(384, S7, "Lung donor history: age:", "<55 yrs", [">55 yrs", "<18 yrs", ">70 yrs"])
q(384, S7, "Lung donor smoking history:", "<20 pack-years", [">20 pack-years", "Any smoking", "No limit"])
q(384, S7, "Lung donors must have no:", "Chest trauma, aspiration, pneumonia", ["Smoking history", "Any age limit", "O2 requirement"])
q(384, S7, "A disease requiring lung transplant is:", "B/L cystic fibrosis", ["Asthma", "Pneumonia", "TB"])
q(384, S7, "Lung transplant is needed for:", "Interstitial lung disease", ["COPD only", "Asthma", "Bronchitis"])
q(384, S7, "Lung transplant is indicated in:", "Emphysema/COPD", ["Pneumonia", "Pleurisy", "Pneumothorax"])
q(384, S7, "Lung transplant is needed for:", "Pulmonary hypertension", ["Systemic hypertension", "Hypotension", "Aortic stenosis"])
q(384, S7, "Pulmonary hypertension can need combined heart-lung transplantation if associated with:", "Congenital heart disease", ["Acquired disease", "No heart disease", "Coronary disease"])
q(384, S7, "First in lung transplant sequence: pulmonary vein with cuff of left atrium to:", "Left atrium of recipient", ["Right atrium", "Pulmonary artery", "Aorta"])
q(384, S7, "Lung transplant sequence includes:", "Bronchial anastomosis", ["Tracheal resection", "Lobectomy", "Pneumonectomy"])
q(384, S7, "Last in lung transplant sequence is the:", "Pulmonary artery", ["Pulmonary vein", "Bronchus", "Aorta"])
q(384, S7, "Small bowel transplant challenge is:", "Large lymphoid tissue", ["Small lymphoid tissue", "No lymphoid tissue", "Avascular tissue"])
q(384, S7, "Large lymphoid tissue increases the risk of:", "Rejection", ["Infection only", "Bleeding", "No risk"])
q(384, S7, "Small bowel transplant risks:", "Graft vs host reaction", ["No immune risk", "Only infection", "Only bleeding"])
q(384, S7, "Ischemia & rejection increase intestinal permeability and risk of:", "Bacterial infections", ["Viral infections", "Fungal infections", "No infections"])
q(384, S7, "Graft rejection and infection in small bowel transplant give:", "Poor outcomes", ["Good outcomes", "No effect", "Cure"])
q(384, S7, "Indication for small bowel transplant is short bowel syndrome requiring:", "Long term total parenteral nutrition (TPN)", ["Short term TPN", "No TPN", "Enteral feeds"])
q(384, S7, "Isolated small bowel transplant uses:", "Jejunum or ileum", ["Duodenum only", "Colon only", "Stomach"])
q(384, S7, "Combined small bowel + liver transplant is indicated for:", "Liver dysfunction d/t long term TPN", ["Normal liver", "Acute liver failure", "HCC"])
q(384, S7, "Multivisceral transplants are called:", "Cluster transplants", ["Split transplants", "Domino transplants", "Paired exchange"])
q(385, S7, "Early complications of small bowel transplant include:", "Vascular", ["Chronic rejection", "Hernias", "Thrombosis only"])
q(385, S7, "An early complication is:", "Anastomotic leaks", ["Chronic rejection", "Hernias", "Thrombosis"])
q(385, S7, "Early complications include:", "Abdominal collections", ["Late hernias", "Chronic rejection", "No collections"])
q(385, S7, "An early complication is:", "Pancreatitis", ["Hepatitis", "Cholecystitis", "Appendicitis"])
q(385, S7, "Early complications include:", "Renal impairment", ["Hepatic failure", "No renal issues", "Polyuria"])
q(385, S7, "Early complications include:", "Stomal complications", ["No stomal issues", "Late hernias", "Chronic rejection"])
q(385, S7, "Early complications include:", "Drug related", ["No drug effects", "Late effects", "Surgical only"])
q(385, S7, "Early complications include:", "GVHD", ["No immunity", "Late only", "Chronic only"])
q(385, S7, "Early complications include:", "PTLD", ["No tumours", "Late only", "Benign only"])
q(385, S7, "Late complications of small bowel transplant include:", "Thrombosis", ["Anastomotic leaks", "Abdominal collections", "Pancreatitis"])
q(385, S7, "A late complication is:", "Renal impairment", ["Acute rejection", "Anastomotic leak", "Pancreatitis"])
q(385, S7, "Late complications include:", "Hernias", ["Leaks", "Collections", "Stomal issues"])
q(385, S7, "A late complication is:", "Chronic rejection", ["Hyperacute rejection", "Acute rejection", "No rejection"])
q(385, S7, "Late complications include:", "PTLD", ["No tumours", "Benign polyps", "Skin cancer"])
q(385, S7, "1 year graft survival in small bowel transplant is:", "80%", ["70%", "90%", "50%"])
q(385, S7, "3 year survival in small bowel transplant is:", "70%", ["80%", "90%", "100%"])
q(385, S7, "Small bowel transplant has high incidence of:", "Lymphoproliferative disease (PTLD, Lymphomas)", ["No tumours", "Skin cancer", "Breast cancer"])
q(385, S7, "Graft vs host disease is active white cells in donor organs that:", "Attack immunocompromised recipient", ["Protect the recipient", "Attack the donor", "Cause no harm"])
q(385, S7, "GVHD is seen in:", "Small intestinal transplant", ["Kidney transplant", "Liver transplant", "Heart transplant"])
q(385, S7, "GVHD is also seen in:", "Bone marrow transplant", ["Corneal transplant", "Skin graft", "Heart valves"])
q(385, S7, "A clinical feature of GVHD is:", "Extensive rash", ["No rash", "Jaundice only", "Fever only"])
q(385, S7, "GI disturbances in GVHD include:", "Diarrhoea", ["Constipation", "Vomiting only", "No GI symptoms"])
q(385, S7, "GVHD causes:", "Protein losing enteropathy", ["Protein gain", "No enteropathy", "Malabsorption never"])
q(385, S7, "GVHD causes:", "Edema", ["Dehydration", "Weight loss only", "No swelling"])
q(385, S7, "GVHD causes:", "Liver dysfunction", ["Normal liver", "Renal failure", "Lung fibrosis"])

# ------------------------------------------------------------------ units
def first_page(title):
    return next(x["page"] for x in Q if x["sec"] == title)

UNIT_DEFS = [
    (S1, "Autografts stay within one person, isografts pass between identical twins, allografts within a species and xenografts across species, harvested from living or dead donors. Maastricht grades dead donors from uncontrolled dead-on-arrival and failed resuscitation yielding valves, corneas and kidneys, to controlled anticipated and brain-dead arrests plus uncontrolled in-hospital arrests that can give all organs except the heart."),
    (S2, "Cold UW solution at 4°C with hydroxyethyl starch, lactobionate, adenosine, allopurinol and reduced glutathione flushes through aorta and portal vein to block thrombosis, cut oxygen demand and swap in preservative. Cold tolerance runs kidney 36 hours longest through liver 12–18, pancreas <10–18, small bowel 4–6 and lung 3–8 down to heart 3–6 shortest, while normothermic machine perfusion of heart, lung, liver and kidney restores ATP ex-vivo for marginal donors and early function."),
    (S3, "Diabetic nephropathy leads adult renal indications and glomerulonephritis leads paediatric ones, extended by fit over-60 or over-50 donors with stroke death, hypertension or creatinine above 1.5, doubling marginal kidneys into one iliac fossa for nephron mass. Match ABO, Rh and HLA-A/B/DR with DR supreme plus KFT, favour the left kidney's long vein, park the graft heterotopically in the iliac fossa with dead-donor end-to-side external iliac or live-donor end-to-end internal iliac arterial joins in Proline, vein to external iliac vein and ureter to bladder in Vicryl/PDS; creatinine rises over 10% or 30 μmol/L flag rejection, calcineurin toxicity, dehydration, UTI, obstruction, vascular thrombosis or sepsis, with 90% live and 85% dead five-year survival improving through drugs and technique."),
    (S4, "Hyperacute on-table dusky anuric rejection comes from preformed HLA type-II antibody with intravascular thrombosis, acute disease splits into responsive T-cell and stubborn antibody arms, and chronic type-IV disease past six months with glomerular sclerosis is commonest, all graded by Banff on needle kidney/liver, endoscopic bowel or jugular subendocardial heart biopsies. Bacteria dominate month one and viruses led by CMV and BK dominate overall; skin SCC leads malignancy ahead of haematological and post-renal breast cancers, while EBV-driven B-cell PTLD mimics mononucleosis with fever and nodes, kills frequently and worsens with CNS spread."),
    (S5, "Post-renal vascular trouble is usually vein thrombosis with falling function fixed by anticoagulation versus gradual hypertensive arterial stenosis opened by balloon, both imaged by CT angiography. Diabetic nephropathy earns combined kidney-pancreas grafts monitored by insulin and amylase through bladder drainage until 3–4-year complications force conversion to better but harder-to-watch enteric drainage. Cirrhosis from hepatitis B/C and alcohol leads adult liver indications and extrahepatic biliary atresia leads paediatric ones without HLA worry or hyperacute rejection, scored by Child-Pugh A 5–6 against transplantable B 7–9 and C 10–15, adult MELD and paediatric PELD models, and Milan HCC limits of one sub-5-cm or up to three sub-3-cm tumours without mets."),
    (S6, "King's College lists acute-liver-failure transplant triggers of PT over 100 seconds or any three of non-A/B hepatitis, >7-day jaundice-encephalopathy gap, age under 10 or over 40, PT over 50 and bilirubin over 18. Livers come dead, live, split with IV–VIII to adults and II–III to children, or extended by age, dysfunction and hepatitis; piggy-back auxiliaries leave the native liver in fulminant failure, domino grafts recycle amyloid/HIV livers, and paired exchanges swap mismatched pairs. Sew supra- then infra-hepatic IVC, portal vein and hepatic artery in Proline before the PDS bile duct; expect no hyperacute, suppressible acute and dominant post-6-month chronic vanishing-duct rejection, hepatic-artery thrombosis with failure needing re-transplant plus strictures, recurrence of hepatitis, cholangitis, autoimmune, fatty, Budd-Chiari and malignant disease, and renal-like infection, malignancy and PTLD."),
    (S7, "Hearts go to NYHA-III medically-maxed poor-prognosis LV failure with resynchronisation or defibrillators, sewn left atrium, right atrium, pulmonary artery then aorta and watched by jugular subendocardial biopsy. Lungs need clear films, clean gram stains, PaO2 above 300, age under 55, under 20 pack-years and no trauma/aspiration/pneumonia for cystic fibrosis, interstitial disease, COPD/emphysema and pulmonary hypertension with congenital heart combos, joined vein-cuff to left atrium, bronchus then artery. Lymphoid-rich small bowel fights rejection, graft-versus-host and permeability-driven bacterial sepsis with poor rescue, serving TPN-dependent short bowel by isolated jejunal/ileal, liver-combined or multivisceral cluster grafts; early vascular, leak, collection, pancreatitis, renal, stomal, drug, GVHD and PTLD hazards mature into late thrombosis, renal, hernia, chronic rejection and PTLD with 80% one-year and 70% three-year survival plus lymphomas, while donor white cells attacking immunocompromised intestinal or marrow recipients produce rash, diarrhoea, protein-losing enteropathy, oedema and liver dysfunction."),
]

UNITS = []
for i, (title, guide) in enumerate(UNIT_DEFS, 1):
    UNITS.append({
        "id": f"SURG-U50-{i}",
        "ch": 50,
        "n": i,
        "title": title,
        "sec": f"{title} · p{first_page(title)}",
        "qs": [x["id"] for x in Q if x["sec"] == title],
        "guide": guide,
    })

covered = [x for u in UNITS for x in u["qs"]]
assert covered == [x["id"] for x in Q]
assert len(set(covered)) == len(covered)
with open("data/ch50.json", "w", encoding="utf-8") as f:
    json.dump({"questions": Q, "units": UNITS}, f, ensure_ascii=False, indent=1)
print(f"ch50: {len(Q)} questions, {len(UNITS)} units")
