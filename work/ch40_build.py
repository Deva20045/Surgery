#!/usr/bin/env python3
"""Build data/ch40.json — ch40 Pancreatic Tumour (Marrow Surgery Ed 8, book p297-306)."""
import json

Q = []


def q(page, sec, text, opts, ans, exp):
    Q.append({
        "id": f"SURG-C40-{len(Q)+1:03d}",
        "sec": sec,
        "page": page,
        "q": text,
        "opts": opts,
        "ans": ans,
        "exp": exp,
    })


# ------------------------------------------------------------------ p297
S1 = "Pancreatic Ductal Adenocarcinoma: Risk Factors and PanIN"
q(297, S1, "The most common carcinoma of the pancreas is:",
  ["Pancreatic ductal adenocarcinoma", "Insulinoma", "Gastrinoma", "Glucagonoma"], 0,
  "Pancreatic ductal adenocarcinoma: m/c carcinoma of pancreas. (Book p297)")
q(297, S1, "Which of the following is a risk factor for pancreatic ductal adenocarcinoma?",
  ["Smoking", "Tonsillitis", "Otitis media", "Sinusitis"], 0,
  "Risk factors: smoking, obesity, African American ethnicity, genetic factors, chronic pancreatitis, syndromes. (Book p297)")
q(297, S1, "Which of the following is a risk factor for pancreatic cancer?",
  ["African American ethnicity", "Cystic fibrosis only", "Down's syndrome", "Addison's disease"], 0,
  "Risk factors: African American ethnicity. (Book p297)")
q(297, S1, "The PRSS1 gene is associated with which pancreatic condition as a risk factor for cancer?",
  ["Hereditary pancreatitis", "Tropical calcific pancreatitis", "Pancreas divisum", "Duodenal atresia"], 0,
  "Genetic factors: PRSS1 gene — hereditary pancreatitis. (Book p297)")
q(297, S1, "The SPINK1 gene is associated with:",
  ["Tropical calcific pancreatitis", "Hereditary pancreatitis", "Chronic cholecystitis", "Gastric ulcer"], 0,
  "Genetic factors: SPINK1 gene — tropical calcific pancreatitis. (Book p297)")
q(297, S1, "Which syndrome raises the risk of pancreatic cancer by 100 folds?",
  ["STK11 Peutz-Jeghers syndrome", "Turner syndrome", "Down's syndrome", "Marfan syndrome"], 0,
  "Syndromes: STK11 Peutz-Jeghers syndrome — risk of pancreatic cancer raised by 100 folds. (Book p297)")
q(297, S1, "Which of the following is a syndrome listed as a risk factor for pancreatic cancer?",
  ["Familial atypical mole and multiple melanoma syndrome", "Carpal tunnel syndrome", "Horner's syndrome", "Raynaud's phenomenon"], 0,
  "Syndromes: familial atypical mole and multiple melanoma syndrome, cystic fibrosis, BRCA-2 gene mutation, Lynch syndrome, familial adenomatous polyposis. (Book p297)")
q(297, S1, "Familial adenomatous polyposis raises the risk of:",
  ["Periampullary cancer and pancreatic ductal adenocarcinoma", "Only colon polyps", "Only thyroid cancer", "Only oral cancer"], 0,
  "Syndromes: familial adenomatous polyposis — risk of periampullary cancer, pancreatic ductal adenocarcinoma. (Book p297)")
q(297, S1, "The BRCA-2 gene predisposes to which combination of cancers?",
  ["Pancreatic, prostate and male breast cancer", "Only breast cancer", "Only lung cancer", "Only thyroid cancer"], 0,
  "Note: BRCA-2 gene predisposes to pancreatic, prostate, male breast cancer. (Book p297)")
q(297, S1, "Lynch syndrome raises the risk of:",
  ["Colorectal cancer", "Only melanoma", "Only oral cancer", "Only skin sarcoma"], 0,
  "Note: Lynch — raised risk of colorectal cancer. (Book p297)")
q(297, S1, "PanIN stands for:",
  ["Pancreatic intraepithelial neoplasia", "Pancreatic intraductal neoplasm", "Pancreatic interstitial neuroendocrine", "Primary acinar node infarction"], 0,
  "PanIN: pancreatic intraepithelial neoplasia. (Book p297)")
q(297, S1, "In the PanIN sequence, the first and most common mutation is:",
  ["K-ras (in PanIN-1A and 1B)", "CDKN2A", "p53", "SMAD4"], 0,
  "PanIN diagram: PanIN-1A/1B — K-ras, 1st and m/c mutation. (Book p297)")
q(297, S1, "In the PanIN sequence, the mutation seen at PanIN-2A is:",
  ["CDKN2A", "K-ras", "p53", "SMAD4"], 0,
  "PanIN diagram: PanIN-2A — CDKN2A. (Book p297)")
q(297, S1, "In the PanIN sequence, PanIN-3 carries which mutations before the final hit?",
  ["p53 and SMAD4", "K-ras and CDKN2A", "Only K-ras", "BRCA-2 and TP53"], 0,
  "PanIN diagram: PanIN-3 — p53, SMAD4, then final hit. (Book p297)")
q(297, S1, "The mnemonic for the pancreatic cancer mutation sequence (K-ras, p53, SMAD4) is:",
  ["K53", "K75", "K12", "K9"], 0,
  "Mnemonic: K53. (Book p297)")

# ------------------------------------------------------------------ p298-299
S2 = "Periampullary Carcinoma and Courvoisier's Law"
q(298, S2, "Periampullary carcinoma is a group of how many cancers within 2 cm of the ampullary opening?",
  ["Four", "Two", "Three", "Five"], 0,
  "Periampullary carcinoma: group of 4 cancers within 2 cm of ampullary opening. (Book p298)")
q(298, S2, "Which of the following is one of the four periampullary cancers?",
  ["Ampullary variety", "Insulinoma", "Glucagonoma", "Ganglioneuroma"], 0,
  "Periampullary: 1. Carcinoma head of pancreas, 2. Ampullary variety, 3. Cholangiocarcinoma of distal CBD, 4. Duodenal adenocarcinoma. (Book p298)")
q(298, S2, "The four periampullary cancers share:",
  ["Similar presentation and management", "Different management only", "Different presentation only", "No relation at all"], 0,
  "Periampullary carcinoma: similar presentation and Mx. (Book p298)")
q(298, S2, "The most common presentation of periampullary carcinoma is:",
  ["Progressive obstructive jaundice due to CBD obstruction", "Non-bilious vomiting", "Haematemesis", "Chronic diarrhoea"], 0,
  "Clinical presentation: progressive obstructive jaundice d/t CBD obstruction — m/c presentation. (Book p298)")
q(298, S2, "Obstructive jaundice from a periampullary tumour is also called:",
  ["Surgical jaundice", "Hepatic jaundice", "Haemolytic jaundice", "Physiological jaundice"], 0,
  "Clinical presentation: aka surgical jaundice. (Book p298)")
q(298, S2, "Pain in pancreatic carcinoma is of high intensity when the tumour is in the:",
  ["Tail and body", "Head only", "Uncinate process only", "Ampulla only"], 0,
  "Clinical presentation: pain — high intensity in tail and body. (Book p298)")
q(298, S2, "Waxing and waning jaundice is a specific presentation of:",
  ["The ampullary variety", "Body tumour only", "Tail tumour only", "Duodenal adenocarcinoma only"], 0,
  "Specific presentations: waxing and waning of jaundice — seen in ampullary variety. (Book p298)")
q(298, S2, "In waxing jaundice of an ampullary tumour, the fall in jaundice is associated with:",
  ["Melena", "Constipation", "Weight gain", "Pallor only"], 0,
  "Waxing and waning: decreased jaundice — associated with melena (friable tumour growth obstructs bile, then sloughs off, causing decreased jaundice and melena). (Book p298)")
q(298, S2, "Gastric outlet obstruction with jaundice is a specific presentation of:",
  ["Duodenal adenocarcinoma", "Insulinoma", "Tail tumour", "Gastrinoma only"], 0,
  "Specific presentations: gastric outlet obstruction — seen in duodenal adenocarcinoma, associated with jaundice. (Book p298)")
q(298, S2, "Courvoisier's law states that obstructive jaundice with a palpable gallbladder is:",
  ["Seldom due to stone disease", "Almost always due to stones", "Always due to a Phrygian cap", "Due to hepatitis"], 0,
  "Courvoisier's law: obstructive jaundice + palpable gallbladder — seldom d/t stone disease. (Book p298)")
q(298, S2, "A tumour blocking the CBD produces:",
  ["A dilated biliary tree and a distended, palpable, pyriform gallbladder", "A shrunken gallbladder", "A normal biliary tree", "A calcified gallbladder only"], 0,
  "Courvoisier's law: tumour blocking CBD — obstruction, dilated biliary tree, distended gallbladder (palpable, pyriform shaped). (Book p298)")
q(298, S2, "In gall stone obstruction of the CBD, the gallbladder does NOT distend because of:",
  ["Inflammatory fibrosis of the gallbladder", "Normal physiology", "Pyloric stenosis", "A Phrygian cap"], 0,
  "Courvoisier's law: gall stones causing obstruction of CBD — no distension of GB d/t inflammatory fibrosis of gallbladder; jaundice plus shrunken gallbladder. (Book p298)")
q(299, S2, "An exception to Courvoisier's law is:",
  ["Primary CBD stones (10% of cases)", "Pancreatitis", "Appendicitis", "Hernia"], 0,
  "Exceptions: primary CBD stones (10% cases). (Book p299)")
q(299, S2, "Which of the following is an exception to Courvoisier's law?",
  ["Double impaction of stone", "A Phrygian cap", "A WES sign", "Bouveret syndrome"], 0,
  "Exceptions: double impaction of stone, oriental cholangiohepatitis, Mirizzi syndrome. (Book p299)")
q(299, S2, "Oriental cholangiohepatitis, an exception to Courvoisier's law, is due to infection by:",
  ["The Chinese liver fluke", "Echinococcus", "Taenia solium", "Entamoeba"], 0,
  "Exceptions: oriental cholangiohepatitis — d/t infection by Chinese liver fluke. (Book p299)")
q(299, S2, "Mirizzi syndrome, an exception to Courvoisier's law, involves:",
  ["A fistula between the gallbladder and the CBD", "A fistula to the stomach", "A fistula to the colon", "A patent ampulla"], 0,
  "Exceptions: Mirizzi syndrome — fistula between gallbladder and CBD. (Book p299)")

# ------------------------------------------------------------------ p299
S3 = "Investigation of Pancreatic Cancer"
q(299, S3, "The investigation of choice for pancreatic carcinoma is:",
  ["CECT", "USG alone", "Plain X-ray", "Barium meal"], 0,
  "Investigation: CECT — IOC. (Book p299)")
q(299, S3, "Duodenography in pancreatic carcinoma shows:",
  ["The Frostberg reverse 3 sign", "A double bubble sign", "A sentinel loop", "A WES sign"], 0,
  "Duodenography: Frostberg reverse 3 sign. (Book p299)")
q(299, S3, "Duodenography for pancreatic carcinoma is:",
  ["Obsolete", "The current gold standard", "The IOC", "Never done"], 0,
  "Duodenography: obsolete. (Book p299)")
q(299, S3, "The X-ray finding in pancreatic carcinoma is:",
  ["Widening of the duodenal loops", "A double bubble", "Free air", "Pneumobilia"], 0,
  "X-ray: widening of duodenal loops. (Book p299)")
q(299, S3, "The double duct sign on MRCP/ERCP means:",
  ["Blockage of the ampullary opening with widening of the pancreatic duct and CBD", "A dilated gallbladder only", "Air in the biliary tree", "A sentinel loop"], 0,
  "MRCP, ERCP — double duct sign: blockage of ampullary opening, widening of pancreatic duct and CBD. (Book p299)")
q(299, S3, "When the radiological diagnosis of a pancreatic head mass is in doubt, the next step is:",
  ["Transgastric EUS guided FNAC", "Laparotomy without biopsy", "Observation for 6 months", "Barium meal"], 0,
  "Radiological diagnosis, in doubt — trans gastric EUS guided FNAC (EUS — endoscopic guided ultrasound). (Book p299)")
q(299, S3, "CA 19-9 in pancreatic cancer is:",
  ["A predictive and prognostic marker", "Only a therapeutic target", "A radiological sign", "A histological grade"], 0,
  "CA 19-9: predictive and prognostic marker. (Book p299)")
q(299, S3, "CA 19-9 helps identify patients for:",
  ["Staging laparoscopy", "Cholecystectomy", "Hernia repair", "Appendectomy"], 0,
  "CA 19-9: identifies patients for staging laparoscopy — done prior to definitive Sx in GI tumors to identify metastases. (Book p299)")
q(299, S3, "A raised CA 19-9 is an indication for:",
  ["Staging laparoscopy", "Immediate Whipple's surgery", "No further workup", "Cholecystectomy"], 0,
  "CA 19-9: raised CA 19-9 — indication for staging laparoscopy. (Book p299)")
q(299, S3, "A normal CA 19-9 after neoadjuvant chemotherapy is:",
  ["An important prognostic marker (not specific)", "Irrelevant", "A sign of metastasis", "A contraindication to surgery"], 0,
  "CA 19-9 (normal) after neoadjuvant chemotherapy — important prognostic marker (not specific). (Book p299)")
q(299, S3, "Which of the following conditions shows a raised CA 19-9?",
  ["Cholangiocarcinoma", "Appendicitis", "Hernia", "Hypothyroidism"], 0,
  "Conditions with raised CA 19-9: cholangio-carcinoma, gall bladder cancer, pancreatic cancer. (Book p299)")
q(299, S3, "Staging of pancreatic cancer uses PET CT, which stands for:",
  ["Positron emission tomography", "Plain enhanced thoracic contrast", "Pancreatic enzymatic tomography", "Percutaneous endoscopic transluminal"], 0,
  "Staging: PET CT — positron emitted tomography. (Book p299)")

# ------------------------------------------------------------------ p300
S4 = "Staging and Resectability"
q(300, S4, "In the AJCC classification (7th and 8th editions), T1 pancreatic cancer is:",
  ["Diameter 2 cm or less", "Diameter 2-4 cm", "Diameter more than 4 cm", "Adjacent structure involvement"], 0,
  "AJCC: T1 — diameter ≤2 cm. (Book p300)")
q(300, S4, "T2 pancreatic cancer is:",
  ["Diameter 2-4 cm", "Diameter ≤2 cm", "Diameter >4 cm", "Adjacent structure involvement"], 0,
  "AJCC: T2 — diameter 2-4 cm. (Book p300)")
q(300, S4, "T3 pancreatic cancer is:",
  ["Diameter more than 4 cm", "Diameter ≤2 cm", "Diameter 2-4 cm", "Carcinoma in situ"], 0,
  "AJCC: T3 — diameter >4 cm. (Book p300)")
q(300, S4, "T4 pancreatic cancer is defined by:",
  ["Adjacent structure involvement", "Size only", "Lymph node count only", "A normal size"], 0,
  "AJCC: T4 — adjacent structure involvement. (Book p300)")
q(300, S4, "The most common site of distant metastasis (M1) in pancreatic cancer is:",
  ["The liver", "The lung", "The bone", "The brain"], 0,
  "Metastasis staging: M1 — distant metastasis, m/c site — liver. (Book p300)")
q(300, S4, "In nodal staging, N1 pancreatic cancer means:",
  ["1-3 regional nodes", "No regional nodes", "More than 3 regional nodes", "Distant nodes only"], 0,
  "Nodal staging: N0 — no regional nodes, N1 — 1-3 regional nodes, N2 — >3 regional nodes. (Book p300)")
q(300, S4, "In nodal staging, N2 pancreatic cancer means:",
  ["More than 3 regional nodes", "No nodes", "Exactly 1 node", "Exactly 3 nodes"], 0,
  "Nodal staging: N2 — >3 regional nodes. (Book p300)")
q(300, S4, "In the Varadhachary-Katz criteria, a RESCTABLE pancreatic tumour has:",
  ["No involvement of the superior mesenteric artery with a patent portal vein junction", "Encasement of the superior mesenteric artery", "Long segment occlusion of the portal vein", "Abutment of the celiac axis of 180 degrees"], 0,
  "Varadhachary-Katz: resectable (all 4 resectables), AJCC I/II — SMA no involvement, SMV/portal V junction patent — surgery. (Book p300)")
q(300, S4, "In the Varadhachary-Katz criteria, BORDERLINE pancreatic tumour has:",
  ["Abutment of the superior mesenteric artery (180 degrees or less than 50%) and short segment occlusion of the portal vein junction", "Encasement of the superior mesenteric artery", "No vessel involvement at all", "Long segment occlusion only"], 0,
  "Borderline, AJCC III — SMA abutment (≥180° or <50%), celiac axis abutment, short segment occlusion of SMV/portal junction — chemotherapy then surgery. (Book p300)")
q(300, S4, "Borderline pancreatic tumours in the Varadhachary-Katz criteria are managed by:",
  ["Chemotherapy followed by surgery", "Surgery alone", "Palliation only", "Observation"], 0,
  "Borderline: Mx — chemotherapy, then Sx. (Book p300)")
q(300, S4, "In the Varadhachary-Katz criteria, a LOCALLY ADVANCED pancreatic tumour has:",
  ["Encasement of the superior mesenteric artery with long segment occlusion of the portal vein", "No involvement at all", "Only abutment", "A patent portal vein"], 0,
  "Locally advanced: SMA encasement, excessive encasement of the common hepatic artery, long segment of occlusion — Mx: unresectable, palliative. (Book p300)")
q(300, S4, "The investigation of choice for peritoneal metastases in pancreatic cancer is:",
  ["Diagnostic laparoscopy", "USG", "Plain X-ray", "HIDA scan"], 0,
  "Peritoneal mets: diagnostic laparoscopy — IOC. (Book p300)")
q(300, S4, "If peritoneal metastases are found at diagnostic laparoscopy, the procedure is:",
  ["Abandoned", "Completed as planned", "Converted to Whipple's", "Repeated in 2 weeks"], 0,
  "Peritoneal mets: mets (+) — procedure abandoned. (Book p300)")
q(300, S4, "Which of the following is a criterion of unresectability in pancreatic cancer?",
  ["Malignant ascites", "A small tumour", "No lymph nodes", "A normal CA 19-9"], 0,
  "Criteria of unresectability: peritoneal mets, malignant ascites, liver mets. (Book p300)")
q(300, S4, "Which of the following is a criterion of unresectability in pancreatic cancer?",
  ["Liver metastases", "A T1 tumour", "N0 status", "A 2 cm size"], 0,
  "Criteria of unresectability: liver mets. (Book p300)")
q(300, S4, "A resectable pancreatic tumour in the HEAD (the commonest site) or periampullary is managed by:",
  ["Whipple's surgery", "Distal pancreatectomy", "Total pancreatectomy in all", "Chemotherapy only"], 0,
  "Surgical management: resectable — head (m/c site), periampullary — Whipple surgery. (Book p300)")
q(300, S4, "A resectable pancreatic tumour in the BODY or TAIL is managed by:",
  ["Distal pancreatectomy", "Whipple's surgery", "Enucleation always", "Observation"], 0,
  "Surgical management: body/tail — distal pancreatectomy. (Book p300)")

# ------------------------------------------------------------------ p301
S5 = "Whipple's Surgery"
q(301, S5, "Whipple's surgery is also called:",
  ["Pancreaticoduodenectomy", "Distal pancreatectomy", "Hepaticojejunostomy only", "Gastrojejunostomy only"], 0,
  "Whipple surgery: pancreaticoduodenectomy. (Book p301)")
q(301, S5, "The pylorus preserving Whipple is the:",
  ["Longmire transverso procedure", "Beger's procedure", "Frey's procedure", "Duval procedure"], 0,
  "Pylorus preserving Whipple: Longmire transverso procedure. (Book p301)")
q(301, S5, "The pylorus preserving Whipple:",
  ["Reduces the chances of dumping syndrome and is the preferred procedure", "Increases dumping syndrome", "Is obsolete", "Removes the pylorus always"], 0,
  "Pylorus preserving Whipple: decreased chances of dumping syndrome, preferred procedure. (Book p301)")
q(301, S5, "The traditional Whipple is used when:",
  ["The pylorus is involved or the margin is unattainable", "The pylorus is normal", "The tumour is in the tail", "There is no jaundice"], 0,
  "Pylorus preserving Whipple: involvement of pylorus/unattainable margin — traditional Whipple's. (Book p301)")
q(301, S5, "The incision for Whipple's surgery is:",
  ["Chevron / roof top", "Midline vertical only", "Langer's incision", "McBurney's incision"], 0,
  "Incision: chevron/roof top. (Book p301)")
q(301, S5, "Structures removed in Whipple's surgery include all of the following EXCEPT:",
  ["The spleen", "The gallbladder (cholecystectomy)", "The CBD", "The duodenum"], 0,
  "Procedure: 1. Cholecystectomy, 2. CBD, 3. Pylorus, 4. Pancreatectomy, 5. Duodenectomy. (Book p301)")
q(301, S5, "The anastomoses performed in Whipple's surgery are:",
  ["Hepaticojejunostomy, gastrojejunostomy and pancreaticojejunostomy", "Only a gastrojejunostomy", "Only a hepaticojejunostomy", "A choledochojejunostomy and a sleeve gastrostomy"], 0,
  "Procedure: hepaticojejunostomy (anastomoses with common hepatic duct), gastrojejunostomy, pancreaticojejunostomy. (Book p301)")
q(301, S5, "In Whipple's surgery, the hepaticojejunostomy is made with the:",
  ["Common hepatic duct", "Cystic duct", "Right hepatic duct only", "Left hepatic duct only"], 0,
  "Anastomoses: hepaticojejunostomy — anastomoses with common hepatic duct. (Book p301)")
q(301, S5, "The tunnel of love in Whipple's surgery is:",
  ["The space between the vessels and the pancreas, which needs to be intact to proceed", "The duodenal lumen", "The cystic duct", "The lesser sac"], 0,
  "Tunnel of love: space between the vessels and pancreas; needs to be intact to proceed with Whipple's. (Book p301)")
q(301, S5, "The most common complication of Whipple's surgery is:",
  ["Impaired gastric emptying", "Pancreatic fistula", "Wound infection", "Recurrence"], 0,
  "Complication: impaired gastric emptying — m/c. (Book p301)")
q(301, S5, "Impaired gastric emptying after Whipple's is due to:",
  ["Loss of receptive relaxation", "Gastric ulceration", "Pyloric oedema only", "Adhesions only"], 0,
  "Impaired gastric emptying: d/t loss of receptive relaxation. (Book p301)")
q(301, S5, "Impaired gastric emptying after Whipple's is more common after:",
  ["Conventional Whipple than pylorus preserving", "Pylorus preserving Whipple than conventional", "Both equally", "Neither"], 0,
  "Impaired gastric emptying: conventional Whipple > pylorus preserving. (Book p301)")
q(301, S5, "The most common cause of death after Whipple's surgery is:",
  ["Sepsis due to anastomotic leak", "Wound infection", "Haemorrhage", "Dumping syndrome"], 0,
  "Complication: sepsis d/t anastomotic leak — m/c cause of death. (Book p301)")
q(301, S5, "Pancreatic fistula after Whipple's is due to:",
  ["Pancreaticojejunal anastomotic leak", "Gastrojejunal leak only", "Hepaticojejunal leak only", "Duodenal stump closure only"], 0,
  "Pancreatic fistula: d/t pancreaticojejunal anastomotic leak. (Book p301)")
q(301, S5, "Pancreatic fistula after Whipple's classically appears on:",
  ["Post op day 2-3 with turbid, amylase-rich drainage", "Post op day 20", "Immediately at the end of surgery", "At discharge only"], 0,
  "Pancreatic fistula: post op day 2-3, turbid drainage rich in amylase. (Book p301)")
q(301, S5, "Pancreatic fistula after Whipple's:",
  ["Stops spontaneously and octreotide is effective", "Always needs a second laparotomy", "Is fatal in all", "Requires a total pancreatectomy"], 0,
  "Pancreatic fistula: stops spontaneously; octreotide is effective. (Book p301)")
q(301, S5, "For efficacy, the better pancreatic cancer chemotherapy regimen is:",
  ["Gemcitabine plus capecitabine over gemcitabine monotherapy", "Gemcitabine monotherapy alone", "Cisplatin alone", "No chemotherapy"], 0,
  "Chemotherapy: effectiveness — gemcitabine + capecitabine > gemcitabine monotherapy. (Book p301)")
q(301, S5, "For survival, the better pancreatic cancer chemotherapy regimen is:",
  ["FOLFIRINOX over gemcitabine monotherapy", "Gemcitabine monotherapy alone", "5-FU alone", "Observation"], 0,
  "Chemotherapy: survival — FOLFIRINOX > gemcitabine monotherapy. (Book p301)")

# ------------------------------------------------------------------ p301-302
S6 = "Management of Unresectable Tumour"
q(301, S6, "The management of an unresectable pancreatic tumour includes palliation of:",
  ["Pruritus and jaundice", "Only pruritus", "Only constipation", "Only diabetes"], 0,
  "Management of unresectable tumour: palliation of pruritus and jaundice. (Book p301)")
q(301, S6, "Palliation of jaundice in an unresectable pancreatic tumour is done by:",
  ["ERCP with stenting", "Cholecystectomy", "Whipple's surgery", "Appendectomy"], 0,
  "Palliation: ERCP and stenting. (Book p301)")
q(302, S6, "Percutaneous transhepatic biliary drainage (PTBD) works because:",
  ["Distal blockage dilates the proximal radicals, which are punctured to drain bile", "It dissolves the tumour", "It removes the stones", "It cures the pancreatitis"], 0,
  "PTBD: distal blockage — dilatation of proximal radicals, punctured, drainage of bile. (Book p302)")
q(302, S6, "The chemotherapy listed for unresectable pancreatic tumour is:",
  ["NAB paclitaxel", "Oral amoxicillin", "Intramuscular penicillin", "Topical iodine"], 0,
  "Chemotherapy: NAB paclitaxel. (Book p302)")
q(302, S6, "The triple bypass palliation in an unresectable pancreatic tumour consists of:",
  ["Hepaticojejunostomy, gastrojejunostomy and jejunojejunostomy, without removing the tumour", "Whipple's surgery", "Distal pancreatectomy", "Splenectomy"], 0,
  "Palliative Sx: a. Triple bypass — hepaticojejunostomy, gastrojejunostomy, jejunojejunostomy; tumour is not removed. (Book p302)")
q(302, S6, "In the triple bypass, the gastrojejunostomy is done to:",
  ["Prevent gastric outlet obstruction", "Prevent jaundice", "Remove the tumour", "Treat the diabetes"], 0,
  "Triple bypass: gastrojejunostomy — to prevent gastric outlet obstruction. (Book p302)")
q(302, S6, "In the triple bypass, the hepaticojejunostomy diverts:",
  ["Bile into the jejunum", "Bile into the stomach", "Pancreatic juice into the stomach", "Chyme into the colon"], 0,
  "Triple bypass: hepaticojejunostomy — bile to jejunum. (Book p302)")
q(302, S6, "Palliative coeliac ganglion block in pancreatic cancer is done to:",
  ["Reduce the pain", "Reduce the jaundice", "Prevent the fistula", "Treat the diabetes"], 0,
  "Palliative Sx: b. Coeliac ganglion block — decreases pain. (Book p302)")
q(302, S6, "The most important prognostic factor in pancreatic cancer is:",
  ["Stage", "Gender", "Smoking history only", "CA 19-9 level only"], 0,
  "Prognostic factor: stage (most important). (Book p302)")

# ------------------------------------------------------------------ p302-303
S7 = "Insulinoma"
q(302, S7, "The most common endocrine tumour of the pancreas is:",
  ["Insulinoma", "Gastrinoma", "Glucagonoma", "VIPoma"], 0,
  "Insulinoma: m/c endocrine tumour. (Book p302)")
q(302, S7, "Insulinoma arises from:",
  ["Beta cells", "Alpha cells", "G cells", "D cells"], 0,
  "Insulinoma: arises from beta-cells. (Book p302)")
q(302, S7, "What proportion of insulinomas are benign?",
  ["90%", "10%", "50%", "100%"], 0,
  "Insulinoma: 90% benign. (Book p302)")
q(302, S7, "Insulinomas are distributed in the pancreas:",
  ["Evenly distributed throughout", "Only in the head", "Only in the tail", "Only in the uncinate process"], 0,
  "Insulinoma: evenly distributed throughout. (Book p302)")
q(302, S7, "Whipple's triad in insulinoma consists of:",
  ["Fasting hypoglycaemia, a low blood glucose value (less than 50 mg/dL) and rapid resolution on giving glucose", "Fever, jaundice and pain", "Pain, mass and jaundice", "Pneumobilia, SBO and a stone"], 0,
  "Whipple's triad: fasting hypoglycaemia, low blood glucose value (<50 mg/dL), rapid resolution on giving glucose. (Book p302)")
q(302, S7, "In Whipple's triad, the blood glucose value is:",
  ["Less than 50 mg/dL", "Greater than 200 mg/dL", "Exactly 100 mg/dL", "Greater than 150 mg/dL"], 0,
  "Whipple's triad: low blood glucose value (<50 mg/dL). (Book p302)")
q(302, S7, "The gold standard test for insulinoma is:",
  ["The 72 hours fasting test (now obsolete)", "A plain X-ray", "USG", "A barium meal"], 0,
  "Investigation: gold standard test — 72 hrs fasting test; obsolete. (Book p302)")
q(302, S7, "In insulinoma, the insulin to glucose ratio is:",
  ["Greater than 0.3", "Less than 0.1", "Exactly 1.0", "Zero"], 0,
  "Investigation: insulin/glucose >0.3. (Book p302)")
q(302, S7, "The best method of localisation of an insulinoma is:",
  ["Endoscopic ultrasound", "Plain X-ray", "Barium meal", "HIDA scan"], 0,
  "Investigation: best method of localisation — endoscopic ultrasound. (Book p302)")
q(302, S7, "Compared with exogenous insulin injection, an insulinoma shows:",
  ["A raised C peptide", "A normal C peptide", "A zero C peptide", "No insulin at all"], 0,
  "Table: conditions with raised fasting insulin — exogenous insulin injections have a normal C peptide; insulinoma has a raised C peptide. (Book p302)")
q(303, S7, "An insulinoma GREATER than 2 cm is managed by:",
  ["Wider resection", "Enucleation only", "Observation", "Antibiotics"], 0,
  "Management: >2 cm — wider resection. (Book p303)")
q(303, S7, "An insulinoma LESS than 2 cm is managed by:",
  ["Enucleation", "Whipple's surgery", "Total pancreatectomy", "Observation only"], 0,
  "Management: <2 cm — enucleation. (Book p303)")
q(303, S7, "Diazoxide in insulinoma:",
  ["Inhibits insulin release and prevents hypoglycaemia", "Increases insulin release", "Dissolves the tumour", "Treats the diabetes"], 0,
  "Management: diazoxide — inhibits release of insulin and prevents hypoglycaemia. (Book p303)")
q(303, S7, "Insulinoma with metastasis is treated with:",
  ["Chemotherapy, streptozocin and diazoxide", "Observation only", "Antibiotics only", "Radiotherapy alone"], 0,
  "Management: in metastasis — chemotherapy, streptozocin, diazoxide. (Book p303)")

# ------------------------------------------------------------------ p303-304
S8 = "Gastrinoma"
q(303, S8, "Gastrinoma is also known as:",
  ["Zollinger Ellison syndrome", "MEN syndrome", "WDHA syndrome", "Peutz-Jeghers syndrome"], 0,
  "Gastrinoma: aka Zollinger Ellison syndrome. (Book p303)")
q(303, S8, "Gastrinoma arises from:",
  ["Gastrin producing G-cells", "Beta cells", "Alpha cells", "Parietal cells"], 0,
  "Gastrinoma: arise from gastrin producing (G-cells) cells. (Book p303)")
q(303, S8, "Gastrinoma is the most common pancreatic endocrine neoplasm in:",
  ["MEN 1 syndrome", "MEN 2 syndrome", "Down's syndrome", "Turner syndrome"], 0,
  "Gastrinoma: m/c pancreatic endocrine neoplasm in MEN 1 syndrome. (Book p303)")
q(303, S8, "What proportion of gastrinomas are malignant?",
  ["70-80%", "10-20%", "50%", "100%"], 0,
  "Gastrinoma: malignant (70-80%). (Book p303)")
q(303, S8, "Passaro's (gastrinoma) triangle is:",
  ["The most common site of the gastrinoma", "The site of the cystic artery", "The gallbladder fossa", "The splenic hilum"], 0,
  "Passaro's triangle/gastrinoma triangle: m/c site of the gastrinoma. (Book p303)")
q(303, S8, "One boundary of Passaro's triangle is:",
  ["The junction of the cystic and common hepatic duct", "The splenic flexure", "The falciform ligament", "The left kidney"], 0,
  "Boundaries: junction of cystic + common hepatic duct. (Book p303)")
q(303, S8, "Another boundary of Passaro's triangle is:",
  ["The junction of the head and neck with the body of the pancreas", "The pancreatic tail", "The duodenojejunal flexure", "The hepatic flexure"], 0,
  "Boundaries: junction of head and neck with body of the pancreas. (Book p303)")
q(303, S8, "The third boundary of Passaro's triangle is:",
  ["The junction of D2 and D3 of the duodenum", "The pylorus", "The ampulla only", "The jejunum"], 0,
  "Boundaries: junction of D2 and D3 (D: duodenum). (Book p303)")
q(303, S8, "The most common site of a gastrinoma is the wall of:",
  ["D1", "D3", "The jejunum", "The stomach antrum"], 0,
  "M/c site of gastrinoma: wall of D1. (Book p303)")
q(303, S8, "A gastrinoma located OUTSIDE Passaro's triangle is:",
  ["More aggressive, larger in size, with poor prognosis", "More indolent and smaller", "Always benign", "Always in D1"], 0,
  "Gastrinoma outside Passaro's triangle: more aggressive, larger in size, poor prognosis. (Book p303)")
q(303, S8, "The clinical features of gastrinoma include:",
  ["Pain, diarrhoea, multiple recurrent peptic ulcers", "Painless jaundice only", "Obstipation", "Weight gain"], 0,
  "Clinical features: pain, diarrhoea, peptic ulcer, multiple, recurrent. (Book p303)")
q(303, S8, "Atypical locations of gastrinoma peptic ulcers include:",
  ["D3 and the jejunum", "Only the stomach", "Only the duodenal bulb", "Only the colon"], 0,
  "Clinical features: atypical locations — D3, jejunum. (Book p303)")
q(303, S8, "In gastrinoma, the diarrhoea is due to:",
  ["Acidic pH in the duodenum causing non-activation of pancreatic enzymes and malabsorption", "Bacterial overgrowth only", "Lactose intolerance", "A normal mechanism"], 0,
  "Pathophysiology: raised gastrin — raised HCl production, peptic ulcer; acidic pH in duodenum — non-activation pancreatic enzyme, malabsorption and diarrhoea. (Book p303)")
q(304, S8, "The Zollinger Ellison triad consists of:",
  ["Increased gastrin, increased acid output and a non-beta cell tumour", "Fasting hypoglycaemia, low glucose and resolution on glucose", "Pain, jaundice and fever", "Pneumobilia, SBO and stone"], 0,
  "Zollinger Ellison triad: 1. Increased gastrin, 2. Increased acid output, 3. Non-beta cell tumour. (Book p304)")
q(304, S8, "A serum gastrin level greater than 1000 pg/mL in gastrinoma is:",
  ["Diagnostic", "Normal", "Mildly raised", "A false positive"], 0,
  "Diagnosis: S. gastrin >1000 pg/mL — diagnostic. (Book p304)")
q(304, S8, "When the serum gastrin is less than 1000 pg/mL, the secretin stimulation test is positive if:",
  ["Serum gastrin rises by 300 pg/mL after the test", "Serum gastrin falls by 300 pg/mL", "The pH becomes alkaline", "The C peptide falls"], 0,
  "Diagnosis: S. gastrin <1000 pg/mL — secretin stimulation test, S. gastrin increased by 300 pg/mL after test — positive. (Book p304)")
q(304, S8, "A pH of less than 2.0 in the duodenum is:",
  ["Diagnostic of gastrinoma", "Normal", "Seen only in Zollinger Ellison triad patients with no treatment", "Excludes gastrinoma"], 0,
  "Diagnosis: pH <2.0 — diagnostic. (Book p304)")
q(304, S8, "For localisation, gastrinoma is investigated by SRS, which stands for:",
  ["Somatostatin receptor scintigraphy", "Standard radio isotope survey", "Small bowel radio series", "Sequential radiological scintigraphy"], 0,
  "Localisation: SRS — somatostatin receptor scintigraphy. (Book p304)")
q(304, S8, "On somatostatin receptor scintigraphy, a gastrinoma:",
  ["Lightens up", "Does not light up", "Disappears", "Calcifies"], 0,
  "SRS: does not lighten — insulinoma; lightens — gastrinoma. (Book p304)")
q(304, S8, "On somatostatin receptor scintigraphy, an insulinoma:",
  ["Does not light up", "Lightens up", "Disappears completely", "Shows a double duct sign"], 0,
  "SRS: does not lighten — insulinoma. (Book p304)")
q(304, S8, "A patient with gastrinoma should also be evaluated for:",
  ["MEN 1 syndrome", "Down's syndrome", "Turner syndrome", "Addison's disease"], 0,
  "Localisation: evaluation for MEN 1 syndrome. (Book p304)")
q(304, S8, "A gastrinoma GREATER than 5 mm is managed by:",
  ["Full thickness resection", "Enucleation", "Observation", "Antibiotics"], 0,
  "Management: >5 mm — full thickness resection. (Book p304)")
q(304, S8, "A gastrinoma of 5 mm or LESS is managed by:",
  ["Enucleation", "Full thickness resection", "Whipple's surgery in all", "Observation only"], 0,
  "Management: <5 mm — enucleation. (Book p304)")
q(304, S8, "The most common site of gastrinoma metastasis is:",
  ["The liver", "The lung", "The bone", "The brain"], 0,
  "Metastasis: m/c site — liver. (Book p304)")
q(304, S8, "Octreotide in gastrinoma is used to:",
  ["Decrease gastrin secretion", "Increase acid output", "Remove the tumour", "Prevent the ulcers mechanically"], 0,
  "Metastasis: octreotide — decreased secretion of gastrin. (Book p304)")
q(304, S8, "Streptozocin is used in gastrinoma for:",
  ["Malignant or metastatic carcinoma", "Benign gastrinoma only", "Gastric ulcers only", "Pancreatitis only"], 0,
  "Metastasis: streptozocin — for malignant/metastatic carcinoma. (Book p304)")

# ------------------------------------------------------------------ p304-305
S9 = "Glucagonoma, WDHA and Somatostatinoma"
q(304, S9, "Glucagonoma arises from:",
  ["Alpha cells of the islets of Langerhans", "Beta cells", "G cells", "Parietal cells"], 0,
  "Glucagonoma: origin — alpha cells of islets of Langerhans. (Book p304)")
q(304, S9, "Diabetes in glucagonoma is due to:",
  ["Raised blood sugar", "Low blood sugar", "Insulin excess", "A Phrygian cap"], 0,
  "Glucagonoma: diabetes — d/t raised blood sugar. (Book p304)")
q(304, S9, "The dermatitis of glucagonoma is:",
  ["Necrolytic migratory rash", "Psoriasis", "Eczema", "Urticaria"], 0,
  "Glucagonoma: dermatitis — necrolytic migratory rash. (Book p304)")
q(304, S9, "Migratory thrombophlebitis in glucagonoma is also known as:",
  ["Trousseau syndrome", "Courvoisier's law", "Rigler's triad", "Bouveret syndrome"], 0,
  "Glucagonoma: DVT — migratory thrombophlebitis — Trousseau syndrome. (Book p304)")
q(304, S9, "Which of the following is a feature of glucagonoma?",
  ["Depression", "Fasting hypoglycaemia", "A WES sign", "Pneumobilia"], 0,
  "Glucagonoma: depression. (Book p304)")
q(305, S9, "WDHA syndrome is also known as:",
  ["Verner Morrison syndrome", "Zollinger Ellison syndrome", "Peutz-Jeghers syndrome", "MEN 1 syndrome"], 0,
  "WDHA syndrome: aka Verner Morrison syndrome. (Book p305)")
q(305, S9, "WDHA syndrome is due to a raised:",
  ["Vasoactive intestinal peptide (VIPoma)", "Gastrin", "Insulin", "Glucagon"], 0,
  "WDHA syndrome: d/t raised vasoactive intestinal peptide — VIPoma. (Book p305)")
q(305, S9, "The features of WDHA syndrome include:",
  ["Watery diarrhoea, hypokalaemia, achlorhydria and acidosis", "Steatorrhoea only", "Hypertension only", "Painless jaundice"], 0,
  "WDHA: watery diarrhoea, hypokalaemia, achlorhydria, acidosis. (Book p305)")
q(305, S9, "The features of somatostatinoma include:",
  ["Steatorrhoea due to malabsorption, diabetes and cholelithiasis", "Fasting hypoglycaemia", "Necrolytic migratory rash", "Watery diarrhoea with hypokalaemia"], 0,
  "Somatostatinoma: steatorrhoea d/t malabsorption, diabetes, cholelithiasis. (Book p305)")

# ------------------------------------------------------------------ p305-306
S10 = "Non-functional and Cystic Neoplasms"
q(305, S10, "A non functional pancreatic endocrine neoplasm is typically seen in:",
  ["Elderly patients", "Neonates", "Only in pregnancy", "Only in children"], 0,
  "Non functional pancreatic endocrine neoplasm: elderly patients. (Book p305)")
q(305, S10, "A non functional pancreatic endocrine neoplasm is usually:",
  ["Malignant", "Always benign", "Benign in 90%", "Cystic"], 0,
  "Non functional: malignant. (Book p305)")
q(305, S10, "The most common site of origin of a non functional pancreatic endocrine neoplasm is:",
  ["The head of the pancreas", "The tail", "The body only", "The uncinate process only"], 0,
  "Non functional: origin — m/c head of pancreas. (Book p305)")
q(305, S10, "Blood markers of a non functional pancreatic endocrine neoplasm include:",
  ["Chromogranin A and synaptophysin", "AFP", "PSA", "CA-125 only"], 0,
  "Non functional: presence of chromogranin A, synaptophysin in blood. (Book p305)")
q(305, S10, "The management of a non functional pancreatic endocrine neoplasm is:",
  ["Resection", "Observation", "Antibiotics", "Diazoxide"], 0,
  "Non functional: Mx — resection. (Book p305)")
q(305, S10, "A serous cystic neoplasm of the pancreas is most commonly sited at:",
  ["The head of the pancreas", "The tail", "The body only", "The uncinate process only"], 0,
  "Serous cystic neoplasm: site — head of pancreas (m/c). (Book p305)")
q(305, S10, "Serous cystic neoplasms are seen in:",
  ["Older patients", "Neonates", "Only in pregnancy", "Only in the young"], 0,
  "Serous cystic neoplasm: older patients. (Book p305)")
q(305, S10, "Serous cystic neoplasms are characterised histologically by:",
  ["Glycogen rich cells", "Ovarian-like stroma", "Beta catenin mutation", "Inflammatory cells only"], 0,
  "Serous cystic neoplasm: presence of glycogen rich cells. (Book p305)")
q(305, S10, "In a serous cystic neoplasm, the CEA is:",
  ["Not raised", "Markedly raised", "Always zero", "Unmeasurable"], 0,
  "Serous cystic neoplasm: CEA not raised; large multiloculate mass, usually benign. (Book p305)")
q(305, S10, "A serous cystic neoplasm on CECT shows:",
  ["A sunburst appearance", "An egg shell calcification", "A double duct sign", "A double bubble"], 0,
  "Investigation: CECT (IOC) — sunburst appearance. (Book p305)")
q(305, S10, "A large and symptomatic serous cystic neoplasm is managed by:",
  ["Enucleation", "Observation", "Chemotherapy", "Radiotherapy"], 0,
  "Management: large and symptomatic — enucleation. (Book p305)")
q(305, S10, "A small and asymptomatic serous cystic neoplasm is managed by:",
  ["Observation", "Immediate enucleation", "Whipple's surgery", "Antibiotics"], 0,
  "Management: small and asymptomatic — observation. (Book p305)")
q(306, S10, "Mucinous tumours of the pancreas are most commonly sited at:",
  ["The body and tail of the pancreas", "The head only", "The uncinate process only", "The ampulla only"], 0,
  "Mucinous tumours: site — body and tail of pancreas. (Book p306)")
q(306, S10, "Mucinous cystic neoplasms are most common in:",
  ["Pre-menopausal females", "Males", "Children", "Both sexes equally"], 0,
  "Mucinous tumours: m/c in females (pre menopausal). (Book p306)")
q(306, S10, "The characteristic stroma of a mucinous cystic neoplasm is:",
  ["Ovarian like stroma", "Granulation tissue", "Fibrous tissue only", "Adipose tissue only"], 0,
  "Mucinous tumours: ovarian like stroma. (Book p306)")
q(306, S10, "Mucinous cystic neoplasms are:",
  ["ER and PR positive", "ER and PR negative", "Only CEA positive", "Only AFP positive"], 0,
  "Mucinous tumours: ER, PR +ve. (Book p306)")
q(306, S10, "The CEA in a mucinous tumour of the pancreas is:",
  ["Raised", "Normal", "Zero", "Unmeasurable"], 0,
  "Mucinous tumours: raised CEA. (Book p306)")
q(306, S10, "A history of pancreatitis is a feature of a mucinous tumour, and the differential diagnosis is:",
  ["Pseudocyst", "Phrygian cap", "Porcelain gallbladder", "Bouveret syndrome"], 0,
  "Mucinous tumours: H/o pancreatitis (+); D/d — pseudocyst. (Book p306)")
q(306, S10, "Compared with a mucinous tumour, a pseudocyst is:",
  ["Homogeneous with CEA not elevated", "Heterogeneous with raised CEA", "Ovarian stroma positive", "ER positive"], 0,
  "Note: pseudocyst — homogenous, CEA not elevated. (Book p306)")
q(306, S10, "On CT, a mucinous tumour shows:",
  ["Egg shell calcification with a heterogeneous lining", "A sunburst appearance", "A double duct sign", "A double bubble sign"], 0,
  "Investigation: CT — egg shell calcification, heterogeneous lining. (Book p306)")
q(306, S10, "Intraductal papillary mucinous neoplasm (IPMN) has how many types?",
  ["Three", "One", "Two", "Four"], 0,
  "IPMN: 3 types. (Book p306)")
q(306, S10, "The types of IPMN are:",
  ["Branch duct, main duct and mixed", "Serous and mucinous only", "Solid and cystic only", "Benign and malignant only"], 0,
  "IPMN: branch duct type, main duct type, mixed type (starts in branch duct, then main duct). (Book p306)")
q(306, S10, "The mixed type of IPMN:",
  ["Starts in the branch duct and then involves the main duct", "Involves only the main duct", "Involves only the branch duct", "Never involves the ducts"], 0,
  "IPMN: mixed type — starts in branch duct, main duct. (Book p306)")
q(306, S10, "Ohashi's triad of IPMN consists of:",
  ["Dilated hepatopancreatic duct, fish mouth appearance of the ampulla and mucin coming out", "Waxing jaundice, melena and a mass", "Pain, jaundice and fever", "Pneumobilia, SBO and a stone"], 0,
  "Ohashi triad: 1. Dilated hepatopancreatic duct, 2. Fish mouth appearance of ampulla, 3. Mucin coming out. (Book p306)")
q(306, S10, "The diagnosis of IPMN is made by:",
  ["ERCP", "Plain X-ray", "USG alone", "Barium meal"], 0,
  "IPMN: Dx — ERCP. (Book p306)")
q(306, S10, "A MAIN DUCT or MIXED type IPMN greater than 2 cm is managed by:",
  ["Resection", "Observation", "Antibiotics", "Diazoxide"], 0,
  "IPMN Mx: main duct/mixed type >2 cm — resection. (Book p306)")
q(306, S10, "A BRANCH DUCT type IPMN of 2 cm or less is managed by:",
  ["Observation", "Immediate resection", "Chemotherapy", "Radiotherapy"], 0,
  "IPMN Mx: branch duct type <2 cm — observe. (Book p306)")
q(306, S10, "A solid pseudopapillary tumour is also known as:",
  ["Gruber Frantz tumour (aka Hamoudi tumour)", "Beger's tumour", "Puestow's tumour", "Duval's tumour"], 0,
  "Solid pseudopapillary tumour/Gruber Frantz tumour: aka Hamoudi tumour. (Book p306)")
q(306, S10, "Solid pseudopapillary tumours are seen in:",
  ["Females", "Males only", "Children only", "Both sexes equally"], 0,
  "Solid pseudopapillary tumour: seen in females. (Book p306)")
q(306, S10, "The site of a solid pseudopapillary tumour is:",
  ["The tail of the pancreas", "The head only", "The uncinate process only", "The ampulla only"], 0,
  "Solid pseudopapillary tumour: site — tail. (Book p306)")
q(306, S10, "The mutation of a solid pseudopapillary tumour is:",
  ["Beta catenin / vimentin mutation", "K-ras mutation only", "PRSS1 mutation", "CFTR mutation"], 0,
  "Solid pseudopapillary tumour: beta catenin/vimentin mutation. (Book p306)")
q(306, S10, "The management of a solid pseudopapillary tumour is:",
  ["Resection", "Observation", "Antibiotics", "Diazoxide"], 0,
  "Solid pseudopapillary tumour: Mx — resection. (Book p306)")

# ------------------------------------------------------------------ units
def first_page(label):
    for x in Q:
        if x["sec"] == label:
            return x["page"]
    return 0


UNIT_DEFS = [
    (S1, "Pancreatic ductal adenocarcinoma is the commonest carcinoma of the pancreas, fed by smoking, obesity, African American ethnicity, chronic pancreatitis and the gene list — PRSS1 of hereditary pancreatitis, SPINK1 of tropical calcific pancreatitis — plus the syndromes: Peutz-Jeghers (STK11) with its 100-fold risk, the melanoma-mole family, cystic fibrosis, BRCA-2 (pancreas, prostate, male breast), Lynch (and its colorectal risk) and FAP. The road runs through PanIN: K-ras first and commonest at 1A/1B, CDKN2A at 2A, p53 and SMAD4 at 3, then the final hit — K53."),
    (S2, "Periampullary carcinoma bundles four cancers within 2 cm of the ampulla — pancreatic head, ampullary, distal cholangiocarcinoma and duodenal adenocarcinoma — with similar presentation and management. They present as progressive, surgical obstructive jaundice with weight loss, and pain that bites hardest from the body and tail. The ampullary variety waxes and wanes, each fade of jaundice sloughing tumour into the bowel as melena; the duodenal adenocarcinoma blocks the outlet. Courvoisier's law holds firm — a palpable gallbladder with obstructive jaundice is seldom stone, because stones fibrose the gallbladder shrivelled while a tumour lets it balloon pyriform and palpable; the exceptions are the 10% primary CBD stone, double impaction, the Chinese liver fluke of oriental cholangiohepatitis and Mirizzi's fistula."),
    (S3, "CECT is the IOC of pancreatic cancer; duodenography with its Frostberg reverse 3 sign is obsolete, and the X-ray shows only widened duodenal loops. MRCP and ERCP carry the double duct sign — a blocked ampulla dilating both the pancreatic duct and the CBD — and when the radiological diagnosis is in doubt, a transgastric EUS-guided FNAC settles it. CA 19-9 is the predictive and prognostic marker that flags patients for staging laparoscopy before definitive surgery, stays an important (if not specific) prognostic marker when normalised by neoadjuvant chemo, and is shared with cholangiocarcinoma and gallbladder cancer; PET CT completes the staging."),
    (S4, "The AJCC stages it: T1 up to 2 cm, T2 from 2 to 4, T3 beyond 4, T4 by adjacent involvement; M1 metastases land in the liver; N1 is 1-3 nodes, N2 more than three. Varadhachary-Katz decides resectability on the vessels — a clear SMA with a patent portal junction goes straight to surgery; abutment over 180 degrees or under 50% with short-segment occlusion is borderline, taking chemotherapy before surgery; encasement with long-segment occlusion is locally advanced and palliative. Diagnostic laparoscopy is the IOC for peritoneal mets — found, and the procedure is abandoned; peritoneal mets, malignant ascites or liver mets write the word unresectable. Resectable head or periampullary disease is Whipple's; body and tail take a distal pancreatectomy."),
    (S5, "Whipple's is the pancreaticoduodenectomy: a chevron or roof top incision, then cholecystectomy, CBD, pylorus, pancreatectomy and duodenectomy out, and three anastomoses in — hepaticojejunostomy on the common hepatic duct, gastrojejunostomy and pancreaticojejunostomy. The pylorus-preserving Longmire transverso variant is preferred for fewer dumping syndrome episodes, with the conventional Whipple reserved for an involved pylorus or unattainable margin; the tunnel of love between vessels and pancreas must be intact to proceed at all. Its complications rank: impaired gastric emptying is the commonest (lost receptive relaxation, worse with the conventional), sepsis from anastomotic leak the commonest cause of death, and the pancreatic fistula — a pancreaticojejunostomy leak on post op day 2-3 with turbid amylase-rich drainage that stops spontaneously and answers to octreotide. Gemcitabine plus capecitabine beats monotherapy for effect, FOLFIRINOX for survival."),
    (S6, "Unresectable disease is palliated: the pruritus and jaundice by ERCP stenting or PTBD (the distal blockage dilates the proximal radicals for puncture drainage), pain by coeliac ganglion block, and the double obstruction prophylactically by the triple bypass — hepaticojejunostomy for bile, gastrojejunostomy against gastric outlet obstruction, jejunojejunostomy — all without touching the tumour. NAB paclitaxel is the listed chemo, and stage remains the most important prognostic factor."),
    (S7, "The insulinoma is the commonest endocrine tumour, a beta-cell lesion, 90% benign and evenly scattered through the gland. Whipple's triad — fasting hypoglycaemia, glucose below 50, rapid resolution with glucose — frames it; the 72-hour fast was the gold standard until it went obsolete, and now the insulin/glucose ratio over 0.3 and the C peptide (raised, unlike exogenous insulin's normal one) carry the diagnosis, with EUS as the best localisation. Under 2 cm it is enucleated, over 2 cm more widely resected; diazoxide holds the insulin in check, and metastatic disease takes chemotherapy, streptozocin and diazoxide."),
    (S8, "The gastrinoma — Zollinger Ellison syndrome — is the G-cell tumour, the commonest pancreatic endocrine neoplasm of MEN 1, malignant in 70-80%. It hides in Passaro's triangle (cystic-common hepatic junction, head-neck to body junction, D2-D3 junction), most often in the wall of D1; outside the triangle it is bigger, more aggressive and poorer. Acid floods: gastrin up, HCl up, ulcers multiple, recurrent and atypical in D3 and jejunum, the acidic duodenum inactivating the enzymes into malabsorptive diarrhoea. The triad — raised gastrin, raised acid output, non-beta cell tumour — is proved by a gastrin above 1000, or a secretin rise of 300 below that, with a duodenal pH under 2. SRS lights it up (the insulinoma stays dark), MEN 1 is screened, over 5 mm is fully resected, under 5 mm enucleated, and liver metastases take octreotide against the gastrin and streptozocin against the malignancy."),
    (S9, "The rare endocrines each keep their signature: the glucagonoma from alpha cells brings diabetes from high sugar, the necrolytic migratory rash, migratory thrombophlebitis (Trousseau) and depression. WDHA — Verner Morrison — is the VIPoma of watery diarrhoea, hypokalaemia, achlorhydria and acidosis; the somatostatinoma steatorrhoeas, sweetens the blood to diabetes and seeds the gallbladder with stones."),
    (S10, "The non-functional endocrine neoplasm hits the elderly, is malignant, favours the head and announces itself with chromogranin A and synaptophysin — resect it. The cystic neoplasms are a family to sort: the serous cystic neoplasm, an older patient's head mass of glycogen-rich cells, CEA normal, multiloculated and usually benign, sunburst on CECT — enucleated if large and symptomatic, watched if small. The mucinous tumour, pre-menopausal women in the body and tail with ovarian-like stroma, ER/PR positive, CEA raised and a pancreatitis history (against which the pseudocyst is homogeneous and CEA quiet), egg-shell calcified with a heterogeneous lining. IPMN comes in branch, main and mixed (branch first, then main), triad of Ohashi — dilated hepatopancreatic duct, fish-mouth ampulla, mucin oozing — diagnosed by ERCP: main/mixed over 2 cm resected, branch duct up to 2 cm observed. And the solid pseudopapillary (Gruber Frantz, aka Hamoudi) tumour of the tail in women, beta-catenin/vimentin mutated, is resected."),
]

UNITS = []
for i, (title, guide) in enumerate(UNIT_DEFS, 1):
    UNITS.append({
        "id": f"SURG-U40-{i}",
        "ch": 40,
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
with open("data/ch40.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
print(f"ch40: {len(Q)} questions, {len(UNITS)} units")
