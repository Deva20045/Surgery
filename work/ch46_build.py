#!/usr/bin/env python3
"""Build data/ch46.json — Bladder (Marrow Surgery Ed 8, pp353-359)."""
import json

Q = []

def q(page, sec, text, correct, wrongs, note=None):
    opts = [correct] + list(wrongs)
    assert len(opts) == 4
    Q.append({
        "id": f"SURG-C46-{len(Q)+1:03d}",
        "sec": sec,
        "page": page,
        "q": text,
        "opts": opts,
        "ans": 0,
        "exp": (note or correct) + f" (Book p{page})",
    })

# ------------------------------------------------------------------ p353
S1 = "Foley's Catheter"
q(353, S1, "French grading of a Foley's catheter is for:", "Outer circumference/diameter", ["Inner lumen length only", "Balloon volume only", "Irrigation flow rate only"])
q(353, S1, "One French equals:", "0.33 mm", ["1.0 mm", "3.3 mm", "0.033 cm only"])
q(353, S1, "A white Foley's catheter is size:", "12 French", ["14 French", "18 French", "20 French"])
q(353, S1, "A white (12 French) Foley's catheter measures:", "4 mm", ["4.7 mm", "5.3 mm", "6.7 mm"])
q(353, S1, "A green Foley's catheter is size:", "14 French", ["12 French", "16 French", "20 French"])
q(353, S1, "A green (14 French) Foley's catheter measures:", "4.7 mm", ["4 mm", "5.3 mm", "6 mm"])
q(353, S1, "An orange Foley's catheter is size:", "16 French", ["12 French", "14 French", "18 French"])
q(353, S1, "An orange (16 French) Foley's catheter measures:", "5.3 mm", ["4 mm", "4.7 mm", "6.7 mm"])
q(353, S1, "A red Foley's catheter is size:", "18 French", ["14 French", "16 French", "20 French"])
q(353, S1, "A red (18 French) Foley's catheter measures:", "6 mm", ["4 mm", "5.3 mm", "6.7 mm"])
q(353, S1, "A yellow Foley's catheter is size:", "20 French", ["12 French", "16 French", "18 French"])
q(353, S1, "A yellow (20 French) Foley's catheter measures:", "6.7 mm", ["4 mm", "4.7 mm", "6 mm"])
q(353, S1, "The Foley's catheter diagram labels the tip opening as the:", "Bladder opening", ["Urethral meatus", "Ureteric orifice", "Irrigation valve"])
q(353, S1, "The retaining structure near the tip of a Foley's catheter is the:", "Balloon", ["Metal stylet", "Ureteric stent", "Prostatic coil"])
q(353, S1, "The size marking on a Foley's catheter is given in:", "French scale and millimeters", ["Inches only", "Gauge and litres", "Centimetres of water only"])
q(353, S1, "One channel of a Foley's catheter is the:", "Urine drainage port", ["Arterial pressure port", "Bile drainage port", "Epidural port"])
q(353, S1, "Another channel of a Foley's catheter is the:", "Balloon port", ["Nasogastric port", "Central venous port", "Peritoneal port"])
q(353, S1, "The balloon port of a Foley's catheter is marked with the:", "Volume of fluid recommended to inflate the balloon", ["Patient's blood group", "Urine culture result", "French colour of the ureter"])
q(353, S1, "The third channel of a 3-way Foley's catheter is for:", "Irrigation to remove clots", ["Balloon deflation only", "Ureteric stenting", "Rectal suction"])
q(353, S1, "A 3-way Foley's catheter is shown with an extra channel for:", "Irrigation", ["Urethral dilatation", "Prostatic biopsy", "Bladder neck resection"])
q(353, S1, "A type of Foley's catheter listed is the:", "Rubber Foley's", ["Steel Foley's", "Glass Foley's", "Cotton Foley's"])
q(353, S1, "The duration of use of a rubber Foley's catheter is:", "25–30 days", ["3 months", "1 year", "7–10 days only"])
q(353, S1, "The other type of Foley's catheter listed is the:", "Silicone Foley's", ["Latex-core steel Foley's", "Paper Foley's", "Silver-chain Foley's"])
q(353, S1, "The duration of use of a silicone Foley's catheter is:", "3 months", ["25–30 days", "7–10 days", "24 hours only"])
q(353, S1, "Silicone Foley's catheters show decreased colonization and decreased:", "Crusting", ["Balloon capacity", "French size", "Urine output"])
q(353, S1, "A stuck Foley's during deflation is best managed by retracting the balloon with:", "USG guided balloon puncture", ["Blind forceful pulling", "Cutting the urethra", "Leaving it permanently"])

# ------------------------------------------------------------------ p353-354
S2 = "Urinary Retention"
q(353, S2, "A clinical feature of acute urinary retention is:", "Pain", ["Painless large lump only", "Jaundice", "Haemoptysis"])
q(353, S2, "Acute urinary retention presents with:", "Abdominal swelling", ["Scrotal transillumination", "Perineal ulcer", "Penile curvature"])
q(353, S2, "Dehydration in acute urinary retention is:", "Usually absent", ["Always severe", "Present with uraemia in every case", "Associated with deranged KFT in every case"])
q(353, S2, "The investigation finding in acute urinary retention is:", "KFT usually normal", ["KFT always deranged", "Uraemia in every case", "Hyperchloremic acidosis in every case"])
q(353, S2, "Management of acute urinary retention includes:", "Foley catheterisation/SPC (suprapubic catheterisation)", ["Immediate radical cystectomy", "Only oral antibiotics", "Observation without drainage"])
q(353, S2, "Along with drainage, acute urinary retention needs:", "Treatment of the underlying cause", ["No further treatment", "Only bladder irrigation forever", "Ureteric reimplantation in every case"])
q(353, S2, "A predisposing factor for chronic urinary retention is:", "Bladder outlet obstruction", ["Acute appendicitis", "Pneumothorax", "Inguinal hernia only"])
q(353, S2, "Chronic urinary retention is predisposed by:", "BPH", ["Acute orchitis", "Penile fracture", "Urethral condyloma only"])
q(354, S2, "A predisposing factor for chronic urinary retention is:", "Bladder neck stenosis", ["Bladder dome perforation only", "Urachal cyst", "Hutch diverticulum only"])
q(354, S2, "Chronic urinary retention may follow:", "Spinal injury", ["Nasal fracture", "Clavicle fracture", "Acute tonsillitis"])
q(354, S2, "A clinical feature of chronic urinary retention is:", "Inability to pass urine", ["Passage of large volumes hourly", "Painless jaundice", "Scrotal pain only"])
q(354, S2, "Chronic urinary retention presents with an:", "Abdominal lump", ["Acute tender groin lump", "Perianal abscess", "Breast lump"])
q(354, S2, "Pain in chronic urinary retention is:", "Relatively less", ["Always excruciating", "Absent in every case", "Referred to the shoulder"])
q(354, S2, "Lab findings in chronic urinary retention include:", "Deranged KFT", ["Normal KFT in every case", "Normal creatinine always", "Only anaemia"])
q(354, S2, "Uraemia in chronic urinary retention is:", "Present +/-", ["Never seen", "Always absent", "Seen only in acute retention"])
q(354, S2, "Management of chronic urinary retention is:", "Foley's catheterisation/SPC", ["Immediate nephrectomy", "Only antacids", "Radiotherapy"])
q(354, S2, "A complication of draining chronic urinary retention is:", "Post-obstructive diuresis", ["Post-obstructive jaundice", "Acute pancreatitis", "Tension pneumothorax"])
q(354, S2, "Post-obstructive diuresis is prevented by:", "Aggressive i/v hydration", ["Fluid restriction only", "Clamping the IV line", "Only oral vitamins"])
q(354, S2, "Haematuria after draining chronic retention is due to:", "Sudden decompression", ["A bladder tumour in every case", "A ureteric stone", "Cystitis cystica only"])
q(354, S2, "Haematuria due to sudden decompression is prevented by:", "Clamp/gradual release", ["Rapid complete drainage", "Aggressive IV hydration alone", "Immediate cystectomy"])

# ------------------------------------------------------------------ p354-355
S3 = "Bladder Trauma and Grading"
q(354, S3, "A type of bladder trauma is:", "Extraperitoneal rupture", ["Subcutaneous rupture", "Intrathoracic rupture", "Intracranial rupture"])
q(354, S3, "The most common type of bladder rupture is:", "Extraperitoneal", ["Intraperitoneal", "Combined thoracoabdominal", "Urethral only"])
q(354, S3, "The other type of bladder rupture is:", "Intraperitoneal", ["Extrapleural", "Subdural", "Retropharyngeal"])
q(354, S3, "Extraperitoneal bladder rupture is secondary to:", "Pelvic fracture", ["Rib fracture", "Skull fracture", "Humerus fracture"])
q(354, S3, "Extraperitoneal bladder rupture may have associated:", "Proximal urethral injury +/-", ["Distal penile injury in every case", "Renal artery injury in every case", "Ureteric avulsion in every case"])
q(354, S3, "A clinical feature of extraperitoneal bladder rupture is:", "Inability to pass urine", ["Polyuria", "Painless jaundice", "Haemoptysis"])
q(354, S3, "Blood at the tip of the meatus suggests:", "Extraperitoneal bladder rupture with urethral involvement", ["Acute appendicitis", "Cholecystitis", "Pneumonia"])
q(354, S3, "A clinical feature of extraperitoneal bladder rupture is:", "Deep perineal hematoma", ["Superficial leg hematoma", "Scalp hematoma", "Subconjunctival haemorrhage only"])
q(354, S3, "The investigation of choice in a stable patient with bladder rupture is:", "CT urography", ["Plain X-ray only", "HIDA scan", "Barium enema"])
q(354, S3, "An investigation listed for bladder rupture is:", "MCU", ["ECG", "EEG", "Spirometry"])
q(354, S3, "An investigation listed for bladder rupture is:", "RGU", ["HIDA scan", "PET-CT only", "Mammography"])
q(354, S3, "The CT image of extraperitoneal bladder rupture shows:", "Extraperitoneal extravasation of urine", ["Spilled dye outlining the bowel", "A normal bladder", "A ureterocele"])
q(354, S3, "Management of extraperitoneal bladder rupture is:", "Foley's catheter/SPC x 7–10 days", ["Immediate laparotomy in every case", "Bladder repair in 2 layers in every case", "Only antibiotics"])
q(354, S3, "Intraperitoneal bladder rupture occurs with:", "Full bladder with lower abdominal injury", ["Empty bladder with head injury", "Pelvic fracture in every case", "Chest trauma only"])
q(354, S3, "A surgical cause of intraperitoneal bladder rupture is:", "Hysterectomy", ["Circumcision", "Hydrocelectomy", "Thyroidectomy"])
q(354, S3, "Intraperitoneal bladder rupture may follow:", "Cancer surgeries", ["Cataract surgery", "Dental extraction", "Skin biopsy"])
q(355, S3, "The post-void image of intraperitoneal bladder rupture shows:", "Spilled dye outlining the bowel", ["Extraperitoneal extravasation only", "A normal cystogram", "A drooping lily sign"])
q(355, S3, "A clinical feature of intraperitoneal bladder rupture is:", "Syncopal attack", ["Deep perineal hematoma only", "Blood at meatus in every case", "Scrotal swelling only"])
q(355, S3, "Intraperitoneal bladder rupture causes:", "Peritonitis", ["Pericarditis", "Meningitis", "Cellulitis of the leg"])
q(355, S3, "Investigation of choice in a stable patient with intraperitoneal rupture is:", "CT urography", ["USG Doppler only", "Plain radiograph only", "Arterial blood gas only"])
q(355, S3, "Management of intraperitoneal bladder rupture is:", "Explorative laparotomy with bladder repair in 2 layers + Foley's catheterisation/SPC", ["Foley's catheter alone in every case", "Only SPC without repair", "Observation without surgery"])
q(355, S3, "Grade I bladder injury with haematoma is described as:", "Contusion, intramural haematoma", ["Extraperitoneal laceration <2 cm", "Intraperitoneal laceration ≥2 cm", "Laceration into the trigone"])
q(355, S3, "Grade I bladder injury with laceration is:", "Partial thickness", ["Full thickness intraperitoneal ≥2 cm", "Bladder neck involvement", "Ureteral orifice involvement"])
q(355, S3, "Grade II bladder injury is:", "Extraperitoneal bladder wall laceration <2 cm", ["Extraperitoneal laceration ≥2 cm", "Intraperitoneal laceration ≥2 cm", "Contusion only"])
q(355, S3, "Grade III bladder injury is:", "Extraperitoneal ≥2 cm or intraperitoneal <2 cm bladder wall laceration", ["Intraperitoneal laceration ≥2 cm", "Contusion only", "Partial thickness only"])
q(355, S3, "Grade IV bladder injury is:", "Intraperitoneal bladder wall laceration ≥2 cm", ["Extraperitoneal laceration <2 cm", "Contusion only", "Partial thickness only"])
q(355, S3, "Grade V bladder injury is laceration extending into the:", "Bladder neck or ureteral orifice (Trigone)", ["Bladder dome only", "Urachus only", "Anterior abdominal wall only"])

# ------------------------------------------------------------------ p355-356
S4 = "Bladder Diverticulum"
q(355, S4, "Bladder diverticulum is:", "Outpouching of bladder", ["Inward growth of prostate", "Rupture of the urethra", "Stone in the bladder neck"])
q(355, S4, "A type of bladder diverticulum is:", "Primary congenital", ["Primary malignant", "Traumatic intraperitoneal", "Metastatic"])
q(355, S4, "Primary congenital diverticulum is:", "Herniation of mucosa", ["Herniation of full-thickness detrusor in every case", "A pulsion diverticulum", "Secondary to outlet obstruction"])
q(355, S4, "The defect in primary congenital diverticulum is a congenital muscular defect between the intravesical ureter and the:", "Root of ureteral hiatus", ["Bladder dome", "Urachus", "External meatus"])
q(355, S4, "Primary congenital bladder diverticulum is called:", "Hutch diverticulum", ["Meckel diverticulum", "Zenker diverticulum", "Calot diverticulum"])
q(355, S4, "Primary bladder diverticulum may be associated with:", "VUR +/- (vesico ureteric reflux)", ["Ureterocele in every case", "Bladder exstrophy in every case", "Posterior urethral valves in every case"])
q(355, S4, "Secondary bladder diverticulum is a:", "Pulsion diverticulum", ["Traction diverticulum", "Malignant diverticulum", "Congenital mucosal hernia"])
q(355, S4, "Secondary diverticulum is due to:", "Increased pressure", ["Decreased pressure", "Normal pressure in every case", "Negative pressure"])
q(355, S4, "A cause of secondary bladder diverticulum is:", "Bladder outlet obstruction", ["Bladder dome perforation", "Urachal patency", "Renal agenesis"])
q(355, S4, "Secondary bladder diverticulum may be secondary to:", "BPH", ["Acute prostatitis only", "Testicular torsion", "Epididymitis"])
q(355, S4, "A cause of secondary bladder diverticulum is:", "Urethral stricture", ["Urethral duplication", "Hypospadias only", "Phimosis only"])
q(355, S4, "Secondary bladder diverticulum may follow:", "Bladder neck stenosis", ["Bladder neck hypermobility only", "Ureteric reflux alone", "Renal ptosis"])
q(355, S4, "A clinical feature of bladder diverticulum is:", "Recurrent UTI", ["Recurrent pneumonia", "Recurrent jaundice", "Recurrent epistaxis"])
q(355, S4, "VUR in bladder diverticulum leads to:", "Upper urinary tract infections", ["Lower lobe pneumonia", "Acute cholecystitis", "Acute appendicitis"])
q(355, S4, "On changing posture, bladder diverticulum causes:", "Sudden, repeated urge to pass urine", ["Sudden faecal urge", "Shoulder pain", "Chest pain"])
q(356, S4, "The investigation of choice for bladder diverticulum is:", "CT urography", ["HIDA scan", "Barium meal", "Plain skull radiograph"])
q(356, S4, "Symptomatic and large bladder diverticula are treated with:", "Diverticulectomy + treat the cause", ["Only antibiotics forever", "Radical cystectomy in every case", "Ureteric reimplantation alone"])

# ------------------------------------------------------------------ p356
S5 = "Bladder Cancer: Types, Risk Factors and Clinical Features"
q(356, S5, "A type of bladder cancer is:", "Transitional cell carcinoma", ["Basal cell carcinoma", "Hepatocellular carcinoma", "Nasopharyngeal carcinoma"])
q(356, S5, "The most common type of bladder cancer is:", "Transitional cell carcinoma", ["Squamous cell carcinoma", "Adenocarcinoma", "Small cell carcinoma"])
q(356, S5, "A type of bladder cancer is:", "Squamous cell carcinoma", ["Transitional papilloma only", "Renal oncocytoma", "Seminoma"])
q(356, S5, "A type of bladder cancer is:", "Adenocarcinoma", ["Squamous papilloma only", "Pheochromocytoma", "Liposarcoma"])
q(356, S5, "A risk factor for transitional cell carcinoma is:", "Cigarette smoking", ["Schistosomiasis only", "Persistent urachus only", "African residence only"])
q(356, S5, "Chemicals causing transitional cell carcinoma include:", "Aniline dye, rubber", ["Asbestos only", "Silica only", "Coal dust only"])
q(356, S5, "A drug risk factor for transitional cell carcinoma is:", "Cyclophosphamide", ["Paracetamol", "Metformin", "Aspirin"])
q(356, S5, "Squamous cell carcinoma of the bladder is commonly seen in:", "Africa", ["Japan only", "Scandinavia only", "Australia only"])
q(356, S5, "A risk factor for squamous cell carcinoma of the bladder is:", "Smoking", ["Aniline dye only", "Persistent urachus only", "Cyclophosphamide only"])
q(356, S5, "Squamous cell carcinoma of the bladder is associated with:", "Schistosomiasis (Bilharziasis)", ["Filariasis", "Ascariasis", "Amoebiasis"])
q(356, S5, "The site of bladder adenocarcinoma is the:", "Trigone", ["Dome only", "Bladder neck only", "Urachus only"])
q(356, S5, "Adenocarcinoma of the bladder is associated with:", "Persistent urachus", ["Aniline dye", "Schistosomiasis", "Cigarette only"])
q(356, S5, "The most common clinical feature of bladder cancer is:", "Gross painless haematuria", ["Painful microscopic haematuria only", "Painless jaundice", "Haemoptysis"])
q(356, S5, "Lymph node metastasis in bladder cancer goes to the:", "Obturator LN", ["Inguinal LN only", "Cervical LN only", "Axillary LN only"])
q(356, S5, "Distant metastasis in bladder cancer goes to the:", "Bones", ["Lungs only", "Liver only", "Brain only"])
q(356, S5, "Cystoscopy in bladder cancer shows a:", "Papillary growth", ["Flat normal mucosa in every case", "Ureterocele", "Bladder stone only"])

# ------------------------------------------------------------------ p356-357
S6 = "Bladder Cancer: Investigations and Staging"
q(356, S6, "Urine routine microscopy and cytology in bladder cancer has:", "Decreased sensitivity", ["100% sensitivity", "No role", "Increased specificity in every case"])
q(356, S6, "An investigation in bladder cancer workup is:", "Urine culture and sensitivity", ["Stool culture", "Blood culture only", "Sputum cytology"])
q(356, S6, "USG KUB in bladder cancer looks for:", "Growth", ["Gallstones", "Liver cysts", "Splenic size only"])
q(356, S6, "USG KUB in bladder cancer looks for:", "Clots", ["Bowel gas only", "Pancreatic mass", "Aortic aneurysm"])
q(356, S6, "USG KUB in bladder cancer assesses the:", "Status of upper tracts", ["Status of coronary arteries", "Status of lungs", "Status of brain"])
q(356, S6, "The investigation of choice for bladder cancer is:", "Cystoscopic biopsy", ["USG KUB only", "Urine cytology only", "MRI only"])
q(356, S6, "Cystoscopic biopsy includes removing the lesion plus:", "Cold cup biopsy of base", ["Hot snare of ureter", "Laser of prostate", "Biopsy of rectum"])
q(356, S6, "Histopathology and MRI in bladder cancer determine the:", "Depth of invasion", ["Urine pH", "Serum PSA", "Bladder capacity only"])
q(357, S6, "Bladder cancer staging used is:", "pTNM (P = Pathological)", ["cTNM clinical only", "Dukes staging", "Robson staging"])
q(357, S6, "Tx bladder cancer means:", "Primary tumor cannot be assessed", ["No evidence of primary tumor", "Noninvasive papillary carcinoma", "Invasion of pelvic wall"])
q(357, S6, "T0 bladder cancer means:", "No evidence of primary tumor", ["Primary tumor cannot be assessed", "Carcinoma in situ", "Invasion of perivesical tissue"])
q(357, S6, "Ta bladder cancer is:", "Noninvasive papillary carcinoma", ["Carcinoma in situ", "Invasion of lamina propria", "Invasion of deep muscle"])
q(357, S6, "Tis bladder cancer is:", "Carcinoma in situ", ["Noninvasive papillary carcinoma", "Invasion of superficial muscle", "Invasion of prostate"])
q(357, S6, "T1 bladder cancer invades the:", "Subepithelial connective tissue (Lamina propria)", ["Muscularis propria", "Perivesical tissue", "Pelvic wall"])
q(357, S6, "T2 bladder cancer invades the:", "Muscularis propria bladder wall", ["Lamina propria only", "Perivesical fat only", "Abdominal wall"])
q(357, S6, "T2a bladder cancer invades:", "Superficial muscle (Inner half)", ["Deep muscle outer half", "Perivesical tissue microscopically", "Prostate"])
q(357, S6, "T2b bladder cancer invades:", "Deep muscle (Outer half)", ["Superficial inner half only", "Lamina propria only", "Urethra only"])
q(357, S6, "T3 bladder cancer invades the:", "Perivesical tissue", ["Lamina propria", "Inner half muscle only", "Pelvic wall"])
q(357, S6, "T3a bladder cancer is invasion:", "Microscopically", ["Macroscopically with extravesical mass", "Of the prostate", "Of the pelvic wall"])
q(357, S6, "T3b bladder cancer is invasion:", "Macroscopically (Extravesical mass)", ["Microscopically only", "Limited to lamina propria", "Of the abdominal wall"])
q(357, S6, "T4 bladder cancer invades:", "Adjacent structures", ["Only lamina propria", "Only inner-half muscle", "Only perivesical fat"])
q(357, S6, "T4a bladder cancer invades the:", "Prostate, uterus, or vagina", ["Pelvic wall", "Abdominal wall", "Bones"])
q(357, S6, "T4b bladder cancer invades the:", "Pelvic wall or abdominal wall", ["Prostate only", "Lamina propria", "Inner-half muscle"])
q(357, S6, "Non muscle invasive tumors include:", "Ta, Tis and T1", ["T2a and T2b", "T3 and T4", "T4a and T4b"])

# ------------------------------------------------------------------ p357-358
S7 = "Bladder Cancer: Management, Monitoring and Surgery"
q(357, S7, "Non muscle invasive bladder tumors are first treated with:", "TURBT (Transurethral resection of bladder tumor)", ["Radical cystectomy upfront", "Nephrectomy", "Prostatectomy"])
q(357, S7, "After TURBT, further management is based on the:", "Pathological state", ["Patient's age only", "Urine pH only", "Serum creatinine only"])
q(357, S7, "Non invasive papillary tumor is managed with:", "Observation or single cycle of intravesical chemotherapy", ["6 cycles of BCG in every case", "Radical cystectomy in every case", "Neoadjuvant chemotherapy"])
q(357, S7, "An intravesical chemotherapy drug listed is:", "Thiopeta", ["Cisplatin IV only", "Sorafenib", "Imatinib"])
q(357, S7, "An intravesical chemotherapy drug listed is:", "Mitomycin C", ["Doxycycline", "Amphotericin", "Penicillin"])
q(357, S7, "An intravesical chemotherapy drug listed is:", "Adriamycin", ["Streptomycin", "Gentamicin", "Ciprofloxacin"])
q(357, S7, "In situ cancer and lamina propria disease get:", "6 cycles of intravesical BCG (Immunotherapy)", ["Single cycle chemotherapy only", "Observation only", "Immediate cystectomy"])
q(357, S7, "If intravesical BCG is not tolerated, give:", "Intravesical chemotherapy", ["No further treatment", "Only radiotherapy", "Nephrectomy"])
q(357, S7, "A complication of intravesical BCG is:", "Hematuria", ["Jaundice", "Pancreatitis", "Pneumonia"])
q(357, S7, "Intravesical BCG may cause:", "TB", ["Malaria", "Filariasis", "Typhoid"])
q(357, S7, "A complication of intravesical BCG is:", "Granulomatous cystitis", ["Interstitial nephritis only", "Acute appendicitis", "Ulcerative colitis"])
q(357, S7, "Field cancerisation means:", "Mucosa at risk of Ca + multiple cancers", ["Single localized polyp only", "Distant metastasis only", "Benign hyperplasia only"])
q(357, S7, "Field cancerisation is positive in:", "Oral cavity", ["Liver only", "Spleen only", "Kidney only"])
q(357, S7, "Field cancerisation is positive in the:", "Bladder", ["Heart", "Lung only", "Pancreas only"])
q(357, S7, "Field cancerisation is positive in:", "Colorectal cancer", ["Gastric ulcer only", "Duodenal atresia", "Acute appendicitis"])
q(357, S7, "Monitoring after treatment is with check cystoscopies:", "Every 3 months", ["Every 3 years", "Once in a lifetime", "Only if haematuria recurs"])
q(357, S7, "The urinary marker to detect recurrence is:", "NMP-22 (Nuclear matrix protein)", ["PSA", "AFP", "CA 19-9"])
q(357, S7, "T2 muscle invasive tumor is treated with:", "Upfront surgery", ["Neoadjuvant chemotherapy first", "Only BCG", "Only observation"])
q(357, S7, "T3, T4 tumors are treated with:", "Neo adjuvant chemo", ["Upfront surgery only", "Single-cycle BCG", "Observation"])
q(357, S7, "If good response to neoadjuvant chemo, then:", "Surgery + Radiotherapy", ["Only observation", "Only BCG", "Ureteric stenting only"])
q(358, S7, "An indication for partial cystectomy is:", "Small tumors", ["Large multicentric tumors", "Trigone involvement in every case", "Distant metastasis"])
q(358, S7, "Partial cystectomy is indicated for carcinoma on the:", "Dome of bladder", ["Trigone", "Bladder neck", "Ureteric orifice"])
q(358, S7, "Partial cystectomy needs carcinoma:", "Away from ureteric orifice", ["Involving the ureteric orifice", "Involving the trigone", "With nodal metastasis"])
q(358, S7, "Radical cystectomy removes the:", "Bladder", ["Kidney", "Prostate only", "Urethra only"])
q(358, S7, "In males, radical cystectomy also removes the:", "Prostate", ["Testis", "Penis", "Scrotum"])
q(358, S7, "In females, radical cystectomy removes the:", "Urethra ± uterus", ["Ovaries in every case", "Vagina in every case", "Kidneys"])
q(358, S7, "Radical cystectomy includes removal of:", "Iliac + Obturator LN", ["Inguinal LN only", "Cervical LN", "Axillary LN"])
q(358, S7, "T1, multicentric, Grade 3 tumors progress to muscle invasive in:", "40%", ["4%", "90%", "100%"])
q(358, S7, "Hence T1 multicentric Grade 3 tumors need:", "Surgery", ["Only observation", "Only single-cycle chemo", "Only BCG forever"])

# ------------------------------------------------------------------ p358
S8 = "Urinary Diversion and Prognosis"
q(358, S8, "Urinary diversion means:", "Divert ureter post cystectomy", ["Divert bile post cholecystectomy", "Divert bowel post colectomy", "Divert urethra post circumcision"])
q(358, S8, "A type of urinary diversion is:", "Non continent urinary diversion", [" continent ileal conduit only", "No diversion", "Urethral diversion only"])
q(358, S8, "The other type of urinary diversion is:", "Continent urinary diversion", ["Non continent only", "Cutaneous only", "Rectal only"])
q(358, S8, "A non continent urinary diversion is:", "Uretero sigmoid anastomosis (Obsolete)", ["Neo-bladder using ileum", "Ileal conduit only", "Orthotopic bladder only"])
q(358, S8, "A complication of uretero sigmoid anastomosis is:", "Increased risk of UTI", ["Decreased risk of UTI", "No infection risk", "Only pneumonia"])
q(358, S8, "Uretero sigmoid anastomosis causes:", "Hyperchloremic, hypokalemic metabolic acidosis", ["Hyperkalemic metabolic alkalosis", "Respiratory acidosis only", "Normal electrolytes always"])
q(358, S8, "Uretero sigmoid anastomosis carries:", "100x risk of adenocarcinoma", ["No cancer risk", "100x risk of SCC only", "Protection from cancer"])
q(358, S8, "The most common urinary diversion is the:", "Ileal conduit (m/c)", ["Uretero sigmoid anastomosis", "Neo-bladder", "Cutaneous ureterostomy"])
q(358, S8, "A complication of ileal conduit is:", "Hyperchloremic, hypokalemic metabolic acidosis", ["Hypochloremic alkalosis", "Respiratory alkalosis", "Normal ABG always"])
q(358, S8, "Ileal conduit may complicate with:", "Stenosis", ["Fistula healing in every case", "No complications", "Only diarrhoea"])
q(358, S8, "Ileal conduit may complicate with:", "Stricture", ["Complete resolution always", "Only polyuria", "Only haematuria"])
q(358, S8, "Ileal conduit may complicate with:", "Recurrence", ["Cure in every case", "Only stone formation", "Only weight gain"])
q(358, S8, "Continent urinary diversion is a:", "Neo-bladder using ileum", ["Uretero sigmoid anastomosis", "Ileal conduit", "Nephrostomy"])
q(358, S8, "The most important prognostic factor in bladder cancer is:", "Depth of invasion/T-stage", ["Patient's age", "Urine pH", "Serum PSA"])

# ------------------------------------------------------------------ p359
S9 = "Urachal Abnormalities"
q(359, S9, "The urachus connects the:", "Bladder to umbilicus", ["Kidney to bladder", "Ureter to urethra", "Prostate to testis"])
q(359, S9, "Normal urachus is labelled in the diagram as:", "A Normal", ["B Patent urachus", "C Urachal cyst", "E Urachal diverticulum"])
q(359, S9, "Complete patency of the urachus is:", "Patent urachus", ["Urachal cyst", "Urachal sinus", "Urachal diverticulum"])
q(359, S9, "When a small portion does not obliterate, it forms a:", "Urachal cyst", ["Patent urachus", "Urachal sinus", "Urachal diverticulum"])
q(359, S9, "When the umbilical part does not obliterate, it forms a:", "Urachal sinus", ["Urachal cyst", "Patent urachus", "Urachal diverticulum"])
q(359, S9, "When the bladder part does not obliterate, it forms a:", "Urachal diverticulum", ["Urachal cyst", "Urachal sinus", "Patent urachus"])
q(359, S9, "Patent urachus presents with:", "Urine leak from umbilicus on straining/crying", ["Stool from umbilicus", "Bile from umbilicus", "Blood from umbilicus only"])
q(359, S9, "Urachal sinus presents with:", "Discharge from umbilicus", ["Discharge from urethra only", "Haematuria only", "Pneumaturia only"])
q(359, S9, "Urachal sinus is:", "Prone to infections", ["Never infected", "Protective against infection", "Malignant in every case"])
q(359, S9, "Management of urachal abnormalities is:", "Excision", ["Only antibiotics", "Only observation", "Radical cystectomy in every case"])
q(359, S9, "A complication of urachal abnormalities is risk of:", "Adenocarcinoma", ["Transitional cell carcinoma only", "Squamous papilloma", "Renal cell carcinoma"])

# ------------------------------------------------------------------ units
def first_page(title):
    return next(x["page"] for x in Q if x["sec"] == title)

UNIT_DEFS = [
    (S1, "French sizing measures outer circumference where 1 French is 0.33 mm, running white 12/4 mm through green 14/4.7, orange 16/5.3, red 18/6 to yellow 20/6.7. Know the drainage, balloon and marked inflation-volume ports plus the irrigation channel of a 3-way catheter, rubber wear for 25–30 days versus silicone for 3 months with less colonization and crusting, and USG-guided balloon puncture for a stuck catheter."),
    (S2, "Acute retention is painful with swelling, absent dehydration and normal KFT, relieved by Foley/SPC plus cause treatment. Chronic retention follows outlet obstruction, BPH, neck stenosis or spinal injury with painless lump, deranged KFT and uraemia, drained by Foley/SPC while guarding against post-obstructive diuresis with aggressive IV fluids and decompression haematuria with clamp/gradual release."),
    (S3, "Extraperitoneal rupture is commonest, follows pelvic fracture with possible proximal urethral injury, and shows inability to void, meatal blood and deep perineal haematoma managed by 7–10 days of Foley/SPC. Intraperitoneal rupture follows a full-bladder blow or hysterectomy/cancer surgery with syncope and peritonitis needing two-layer laparotomy repair; CT urography is the stable-patient test and grading runs contusion through <2 cm, ≥2 cm and trigonal grade V tears."),
    (S4, "A diverticulum is a bladder outpouching: primary Hutch lesions herniate mucosa through the muscular defect between intravesical ureter and ureteral hiatus with possible VUR, while secondary pulsion lesions arise from high pressure due to obstruction, BPH, stricture or neck stenosis. Recurrent UTI, ascending infection and posture-triggered repeated urge suggest it; CT urography confirms and large symptomatic lesions need diverticulectomy plus cause treatment."),
    (S5, "Transitional cell carcinoma dominates bladder cancer, with squamous and trigonal adenocarcinoma behind it. Cigarettes, aniline/rubber chemicals and cyclophosphamide drive TCC; African endemicity, smoking and bilharzial schistosomiasis drive SCC; persistent urachus drives adenocarcinoma. Gross painless haematuria is the classic clue, obturator nodes take lymph spread, bones take distant spread, and cystoscopy shows papillary growth."),
    (S6, "Work up runs urine microscopy/cytology with low sensitivity, culture, USG KUB for growth, clots and upper tracts, then cystoscopic biopsy as the investigation of choice with cold-cup base sampling while histology plus MRI fix depth. Stage pathologically from Tx/T0 through Ta papillary, Tis in situ and T1 lamina propria as non-muscle-invasive, then T2 inner/outer muscle, T3 micro/macro perivesical and T4 prostate/uterus/vagina versus pelvic/abdominal wall disease."),
    (S7, "Non-muscle-invasive disease starts with TURBT, then observation or single-cycle thiopeta/mitomycin/adriamycin for papillary lesions and six BCG immunotherapy cycles for in-situ/lamina disease, switching to chemotherapy if BCG with its haematuria, TB and granulomatous cystitis is intolerable. Field cancerisation links oral, bladder and colorectal sites; survey with 3-monthly cystoscopy and NMP-22. T2 goes straight to surgery while T3/T4 take neoadjuvant chemo then surgery plus radiotherapy, choosing dome partial versus radical cystectomy with iliac/obturator clearance, and operating T1 multicentric grade-3 lesions because 40% invade muscle."),
    (S8, "After cystectomy the ureters must be diverted, either non-continent through the obsolete ureterosigmoid route or the common ileal conduit, or continent through an ileal neobladder. Both conduit routes risk hyperchloraemic hypokalaemic acidosis, with added UTI and 100-fold adenocarcinoma risk after ureterosigmoid diversion and stenosis, stricture and recurrence after ileal conduit; depth of invasion/T-stage remains the key prognostic factor."),
    (S9, "The urachus joins bladder to umbilicus, persisting as patent urachus, mid-portion cyst, umbilical sinus or bladder diverticulum according to the unobliterated segment. Patent lesions leak urine on straining or crying while sinuses discharge and infect repeatedly; excision is curative and removes the adenocarcinoma risk."),
]

UNITS = []
for i, (title, guide) in enumerate(UNIT_DEFS, 1):
    UNITS.append({
        "id": f"SURG-U46-{i}",
        "ch": 46,
        "n": i,
        "title": title,
        "sec": f"{title} · p{first_page(title)}",
        "qs": [x["id"] for x in Q if x["sec"] == title],
        "guide": guide,
    })

covered = [x for u in UNITS for x in u["qs"]]
assert covered == [x["id"] for x in Q]
assert len(set(covered)) == len(covered)
with open("data/ch46.json", "w", encoding="utf-8") as f:
    json.dump({"questions": Q, "units": UNITS}, f, ensure_ascii=False, indent=1)
print(f"ch46: {len(Q)} questions, {len(UNITS)} units")
