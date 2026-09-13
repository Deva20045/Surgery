#!/usr/bin/env python3
"""Build data/ch4.json for PULSE Surgery ch4 (Post-operative Fever and Wound Infection, book p18-24)."""
import json

Q = []
def q(page, sec, text, opts, ans, exp):
    Q.append({"id": f"SURG-C4-{len(Q)+1:03d}", "sec": sec, "page": page,
              "q": text, "opts": opts, "ans": ans, "exp": exp})

# ---------------- p18 · FEVER CAUSES ----------------
q(18, "Fever Causes", "The most common cause of post-operative fever on POD 1 is:",
  ["Pneumonia", "Atelectasis", "UTI", "Wound infection"], 1,
  "POD 1: Atelectasis (m/c on POD 1). (Book p18)")
q(18, "Fever Causes", "Causes of fever on POD 2-3 include all of the following EXCEPT:",
  ["Pneumonia", "Superficial thrombophlebitis", "UTI", "Burst abdomen"], 3,
  "POD 2-3: Pneumonia, Superficial thrombophlebitis, UTI. (Book p18)")
q(18, "Fever Causes", "UTI is described as the:",
  ["m/c cause of post-op fever on POD 1", "m/c cause of hospital acquired infections", "m/c cause of burst abdomen", "m/c indication for laparotomy"], 1,
  "POD 2-3: UTI (m/c cause of hospital acquired infections). (Book p18)")
q(18, "Fever Causes", "Fever on POD 4-5 is caused by:",
  ["Atelectasis", "Pneumonia", "Surgical site infection / DVT", "Burst abdomen"], 2,
  "POD 4-5: Surgical site infections (SSI)/wound infection; Deep vein thrombosis. (Book p18)")
q(18, "Fever Causes", "Fever with wound dehiscence on POD 6 suggests:",
  ["Atelectasis", "UTI", "Pneumonia", "Burst abdomen / Abdominal wound dehiscence"], 3,
  "POD 6: Burst abdomen/Abdominal wound dehiscence. (Book p18)")
q(18, "Fever Causes", "Fever on POD 7 and beyond is caused by:",
  ["Atelectasis", "Superficial thrombophlebitis", "Pneumonia", "Intra-abdominal wound infection / collections"], 3,
  "POD 7 & beyond: Intra-abdominal wound infection/collections. (Book p18)")
q(18, "Fever Causes", "A patient spikes fever on the first post-operative day. The most likely cause is:",
  ["Wound infection", "Atelectasis", "DVT", "Intra-abdominal abscess"], 1,
  "Atelectasis: m/c cause of post op fever on day 1. (Book p18)")
q(18, "Fever Causes", "Deep vein thrombosis presents as post-operative fever on:",
  ["POD 1", "POD 2-3", "POD 4-5", "POD 7 and beyond"], 2,
  "POD 4-5: SSI/wound infection; Deep vein thrombosis. (Book p18)")

# ---------------- p18 · PNEUMONIA / THROMBOPHLEBITIS / ATELECTASIS ----------------
q(18, "Pneumonia", "The clinical feature of post-operative pneumonia is:",
  ["Pain", "Fever", "Swelling", "Cough with haemoptysis"], 1,
  "Pneumonia: Clinical features: Fever; Rx: Antibiotics. (Book p18)")
q(18, "Pneumonia", "The treatment of post-operative pneumonia is:",
  ["Topical heparinoids", "Antibiotics", "Incentive spirometry alone", "Anticoagulation"], 1,
  "Pneumonia: Rx: Antibiotics. (Book p18)")
q(18, "Thrombophlebitis", "Superficial thrombophlebitis presents with:",
  ["Fever only", "Pain and fever", "Swelling only", "Dyspnea"], 1,
  "Superficial thrombophlebitis: Clinical features: Pain, fever; Rx: Topical heparinoids. (Book p18)")
q(18, "Thrombophlebitis", "The treatment of superficial thrombophlebitis is:",
  ["Antibiotics", "Topical heparinoids", "Anticoagulation", "Surgical excision"], 1,
  "Superficial thrombophlebitis: Rx: Topical heparinoids. (Book p18)")
q(18, "Atelectasis", "Atelectasis is:",
  ["Collection of pus", "Collapse of alveoli", "Clot in deep veins", "Lung malignancy"], 1,
  "Atelectasis: Collapse of alveoli; m/c cause of post op fever on day 1. (Book p18)")
q(18, "Atelectasis", "Atelectasis is the most common cause of post-operative fever on:",
  ["Day 1", "Day 4-5", "Day 6", "Day 7 and beyond"], 0,
  "Atelectasis: m/c cause of post op fever on day 1. (Book p18)")
q(18, "Atelectasis", "Chest physiotherapy to prevent atelectasis uses the:",
  ["Nebulizer", "Incentive spirometer", "Oxygen mask", "Ventilator"], 1,
  "Atelectasis Prevention: Chest physiotherapy: Incentive spirometer. (Book p18)")
q(18, "Atelectasis", "Prevention of atelectasis includes all of the following EXCEPT:",
  ["Chest physiotherapy with incentive spirometer", "Pain control", "Steam inhalation", "Bed rest without mobilization"], 3,
  "Atelectasis prevention: chest physiotherapy, pain control, treat CHF & COPD, steam inhalation, stop smoking. (Book p18)")
q(18, "Atelectasis", "Before surgery, to prevent atelectasis, one must treat:",
  ["Diabetes and hypertension", "Congestive heart failure & COPD", "Anemia and jaundice", "UTI and wound infection"], 1,
  "Treat congestive heart failure (CHF) & chronic obstructive pulmonary disease (COPD) before Sx. (Book p18)")
q(18, "Atelectasis", "Smoking must be stopped how long prior to surgery to prevent atelectasis?",
  ["1-2 days", "1 week", "4-6 weeks", "6 months"], 2,
  "Cessation of smoking 4-6 weeks prior to Sx. (Book p18)")
q(18, "Atelectasis", "Steam inhalation is listed in the prevention of:",
  ["DVT", "Atelectasis", "UTI", "Wound infection"], 1,
  "Atelectasis Prevention: ... Steam inhalation. (Book p18)")

# ---------------- p19 · DVT ----------------
q(19, "DVT", "Deep vein thrombosis is typically:",
  ["Bilateral", "Unilateral (U/L)", "Upper limb only", "Facial"], 1,
  "DVT Clinical Features: U/L; Lower limbs > Upper limbs; Swelling & pain. (Book p19)")
q(19, "DVT", "In DVT, involvement is:",
  ["Upper limbs > Lower limbs", "Lower limbs > Upper limbs", "Equal in all limbs", "Facial veins only"], 1,
  "DVT: Lower limbs > Upper limbs; Swelling & pain. (Book p19)")
q(19, "DVT", "DVT presents with:",
  ["Swelling & pain", "Fever only", "Hiccups", "Diarrhoea"], 0,
  "DVT Clinical Features: Swelling & pain. (Book p19)")
q(19, "DVT", "The investigation of choice for DVT is:",
  ["CT venography", "Duplex scan", "D-dimer", "Contrast MRI"], 1,
  "DVT Ix: Duplex scan (IOC). (Book p19)")
q(19, "DVT", "Early ambulation prevents DVT because:",
  ["Clots dissolve", "Stasis is prevented", "Veins constrict", "Platelets fall"], 1,
  "Mechanical prophylaxis: Early ambulation: Stasis prevented. (Book p19)")
q(19, "DVT", "Mechanical prophylaxis of DVT includes:",
  ["Heparin", "Pneumatic stockings", "Warfarin", "Aspirin"], 1,
  "Mechanical prophylaxis: Early ambulation; Pneumatic stockings. (Book p19)")
q(19, "DVT", "The drug of choice for pharmacological prophylaxis of DVT is:",
  ["Unfractionated heparin", "Low molecular weight heparin", "Warfarin", "Aspirin"], 1,
  "Pharmacological prophylaxis: DOC: Low molecular weight heparin. (Book p19)")
q(19, "DVT", "The pneumatic compression stocking is noted to have:",
  ["Numbering present on it", "No numbering present on it", "A heparin coating", "Steel wires"], 1,
  "Pneumatic compression stocking: No numbering present on it; Connected to machine. (Book p19)")
q(19, "DVT", "Pneumatic anti-DVT stockings work when:",
  ["Worn loose", "Connected to machine", "Filled with water", "Heated"], 1,
  "Pneumatic compression stocking: Connected to machine. (Book p19)")

# ---------------- p19 · BURST ABDOMEN ----------------
q(19, "Burst Abdomen", "Burst abdomen means: after abdominal surgery, the rectus sheath opens up with:",
  ["Bleeding only", "Direct visualization of bowel", "Fever only", "Urinary retention"], 1,
  "Burst abdomen: Abdominal Sx -> Rectus sheath opens up -> Direct visualization of bowel. (Book p19)")
q(19, "Burst Abdomen", "Cough on POD 6 is a clinical feature of:",
  ["Atelectasis", "Burst abdomen", "Pneumonia", "UTI"], 1,
  "Burst abdomen Clinical Features: Cough on POD 6. (Book p19)")
q(19, "Burst Abdomen", "In burst abdomen, the dressing is soaked with:",
  ["Clear urine", "Reddish fluid", "Green bile", "Black stool"], 1,
  "Burst abdomen: Dressing soaked with reddish fluid; Serous/salmon fluid sign. (Book p19)")
q(19, "Burst Abdomen", "The serous/salmon fluid sign is seen in:",
  ["Atelectasis", "Burst abdomen", "DVT", "UTI"], 1,
  "Burst abdomen: Serous/salmon fluid sign. (Book p19)")
q(19, "Burst Abdomen", "Emergency management of burst abdomen is:",
  ["Immediate resuturing in OT", "Reposit the bowel + urobag/Bogota bag laparostomy", "Antibiotics alone", "Percutaneous drainage"], 1,
  "Burst abdomen Emergency mx: Reposit the bowel + urobag/Bogota bag laparostomy. (Book p19)")
q(19, "Burst Abdomen", "Definitive management of burst abdomen is:",
  ["Urobag laparostomy", "Resuturing of rectus sheath (OT)", "Skin grafting", "Pigtail drainage"], 1,
  "Burst abdomen Definitive mx: Resuturing of rectus sheath (OT). (Book p19)")
q(19, "Burst Abdomen", "Patient factors predisposing to burst abdomen include all of the following EXCEPT:",
  ["Chronic cough", "Obesity", "Young athletic age", "Malnourished"], 2,
  "Patient factors: Chronic cough, Constipation, Infection, Obesity, Immunocompromised, Malnourished. (Book p19)")
q(19, "Burst Abdomen", "Which pair predisposes to burst abdomen?",
  ["Immunocompromised and malnourished", "Young and athletic", "Thin and tall", "None of these"], 0,
  "Patient factors: ... Immunocompromised, Malnourished. (Book p19)")
q(19, "Burst Abdomen", "In the Bogota bag laparostomy diagram, the urobag is:",
  ["Placed inside the peritoneum", "Sutured with skin sheath", "Connected to suction", "Left open to air"], 1,
  "Diagram: urobag sutured with skin sheath (Urobag/Bogota bag laparostomy). (Book p19)")

# ---------------- p20 · SURGEON/SX FACTORS ----------------
q(20, "Sx Factors", "For burst abdomen, the higher-risk incision is:",
  ["Transverse incision", "Midline incision", "Subcostal incision", "Pfannenstiel incision"], 1,
  "Surgeon/Sx factors: Midline incision > transverse incision. (Book p20)")
q(20, "Sx Factors", "Burst abdomen is more common after:",
  ["Elective Sx", "Emergency Sx", "Day care Sx", "Laparoscopic Sx"], 1,
  "Surgeon/Sx factors: Emergency Sx > elective Sx. (Book p20)")
q(20, "Sx Factors", "For rectus sheath closure, the higher-risk technique is:",
  ["Interrupted sutures", "Continuous sutures", "Staples", "Glue"], 1,
  "Surgeon/Sx factors: Continuous sutures > interrupted sutures. (Book p20)")
q(20, "Sx Factors", "For sheath closure, long bites (1 cm) are worse than short bites of:",
  ["0.5 cm", "2 cm", "3 cm", "5 cm"], 0,
  "Long bites (1 cm) > short bites (0.5 cm). (Book p20)")
q(20, "Sx Factors", "Jenkins' theory states: Length of thread = minimum 4 times:",
  ["Thickness of rectus", "Length of the wound", "Patient weight", "Suture diameter"], 1,
  "Short thread > long thread (Jenkins' theory: Length of thread = min 4 times length of the wound). (Book p20)")
q(20, "Sx Factors", "For rectus sheath closure, preferred suture is:",
  ["Absorbable over non absorbable", "Non absorbable over absorbable", "Catgut only", "Staples only"], 1,
  "For rectus sheath closure: Non absorbable > absorbable. (Book p20)")
q(20, "Sx Factors", "For rectus sheath closure in children, the book advises:",
  ["Silk", "Polydioxanone suture-PDS (Delayed absorbable)", "Plain catgut", "Steel wire"], 1,
  "In children: Polydioxanone suture-PDS (Delayed absorbable sutures) is used. (Book p20)")

# ---------------- p20 · INTRA-ABDOMINAL ABSCESSES ----------------
q(20, "Abscess", "Overall, the most common site of intra-abdominal abscess is the:",
  ["Morrison's pouch", "Pelvis/pouch of Douglas", "Subdiaphragmatic space", "Lesser sac"], 1,
  "Intra-abdominal abscess Site: m/c Overall: Pelvis/pouch of Douglas. (Book p20)")
q(20, "Abscess", "In a supine patient, the most common site of collection is:",
  ["Pelvis", "Morrison's pouch / right hepatorenal pouch", "Left paracolic gutter", "Spleen"], 1,
  "Supine patient: Morrison's pouch/right hepatorenal pouch. (Book p20)")
q(20, "Abscess", "In an ambulatory patient, the most common site of collection is the:",
  ["Morrison's pouch", "Pelvis/pouch of Douglas", "Subdiaphragmatic space", "Liver"], 1,
  "Ambulatory patient: Pelvis/pouch of Douglas. (Book p20)")
q(20, "Abscess", "Intra-abdominal abscess presents with:",
  ["Fever with chills & rigor", "Painless swelling", "Jaundice only", "Constipation only"], 0,
  "Abscess Clinical features: Fever with chills & rigor. (Book p20)")
q(20, "Abscess", "Hiccups suggest a collection in the:",
  ["Pelvis", "Subdiaphragmatic space", "Morrison's pouch", "Paracolic gutter"], 1,
  "Subdiaphragmatic space collection: Hiccups; Shoulder pain (Referred pain). (Book p20)")
q(20, "Abscess", "Shoulder pain in a subdiaphragmatic collection is a:",
  ["Direct pain", "Referred pain", "Psychogenic pain", "Cardiac pain"], 1,
  "Subdiaphragmatic space: Shoulder pain (Referred pain). (Book p20)")
q(20, "Abscess", "Pelvic diarrhoea, mainly mucous, suggests a collection in the:",
  ["Subdiaphragmatic space", "Pelvis", "Liver", "Spleen"], 1,
  "Pelvis collection: Pelvic diarrhoea (mainly mucous); increased frequency of micturition. (Book p20)")
q(20, "Abscess", "Increased frequency of micturition suggests a collection in the:",
  ["Subdiaphragmatic space", "Pelvis", "Morrison's pouch", "Kidney"], 1,
  "Pelvis collection: increased frequency of micturition. (Book p20)")
q(20, "Abscess", "The investigation of choice for intra-abdominal abscess is:",
  ["USG abdomen", "CECT Abdomen", "Plain X-ray", "PET scan"], 1,
  "Ix: CECT Abdomen (IOC). (Book p20)")
q(20, "Abscess", "Management of intra-abdominal abscess is:",
  ["Open surgery always", "Drainage with pigtail catheter under USG guidance", "Antibiotics alone", "Observation only"], 1,
  "Mx: Drainage with pigtail catheter under USG guidance. (Book p20)")
q(20, "Abscess", "On CECT, a pelvic abscess appears as a:",
  ["Homogeneous enhancement", "Heterogeneous collection", "Calcified mass", "Air-fluid cyst"], 1,
  "CECT Pelvic abscess: Heterogeneous collection. (Book p20)")

# ---------------- p21 · SSI ----------------
q(21, "SSI", "Surgical site infection is a wound infection occurring within:",
  ["7 days of Sx", "30 days of Sx", "6 months of Sx", "5 years of Sx"], 1,
  "SSI: wound infection within 30 days of Sx. (Book p21)")
q(21, "SSI", "If an implant is placed, SSI is defined within:",
  ["30 days of Sx", "One year of Sx", "5 years of Sx", "10 years of Sx"], 1,
  "SSI: within 30 days of Sx or if an implant is placed within one year of Sx. (Book p21)")
q(21, "SSI", "Superficial SSI is:",
  ["Below fascia", "Above fascia", "Collection in organ/cavity", "Bloodstream infection"], 1,
  "SSI Types: Superficial: Above fascia; Deep: Below fascia; Organ space: Collection in organ/cavity. (Book p21)")
q(21, "SSI", "Deep SSI is:",
  ["Above fascia", "Below fascia", "Skin redness only", "Bloodstream infection"], 1,
  "SSI Types: Deep: Below fascia. (Book p21)")
q(21, "SSI", "Organ space SSI is:",
  ["Above fascia", "Below skin only", "Collection in organ/cavity", "Fever without focus"], 2,
  "SSI Types: Organ space: Collection in organ/cavity. (Book p21)")

# ---------------- p21 · ASEPSIS ----------------
q(21, "ASEPSIS", "'Additional treatment' in the ASEPSIS score includes:",
  ["Only antibiotics", "Antibiotics, drainage of pus under LA, debridement under GA", "Only dressings", "Only physiotherapy"], 1,
  "ASEPSIS Additional treatment: Antibiotics; Drainage of pus under LA; Debridement under GA. (Book p21)")
q(21, "ASEPSIS", "In the ASEPSIS score, drainage of pus is done under __ and debridement under __:",
  ["GA, LA", "LA, GA", "LA, LA", "GA, GA"], 1,
  "Drainage of pus under local anesthesia; Wound debridement under general anesthesia. (Book p21)")
q(21, "ASEPSIS", "In ASEPSIS, the first 'S' stands for:",
  ["Surgery", "Serous discharge", "Sepsis", "Stitch abscess"], 1,
  "ASEPSIS: Serous discharge; Erythema; Purulent exudate; Separation of deep tissues; Isolation of bacteria; Stay prolonged. (Book p21)")
q(21, "ASEPSIS", "'Erythema' in ASEPSIS stands for the letter:",
  ["A", "S", "E", "P"], 2,
  "ASEPSIS: ... Erythema ... (Book p21)")
q(21, "ASEPSIS", "'Purulent exudate' in ASEPSIS stands for the letter:",
  ["A", "S", "E", "P"], 3,
  "ASEPSIS: ... Purulent exudate ... (Book p21)")
q(21, "ASEPSIS", "Separation of deep tissues in ASEPSIS stands for the second:",
  ["A", "P", "S", "I"], 2,
  "ASEPSIS: ... Separation of deep tissues ... (Book p21)")
q(21, "ASEPSIS", "'Isolation of bacteria from the wound' stands for the letter:",
  ["A", "P", "I", "S"], 2,
  "ASEPSIS: ... Isolation of bacteria from the wound ... (Book p21)")
q(21, "ASEPSIS", "In ASEPSIS, prolonged inpatient stay means over:",
  ["7 days", "14 days due to wound infection", "30 days", "1 year"], 1,
  "ASEPSIS: Stay as inpatient prolonged over 14 days due to wound infection. (Book p21)")

# ---------------- p21 · SOUTHAMPTON ----------------
q(21, "Southampton", "Southampton grade 0 means:",
  ["Mild bruising", "Normal healing", "Erythema", "Pus discharge"], 1,
  "Southampton: 0: Normal healing. (Book p21)")
q(21, "Southampton", "Southampton grade I means:",
  ["Normal healing", "Normal healing with mild bruising or erythema", "Erythema plus inflammation", "Pus discharge"], 1,
  "Southampton: I: Normal healing with mild bruising or erythema. (Book p21)")
q(21, "Southampton", "Southampton grade II means:",
  ["Normal healing", "Mild bruising", "Erythema plus other signs of inflammation", "Pus discharge"], 2,
  "Southampton: II: Erythema plus other signs of inflammation. (Book p21)")
q(21, "Southampton", "Southampton grade III means:",
  ["Normal healing", "Erythema", "Clear or haemoserous discharge", "Pus/purulent discharge"], 2,
  "Southampton: III: Clear or haemoserous discharge. (Book p21)")
q(21, "Southampton", "Southampton grade IV means:",
  ["Clear discharge", "Haemoserous discharge", "Erythema only", "Pus/purulent discharge"], 3,
  "Southampton: IV: Pus/purulent discharge. (Book p21)")
q(21, "Southampton", "Southampton grade V means:",
  ["Normal healing", "Mild bruising", "Clear discharge", "Deep or severe wound infection with or without tissue breakdown"], 3,
  "Southampton: V: Deep or severe wound infection with or without tissue breakdown. (Book p21)")

# ---------------- p21 · RISK FACTORS ----------------
q(21, "Risk Factors", "Extremes of age at risk for SSI are:",
  ["Neonates and older adults", "Teenagers only", "Middle-aged only", "None"], 0,
  "Risk factors: Extremities of age: Neonates, older adults. (Book p21)")
q(21, "Risk Factors", "Which pair is listed as SSI risk factors?",
  ["Recent Sx of chest/abdomen and coexisting remote infection", "Tall height and fair skin", "Male sex and blood group O", "None of these"], 0,
  "Risk factors: Recent Sx especially of chest/abdomen; Coexisting infection remote to surgical site. (Book p21)")
q(21, "Risk Factors", "Which pair is listed as SSI risk factors?",
  ["Diabetes mellitus and corticosteroid therapy", "Hypertension and asthma", "Migraine and epilepsy", "None of these"], 0,
  "Risk factors: Diabetes mellitus; Corticosteroid therapy. (Book p21)")
q(21, "Risk Factors", "Which metabolic factor increases SSI risk?",
  ["Hypercholesterolemia", "Hypocholesterolemia", "Hypernatremia", "Hypokalemia"], 1,
  "Risk factors: Hypocholesterolemia. (Book p21)")
q(21, "Risk Factors", "Which pair is listed as SSI risk factors?",
  ["Obesity and malnutrition", "Fitness and protein diet", "Youth and exercise", "None of these"], 0,
  "Risk factors: Obesity; Malnutrition. (Book p21)")
q(21, "Risk Factors", "Which pair is listed as SSI risk factors?",
  ["Chronic inflammation and prior site irradiation", "Acute pain and fever", "Single surgery and youth", "None of these"], 0,
  "Risk factors: Chronic inflammation; Prior site irradiation. (Book p21)")
q(21, "Risk Factors", "Which pair is listed as SSI risk factors?",
  ["Hypothermia and hypoxemia", "Hyperthermia and hyperoxia", "Fever and tachycardia", "None of these"], 0,
  "Risk factors: Hypothermia; Hypoxemia. (Book p21)")

# ---------------- p22 · WOUND TYPES ----------------
q(22, "Wound Types", "Clean (Class I) wounds include all of the following EXCEPT:",
  ["Thyroid surgery", "Breast surgery", "CABG", "Emergency appendectomy"], 3,
  "Class I Clean: Thyroid, Breast, CABG, Knee replacement, Uncomplicated inguinal hernia Sx. (Book p22)")
q(22, "Wound Types", "Uncomplicated inguinal hernia surgery is a:",
  ["Clean wound", "Clean contaminated wound", "Contaminated wound", "Dirty wound"], 0,
  "Class I Clean: ... Uncomplicated inguinal hernia surgery. (Book p22)")
q(22, "Wound Types", "SSI rate in clean wounds with and without antibiotic prophylaxis is:",
  ["1-2% both", "3% and 6-9%", "6% and 20%", "7-8% and 20-40%"], 0,
  "Clean wound SSI: 1-2% with and 1-2% without prophylaxis. (Book p22)")
q(22, "Wound Types", "Prophylactic antibiotics have no role in clean wounds EXCEPT when:",
  ["Patient is young", "An implant or mesh has been placed", "Surgery is short", "Wound is small"], 1,
  "No role of prophylactic antibiotics in clean wounds except when an implant or mesh is placed. (Book p22)")
q(22, "Wound Types", "Clean contaminated (Class II) wounds involve the GI/GU system but:",
  ["With pus", "With no inflammation", "With fecal contamination", "After 6 hours trauma"], 1,
  "Class II: GI/GU system - but there is no inflammation. (Book p22)")
q(22, "Wound Types", "Class II wounds include all of the following EXCEPT:",
  ["Elective cholecystectomy", "Elective appendectomy", "LSCS", "Emergency appendectomy"], 3,
  "Class II: Elective/interval cholecystectomy, Elective appendectomy, LSCS, Lap hysterectomy, prepared bowel Sx. (Book p22)")
q(22, "Wound Types", "Bowel surgery belongs to Class II if the bowel is:",
  ["Unprepared", "Prepared (Enema or Peglec)", "Obstructed", "Perforated"], 1,
  "Class II: Bowel surgery, if the bowel is prepared (Enema or Peglec). (Book p22)")
q(22, "Wound Types", "Urinary stone removal without UTI is a:",
  ["Clean wound", "Clean contaminated wound", "Contaminated wound", "Dirty wound"], 1,
  "Class II: Urinary stone removal when no UTI. (Book p22)")
q(22, "Wound Types", "SSI rate in Class II wounds with vs without prophylaxis is:",
  ["1-2% both", "3% vs 6-9%", "6% vs 20%", "7-8% vs 20-40%"], 1,
  "Class II SSI: 3% with, 6-9% without prophylaxis. (Book p22)")
q(22, "Wound Types", "Contaminated (Class III) wounds involve the GI/GU system with:",
  ["No inflammation", "Non-purulent inflammation", "Pus", "Fecal contamination"], 1,
  "Class III: GI/GU system when non-purulent inflammation is present. (Book p22)")
q(22, "Wound Types", "Class III wounds include all of the following EXCEPT:",
  ["Emergency cholecystectomy", "Emergency appendectomy", "Elective cholecystectomy", "Bowel opened in intestinal obstruction"], 2,
  "Class III: Emergency cholecystectomy, Emergency appendectomy, bowel opened in obstruction, open cardiac massage. (Book p22)")
q(22, "Wound Types", "Open cardiac massage is a Class III wound because of:",
  ["Pus", "Major break in sterile technique", "Fecal contamination", "Delayed closure"], 1,
  "Class III: Open cardiac massage (Major break in sterile technique). (Book p22)")
q(22, "Wound Types", "SSI rate in Class III wounds with vs without prophylaxis is:",
  ["1-2% both", "3% vs 6-9%", "6% vs 20%", "7-8% vs 20-40%"], 2,
  "Class III SSI: 6% with, 20% without prophylaxis. (Book p22)")
q(22, "Wound Types", "In contaminated (Class III) wounds:",
  ["No antibiotics needed", "Antibiotics should be continued", "Single dose only", "Antibiotics stopped"], 1,
  "Class III: Antibiotics should be continued. (Book p22)")
q(22, "Wound Types", "Dirty (Class IV) wounds are defined by:",
  ["No inflammation", "Non-purulent inflammation", "Pus present", "Clean incision"], 2,
  "Class IV Dirty wound: Pus present. (Book p22)")
q(22, "Wound Types", "Class IV wounds include all of the following EXCEPT:",
  ["All abscesses", "Peritonitis/fecal contamination", "Neglected traumatic wound >6 hours", "Elective hernia repair"], 3,
  "Class IV: All abscesses; Peritonitis/fecal contamination; Neglected traumatic wound >6 hours. (Book p22)")
q(22, "Wound Types", "A neglected traumatic wound becomes a dirty wound after:",
  ["1 hour", "4 hours", "6 hours", "24 hours"], 2,
  "Class IV: Any neglected traumatic wound >6 hours. (Book p22)")
q(22, "Wound Types", "SSI rate in Class IV wounds with vs without prophylaxis is:",
  ["1-2% both", "3% vs 6-9%", "6% vs 20%", "7-8% vs 20-40%"], 3,
  "Class IV SSI: 7-8% with, 20-40% without prophylaxis. (Book p22)")

# ---------------- p22 · GOLDEN / DECISIVE PERIOD ----------------
q(22, "Periods", "The golden period for a traumatic wound is:",
  ["1 hour", "4 hours", "6 hours", "24 hours"], 2,
  "Golden period: Traumatic wound: 6 hours. (Book p22)")
q(22, "Periods", "For trauma, the golden period is:",
  ["1 hour following trauma", "4 hours following trauma", "6 hours following trauma", "24 hours following trauma"], 0,
  "Golden period: Trauma: 1 hour following trauma. (Book p22)")
q(22, "Periods", "The decisive period is 4 hours - the time between:",
  ["Trauma and admission", "Skin incision & bacterial colonisation", "Fever and antibiotics", "Surgery and discharge"], 1,
  "Decisive period: 4 hours - time b/w skin incision & bacterial colonisation. (Book p22)")
q(22, "Periods", "In an elective OT list:",
  ["Dirty cases are posted first", "Clean cases are posted first", "Emergency cases first", "Order does not matter"], 1,
  "In an elective OT list, clean cases are posted first. (Book p22)")

# ---------------- p23 · HAND HYGIENE ----------------
q(23, "Hand Hygiene", "The most important factor in prevention of wound infection is:",
  ["Antibiotics", "Hand hygiene by surgeon", "OT temperature", "Suture type"], 1,
  "Hand hygiene by surgeon: most important factor. (Book p23)")
q(23, "Hand Hygiene", "Minimum duration of surgical handwash is:",
  ["1 min", "3 mins", "10 mins", "30 secs"], 1,
  "Min duration of handwash: 3 mins. (Book p23)")
q(23, "Hand Hygiene", "For routine hand hygiene, one may use:",
  ["Only soap & water", "Soap & water / alcohol hand rub", "Only alcohol", "Only betadine"], 1,
  "Soap & water/alcohol hand rub should be used. (Book p23)")
q(23, "Hand Hygiene", "After toilet visit or if hands are visibly soiled:",
  ["Only alcohol rub is used", "Only soap & water used", "No wash needed", "Gloves suffice"], 1,
  "After toilet visit / visibly soiled: Only soap & water used. (Book p23)")
q(23, "Hand Hygiene", "The 'before' moments of hand hygiene are:",
  ["Before touching a patient; Before clean/aseptic procedure", "After touching a patient only", "After toilet only", "None"], 0,
  "5 moments: Before touching a patient; Before clean/aseptic procedure; After body fluid risk; After touching patient; After surroundings. (Book p23)")
q(23, "Hand Hygiene", "The 'after' moments of hand hygiene include all of the following EXCEPT:",
  ["After body fluid exposure risk", "After touching a patient", "After touching patient's surroundings", "After entering the hospital gate"], 3,
  "5 moments include: After body fluid risk; After touching patient; After touching surroundings. (Book p23)")

# ---------------- p23 · PART PREP / CLEANING ----------------
q(23, "Part Prep", "The best method to remove hair before surgery is:",
  ["Shaving with razor", "Hair clipper", "Waxing", "Depilatory cream"], 1,
  "To remove hair before Sx: Hair clipper (Best method). (Book p23)")
q(23, "Part Prep", "Shaving of hair is not done because it causes microabrasions leading to:",
  ["Less pain", "Bacterial colonisation -> increased SSI rates", "Faster healing", "Better cosmesis"], 1,
  "Shaving (Not done): microabrasions -> Bacterial colonisation -> increased SSI rates. (Book p23)")
q(23, "Cleaning", "The preferred sterilising agent for skin preparation is:",
  ["Betadine alone", "Chlorhexidine + alcohol > betadine", "Saline alone", "Hydrogen peroxide"], 1,
  "Sterilising agent: Chlorhexidine + alcohol > betadine. (Book p23)")
q(23, "Cleaning", "In a female patient for abdominal surgery, the area cleaned is:",
  ["Nipple to mid thigh", "Infra mammary crease to mid thigh", "Neck to ankle", "Umbilicus only"], 1,
  "Area cleaned: Female: Infra mammary crease to mid thigh; Male: Nipple to mid thigh. (Book p23)")
q(23, "Cleaning", "In a male patient for abdominal surgery, the area cleaned is:",
  ["Infra mammary crease to mid thigh", "Nipple to mid thigh", "Neck to ankle", "Umbilicus only"], 1,
  "Area cleaned: Male: Nipple to mid thigh. (Book p23)")
q(23, "Cleaning", "The abdomen is cleaned:",
  ["Lateral to medial", "Medial to lateral", "Upwards only", "In circles anywhere"], 1,
  "Abdomen: Cleaned medial to lateral; Thigh: lateral to medial. (Book p23)")
q(23, "Cleaning", "The thigh is cleaned:",
  ["Medial to lateral", "Lateral to medial", "Upwards only", "Distal to proximal only"], 1,
  "Thigh: Cleaned lateral to medial. (Book p23)")
q(23, "Cleaning", "Limbs are cleaned till:",
  ["One joint up", "One joint down", "Toes only", "Whole body"], 0,
  "Limbs: Till one joint up. (Book p23)")
q(23, "Cleaning", "After cleaning the part, one must:",
  ["Cover immediately while wet", "Always let the area dry up", "Wipe with dry cloth fast", "Apply powder"], 1,
  "Always let the area dry up after cleaning. (Book p23)")
q(23, "Cleaning", "While cleaning, the rule is:",
  ["Clean periphery first", "Always clean the incision site first, go outwards", "Clean randomly", "Clean twice with same gauze"], 1,
  "Always clean the incision site first, go outwards; Cleaned twice (1 gauze + another gauze). (Book p23)")
q(23, "Cleaning", "The part is cleaned twice using:",
  ["Same gauze twice", "1 gauze then another gauze", "Same mop", "Water only"], 1,
  "Cleaned twice: 1 gauze + Another gauze. (Book p23)")

# ---------------- p23 · PROPHYLACTIC ANTIBIOTICS ----------------
q(23, "Prophylactic Abx", "The best time for prophylactic antibiotics is:",
  ["At skin closure", "30-60 mins before Sx", "One day before Sx", "After Sx only"], 1,
  "Prophylactic antibiotics: Best time: 30-60 mins before Sx. (Book p23)")
q(23, "Prophylactic Abx", "In prolonged surgery, the prophylactic dose is repeated after:",
  ["1 hour", "2 hours", "4 hours", "12 hours"], 2,
  "In prolonged Sx: Repeat dose after 4 hours. (Book p23)")

# ---------------- p24 · OT PARAMETERS ----------------
q(24, "OT Parameters", "HEPA filters must be 90% efficient in removing particles greater than:",
  ["0.5 mm", "5 mm", "5 cm", "0.5 cm"], 0,
  "Ultra clean laminar air flow: Hepa filters -> must be 90% efficient in removing particles >0.5 mm. (Book p24)")
q(24, "OT Parameters", "The optimum OT temperature is:",
  ["10-14 C", "18-22 C", "25-30 C", "32-36 C"], 1,
  "Optimum temperature: 18-22 C - Avoid hypothermia. (Book p24)")
q(24, "OT Parameters", "The Bair hugger is used to:",
  ["Prevent hypothermia", "Prevent hyperthermia", "Give oxygen", "Monitor BP"], 0,
  "Bair hugger (To prevent hypothermia). (Book p24)")
q(24, "OT Parameters", "The optimum relative humidity in OT is:",
  ["20-30%", "50-60%", "80-90%", "100%"], 1,
  "Relative humidity: 50-60%. (Book p24)")
q(24, "OT Parameters", "Laminar air flow in OT is:",
  ["4 fresh air changes/hour from clean to dirty area", "1 change/hour dirty to clean", "No changes needed", "20 changes/hour"], 0,
  "Laminar air flow: 4 fresh air changes/hour from clean -> Dirty area. (Book p24)")
q(24, "OT Parameters", "Inside the OT there must be:",
  ["Negative pressure", "Positive pressure", "Zero pressure", "Vacuum"], 1,
  "Positive pressure inside OT. (Book p24)")
q(24, "OT Parameters", "To prevent wound infection, blood sugar must be controlled to:",
  ["Prevent hyperglycemia", "Allow hyperglycemia", "Cause hypoglycemia", "Ignore sugar"], 0,
  "Prevent hyperglycemia. (Book p24)")
q(24, "OT Parameters", "Proper hemostasis is listed in the prevention of:",
  ["DVT", "Wound infection", "Atelectasis", "Hypothermia"], 1,
  "Prevention: Proper hemostasis. (Book p24)")
q(24, "OT Parameters", "In the immediate post-operative period, the patient must be given:",
  ["Antibiotics", "O2", "Blood", "Sedation"], 1,
  "Give O2 in immediate post operative period. (Book p24)")

# ---------------- UNITS ----------------
def uid(n): return {"id": f"SURG-U4-{n}", "ch": 4, "n": n}
def rng(a, b): return [f"SURG-C4-{i:03d}" for i in range(a, b + 1)]
UNITS = [
    {**uid(1), "title": "Post-op Fever: Causes by Day", "sec": "Fever Causes \u00b7 p18",
     "qs": rng(1, 8),
     "guide": "Fever tells time after surgery: atelectasis on day 1, pneumonia, thrombophlebitis and UTI on days 2-3, wound infection and DVT on days 4-5, burst abdomen on day 6, and deep intra-abdominal collections from day 7 onward."},
    {**uid(2), "title": "Pneumonia, Thrombophlebitis & Atelectasis", "sec": "Atelectasis \u00b7 p18",
     "qs": rng(9, 19),
     "guide": "Post-operative pneumonia brings fever cured by antibiotics, while superficial thrombophlebitis adds pain soothed by topical heparinoids. Atelectasis - collapsed alveoli, the commonest day-1 fever - is prevented by incentive spirometry, pain control, treating CHF and COPD, steam, and quitting smoking 4-6 weeks ahead."},
    {**uid(3), "title": "Deep Vein Thrombosis", "sec": "DVT \u00b7 p19",
     "qs": rng(20, 28),
     "guide": "DVT swells one leg - lower limbs far more than upper - and is confirmed on duplex scan. Early ambulation defeats stasis, pneumatic stockings squeeze the calves, and low molecular weight heparin is the drug of choice for prophylaxis."},
    {**uid(4), "title": "Burst Abdomen", "sec": "Burst Abdomen \u00b7 p19",
     "qs": rng(29, 37),
     "guide": "On day 6 a cough can split the rectus sheath open, baring bowel beneath a dressing soaked in reddish salmon fluid. The emergency answer is repositing bowel under a Bogota bag, with definitive resuturing in theatre - while chronic cough, constipation, infection, obesity, immunosuppression and malnutrition set the stage."},
    {**uid(5), "title": "Surgeon Factors & Rectus Closure", "sec": "Sx Factors \u00b7 p20",
     "qs": rng(38, 44),
     "guide": "Midline, emergency, continuous, long-bite, short-thread closures burst most - Jenkins demands thread four times the wound length. Non-absorbable suture closes adult rectus, while children get delayed-absorbable PDS."},
    {**uid(6), "title": "Intra-abdominal Abscesses", "sec": "Abscess \u00b7 p20",
     "qs": rng(45, 55),
     "guide": "Pus seeks the pelvis in walkers and Morrison's pouch in the bedridden, announcing itself with fever, chills and rigor. Subdiaphragmatic pus triggers hiccups and referred shoulder pain; pelvic pus brings mucous diarrhoea and frequent micturition - diagnosed by CECT and drained by USG-guided pigtail."},
    {**uid(7), "title": "SSI: Definition & Types", "sec": "SSI \u00b7 p21",
     "qs": rng(56, 60),
     "guide": "A surgical site infection strikes within 30 days - or within a year if an implant was placed. Superficial infection stays above fascia, deep goes below it, and organ-space infection pools inside an organ or cavity."},
    {**uid(8), "title": "ASEPSIS Wound Score", "sec": "ASEPSIS \u00b7 p21",
     "qs": rng(61, 68),
     "guide": "ASEPSIS grades wounds by Additional treatment, Serous discharge, Erythema, Purulent exudate, Separation of deep tissues, Isolation of bacteria, and inpatient Stay beyond 14 days - with pus drained under local but debridement under general anaesthesia."},
    {**uid(9), "title": "Southampton Wound Score", "sec": "Southampton \u00b7 p21",
     "qs": rng(69, 74),
     "guide": "Southampton climbs from 0 - normal healing - through bruising, erythema and clear discharge to frank pus at grade IV and deep severe infection with or without breakdown at grade V."},
    {**uid(10), "title": "SSI Risk Factors", "sec": "Risk Factors \u00b7 p21",
     "qs": rng(75, 81),
     "guide": "Neonates and the elderly, recent chest or abdominal surgery, distant coexisting infection, diabetes, steroids, low cholesterol, obesity, malnutrition, chronic inflammation, prior irradiation, hypothermia and hypoxemia - twelve flags that mark a wound for infection."},
    {**uid(11), "title": "Wound Classes I-IV", "sec": "Wound Types \u00b7 p22",
     "qs": rng(82, 99),
     "guide": "Clean wounds infect at 1-2% with or without antibiotics; clean-contaminated at 3% versus 6-9%; contaminated at 6% versus 20% with antibiotics continued; and dirty pus-filled wounds at 7-8% versus 20-40% - from thyroid and hernia surgery at one end to abscesses and peritonitis at the other."},
    {**uid(12), "title": "Golden & Decisive Periods", "sec": "Periods \u00b7 p22",
     "qs": rng(100, 103),
     "guide": "The golden period gives traumatic wounds 6 hours - just 1 hour after major trauma - while the decisive 4 hours span skin incision to bacterial colonisation. On elective lists, clean cases always go first."},
    {**uid(13), "title": "Hand Hygiene & Part Preparation", "sec": "Hand Hygiene \u00b7 p23",
     "qs": rng(104, 111),
     "guide": "The surgeon's hands matter most: 3-minute scrubs with soap or alcohol rub - soap alone after toilets or visible soil - across the five WHO moments. Hair falls to clippers, never razors, whose microabrasions seed infection."},
    {**uid(14), "title": "Cleaning the Operative Part", "sec": "Cleaning \u00b7 p23",
     "qs": rng(112, 122),
     "guide": "Chlorhexidine plus alcohol beats betadine for skin prep - inframammary crease to mid-thigh in women, nipple to mid-thigh in men, abdomen medial-to-lateral, thigh lateral-to-medial, limbs a joint beyond, always incision-first and outward, twice over, then left to dry."},
    {**uid(15), "title": "Prophylactic Antibiotics & OT Parameters", "sec": "OT Parameters \u00b7 p24",
     "qs": rng(123, 131),
     "guide": "Antibiotics peak 30-60 minutes before incision and repeat at 4 hours in long cases. The theatre breathes HEPA-filtered laminar flow at 4 changes an hour under positive pressure, 18-22 degrees, 50-60% humidity - with the Bair hugger, euglycemia, hemostasis and post-operative oxygen completing the shield."},
]

data = {"questions": Q, "units": UNITS}
with open("data/ch4.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
print(f"ch4: {len(Q)} questions, {len(UNITS)} units")
