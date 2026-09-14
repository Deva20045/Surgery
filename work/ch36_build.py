#!/usr/bin/env python3
"""Build data/ch36.json — ch36 Spleen (Marrow Surgery Ed 8, book p260-264)."""
import json

Q = []


def q(page, sec, text, opts, ans, exp):
    Q.append({
        "id": f"SURG-C36-{len(Q)+1:03d}",
        "sec": sec,
        "page": page,
        "q": text,
        "opts": opts,
        "ans": ans,
        "exp": exp,
    })


# ------------------------------------------------------------------ p260
S1 = "Anatomy of the Spleen"
q(260, S1, "In surface anatomy, the spleen lies along the axis of which ribs?",
  ["9th to 11th ribs", "7th to 9th ribs", "10th to 12th ribs", "5th to 7th ribs"], 0,
  "Surface anatomy: location — along axis of 9th-11th ribs. (Book p260)")
q(260, S1, "Which border of the spleen has a notch?",
  ["Inferolateral border", "Superomedial border", "Anterior border", "Posterior border"], 0,
  "Surface anatomy: border — the inferolateral border has a notch. (Book p260)")
q(260, S1, "Splenomegaly displaces the spleen in which direction?",
  ["Medially", "Laterally", "Superiorly into the chest", "Anteromedially into the epigastrium only"], 0,
  "Applied aspect: splenic enlargement is medially. (Book p260)")
q(260, S1, "Downward displacement of the spleen is prevented by which ligament?",
  ["Phrenicocolic ligament", "Gastrosplenic ligament", "Lienorenal ligament", "Splenoportal ligament"], 0,
  "Applied aspect: downward displacement is prevented by the phrenicocolic ligament. (Book p260)")
q(260, S1, "Splenic trauma is classically associated with fractures of which ribs?",
  ["9th to 11th ribs on the left side", "9th to 11th ribs on the right side", "5th to 8th ribs on the left", "11th and 12th ribs on both sides"], 0,
  "Applied aspect: fracture of 9th-11th ribs on the left side leads to splenic trauma. (Book p260)")
q(260, S1, "Which of the splenic ligaments are avascular and can be cut directly?",
  ["Splenophrenic and splenocolic ligaments", "Gastrosplenic and lienorenal ligaments",
   "Gastrosplenic and splenophrenic ligaments", "Lienorenal and splenocolic ligaments"], 0,
  "Splenic ligaments table: splenophrenic and splenocolic — avascular, the ligament can be cut. (Book p260)")
q(260, S1, "The gastrosplenic ligament contains which vessels?",
  ["Short gastric vessels", "Splenic vessels", "Pancreaticoduodenal vessels", "Left gastroepiploic vessels only"], 0,
  "Splenic ligaments table: gastrosplenic ligament carries the short gastric vessels. (Book p260)")
q(260, S1, "The lienorenal ligament transmits all of the following EXCEPT:",
  ["Gastroduodenal vessels", "Splenic vessels", "Tail of the pancreas", "Short gastric vessels"], 0,
  "Splenic ligaments table: lienorenal ligament carries the splenic vessels and the tail of the pancreas — the gastroduodenal vessels are not in it. (Book p260)")
q(260, S1, "Before the lienorenal ligament is cut, what must be done to its contents?",
  ["Vessels are ligated and then the ligament is cut", "The ligament is cut first and the vessels tied later",
   "Only the tail of the pancreas is divided", "No ligation is needed as it is avascular"], 0,
  "Splenic ligaments table: gastrosplenic and lienorenal contents (short gastric vessels, splenic vessels, tail of pancreas) — vessels are ligated and then the ligament is cut. (Book p260)")
q(260, S1, "The splenic artery is a branch of:",
  ["Coeliac trunk", "Superior mesenteric artery", "Inferior mesenteric artery", "Abdominal aorta directly"], 0,
  "Blood supply of spleen: splenic artery — a branch of the coeliac trunk. (Book p260)")
q(260, S1, "The portal vein is formed by the union of the splenic vein with which vein?",
  ["Superior mesenteric vein", "Inferior mesenteric vein", "Right portal vein", "Left gastric vein"], 0,
  "Blood supply: splenic vein — the portal vein is formed by the splenic vein joining the superior mesenteric vein. (Book p260)")
q(260, S1, "The inferior mesenteric vein drains into:",
  ["Splenic vein", "Superior mesenteric vein", "Portal vein directly", "Left gastric vein"], 0,
  "Blood supply: inferior mesenteric vein drains into the splenic vein. (Book p260)")

# ------------------------------------------------------------------ p261
S2 = "Functions of the Spleen"
q(261, S2, "The immunological function of the spleen is to:",
  ["Produce antibodies", "Produce red cells", "Store platelets", "Filter lymph"], 0,
  "Functions: 1. Immunological — produces antibodies. (Book p261)")
q(261, S2, "After splenectomy, the risk of which type of infection rises?",
  ["Opportunistic infections", "Only viral infections", "Only fungal infections", "No change in infection risk"], 0,
  "Functions: post splenectomy there is a rise in the risk of opportunistic infections. (Book p261)")
q(261, S2, "The spleen acts as a 'graveyard' for blood cells by:",
  ["Filtering the non-functioning cells", "Producing new cells", "Storing iron only", "Releasing reticulocytes"], 0,
  "Functions: 2. Acts as graveyard for blood cells — filters the non-functioning cells. (Book p261)")
q(261, S2, "Physiological haematopoiesis by the spleen occurs in:",
  ["The 3rd to 5th week of intrauterine life", "The 3rd to 5th month of fetal life", "The first year after birth", "Adulthood during severe anaemia"], 0,
  "Functions: 3. Haematopoiesis (physiological) — 3rd-5th week of intrauterine life. (Book p261)")
q(261, S2, "Pathological haematopoiesis by the spleen is seen in:",
  ["Myeloproliferative diseases", "Splenomegaly due to congestion only", "ITP", "Viral infections"], 0,
  "Functions: pathological haematopoiesis occurs in myeloproliferative diseases. (Book p261)")
q(261, S2, "The reservoir function of the spleen is for:",
  ["WBCs, RBCs and platelets", "Red cells only", "Platelets only", "Serum only"], 0,
  "Functions: 4. Reservoir function for WBCs, RBCs and platelets. (Book p261)")
q(261, S2, "Immediately after splenectomy, the blood cells show:",
  ["A transient rise in blood cells", "A permanent fall in all cell lines", "No change", "Immediate aplasia"], 0,
  "Functions: post splenectomy — transient rise in blood cells. (Book p261)")

S3 = "Applied Aspects of Splenic Tissue"
q(261, S3, "Splenunculi are:",
  ["Accessory splenic tissue", "Metastatic deposits in the spleen", "Cystic degeneration of the spleen", "Embryonic rests of the liver"], 0,
  "Applied aspects of splenic tissue: splenunculi — accessory splenic tissue. (Book p261)")
q(261, S3, "The most common site of splenunculi is:",
  ["The hilum", "The splenophrenic ligament", "The greater curvature of the stomach", "The peritoneal cavity"], 0,
  "Splenunculi: site — hilum (m/c). (Book p261)")
q(261, S3, "In a haematological condition such as ITP, if splenunculi is left behind during splenectomy the result is:",
  ["Recurrence", "Oversplenism", "Haemoperitoneum", "Pneumonia"], 0,
  "Splenunculi: significance — in haematological conditions (ITP), if splenunculi is left behind, recurrence. (Book p261)")
q(261, S3, "Splenosis refers to:",
  ["Splenic tissue deposits in the omentum and bowel following trauma", "Spontaneous rupture of the spleen", "Malignant transformation of splenic tissue", "Infarction of accessory spleens"], 0,
  "Splenosis: following trauma, splenic tissue deposits in the omentum and bowel. (Book p261)")
q(261, S3, "On imaging, splenosis appears as:",
  ["A tumour or mass", "A hypodense cyst", "Free fluid", "Air under the diaphragm"], 0,
  "Splenosis: appears as a tumour/mass on imaging. (Book p261)")
q(261, S3, "A biopsy of a splenosis nodule shows:",
  ["Normal splenic tissue", "Adenocarcinoma", "Caseous necrosis", "Lymphoma"], 0,
  "Splenosis: on biopsy — normal splenic tissue. (Book p261)")

S4 = "Splenic Cysts"
q(261, S4, "A splenic pseudocyst is:",
  ["A false cyst not lined by epithelium", "A true cyst lined by mesothelium", "A cyst of flattened squamous epithelium", "A parasitic cyst"], 0,
  "Splenic cyst: 1. Pseudocyst — false cyst, not lined by epithelium. (Book p261)")
q(261, S4, "A splenic pseudocyst is classically associated with a history of:",
  ["Trauma", "Echinococcus exposure", "Sickle cell disease", "Pancreatitis"], 0,
  "Pseudocyst: H/o trauma (+). (Book p261)")
q(261, S4, "Splenic pseudocysts usually:",
  ["Resolve spontaneously", "Always need splenectomy", "Always recur", "Malignant transform"], 0,
  "Pseudocyst: resolve spontaneously. (Book p261)")
q(261, S4, "On CT, a splenic pseudocyst shows:",
  ["A smooth outline with hypodense consistency", "Peripheral nodular enhancement", "A central stellate scar", "Diffuse calcification"], 0,
  "Pseudocyst CT figure: smooth outline and hypodense consistency. (Book p261)")
q(261, S4, "A splenic hydatid cyst is a type of:",
  ["True cyst", "Pseudocyst", "Haemangioma", "Epidermoid cyst"], 0,
  "Splenic cyst: 2. True cyst — a. Hydatid cyst is the first listed true cyst. (Book p261)")
q(261, S4, "A splenic hydatid cyst is associated with exposure to:",
  ["Echinococcus", "Taenia solium", "Entamoeba", "Mycobacterium"], 0,
  "Hydatid cyst: H/o exposure to Echinococcus. (Book p261)")
q(261, S4, "A splenic hydatid cyst with multiple daughter cysts is managed by:",
  ["Splenectomy under cover of albendazole", "Observation alone", "Percutaneous drainage alone", "Antibiotics only"], 0,
  "Hydatid cyst: if multiple cysts (+), splenectomy under cover of albendazole. (Book p261)")
q(262, S4, "A splenic epidermoid cyst is lined by:",
  ["Flattened squamous epithelium", "Cuboidal epithelium", "Columnar epithelium", "Mesothelium"], 0,
  "True cyst: c. Epidermoid cyst — flattened squamous epithelium. (Book p262)")
q(262, S4, "An epidermoid splenic cyst requires excision when it is:",
  ["Greater than 5 cm and symptomatic", "Less than 1 cm and asymptomatic", "Present for more than a year", "Found on routine screening only"], 0,
  "Epidermoid cyst: if >5 cm and symptomatic — excision. (Book p262)")
q(262, S4, "Which of the following is listed under true splenic cysts?",
  ["Dermoid cyst", "Pseudocyst", "Hypodense collection after trauma", "Walled-off necrosis"], 0,
  "True cysts: a. Hydatid cyst, b. Dermoid cyst, c. Epidermoid cyst — dermoid cyst is a true cyst. (Book p262)")

# ------------------------------------------------------------------ p262
S5 = "Splenic Artery Aneurysm"
q(262, S5, "A splenic artery aneurysm is the most common:",
  ["Visceral artery aneurysm", "Peripheral artery aneurysm", "Aortic aneurysm", "Capillary malformation"], 0,
  "Splenic artery aneurysm, etiology: visceral artery aneurysm (m/c). (Book p262)")
q(262, S5, "Which of the following is listed as a cause of splenic artery aneurysm?",
  ["Pancreatitis", "Cholelithiasis", "Appendicitis", "Coeliac disease"], 0,
  "Etiology: occurs also to — pancreatitis, trauma, atherosclerosis and pregnancy. (Book p262)")
q(262, S5, "Atherosclerotic splenic artery aneurysms typically:",
  ["Occur in the elderly, with rupture uncommon", "Occur in children with frequent rupture", "Occur only in pregnancy", "Never rupture"], 0,
  "Etiology: atherosclerosis — occurs in the elderly, rupture is uncommon. (Book p262)")
q(262, S5, "In pregnancy, splenic artery aneurysm:",
  ["Occurs in the 2nd and 3rd trimesters and rupture is common", "Occurs only in the 1st trimester", "Never ruptures in pregnancy", "Is always asymptomatic and never treated"], 0,
  "Etiology: pregnancy — occurs in the 2nd and 3rd trimester, rupture is common. (Book p262)")
q(262, S5, "The most common clinical presentation of a splenic artery aneurysm is:",
  ["Asymptomatic", "High grade fever", "Jaundice", "Chronic diarrhoea"], 0,
  "Clinical features: asymptomatic. (Book p262)")
q(262, S5, "Rupture of a splenic artery aneurysm presents with:",
  ["Pain", "Fever only", "Obstructive jaundice", "Diarrhoea"], 0,
  "Clinical features: if rupture (+), pain. (Book p262)")
q(262, S5, "Kehr's sign in splenic artery aneurysm is:",
  ["Referred pain in the left shoulder tip on raising the left lower limb", "Pain in the right shoulder on inspiration", "Pain radiating to the jaw", "Pain in the back on flexion"], 0,
  "Clinical features: Kehr's sign (+) — referred pain in the left shoulder tip on raising the left lower limb. (Book p262)")
q(262, S5, "The investigation of choice for splenic artery aneurysm is:",
  ["CT angiography", "Plain X-ray abdomen", "Ultrasound alone", "MRI without contrast"], 0,
  "Investigation: CT angiography (IOC). (Book p262)")
q(262, S5, "First-line management of splenic artery aneurysm is:",
  ["Embolisation or grafting", "Immediate splenectomy", "Conservative observation", "Thrombolysis"], 0,
  "Management: embolisation and grafting — 1st line. (Book p262)")
q(262, S5, "Splenectomy for a splenic artery aneurysm is:",
  ["The last resort", "The 1st line", "Never indicated", "Only for children"], 0,
  "Management: splenectomy — last resort. (Book p262)")

S6 = "Splenic Infarct"
q(262, S6, "Splenic infarcts are seen in hypersplenism due to:",
  ["Portal hypertension and myelodysplastic syndromes", "Chronic cholecystitis", "Gastric ulcers", "Pancreatic adenocarcinoma"], 0,
  "Splenic infarct, etiology: seen in hypersplenism — portal HTN, myelodysplastic syndromes. (Book p262)")
q(262, S6, "The majority of splenic infarcts are:",
  ["Asymptomatic", "Fatal", "Present with jaundice", "Present with peritonitis"], 0,
  "Clinical features: asymptomatic — the majority. (Book p262)")
q(262, S6, "Pain in splenic infarct is all of the following EXCEPT:",
  ["Colicky central abdominal pain", "Left upper quadrant pain", "Pleuritic pain", "Referred pain in the left shoulder tip"], 0,
  "Clinical features: pain — left upper quadrant pain, pleuritic pain and referred pain in the left shoulder tip. (Book p262)")
q(262, S6, "The investigation of choice for splenic infarct is:",
  ["CECT", "Plain X-ray", "MRCP", "HIDA scan"], 0,
  "Investigation: CECT (IOC). (Book p262)")
q(262, S6, "On CECT, a splenic infarct appears as:",
  ["A hypodense infarcted spleen", "A hyperdense mass", "A ring-enhancing abscess only", "Normal spleen with dilated bowel"], 0,
  "CECT figure: hypodense infarcted spleen. (Book p262)")
q(262, S6, "The usual management of splenic infarct is:",
  ["Conservative", "Emergency splenectomy", "Embolisation", "Antibiotics alone"], 0,
  "Management: conservative. (Book p262)")
q(262, S6, "Surgical excision for splenic infarct is done when:",
  ["It is symptomatic or an abscess is present", "The spleen is small", "The patient has fever only", "Infarction is partial and asymptomatic"], 0,
  "Management: if symptomatic or abscess (+), surgical excision. (Book p262)")

# ------------------------------------------------------------------ p263
S7 = "Splenic Abscess"
q(263, S7, "Splenic abscess is seen in:",
  ["Immunocompromised patients and post infarcts", "Only after trauma", "Only in children", "Only in pregnancy"], 0,
  "Splenic abscess, etiology: seen in immunocompromised patients, post infarcts. (Book p263)")
q(263, S7, "The clinical features of splenic abscess include:",
  ["High grade fever and pleuritic pain", "Painless jaundice", "Chronic constipation", "Weight gain"], 0,
  "Clinical features: high grade fever, pleuritic pain. (Book p263)")
q(263, S7, "The investigation of choice for splenic abscess is:",
  ["CECT", "Plain X-ray", "USG with no further workup", "Barium meal"], 0,
  "Investigation: CECT (IOC). (Book p263)")
q(263, S7, "On CECT, a splenic abscess shows:",
  ["Hypodense tissue with necrotic debris", "Homogeneous enhancement", "A calcified nodule", "Free air only"], 0,
  "CECT figure: hypodense tissue with necrotic debris. (Book p263)")
q(263, S7, "The management of a splenic abscess is:",
  ["Pigtail catheter drainage", "Oral antibiotics alone", "Immediate splenectomy in all", "No treatment"], 0,
  "Management: pigtail catheter drainage. (Book p263)")

S8 = "Splenectomy: Indications"
q(263, S8, "The most common indication for splenectomy is:",
  ["Trauma", "Gastric cancer", "Spherocytosis", "Lymphoma"], 0,
  "Indications: 1. Trauma (m/c). (Book p263)")
q(263, S8, "Traumatic splenectomy may be caused by:",
  ["Accidental or operative injury", "Only burns", "Only iatrogenic injury at laparoscopy", "Only rib fractures without organ injury"], 0,
  "Indications: trauma — accidental and operative. (Book p263)")
q(263, S8, "Splenectomy as part of oncological disease is performed in:",
  ["Gastric and pancreatic cancers (en bloc resection)", "Breast cancer", "Prostate cancer", "Oral cancer"], 0,
  "Indications: 2. Oncological — part of en bloc resection in gastric and pancreatic cancers. (Book p263)")
q(263, S8, "The most common benign splenic tumour is:",
  ["Haemangioma", "Lymphoma", "Lipoma", "Haemoblastoma"], 0,
  "Splenic tumours: m/c benign — haemangioma. (Book p263)")
q(263, S8, "The most common malignant splenic tumour is:",
  ["Lymphoma", "Haemangioma", "Adenocarcinoma", "Sarcoma"], 0,
  "Splenic tumours: m/c malignant — lymphoma. (Book p263)")
q(263, S8, "An incidentally discovered benign splenic tumour (haemangioma) requires:",
  ["No treatment", "Splenectomy", "Chemotherapy", "Radiotherapy"], 0,
  "Splenic tumours: benign (haemangioma) — incidental diagnosis, no treatment required. (Book p263)")
q(263, S8, "First-line treatment of splenic lymphoma is:",
  ["Chemotherapy, which shows a good response", "Splenectomy", "Radiotherapy alone", "Observation only"], 0,
  "Splenic tumours: malignant (lymphoma) — chemotherapy is 1st line; the disease shows a good response to treatment. (Book p263)")
q(263, S8, "Surgery for splenic lymphoma is:",
  ["Only in rare cases", "The 1st line in all cases", "Always curative", "Never done"], 0,
  "Splenic tumours: malignant (lymphoma) — surgery only in rare cases. (Book p263)")
q(263, S8, "Which of the following is a haematological indication for splenectomy?",
  ["Spherocytosis", "Cholelithiasis", "Peptic ulcer disease", "Diverticular disease"], 0,
  "Indications: 3. Haematological — spherocytosis, purpura (ITP), hypersplenism. (Book p263)")
q(263, S8, "Splenectomy for left-sided portal hypertension is due to:",
  ["Splenic vein thrombosis", "Hepatic vein thrombosis", "Portal vein thrombosis", "Mesenteric varices"], 0,
  "Indications: portal HTN (left sided) — splenic vein thrombosis. (Book p263)")

S9 = "Splenectomy: Steps and Complications"
q(263, S9, "In the steps of splenectomy, step 1 is:",
  ["Dissection of the aspect of spleen", "Transection of the splenic hilum", "Removal of the spleen", "Dissection of the short gastric vessels"], 0,
  "Steps: Step 1 — dissection of the aspect of spleen. (Book p263)")
q(263, S9, "Step 2 of splenectomy is:",
  ["Dissection of the lateral aspect and retroperitoneal attachments", "Transection of the splenic hilum", "Dissection of short gastric vessels", "Removal of the spleen"], 0,
  "Steps: Step 2 — dissection of the lateral aspect and retroperitoneal attachments. (Book p263)")
q(263, S9, "Step 3 of splenectomy is:",
  ["Transection of the splenic hilum", "Dissection of the lateral aspect", "Ligation of the aorta", "Removal of the spleen"], 0,
  "Steps: Step 3 — transection of the splenic hilum. (Book p263)")
q(263, S9, "Step 4 of splenectomy is:",
  ["Dissection of the short gastric vessels", "Transection of the splenic hilum", "Removal of the spleen", "Dissection of the lateral aspect"], 0,
  "Steps: Step 4 — dissection of short gastric vessels. (Book p263)")
q(263, S9, "Step 5 of splenectomy is:",
  ["Removal of the spleen", "Dissection of short gastric vessels", "Transection of the hilum", "Closure"], 0,
  "Steps: Step 5 — removal of the spleen. (Book p263)")
q(263, S9, "Injury to the tail of the pancreas during splenectomy presents with:",
  ["Amylase-rich secretions in the drain", "Haematemesis", "Bilious vomiting", "High amylase only in serum"], 0,
  "Complications: 2. Injury — tail of pancreas presents with amylase-rich secretions in the drain. (Book p263)")
q(263, S9, "Haematemesis after splenectomy, if short gastric vessels are ligated, suggests injury to:",
  ["The stomach", "The tail of the pancreas", "The colon", "The duodenum"], 0,
  "Complications: injury — stomach presents with haematemesis if short gastric vessels are ligated. (Book p263)")
q(264, S9, "Post splenectomy, a transient rise in all 3 cell lines with a raised WBC is:",
  ["Mistaken for infection", "A sign of sepsis requiring antibiotics", "A sign of bleeding", "Never seen after splenectomy"], 0,
  "Complications: 3. Haematological — transient rise in all 3 cell lines; the raised WBC is mistaken for infection. (Book p264)")
q(264, S9, "After splenectomy, platelets greater than 10 lakh/cumm:",
  ["Predispose to thrombosis, treated with prophylactic aspirin", "Are always normal", "Cause haemorrhage", "Require plateletpheresis in all"], 0,
  "Complications: platelet >10 lakh/cumm predispose to thrombosis — Rx: prophylactic aspirin. (Book p264)")
q(264, S9, "Which of the following is a permanent haematological change on the peripheral smear after splenectomy?",
  ["Howell Jolly bodies", "Schistocytes", "Spherocytes", "Target cells only"], 0,
  "Complications: 4. Permanent haematological changes on peripheral smear — basophilic stippling, Howell Jolly bodies, reticulocytes, hypersegmented WBCs. (Book p264)")
q(264, S9, "The most common complication of splenectomy is:",
  ["Left lower lobe atelectasis / pneumonia", "Pancreatic fistula", "Wound infection", "Portal vein thrombosis"], 0,
  "Complications: 5. Left lower lobe atelectasis/pneumonia (m/c). (Book p264)")
q(264, S9, "Prevention of left lower lobe atelectasis after splenectomy includes:",
  ["Active chest physiotherapy with incentive spirometry", "Keeping the patient supine without mobilisation", "Withholding analgesia", "Early feeding only"], 0,
  "Prevention: active chest physiotherapy — incentive spirometry. (Book p264)")
q(264, S9, "Pain control after splenectomy is important because it:",
  ["Facilitates deep breaths", "Prevents jaundice", "Reduces amylase levels", "Prevents lymphoma"], 0,
  "Prevention: pain control — facilitates deep breaths. (Book p264)")

S10 = "OPSI: Post-Splenectomy Sepsis and Vaccination"
q(264, S10, "OPSI stands for:",
  ["Opportunistic overwhelming post splenectomy infections", "Operative post splenectomy ileus",
   "Overwhelming peritoneal sepsis after injury", "Opportunistic pneumonia and splenic infarct"], 0,
  "Complications: 6. OPSI — opportunistic overwhelming post splenectomy infections. (Book p264)")
q(264, S10, "The etiology of OPSI is:",
  ["Encapsulated bacteria", "Anaerobic gut flora", "Fungal organisms", "Viral pathogens"], 0,
  "OPSI, etiology: encapsulated bacteria. (Book p264)")
q(264, S10, "The most common organism in OPSI is:",
  ["Pneumococcus", "Meningococcus", "H. influenzae", "Pseudomonas"], 0,
  "OPSI: encapsulated bacteria — pneumococcus (m/c), meningococcus, H. influenzae. (Book p264)")
q(264, S10, "OPSI occurs more commonly in:",
  ["Children than adults", "Adults than children", "Only in the elderly", "Only in pregnancy"], 0,
  "OPSI, occurrence: children > adults. (Book p264)")
q(264, S10, "OPSI is seen commonly within how many years of splenectomy?",
  ["First 2 years", "First 6 months only", "After 10 years", "Only after 5 years"], 0,
  "OPSI, occurrence: seen commonly within the first 2 years of splenectomy. (Book p264)")
q(264, S10, "High mortality rates in OPSI are greater when splenectomy was done for:",
  ["A haematological condition than for trauma", "Trauma than a haematological condition", "Both equally", "Only in iatrogenic splenectomy"], 0,
  "OPSI, occurrence: high mortality rates — haematological condition > trauma. (Book p264)")
q(264, S10, "The pneumococcal and meningococcal vaccines after splenectomy are:",
  ["Repeated every 5 years", "Given once in a lifetime", "Repeated every year", "Repeated every 10 years"], 0,
  "Vaccination: pneumococcal and meningococcal — repeated every 5 years. (Book p264)")
q(264, S10, "The H. influenzae vaccine after splenectomy is repeated:",
  ["Every 10 years", "Every year", "Every 5 years", "Never"], 0,
  "Vaccination: H. influenzae — every 10 years. (Book p264)")
q(264, S10, "The influenza vaccine after splenectomy is given:",
  ["Yearly", "Once in a lifetime", "Every 5 years", "Only when ill"], 0,
  "Vaccination: influenza — yearly. (Book p264)")
q(264, S10, "In an elective splenectomy, the timing of vaccination is:",
  ["2 weeks before the surgery", "1 week after the surgery", "On the day of surgery", "Post op day 1/2"], 0,
  "Timing of vaccine: elective — 2 weeks before. (Book p264)")
q(264, S10, "In an emergency splenectomy, the timing of vaccination is:",
  ["Post op day 1/2", "2 weeks before surgery", "Never", "Only after 1 year"], 0,
  "Timing of vaccine: emergency — post op day 1/2. (Book p264)")

# ------------------------------------------------------------------ units
def first_page(label):
    for x in Q:
        if x["sec"] == label:
            return x["page"]
    return 0


UNIT_DEFS = [
    (S1, "The spleen hides behind the 9th to 11th ribs, so fractures of those left ribs are splenic injuries, and its inferolateral border carries the notch. The gastrosplenic and lienorenal ligaments hold vessels and the pancreatic tail, so they are ligated before being cut, while the splenophrenic and splenocolic ligaments are avascular and can be divided freely. The splenic artery rides out of the coeliac trunk, and the portal vein is born where the splenic vein meets the superior mesenteric vein — the IMV joining the splenic vein on the way."),
    (S2, "The spleen makes antibodies, acts as the graveyard that filters spent blood cells, haematopoieses in the 3rd-5th week of fetal life (and pathologically in myeloproliferative disease), and banks WBCs, RBCs and platelets. Take it away and opportunistic infections loom while blood counts rise transiently."),
    (S3, "Left-behind accessory splenic tissue — splenunculi, most often at the hilum — can make an ITP come back, so the spleen bed is searched carefully. Splenosis is different: trauma seeds the omentum and bowel with splenic tissue that mimics a tumour on imaging but is normal splenic tissue on biopsy."),
    (S4, "Pseudocysts are post-traumatic false cysts, unlined by epithelium, that smooth out on CT and resolve on their own. True cysts — hydatid, dermoid and epidermoid — behave differently: a hydatid with multiple daughter cysts needs splenectomy under albendazole cover, and a squamous-lined epidermoid cyst over 5 cm that is symptomatic is excised."),
    (S5, "The splenic artery is the commonest site of visceral artery aneurysm, born of pancreatitis, trauma, atherosclerosis or pregnancy — and in pregnancy it ruptures in the 2nd-3rd trimester. Most stay silent; rupture brings pain and Kehr's sign. CT angiography diagnoses it, embolisation or grafting is first line, and splenectomy is the last resort."),
    (S6, "Splenic infarcts follow hypersplenism of portal hypertension or myelodysplastic syndromes and mostly stay silent. When they speak, it is with LUQ pain, pleuritic pain and shoulder-tip referral. CECT shows the hypodense infarcted spleen; treat conservatively and operate only if symptoms persist or an abscess supervenes."),
    (S7, "The splenic abscess is the infection of the immunocompromised and the post-infarct spleen — high-grade fever, pleuritic pain, and a CECT hypodense collection of necrotic debris. A pigtail catheter drains it before anyone thinks of removing the spleen."),
    (S8, "Trauma is the commonest reason the spleen comes out, followed by oncology — en bloc with gastric and pancreatic cancers — and haematology: spherocytosis, ITP and hypersplenism, plus left-sided portal hypertension from splenic vein thrombosis. Among splenic tumours, haemangioma is the commonest benign lesion and needs nothing, while lymphoma, the commonest malignancy, answers to chemotherapy and is rarely operated on."),
    (S9, "Splenectomy runs in five steps: dissection of the aspect of spleen, lateral and retroperitoneal attachments, transection of the hilum, the short gastric vessels, and removal. Its complications are a teaching list — pancreatic tail injury with amylase-rich drain, gastric haematemesis when short gastric vessels are ligated, a transient trilineage count rise mistaken for infection, platelets over 10 lakh predisposing to thrombosis (aspirin), permanent Howell Jolly bodies on smear, and the commonest of all: left lower lobe atelectasis, prevented by incentive spirometry and pain control."),
    (S10, "OPSI — opportunistic overwhelming post splenectomy infection — is the lethal shadow of the operation: encapsulated bacteria (pneumococcus above all, then meningococcus and H. influenzae), striking children more than adults, mostly within the first 2 years, with higher mortality after haematological indications. Vaccinate: pneumococcal and meningococcal repeated every 5 years, H. influenzae every 10 years, influenza yearly — 2 weeks before if elective, post op day 1/2 if emergency."),
]

UNITS = []
for i, (title, guide) in enumerate(UNIT_DEFS, 1):
    UNITS.append({
        "id": f"SURG-U36-{i}",
        "ch": 36,
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
with open("data/ch36.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
print(f"ch36: {len(Q)} questions, {len(UNITS)} units")
