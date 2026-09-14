#!/usr/bin/env python3
"""Build data/ch39.json — ch39 Benign Pancreatic Conditions (Marrow Surgery Ed 8, book p285-296)."""
import json

Q = []


def q(page, sec, text, opts, ans, exp):
    Q.append({
        "id": f"SURG-C39-{len(Q)+1:03d}",
        "sec": sec,
        "page": page,
        "q": text,
        "opts": opts,
        "ans": ans,
        "exp": exp,
    })


# ------------------------------------------------------------------ p285
S1 = "Congenital Disorders of the Pancreas"
q(285, S1, "The most common congenital anomaly of the pancreas is:",
  ["Pancreas divisum", "Annular pancreas", "Abernethy malformation", "Pancreatic heterotopia"], 0,
  "Pancreas divisum: m/c congenital anomaly of pancreas. (Book p285)")
q(285, S1, "Pancreas divisum results from:",
  ["Failure of fusion of the dorsal and ventral pancreatic buds", "Malrotation of the ventral bud", "Atresia of the dorsal duct", "Duplication of the pancreatic bud"], 0,
  "Pancreas divisum: failure of fusion of dorsal and ventral pancreatic buds. (Book p285)")
q(285, S1, "Pancreas divisum predisposes to pancreatitis because of:",
  ["Ineffective drainage", "Excess trypsin", "Duct obstruction by a stone", "Autoimmune inflammation"], 0,
  "Pancreas divisum: ineffective drainage raises the risk of pancreatitis. (Book p285)")
q(285, S1, "The diagnosis of pancreas divisum is made by:",
  ["MRCP", "CECT", "USG alone", "ERCP alone"], 0,
  "Pancreas divisum: diagnosis — magnetic resonance cholangiopancreatography (MRCP). (Book p285)")
q(285, S1, "Pancreas divisum is managed by:",
  ["ERCP with sphincterotomy", "Distal pancreatectomy", "Observation only", "Total pancreatectomy"], 0,
  "Pancreas divisum: Mx — ERCP + sphincterotomy. (Book p285)")
q(285, S1, "Annular pancreas is caused by:",
  ["Malrotation of the ventral pancreatic bud encircling the 2nd part of the duodenum", "Failure of fusion of the dorsal and ventral buds", "Duplication of the duodenum", "A congenital duodenal web"], 0,
  "Annular pancreas: malrotation of ventral pancreatic bud — encircles the 2nd part of duodenum. (Book p285)")
q(285, S1, "Annular pancreas is associated with:",
  ["Down's syndrome", "Marfan syndrome", "Turner syndrome", "Neurofibromatosis"], 0,
  "Clinical features: associated with Down's syndrome. (Book p285)")
q(285, S1, "In duodenal atresia associated with annular pancreas, the presentation is:",
  ["Bilious vomiting", "Non-bilious vomiting only", "Haematemesis", "Chronic constipation"], 0,
  "Clinical features: also in duodenal atresia — presents with bilious vomiting. (Book p285)")
q(285, S1, "Which clinical feature of annular pancreas is listed separately from duodenal atresia?",
  ["Non-bilious vomiting", "Bilious vomiting", "Jaundice", "Hematemesis"], 0,
  "Clinical features: non-bilious vomiting (listed for annular pancreas apart from duodenal atresia). (Book p285)")
q(285, S1, "The investigation of choice for annular pancreas is:",
  ["CECT", "Plain X-ray only", "USG alone", "HIDA scan"], 0,
  "Investigation: IOC — CECT. (Book p285)")
q(285, S1, "The X-ray sign of annular pancreas (duodenal obstruction) is:",
  ["Double bubble sign", "Triple bubble sign", "Scaphoid abdomen", "Air fluid level in the stomach only"], 0,
  "Investigation: X-ray — double bubble sign. (Book p285)")
q(285, S1, "The management of annular pancreas is:",
  ["Duodeno-duodenostomy", "Pancreatectomy", "Gastrostomy alone", "Observation"], 0,
  "Management: duodeno-duodenostomy. (Book p285)")
q(285, S1, "In annular pancreas, cutting of the encircling pancreatic segment is avoided to:",
  ["Prevent devascularisation", "Prevent diabetes", "Prevent pancreatitis", "Facilitate healing"], 0,
  "Management: cutting of segment is avoided to prevent devascularisation. (Book p285)")

# ------------------------------------------------------------------ p286
S2 = "Surgical Anatomy: Tunnel of Love and the Sphincter of Oddi"
q(286, S2, "The tunnel of love at the pancreatic head lies between which vessels, and its intact status makes possible:",
  ["The superior mesenteric artery and vein, and Whipple's surgery", "The hepatic artery and portal vein, and cholecystectomy",
   "The splenic artery and vein, and splenectomy", "The coeliac trunk and aorta, and distal pancreatectomy"], 0,
  "Surgical anatomy: tunnel of love — between the superior mesenteric artery and vein; tunnel of love intact — Whipple's surgery. (Book p286)")
q(286, S2, "The sphincter of Oddi is made up of how many sphincters?",
  ["Four", "Two", "Three", "Five"], 0,
  "Sphincter of Oddi: made up of 4 sphincters. (Book p286)")
q(286, S2, "Which of the following is one of the four sphincters of the sphincter of Oddi?",
  ["Superior choledochal sphincter", "Pyloric sphincter", "Ileocaecal sphincter", "Anal sphincter"], 0,
  "Sphincters: 1. Superior choledochal, 2. Inferior choledochal, 3. Ampullary, 4. Pancreatic. (Book p286)")
q(286, S2, "The pancreatic component of the sphincter of Oddi is the:",
  ["Pancreatic sphincter", "Superior choledochal sphincter", "Inferior choledochal sphincter", "Ampullary sphincter only"], 0,
  "Sphincter of Oddi: 4. Pancreatic sphincter. (Book p286)")
q(286, S2, "Sphincter of Oddi dysfunction causes:",
  ["Improper drainage of bile and pancreatic secretions", "Excess bile production", "Pancreatic atrophy", "Duodenal obstruction"], 0,
  "Sphincter of Oddi dysfunction: poor functioning — improper drainage of bile and pancreatic secretions. (Book p286)")
q(286, S2, "The biliary type of sphincter of Oddi dysfunction presents as:",
  ["Biliary colic and post cholecystectomy syndrome", "Pancreatitis", "Gastric outlet obstruction", "Chronic diarrhoea"], 0,
  "Types: biliary — biliary colic, post cholecystectomy syndrome. (Book p286)")
q(286, S2, "The pancreatic type of sphincter of Oddi dysfunction presents as:",
  ["Pancreatitis", "Biliary colic", "A WES sign", "Rigler's triad"], 0,
  "Types: pancreatic — pancreatitis. (Book p286)")
q(286, S2, "The investigation of choice for sphincter of Oddi dysfunction is:",
  ["ERCP with manometry", "USG alone", "Plain X-ray", "HIDA scan"], 0,
  "IOC: ERCP + manometry. (Book p286)")
q(286, S2, "On manometry, sphincter of Oddi dysfunction is defined by a pressure of:",
  ["Greater than 40 mmHg", "Less than 10 mmHg", "Exactly 4 mmHg", "Greater than 100 mmHg"], 0,
  "IOC: ERCP + manometry — >40 mmHg. (Book p286)")
q(286, S2, "Type I sphincter of Oddi dysfunction (Milwaukee classification) is:",
  ["Biliary pain, CBD dilatation and enzyme derangement", "Biliary pain only", "Pain with CBD dilatation only", "Enzyme derangement only"], 0,
  "Milwaukee classification: Type I — biliary pain +, CBD dilatation +, enzyme derangement. (Book p286)")
q(286, S2, "Type II sphincter of Oddi dysfunction (Milwaukee classification) is:",
  ["Pain plus CBD dilatation", "Biliary pain only", "Pain, dilatation and enzyme derangement", "Only enzyme derangement"], 0,
  "Milwaukee classification: Type 2 — pain + CBD dilatation. (Book p286)")
q(286, S2, "Type III sphincter of Oddi dysfunction (Milwaukee classification) is:",
  ["Biliary pain alone", "Biliary pain with CBD dilatation", "Pain with enzyme derangement", "Only CBD dilatation"], 0,
  "Milwaukee classification: Type 3 — biliary pain. (Book p286)")

# ------------------------------------------------------------------ p287
S3 = "Acute Pancreatitis: Causes and Pathophysiology"
q(287, S3, "The most common cause of acute pancreatitis is:",
  ["Gall stones", "Alcohol", "Trauma", "Scorpion bite"], 0,
  "Causes: gall stones — m/c. (Book p287)")
q(287, S3, "The second most common cause of acute pancreatitis is:",
  ["Alcohol", "Gall stones", "Hypertriglyceridaemia", "Post-ERCP"], 0,
  "Causes: alcohol — 2nd m/c. (Book p287)")
q(287, S3, "The most common cause of acute pancreatitis in children is:",
  ["Trauma", "Alcohol", "Gall stones", "Drug induced"], 0,
  "Causes: due to trauma — m/c cause in children. (Book p287)")
q(287, S3, "Iatrogenic acute pancreatitis is commonly seen after:",
  ["ERCP", "Cholecystectomy", "Appendectomy", "Cataract surgery"], 0,
  "Causes: iatrogenic — post-ERCP (endoscopic retrograde cholangio pancreatiocography). (Book p287)")
q(287, S3, "The risk of pancreatitis after ERCP is:",
  ["5%", "50%", "1%", "90%"], 0,
  "Iatrogenic: ERCP — 5% risk of pancreatitis. (Book p287)")
q(287, S3, "The risk of post-ERCP pancreatitis is higher when:",
  ["The procedure is therapeutic rather than diagnostic", "The procedure is diagnostic only", "The patient is male", "Cannulation is easy"], 0,
  "ERCP: therapeutic > diagnostic; females > males; difficult cannulation. (Book p287)")
q(287, S3, "Post-ERCP pancreatitis occurs more commonly in:",
  ["Females than males", "Males than females", "Children than adults", "Both sexes equally"], 0,
  "ERCP: females > males. (Book p287)")
q(287, S3, "Which of the following is a cause of drug-induced pancreatitis?",
  ["Thiazide diuretics", "Paracetamol", "Aspirin", "Amitriptyline"], 0,
  "Drug induced pancreatitis: thiazide diuretics, anti retroviral drugs, chemotherapeutic agents. (Book p287)")
q(287, S3, "Which of the following is a listed cause of acute pancreatitis?",
  ["Scorpion bite", "Common cold", "Tonsillitis", "Conjunctivitis"], 0,
  "Causes include: hyperparathyroidism/hypercalcaemia, raised triglycerides, pancreas divisum, idiopathic, scorpion bite. (Book p287)")
q(287, S3, "The co-localisation theory of acute pancreatitis pathophysiology proposes that:",
  ["Zymogens are activated inside the pancreas and destroy it", "Zymogens are activated in the duodenum normally", "Lysosomes digest the acinar cells directly", "Calcium prevents enzyme activation"], 0,
  "Pathophysiology: pathology — zymogens activated inside the pancreas destroy the pancreas, causing pancreatitis (normally zymogens reach the duodenum and are activated there). (Book p287)")
q(287, S3, "In the pathogenesis of pancreatitis, a pathologic stimulus causes a sustained rise in which ion, activating PKC and NF-KB?",
  ["Calcium (Ca2+)", "Sodium", "Potassium", "Magnesium"], 0,
  "Pathogenesis diagram: pathologic stimulus — sustained rise in Ca2+ and PKC activation — NF-KB activation — co-localisation of zymogen and lysosome. (Book p287)")
q(287, S3, "Inflammatory mediators released in acute pancreatitis include:",
  ["IL-1, IL-6, IL-10 and TNF-alpha", "Only histamine", "Only serotonin", "Only cortisol"], 0,
  "Pathogenesis: release of inflammatory mediators IL-1, 6, 10, TNF-alpha — systemic inflammation. (Book p287)")
q(287, S3, "Bile reflux in acute pancreatitis is due to:",
  ["A gall stone", "A Phrygian cap", "Vagotomy", "Cholecystectomy"], 0,
  "Bile reflux: d/t gall stone — inflammation of pancreas. (Book p287)")
q(287, S3, "The characteristic pain of acute pancreatitis is:",
  ["Epigastric pain radiating to the back, relieved on forward bending", "Colicky periumbilical pain", "Pain relieved by defecation", "Chest pain on inspiration"], 0,
  "Clinical features: pain in epigastrium — radiates to back, relieves on forward bending. (Book p287)")
q(287, S3, "A notable feature of acute pancreatitis on examination is that:",
  ["Symptoms are out of proportion to signs", "Signs are out of proportion to symptoms", "The abdomen is always rigid", "There is always a mass"], 0,
  "Clinical features: symptoms out of proportion to signs. (Book p287)")

S4 = "Acute Pancreatitis: Signs, Diagnosis and Investigations"
q(288, S4, "Cullen's sign in acute haemorrhagic pancreatitis is:",
  ["Discoloration around the umbilicus", "Discoloration around the flanks", "Discoloration around the inguinal region", "Yellowing of the sclera"], 0,
  "Signs of acute haemorrhagic pancreatitis: 1. Cullen sign — discoloration around umbilicus. (Book p288)")
q(288, S4, "Grey Turner's sign is:",
  ["Discoloration around the flanks", "Discoloration around the umbilicus", "Discoloration around the inguinal region", "Cyanosis of the lips"], 0,
  "Signs: 2. Grey Turner sign — discoloration around flanks. (Book p288)")
q(288, S4, "Fox's sign in acute haemorrhagic pancreatitis is:",
  ["Discoloration around the inguinal region", "Discoloration around the umbilicus", "Discoloration around the flanks", "A tender right iliac fossa mass"], 0,
  "Signs: 3. Fox sign — discoloration around inguinal region. (Book p288)")
q(288, S4, "The peritonitis of severe pancreatitis is characterised by:",
  ["Deposition of chalky white material without perforation", "Free air under the diaphragm", "Fecal peritonitis", "Haemoperitoneum only"], 0,
  "Signs of severe pancreatitis: peritonitis — deposition of chalky white material, no perforation. (Book p288)")
q(288, S4, "The diagnosis of acute pancreatitis requires how many of the three diagnostic features?",
  ["2 out of 3", "1 out of 3", "All 3", "Any 2 of 5"], 0,
  "Diagnosis: 2 out of 3 features. (Book p288)")
q(288, S4, "Which of the following is one of the three diagnostic features of acute pancreatitis?",
  ["Abdominal pain consistent with acute pancreatitis", "A positive Murphy's sign", "Pneumobilia", "A WES sign"], 0,
  "Diagnosis: 1. Abdominal pain consistent with acute pancreatitis. (Book p288)")
q(288, S4, "Regarding enzymes, acute pancreatitis is diagnosed when:",
  ["Serum amylase or lipase is threefold or higher above the upper normal limit", "Serum amylase is above normal by any amount", "Serum bilirubin is raised", "Serum calcium is low"], 0,
  "Diagnosis: 2. Three fold or high elevation of serum amylase or lipase levels above upper normal limit. (Book p288)")
q(288, S4, "The third diagnostic feature of acute pancreatitis is:",
  ["A characteristic finding of pancreatitis by imaging", "A plain X-ray double bubble sign", "A positive HIDA scan", "A WES sign on USG"], 0,
  "Diagnosis: 3. Characteristic finding of pancreatitis by imaging. (Book p288)")
q(288, S4, "Compared with serum lipase, serum amylase has a:",
  ["Shorter half-life", "Longer half-life", "The same half-life", "Unpredictable half-life"], 0,
  "S. amylase and lipase table: half-life — amylase shorter, lipase longer. (Book p288)")
q(288, S4, "Serum lipase in acute pancreatitis:",
  ["Rises gradually and declines late, and is more specific", "Rises early and declines early", "Is less specific than amylase", "Does not rise at all"], 0,
  "Table: lipase — gradual rise, declines late, more specific. (Book p288)")
q(288, S4, "Serum amylase in acute pancreatitis is:",
  ["Sensitive, rising and declining early", "More specific than lipase", "Slow to rise", "Unhelpful in diagnosis"], 0,
  "Table: amylase — rises early, declines early, sensitive. (Book p288)")
q(288, S4, "A raised amylase level:",
  ["Does not predict severity", "Always predicts a fatal course", "Means surgery is needed", "Excludes other diagnoses"], 0,
  "Table: does not predict severity. (Book p288)")
q(288, S4, "In acute pancreatitis, the serum amylase rises to:",
  ["3 to 4 times normal", "50 times normal", "Never above normal", "Exactly 10 times normal"], 0,
  "Conditions with raised amylase: acute pancreatitis — 3 to 4 times normal. (Book p288)")
q(288, S4, "Which of the following is another condition with a raised amylase?",
  ["Mesenteric ischaemia", "Appendicitis", "Cholecystitis", "Hernia"], 0,
  "Conditions with raised amylase: mesenteric ischaemia, bowel perforation, salpingitis, volvulus, torsion. (Book p288)")
q(288, S4, "Which of the following is a condition associated with raised amylase?",
  ["Salpingitis", "Tonsillitis", "Asthma", "Urticaria"], 0,
  "Conditions with raised amylase: salpingitis, volvulus, torsion. (Book p288)")
q(288, S4, "The X-ray of a gasless abdomen in acute pancreatitis is a non-specific sign of:",
  ["Stunned bowel (ileus)", "Perforation", "Gallstones", "A Phrygian cap"], 0,
  "X-ray (non-specific signs): gasless abdomen; d/t ileus — stunned bowel. (Book p288)")
q(288, S4, "The colon cut off sign on X-ray is:",
  ["A dilated colonic loop with incomplete haustrations", "Air under the diaphragm", "A double bubble", "A sentinel loop"], 0,
  "X-ray: colon cut off sign — dilated colonic loop with incomplete haustrations. (Book p288)")
q(288, S4, "The sentinel loop in acute pancreatitis is:",
  ["A focal dilated proximal jejunal loop in the left upper quadrant", "A dilated colonic loop", "Free air under the diaphragm", "A double bubble sign"], 0,
  "X-ray: sentinel loop — a focal dilated proximal jejunal loop in left upper quadrant. (Book p288)")
q(289, S4, "The investigation of choice in acute pancreatitis is:",
  ["CECT", "Plain X-ray", "USG only", "HIDA scan"], 0,
  "CECT: IOC. (Book p289)")
q(289, S4, "The CECT in acute pancreatitis is done:",
  ["After 72 hours", "Within 6 hours", "Exactly at 24 hours", "After 7 days"], 0,
  "CECT: done >72 hrs. (Book p289)")
q(289, S4, "A CECT done BEFORE 72 hours in acute pancreatitis:",
  ["Underestimates the severity", "Overestimates the severity", "Is normal in all", "Shows only gallstones"], 0,
  "CECT: <72 hrs — underestimate severity. (Book p289)")
q(289, S4, "The CECT phase most sensitive for necrosis is the portal venous phase, taken:",
  ["60-70 seconds after dye injection", "10 seconds after dye injection", "5 minutes after dye injection", "Without any dye"], 0,
  "CECT: portal venous phase — 60-70 s after injection of dye; most sensitive for necrosis. (Book p289)")
q(289, S4, "Other findings in biliary acute pancreatitis include:",
  ["Liver enzymes deranged", "A normal liver profile always", "A WES sign", "Pneumobilia"], 0,
  "Other findings: liver enzymes deranged in biliary pancreatitis. (Book p289)")
q(289, S4, "Hypocalcaemia in acute pancreatitis is due to:",
  ["Saponification of fat and calcium chelation", "Vitamin D excess", "Hypoventilation", "Diuretics"], 0,
  "Other findings: hypocalcaemia — saponification of fat and Ca++ chelation. (Book p289)")

S5 = "Severity Scores in Acute Pancreatitis"
q(289, S5, "The Glasgow criteria for acute pancreatitis define acute severe pancreatitis at:",
  ["3 or more points", "1 or more points", "5 or more points", "10 or more points"], 0,
  "Severity scores: Glasgow criteria — 3 or more: acute severe pancreatitis. (Book p289)")
q(289, S5, "Ranson's criteria define acute severe pancreatitis at:",
  ["3 or more points", "1 point", "10 points", "Exactly 2 points"], 0,
  "Ranson's criteria: 3 or more — acute severe pancreatitis. (Book p289)")
q(289, S5, "Which of the following is a Ranson's criterion ON ADMISSION?",
  ["WBC greater than 16,000/microL", "Hematocrit decrease greater than 10%", "BUN increase greater than 5 mg/dL", "Base deficit greater than 4 mEq/L"], 0,
  "Ranson's on admission: WBC >16,000/microL, age >55 yrs, glucose >200 mg/dL, AST >250 IU/L, LDH >350 IU/L. (Book p289)")
q(289, S5, "Which of the following is a Ranson's criterion within 48 HOURS of admission?",
  ["Fluid needs greater than 6 L", "WBC greater than 16,000/microL", "Age greater than 55 years", "Glucose greater than 200 mg/dL"], 0,
  "Ranson's within 48 hrs: hematocrit decrease >10%, BUN increase >5 mg/dL, S. calcium <8 mg/dL, arterial PaO2 <60 mmHg, base deficit >4 mEq/L (acidosis), fluid needs >6 L. (Book p289)")
q(289, S5, "Arterial PaO2 below 60 mmHg is a Ranson's criterion:",
  ["Within 48 hours of admission", "On admission", "At discharge", "Only in children"], 0,
  "Ranson's within 48 hrs: arterial PaO2 <60 mmHg. (Book p289)")
q(289, S5, "The BISAP (bedside) score in acute pancreatitis includes:",
  ["BUN greater than 25 mg/dL", "BUN greater than 5 mg/dL", "A low WBC count", "A normal CT"], 0,
  "BISAP score (beside score): BUN >25 mg/dL. (Book p289)")
q(289, S5, "Which of the following is a component of the BISAP score?",
  ["Impaired mental status", "Impaired vision", "A positive Murphy's sign", "A Phrygian cap"], 0,
  "BISAP: BUN >25 mg/dL, impaired mental status, SIRS, age >60 yrs, pleural effusion. (Book p289)")
q(289, S5, "A BISAP score of 3 or more indicates:",
  ["Severe pancreatitis", "Mild pancreatitis", "Chronic pancreatitis", "Gallstone disease"], 0,
  "BISAP score: score 3 or more — severe pancreatitis. (Book p289)")
q(289, S5, "APACHE II stands for:",
  ["Acute physiology and chronic health evaluation", "Abdominal pain and chronic hepatitis evaluation", "Acute peritonitis and cholecystitis health index", "Assessment of pancreatitis and its complications"], 0,
  "Other scores: APACHE II — acute physiology and chronic health evaluation criteria. (Book p289)")
q(289, S5, "An APACHE II score of 8 or more indicates:",
  ["Severe pancreatitis", "Mild pancreatitis", "No pancreatitis", "Chronic pancreatitis only"], 0,
  "APACHE II: score 8 or more — severe pancreatitis. (Book p289)")
q(290, S5, "HAPS in acute pancreatitis stands for:",
  ["Harmless acute pancreatitis score", "High APACHE pancreatitis score", "Haemorrhagic acute pancreatitis scale", "Hospital acute pain score"], 0,
  "Other scores: HAPS — harmless acute pancreatitis score. (Book p290)")
q(290, S5, "A modified Marshall score of 2 or more indicates:",
  ["Severe pancreatitis", "Mild pancreatitis", "Chronic pancreatitis", "Pseudocyst"], 0,
  "Modified Marshall score: score 2 or more — severe pancreatitis. (Book p290)")
q(290, S5, "A CRP greater than 150 mg/L indicates:",
  ["Severe pancreatitis", "Mild pancreatitis", "Gallstones", "Cholecystitis"], 0,
  "CRP: >150 mg/L — severe pancreatitis. (Book p290)")
q(290, S5, "The CT severity index is made of:",
  ["Balthazar grade plus pancreatic necrosis score (total 10)", "Glasgow plus Ranson's", "BISAP plus CRP", "APACHE II only"], 0,
  "CT severity index: Balthazar grade table plus pancreatic necrosis table — total 10. (Book p290)")
q(290, S5, "In the Balthazar grade, a normal pancreas scores:",
  ["0", "1", "2", "3"], 0,
  "Balthazar grade: normal pancreas — 0. (Book p290)")
q(290, S5, "In the Balthazar grade, focal or diffuse enlargement scores:",
  ["1", "0", "2", "3"], 0,
  "Balthazar grade: focal or diffuse enlargement — 1. (Book p290)")
q(290, S5, "In the Balthazar grade, pancreatic gland abnormalities with peripancreatic inflammation score:",
  ["2", "1", "3", "4"], 0,
  "Balthazar grade: pancreatic gland abnormalities, peripancreatic inflammation — 2. (Book p290)")
q(290, S5, "In the Balthazar grade, fluid collection in a single location scores:",
  ["3", "2", "1", "4"], 0,
  "Balthazar grade: fluid collection in a single location — 3. (Book p290)")
q(290, S5, "In the Balthazar grade, 2 or more fluid collections and/or gas bubbles in or adjacent to the pancreas score:",
  ["4", "3", "2", "0"], 0,
  "Balthazar grade: 2+ fluid collections and/or gas bubbles in or adjacent to pancreas — 4. (Book p290)")
q(290, S5, "In the CT severity index, necrosis of one third of the pancreas scores:",
  ["2", "0", "4", "6"], 0,
  "Pancreatic necrosis table: 1/3rd of pancreas — 2. (Book p290)")
q(290, S5, "In the CT severity index, necrosis of more than half of the pancreas scores:",
  ["6", "4", "2", "0"], 0,
  "Pancreatic necrosis table: >1/2 of pancreas — 6. (Book p290)")
q(290, S5, "The CT severity index calls a case severe at a total score of:",
  ["6 or more (out of 10)", "3 or more", "8 or more", "10 only"], 0,
  "CT severity index: total 10; 6 or more — severe. (Book p290)")

# ------------------------------------------------------------------ p290
S6 = "Management of Acute Pancreatitis"
q(290, S6, "The initial management of acute pancreatitis includes:",
  ["Nil per oral, IV fluids, analgesia", "Immediate cholecystectomy", "Immediate ERCP in all", "Early feeding in all"], 0,
  "Management: nil per oral (NPO), IV fluids, analgesia. (Book p290)")
q(290, S6, "The fluid of choice in acute pancreatitis is:",
  ["Ringer's lactate", "Dextrose 5%", "Hartmann's solution only", "Normal saline only"], 0,
  "Management: IV fluids — RL, fluid of choice. (Book p290)")
q(290, S6, "Analgesia in acute pancreatitis is given to:",
  ["Reduce the pain, with opioids used if uncontrolled", "Reduce the amylase", "Prevent necrosis", "Reverse the ileus"], 0,
  "Management: analgesia — to decrease pain; opioids can be used if uncontrolled. (Book p290)")
q(290, S6, "Antibiotics in acute pancreatitis are indicated in:",
  ["Severe pancreatitis and infected necrosis", "Every mild attack", "Every post-ERCP patient", "Only in children"], 0,
  "Management — antibiotics: indications — severe pancreatitis, infected necrosis. (Book p290)")
q(290, S6, "The IV antibiotic of choice in acute pancreatitis is:",
  ["Meropenem", "Oral amoxicillin", "Intramuscular penicillin", "Topical neomycin"], 0,
  "Management: IV antibiotic of choice — meropenem. (Book p290)")
q(290, S6, "In the nutrition of acute pancreatitis, the book's preferred route is:",
  ["Enteral nutrition, initiated early", "Long-term TPN in all", "No nutrition until one month", "Oral diet immediately"], 0,
  "Nutrition: total parenteral nutrition (initial phase, in severe cases) leads to enteral nutrition — initiated early, preferred nasojejunal tube. (Book p290)")
q(290, S6, "Enteral nutrition initiated early in acute pancreatitis:",
  ["Reduces mortality", "Increases mortality", "Has no effect", "Worsens the pancreatitis"], 0,
  "Nutrition: enteral nutrition initiated early — decreases mortality. (Book p290)")
q(290, S6, "Inadequate nutrition in acute pancreatitis leads to:",
  ["Leaky gut bacteria and infections", "A normal gut", "Increased immunity", "Faster recovery"], 0,
  "Nutrition: decreased nutrition — leaky gut bacteria, infections. (Book p290)")
q(290, S6, "The preferred tube for enteral nutrition in acute pancreatitis is the:",
  ["Nasojejunal tube", "Nasogastric tube", "Gastrostomy", "Jejunal stoma"], 0,
  "Nutrition: preferred — nasojejunal tube. (Book p290)")
q(290, S6, "An indication for ERCP and sphincterotomy in acute pancreatitis is:",
  ["A documented CBD stone", "A normal CBD", "Mild pain only", "A Phrygian cap"], 0,
  "ERCP and sphincterotomy: indications — documented CBD stone, biliary pancreatitis, symptoms >48 hrs, jaundice. (Book p290)")
q(290, S6, "ERCP and sphincterotomy are indicated in acute pancreatitis when symptoms last:",
  ["More than 48 hours", "Less than 6 hours", "Only at 1 week", "Never"], 0,
  "ERCP and sphincterotomy: indications — symptoms >48 hrs. (Book p290)")
q(290, S6, "In gall stone induced acute pancreatitis, cholecystectomy is done:",
  ["Before discharge", "Only after one year", "Never", "Only if there is jaundice"], 0,
  "Cholecystectomy: in gall stone induced pancreatitis, before discharge. (Book p290)")

# ------------------------------------------------------------------ p291
S7 = "Complications of Acute Pancreatitis"
q(291, S7, "In the Atlanta classification, moderate acute pancreatitis is:",
  ["Local complications without systemic complications", "No local or systemic complications", "Both local and systemic complications", "Only systemic complications"], 0,
  "Atlanta classification: moderate — local (+), systemic (−). (Book p291)")
q(291, S7, "In the Atlanta classification, severe acute pancreatitis has:",
  ["Both local and systemic complications", "Only local complications", "Only systemic complications", "Neither"], 0,
  "Atlanta classification: severe — local (+), systemic (+). (Book p291)")
q(291, S7, "A LOCAL complication of acute pancreatitis is:",
  ["Pseudocyst", "ARDS", "Sepsis", "SIRS"], 0,
  "Local: pseudocyst, necrosis, pseudoaneurysm of splenic artery, splenic vein thrombosis, left pleural effusion. (Book p291)")
q(291, S7, "The most common vessel involved in a pseudoaneurysm after acute pancreatitis is the:",
  ["Splenic artery", "Hepatic artery", "Gastroduodenal artery only", "Coeliac trunk"], 0,
  "Local: pseudoaneurysm of splenic artery — m/c vessel involved. (Book p291)")
q(291, S7, "A pseudoaneurysm of the splenic artery after pancreatitis is managed by:",
  ["Ligation or embolization", "Observation only", "Total pancreatectomy", "Antibiotics only"], 0,
  "Pseudoaneurysm of splenic artery: Mx — ligation/embolization. (Book p291)")
q(291, S7, "Splenic vein thrombosis after acute pancreatitis causes:",
  ["Left sided (sinistral) portal hypertension", "Generalized portal hypertension", "Budd-Chiari syndrome", "Mesenteric venous obstruction only"], 0,
  "Local: splenic vein thrombosis — left sided portal HTN aka sinistral portal HTN. (Book p291)")
q(291, S7, "Sinistral portal hypertension presents with:",
  ["Upper GI bleeding", "Isolated lower limb oedema", "Jaundice only", "A Phrygian cap"], 0,
  "Sinistral portal HTN: C/F — upper GI bleeding. (Book p291)")
q(291, S7, "Sinistral portal hypertension after pancreatitis is managed by:",
  ["Splenectomy", "Portosystemic shunt", "TIPS only", "Observation"], 0,
  "Sinistral portal HTN: Mx — splenectomy. (Book p291)")
q(291, S7, "Which of the following is a local complication of acute pancreatitis?",
  ["Left pleural effusion", "MODS", "SIRS", "Sepsis"], 0,
  "Local: left pleural effusion. (Book p291)")
q(291, S7, "The most common cause of EARLY death in acute pancreatitis is:",
  ["MODS (multiple organ dysfunction syndrome)", "Bleeding", "Pneumonia", "DVT"], 0,
  "Systemic: MODS — m/c cause of early death. (Book p291)")
q(291, S7, "The most common cause of death in acute pancreatitis is:",
  ["SIRS", "MODS", "ARDS", "Sepsis only"], 0,
  "Systemic: SIRS — m/c cause of death. (Book p291)")
q(291, S7, "A homogeneous collection LESS than 4 weeks old with no fully definable wall in pancreatitis is:",
  ["An acute peripancreatic collection", "A pseudocyst", "Walled-off necrosis", "An acute necrotic collection"], 0,
  "Terminologies table: <4 weeks, no fully definable wall — homogeneous: acute peripancreatic collection. (Book p291)")
q(291, S7, "A heterogeneous collection LESS than 4 weeks old with no fully definable wall is:",
  ["An acute necrotic collection", "A pseudocyst", "Walled-off necrosis", "A mucinous neoplasm"], 0,
  "Terminologies table: <4 weeks — heterogeneous: acute necrotic collection. (Book p291)")
q(291, S7, "A homogeneous collection MORE than 4 weeks old with a well-defined wall is:",
  ["A pseudocyst", "An acute peripancreatic collection", "Walled-off necrosis", "A retention cyst"], 0,
  "Terminologies table: >4 wks, well-defined wall — homogeneous: pseudocyst. (Book p291)")
q(291, S7, "A heterogeneous collection MORE than 4 weeks old with a well-defined wall is:",
  ["Walled-off necrosis", "A pseudocyst", "An acute necrotic collection", "An acute peripancreatic collection"], 0,
  "Terminologies table: >4 wks, well-defined wall — heterogeneous: walled-off necrosis. (Book p291)")
q(291, S7, "A small amount of collection on CECT after pancreatitis is managed by:",
  ["Conservative management", "Immediate surgery", "Immediate drainage", "Antibiotics only"], 0,
  "Mx: small amount of collection in CECT — conservative Mx. (Book p291)")
q(291, S7, "A symptomatic and large pancreatic collection is managed by:",
  ["Pigtail catheter and drainage", "Total pancreatectomy", "Observation only", "Open drainage in all"], 0,
  "Mx: symptomatic and large — pigtail catheter and drainage. (Book p291)")
q(291, S7, "Pancreatic ascites results from:",
  ["Disruption of the pancreatic duct", "Cirrhosis only", "Nephrotic syndrome", "Heart failure only"], 0,
  "Pancreatic ascites: disruption of pancreatic duct. (Book p291)")
q(291, S7, "The fluid in pancreatic ascites is:",
  ["Amylase and protein rich turbid fluid", "Clear straw-coloured fluid with low amylase", "Purulent with low protein", "Sanguineous with normal amylase"], 0,
  "Pancreatic ascites: significant abdominal distension with intra-abdominal fluid, amylase and protein rich turbid fluid. (Book p291)")
q(291, S7, "Pancreatic ascites is managed by:",
  ["Paracentesis with a pigtail catheter", "Observation only", "Cholecystectomy", "Whipple's surgery"], 0,
  "Pancreatic ascites Mx: paracentesis (with pigtail catheter). (Book p291)")
q(291, S7, "Octreotide / somatostatin in pancreatic ascites is used to:",
  ["Decrease secretions", "Increase bile flow", "Dissolve the ascites", "Prevent infection"], 0,
  "Pancreatic ascites Mx: octreotide/somatostatin — decrease secretions; also stent placement. (Book p291)")

# ------------------------------------------------------------------ p292
S8 = "Pancreatic Necrosis"
q(292, S8, "On CT, pancreatic necrosis is:",
  ["Heterogeneous, with gas bubbles suggesting infection", "Homogeneous and smooth", "Always hyperdense", "Normal in all"], 0,
  "Pancreatic necrosis CT: heterogeneous; gas bubbles (+) — infected. (Book p292)")
q(292, S8, "Sterile pancreatic necrosis is managed by:",
  ["No intervention", "Immediate open debridement", "Total pancreatectomy", "Antibiotics only"], 0,
  "Necrosis: sterile — no intervention. (Book p292)")
q(292, S8, "An indication for intervention in pancreatic necrosis is:",
  ["Persistent pain", "A normal CT", "Mild epigastric discomfort", "A normal amylase"], 0,
  "Mx: indication for intervention — persistent pain. (Book p292)")
q(292, S8, "Another indication for intervention in pancreatic necrosis is:",
  ["Failure to improve clinically with conservative management", "A normal clinical course", "Mild nausea", "A normal CRP"], 0,
  "Indication for intervention: failure to improve clinically with conservative management. (Book p292)")
q(292, S8, "Yet another indication for intervention in pancreatic necrosis is:",
  ["Symptomatic biliary or enteric obstruction", "Asymptomatic course", "A small pseudocyst", "A Phrygian cap"], 0,
  "Indication for intervention: symptomatic biliary/enteric obstruction. (Book p292)")
q(292, S8, "Sterile pancreatic necrosis that needs intervention has a prognosis that is:",
  ["Better", "Worse than infected necrosis", "Always fatal", "Unpredictable only"], 0,
  "Prognosis: sterile — better. (Book p292)")
q(292, S8, "Features of INFECTED pancreatic necrosis include:",
  ["Fever, raised TLC and raised CRP with gas bubbles on CT", "A normal temperature and normal CRP", "Absence of gas on CT with normal TLC", "Only weight gain"], 0,
  "Infected: fever (+), raised TLC, raised CRP, CT — gas bubbles. (Book p292)")
q(292, S8, "The management of infected pancreatic necrosis follows the:",
  ["Step-up approach", "One-step open necrosectomy only", "Observation only", "Antibiotics only"], 0,
  "Infected: step-up approach. (Book p292)")
q(292, S8, "The first step of the step-up approach in infected pancreatic necrosis is:",
  ["Percutaneous drainage with a pigtail catheter", "Open debridement", "Total pancreatectomy", "ERCP only"], 0,
  "Step-up approach: percutaneous drainage with pigtail catheter. (Book p292)")
q(292, S8, "If percutaneous drainage is unsuccessful in infected pancreatic necrosis, the next step is:",
  ["Minimally invasive retroperitoneal debridement", "Observation", "Cholecystectomy", "Antibiotics alone"], 0,
  "Step-up approach: unsuccessful — minimally invasive retroperitoneal debridement. (Book p292)")
q(292, S8, "Infected pancreatic necrosis carries:",
  ["High mortality", "No mortality", "Mortality only in children", "Low mortality overall"], 0,
  "Infected necrosis: high mortality. (Book p292)")
q(292, S8, "Beger's method for infected necrosis involves:",
  ["Continuous irrigation and drainage of saline through both tubes", "A single drain without irrigation", "Antibiotics only", "Total pancreatectomy in all"], 0,
  "Beger's method for Mx of infected necrosis: high mortality; continuous irrigation and drainage of saline through both tubes. (Book p292)")

# ------------------------------------------------------------------ p292-294
S9 = "Pseudocyst"
q(292, S9, "A pancreatic pseudocyst is lined by:",
  ["Granulation tissue", "Mature squamous epithelium", "Columnar epithelium", "No lining at all, by definition"], 0,
  "Pseudocyst: lined by granulation tissue. (Book p292)")
q(292, S9, "The most common site of a pancreatic pseudocyst is:",
  ["The lesser sac", "The free peritoneal cavity", "The retroperitoneum only", "The gallbladder fossa"], 0,
  "Pseudocyst: site — lesser sac (m/c), abdomen. (Book p292)")
q(292, S9, "The clinical features of a pancreatic pseudocyst include:",
  ["Epigastric lump, nausea and vomiting, with a history of acute pancreatitis or recurrent attacks", "Painless jaundice", "Obstipation", "Reynold's pentad"], 0,
  "Clinical features: epigastric lump, nausea and vomiting, H/o acute pancreatitis/recurrent attacks in the past. (Book p292)")
q(292, S9, "Pancreatic pseudocysts are more common in:",
  ["Chronic pancreatitis", "Acute cholecystitis", "Gastric ulcers", "Colitis"], 0,
  "Pseudocyst: more common in chronic pancreatitis. (Book p292)")
q(293, S9, "The investigation of choice for a pancreatic pseudocyst is:",
  ["CECT", "Plain X-ray", "USG alone", "HIDA scan"], 0,
  "Diagnosis: CECT — IOC. (Book p293)")
q(293, S9, "In the D'Esio classification, Type I pseudocyst occurs in:",
  ["Acute pancreatitis with normal ductal anatomy and no ductal communication", "Chronic pancreatitis with strictures", "Acute on chronic pancreatitis", "Only in trauma"], 0,
  "D'Esio classification: Type I — acute pancreatitis, normal ductal anatomy, no ductal communication/fistula. (Book p293)")
q(293, S9, "In the D'Esio classification, Type II pseudocyst is:",
  ["Acute on chronic pancreatitis with abnormal duct anatomy without strictures", "Chronic pancreatitis with strictures communicating with the duct", "Acute pancreatitis with a normal duct", "Only post-traumatic"], 0,
  "D'Esio classification: Type 2 — acute on chronic pancreatitis, abnormal duct anatomy without strictures. (Book p293)")
q(293, S9, "In the D'Esio classification, Type III pseudocyst is:",
  ["Chronic pancreatitis with abnormal duct anatomy with strictures, communicating with the duct, appearing as a retention cyst", "Acute pancreatitis with a normal duct", "Acute on chronic pancreatitis", "Only in children"], 0,
  "D'Esio classification: Type 3 — chronic pancreatitis, abnormal anatomy of duct with strictures, communicating with duct, appears as retention cyst. (Book p293)")
q(293, S9, "The usual course of a pancreatic pseudocyst is that it:",
  ["Resolves spontaneously", "Always needs surgery", "Malignant transforms", "Never resolves"], 0,
  "Management: resolves spontaneously. (Book p293)")
q(293, S9, "An indication for intervention for a pseudocyst is a size of:",
  ["More than 6 cm", "More than 1 cm", "More than 2 cm", "More than 10 cm"], 0,
  "Indication for intervention: size >6 cm. (Book p293)")
q(293, S9, "An indication for intervention for a pseudocyst is a duration of:",
  ["More than 6 weeks", "More than 1 week", "More than 3 months", "More than 1 day"], 0,
  "Indication for intervention: duration >6 weeks. (Book p293)")
q(293, S9, "An indication for intervention for a pseudocyst is a wall thickness of:",
  ["More than 6 mm", "More than 1 mm", "More than 10 mm", "More than 2 mm"], 0,
  "Indication for intervention: wall thickness >6 mm. (Book p293)")
q(293, S9, "External drainage of a pseudocyst is indicated in:",
  ["An infected pseudocyst", "A small asymptomatic pseudocyst", "A Type I pseudocyst always", "A retention cyst only"], 0,
  "Intervention — external drainage: indications — infected pseudocyst, hemorrhage inside cyst. (Book p293)")
q(293, S9, "External drainage of a pseudocyst is also indicated when there is:",
  ["Hemorrhage inside the cyst", "A normal amylase", "A thin wall", "A small size"], 0,
  "External drainage: indications — hemorrhage inside cyst. (Book p293)")
q(293, S9, "The principle of external drainage of a pseudocyst is:",
  ["Drainage with a pigtail catheter", "Open cystgastrostomy", "Total pancreatectomy", "ERCP with stenting only"], 0,
  "External drainage: principles — drainage with pigtail catheter. (Book p293)")
q(293, S9, "If a pseudocyst communicates with the duct, the resulting complication is:",
  ["A pancreatic fistula", "A splenic pseudoaneurysm", "A WES sign", "Bouveret syndrome"], 0,
  "External drainage: rule out communication with duct — pancreatic fistula. (Book p293)")
q(293, S9, "A pancreatic fistula is managed by:",
  ["A stent in the duct, with or without external drainage", "Total pancreatectomy", "Cholecystectomy", "Observation only"], 0,
  "Pancreatic fistula: Mx — stent in duct with/without external drainage. (Book p293)")
q(293, S9, "Internal drainage of a pseudocyst is done by:",
  ["Cystojejunostomy or cystogastrostomy", "Pigtail drainage", "ERCP", "Cholecystectomy"], 0,
  "Intervention — internal drainage: cystojejunostomy, cystogastrostomy. (Book p293)")
q(293, S9, "Internal drainage of a pseudocyst can be done by all of the following EXCEPT:",
  ["Open or laparoscopic or endoscopic/natural orifice transluminal (NOTES) surgery", "A percutaneous pigtail catheter", "Cystogastrostomy", "Cystojejunostomy"], 0,
  "Internal drainage: open surgery, laparoscopic, endoscopy/natural orifice transluminal endoscopic Sx (NOTES). (Book p293)")
q(294, S9, "The most common complication of a pancreatic pseudocyst is:",
  ["Infection", "Rupture", "Diabetes", "Jaundice only"], 0,
  "Complications: infection — m/c. (Book p294)")
q(294, S9, "Hemorrhage as a complication of a pseudocyst is most commonly due to:",
  ["Pseudocyst surgery", "Cholecystectomy", "ERCP", "Appendicitis"], 0,
  "Complications: hemorrhage — m/c due to pseudocyst surgery. (Book p294)")
q(294, S9, "Which of the following is a complication of a pancreatic pseudocyst?",
  ["Pancreatico-pleural fistula", "A Phrygian cap", "A WES sign", "Rigler's triad"], 0,
  "Complications: rupture of cyst, pancreatico-pleural fistula. (Book p294)")
q(294, S9, "A differential diagnosis of a pancreatic pseudocyst is:",
  ["A mucinous cystic neoplasm", "A Phrygian cap", "A porcelain gallbladder", "Duodenal atresia"], 0,
  "D/d: mucinous cystic neoplasm. (Book p294)")
q(294, S9, "Compared with a pseudocyst, a mucinous neoplasm has:",
  ["A raised CEA and a thick wall", "A normal CEA and a thinner wall", "A lower amylase", "No wall at all"], 0,
  "D/d table: mucinous neoplasm — raised CEA, thick walled; pseudocyst — normal CEA, thinner than neoplasm. (Book p294)")

# ------------------------------------------------------------------ p294-296
S10 = "Chronic Pancreatitis"
q(294, S10, "Chronic pancreatitis is defined by:",
  ["Fibrosis and chronic inflammation causing irreversible damage to the pancreatic parenchyma", "A reversible inflammatory attack", "Gallstones only", "A single bout of acute pain"], 0,
  "Chronic pancreatitis: fibrosis and chronic inflammation — irreversible damage to pancreatic parenchyma. (Book p294)")
q(294, S10, "The TIGAR-O classification of chronic pancreatitis causes stands for:",
  ["Toxins, idiopathic, genetic, autoimmune, recurrent, obstructive", "Toxins, infection, granulomatous, autoimmune, recurrent, obstructive",
   "Trauma, idiopathic, genetic, alcohol, recurrent, obstructive", "Toxins, immunology, genetic, atresia, recurrent, obstruction"], 0,
  "Causes: TIGAR-O classification — toxins, idiopathic, genetic, autoimmune, recurrent, obstructive. (Book p294)")
q(294, S10, "The most common toxic cause of chronic pancreatitis is:",
  ["Alcohol", "Cigarette smoking", "Hypercalcaemia", "Chronic renal failure"], 0,
  "TIGAR-O — toxins: alcohol (m/c), cigarette smoking, hypercalcaemia, chronic renal failure. (Book p294)")
q(294, S10, "Which genetic mutations are listed under the genetic cause of chronic pancreatitis?",
  ["PRSS1, CFTR and SPINK1 mutations", "BRCA1 and BRCA2", "APC and MSH2", "CFTR alone"], 0,
  "TIGAR-O — genetic: PRSS1, CFTR, SPINK1 mutation. (Book p294)")
q(294, S10, "The autoimmune cause of chronic pancreatitis is:",
  ["IgG4 mediated, causing fibrosis", "ANA mediated", "Anti-smooth muscle antibody only", "HLA B27 related"], 0,
  "TIGAR-O — autoimmune: IgG4 mediated, causes fibrosis. (Book p294)")
q(294, S10, "A recurrent cause of chronic pancreatitis is:",
  ["Post necrotic (severe acute pancreatitis), recurrent acute pancreatitis and vascular diseases", "Alcohol only", "A Phrygian cap", "A single attack of pancreatitis"], 0,
  "TIGAR-O — recurrent: post necrotic (severe acute pancreatitis), recurrent acute pancreatitis, vascular diseases. (Book p294)")
q(294, S10, "An obstructive cause of chronic pancreatitis is:",
  ["Gall stones, pancreas divisum and pancreatic duct scars", "Alcohol", "Cigarette smoking", "Autoimmune disease"], 0,
  "TIGAR-O — obstructive: gall stones, pancreas divisum, pancreatic duct scars. (Book p294)")
q(295, S10, "The PRSS1 gene is:",
  ["Located on chromosome 7 and raises the risk of hereditary chronic pancreatitis", "Located on chromosome 11", "A tumour suppressor of the liver", "Associated with cassava only"], 0,
  "Genes associated: PRSS1 — located on chromosome 7, raised risk of hereditary chronic pancreatitis. (Book p295)")
q(295, S10, "The SPINK1 gene is seen in:",
  ["Tropical calcific pancreatitis", "Hereditary pancreatitis only", "Acute cholecystitis", "Duodenal atresia"], 0,
  "SPINK1: seen in tropical calcific pancreatitis. (Book p295)")
q(295, S10, "SPINK1 is secreted by which cells, and what does it regulate?",
  ["Acinar cells, regulating premature activation of trypsinogen", "Ductal cells, regulating bile", "Islet cells, regulating insulin", "Gastric parietal cells"], 0,
  "SPINK1: secreted by acinar cells — regulates premature activation of trypsinogen. (Book p295)")
q(295, S10, "SPINK1 is associated with ingestion of:",
  ["Cassava", "Tamarind", "Cassia", "Cashew"], 0,
  "SPINK1: associated with cassava ingestion. (Book p295)")
q(295, S10, "The SPINK1 mutation also:",
  ["Raises the risk of cancer", "Prevents cancer", "Cures pancreatitis", "Lowers amylase"], 0,
  "SPINK1: raised risk of cancer. (Book p295)")
q(295, S10, "The clinical features of chronic pancreatitis are seen after destruction of:",
  ["80-90% of the pancreas", "10% of the pancreas", "50% of the pancreas", "The whole pancreas only"], 0,
  "Clinical features: features seen after 80-90% destruction of pancreas. (Book p295)")
q(295, S10, "In chronic pancreatitis, which deficiency is more common?",
  ["Exocrine deficiency", "Endocrine deficiency", "Both equally", "Neither"], 0,
  "Clinical features: exocrine deficiency more common. (Book p295)")
q(295, S10, "Exocrine deficiency in chronic pancreatitis is caused by:",
  ["Decreased pancreatic enzymes", "Decreased insulin", "Increased bile", "Increased gastrin"], 0,
  "Table: exocrine deficiency caused d/t pancreatic enzymes decreased. (Book p295)")
q(295, S10, "Features of exocrine deficiency in chronic pancreatitis include:",
  ["Malabsorption, steatorrhoea, diarrhoea and weight loss", "Diabetes", "Hypertension", "Pneumobilia"], 0,
  "Table — exocrine features: malabsorption, steatorrhoea, diarrhoea, weight loss. (Book p295)")
q(295, S10, "A test for exocrine deficiency in chronic pancreatitis is:",
  ["Decreased fecal elastase with increased fecal fat and NBT PABA", "Blood glucose only", "HbA1c only", "Serum calcium only"], 0,
  "Table — exocrine tests: raised fecal fat, decreased fecal elastase, NBT PABA. (Book p295)")
q(295, S10, "Exocrine deficiency in chronic pancreatitis is treated with:",
  ["Exogenous enzyme replacement and PPI", "Insulin", "Oral hypoglycemics", "Antibiotics"], 0,
  "Table — exocrine Mx: exogenous enzyme replacement, PPI. (Book p295)")
q(295, S10, "Endocrine deficiency in chronic pancreatitis is caused by:",
  ["Decreased insulin", "Decreased pancreatic enzymes", "Increased bile acids", "Increased glucagon only"], 0,
  "Table: endocrine deficiency caused d/t insulin decreased. (Book p295)")
q(295, S10, "The feature of endocrine deficiency in chronic pancreatitis is:",
  ["Diabetes", "Steatorrhoea", "Malabsorption", "Jaundice only"], 0,
  "Table — endocrine features: diabetes. (Book p295)")
q(295, S10, "Tests for endocrine deficiency in chronic pancreatitis include:",
  ["Blood glucose and HbA1c", "Fecal elastase", "NBT PABA", "Serum amylase"], 0,
  "Table — endocrine tests: blood glucose, HbA1c. (Book p295)")
q(295, S10, "Endocrine deficiency in chronic pancreatitis is treated with:",
  ["Oral hypoglycaemic agents and insulin", "Exogenous enzymes", "PPI", "Antibiotics"], 0,
  "Table — endocrine Mx: oral hypoglycaemic agents, insulin. (Book p295)")
q(295, S10, "The pain of chronic pancreatitis is caused by:",
  ["Fibrosis and ineffective drainage due to scars, strictures or stones in the main pancreatic duct", "Gallstones in the gallbladder", "Appendicitis", "Diverticulitis"], 0,
  "Table — pain: fibrosis, ineffective drainage d/t scars/strictures/stones (CaCO3) in major pancreatic duct. (Book p295)")
q(295, S10, "The feature of the pain component of chronic pancreatitis is:",
  ["Intractable pain", "Colicky pain relieved by eating", "Pain only at night", "No pain"], 0,
  "Table — pain features: intractable pain. (Book p295)")
q(295, S10, "The investigation of choice in chronic pancreatitis is:",
  ["MRCP with secretin stimulation", "USG alone", "Plain X-ray", "HIDA scan"], 0,
  "Investigations: MRCP with secretin stimulation — IOC. (Book p295)")
q(295, S10, "In chronic pancreatitis, MRCP with secretin stimulation shows:",
  ["Ineffective drainage due to stones and a dilated main pancreatic duct", "A normal duct in all", "Only gallstones", "Pneumobilia"], 0,
  "MRCP with secretin stimulation: ineffective drainage d/t stones, dilated main pancreatic duct. (Book p295)")
q(295, S10, "The gold standard investigation in chronic pancreatitis is:",
  ["ERCP", "USG", "CECT", "MRCP"], 0,
  "Investigations: ERCP — gold standard. (Book p295)")
q(295, S10, "EUS in chronic pancreatitis is assessed by:",
  ["The Rosemont criteria", "The Rosewood score", "The Tokyo guidelines", "The Ranson's criteria"], 0,
  "Investigations: EUS — Rosemont criteria. (Book p295)")
q(295, S10, "The MRCP appearance of a dilated, beaded main pancreatic duct in chronic pancreatitis is called:",
  ["Chain of lakes", "Double bubble", "Sentinel loop", "Seagull sign"], 0,
  "MRCP figure: chain of lakes in MRCP. (Book p295)")

S11 = "Management of Pain in Chronic Pancreatitis"
q(296, S11, "The first step in managing pain in chronic pancreatitis is:",
  ["Analgesics", "Puestow's procedure", "Distal pancreatectomy", "ERCP with sphincterotomy"], 0,
  "Management of pain: analgesics. (Book p296)")
q(296, S11, "If pain in chronic pancreatitis responds to analgesics, the next step is:",
  ["No intervention", "Drainage surgery", "Resection surgery", "ERCP"], 0,
  "Management of pain: responds — no intervention. (Book p296)")
q(296, S11, "If pain in chronic pancreatitis stops responding to analgesics, the approach is:",
  ["Intervention — drainage or resection", "Observation only", "More of the same analgesic", "Cholecystectomy"], 0,
  "Management of pain: stops responding — intervention (drainage, resection). (Book p296)")
q(296, S11, "In drainage of painful chronic pancreatitis, if the main pancreatic duct diameter is LESS than 5-6 mm, the procedure is:",
  ["ERCP with sphincterotomy", "Puestow's procedure", "Duval procedure", "Beger's procedure"], 0,
  "Drainage: diameter of main pancreatic duct <5-6 mm — ERCP + sphincterotomy. (Book p296)")
q(296, S11, "In drainage of painful chronic pancreatitis, if the main pancreatic duct is GREATER than 5-6 mm, which procedure is listed?",
  ["Puestow's procedure", "Beger's procedure", "Distal pancreatectomy", "Whipple's surgery"], 0,
  "Drainage: >5-6 mm — Puestow's and Duval. (Book p296)")
q(296, S11, "Puestow's procedure is:",
  ["A longitudinal pancreaticojejunostomy", "An end-to-end pancreaticojejunostomy", "A distal pancreatectomy", "A Whipple's surgery"], 0,
  "Puestow's: longitudinal pancreatico-jejunostomy. (Book p296)")
q(296, S11, "Puestow's procedure is indicated for:",
  ["Stones throughout the pancreatic duct", "Stones in the distal pancreas only", "A head mass only", "A normal duct"], 0,
  "Puestow's: indication — stones throughout pancreatic duct. (Book p296)")
q(296, S11, "The Duval procedure is:",
  ["An end-to-end pancreaticojejunostomy", "A longitudinal pancreaticojejunostomy", "A distal pancreatectomy", "A Beger's procedure"], 0,
  "Duval: end-to-end pancreatico-jejunostomy. (Book p296)")
q(296, S11, "The Duval procedure is indicated for:",
  ["Stones in the distal pancreas", "Stones throughout the duct", "A normal duct", "A head mass"], 0,
  "Duval: indication — stones in distal pancreas. (Book p296)")
q(296, S11, "In resection for painful chronic pancreatitis restricted to the HEAD, the procedure is:",
  ["Beger's procedure — duodenal preserving pancreatic head resection", "Distal pancreatectomy", "Puestow's procedure", "Whipple's surgery"], 0,
  "Resection: restricted to head — Beger's procedure, duodenal preserving pancreatic head resection. (Book p296)")
q(296, S11, "In resection for painful chronic pancreatitis restricted to the BODY and TAIL, the procedure is:",
  ["Distal pancreatectomy", "Beger's procedure", "Puestow's procedure", "Whipple's surgery"], 0,
  "Resection: restricted to body and tail — distal pancreatectomy. (Book p296)")
q(296, S11, "Frey's procedure is:",
  ["Beger's plus Puestow's procedure", "Beger's plus Duval", "Puestow's plus Duval", "Distal pancreatectomy plus Beger's"], 0,
  "Frey's procedure: Beger's + Puestow's procedure. (Book p296)")

# ------------------------------------------------------------------ units
def first_page(label):
    for x in Q:
        if x["sec"] == label:
            return x["page"]
    return 0


UNIT_DEFS = [
    (S1, "The pancreas is born with its quirks: divisum — the commonest anomaly — is unfused dorsal and ventral buds draining badly and setting the stage for pancreatitis, diagnosed on MRCP and treated with ERCP and sphincterotomy. The annular pancreas is a malrotated ventral bud strangling the second part of the duodenum, the friend of Down's syndrome, flashing the double bubble on X-ray; CECT defines it and duodeno-duodenostomy relieves it — never cut the ring, or its blood supply dies."),
    (S2, "At the head of the pancreas runs the tunnel of love between the superior mesenteric artery and vein — keep it intact and Whipple's stays on the table. The sphincter of Oddi is four sphincters in a sleeve (superior and inferior choledochal, ampullary, pancreatic); when it malfunctions, bile and juice back up as biliary colic or post-cholecystectomy syndrome or as pancreatitis. ERCP manometry above 40 mmHg proves it, and the Milwaukee types grade it: pain, dilation and enzymes for Type I, pain plus dilation for Type II, pain alone for Type III."),
    (S3, "Gallstones top the cause list of acute pancreatitis, alcohol second, trauma first in children, and ERCP — 5% of the time, more in females, in difficult cannulation and in therapeutic runs — iatrogenically. Thiazides, antiretrovirals and chemo add their names, with hypercalcaemia, hypertriglyceridaemia, divisum, idiopathic and the odd scorpion bite rounding it out. The co-localisation theory plays out the pathology: a pathologic stimulus drives calcium and PKC, NF-KB fires, zymogens meet lysosomes and trypsin activates where it should not — acinar death, inflammatory cells, IL-1, IL-6, IL-10 and TNF-alpha, systemic inflammation, necrosis. The pain is epigastric, boring to the back, relieved leaning forward — symptoms always out of proportion to the quiet signs."),
    (S4, "Hemorrhagic pancreatitis bruises the body in three places: Cullen's at the umbilicus, Grey Turner's at the flanks, Fox's at the groin; the peritonitis is chalky white without a perforation. Two of three makes the diagnosis — the pain, a threefold amylase or lipase, or characteristic imaging. Amylase is the early riser and early leaver, sensitive; lipase rises gradually, lingers, and is more specific; neither predicts severity. Amylase climbs only 3-4 times normal and climbs for other culprits too — mesenteric ischaemia, bowel perforation, salpingitis, volvulus, torsion. The X-ray is non-specific: gasless stunned bowel, the colon cut off sign, the sentinel loop in the left upper quadrant. CECT is the IOC after 72 hours — before that it understates the damage — in the portal venous phase at 60-70 seconds, most sensitive for necrosis; deranged liver enzymes whisper biliary, and hypocalcaemia is saponified fat chelating the calcium."),
    (S5, "The severity scores are the scorecard: Glasgow 3 or more, Ranson's 3 or more (WBC over 16,000, age over 55, glucose over 200, AST over 250, LDH over 350 on admission; hematocrit drop over 10%, BUN rise over 5, calcium under 8, PaO2 under 60, base deficit over 4 and fluid needs over 6 litres within 48 hours), BISAP's bedside five (BUN over 25, impaired mentation, SIRS, age over 60, pleural effusion) at 3 or more, APACHE II at 8 or more, HAPS, modified Marshall at 2 or more, and CRP over 150. The CT severity index — Balthazar 0 to 4 plus necrosis 0, 2, 4, 6 — tops 10 and calls 6 or more severe."),
    (S6, "The management is a disciplined ladder: NPO, Ringer's lactate as the fluid of choice, analgesia with opioids when the pain won't sit, antibiotics only for severe disease and infected necrosis — meropenem is the IV drug of choice. Nutrition walks from TPN in the initial and severe phase toward early enteral feeding, preferably through a nasojejunal tube, because an early gut reduces mortality while a starved one leaks bacteria into infection. ERCP with sphincterotomy enters when a CBD stone is documented, the pancreatitis is biliary, the symptoms outlast 48 hours or jaundice appears — and in gallstone pancreatitis the gallbladder comes out before discharge."),
    (S7, "The Atlanta classification sorts complications: mild none, moderate local only, severe both. Locally the pseudocyst forms, necrosis sets in, the splenic artery — the commonest vessel — pseudoaneurysms and needs ligation or embolisation, splenic vein thrombosis makes sinistral portal hypertension bleeding from the upper GI tract (splenectomy cures it), and the left pleural effusion accumulates. Systemically, ARDS, MODS — the commonest cause of early death, sepsis and SIRS — the commonest cause of death. The timeline terms are exact: under 4 weeks, an acute peripancreatic collection or an acute necrotic collection; beyond 4 weeks with a wall, a pseudocyst or walled-off necrosis. Small collections are watched; large or symptomatic ones get a pigtail. And when the duct ruptures into the peritoneum, the amylase-rich turbid ascites answers to paracentesis, octreotide to dry the secretions, and a stent to seal the leak."),
    (S8, "Necrosis is dead tissue, and sterile dead tissue is left alone unless the pain persists, the patient fails to improve, or the biliary or enteric obstruction becomes symptomatic — then the prognosis is still the better of the two fates. Infected necrosis announces itself with fever, rising TLC and CRP and gas bubbles on CT, and is managed by the step-up approach: percutaneous pigtail drainage first, then minimally invasive retroperitoneal debridement if that fails — and it carries high mortality. Beger's method, the open era's answer, irrigates and drains saline through both tubes and keeps its high mortality too."),
    (S9, "The pseudocyst is a granulation-lined collection, most often in the lesser sac, more common in chronic pancreatitis, presenting as an epigastric lump with vomiting on a history of pancreatitis. CECT is the IOC; D'Esio types it — Type I acute with a normal duct, Type II acute-on-chronic with abnormal anatomy but no strictures, Type III chronic, strictured, duct-communicating, a retention cyst. It usually resolves on its own; intervene when it is over 6 cm, over 6 weeks old, or walled over 6 mm thick. External drainage (pigtail) takes the infected and the hemorrhagic, with a stent for the duct-communicating fistula; internal drainage — cystojejunostomy or cystogastrostomy — is done open, laparoscopically or by NOTES. Infection is its commonest complication, hemorrhage the commonest surgical one, with rupture and pancreato-pleural fistula besides; and against the mucinous cystic neoplasm in the differential, the pseudocyst shows a normal CEA and the thinner wall."),
    (S10, "Chronic pancreatitis is fibrosis and chronic inflammation doing irreversible damage to the parenchyma, catalogued by TIGAR-O: toxins (alcohol first, then smoking, hypercalcaemia, renal failure), idiopathic, genetic (PRSS1 on chromosome 7, SPINK1 of tropical calcific pancreatitis — acinar-cell guard against premature trypsinogen activation, cassava-linked, cancer-prone — and CFTR), autoimmune (IgG4 mediated fibrosis), recurrent (post-necrotic, recurrent acute, vascular) and obstructive (stones, divisum, duct scars). It speaks only after 80-90% destruction, exocrine before endocrine: enzymes fall into steatorrhoea, malabsorption, diarrhoea and weight loss (fecal fat up, elastase down, NBT PABA), treated with exogenous enzymes and a PPI; insulin falls into diabetes (glucose and HbA1c) treated with hypoglycaemics or insulin; and the intractable pain is fibrosis and stones choking a scarred main duct. Secretin MRCP is the IOC, ERCP the gold standard, EUS graded by Rosemont, and the dilated beaded duct runs as the chain of lakes."),
    (S11, "Pain is managed in tiers: analgesics first, and if they hold, no intervention. When they fail, the duct decides: under 5-6 mm, ERCP with sphincterotomy; over 5-6 mm, drainage — Puestow's longitudinal pancreaticojejunostomy for stones running the whole duct, Duval's end-to-end pancreaticojejunostomy for stones stuck distally. Resection takes the rest: Beger's duodenal-preserving head resection for a head-limited disease, distal pancreatectomy for body and tail — and Frey's combines Beger's with Puestow's when both are needed."),
]

UNITS = []
for i, (title, guide) in enumerate(UNIT_DEFS, 1):
    UNITS.append({
        "id": f"SURG-U39-{i}",
        "ch": 39,
        "n": i,
        "title": title,
        "sec": f"{title} · p{first_page(title)}",
        "qs": [x["id"] for x in Q if x["sec"] == title],
        "guide": guide,
    })

covered = [i for u in UNITS for i in u["qs"]]
assert covered == [x["id"] for x in Q], "units must cover questions in order"
assert len(set(covered)) == len(covered), "duplicate question in units"

data = {"questions": Q, "units": UNITS}
with open("data/ch39.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
print(f"ch39: {len(Q)} questions, {len(UNITS)} units")
