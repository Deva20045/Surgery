#!/usr/bin/env python3
"""Build data/ch37.json — ch37 Gall Bladder and Bile Ducts: Part 1 (Marrow Surgery Ed 8, book p265-275)."""
import json

Q = []


def q(page, sec, text, opts, ans, exp):
    Q.append({
        "id": f"SURG-C37-{len(Q)+1:03d}",
        "sec": sec,
        "page": page,
        "q": text,
        "opts": opts,
        "ans": ans,
        "exp": exp,
    })


# ------------------------------------------------------------------ p265
S1 = "Surgical Anatomy of the Gallbladder"
q(265, S1, "A pyriform, distended gallbladder on examination is a cause of all of the following EXCEPT:",
  ["A gallbladder mass", "Periampullary cancers (obstructive jaundice)", "Mucocele", "Common bile duct obstruction"], 0,
  "Shape of gallbladder: pyriform means distended GB — causes are periampullary cancers (obstructive jaundice) and mucocele; a GB mass is the NOT-pyriform variant. (Book p265)")
q(265, S1, "A distended (pyriform) gallbladder shows on examination:",
  ["Side to side mobility", "No side to side mobility", "Fixed to the abdominal wall", "Rebound tenderness only"], 0,
  "Pyriform (distended) GB: O/E — side to side mobility. (Book p265)")
q(265, S1, "A gallbladder mass is NOT pyriform and on examination shows:",
  ["No side to side mobility", "Side to side mobility", "A positive Murphy's sign", "A palpable cystic plate"], 0,
  "Shape of gallbladder: not pyriform — GB mass, due to GB cancer; O/E — no side to side mobility. (Book p265)")
q(265, S1, "The boundaries of the hepatocystic triangle are:",
  ["Inferior edge of liver, common hepatic duct and cystic duct", "Cystic artery, cystic duct and common hepatic duct",
   "Inferior edge of liver, cystic artery and cystic duct", "Gallbladder neck, cystic artery and common bile duct"], 0,
  "Hepatocystic triangle boundaries: inferior edge of liver, common hepatic duct and cystic duct. (Book p265)")
q(265, S1, "Calot's triangle is bounded by:",
  ["Cystic artery, cystic duct and common hepatic duct", "Inferior edge of liver, common hepatic duct and cystic duct",
   "Cystic artery, common bile duct and gallbladder neck", "Hepatic artery, cystic duct and cystic plate"], 0,
  "Calot's triangle boundaries: cystic artery, cystic duct and common hepatic duct. (Book p265)")
q(265, S1, "The content of Calot's triangle is:",
  ["Cystic lymph node of Lund", "The common bile duct", "The portal vein", "The tail of the pancreas"], 0,
  "Calot's triangle: content — cystic lymph node of Lund. (Book p265)")
q(265, S1, "The cystic lymph node of Lund is also known as:",
  ["The sentinel node of the gallbladder", "Virchow's node", "The celiac node", "The inferior mesenteric node"], 0,
  "Calot's triangle: the cystic lymph node of Lund is the sentinel node of the gallbladder. (Book p265)")
q(265, S1, "During laparoscopic cholecystectomy, the critical view of safety is achieved by dissecting:",
  ["Calot's triangle", "The hepatocystic triangle only", "The cystic plate", "Rouviere's sulcus"], 0,
  "Critical view of safety: Calot's triangle is dissected during lap cholecystectomy. (Book p265)")
q(265, S1, "In the critical view of safety, which two structures are clipped before the gallbladder is removed?",
  ["Cystic artery and cystic duct", "Cystic artery and common hepatic duct", "Cystic duct and common bile duct", "Right hepatic artery and cystic duct"], 0,
  "Critical view of safety: the cystic artery and cystic duct are clipped, then the gallbladder is removed. (Book p265)")
q(265, S1, "Moynihan's hump is:",
  ["A tortuous right hepatic artery lying in Calot's triangle", "A stone in the cystic duct", "A mucocele of the gallbladder", "A variant of the cystic plate"], 0,
  "Moynihan's hump: tortuous (R) hepatic artery lying in Calot's triangle. (Book p265)")
q(265, S1, "The cystic artery is a branch of:",
  ["The right hepatic artery", "The left hepatic artery", "The common hepatic artery only", "The gastroduodenal artery only"], 0,
  "Moynihan's hump: cystic artery — branch of the right hepatic artery. (Book p265)")
q(265, S1, "The clinical significance of Moynihan's hump is that it may be:",
  ["Injured during laparoscopic cholecystectomy causing bleeding", "Misidentified as the cystic duct", "The cause of Charcot's triad", "A marker of gallbladder cancer"], 0,
  "Moynihan's hump: clinical significance — injury during lap cholecystectomy leads to bleeding. (Book p265)")

# ------------------------------------------------------------------ p266
S2 = "Surface Anatomy: Cystic Plate, Rouviere's Sulcus and the R4U Line"
q(266, S2, "The cystic plate:",
  ["Covers the gallbladder fossa", "Is the peritoneal lining of the cystic duct", "Contains the cystic artery", "Lies below the liver capsule of segment 2"], 0,
  "Cystic plate: covers the gallbladder fossa. (Book p266)")
q(266, S2, "The cystic plate is a sheet continuous with the liver capsule of which Couinaud segments?",
  ["4 and 5", "2 and 3", "6 and 7", "8 and 4a"], 0,
  "Cystic plate: sheet continuous with the liver capsule of segments 4 and 5. (Book p266)")
q(266, S2, "Exposure of the cystic plate corresponds to:",
  ["The critical view of safety", "Rouviere's sulcus", "The R4U line", "The gallbladder fossa only"], 0,
  "Cystic plate: cystic plate exposed — critical view of safety. (Book p266)")
q(266, S2, "Rouviere's sulcus is located on:",
  ["The undersurface of the right lobe of liver", "The undersurface of the left lobe", "The anterior surface of segment 4", "The gallbladder fossa"], 0,
  "Rouviere's sulcus: undersurface of the right lobe of liver. (Book p266)")
q(266, S2, "Rouviere's sulcus runs to the right of the hepatic hilum, marking the position of:",
  ["The right posterior sectoral pedicle", "The left hepatic duct", "The portal vein only", "The cystic artery"], 0,
  "Rouviere's sulcus: running to the right of the hepatic hilum — position of the right posterior sectoral pedicle. (Book p266)")
q(266, S2, "The R4U line runs from:",
  ["The roof of Rouviere's sulcus to the base of segment 4", "The gallbladder fundus to the umbilicus", "Segment 8 to segment 6", "The porta hepatis to the IVC"], 0,
  "R4U line: roof of the Rouviere sulcus to the base of segment 4. (Book p266)")
q(266, S2, "In the sequence Rouviere's sulcus leads to segment 4 and then to:",
  ["The umbilical fissure", "The falciform ligament", "Segment 2", "The gallbladder fossa"], 0,
  "R4U line: Rouviere's sulcus leads to segment 4 and then to the umbilical fissure (U). (Book p266)")
q(266, S2, "The common bile duct lies in relation to the R4U line:",
  ["Below the line, where it is at risk of injury", "Above the line", "Within the line", "Always at the roof of Rouviere's sulcus"], 0,
  "Clinical significance: CBD present below the R4U line — injury. (Book p266)")
q(266, S2, "Doing laparoscopic cholecystectomy above the R4U line:",
  ["Minimises injury", "Increases the risk of CBD injury", "Prevents exposure of the cystic plate", "Is contraindicated in all"], 0,
  "Clinical significance: lap cholecystectomy above the line minimises injury. (Book p266)")
q(266, S2, "Which layer is characteristically ABSENT from the gallbladder wall?",
  ["Submucosa", "Mucosa", "Muscularis", "Serosa"], 0,
  "General anatomy: the gallbladder lacks submucosa. (Book p266)")
q(266, S2, "The subserosal lymphatics of the gallbladder drain into the gallbladder fossa, which explains:",
  ["Metastasis of gallbladder cancer into the liver", "Pneumobilia", "Charcot's triad", "Porcelain gallbladder"], 0,
  "General anatomy: contains subserosal lymphatics that drain into the GB fossa — metastasis of GB cancer into liver. (Book p266)")
q(266, S2, "Spread of gallbladder cancer into the liver occurs by all of the following EXCEPT:",
  ["Lymphatic emboli to the lung only", "Subserosal lymphatics", "Direct infiltration", "Haematogenous spread"], 0,
  "Note: spread of GB cancer into liver — subserosal lymphatics, direct infiltration and haematogenous spread. (Book p266)")
q(266, S2, "A Phrygian cap is:",
  ["A physiological variant of the gallbladder", "A malignant gallbladder tumour", "A sign of acute cholecystitis", "A radiopaque stone"], 0,
  "Phrygian cap: physiological variant of gallbladder. (Book p266)")
q(266, S2, "A Phrygian cap:",
  ["Is NOT an indication for surgical removal", "Always requires cholecystectomy", "Increases the risk of cancer", "Causes obstructive jaundice"], 0,
  "Phrygian cap: not an indication for surgical removal. (Book p266)")
q(266, S2, "A Phrygian cap on USG shows:",
  ["The fundus folded inwards", "A thickened wall", "Pericholecystic fluid", "Post acoustic shadowing"], 0,
  "Phrygian cap USG figure: fundus folded inwards; it does not raise the risk of cancer. (Book p266)")

# ------------------------------------------------------------------ p267
S3 = "Gallstones: Classification and Risk Factors"
q(267, S3, "The functions of the gallbladder include all of the following EXCEPT:",
  ["Production of bile by hepatocytes", "Reservoir of bile", "Secretion of mucin", "Concentration of bile"], 0,
  "Functions: reservoir of bile, secretion of mucin, concentration of bile. (Book p267)")
q(267, S3, "Pure cholesterol gallstones have a cholesterol content of:",
  ["More than 90%", "30-40%", "Less than 10%", "Exactly 50%"], 0,
  "Gall stones: pure cholesterol stones — >90% cholesterol content. (Book p267)")
q(267, S3, "Pure cholesterol gallstones are characteristically:",
  ["Solitary", "Multiple and small", "Black in colour", "Associated with haemolysis"], 0,
  "Gall stones: pure cholesterol stones — solitary. (Book p267)")
q(267, S3, "Pigment gallstones contain:",
  ["30-40% cholesterol", "More than 90% cholesterol", "No cholesterol at all", "Only calcium palmitate"], 0,
  "Gall stones: pigment stones — 30-40% cholesterol. (Book p267)")
q(267, S3, "The most common stones overall are:",
  ["Mixed stones", "Pure cholesterol stones", "Black pigment stones", "Brown pigment stones"], 0,
  "Gall stones: mixed stones — m/c stones overall. (Book p267)")
q(267, S3, "Brown pigment stones are seen in:",
  ["Infected bile with ascariasis, clonorchiasis and cholangitis", "Haemolytic anaemia", "Pregnancy", "Diabetes only"], 0,
  "Brown pigment stones: seen in infected bile — ascariasis infection, clonorchiasis infection, cholangitis. (Book p267)")
q(267, S3, "The composition of brown pigment stones includes:",
  ["Calcium palmitate, calcium stearate and calcium bilirubinate", "Insoluble bilirubin pigment polymer only",
   "Pure cholesterol", "Calcium bicarbonate and phosphate only"], 0,
  "Brown pigment stones: composition — calcium palmitate, calcium stearate, calcium bilirubinate. (Book p267)")
q(267, S3, "Black pigment stones are seen in haemolytic disorders such as:",
  ["G6PD, sickle cell anaemia and spherocytosis", "Iron deficiency anaemia", "Vitamin B12 deficiency", "Lead poisoning only"], 0,
  "Black pigment stones: seen in haemolytic disorders — G6PD, sickle cell anaemia, spherocytosis. (Book p267)")
q(267, S3, "The predominant composition of black pigment stones is:",
  ["Insoluble bilirubin pigment polymer", "Calcium palmitate", "Pure cholesterol", "Mucin"], 0,
  "Black pigment stones: composition — insoluble bilirubin pigment polymer (predominate) and calcium bicarbonate/phosphate. (Book p267)")
q(267, S3, "Which of the following is a risk factor for gallstones through lithogenic bile?",
  ["Obese individuals", "Underweight individuals", "Post cholecystectomy", "Prolonged fasting"], 0,
  "Risk factors — lithogenic bile: raised cholesterol, obese individuals, post ileal resection. (Book p267)")
q(267, S3, "Post ileal resection predisposes to gallstones because of:",
  ["Lithogenic bile", "Bowel obstruction", "Pancreatitis", "Hilum lymphadenopathy"], 0,
  "Risk factors — lithogenic bile includes post ileal resection. (Book p267)")
q(267, S3, "Nucleation in gallstone formation is promoted by:",
  ["Infection, ascariasis, clonorchiasis and cholangitis", "Pregnancy", "Oral contraceptive pills", "Vagotomy"], 0,
  "Risk factors — nucleation: infection, ascariasis, clonorchis, cholangitis. (Book p267)")
q(267, S3, "Which of the following causes gallstones by biliary stasis?",
  ["Pregnancy and OCP use", "Cholangitis", "Ascariasis", "Post ileal resection"], 0,
  "Risk factors — stasis: pregnancy, OCP. (Book p267)")
q(267, S3, "Post vagotomy predisposes to gallstones because:",
  ["There is decreased vagal contraction leading to stasis", "The bile becomes more dilute", "Cholesterol falls in the bile", "The sphincter of Oddi opens constantly"], 0,
  "Risk factors — stasis: post vagotomy leads to decreased contraction of the vagus, causing stasis. (Book p267)")

S4 = "Gallstones: Diagnosis, Asymptomatic Stones and Acute Cholecystitis"
q(267, S4, "On X-ray, what proportion of gallstones are radiolucent?",
  ["90%", "10%", "50%", "100%"], 0,
  "Investigation — X-ray: 90% radiolucent, 10% radiopaque. (Book p267)")
q(267, S4, "On X-ray, what proportion of gallstones are radiopaque?",
  ["10%", "90%", "50%", "1%"], 0,
  "Investigation — X-ray: 10% radiopaque. (Book p267)")
q(267, S4, "The seagull sign on X-ray is produced by:",
  ["A bircusped (two-cusped) stone", "A trircusped stone", "Pneumobilia", "A porcelain gallbladder"], 0,
  "Signs: seagull sign — bircusped stone. (Book p267)")
q(267, S4, "The mercedes Benz sign on X-ray is produced by:",
  ["A trircusped (three-cusped) stone", "A bircusped stone", "A solitary cholesterol stone", "Gas in the gallbladder wall"], 0,
  "Signs: mercedes Benz sign — trircusped stone. (Book p267)")
q(268, S4, "The investigation of choice for gallstones is:",
  ["USG", "Plain X-ray", "ERCP", "HIDA scan"], 0,
  "Investigation: USG — IOC. (Book p268)")
q(268, S4, "A gallstone on USG characteristically shows:",
  ["Post acoustic shadow", "Post acoustic enhancement", "No shadow at all", "A Phrygian cap"], 0,
  "USG: post acoustic shadows. (Book p268)")
q(268, S4, "Post acoustic shadowing on USG is ABSENT in:",
  ["Gallbladder polyp", "Cholesterol stones", "Pigment stones", "Mucocele"], 0,
  "USG: post acoustic shadow is absent in gallbladder polyp. (Book p268)")
q(268, S4, "Asymptomatic gallstones are managed by:",
  ["Observation", "Elective cholecystectomy in all", "Ursodeoxycholic acid in all", "ERCP with sphincterotomy"], 0,
  "Presentation and management: asymptomatic stones — no pain, observation. (Book p268)")
q(268, S4, "A porcelain gallbladder is defined by:",
  ["Calcification of the gallbladder wall", "A Phrygian cap", "A thickened wall on USG", "Air in the gallbladder wall"], 0,
  "Indication for surgery: a. Porcelain gallbladder — calcification of gallbladder wall. (Book p268)")
q(268, S4, "A porcelain gallbladder raises the risk of cancer by:",
  ["5-7%", "50%", "1%", "90%"], 0,
  "Porcelain gallbladder: risk of cancer raised by 5-7%. (Book p268)")
q(268, S4, "A gallbladder polyp is an indication for surgery when it is:",
  ["Greater than 1 cm", "Less than 5 mm and asymptomatic", "Stable in size", "Found incidentally at any size"], 0,
  "Indication for surgery: b. GB polyp — >1 cm. (Book p268)")
q(268, S4, "Which additional feature of a gallbladder polyp strengthens the indication for surgery?",
  ["Increasing size, especially with associated stones", "A small stable size", "No stones", "Young age only"], 0,
  "GB polyp: increasing in size and associated with stones are surgical indications. (Book p268)")
q(268, S4, "Which of the following is a listed indication for cholecystectomy in gallstone carriers?",
  ["Salmonella typhi carrier", "Hypertension", "Asthma", "Hyperthyroidism"], 0,
  "Indication for surgery: c. Salmonella typhi carrier. (Book p268)")
q(268, S4, "In a diabetic, cholecystectomy is indicated because:",
  ["The first attack of stones is severe and painful", "Diabetics never form stones", "Stones are always radiolucent in diabetics", "Diabetics have a Phrygian cap"], 0,
  "Indication for surgery: d. Diabetes — first attack of stones is severe and painful. (Book p268)")
q(268, S4, "Cholecystectomy before bariatric surgery is indicated in:",
  ["The endemic zone of gallbladder cancer", "Patients with a Phrygian cap", "Patients with radiolucent stones only", "Patients with a 1 cm polyp"], 0,
  "Indication for surgery: e. Bariatric surgery — endemic zone of GB cancer. (Book p268)")
q(268, S4, "A gallstone of what size is an indication for surgery?",
  ["Greater than 2 cm", "Greater than 5 mm", "Greater than 1 cm", "Greater than 5 cm"], 0,
  "Indication for surgery: f. >2 cm stone. (Book p268)")
q(268, S4, "Acute cholecystitis is:",
  ["Inflammation of the gallbladder", "Inflammation of the bile ducts", "Cancer of the gallbladder", "Infection of the pancreatic duct"], 0,
  "Acute cholecystitis: inflammation of gallbladder. (Book p268)")
q(268, S4, "The symptoms of acute cholecystitis include:",
  ["Pain on the right side of the abdomen, nausea and vomiting, anorexia", "Painless jaundice only", "Chronic diarrhoea", "Haematemesis"], 0,
  "Symptoms: pain in right side of abdomen, nausea and vomiting, anorexia. (Book p268)")
q(268, S4, "Murphy's sign is:",
  ["Pressing on the right hypochondrium catches the breath", "Tenderness at McBurney's point", "Pain on rectal examination", "A positive psoas sign"], 0,
  "Signs: Murphy's sign — pressing on right hypochondrium catches the breath. (Book p268)")
q(268, S4, "BoA's sign in acute cholecystitis is:",
  ["Hyperesthesia over the region of the 10th rib", "Pain in the right shoulder tip", "A positive obturator sign", "Tenderness at the costochondral junction"], 0,
  "Signs: BoA's sign — hyperesthesia over the region of the 10th rib. (Book p268)")
q(268, S4, "Under the Tokyo consensus guidelines, a LOCALISED sign of inflammation in acute cholecystitis is:",
  ["Murphy's sign and right upper quadrant pain", "Fever and raised CRP", "Wall thickness greater than 3 mm", "Leukocytosis"], 0,
  "Tokyo consensus: A. Localised signs of inflammation — Murphy's sign, right upper quadrant pain. (Book p268)")
q(268, S4, "A SYSTEMIC sign of inflammation in the Tokyo consensus criteria is:",
  ["Fever with raised CRP and leukocytosis", "Murphy's sign", "Probe tenderness", "Right upper quadrant pain"], 0,
  "Tokyo consensus: B. Systemic signs of inflammation — fever, raised CRP, leukocytosis. (Book p268)")
q(268, S4, "A classical imaging feature of acute cholecystitis is:",
  ["Wall thickness greater than 3 mm", "Wall thickness less than 2 mm", "A normal wall with a small lumen", "Diffuse hepatic enhancement"], 0,
  "Tokyo consensus: C. Classical features — wall thickness >3 mm, pericholecystic fluid (due to inflammation), probe tenderness. (Book p268)")
q(268, S4, "Pericholecystic fluid in acute cholecystitis is due to:",
  ["Inflammation", "Haemorrhage only", "Tumour only", "Normal physiology"], 0,
  "Classical features: pericholecystic fluid (d/t inflammation). (Book p268)")
q(268, S4, "A SUSPECTED diagnosis of acute cholecystitis (Tokyo consensus) requires:",
  ["Any 1 of A plus any 1 of B", "Only C (imaging)", "Only A (localised signs)", "All three criteria together"], 0,
  "Dx: suspected Dx — any 1 of A + any 1 of B. (Book p268)")
q(268, S4, "A DEFINITE diagnosis of acute cholecystitis (Tokyo consensus) requires:",
  ["Any 1 of B/A plus any 1 of B plus C", "Any 1 of A only", "Only fever", "Only a positive Murphy's sign"], 0,
  "Dx: definite Dx — any 1 of B/A + any 1 of B + C, as written in the book. (Book p268)")
q(269, S4, "A HIDA scan is:",
  ["A hepatobiliary iminodiacetic acid scan", "A hepatic isotope absorption scan", "A hydrostatic intraduodenal assay", "A histamine inhibition of dilation assay"], 0,
  "HIDA scan: hepatobiliary iminodiacetic acid scan. (Book p269)")
q(269, S4, "In a normal HIDA scan, the tracer:",
  ["Reaches the bowel in 30 minutes in 90% of cases", "Reaches the bowel in 30 minutes in 10% of cases", "Never enters the bowel", "Reaches the bowel within 1 hour in all patients"], 0,
  "HIDA scan: affinity to biliary tree — reaches bowel in 30 mins (in 90%). (Book p269)")
q(269, S4, "In acute cholecystitis, the HIDA scan shows:",
  ["Non-visualisation of the gallbladder", "Early filling of the gallbladder", "No tracer in the bowel", "Only a dilated common bile duct"], 0,
  "HIDA scan: acute cholecystitis — inflamed neck leads to non-visualisation of the gallbladder. (Book p269)")
q(269, S4, "Grade III acute cholecystitis (Tokyo consensus) is defined as:",
  ["Severe cholecystitis with organ dysfunction", "Mild cholecystitis", "Moderate cholecystitis without organ dysfunction", "Cholecystitis with a normal white cell count"], 0,
  "Severity grading: Grade III — severe cholecystitis + organ dysfunction. (Book p269)")
q(269, S4, "Which of the following places a patient in Grade II (moderate) acute cholecystitis?",
  ["White cell count greater than 18,000/mm3", "A white cell count of 8,000/mm3", "Duration of 24 hours with a normal mass", "No local mass and no complications"], 0,
  "Grade II — associated with any one of: raised WBC (>18,000/mm3), palpable tender mass in the right upper quadrant, duration >72 hrs, gangrenous cholecystitis/pericholecystic abscess/hepatic abscess/biliary peritonitis/emphysematous cholecystitis. (Book p269)")
q(269, S4, "Grade II acute cholecystitis includes all of the following EXCEPT:",
  ["Mild cholecystitis with none of the listed features", "A palpable tender mass in the right upper abdominal quadrant", "Duration greater than 72 hours", "Gangrenous cholecystitis or emphysematous cholecystitis"], 0,
  "Grade II: moderate cholecystitis associated with any one of the listed features — plain mild cholecystitis is Grade I. (Book p269)")
q(269, S4, "Grade I acute cholecystitis is:",
  ["Mild cholecystitis", "Moderate cholecystitis with a tender mass", "Severe cholecystitis with organ dysfunction", "Acalculous cholecystitis only"], 0,
  "Severity grading: Grade I — mild cholecystitis. (Book p269)")
q(269, S4, "Initial management of acute cholecystitis includes:",
  ["Nil per oral, IV fluids, IV antibiotics with aerobic and anaerobic cover, and analgesics", "Immediate laparotomy in all", "Oral antibiotics alone", "ERCP before any antibiotics"], 0,
  "Management: nil per oral, IV fluids, IV antibiotics (aerobic + anaerobic cover), analgesics. (Book p269)")
q(269, S4, "A Grade I acute cholecystitis in a patient FIT for surgery is managed definitively by:",
  ["Early laparoscopic cholecystectomy", "Tube cholecystostomy first", "Observation for a year", "Open cholecystectomy in all"], 0,
  "Definitive management: Grade I, fit for surgery — early lap cholecystectomy. (Book p269)")
q(269, S4, "A Grade I acute cholecystitis in a patient UNFIT for surgery is managed by:",
  ["Antibiotics and supportive care, then observation, then lap cholecystectomy", "Immediate tube cholecystostomy with no further surgery", "Surgery within 24 hours", "Discharge without follow-up"], 0,
  "Definitive management: Grade I, unfit for surgery — antibiotics and supportive care, observation, then lap cholecystectomy. (Book p269)")

# ------------------------------------------------------------------ p270
S5 = "Management by Grade and Acalculous Cholecystitis"
q(270, S5, "Grade II acute cholecystitis in a centre with advanced laparoscopic technique available is managed by:",
  ["Antibiotics and general supportive care with early lap cholecystectomy", "Immediate open cholecystectomy", "Tube cholecystostomy only", "Observation for 6 months"], 0,
  "Grade II: antibiotics and general supportive care — with advanced lap cholecystectomy technique available, early lap cholecystectomy. (Book p270)")
q(270, S5, "A Grade II acute cholecystitis in a patient unfit for surgery is managed by:",
  ["GB drainage (tube cholecystostomy), then delayed lap cholecystectomy", "Immediate lap cholecystectomy", "Antibiotics alone with no drainage", "Open cholecystectomy under local anaesthesia"], 0,
  "Grade II, unfit for surgery: GB drainage — tube cholecystostomy (the tube decompresses the GB and reduces inflammation) then delayed lap cholecystectomy. (Book p270)")
q(270, S5, "The purpose of tube cholecystostomy in acute cholecystitis is that:",
  ["The tube decompresses the gallbladder and reduces inflammation", "It removes the stones permanently", "It cures emphysematous cholecystitis", "It prevents Charcot's triad"], 0,
  "Tube cholecystostomy: the tube decompresses the GB, reducing inflammation. (Book p270)")
q(270, S5, "Grade III acute cholecystitis with NO negative predictive factors, in an advanced centre with good performance status, is managed by:",
  ["Antibiotics and supportive care with early lap cholecystectomy", "Permanent tube cholecystostomy", "Observation alone", "Palliative care only"], 0,
  "Grade III: antibiotics and supportive care; no negative predictive factors — advanced centre with good performance status (PS) gets early lap cholecystectomy. (Book p270)")
q(270, S5, "Grade III acute cholecystitis WITH negative predictive factors is first managed by:",
  ["Tube cholecystostomy / drainage", "Early lap cholecystectomy in all", "Open cholecystectomy without staging", "No treatment"], 0,
  "Grade III: with negative predictive factors — tube cholecystostomy/drainage. (Book p270)")
q(270, S5, "After drainage, a Grade III patient with POOR performance status is managed by:",
  ["Observation", "Immediate lap cholecystectomy", "Delayed lap cholecystectomy within a week", "Second-look drainage"], 0,
  "Grade III with negative predictive factors: good PS — delayed lap cholecystectomy; poor PS — observation. (Book p270)")
q(270, S5, "Acalculous cholecystitis is defined as:",
  ["Cholecystitis without a gallbladder stone", "Cholecystitis with a single large stone", "Cancer of the gallbladder", "Chronic cholecystitis with a WES sign"], 0,
  "Acalculous cholecystitis: cholecystitis + no GB stone. (Book p270)")
q(270, S5, "Which of the following is a risk factor for acalculous cholecystitis?",
  ["An ICU patient", "A healthy outpatient", "A patient with a Phrygian cap", "A patient with radiopaque stones"], 0,
  "Risk factors: ICU patient. (Book p270)")
q(270, S5, "Prolonged TPN predisposes to acalculous cholecystitis because:",
  ["TPN causes biliary stasis leading to inflammation", "TPN dissolves the stones", "TPN thickens the cystic plate", "TPN causes a Phrygian cap"], 0,
  "Risk factors: prolonged TPN — TPN causes biliary stasis, leading to inflammation. (Book p270)")
q(270, S5, "Acalculous cholecystitis is also seen after:",
  ["CABG", "Appendectomy", "Hernia repair", "Cataract surgery"], 0,
  "Risk factors: post CABG. (Book p270)")
q(270, S5, "The clinical features of acalculous cholecystitis are:",
  ["The same as cholecystitis", "Painless jaundice only", "Weight loss only", "Haematemesis and melaena"], 0,
  "Acalculous cholecystitis: C/F — same as cholecystitis. (Book p270)")
q(270, S5, "USG findings in acalculous cholecystitis include:",
  ["Thickened GB wall and pericholecystic fluid", "Post acoustic shadow", "A WES sign", "A Phrygian cap"], 0,
  "Investigation: USG (IOC) — thickened GB wall, pericholecystic fluid. (Book p270)")
q(270, S5, "Acalculous cholecystitis that does not improve on supportive care is managed by:",
  ["Laparoscopic cholecystectomy", "Observation for a year", "Oral antibiotics only", "ERCP with sphincterotomy"], 0,
  "Management: supportive care (nil per oral, IV fluids, IV antibiotics, analgesics); no improvement — lap cholecystectomy. (Book p270)")
q(270, S5, "An acalculous cholecystitis patient who is UNFIT for surgery is managed by:",
  ["Tube cholecystostomy", "Emergency open cholecystectomy", "Palliation only", "No treatment"], 0,
  "Management: unfit — tube cholecystostomy. (Book p270)")

# ------------------------------------------------------------------ p271
S6 = "Chronic and Emphysematous Cholecystitis"
q(271, S6, "Chronic cholecystitis is characterised by:",
  ["Multiple episodes of cholecystitis", "A single attack", "Painless jaundice", "A normal gallbladder wall"], 0,
  "Chronic cholecystitis: multiple episodes of cholecystitis. (Book p271)")
q(271, S6, "The clinical features of chronic cholecystitis are:",
  ["Right upper quadrant pain with nausea and vomiting", "Painless weight loss", "Chronic diarrhoea", "Haematemesis"], 0,
  "Clinical features: right upper quadrant pain, nausea and vomiting. (Book p271)")
q(271, S6, "The WES sign on USG in chronic cholecystitis stands for:",
  ["Wall echo shadow sign", "White echo stone sign", "Wall edema syndrome", "Wandering echo sign"], 0,
  "Investigation: USG (IOC) — wall echo shadow (WES) sign. (Book p271)")
q(271, S6, "Histopathology of chronic cholecystitis shows all of the following EXCEPT:",
  ["Acute neutrophilic abscess as the defining feature", "Clefts (ulceration of mucosa)", "Chronic inflammatory cells", "Rokitansky Aschoff sinuses"], 0,
  "Histopathology: 1. Clefts (ulceration of mucosa), 2. Chronic inflammatory cells — plus Rokitansky Aschoff sinuses. (Book p271)")
q(271, S6, "Rupture of Rokitansky Aschoff sinuses leads to:",
  ["Xanthogranulomatous cholecystitis", "Gallstone ileus", "Mirizzi syndrome", "Charcot's triad"], 0,
  "Rokitansky Aschoff sinuses, on rupture, cause xanthogranulomatous cholecystitis — differential diagnosis: cancer. (Book p271)")
q(271, S6, "Xanthogranulomatous cholecystitis is an important differential diagnosis of:",
  ["Gallbladder cancer", "Appendicitis", "Pancreatitis", "Cholelithiasis only"], 0,
  "Rupture of Rokitansky Aschoff sinuses — xanthogranulomatous cholecystitis; D/d: cancer. (Book p271)")
q(271, S6, "The management of chronic cholecystitis is:",
  ["Laparoscopic cholecystectomy", "Observation in all", "Antibiotics only", "Ursodeoxycholic acid"], 0,
  "Management: lap cholecystectomy. (Book p271)")
q(271, S6, "The causative organism of emphysematous cholecystitis is:",
  ["Clostridium", "E. coli only", "Salmonella only", "Staphylococcus only"], 0,
  "Emphysematous cholecystitis: causative organism — Clostridium. (Book p271)")
q(271, S6, "A predisposing factor for emphysematous cholecystitis is:",
  ["Diabetes", "Hypothyroidism", "Asthma", "Coeliac disease"], 0,
  "Predisposing factors: immunocompromised, diabetes. (Book p271)")
q(271, S6, "The clinical features of emphysematous cholecystitis are:",
  ["Pain, fever and sepsis", "Painless jaundice", "Chronic constipation", "Weight gain"], 0,
  "Clinical features: pain, fever, sepsis. (Book p271)")
q(271, S6, "On USG, emphysematous cholecystitis shows:",
  ["Gas within the gallbladder and in the wall of the gallbladder", "Post acoustic shadow", "A WES sign", "A Phrygian cap"], 0,
  "Investigation: USG (IOC) — gas within GB, wall of GB; also CECT. (Book p271)")
q(271, S6, "The management of emphysematous cholecystitis includes:",
  ["Nil per oral, IV fluids, broad-spectrum IV antibiotics and early lap cholecystectomy or tube cholecystostomy", "Observation only", "Oral antibiotics only", "ERCP first in all"], 0,
  "Management: nil per oral, IV fluids, IV antibiotics (broad spectrum), early lap cholecystectomy/tube cholecystostomy. (Book p271)")

S7 = "Mucocele and Gallstone Ileus"
q(271, S7, "A mucocele of the gallbladder is:",
  ["Aseptic dilatation of the gallbladder due to a stone impacted at the Hartmann pouch neck", "An infected gallbladder", "A cancer of the gallbladder fundus", "A Phrygian cap"], 0,
  "Mucocele of GB: aseptic dilatation of GB d/t stone impacted at Hartmann pouch neck. (Book p271)")
q(272, S7, "In a mucocele, the gallbladder distends because:",
  ["Bile is absorbed and mucus is produced by the wall", "Bile production increases", "The cystic duct is patent and fills", "The liver stops making bile"], 0,
  "Pathophysiology: impaction of stone in the neck of GB, bile absorbed and mucus produced by the wall. (Book p272)")
q(272, S7, "On examination, a mucocele of the gallbladder shows:",
  ["A distended gallbladder with pain", "No palpable gallbladder", "A fixed gallbladder mass without mobility", "Jaundice always"], 0,
  "Mucocele: O/E — distended GB, pain. (Book p272)")
q(272, S7, "The investigation of choice for a mucocele of the gallbladder is:",
  ["USG", "ERCP", "HIDA scan", "MRCP"], 0,
  "Mucocele: IOC — USG. (Book p272)")
q(272, S7, "The management of a mucocele of the gallbladder is:",
  ["Laparoscopic cholecystectomy", "Observation", "Ursodeoxycholic acid", "Percutaneous drainage only"], 0,
  "Mucocele: Mx — lap cholecystectomy. (Book p272)")
q(272, S7, "A mucocele that becomes infected turns into:",
  ["Empyema of the gallbladder", "A WES sign", "A Phrygian cap", "Charcot's triad"], 0,
  "Mucocele, if infected, becomes empyema of GB — Mx: lap cholecystectomy. (Book p272)")
q(272, S7, "Gallstone ileus is best described as:",
  ["A misnomer causing dynamic bowel obstruction", "A true ileus of the colon", "A static large bowel obstruction", "An inflammation of the gallbladder"], 0,
  "Gall stone ileus: misnomer; dynamic bowel obstruction. (Book p272)")
q(272, S7, "Gallstone ileus is secondary to:",
  ["A cholecystoduodenal fistula", "A cholecystocolic fistula only", "A stone in the common bile duct", "A Phrygian cap"], 0,
  "Gall stone ileus: a° to cholecystoduodenal fistula. (Book p272)")
q(272, S7, "The clinical features of gallstone ileus are those of bowel obstruction:",
  ["Obstipation, vomiting and pain", "Painless distension only", "Haematemesis only", "Chronic diarrhoea only"], 0,
  "Clinical features: bowel obstruction — obstipation, vomiting, pain. (Book p272)")
q(272, S7, "The initial investigation in gallstone ileus is:",
  ["X-ray abdomen erect and supine", "CT abdomen without contrast only", "ERCP", "HIDA scan"], 0,
  "Investigation: X-ray abdomen erect and supine — initial investigation. (Book p272)")
q(272, S7, "Rigler's triad in gallstone ileus consists of:",
  ["Small bowel obstruction, pneumobilia and a radiopaque shadow in the right iliac fossa", "Fever, jaundice and pain", "Murphy's sign, BoA's sign and fever", "Air under the diaphragm, free fluid and mass"], 0,
  "Rigler's triad: 1. Features of small bowel obstruction, 2. Pneumobilia (air in biliary tree), 3. Radiopaque shadow in right iliac fossa. (Book p272)")
q(272, S7, "Pneumobilia in Rigler's triad means:",
  ["Air in the biliary tree", "Air in the gallbladder only", "Air under the diaphragm", "Air in the appendix"], 0,
  "Rigler's triad: pneumobilia — air in the biliary tree. (Book p272)")
q(272, S7, "The investigation of choice for gallstone ileus is:",
  ["CECT", "Plain X-ray only", "USG only", "HIDA scan"], 0,
  "Investigation: CECT — IOC. (Book p272)")
q(272, S7, "The most common site of obstruction in gallstone ileus is:",
  ["The last 2 feet (60 cm) of the ileum", "The duodenum", "The colon", "The jejunal flexure"], 0,
  "M/c site of obstruction: last 2 feet / 60cm of ileum. (Book p272)")
q(272, S7, "Rarely, a gallstone causing gastric outlet obstruction is called:",
  ["Bouveret syndrome", "Mirizzi syndrome", "Charcot's triad", "A WES sign"], 0,
  "Rarely, stone causing gastric outlet obstruction: Bouveret syndrome. (Book p272)")
q(273, S7, "The first step in managing gallstone ileus is:",
  ["Emergency laparotomy", "ERCP", "Observation for 48 hours", "Oral laxatives"], 0,
  "Management: 1. Emergency laparotomy. (Book p273)")
q(273, S7, "At laparotomy for gallstone ileus, if there is NO peritonitis or perforation, the stone is:",
  ["Milked or crushed and taken beyond the ileocaecal junction", "Left in situ", "Removed only by resection", "Dissolved with bile salts"], 0,
  "Management: no peritonitis/perforation — milk the stone/crush the stone, taken beyond the ileocaecal junction. (Book p273)")
q(273, S7, "At laparotomy for gallstone ileus with peritonitis or perforation, the management is:",
  ["Resection and anastomosis", "Milking the stone only", "Drainage alone", "Observation"], 0,
  "Management: peritonitis/perforation — resection and anastomosis. (Book p273)")
q(273, S7, "When the patient is stable, the second operation for gallstone ileus is:",
  ["Cholecystectomy and repair of the fistula", "A second laparotomy for milking", "ERCP", "No further surgery"], 0,
  "Management: a. When patient is stable — 2nd surgery: cholecystectomy and repair of fistula. (Book p273)")

S8 = "Mirizzi Syndrome"
q(273, S8, "Mirizzi syndrome is due to:",
  ["Inflammation", "A congenital stricture", "A stone in the ampulla", "Cirrhosis"], 0,
  "Mirizzi syndrome: d/t inflammation. (Book p273)")
q(273, S8, "In Mirizzi syndrome, the inflamed gallbladder:",
  ["Adheres to the common bile duct and pushes it", "Adheres to the stomach", "Adheres to the colon only", "Necroses completely"], 0,
  "Mirizzi syndrome: GB adheres to CBD and pushes the CBD. (Book p273)")
q(273, S8, "Later, Mirizzi syndrome can progress to:",
  ["Fistula formation with obstructive jaundice", "Gallstone ileus", "Bouveret syndrome", "A WES sign"], 0,
  "Mirizzi syndrome: pushes the CBD — later, fistula formation, obstructive jaundice. (Book p273)")
q(273, S8, "The clinical features of Mirizzi syndrome are:",
  ["Pain and jaundice", "Painless mass only", "Fever with rigors only", "Haematemesis"], 0,
  "Clinical features: pain, jaundice. (Book p273)")
q(273, S8, "The investigation of choice for Mirizzi syndrome is:",
  ["MRCP", "ERCP", "USG alone", "Plain X-ray"], 0,
  "Investigation: MRCP — IOC. (Book p273)")
q(273, S8, "MRCP stands for:",
  ["Magnetic resonance cholangiopancreatography", "Magnetic retrograde cholangiography with puncture", "Modified radio contrast pneumography", "Magnetic resonance of the common bile duct only"], 0,
  "MRCP — magnetic resonance cholangio pancreatography; a non-invasive diagnostic test. (Book p273)")
q(273, S8, "MRCP is a:",
  ["Non-invasive diagnostic test", "Invasive test requiring a side-viewing scope", "Therapeutic procedure", "Biopsy technique"], 0,
  "MRCP: non-invasive diagnostic test. (Book p273)")
q(273, S8, "The management of Mirizzi syndrome is:",
  ["Laparoscopic cholecystectomy", "ERCP with sphincterotomy", "Observation", "Percutaneous drainage only"], 0,
  "Management: lap cholecystectomy. (Book p273)")
q(273, S8, "A partial cholecystectomy in Mirizzi syndrome is done for:",
  ["A densely adherent gallbladder", "A small gallbladder", "A Phrygian cap", "A porcelain gallbladder"], 0,
  "Management: partial cholecystectomy — densely adherent GB. (Book p273)")

# ------------------------------------------------------------------ p273-275
S9 = "Choledocholithiasis"
q(273, S9, "Stones in the common bile duct are secondary to gallbladder stones in what proportion of cases?",
  ["90%", "10%", "50%", "99%"], 0,
  "Choledocholithiasis: stones in CBD — 90% are a° to GB stones. (Book p273)")
q(273, S9, "Primary CBD stones account for what proportion of choledocholithiasis?",
  ["10%", "90%", "50%", "1%"], 0,
  "Stones in CBD: 10% — primary CBD stones. (Book p273)")
q(273, S9, "Primary CBD stones are:",
  ["Formed in the CBD and are brown pigment stones", "Formed in the gallbladder", "Pure cholesterol stones", "Always radiolucent"], 0,
  "Primary CBD stones: formed in CBD, brown pigment stone. (Book p273)")
q(274, S9, "Choledocholithiasis may present as:",
  ["Asymptomatic", "Always with Charcot's triad", "Always with shock", "Never with jaundice"], 0,
  "Clinical features: asymptomatic. (Book p274)")
q(274, S9, "Obstructive jaundice in choledocholithiasis is due to:",
  ["Obstruction of the common bile duct", "Haemolysis", "Cirrhosis", "A Phrygian cap"], 0,
  "Clinical features: obstructive jaundice (d/t obstruction of CBD). (Book p274)")
q(274, S9, "Charcot's triad is seen in:",
  ["Cholangitis (inflammation of the biliary tree)", "Cholecystitis only", "Gallstone ileus", "Pancreatitis only"], 0,
  "Charcot's triad: seen in cholangitis (inflammation of biliary tree). (Book p274)")
q(274, S9, "Charcot's triad consists of:",
  ["Intermittent pain, intermittent jaundice and intermittent fever", "Fever, shock and altered sensorium", "Pain, mass and jaundice", "Vomiting, obstipation and pain"], 0,
  "Charcot's triad: intermittent pain, intermittent jaundice, intermittent fever. (Book p274)")
q(274, S9, "Reynold's pentad is:",
  ["Charcot's triad plus shock/hypotension and altered mental status", "Charcot's triad only", "A triad of pain, fever and mass", "Pentad of Rigler's triad plus two signs"], 0,
  "Reynold's pentad: Charcot's triad + shock/hypotension + altered mental status. (Book p274)")
q(274, S9, "The investigation of choice for choledocholithiasis is:",
  ["MRCP", "ERCP", "USG alone", "HIDA scan"], 0,
  "Investigation: MRCP — IOC. (Book p274)")
q(274, S9, "The investigation of choice for CBD microliths is:",
  ["EUS (endoscopic ultrasound)", "Plain X-ray", "HIDA scan", "Barium meal"], 0,
  "Investigation: IOC for CBD microliths — EUS (endoscopic ultrasound). (Book p274)")
q(274, S9, "A patient with NO history of cholangitis/pancreatitis, NORMAL LFTs and a CBD diameter of 6 mm or less on USG has:",
  ["A low risk of CBD stones — proceed to lap cholecystectomy", "A high risk needing ERCP", "A medium risk needing MRCP", "No need for any imaging"], 0,
  "Risk factors table: low risk — history (−), LFT normal, CBD diameter ≤6 mm — lap chole. (Book p274)")
q(274, S9, "A medium risk of CBD stone (history of cholangitis/pancreatitis, LFT 2x normal, CBD 8-10 mm) requires:",
  ["MRCP before surgery", "ERCP immediately", "No further evaluation", "Only USG follow-up"], 0,
  "Risk factors table: medium/high risk — MRCP before Sx. (Book p274)")
q(274, S9, "A HIGH risk of CBD stone is indicated by:",
  ["History of cholangitis/pancreatitis with jaundice, LFT 2x normal and CBD greater than 10 mm", "A normal LFT and a 5 mm CBD", "An asymptomatic patient with no history", "A 7 mm CBD with no history"], 0,
  "Risk factors table: high — history + jaundice (+), LFT 2x (N), CBD >10 mm — MRCP before Sx. (Book p274)")
q(274, S9, "If CBD stones are detected BEFORE lap cholecystectomy, the management is:",
  ["ERCP followed by lap cholecystectomy", "Lap cholecystectomy alone", "Open choledochotomy only", "Observation"], 0,
  "Management: 1. If CBD stones detected before lap cholecystectomy — ERCP, followed by lap cholecystectomy. (Book p274)")
q(274, S9, "ERCP stands for:",
  ["Endoscopic retrograde cholangiopancreatography", "Endoscopic resection of the common bile duct", "External radiocontrast cholangiography", "Elective retrograde colonic puncture"], 0,
  "ERCP: endoscopic retrograde cholangiopancreatography. (Book p274)")
q(274, S9, "During ERCP, the cut (sphincterotomy) is made at the:",
  ["11 o'clock position in the Ampulla of Vater", "3 o'clock position", "12 o'clock position", "6 o'clock position"], 0,
  "ERCP: cut made at 11 o'clock position in the Ampulla of Vater. (Book p274)")
q(274, S9, "After dye is injected during ERCP, it:",
  ["Delineates the biliary tree", "Dissolves the stones", "Prevents pancreatitis", "Removes the stones"], 0,
  "ERCP: dye is injected and delineates the biliary tree; advantage — diagnostic + therapeutic. (Book p274)")
q(274, S9, "The advantage of ERCP is that it is:",
  ["Both diagnostic and therapeutic", "Only diagnostic", "Only therapeutic", "Only a biopsy tool"], 0,
  "ERCP: Adv — diagnostic + therapeutic. (Book p274)")
q(274, S9, "The most common complication of ERCP is:",
  ["Pancreatitis", "Duodenal perforation only", "Haemorrhage only", "Biliary stricture only"], 0,
  "ERCP complication: pancreatitis (m/c), duodenal perforation. (Book p274)")
q(275, S9, "If CBD stones are detected DURING lap cholecystectomy, the procedure continues with:",
  ["Laparoscopic exploration of the CBD and stone removal", "Aborting the operation and sending for ERCP later in all", "Open conversion in all", "No further workup"], 0,
  "Management: 2. CBD stones detected during lap cholecystectomy — lap exploration of CBD and stone removal. (Book p275)")
q(275, S9, "After laparoscopic CBD exploration and stone removal, the next step is:",
  ["Insertion of a T-tube", "Immediate removal of the T-tube", "No tube at all", "ERCP the same day"], 0,
  "Management: insert T-tube. (Book p275)")
q(275, S9, "A T-tube cholangiogram is done:",
  ["7-10 days after insertion", "On the day of surgery", "After 3 months", "After 2 weeks always"], 0,
  "Management: T-tube cholangiogram at 7-10 days. (Book p275)")
q(275, S9, "If the T-tube cholangiogram shows residual stones, the T-tube is:",
  ["Retained for 2-3 weeks to form a channel, then choledoscope is used to remove stones (Burhenne technique)", "Removed immediately", "Replaced with a new one", "Clipped off"], 0,
  "Management: residual stones present — retain T-tube for 2-3 weeks, forms a channel, choledoscope to remove stones — Burhenne technique. (Book p275)")
q(275, S9, "The Burhenne technique involves:",
  ["Removing stones with a choledoscope through the matured T-tube tract", "Milking stones beyond the ileocaecal junction", "ERCP with sphincterotomy", "Open choledochotomy without a tube"], 0,
  "Burhenne technique: retain T-tube 2-3 weeks, channel forms, choledoscope removes the stones. (Book p275)")
q(275, S9, "If the T-tube cholangiogram shows NO residual stones, the T-tube is:",
  ["Removed", "Retained for 3 months", "Replaced", "Clipped"], 0,
  "Management: residual stones absent — remove T-tube. (Book p275)")
q(275, S9, "CBD stones detected AFTER lap cholecystesis present with:",
  ["Pain, fever and jaundice", "Painless distension", "Weight loss only", "Chronic diarrhoea only"], 0,
  "Management: 3. CBD stones detected after lap cholecystectomy — presents with pain, fever, jaundice. (Book p275)")
q(275, S9, "A CBD stone presenting within 2 years of lap cholecystectomy is classified as:",
  ["Residual / retained CBD stone", "Recurrent / primary CBD stone", "A mucocele", "A Phrygian cap"], 0,
  "Within 2 yrs of lap cholecystectomy — residual/retained CBD. (Book p275)")
q(275, S9, "A CBD stone presenting MORE than 2 years after lap cholecystectomy is classified as:",
  ["Recurrent / primary CBD stone", "Residual / retained CBD stone", "A gallbladder stone", "A brown pigment stone only"], 0,
  ">2 yrs of lap cholecystectomy — recurrent/primary CBD stones. (Book p275)")
q(275, S9, "The management of CBD stones after lap cholecystectomy is:",
  ["ERCP with sphincterotomy", "Re-do laparotomy in all", "Observation", "HIDA scan"], 0,
  "Management: Mx — ERCP + sphincterotomy. (Book p275)")

# ------------------------------------------------------------------ units
def first_page(label):
    for x in Q:
        if x["sec"] == label:
            return x["page"]
    return 0


UNIT_DEFS = [
    (S1, "A distended pyriform gallbladder moves side to side and hints at periampullary cancer or mucocele, while a fixed non-pyriform mass whispers gallbladder cancer. Calot's triangle — cystic artery, cystic duct, common hepatic duct — hides the cystic lymph node of Lund, the sentinel node, and is the field dissected for the critical view of safety where the cystic artery and duct are clipped before the gallbladder comes out. Watch for Moynihan's hump: a tortuous right hepatic artery that masquerades in Calot's triangle and bleeds when mistaken."),
    (S2, "Work above the danger line: the cystic plate, continuous with the capsule of segments 4 and 5, is exposed at the critical view of safety; Rouviere's sulcus on the undersurface marks the right posterior sectoral pedicle, and the R4U line — sulcus to segment 4 base — keeps the CBD below it out of the dissection. The gallbladder has no submucosa but rich subserosal lymphatics, which is how its cancer seeds the liver, and the Phrygian cap, a folded fundus, needs no operation."),
    (S3, "The gallbladder stores, mucins and concentrates bile — and it makes stones. Pure cholesterol stones are over 90% cholesterol and solitary, mixed stones rule overall, and pigment stones split: brown ones born of infected bile (ascariasis, clonorchiasis, cholangitis) with calcium palmitate, stearate and bilirubinate, black ones of haemolysis (G6PD, sickle cell, spherocytosis) built on an insoluble bilirubin polymer. Lithogenic bile, nucleation and stasis — obesity, ileal resection, infection, pregnancy, OCP, vagotomy — are the three engines of stone formation."),
    (S4, "Nine out of ten stones are radiolucent — the exceptions flash the seagull sign (bircusped) or the mercedes Benz sign (trircusped), and USG, the IOC, catches them by their post acoustic shadow, absent in polyps. Silent stones are observed, but the porcelain gallbladder (5-7% cancer risk), a polyp over 1 cm, the Salmonella typhi carrier, the diabetic, the bariatric candidate in an endemic zone and the stone over 2 cm all go to theatre. Acute cholecystitis — Murphy's sign, BoA's sign over the 10th rib, the Tokyo criteria A plus B suspecting and the imaging confirming — runs from mild Grade I to organ-failing Grade III, with HIDA showing the non-visualised gallbladder between."),
    (S5, "Grade II is antibiotics and support with early lap cholecystectomy where the technique exists, otherwise tube cholecystostomy to decompress and delay; Grade III splits on negative predictive factors — early lap cholecystectomy in the fit at an advanced centre, drainage and delayed surgery for good performance status, and observation for the poor. Acalculous cholecystitis strikes the ICU patient, the prolonged-TPN patient, post CABG and septic — same signs, same USG, and when it fails to improve it needs the gallbladder out or a tube in."),
    (S6, "Chronic cholecystitis is the story of repeated attacks — the WES sign on USG, clefts and chronic cells on the slide, and Rokitansky Aschoff sinuses that, rupturing, make xanthogranulomatous cholecystitis, a great imitator of cancer. Emphysematous cholecystitis is Clostridium in the diabetic and immunocompromised: gas in the wall on USG, sepsis in the history, and early lap cholecystectomy or drainage after broad-spectrum antibiotics."),
    (S7, "A stone impacted at the Hartmann pouch neck turns the gallbladder into a mucocele — aseptic, distended, mucus-filled — that becomes an empyema when infected. When the same stone grinds a cholecystoduodenal fistula, the largest one travels to the terminal ileum and causes gallstone ileus: a misnomer, really a dynamic obstruction with Rigler's triad (SBO, pneumobilia, radiopaque shadow in the right iliac fossa) on the film and CECT as the IOC. At laparotomy, milk or crush the stone unless peritonitis demands resection, and return for cholecystectomy and fistula repair when stable."),
    (S8, "Mirizzi syndrome is the inflamed gallbladder glued to the common bile duct, pushing it until it fistulises and obstructs — pain plus jaundice. MRCP, the non-invasive IOC, makes the diagnosis, and lap cholecystectomy (partial when the gallbladder is densely adherent) is the treatment."),
    (S9, "CBD stones are 90% secondaries from the gallbladder and 10% primary brown pigment stones. They sit silently or bring obstructive jaundice, Charcot's triad in cholangitis and Reynold's pentad when shock and confusion join. The risk table steers the low-risk straight to lap cholecystectomy and the rest to MRCP; ERCP before surgery (cut at 11 o'clock, pancreatitis its commonest complication), T-tube and the Burhenne technique when stones are found at operation, and ERCP with sphincterotomy when they appear afterwards — within 2 years a retained stone, beyond, a recurrent one."),
]

UNITS = []
for i, (title, guide) in enumerate(UNIT_DEFS, 1):
    UNITS.append({
        "id": f"SURG-U37-{i}",
        "ch": 37,
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
with open("data/ch37.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
print(f"ch37: {len(Q)} questions, {len(UNITS)} units")
