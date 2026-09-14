#!/usr/bin/env python3
"""Build data/ch38.json — ch38 Gall Bladder and Bile Ducts: Part 2 (Marrow Surgery Ed 8, book p276-284)."""
import json

Q = []


def q(page, sec, text, opts, ans, exp):
    Q.append({
        "id": f"SURG-C38-{len(Q)+1:03d}",
        "sec": sec,
        "page": page,
        "q": text,
        "opts": opts,
        "ans": ans,
        "exp": exp,
    })


# ------------------------------------------------------------------ p276
S1 = "Laparoscopic Cholecystectomy"
q(276, S1, "In laparoscopic cholecystectomy, the surgeon stands on the:",
  ["Left", "Right", "Foot of the bed", "Head of the bed"], 0,
  "Position: surgeon — left. (Book p276)")
q(276, S1, "In laparoscopic cholecystectomy, the assistant stands on the:",
  ["Left", "Right", "Foot of the bed", "Head of the bed"], 0,
  "Position: assistant — left. (Book p276)")
q(276, S1, "The patient's position for laparoscopic cholecystectomy is:",
  ["Reverse Trendelenburg with right side up", "Trendelenburg with left side up", "Lateral position", "Prone"], 0,
  "Position: patient — reverse Trendelenburg and right up. (Book p276)")
q(276, S1, "In the safe method of laparoscopic cholecystectomy, which structure must be visualized before proceeding with surgery?",
  ["The bile duct, status of Rouviere, hepatic artery, umbilical fissure and enteric/duodenum",
   "Only the cystic duct", "Only the cystic artery", "Only the gallbladder fundus"], 0,
  "Safe method: bile duct, status of rouviere, hepatic artery, umbilical fissure, enteric/duodenum — to be visualized before proceeding with Sx. (Book p276)")
q(276, S1, "The traditional laparoscopic cholecystectomy uses:",
  ["Multiple ports", "A single incision", "No ports", "One port and one mini-laparotomy"], 0,
  "Traditional lap cholecystectomy: multiple ports. (Book p276)")
q(276, S1, "In traditional laparoscopic cholecystectomy, the epigastric port is used for:",
  ["The right hand", "The left hand", "The camera", "Gallbladder retraction"], 0,
  "Traditional lap cholecystectomy: epigastric port (R hand). (Book p276)")
q(276, S1, "In traditional laparoscopic cholecystectomy, the right hypochondrial port is used for:",
  ["The left hand", "The right hand", "The camera", "Gallbladder retraction"], 0,
  "Traditional lap cholecystectomy: (R) hypochondrial port (L hand). (Book p276)")
q(276, S1, "The 4th port in traditional laparoscopic cholecystectomy is used for:",
  ["Retraction of the gallbladder", "The camera", "The right hand", "Aspiration of bile"], 0,
  "Traditional lap cholecystectomy: 4th port — retraction and (GB). (Book p276)")
q(276, S1, "The camera port in traditional laparoscopic cholecystectomy is:",
  ["The infraumbilical port", "The epigastric port", "The hypochondrial port", "The 4th port"], 0,
  "Traditional lap cholecystectomy: infraumbilical port — camera. (Book p276)")
q(276, S1, "SILS laparoscopic cholecystectomy is:",
  ["A single incision procedure", "A multi-port procedure", "An open procedure", "A robot-only procedure"], 0,
  "SILS lap cholecystectomy: single incision. (Book p276)")
q(276, S1, "The disadvantage of SILS laparoscopic cholecystectomy is:",
  ["Increased risk of incisional hernia", "No risk at all", "Worsened vision", "Increased bleeding"], 0,
  "SILS lap cholecystectomy: Disadv — increased risk of incisional hernia. (Book p276)")
q(276, S1, "Bailout strategies in laparoscopic cholecystectomy are used in the presence of:",
  ["A frozen Calot's triangle with inflammation and adhesions", "A normal Calot's triangle", "A Phrygian cap", "Radiolucent stones"], 0,
  "Bailout strategies: used in the presence of frozen Calot's — increased inflammation and adhesions, difficulty in dissection. (Book p276)")
q(276, S1, "Which of the following is a bailout strategy in laparoscopic cholecystectomy?",
  ["Convert to open procedure (4-5%)", "Continue with the same dissection", "Give only antibiotics", "Repeat the operation in 2 days"], 0,
  "Strategies: abort the procedure, convert to open procedure (4-5%), carry out tube cholecystostomy, carry out subtotal cholecystectomy (used in Mirizzi syndrome), fundus first procedure. (Book p276)")
q(276, S1, "Subtotal cholecystectomy as a bailout strategy is used in:",
  ["Mirizzi syndrome", "Phrygian cap", "Acalculous cholecystitis only", "Gallstone ileus"], 0,
  "Strategies: carry out subtotal cholecystectomy — used in Mirizzi syndrome. (Book p276)")
q(276, S1, "The most common complication of laparoscopic cholecystectomy is:",
  ["Right shoulder tip pain", "Bowel injury", "Bile duct stricture", "Residual stones"], 0,
  "Complications: right shoulder tip pain — m/c. (Book p276)")
q(276, S1, "Shoulder tip pain after laparoscopic cholecystectomy is due to:",
  ["Retained CO2 below the right dome of the diaphragm", "Bile in the peritoneum", "Diaphragmatic hernia", "Shoulder muscle injury"], 0,
  "Shoulder tip pain: d/t retained CO2 below right dome of diaphragm — referred pain. (Book p276)")
q(276, S1, "Other complications of laparoscopic cholecystectomy include:",
  ["Bleeding and injury to bile duct", "Pneumothorax only", "Appendicitis", "Renal colic"], 0,
  "Complications: bleeding, injury to bile duct. (Book p276)")

S2 = "Complications: Bile Duct Injury"
q(277, S2, "Which of the following is listed as a complication of laparoscopic cholecystectomy?",
  ["Injury to bowel", "Hypoglycaemia", "Renal colic", "Shoulder arthropathy"], 0,
  "Complications (continued on p277): injury to bowel. (Book p277)")
q(277, S2, "Residual stones after cholecystectomy are defined as those presenting:",
  ["Within 2 years", "After 5 years", "After 10 years", "Immediately only"], 0,
  "Complications: residual stones — within 2 yrs. (Book p277)")
q(277, S2, "Recurrent stones after cholecystectomy are defined as those presenting:",
  ["More than 2 years later", "Within 1 year", "Within 6 months", "Immediately only"], 0,
  "Complications: recurrent stones — >2 yrs. (Book p277)")
q(277, S2, "The diagnosis of residual/recurrent stones after cholecystectomy is made by:",
  ["MRCP", "Plain X-ray", "Barium meal", "HIDA scan"], 0,
  "Residual/recurrent stones: Dx — MRCP. (Book p277)")
q(277, S2, "Residual/recurrent stones after cholecystectomy are managed by:",
  ["ERCP with sphincterotomy", "Re-do cholecystectomy", "Observation only", "Open choledochotomy in all"], 0,
  "Residual/recurrent stones: Mx — ERCP with sphincterotomy. (Book p277)")
q(277, S2, "A late complication of laparoscopic cholecystectomy among the following is:",
  ["Stricture to the common hepatic duct / common bile duct", "Early shoulder pain only", "Retained CO2", "Hypothermia"], 0,
  "Complications: stricture to common hepatic duct/common bile duct. (Book p277)")
q(277, S2, "A partial tear of the common bile duct recognized DURING surgery is managed by:",
  ["Repair with absorbable suture", "Choledochojejunostomy", "T-tube anastomosis", "Observation"], 0,
  "Bile duct injury, aware during Sx: 1. Partial tear — repair with absorbable suture. (Book p277)")
q(277, S2, "A complete transection of the common bile duct WITHOUT loss of segment is managed by:",
  ["Anastomoses with T-tube", "Choledochojejunostomy", "Repair with absorbable suture", "No surgery"], 0,
  "Aware during Sx: 2. Complete transection without loss of segment — anastomoses with T-tube. (Book p277)")
q(277, S2, "A complete transection of the common bile duct WITH loss of segment is managed by:",
  ["Closing the distal end and choledochojejunostomy", "Primary end to end anastomosis", "T-tube alone", "Observation"], 0,
  "Aware during Sx: 3. Complete transection with loss of segment — close distal end and choledochojejunostomy. (Book p277)")
q(277, S2, "A minor bile leak in the drain that decreases with time in a stable patient after cholecystectomy is managed by:",
  ["Observation", "Immediate re-exploration", "ERCP in all", "Emergency laparotomy"], 0,
  "Aware in post-op period: minor bile leak in drain, amount decreases with time, stable patient — observe. (Book p277)")
q(277, S2, "A symptomatic bile leak in the post-operative period presents with:",
  ["Fever, jaundice and pain with an increasing leak", "Isolated constipation", "Only shoulder pain", "Only anaemia"], 0,
  "Symptomatic: fever, jaundice, pain, with increased leak. (Book p277)")
q(277, S2, "The workup of a symptomatic post-operative bile leak includes:",
  ["CBC (raised TLC), USG abdomen (collection below liver) and confirmation by MRCP", "Only a plain X-ray", "Only USG", "ERCP first without MRCP"], 0,
  "Work up: CBC (raised TLC), USG abdomen (collection below liver), confirmation — MRCP. (Book p277)")
q(277, S2, "A bile leak recognized within 1-2 days of surgery is managed by:",
  ["Re-exploration and repair", "Pigtail catheter only", "Observation for a month", "ERCP with stenting in all"], 0,
  "Bile leak: within 1-2 days post-Sx — re explore and repair. (Book p277)")
q(277, S2, "A bile leak recognized MORE than 2 days after surgery is first managed by:",
  ["Pigtail catheter, then ERCP with stenting", "Immediate re-exploration in all", "Observation only", "Oral antibiotics only"], 0,
  "Bile leak: >2 days post-Sx — pig tail catheter (first intervention), then ERCP + stenting. (Book p277)")

# ------------------------------------------------------------------ p278
S3 = "Bismuth and Strasberg Classification of Bile Duct Injury"
q(278, S3, "In the Strasberg classification, a cystic duct leak or minor leak is type:",
  ["A", "B", "C", "D"], 0,
  "Bismuth and Strasberg classification: cystic duct leak or minor leak — Strasberg A. (Book p278)")
q(278, S3, "Occlusion of an aberrant right hepatic duct is Strasberg type:",
  ["B", "A", "C", "D"], 0,
  "Classification: occlusion of an aberrant (R) hepatic duct (RHD) — Strasberg B. (Book p278)")
q(278, S3, "A leak from an aberrant right hepatic duct is Strasberg type:",
  ["C", "A", "B", "D"], 0,
  "Classification: leak from an aberrant RHD — Strasberg C. (Book p278)")
q(278, S3, "A lateral injury to the common bile duct is Strasberg type:",
  ["D", "A", "B", "C"], 0,
  "Classification: lateral injury to CBD — Strasberg D. (Book p278)")
q(278, S3, "A common hepatic duct stricture with a stump GREATER than 2 cm is:",
  ["Bismuth Type I (Strasberg E1)", "Bismuth Type II (Strasberg E2)", "Bismuth Type III (Strasberg E3)", "Bismuth Type IV (Strasberg E4)"], 0,
  "Classification: CHD stricture, stump >2 cm — Bismuth Type I / Strasberg E1. (Book p278)")
q(278, S3, "A common hepatic duct stricture with a stump LESS than 2 cm is:",
  ["Bismuth Type II (Strasberg E2)", "Bismuth Type I (Strasberg E1)", "Bismuth Type III (Strasberg E3)", "Bismuth Type V (Strasberg E5)"], 0,
  "Classification: CHD stricture, stump <2 cm — Bismuth Type II / Strasberg E2. (Book p278)")
q(278, S3, "A hilar stricture WITH preserved confluence is:",
  ["Bismuth Type III (Strasberg E3)", "Bismuth Type IV (Strasberg E4)", "Bismuth Type I (Strasberg E1)", "Bismuth Type V (Strasberg E5)"], 0,
  "Classification: hilar stricture with preserved confluence — Bismuth Type III / Strasberg E3. (Book p278)")
q(278, S3, "A hilar stricture WITH involvement of the confluence is:",
  ["Bismuth Type IV (Strasberg E4)", "Bismuth Type III (Strasberg E3)", "Bismuth Type II (Strasberg E2)", "Bismuth Type I (Strasberg E1)"], 0,
  "Classification: hilar stricture with involvement of confluence — Bismuth Type IV / Strasberg E4. (Book p278)")
q(278, S3, "A stricture to an aberrant right hepatic duct is:",
  ["Bismuth Type V (Strasberg E5)", "Bismuth Type IV (Strasberg E4)", "Bismuth Type III (Strasberg E3)", "Bismuth Type I (Strasberg E1)"], 0,
  "Classification: stricture to an aberrant RHD — Bismuth Type V / Strasberg E5. (Book p278)")

S4 = "Gall Stones in Pregnancy"
q(278, S4, "Gallstones form more readily in pregnancy because of hormonal changes that:",
  ["Increase cholesterol secretion", "Decrease cholesterol secretion", "Stop bile production", "Increase gallbladder motility"], 0,
  "Gall stones in pregnancy: hormonal changes increase cholesterol secretion. (Book p278)")
q(278, S4, "Progesterone in pregnancy promotes gallstone formation by:",
  ["Decreasing bile acid secretion and slowing gallbladder emptying", "Increasing bile acid secretion", "Speeding gallbladder emptying", "Dissolving cholesterol"], 0,
  "Progesterone decreases bile acid secretion and slows GB emptying — stones increase. (Book p278)")
q(278, S4, "The investigation of choice for gallstones in pregnancy is:",
  ["USG", "CECT", "ERCP", "HIDA scan"], 0,
  "Gall stones in pregnancy: IOC — USG. (Book p278)")
q(278, S4, "Mild gallstone disease in the FIRST trimester of pregnancy is managed by:",
  ["Conservative treatment", "Laparoscopic cholecystectomy", "Open cholecystectomy", "ERCP with sphincterotomy"], 0,
  "Management: first trimester — mild cases, conservative. (Book p278)")
q(278, S4, "NSAIDs are avoided in the first trimester of pregnancy because they:",
  ["Cause premature closure of the ductus arteriosus", "Dissolve the stones", "Cause a Phrygian cap", "Increase bile acid secretion"], 0,
  "First trimester: NSAIDs avoided — to prevent premature closure of ductus arteriosus. (Book p278)")
q(278, S4, "Laparoscopic cholecystectomy in pregnancy is ideally done in the:",
  ["Second trimester", "First trimester", "Third trimester", "Any time, trimester is irrelevant"], 0,
  "Management: second trimester — lap cholecystectomy. (Book p278)")
q(278, S4, "Gallstone disease in the THIRD trimester of pregnancy is managed by:",
  ["Non-operative management", "Laparoscopic cholecystectomy", "Open cholecystectomy", "ERCP with sphincterotomy"], 0,
  "Management: third trimester — non-operative Mx. (Book p278)")
q(278, S4, "Laparoscopic appendectomy for appendicitis in pregnancy can be done in:",
  ["Any trimester", "Only the first trimester", "Only the second trimester", "Only the third trimester"], 0,
  "Note: lap appendectomy done in any trimester for appendicitis. (Book p278)")

# ------------------------------------------------------------------ p279-281
S5 = "Gallbladder Cancer"
q(279, S5, "What proportion of gallbladder cancers are associated with gallstones?",
  ["90%", "10%", "50%", "5%"], 0,
  "Risk factors: gall stones — 90% of GB cancer associated with GB stones. (Book p279)")
q(279, S5, "Which of the following is a risk factor for gallbladder cancer?",
  ["Salmonella typhi carrier", "Hypertension", "Asthma", "Coeliac disease"], 0,
  "Risk factors: Salmonella typhi carrier. (Book p279)")
q(279, S5, "A porcelain gallbladder is a risk factor for:",
  ["Gallbladder cancer", "Appendicitis", "Hernia", "Colonic diverticulosis"], 0,
  "Risk factors: porcelain gallbladder. (Book p279)")
q(279, S5, "Abnormal pancreatobiliary duct junction (APBDJ) raises the risk of:",
  ["Gallbladder cancer and cholangiocarcinoma", "Only breast cancer", "Only oral cancer", "Only skin cancer"], 0,
  "Risk factors: APBDJ — increased risk of GB cancer and cholangiocarcinoma. (Book p279)")
q(279, S5, "Heavy metal contamination of which substance is a risk factor for gallbladder cancer?",
  ["Water", "Air only", "Soil only", "Food packaging only"], 0,
  "Risk factors: heavy metal contamination of water. (Book p279)")
q(279, S5, "Which gallbladder polyp feature INCREASES the risk of cancer?",
  ["Adenomatous type, greater than 10 mm, or multiple polyps", "Cholesterol polyps", "A solitary 5 mm polyp", "A Phrygian cap"], 0,
  "GB polyp: adenomatous type, >10 mm/1 cm, multiple polyps increase risk. (Book p279)")
q(279, S5, "Cholesterol (strawberry) gallbladder polyps:",
  ["Do NOT increase the risk of cancer", "Always progress to cancer", "Cause Charcot's triad", "Are the m/c cause of Rigler's triad"], 0,
  "GB polyp: cholesterol polyps do not increase risk; the cholesterol/strawberry GB does not raise the risk of cancer. (Book p279)")
q(279, S5, "A gallbladder polyp LESS than 10 mm is managed by:",
  ["Monitoring with regular USG", "Immediate cholecystectomy", "Chemotherapy", "ERCP"], 0,
  "GB polyp: <10 mm size — monitor + regular USG. (Book p279)")
q(279, S5, "Gallbladder cancer is usually:",
  ["An adenocarcinoma", "A squamous cell carcinoma", "A sarcoma", "A lymphoma"], 0,
  "Types: adenocarcinoma — infiltrating, nodular and papillary. (Book p279)")
q(279, S5, "The most aggressive type of gallbladder adenocarcinoma is:",
  ["Infiltrating", "Papillary", "Nodular", "Cystic"], 0,
  "Types: infiltrating (most aggressive), nodular, papillary. (Book p279)")
q(279, S5, "A gallbladder cancer on examination presents as a GB mass that:",
  ["Does not retain the pyriform shape and has loss of mobility", "Moves side to side freely", "Is tender but mobile", "Is always radiolucent"], 0,
  "Clinical presentation: GB mass — does not retain pyriform shape, loss of mobility. (Book p279)")
q(279, S5, "In gallbladder cancer, jaundice is:",
  ["A late feature", "The earliest feature", "Never seen", "Seen only in metastasis"], 0,
  "Clinical presentation: jaundice — late feature. (Book p279)")
q(279, S5, "Direct invasion in gallbladder cancer occurs because the gallbladder fossa comprises:",
  ["Segments 4b and 5 of liver", "Segments 2 and 3", "Segments 7 and 8", "Segment 1 only"], 0,
  "Spread: direct invasion — gallbladder fossa comprises of 4b, 5th segments of liver. (Book p279)")
q(279, S5, "Lymphatic spread of gallbladder cancer occurs via:",
  ["Subserosal lymphatics to the liver", "The hepatic vein only", "The inferior vena cava", "The portal vein only"], 0,
  "Spread: lymphatic spread — subserosal lymphatics to liver. (Book p279)")
q(279, S5, "The most common site of haematogenous spread of gallbladder cancer is:",
  ["The liver", "The lung", "The bone", "The brain"], 0,
  "Spread: haematogenous spread — liver (m/c site), lung. (Book p279)")
q(280, S5, "The investigation of choice for gallbladder cancer is:",
  ["CECT", "Plain X-ray", "USG alone", "Barium meal"], 0,
  "Investigation: CECT — IOC. (Book p280)")
q(280, S5, "CECT is the investigation of choice for all of the following EXCEPT:",
  ["Gallbladder cancer", "GIST", "Renal cell cancer", "Appendicitis"], 0,
  "Note: CECT is IOC in GIST, GB cancer, renal cell cancer. (Book p280)")
q(280, S5, "FNAC / biopsy in gallbladder cancer is indicated for:",
  ["Metastasis or an indeterminate diagnosis", "Every incidental gallbladder polyp", "All porcelain gallbladders", "All gallstones"], 0,
  "FNAC/biopsy: indication — metastasis, indeterminate Dx. (Book p280)")
q(280, S5, "In gallbladder cancer staging, Tis means:",
  ["Carcinoma in situ", "Invasion of the serosa", "Invasion of the hepatic artery", "Invasion of perimuscular tissue"], 0,
  "Tumour staging: Tis — carcinoma in situ. (Book p280)")
q(280, S5, "T1a gallbladder cancer is:",
  ["Limited to the lamina propria", "Invasion into the muscularis", "Invasion of perimuscular tissue", "Invasion of the serosa and liver"], 0,
  "Staging: T1 — invasion into lamina propria or muscularis; T1a — limited to lamina propria. (Book p280)")
q(280, S5, "T1b gallbladder cancer is:",
  ["Invasion into the muscularis", "Limited to the lamina propria", "Invasion of perimuscular tissue", "Invasion of the hepatic artery"], 0,
  "Staging: T1b — invades into muscularis. (Book p280)")
q(280, S5, "T2 gallbladder cancer is:",
  ["Invasion of perimuscular tissue", "Invasion of the serosa and liver", "Carcinoma in situ", "Invasion of the main portal vein"], 0,
  "Staging: T2 — invasion of perimuscular tissue. (Book p280)")
q(280, S5, "T3 gallbladder cancer is:",
  ["Invasion of the serosa and liver", "Invasion of the hepatic artery", "Invasion of perimuscular tissue", "Carcinoma in situ"], 0,
  "Staging: T3 — invasion of serosa, liver. (Book p280)")
q(280, S5, "T4 gallbladder cancer is:",
  ["Invasion of the hepatic artery or main portal vein", "Invasion of the serosa only", "Carcinoma in situ", "Invasion limited to the lamina propria"], 0,
  "Staging: T4 — invasion of hepatic artery, main portal vein. (Book p280)")
q(280, S5, "T1a gallbladder cancer (above the muscle layer) is managed by:",
  ["Simple cholecystectomy, avoiding bile spillage", "Radical cholecystectomy", "Chemotherapy only", "No treatment"], 0,
  "Management: T1a — above muscle layer, simple cholecystectomy; bile spillage must be avoided. (Book p280)")
q(280, S5, "T1b and T2 gallbladder cancers are managed by:",
  ["Radical cholecystectomy", "Simple cholecystectomy only", "Observation", "Radiotherapy alone"], 0,
  "Management: T1b, T2 — radical cholecystectomy. (Book p280)")
q(280, S5, "Structures removed in radical cholecystectomy for gallbladder cancer include:",
  ["Gallbladder, segments 4b and 5 of liver, lymph nodes along the hepatoduodenal ligament, and CBD if involved or cancer near the neck",
   "Gallbladder alone", "Only the cystic duct", "Only segment 8"], 0,
  "Radical cholecystectomy: structures removed — GB, 4b, 5 segments of liver, lymph node along hepatoduodenal ligament, CBD (+/-) removed if involved / cancer near neck of GB. (Book p280)")
q(280, S5, "If anatomical resection is not done in radical cholecystectomy, the margin rule is:",
  ["A 2 cm rim around the gallbladder is removed", "No margin is needed", "A 5 mm rim", "The whole right lobe is removed"], 0,
  "Radical cholecystectomy: if anatomical resection is not done — a 2 cm rim around GB is removed. (Book p280)")
q(280, S5, "T3 and T4 gallbladder cancers are treated with:",
  ["Gemcitabine based chemotherapy", "Simple cholecystectomy", "Radiotherapy alone", "Observation"], 0,
  "Management: T3, T4 — gemcitabine based chemotherapy. (Book p280)")
q(280, S5, "After gemcitabine-based chemotherapy for T3/T4 gallbladder cancer, a GOOD response leads to:",
  ["Radical cholecystectomy", "Continued palliation only", "No further treatment", "Simple cholecystectomy"], 0,
  "Management: response — good, radical cholecystectomy. (Book p280)")
q(280, S5, "After gemcitabine-based chemotherapy for T3/T4 gallbladder cancer, a POOR response leads to:",
  ["Continued palliative treatment (chemo/radiotherapy)", "Radical cholecystectomy", "Simple cholecystectomy", "Observation for a year"], 0,
  "Management: response — poor, continue palliative Rx (chemo/radiotherapy). (Book p280)")
q(281, S5, "Post-operative chemotherapy for gallbladder cancer is:",
  ["Gemcitabine based", "Methotrexate based", "Cisplatin alone", "Not given at all"], 0,
  "Post Sx: chemotherapy — gemcitabine based. (Book p281)")
q(281, S5, "Post-operative radiotherapy in gallbladder cancer:",
  ["Decreases local recurrence", "Cures the disease", "Has no role", "Only treats distant metastasis"], 0,
  "Post Sx: radiotherapy — decreases local recurrence. (Book p281)")
q(281, S5, "The most important prognostic factor in gallbladder cancer is:",
  ["Depth (T staging)", "Age", "Gender", "Polyp size"], 0,
  "Prognostic factor: most important — depth, T-staging. (Book p281)")
q(281, S5, "Gallbladder cancer is monitored with:",
  ["CA 19-9", "AFP", "PSA", "CEA only"], 0,
  "Prognostic factor: monitoring — CA 19-9. (Book p281)")
q(281, S5, "CA 19-9 is used in:",
  ["Cholangiocarcinoma and pancreatic cancer", "Only breast cancer", "Only thyroid cancer", "Only prostate cancer"], 0,
  "Note: CA 19-9 used in cholangiocarcinoma and pancreatic cancer. (Book p281)")
q(281, S5, "If gallbladder cancer is diagnosed AFTER laparoscopic cholecystectomy, excision of the laparoscopic port sites:",
  ["Is NOT beneficial", "Is always curative", "Is mandatory in all", "Prevents local recurrence"], 0,
  "Note: cancer diagnosed post Sx — excision of laparoscopic ports are not beneficial. (Book p281)")

# ------------------------------------------------------------------ p281-282
S6 = "Extrahepatic Biliary Atresia"
q(281, S6, "Extrahepatic biliary atresia results from:",
  ["Inflammatory fibrosis leading to atresia of the duct", "A congenital absence of the liver", "Gallstone obstruction", "A Phrygian cap"], 0,
  "Extrahepatic biliary atresia: inflammatory fibrosis leads to atresia of duct, causing cirrhosis and liver failure. (Book p281)")
q(281, S6, "Extrahepatic biliary atresia is seen in:",
  ["Children", "Elderly only", "Only in pregnancy", "Only in neonatal hepatitis"], 0,
  "Seen in children. (Book p281)")
q(281, S6, "Extrahepatic biliary atresia is the:",
  ["Most common cause of liver transplantation in children", "Rarest cause of liver failure", "Cause of most gallstones", "Cause of Charcot's triad in adults"], 0,
  "M/c cause of liver Tx in children. (Book p281)")
q(281, S6, "In the Japanese and Anglo-Saxon classification, Type I biliary atresia is:",
  ["Atresia restricted to the common bile duct", "Atresia of the common hepatic duct", "Atresia of the right and left hepatic ducts", "Atresia of the entire intrahepatic tree"], 0,
  "Classification: Type I — atresia restricted to CBD. (Book p281)")
q(281, S6, "In Type IIa biliary atresia:",
  ["The gallbladder and common bile duct are patent", "The gallbladder, cystic duct and CBD are obliterated", "The hepatic ducts are atretic", "Only the cystic duct is atretic"], 0,
  "Type II: atresia of CHD; IIa — patent GB and CBD. (Book p281)")
q(281, S6, "In Type IIb biliary atresia:",
  ["The gallbladder, cystic duct and common bile duct are obliterated", "The gallbladder and CBD are patent", "Only the hepatic ducts are atretic", "The ampulla is atretic"], 0,
  "Type IIb: GB, cystic duct, CBD are obliterated. (Book p281)")
q(281, S6, "Type III biliary atresia involves:",
  ["Atresia of the right and left hepatic ducts and the entire extrahepatic biliary tree", "Atresia restricted to the CBD", "Only a diverticulum of the CBD", "Only the intraduodenal CBD"], 0,
  "Type III: atresia of (R) and (L) hepatic ducts and entire extrahepatic biliary tree. (Book p281)")
q(281, S6, "An associated anomaly of extrahepatic biliary atresia is:",
  ["Preduodenal portal vein", "A Phrygian cap", "A porcelain gallbladder", "Rigler's triad"], 0,
  "Associated anomalies: cardiac lesions, polysplenia, situs inversus, absent vena cava, pre duodenal portal vein. (Book p281)")
q(281, S6, "Which of the following is an associated anomaly of biliary atresia?",
  ["Situs inversus", "Hypertension", "Coeliac disease", "Asthma"], 0,
  "Associated anomalies include situs inversus (also cardiac lesions, polysplenia, absent vena cava, preduodenal portal vein). (Book p281)")
q(281, S6, "The clinical features of extrahepatic biliary atresia are:",
  ["Jaundice at birth with rapidly progressive liver failure and cirrhosis", "Painless jaundice with a mass", "Chronic diarrhoea only", "Pneumobilia"], 0,
  "Clinical features: jaundice at birth, liver failure and cirrhosis (rapid progression). (Book p281)")
q(281, S6, "Blood investigations in biliary atresia show:",
  ["Raised serum bilirubin and alkaline phosphatase", "Normal bilirubin with low alkaline phosphatase", "Only a raised WBC", "Only anaemia"], 0,
  "Investigation — blood investigations: raised S. bilirubin, raised alkaline phosphatase. (Book p281)")
q(282, S6, "The gold standard investigation in extrahepatic biliary atresia is:",
  ["Fasting USG", "Plain X-ray", "Barium meal", "HIDA scan"], 0,
  "Investigation: fasting USG — gold standard. (Book p282)")
q(282, S6, "MRCP in biliary atresia is:",
  ["Highly sensitive and specific", "Useless", "Only therapeutic", "Only for adults"], 0,
  "MRCP: highly sensitive and specific. (Book p282)")
q(282, S6, "A liver biopsy in biliary atresia:",
  ["Confirms the diagnosis, with inflammatory cells present in neonatal hepatitis", "Excludes the diagnosis in all", "Is never done", "Shows a Phrygian cap"], 0,
  "Liver biopsy: confirms Dx; rule out neonatal hepatitis — presence of inflammatory cells. (Book p282)")
q(282, S6, "A differential diagnosis of extrahepatic biliary atresia is:",
  ["Alagille syndrome (biliary atresia, congenital heart disease, skeletal abnormalities)", "Gallstone ileus", "Bouveret syndrome", "Mirizzi syndrome"], 0,
  "D/d: neonatal hepatitis, Alagille syndrome — biliary atresia, congenital heart disease, skeletal abnormalities. (Book p282)")
q(282, S6, "Type I extrahepatic biliary atresia is managed by:",
  ["Hepaticojejunostomy", "Kasai procedure", "Liver transplantation only", "Observation"], 0,
  "Management: Type I — hepaticojejunostomy. (Book p282)")
q(282, S6, "The Kasai procedure (for Type II/III biliary atresia) consists of:",
  ["Portoenterostomy with jejunal anastomosis at the level of the porta hepatis", "Cholecystectomy", "Choledochojejunostomy", "ERCP with stenting"], 0,
  "Management: Type II, III — Kasai procedure: portoenterostomy, jejunal anastomosis at the level of porta hepatis. (Book p282)")
q(282, S6, "In what proportion of biliary atresia does the disease progress despite surgery, leading to liver failure requiring transplantation?",
  ["20-30%", "90%", "1%", "50-70%"], 0,
  "Management: 20-30% — progressive disease despite Sx, live failure, Mx transplantation. (Book p282)")

# ------------------------------------------------------------------ p282-283
S7 = "Choledochal Cysts"
q(282, S7, "A choledochal cyst is:",
  ["Dilatation of the biliary tree", "A stone in the common bile duct", "A cyst of the gallbladder fundus", "A Phrygian cap"], 0,
  "Choledochal cysts: dilatation of biliary tree. (Book p282)")
q(282, S7, "Jaundice in choledochal cysts is due to:",
  ["Ineffective drainage", "Haemolysis", "Cirrhosis", "A Phrygian cap"], 0,
  "Choledochal cysts: dilatation leads to ineffective drainage, causing jaundice. (Book p282)")
q(282, S7, "Choledochal cysts raise the risk of cholangiocarcinoma by:",
  ["10%", "50%", "1%", "90%"], 0,
  "Choledochal cysts: risk of cholangiocarcinoma increased by 10%. (Book p282)")
q(282, S7, "In the Todani / modified Alonso-Lej classification, Type I choledochal cyst is:",
  ["Diffuse common bile duct dilatation (most common)", "A diverticulum of the CBD", "Intraduodenal CBD dilatation", "Intrahepatic radical dilatation"], 0,
  "Todani classification: Type I — diffuse CBD dilatation, m/c. (Book p282)")
q(282, S7, "Type II choledochal cyst is:",
  ["A diverticulum of the common bile duct", "Diffuse CBD dilatation", "Intraduodenal CBD dilatation", "Intrahepatic biliary radical dilatation"], 0,
  "Todani classification: Type II — diverticulum of CBD. (Book p282)")
q(282, S7, "Type III choledochal cyst, involving the intraduodenal portion of the CBD, is also known as:",
  ["Choledochocele", "A mucocele", "Caroli's disease", "A Phrygian cap"], 0,
  "Todani classification: Type III — intraduodenal portion of CBD dilatation, aka choledochocele. (Book p282)")
q(282, S7, "Type IVa choledochal cyst shows:",
  ["Intrahepatic and extrahepatic biliary tree dilatation", "Extrahepatic dilatation only", "Intrahepatic dilatation only", "A CBD diverticulum"], 0,
  "Todani classification: Type IVa — intra and extrahepatic biliary tree dilatation. (Book p282)")
q(282, S7, "Type IVb choledochal cyst shows:",
  ["Extrahepatic biliary tree dilatation", "Intrahepatic radical dilatation only", "A CBD diverticulum", "Diffuse CBD dilatation only"], 0,
  "Todani classification: Type IVb — extrahepatic biliary tree dilatation. (Book p282)")
q(282, S7, "Type V choledochal cyst, with intrahepatic biliary radicals dilatation, is also known as:",
  ["Caroli's disease", "A choledochocele", "Mirizzi syndrome", "A mucocele"], 0,
  "Todani classification: Type V — intrahepatic biliary radicals dilatation, aka Caroli's disease. (Book p282)")
q(282, S7, "The clinical features of a choledochal cyst are:",
  ["Lump, pain and jaundice", "Painless weight loss", "Obstipation and vomiting", "Reynold's pentad"], 0,
  "Clinical features: lump, pain, jaundice. (Book p282)")
q(282, S7, "The investigation of choice for a choledochal cyst is:",
  ["MRCP", "USG alone", "HIDA scan", "Plain X-ray"], 0,
  "Investigation: MRCP — IOC. (Book p282)")
q(283, S7, "Type I choledochal cyst is managed by:",
  ["Roux-en-Y hepaticojejunostomy", "ERCP with sphincterotomy", "Cholecystectomy only", "Observation"], 0,
  "Management: Type I — Roux-en-Y hepaticojejunostomy. (Book p283)")
q(283, S7, "Type II choledochal cyst is managed by:",
  ["Cut and repair of the CBD", "Roux-en-Y hepaticojejunostomy", "ERCP with sphincterotomy", "Transplantation"], 0,
  "Management: Type II — cut and repair CBD. (Book p283)")
q(283, S7, "Type III choledochal cyst is managed by:",
  ["ERCP with sphincterotomy", "Roux-en-Y hepaticojejunostomy", "Transplantation", "Cut and repair of the CBD"], 0,
  "Management: Type III — ERCP + sphincterotomy. (Book p283)")
q(283, S7, "Choledochal cysts with intrahepatic radical involvement (Type IVa and V) are managed by:",
  ["Transplantation", "ERCP with sphincterotomy", "Simple cholecystectomy", "Observation"], 0,
  "Management: intrahepatic radical involvement IVa, V — transplant. (Book p283)")
q(283, S7, "Type IVb choledochal cyst is managed by:",
  ["Portoenterostomy", "Roux-en-Y hepaticojejunostomy", "ERCP with sphincterotomy", "Transplantation"], 0,
  "Management: IVb — portoenterostomy. (Book p283)")

# ------------------------------------------------------------------ p283-284
S8 = "Cholangiocarcinoma"
q(283, S8, "Cholangiocarcinoma is:",
  ["Carcinoma of the bile duct", "Carcinoma of the gallbladder only", "A benign biliary stricture", "Cancer of the pancreas only"], 0,
  "Cholangiocarcinoma: carcinoma of bile duct. (Book p283)")
q(283, S8, "Which of the following is a risk factor for cholangiocarcinoma?",
  ["Choledochal cysts", "A Phrygian cap", "Radiolucent stones", "Bouveret syndrome"], 0,
  "Risk factors: obesity, DM, HBV/HCV, choledochal cysts, thorotrast, abnormal pancreatobiliary duct junction, sclerosing cholangitis. (Book p283)")
q(283, S8, "Thorotrast exposure raises the risk of:",
  ["Hepatocellular cancer, cholangiocarcinoma and renal cell carcinoma", "Only skin cancer", "Only oral cancer", "Only breast cancer"], 0,
  "Risk factors: thorotrast — increased risk of hepatocellular cancer, cholangiocarcinoma, renal cell carcinoma. (Book p283)")
q(283, S8, "Primary sclerosing cholangitis is a:",
  ["Autoimmune disease", "Infective disease only", "Genetic disorder only", "Nutritional disease"], 0,
  "Sclerosing cholangitis: autoimmune disease. (Book p283)")
q(283, S8, "Primary sclerosing cholangitis is associated with:",
  ["Inflammatory bowel disease", "Coeliac disease only", "Hypertension", "Asthma"], 0,
  "Sclerosing cholangitis: associated with inflammatory bowel disease. (Book p283)")
q(283, S8, "Primary sclerosing cholangitis is more common in:",
  ["Females than males", "Males than females", "Children than adults", "Both sexes equally"], 0,
  "Sclerosing cholangitis: F > m. (Book p283)")
q(283, S8, "The HLA association in primary sclerosing cholangitis is:",
  ["DR3/B8", "DR4 only", "B27 only", "No HLA association"], 0,
  "Sclerosing cholangitis: HLA DR3/B8 associations. (Book p283)")
q(283, S8, "Antibodies seen in primary sclerosing cholangitis include:",
  ["Anti-smooth muscle antibodies and antinuclear antibodies", "Anti-mitochondrial antibodies only", "ANA only", "No antibodies"], 0,
  "Sclerosing cholangitis: anti-smooth muscle antibodies, antinuclear antibodies. (Book p283)")
q(283, S8, "Inflammatory fibrosis in primary sclerosing cholangitis leads to:",
  ["Multiple strictures", "A single stricture only", "No strictures", "A Phrygian cap"], 0,
  "Sclerosing cholangitis: inflammatory fibrosis leads to multiple strictures. (Book p283)")
q(283, S8, "The investigation of choice in primary sclerosing cholangitis is:",
  ["MRCP, showing a beaded appearance of the biliary tree", "Plain X-ray", "USG alone", "HIDA scan"], 0,
  "Sclerosing cholangitis: IOC — MRCP (beaded appearance of biliary tree). (Book p283)")
q(283, S8, "The clinical feature of cholangiocarcinoma is:",
  ["Obstructive jaundice", "Painless mass only", "Obstipation", "Haematemesis"], 0,
  "Features: obstructive jaundice. (Book p283)")
q(283, S8, "A distal common bile duct tumour presents as:",
  ["Periampullary cancer", "Gallstone ileus", "A WES sign", "Bouveret syndrome"], 0,
  "Features: distal CBD tumour — presents as periampullary cancer. (Book p283)")
q(283, S8, "The most common site of cholangiocarcinoma is:",
  ["The hilum", "The ampulla", "The intrahepatic ducts only", "The duodenum"], 0,
  "Features: m/c site — hilum. (Book p283)")
q(283, S8, "A Klatskin tumour is:",
  ["A hilar cholangiocarcinoma", "A distal CBD tumour", "A gallbladder carcinoma", "A pancreatic head tumour"], 0,
  "Klatskin tumours: hilar cholangiocarcinoma; Bismuth-Corlette classification. (Book p283)")
q(283, S8, "Klatskin tumours are classified by:",
  ["The Bismuth-Corlette classification", "The Todani classification", "The Couinaud classification", "The TNM of the lung"], 0,
  "Klatskin tumours: Bismuth-Corlette classification. (Book p283)")
q(284, S8, "The investigation of choice for cholangiocarcinoma is:",
  ["MRCP", "ERCP", "CECT alone", "HIDA scan"], 0,
  "Investigation: MRCP — IOC. (Book p284)")
q(284, S8, "A DISTAL CBD cholangiocarcinoma without metastasis is managed by:",
  ["Whipple's surgery", "Hepaticojejunostomy", "Choledochojejunostomy", "Portoenterostomy"], 0,
  "Management — resectable, no metastasis: a. Distal CBD — Whipple's Sx. (Book p284)")
q(284, S8, "A SUPRADUODENAL cholangiocarcinoma without metastasis is managed by:",
  ["Choledochojejunostomy", "Whipple's surgery", "Hepaticojejunostomy", "Portoenterostomy"], 0,
  "Management: b. Supraduodenal — choledochojejunostomy. (Book p284)")
q(284, S8, "A COMMON HEPATIC DUCT cholangiocarcinoma without metastasis is managed by:",
  ["Hepaticojejunostomy", "Whipple's surgery", "Choledochojejunostomy", "Portoenterostomy"], 0,
  "Management: c. CHD — hepaticojejunostomy. (Book p284)")
q(284, S8, "A Klatskin tumour without metastasis is managed by:",
  ["Portoenterostomy", "Whipple's surgery", "Choledochojejunostomy", "Hepaticojejunostomy"], 0,
  "Management: d. Klatskin tumour — portoenterostomy. (Book p284)")
q(284, S8, "Chemotherapy used in cholangiocarcinoma is:",
  ["Gemcitabine based", "Methotrexate based", "Cisplatin alone", "Not used at all"], 0,
  "Management: chemotherapy — gemcitabine based. (Book p284)")
q(284, S8, "The most common site of metastasis in cholangiocarcinoma is:",
  ["The liver", "The lung", "The bone", "The brain"], 0,
  "Non-resectable: m/c site of metastasis — liver. (Book p284)")
q(284, S8, "Palliative management of non-resectable cholangiocarcinoma includes:",
  ["ERCP with stenting or percutaneous transhepatic biliary drainage", "Whipple's surgery", "Radical hepatectomy", "Observation only"], 0,
  "Palliative Mx: ERCP + stenting, percutaneous transhepatic biliary drainage. (Book p284)")
q(284, S8, "The tumour marker for cholangiocarcinoma is:",
  ["Serum CA 19-9", "AFP", "PSA", "CA-125 only"], 0,
  "Tumour marker: S. CA 19-9. (Book p284)")

# ------------------------------------------------------------------ p284
S9 = "Miscellaneous: Hemobilia and Bilhemia"
q(284, S9, "Hemobilia is:",
  ["Bleeding from the biliary tree", "Bile leaking into blood vessels", "Air in the biliary tree", "A distended gallbladder"], 0,
  "Miscellaneous: hemobilia — bleeding from biliary tree. (Book p284)")
q(284, S9, "Bilhemia is:",
  ["Bile leaking into blood vessels", "Bleeding from the biliary tree", "Pneumobilia", "A mucocele"], 0,
  "Miscellaneous: bilhemia — bile leaking into blood vessels. (Book p284)")
q(284, S9, "Causes of hemobilia and bilhemia include:",
  ["Post ERCP and trauma", "Pregnancy", "OCP use", "Vagotomy"], 0,
  "Causes (both): post ERCP, trauma. (Book p284)")
q(284, S9, "Quincke's triad in hemobilia consists of:",
  ["Pain, jaundice and melena", "Fever, shock and altered sensorium", "Pain, mass and jaundice", "Pneumobilia, SBO and a stone"], 0,
  "Features: hemobilia — Quincke's triad: pain, jaundice, melena. (Book p284)")
q(284, S9, "The feature of bilhemia is:",
  ["Rapidly progressive jaundice", "Quincke's triad", "Pneumobilia", "A WES sign"], 0,
  "Features: bilhemia — rapidly progressive jaundice. (Book p284)")
q(284, S9, "The investigation of choice for hemobilia is:",
  ["CT angiography", "ERCP", "USG alone", "HIDA scan"], 0,
  "IOC: hemobilia — CT angiography. (Book p284)")
q(284, S9, "The investigation of choice for bilhemia is:",
  ["ERCP", "CT angiography", "USG alone", "Barium meal"], 0,
  "IOC: bilhemia — ERCP. (Book p284)")
q(284, S9, "Hemobilia is usually:",
  ["Self limiting, with embolisation if bleeding", "Fatal in all", "Always surgical", "Treated only with antibiotics"], 0,
  "Management: hemobilia — self limiting (usually), embolisation if bleeding. (Book p284)")
q(284, S9, "Bilhemia is managed by:",
  ["ERCP with stenting", "Observation only", "Cholecystectomy", "Whipple's surgery"], 0,
  "Management: bilhemia — ERCP + stenting. (Book p284)")

# ------------------------------------------------------------------ units
def first_page(label):
    for x in Q:
        if x["sec"] == label:
            return x["page"]
    return 0


UNIT_DEFS = [
    (S1, "Lap cholecystectomy has its choreography: surgeon and assistant both on the left, the patient in reverse Trendelenburg tipped right. Before a single clip goes on, the safe method demands the bile duct, Rouviere's status, hepatic artery, umbilical fissure and duodenum all in view. The classic four ports each have a job — epigastric for the right hand, hypochondrial for the left, the 4th for fundus retraction, infraumbilical for the camera — while the single-incision variant trades cosmesis for a higher incisional hernia rate. When Calot's freezes, the bailouts are the art: abort, convert to open (4-5%), tube cholecystostomy, subtotal for Mirizzi, or go fundus first."),
    (S2, "The complications list starts with the commonest — right shoulder tip pain from CO2 under the right diaphragmatic dome — then bleeding, bile duct injury, bowel injury, residual stones within 2 years (recurrent beyond) diagnosed on MRCP and cleared by ERCP, and the dreaded CHD/CBD stricture. In the operating room a partial tear is sewn with absorbable suture, a complete transection without a missing segment gets a T-tube anastomosis, and with a lost segment the distal end is closed and a choledochojejunostomy built. In the ward, a small fading leak in a stable patient is observed; a fever, jaundice, pain and rising leak means CBC, a subhepatic collection on USG, confirmation on MRCP — re-explore within 1-2 days, but beyond 2 days drain with a pigtail and stent by ERCP."),
    (S3, "The Strasberg A to D injuries are the small ones — cystic duct or minor leak (A), occluded aberrant right hepatic duct (B), its leak (C) and the lateral CBD injury (D). Above them the Bismuth types stage the big stricture: a stump over 2 cm is Type I (E1), under 2 cm is Type II (E2), a preserved confluence is Type III (E3), a lost confluence is Type IV (E4), and the aberrant duct stricture is Type V (E5)."),
    (S4, "Pregnancy is a lithogenic state — hormones push cholesterol into the bile while progesterone slows the gallbladder, so stones multiply. Treat mildly and conservatively in the first trimester (no NSAIDs, for the ductus arteriosus), operate by laparoscopy in the second, and manage non-operatively in the third. And remember: an appendix can go by laparoscopy in any trimester."),
    (S5, "Gallbladder cancer is the 90%-stone cancer: the typhi carrier, the porcelain wall, APBDJ, heavy metals in the water and the adenomatous, over-10-mm, multiple polyp all push the risk — cholesterol polyps do not. It is an adenocarcinoma, most aggressively infiltrating, presenting as a fixed mass that loses its pyriform shape with jaundice only late, spreading through the 4b/5 fossa, the subserosal lymphatics and the haematogenous route to liver and lung. CECT stages it (Tis in situ, T1a lamina propria, T1b muscularis, T2 perimuscular, T3 serosa/liver, T4 hepatic artery/main portal vein): T1a gets a simple cholecystectomy without bile spillage; T1b and T2 get the radical — gallbladder, 4b/5 or a 2 cm rim, hepatoduodenal nodes, and the CBD when involved; T3/T4 go to gemcitabine, with radical surgery waiting for a good response and palliation for a poor one. Depth is the most important prognostic factor, CA 19-9 is the marker, and port-site excision after a missed diagnosis buys nothing."),
    (S6, "Extrahepatic biliary atresia is inflammatory fibrosis closing the ducts of childhood, the commonest cause of paediatric liver transplantation. The Japanese/Anglo-Saxon types grade the obstruction — CBD only (I), common hepatic duct with patent (IIa) or obliterated (IIb) downstream, and the whole tree (III) — with cardiac lesions, polysplenia, situs inversus, absent vena cava and a preduodenal portal vein lurking alongside. Jaundice at birth marches to cirrhosis; fasting USG is the gold standard, MRCP the sensitive and specific test, and the biopsy separates it from neonatal hepatitis. Type I is hepaticojejunostomised; Types II and III get the Kasai portoenterostomy at the porta hepatis — and in 20-30% the disease still wins, and the transplant is the answer."),
    (S7, "The choledochal cyst is a dilated biliary tree draining so badly it jaundices, carrying a 10% cholangiocarcinoma risk. Todani sorts it: I diffuse CBD (the commonest), II diverticulum, III intraduodenal (choledochocele), IVa intra and extrahepatic, IVb extrahepatic, V the intrahepatic radicals (Caroli's). Lump, pain, jaundice; MRCP defines it. The repair follows the type: Roux-en-Y for I, cut-and-repair for II, ERCP with sphincterotomy for III, transplantation when the intrahepatic radicals are involved, and portoenterostomy for IVb."),
    (S8, "Cholangiocarcinoma is the bile duct's own carcinoma, fed by obesity, diabetes, HBV/HCV, choledochal cysts, thorotrast, abnormal pancreatobiliary junction and sclerosing cholangitis — the autoimmune, IBD-linked, female-predominant, HLA DR3/B8 disease of beaded ducts and antinuclear antibodies. It obstructs; the distal end masquerades as periampullary cancer and the hilum is the commonest site, where the Klatskin tumour keeps the Bismuth-Corlette count. MRCP investigates; the resectable get Whipple's (distal), choledochojejunostomy (supraduodenal), hepaticojejunostomy (CHD) or portoenterostomy (Klatskin) plus gemcitabine — and the unresectable, whose metastases favour the liver, are palliated by ERCP stenting or transhepatic drainage, with CA 19-9 marking the disease."),
    (S9, "The odd twins of biliary bleeding: hemobilia is blood in the biliary tree and bilhemia is bile in the vessels — both born of ERCP or trauma. Hemobilia gives Quincke's triad of pain, jaundice and melena, is found by CT angiography and usually stops by itself, with embolisation if it doesn't; bilhemia jaundices fast, is found by ERCP and is stented through it."),
]

UNITS = []
for i, (title, guide) in enumerate(UNIT_DEFS, 1):
    UNITS.append({
        "id": f"SURG-U38-{i}",
        "ch": 38,
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
with open("data/ch38.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
print(f"ch38: {len(Q)} questions, {len(UNITS)} units")
