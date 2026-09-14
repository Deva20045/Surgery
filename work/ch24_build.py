#!/usr/bin/env python3
"""Build data/ch24.json for PULSE Surgery ch24 (Stomach : Part 3, book p161-169)."""
import json

Q = []
def q(page, sec, text, opts, ans, exp):
    Q.append({"id": f"SURG-C24-{len(Q)+1:03d}", "sec": sec, "page": page,
              "q": text, "opts": opts, "ans": ans, "exp": exp})

# ---------------- p161 · RISK FACTORS ----------------
S1 = "Gastric Cancer: Risk Factors"
q(161, S1, "All of the following are risk factors for gastric cancer EXCEPT:",
  ["Refrigeration of food (reduced preservative intake)", "Smoking",
   "Consumption of smoked food/fish", "Alcohol consumption"], 0,
  "Risk factors: smoking, alcohol, smoked food/fish, preservative rich food - refrigeration ↓ gastric cancer. (Book p161)")
q(161, S1, "Refrigeration of food (with less preservative use) has what effect on gastric cancer?",
  ["Decreases the incidence", "Increases the incidence", "No effect",
   "Doubles the incidence"], 0,
  "Preservative rich food ↑ risk; refrigeration ↓ gastric cancer. (Book p161)")
q(161, S1, "True (adenomatous) gastric polyps are associated with:",
  ["FAP (APC gene)", "Peutz-Jeghers syndrome", "Juvenile polyposis", "Cowden syndrome"], 0,
  "Polyps: true (adenomatous) polyps are associated with FAP (APC gene). (Book p161)")
q(161, S1, "The m/c gastric polyp is the:",
  ["Metaplastic polyp (H. pylori associated)", "Adenomatous polyp", "Hamartomatous polyp",
   "Inflammatory fibroid polyp"], 0,
  "m/c gastric polyp: metaplastic (H. pylori). (Book p161)")
q(161, S1, "Menetrier's disease, a risk factor for gastric cancer, is characterised by:",
  ["Hypertrophy of gastric mucosal folds", "Atrophy of the gastric mucosa",
   "Multiple gastric ulcers", "Gastric outlet obstruction"], 0,
  "Menetrier's disease: hypertrophy of gastric mucosal folds. (Book p161)")
q(161, S1, "The blood group associated with an increased risk of gastric cancer is:",
  ["Group A", "Group O", "Group B", "Bombay blood group"], 0,
  "Risk factors: group A blood group. (Book p161)")
q(161, S1, "Previous gastric resection predisposes to cancer of the:",
  ["Gastric stump", "Esophagus", "Duodenum", "Colon"], 0,
  "Risk factors: previous gastric resections. (Book p161)")
q(161, S1, "Which gastritis is a risk factor for gastric cancer?",
  ["Both type A and type B", "Type A only", "Type B only", "Neither type"], 0,
  "Risk factors: gastritis (type A & B). (Book p161)")
q(161, S1, "The infection associated with an increased risk of gastric cancer is:",
  ["H. pylori", "HPV", "HBV", "CMV"], 0,
  "Risk factors: H. pylori infection. (Book p161)")
q(161, S1, "Which dietary habit increases the risk of gastric cancer?",
  ["Consumption of smoked food/fish", "Refrigerated fresh food", "High fibre diet",
   "Citrus rich diet"], 0,
  "Risk factors: consumption of smoked food/fish and preservative rich food. (Book p161)")
q(161, S1, "Adenomatous gastric polyps are considered:",
  ["True (neoplastic) polyps with malignant potential", "Metaplastic polyps",
   "Hamartomas", "Inflammatory pseudopolyps"], 0,
  "True (adenomatous) polyps: associated with FAP (APC gene) - malignant potential. (Book p161)")

# ---------------- p161 · LAUREN CLASSIFICATION ----------------
S2 = "Lauren Classification: Intestinal v/s Diffuse"
q(161, S2, "Lauren's classification divides gastric adenocarcinoma into:",
  ["Intestinal and diffuse types", "Polypoid and ulcerative types",
   "Superficial and penetrating types", "Early and advanced types"], 0,
  "1. Lauren classification: intestinal v/s diffuse. (Book p161)")
q(161, S2, "The intestinal type of gastric cancer is associated with:",
  ["Environmental factors - gastric atrophy and intestinal metaplasia",
   "Familial factors and blood type A", "Younger age group", "Decreased E-cadherin"], 0,
  "Intestinal: environmental factors - gastric atrophy, intestinal metaplasia. (Book p161)")
q(161, S2, "The diffuse type of gastric cancer is associated with:",
  ["Familial factors and blood type A", "Gastric atrophy and intestinal metaplasia",
   "Older age group", "Microsatellite instability"], 0,
  "Diffuse: familial factors, blood type A. (Book p161)")
q(161, S2, "The gender distribution in the intestinal type of gastric cancer is:",
  ["Men > women", "Women > men", "Equal in both", "Seen only in women"], 0,
  "Intestinal: men > women; diffuse: women > men. (Book p161)")
q(161, S2, "The diffuse type of gastric cancer is seen in the:",
  ["Younger age group", "Elderly with increasing incidence with age",
   "Only in children", "Equal at all ages"], 0,
  "Intestinal: increasing incidence with age; diffuse: younger age group. (Book p161)")
q(161, S2, "The histology of the intestinal type of gastric cancer shows:",
  ["Gland formation", "Poorly differentiated tumour with signet ring cells",
   "Signet ring cells (+)", "No gland formation"], 0,
  "Intestinal HPE: gland formation; diffuse: poorly differentiated. (Book p161)")
q(161, S2, "Signet ring cells are characteristic of the:",
  ["Diffuse type", "Intestinal type", "Both types equally", "Neither type"], 0,
  "Diffuse type: poorly differentiated, more aggressive, signet ring cells (+). (Book p161)")
q(161, S2, "The main route of spread in the intestinal type of gastric cancer is:",
  ["Hematogenous spread", "Transmural/lymphatic spread", "Peritoneal seedling only",
   "Perineural spread"], 0,
  "Intestinal: hematogenous spread; diffuse: transmural/lymphatic spread. (Book p161)")
q(161, S2, "The main route of spread in the diffuse type of gastric cancer is:",
  ["Transmural/lymphatic spread", "Hematogenous spread", "Peritoneal seedling only",
   "Perineural spread"], 0,
  "Diffuse: transmural/lymphatic spread. (Book p161)")
q(161, S2, "Decreased E-cadherin is seen in the:",
  ["Diffuse type", "Intestinal type", "Both types", "Neither type"], 0,
  "Diffuse: decreased E-cadherin. (Book p161)")
q(161, S2, "Microsatellite instability and APC gene mutations are associated with the:",
  ["Intestinal type", "Diffuse type", "Both types equally", "Neither type"], 0,
  "Intestinal: microsatellite instability, APC gene mutations. (Book p161)")

# ---------------- p162 · EARLY / ADVANCED & BORMANN ----------------
S3 = "Early & Advanced Gastric Cancer: Japanese and Bormann"
q(162, S3, "Early gastric cancer is classified by the:",
  ["Japanese classification", "Bormann classification", "Lauren classification",
   "Siewert classification"], 0,
  "Early gastric cancer: Japanese classification (above muscle layer). (Book p162)")
q(162, S3, "Early gastric cancer is a tumour limited to:",
  ["Above the muscle layer (mucosa and submucosa)", "Below the muscle layer",
   "The serosa", "Adjacent structures"], 0,
  "Japanese classification: tumour above the muscle layer. (Book p162)")
q(162, S3, "Advanced gastric cancer, with the muscle layer involved, is classified by the:",
  ["Bormann classification", "Japanese classification", "Lauren classification",
   "TNM only"], 0,
  "Advanced gastric cancer: Bormann classification (muscle layer involved). (Book p162)")
q(162, S3, "Bormann type I gastric cancer is:",
  ["Polypoid or fungating", "Ulcerated with surrounding elevated borders",
   "Diffusely infiltrating (linitis plastica)", "Unable to be classified"], 0,
  "Bormann type I: polypoid or fungating cancers. (Book p162)")
q(162, S3, "Bormann type II gastric cancer is:",
  ["Fungating or ulcerated with surrounding elevated borders", "Polypoid",
   "Diffusely infiltrating", "Flat and superficial"], 0,
  "Type II: fungating or ulcerated with surrounding elevated borders. (Book p162)")
q(162, S3, "Bormann type III gastric cancer is:",
  ["Ulcerated lesions infiltrating the gastric wall", "Polypoid or fungating",
   "Linitis plastica", "Unable to be classified"], 0,
  "Type III: ulcerated lesions infiltrating the gastric wall. (Book p162)")
q(162, S3, "Bormann type IV gastric cancer is:",
  ["Linitis plastica (diffusely infiltrating)", "Polypoid or fungating",
   "Ulcerated with elevated borders", "Superficial flat lesion"], 0,
  "Type IV: linitis plastica - diffusely infiltrating. (Book p162)")
q(162, S3, "Linitis plastica is also known as:",
  ["Leather bottle appearance", "Cascade stomach", "Hourglass stomach", "Cup and spill stomach"], 0,
  "Linitis plastica: aka leather bottle appearance. (Book p162)")
q(162, S3, "The most aggressive Bormann type with the worst prognosis is:",
  ["Type IV (linitis plastica)", "Type I", "Type II", "Type III"], 0,
  "Type IV: most aggressive type, worst prognosis. (Book p162)")
q(162, S3, "Bormann type V means the tumour is:",
  ["Unable to be classified", "Polypoid", "Diffusely infiltrating", "Limited to mucosa"], 0,
  "Type V: unable to be classified. (Book p162)")
q(162, S3, "Which gastric cancer carries the best prognosis?",
  ["Early gastric cancer (above the muscle layer)", "Bormann type III",
   "Bormann type IV", "Linitis plastica"], 0,
  "Early gastric cancer (Japanese classification, above muscle layer) has the best prognosis. (Book p162)")
q(162, S3, "In the Japanese macroscopic typing of early gastric cancer, type IIc is a:",
  ["Depressed lesion", "Elevated lesion", "Flat lesion", "Excavated lesion"], 0,
  "Early gastric cancer types: I polypoid, IIa elevated, IIb flat, IIc depressed, III excavated. (Book p162)")
q(162, S3, "In the Japanese macroscopic typing of early gastric cancer, type III is:",
  ["Excavated", "Polypoid", "Flat", "Depressed"], 0,
  "Type III: excavated lesion. (Book p162)")

# ---------------- p162 · MOLECULAR CLASSIFICATION ----------------
S4 = "Molecular Classification of Gastric Cancer"
q(162, S4, "The molecular subtype of gastric cancer associated with intestinal pathology and the best prognosis is:",
  ["Chromosomal instability", "Genomically stable", "EBV related", "Microsatellite instability"], 0,
  "Chromosomal instability: intestinal pathology, best prognosis. (Book p162)")
q(162, S4, "The genomically stable molecular subtype of gastric cancer is associated with:",
  ["Diffuse pathology and the worst prognosis", "Intestinal pathology and best prognosis",
   "EBV infection", "Microsatellite instability"], 0,
  "Genomically stable: diffuse pathology, worst prognosis. (Book p162)")
q(162, S4, "Epstein-Barr virus (EBV) is one of the molecular subtypes of:",
  ["Gastric cancer", "GIST", "Gastric lymphoma", "MALToma"], 0,
  "Molecular classification: Epstein Barr virus (EBV) subtype. (Book p162)")
q(162, S4, "Microsatellite instability (MSI) is a molecular subtype of:",
  ["Gastric cancer", "GIST", "Gastric lymphoma", "Trichobezoar"], 0,
  "Molecular classification: microsatellite instability (MSI) subtype. (Book p162)")

# ---------------- p162 · CLINICAL FEATURES (LOADS) ----------------
S5 = "Clinical Features: the LOADS Mnemonic"
q(162, S5, "The mnemonic used for the clinical features of gastric cancer is:",
  ["LOADS", "PAIN", "WEIGHT", "MASS"], 0,
  "Clinical features mnemonic: LOADS. (Book p162)")
q(162, S5, "In the LOADS mnemonic for gastric cancer, L stands for:",
  ["Lump", "Leukopenia", "Lethargy", "Liver enlargement"], 0,
  "LOADS: L - lump. (Book p162)")
q(162, S5, "In the LOADS mnemonic for gastric cancer, O stands for:",
  ["Gastric outlet obstruction", "Oesophageal varices", "Obstipation", "Osteomalacia"], 0,
  "LOADS: O - gastric outlet obstruction. (Book p162)")
q(162, S5, "In the LOADS mnemonic for gastric cancer, A stands for:",
  ["Anaemia and anorexia", "Ascites", "Achalasia", "Alopecia"], 0,
  "LOADS: A - anaemia, anorexia. (Book p162)")
q(162, S5, "In the LOADS mnemonic for gastric cancer, D stands for:",
  ["Dyspepsia (new onset GERD)", "Diarrhoea", "Dysphagia", "Dumping"], 0,
  "LOADS: D - dyspepsia (new onset GERD). (Book p162)")
q(162, S5, "In the LOADS mnemonic for gastric cancer, S stands for:",
  ["Silent presentation", "Splenomegaly", "Stricture", "Sepsis"], 0,
  "LOADS: S - silent presentation. (Book p162)")

# ---------------- p163 · METASTATIC SIGNS ----------------
S6 = "Metastatic Signs in Gastric Cancer"
q(163, S6, "Sister Mary Joseph's nodule is:",
  ["Periumbilical metastasis", "Left supraclavicular lymph node enlargement",
   "Left axillary lymph node enlargement", "Metastasis in the pouch of Douglas"], 0,
  "Sister Mary Joseph's nodule: periumbilical metastasis. (Book p163)")
q(163, S6, "The m/c cancer presenting as Sister Mary Joseph's nodule is:",
  ["Stomach > ovarian", "Colorectal > stomach", "Breast > lung", "Prostate"], 0,
  "Sister Mary Joseph's nodule: m/c cancer - stomach > ovarian. (Book p163)")
q(163, S6, "Krukenberg tumour refers to:",
  ["Bilateral ovarian metastases", "Periumbilical metastasis",
   "Left supraclavicular lymph node", "Pelvic peritoneal deposit"], 0,
  "Krukenberg tumor: B/L ovarian metastases. (Book p163)")
q(163, S6, "Krukenberg tumour is seen in cancers of the:",
  ["Stomach, breast > colorectal", "Lung, prostate", "Thyroid, kidney",
   "Cervix, endometrium"], 0,
  "Krukenberg tumor: seen in stomach, breast > colorectal. (Book p163)")
q(163, S6, "The latest (current) theory for the spread of Krukenberg tumour is:",
  ["Retrograde lymphatic spread", "Transcoelomic (drop) metastasis", "Hematogenous spread",
   "Direct invasion"], 0,
  "Latest theory: retrograde lymphatic spread. (Book p163)")
q(163, S6, "The old theory for the spread of Krukenberg tumour is:",
  ["Transcoelomic (drop metastases)", "Retrograde lymphatic spread", "Hematogenous spread",
   "Perineural spread"], 0,
  "Old theory: transcoelomic (drop mets). (Book p163)")
q(163, S6, "Signet ring cells are characteristically seen in:",
  ["Krukenberg tumour", "Sister Mary Joseph's nodule", "Irish nodule", "Blummer's shelf"], 0,
  "Krukenberg tumor: signet ring cells. (Book p163)")
q(163, S6, "Blummer's shelf is metastasis into the:",
  ["Pelvis / pouch of Douglas", "Umbilicus", "Left supraclavicular fossa", "Left axilla"], 0,
  "Blummer's shelf: mets into pelvis/pouch of Douglas. (Book p163)")
q(163, S6, "Blummer's shelf is best detected by:",
  ["Digital rectal examination (DRE)/imaging", "Laparoscopy", "Barium swallow",
   "Colonoscopy"], 0,
  "Diagnosis of Blummer's shelf: digital rectal examination (DRE)/imaging. (Book p163)")
q(163, S6, "Blummer's shelf is a sign of:",
  ["Advanced cancer", "Early cancer", "Benign disease", "Carcinoma in situ"], 0,
  "Blummer's shelf: sign of advanced cancer. (Book p163)")
q(163, S6, "Virchow's node (Troisier's sign) is enlargement of the:",
  ["Left supraclavicular lymph node", "Right supraclavicular lymph node",
   "Left axillary lymph node", "Periumbilical node"], 0,
  "Virchow's node/Troisier's sign: left supraclavicular lymph node enlargement. (Book p163)")
q(163, S6, "The anatomical reason for Virchow's node enlargement is involvement of the:",
  ["Thoracic duct", "Cisterna chyli", "Spleen", "Portal vein"], 0,
  "Anatomical reason: involvement of thoracic duct. (Book p163)")
q(163, S6, "Virchow's node is seen in advanced disease of:",
  ["GI and genitourinary (GU) causes", "Only the stomach", "Only the lung", "Only the breast"], 0,
  "Virchow's node: seen in GI/genitourinary (GU) causes. (Book p163)")
q(163, S6, "Irish nodule is enlargement of the:",
  ["Left axillary lymph node", "Left supraclavicular lymph node",
   "Right axillary lymph node", "Inguinal lymph node"], 0,
  "Irish nodule: left axillary lymph node enlargement. (Book p163)")
q(163, S6, "Migratory thrombophlebitis (Trousseau syndrome) is m/c associated with:",
  ["Pancreatic cancer", "Gastric cancer", "Colorectal cancer", "Lung cancer"], 0,
  "Migratory thrombophlebitis/Trousseau syndrome: m/c - pancreatic cancer. (Book p163)")
q(163, S6, "Leser-Trelat sign refers to:",
  ["Multiple seborrheic keratoses", "Hyperkeratotic palms", "Periumbilical nodule",
   "Left supraclavicular node"], 0,
  "Dermatological manifestation - a) Leser-Trelat sign: multiple seborrheic keratoses. (Book p163)")
q(163, S6, "Tripe palms refers to:",
  ["Hyperkeratotic palms", "Multiple seborrheic keratoses", "Palmar erythema",
   "Digital clubbing"], 0,
  "Dermatological manifestation - b) tripe palms: hyperkeratotic palms. (Book p163)")

# ---------------- p163 · INVESTIGATIONS ----------------
S7 = "Investigations in Gastric Cancer"
q(163, S7, "The investigation used for overall staging of gastric cancer is:",
  ["PET-CT", "CECT", "Endoscopic ultrasound", "Barium meal"], 0,
  "Overall staging: PET-CT. (Book p163)")
q(163, S7, "T and N staging of gastric cancer is best done by:",
  ["Endoscopic ultrasound (EUS)", "PET-CT", "CECT", "Diagnostic laparoscopy"], 0,
  "T & N stage: endoscopic ultrasound (EUS). (Book p163)")
q(163, S7, "The diagnosis of gastric cancer is established by:",
  ["Endoscopic biopsy", "PET-CT", "CECT", "Tumour markers"], 0,
  "Diagnosis: endoscopic biopsy. (Book p163)")
q(163, S7, "The typical endoscopic finding in gastric cancer is a:",
  ["Friable mass", "Smooth submucosal swelling", "Multiple diverticula",
   "Linear ulcer alone"], 0,
  "Endoscopic finding of gastric cancer: friable mass. (Book p163)")
q(163, S7, "The m/c site of gastric cancer overall is the:",
  ["Antrum", "Fundus", "Cardia", "Greater curvature"], 0,
  "Site: m/c overall - antrum. (Book p163)")
q(163, S7, "In the West, there is an increased incidence of:",
  ["Proximal gastric cancer", "Antral cancer", "Pyloric cancer",
   "Greater curvature cancer"], 0,
  "West: ↑ incidence of proximal gastric cancer. (Book p163)")

# ---------------- p164 · TNM ----------------
S8 = "TNM Classification of Gastric Cancer"
q(164, S8, "Tis in the TNM staging of gastric cancer means:",
  ["Carcinoma in situ (lamina propria)", "Tumour invades the submucosa",
   "Tumour invades the muscularis propria", "Tumour invades the serosa"], 0,
  "Tis: carcinoma in situ, lamina propria. (Book p164)")
q(164, S8, "T1a gastric cancer invades the:",
  ["Lamina propria", "Submucosa", "Muscularis propria", "Subserosa"], 0,
  "T1a: lamina propria. (Book p164)")
q(164, S8, "T1b gastric cancer means the tumour:",
  ["Invades the submucosa", "Is limited to the lamina propria",
   "Invades the muscularis propria", "Penetrates the serosa"], 0,
  "T1b: tumor invades the submucosa. (Book p164)")
q(164, S8, "T2 gastric cancer means the tumour:",
  ["Invades the muscularis propria", "Invades the submucosa",
   "Penetrates the subserosal connective tissue", "Invades adjacent structures"], 0,
  "T2: tumor invades the muscularis propria. (Book p164)")
q(164, S8, "T3 gastric cancer means the tumour:",
  ["Penetrates the subserosal connective tissue without invasion of the visceral peritoneum or adjacent structures",
   "Invades the mucosa only", "Invades the serosa", "Invades adjacent structures"], 0,
  "T3: penetrates the subserosal connective tissue without invasion of the visceral peritoneum or adjacent structures. (Book p164)")
q(164, S8, "T4 gastric cancer means the tumour:",
  ["Invades the serosa (visceral peritoneum) or adjacent structures",
   "Invades the muscularis propria", "Invades the submucosa",
   "Penetrates the subserosa only"], 0,
  "T4: tumor invades the serosa (visceral peritoneum) or adjacent structures. (Book p164)")
q(164, S8, "The minimum number of lymph nodes to be removed for staging of gastric cancer is:",
  ["15", "10", "12", "5"], 0,
  "Minimum no. of lymph nodes removed: gastric cancer - 15. (Book p164)")
q(164, S8, "The minimum number of lymph nodes to be removed for staging of esophageal cancer is:",
  ["15", "10", "12", "20"], 0,
  "Minimum no. of lymph nodes removed: esophageal cancer - 15. (Book p164)")
q(164, S8, "The minimum number of lymph nodes to be removed for staging of breast cancer is:",
  ["10", "15", "12", "5"], 0,
  "Minimum no. of lymph nodes removed: breast cancer - 10. (Book p164)")
q(164, S8, "The minimum number of lymph nodes to be removed for staging of colorectal cancer is:",
  ["12", "15", "10", "5"], 0,
  "Minimum no. of lymph nodes removed: colorectal cancer - 12. (Book p164)")
q(164, S8, "The m/c site of metastasis from gastric cancer is the:",
  ["Liver", "Lung", "Brain", "Bone"], 0,
  "m/c site of metastasis: liver. (Book p164)")

# ---------------- p164 · SURGICAL MANAGEMENT ----------------
S9 = "Surgical Management of Gastric Cancer"
q(164, S9, "The management of gastric cancer is:",
  ["Multimodality - chemotherapy, radiotherapy and surgery", "Surgery alone",
   "Chemotherapy alone", "Radiotherapy alone"], 0,
  "Management: multimodality management - chemotherapy, radiotherapy, surgery. (Book p164)")
q(164, S9, "The proximal margin aimed for in surgery for the primary gastric tumour is:",
  ["5 cm", "1 cm", "10 cm", "2 cm"], 0,
  "Surgery for 1° tumor: proximal margin - 5 cm. (Book p164)")
q(164, S9, "The distal margin aimed for in surgery for the primary gastric tumour is:",
  ["Pylorus", "Duodenum", "Jejunum", "Cardia"], 0,
  "Surgery for 1° tumor: distal margin - pylorus. (Book p164)")
q(164, S9, "An R0 resection means:",
  ["Microscopic freedom from disease", "Macroscopic clearance with microscopic residual disease",
   "Gross residual disease", "A purely palliative resection"], 0,
  "To achieve R0 resection: microscopic freedom from disease. (Book p164)")
q(164, S9, "Total gastrectomy is followed by reconstruction with:",
  ["Esophagojejunostomy using a circular stapler", "Gastroduodenostomy",
   "Roux-en-Y duodenojejunostomy", "Billroth I anastomosis"], 0,
  "Total gastrectomy followed by esophageal jejunostomy using circular stapler. (Book p164)")
q(164, S9, "A Siewert III tumour is treated by:",
  ["Subtotal gastrectomy (60-70% of stomach removed)", "Total gastrectomy",
   "Distal gastrectomy (30% of stomach removed)", "Oesophagectomy"], 0,
  "Siewart III: subtotal gastrectomy (60-70% stomach removed). (Book p164)")
q(164, S9, "A distal gastrectomy removes approximately:",
  ["30% of the stomach", "60-70% of the stomach", "90% of the stomach",
   "10% of the stomach"], 0,
  "Distal gastrectomy: 30% stomach removed. (Book p164)")
q(164, S9, "A subtotal gastrectomy removes approximately:",
  ["60-70% of the stomach", "30% of the stomach", "90% of the stomach",
   "100% of the stomach"], 0,
  "Subtotal gastrectomy: 60-70% stomach removed. (Book p164)")

# ---------------- p165 · LYMPH NODE STATIONS & CLEARANCE ----------------
S10 = "Japanese Lymph Node Stations and D1/D2 Clearance"
q(165, S10, "Lymph node clearance in gastric cancer surgery follows the:",
  ["Japanese stations", "Bormann stations", "Siewert stations", "Lauren stations"], 0,
  "Surgery for lymph node clearance: Japanese stations. (Book p165)")
q(165, S10, "Japanese lymph node station 1 is the:",
  ["Right paracardial", "Left paracardial", "Lesser curvature", "Greater curvature"], 0,
  "Station 1: right para-cardial. (Book p165)")
q(165, S10, "Japanese lymph node station 2 is the:",
  ["Left paracardial", "Right paracardial", "Lesser curvature", "Greater curvature"], 0,
  "Station 2: left para-cardial. (Book p165)")
q(165, S10, "Japanese lymph node station 3 is along the:",
  ["Lesser curvature", "Greater curvature", "Splenic artery", "Splenic hilum"], 0,
  "Station 3: lesser curvature. (Book p165)")
q(165, S10, "Japanese lymph node station 4 is along the:",
  ["Greater curvature", "Lesser curvature", "Left gastric artery", "Coeliac axis"], 0,
  "Station 4: greater curvature. (Book p165)")
q(165, S10, "Japanese lymph node stations 5 and 6 are the:",
  ["Suprapyloric and infrapyloric nodes", "Paracardial nodes", "Splenic nodes",
   "Hepatoduodenal nodes"], 0,
  "Station 5: suprapyloric; station 6: infrapyloric. (Book p165)")
q(165, S10, "Japanese lymph node stations 7, 8 and 9 are along the:",
  ["Left gastric artery, common hepatic artery and coeliac axis",
   "Splenic artery, splenic hilum and hepatoduodenal ligament",
   "Right and left paracardial region and lesser curvature",
   "Suprapyloric, infrapyloric and retropancreatic region"], 0,
  "Station 7: left gastric; 8: common hepatic; 9: celiac. (Book p165)")
q(165, S10, "Japanese lymph node stations 10 and 11 are at the:",
  ["Splenic hilum and along the splenic artery", "Coeliac axis and left gastric artery",
   "Hepatoduodenal ligament and retropancreatic region",
   "Greater and lesser curvature"], 0,
  "Station 10: splenic hilum; station 11: splenic artery. (Book p165)")
q(165, S10, "Japanese lymph node stations 12 and 13 are the:",
  ["Hepatoduodenal ligament and retropancreatic nodes", "Splenic hilum and splenic artery nodes",
   "Paracardial and pyloric nodes", "Coeliac and left gastric nodes"], 0,
  "Station 12: hepatoduodenal ligament; station 13: retropancreatic. (Book p165)")
q(165, S10, "D1 lymph node clearance means removal of stations:",
  ["1-6", "1-11", "1-13", "7-11"], 0,
  "D1 lymph node clearance: removal of 1-6 stations. (Book p165)")
q(165, S10, "D2 (optimum) lymph node clearance means removal of stations:",
  ["1-11", "1-6", "1-13", "1-3"], 0,
  "D2 lymph node clearance (optimum): removal of 1-11 stations. (Book p165)")

# ---------------- p165 · CHEMO / RADIO / NEWER MODALITIES ----------------
S11 = "Chemotherapy, Radiotherapy & Newer Modalities"
q(165, S11, "The chemotherapy drugs used in gastric cancer are:",
  ["5-FU and cisplatin", "Cyclophosphamide and methotrexate",
   "Vincristine and prednisolone", "Docetaxel and carboplatin"], 0,
  "Chemotherapy: 5FU, cisplatin. (Book p165)")
q(165, S11, "Chemotherapy in gastric cancer is indicated when there is:",
  ["Lymph node positivity", "Carcinoma in situ", "T1a mucosal disease",
   "A metaplastic polyp"], 0,
  "Indications: lymph node (+). (Book p165)")
q(165, S11, "Neo-adjuvant chemotherapy in gastric cancer is given for:",
  ["Bulky lymph nodes", "T1a tumours", "Carcinoma in situ",
   "Metaplastic polyps"], 0,
  "Indications: bulky lymph node - neo-adjuvant chemotherapy given. (Book p165)")
q(165, S11, "Which T stage of gastric cancer is an indication for chemotherapy?",
  ["T3/T4", "Tis", "T1a", "T1b"], 0,
  "Indications: T3/T4. (Book p165)")
q(165, S11, "Muscle invasion in gastric cancer is an indication for:",
  ["Chemotherapy", "Radiotherapy alone", "Endoscopic mucosal resection",
   "No further treatment"], 0,
  "Indications: muscle invasion. (Book p165)")
q(165, S11, "Radiotherapy in gastric cancer is given to the:",
  ["Stomach bed", "Whole abdomen", "Liver", "Pelvis"], 0,
  "Radiotherapy: site - stomach bed. (Book p165)")
q(165, S11, "The aim of radiotherapy in gastric cancer is to reduce the:",
  ["Loco-regional recurrence (LRR)", "Distant metastasis", "Post-gastrectomy dumping",
   "Iron deficiency"], 0,
  "Radiotherapy: to reduce loco-regional recurrence (LRR). (Book p165)")
q(165, S11, "Newer modalities used in metastatic gastric cancer include:",
  ["Pembrolizumab and nivolumab", "Imatinib and sunitinib", "Rituximab", "Bevacizumab"], 0,
  "Newer modalities for metastatic gastric cancer: pembrolizumab, nivolumab. (Book p165)")
q(165, S11, "A HER2 neu mutation in metastatic gastric cancer is treated with:",
  ["Trastuzumab", "Imatinib", "Rituximab", "Bevacizumab"], 0,
  "HER 2 neu mutation: trastuzumab. (Book p165)")
q(165, S11, "S-1 chemotherapy consists of:",
  ["Oral fluoropyrimidine with enzyme inhibitors (oteracil and gimeracil)",
   "A platinum compound alone", "A taxane alone", "An anthracycline alone"], 0,
  "S-1 chemotherapy: oral fluoropyrimidine + enzyme inhibitors (oteracil & gimeracil). (Book p165)")
q(165, S11, "Overall, the prognosis of gastric cancer depends on the:",
  ["Depth of invasion", "Lymph node status", "Tumour size", "Patient's age"], 0,
  "Note: overall - depth of invasion. (Book p165)")
q(165, S11, "In operable gastric cancer the most important prognostic factor is:",
  ["Lymph node status", "Depth of invasion", "Site of the tumour", "Histological type"], 0,
  "Operable gastric cancer: lymph node status. (Book p165)")

# ---------------- p166 · GIST BASICS ----------------
S12 = "GIST: Origin, Types and Associations"
q(166, S12, "A gastrointestinal stromal tumour arises from:",
  ["Interstitial pacemaker cells of Cajal", "Smooth muscle cells", "Neural crest cells",
   "Mucosal epithelium"], 0,
  "GIST - origin: intestinal pacemaker cells of Cajal. (Book p166)")
q(166, S12, "The m/c site of a GIST is the:",
  ["Stomach", "Small intestine", "Colon", "Esophagus"], 0,
  "GIST: m/c site - stomach. (Book p166)")
q(166, S12, "Familial GIST is associated with:",
  ["Carney's triad", "MEN 1 syndrome", "Von Hippel-Lindau disease", "FAP"], 0,
  "Types: sporadic; familial - associated with Carney's triad. (Book p166)")
q(166, S12, "Carney's triad consists of:",
  ["Gastric GIST, paraganglioma and pulmonary chondroma",
   "Gastric GIST, paraganglioma and phaeochromocytoma",
   "GIST, thyroid carcinoma and chondroma", "GIST, lipoma and chondroma"], 0,
  "Carney's triad: I. gastric GIST, II. paraganglionoma, III. pulmonary chondroma. (Book p166)")
q(166, S12, "Carney-Stratakis syndrome is due to a mutation of:",
  ["Succinate dehydrogenase B", "c-KIT", "PDGFRα", "p53"], 0,
  "Carney Stratakis syndrome: mutation of succinyl dehydrogenase B. (Book p166)")
q(166, S12, "Carney-Stratakis syndrome is associated with:",
  ["Primary resistance to imatinib", "Primary resistance to sunitinib",
   "A very good response to imatinib", "Spontaneous regression"], 0,
  "Carney Stratakis syndrome: I° resistance to imatinib. (Book p166)")

# ---------------- p166 · GIST PRESENTATION / INVESTIGATIONS ----------------
S13 = "GIST: Presentation, Spread and Investigations"
q(166, S13, "The m/c presentation of a GIST is:",
  ["Upper GI haemorrhage", "Abdominal mass", "Perforation", "Gastric outlet obstruction"], 0,
  "Presentation: upper GI hemorrhage - m/c. (Book p166)")
q(166, S13, "The usual mode of spread of a GIST is:",
  ["Local invasion and hematogenous spread", "Lymphatic spread",
   "Transcoelomic seedling", "Perineural spread"], 0,
  "Spread: local invasion; hematogenous spread m/c to liver. (Book p166)")
q(166, S13, "The m/c site of hematogenous metastasis of a GIST is the:",
  ["Liver", "Lung", "Bone", "Brain"], 0,
  "Hematogenous spread: m/c to liver. (Book p166)")
q(166, S13, "Lymphatic spread in GIST occurs in:",
  ["<10% - so lymph node clearance is not mandatory", "More than 50%", "30-40%", "Never"], 0,
  "Lymphatic spread: <10% (LN clearance not mandatory). (Book p166)")
q(166, S13, "The investigation of choice for the radiological diagnosis of a GIST is:",
  ["CECT", "MRI", "Ultrasound", "Plain X-ray abdomen"], 0,
  "Investigations: CECT - IOC (radiological diagnosis). (Book p166)")
q(166, S13, "PET-CT in a GIST is used for:",
  ["Treatment monitoring in malignant GIST and detection of recurrence",
   "The primary radiological diagnosis", "Screening of relatives",
   "Assessment of lymphatic spread"], 0,
  "PET-CT: treatment monitoring in malignant GIST; recurrence. (Book p166)")
q(166, S13, "A GIST biopsy is reported using the:",
  ["Fletcher classification", "Lauren classification", "Bormann classification",
   "Siewert classification"], 0,
  "Biopsy: Fletcher classification - benign/intermediate/malignant. (Book p166)")
q(166, S13, "The malignancy risk of a GIST is assessed on the basis of:",
  ["Size and mitotic figures", "Site and patient's age", "Sex and site",
   "Lymph node status"], 0,
  "Malignancy risk assessed based on size and mitotic figures. (Book p166)")

# ---------------- p167 · GIST IHC & TREATMENT ----------------
S14 = "GIST: Immunohistochemistry and Treatment"
q(167, S14, "The m/c immunohistochemical marker of a GIST is:",
  ["c-KIT (CD117) - positive in >90%", "CD34", "DOG-1", "S-100"], 0,
  "IHC: m/c marker - c-KIT (CD117) (>90%). (Book p167)")
q(167, S14, "CD34 positivity is seen in what proportion of GISTs?",
  ["60-70%", "Less than 10%", "90-100%", "None"], 0,
  "IHC: CD34 (+) in 60-70%. (Book p167)")
q(167, S14, "The most specific immunohistochemical marker for a GIST is:",
  ["DOG-1", "CD34", "CD117", "Desmin"], 0,
  "IHC: most specific - DOG-1. (Book p167)")
q(167, S14, "A wild type GIST is negative for:",
  ["CD117, CD34 and PDGFRα", "DOG-1", "S-100", "Desmin"], 0,
  "Wild type GIST: negative for CD117, CD34, PDGFRα. (Book p167)")
q(167, S14, "The treatment of a benign/borderline GIST is:",
  ["Surgery - wedge resection", "Imatinib alone", "Radiotherapy", "Chemotherapy"], 0,
  "Benign/borderline GIST: surgery - wedge resection. (Book p167)")
q(167, S14, "The margin aimed for in a wedge resection of a GIST is:",
  ["1-2 cm", "5 cm", "0.5 cm", "10 cm"], 0,
  "Wedge resection with a 1-2 cm margin. (Book p167)")
q(167, S14, "A malignant/metastatic GIST is treated with:",
  ["Surgery plus imatinib (tyrosine kinase inhibitor)", "Surgery alone",
   "Radiotherapy alone", "5-FU based chemotherapy"], 0,
  "Malignant/metastatic GIST: surgery + imatinib (tyrosine kinase inhibitors). (Book p167)")
q(167, S14, "Drugs used in a GIST resistant to imatinib are:",
  ["Sunitinib and sorafenib", "Pembrolizumab and nivolumab", "Trastuzumab",
   "Rituximab"], 0,
  "Resistant to imatinib: sunitinib, sorafenib. (Book p167)")

# ---------------- p167 · GASTRIC LYMPHOMA ----------------
S15 = "Gastric Lymphoma"
q(167, S15, "A primary gastric lymphoma, compared with a generalized lymphomatous process involving the stomach, is:",
  ["Much less common", "Much more common", "Equally common", "Always the presentation"], 0,
  "Generalized lymphomatous process >> I° gastric lymphoma. (Book p167)")
q(167, S15, "The m/c type of primary gastric lymphoma is:",
  ["Non-Hodgkin's B cell lymphoma", "Hodgkin's lymphoma", "T cell lymphoma",
   "NK/T cell lymphoma"], 0,
  "I° gastric lymphoma: m/c - non-Hodgkin's B cell. (Book p167)")
q(167, S15, "The m/c subtype of primary gastric lymphoma is:",
  ["DLBCL (diffuse large B cell lymphoma)", "Follicular lymphoma", "Mantle cell lymphoma",
   "Burkitt lymphoma"], 0,
  "m/c: DLBCL (diffuse large B cell). (Book p167)")
q(167, S15, "Clinical features of gastric lymphoma include:",
  ["Upper GI haemorrhage, pain and a lump", "Only B symptoms", "Only perforation",
   "Only gastric outlet obstruction"], 0,
  "Clinical features: upper GI hemorrhage, pain, lump. (Book p167)")
q(167, S15, "B symptoms of gastric lymphoma include:",
  ["Fever, night sweats, pruritus and weight loss", "Fever alone", "Weight gain",
   "Night sweats alone"], 0,
  "B symptoms: fever, night sweat, pruritus, weight loss. (Book p167)")
q(167, S15, "The investigation used to diagnose gastric lymphoma is:",
  ["Endoscopic biopsy", "PET-CT", "Barium meal", "Diagnostic laparoscopy"], 0,
  "Investigation: endoscopic biopsy. (Book p167)")
q(167, S15, "The first line treatment of gastric lymphoma is:",
  ["Chemotherapy - R-CHOP regimen", "Surgery", "Radiotherapy", "Imatinib"], 0,
  "Management: I. chemotherapy (1st line) - R CHOP regime. (Book p167)")
q(167, S15, "Rituximab used in the R-CHOP regimen is a monoclonal antibody against:",
  ["CD20", "CD117", "CD34", "HER2"], 0,
  "Rituximab: mAB against CD20. (Book p167)")
q(167, S15, "The drugs in the R-CHOP regimen are:",
  ["Rituximab, cyclophosphamide, hydroxydaunorubicin, oncovin (vincristine) and prednisolone",
   "Rituximab, cisplatin, fluorouracil and prednisolone",
   "Rituximab, cyclophosphamide and methotrexate",
   "Rituximab, vinblastine and dacarbazine"], 0,
  "R-CHOP: rituximab, cyclophosphamide, hydroxydaunorubicin, oncovin/vincristine, prednisolone. (Book p167)")
q(167, S15, "Surgery in gastric lymphoma is indicated for:",
  ["Residual disease/recurrence", "As first line treatment", "For B symptoms",
   "For all stage I disease"], 0,
  "Surgery: residual disease/recurrence. (Book p167)")

# ---------------- p168 · MALTOMA ----------------
S16 = "MALToma (Mucosa Associated Lymphoid Tissue)"
q(168, S16, "MALToma stands for:",
  ["Mucosa associated lymphoid tissue lymphoma", "Mucosal associated lymphatic tumour",
   "Malignant lymphoid tissue tumour", "Mucosa associated lymphoid tumour"], 0,
  "MALTOMA: mucosa associated lymphoid tissue. (Book p168)")
q(168, S16, "The m/c site of a MALToma is the:",
  ["Stomach", "Salivary gland", "Thyroid", "Lung"], 0,
  "MALToma: m/c site - stomach (associated with H. pylori). (Book p168)")
q(168, S16, "Gastric MALToma is associated with infection by:",
  ["H. pylori", "EBV", "HPV", "HBV"], 0,
  "m/c site: stomach (associated with H. pylori). (Book p168)")
q(168, S16, "Low grade gastric MALToma is managed by:",
  ["H. pylori eradication", "R-CHOP chemotherapy", "Surgery", "Radiotherapy"], 0,
  "Types: low grade - management: H. pylori eradication. (Book p168)")
q(168, S16, "High grade gastric MALToma is managed with:",
  ["R-CHOP (managed as a lymphoma)", "H. pylori eradication alone", "Imatinib",
   "Surgery alone"], 0,
  "High grade: R CHOP (managed as lymphoma). (Book p168)")

# ---------------- p168 · GASTRIC VOLVULUS ----------------
S17 = "Gastric Volvulus: Types and Features"
q(168, S17, "The m/c type of gastric volvulus is:",
  ["Organoaxial", "Mesenteroaxial", "Combined", "Idiopathic"], 0,
  "Organoaxial: most common type. (Book p168)")
q(168, S17, "In an organoaxial volvulus the twist occurs:",
  ["Along the long axis - the line connecting the cardia and pylorus",
   "Along a plane perpendicular to the long axis of the stomach",
   "From the lesser to the greater curvature", "Around the gastrocolic ligament"], 0,
  "Organoaxial: twist occurs along the line connecting the cardia and pylorus, along the long axis of the stomach. (Book p168)")
q(168, S17, "Organoaxial gastric volvulus is also described as:",
  ["Longitudinal", "Vertical", "Transverse", "Horizontal"], 0,
  "Organoaxial volvulus: longitudinal. (Book p168)")
q(168, S17, "Mesenteroaxial gastric volvulus is described as:",
  ["Vertical - rotation in a plane perpendicular to the long axis, from the lesser to the greater curvature",
   "Longitudinal - along the line joining the cardia and pylorus", "Transverse",
   "Horizontal"], 0,
  "Mesenteroaxial volvulus: vertical; twist occurs along a plane perpendicular to the long axis of the stomach from lesser to greater curvature. (Book p168)")
q(168, S17, "In a mesenteroaxial volvulus:",
  ["The stomach folds upon itself - the greater curvature twists over the lesser curvature",
   "The cardia twists over the pylorus", "The antrum twists over the fundus",
   "The stomach rotates around the gastrocolic ligament"], 0,
  "Mesenteroaxial: stomach folds upon itself - greater curvature twists over lesser curvature. (Book p168)")
q(168, S17, "Vascular compromise is more common in:",
  ["Organoaxial volvulus", "Mesenteroaxial volvulus", "Both equally", "Neither type"], 0,
  "Organoaxial: vascular compromise common. (Book p168)")
q(168, S17, "Chronic symptoms are more common in:",
  ["Mesenteroaxial volvulus", "Organoaxial volvulus", "Both equally", "Neither type"], 0,
  "Mesenteroaxial: chronic symptoms common. (Book p168)")
q(168, S17, "A diaphragmatic defect (rolling hiatal hernia) is associated with:",
  ["Organoaxial volvulus", "Mesenteroaxial volvulus", "Both equally", "Neither type"], 0,
  "Organoaxial: associated with diaphragmatic defect (rolling hiatal hernia). (Book p168)")
q(168, S17, "Diaphragmatic defects are less common in:",
  ["Mesenteroaxial volvulus", "Organoaxial volvulus", "Both types", "Neither type"], 0,
  "Mesenteroaxial: diaphragmatic defects less common. (Book p168)")
q(168, S17, "Borchardt's triad of gastric volvulus consists of:",
  ["Retching, pain and inability to pass a Ryle's tube",
   "Vomiting, distension and constipation", "Pain, vomiting and fever",
   "Haematemesis, pain and a mass"], 0,
  "Borchardt's triad: retching, pain, inability to pass Ryle's tube. (Book p168)")
q(168, S17, "The investigation of choice in a stable patient with suspected gastric volvulus is:",
  ["CECT", "Contrast study", "Plain X-ray abdomen", "Upper GI endoscopy"], 0,
  "Investigations - IOC: stable patient - CECT. (Book p168)")
q(168, S17, "In an unstable patient with suspected gastric volvulus the investigation is:",
  ["Contrast study", "CECT", "MRI", "Upper GI endoscopy"], 0,
  "Investigations: unstable - contrast study. (Book p168)")
q(168, S17, "The cascade sign on a contrast study is seen in:",
  ["Gastric volvulus", "Gastric cancer", "Pyloric stenosis", "Achalasia cardia"], 0,
  "Cascade sign: seen on contrast study of volvulus. (Book p168)")

# ---------------- p169 · VOLVULUS MANAGEMENT ----------------
S18 = "Management of Gastric Volvulus"
q(169, S18, "The treatment of gastric volvulus is:",
  ["Surgery (exploratory laparotomy)", "Conservative management only",
   "Endoscopic dilatation", "Nasogastric decompression alone"], 0,
  "Management: surgery (explorative laparotomy). (Book p169)")
q(169, S18, "At laparotomy, if the stomach is viable the treatment is:",
  ["De-rotation, gastropexy and repair of the diaphragmatic defect",
   "Resection and reconstruction", "Total gastrectomy", "Pyloroplasty"], 0,
  "Stomach viable: de-rotate, gastropexy (fix the stomach), repair diaphragmatic defect. (Book p169)")
q(169, S18, "Gastropexy means:",
  ["Fixing the stomach", "Rotating the stomach", "Resecting the stomach",
   "Bypassing the stomach"], 0,
  "Gastropexy: fix the stomach. (Book p169)")
q(169, S18, "If the stomach is not viable at laparotomy the treatment is:",
  ["Resection and reconstruction", "Gastropexy alone", "De-rotation alone",
   "Total gastrectomy with esophagojejunostomy"], 0,
  "Not viable: resection & reconstruction. (Book p169)")
q(169, S18, "In gastric volvulus associated with a diaphragmatic defect, the defect should be:",
  ["Repaired", "Left alone", "Enlarged", "Covered with mesh only"], 0,
  "Surgery: repair diaphragmatic defect. (Book p169)")

# ---------------- p169 · TRICHOBEZOAR ----------------
S19 = "Trichobezoar"
q(169, S19, "A trichobezoar is:",
  ["A mass of hair (hairball) inside the stomach", "A mass of vegetable fibres",
   "A gallstone in the stomach", "A mass of undissolved medication"], 0,
  "Trichobezoar: mass of hair (hairball) inside the stomach. (Book p169)")
q(169, S19, "A trichobezoar occurs secondary to:",
  ["Trichophagy (eating hair)", "Pica for soil", "Iron deficiency", "Achalasia cardia"], 0,
  "Trichobezoar: 2° to trichophagy. (Book p169)")
q(169, S19, "A patient with a trichobezoar additionally requires:",
  ["Psychiatric referral", "Long term PPI therapy", "Iron supplementation",
   "Gastrectomy"], 0,
  "Trichobezoar: psychiatric reference required. (Book p169)")
q(169, S19, "Clinical features of a trichobezoar include:",
  ["Gastric outlet obstruction, vomiting and pain", "Haematemesis alone", "Diarrhoea",
   "Jaundice"], 0,
  "Clinical features: gastric outlet obstruction, vomiting, pain. (Book p169)")
q(169, S19, "Rapunzel syndrome refers to:",
  ["Duodenal extension of the trichobezoar", "Gastric outlet obstruction alone",
   "Multiple bezoars in the stomach", "Perforation of the stomach by a bezoar"], 0,
  "Rapunzel syndrome: duodenal extension of the trichobezoar. (Book p169)")
q(169, S19, "A small trichobezoar is removed:",
  ["Endoscopically", "By laparotomy", "By enzymatic dissolution", "By prokinetics"], 0,
  "Removal: small size - endoscopically. (Book p169)")
q(169, S19, "A large trichobezoar is removed:",
  ["Surgically", "Endoscopically", "By enzymatic dissolution", "By prokinetics"], 0,
  "Removal: large size - surgically. (Book p169)")

# ---------------- units ----------------
def sec_ids(*labels):
    return [x["id"] for x in Q if x["sec"] in labels]
def first_page(label):
    for x in Q:
        if x["sec"] == label:
            return x["page"]
    return 0

UNIT_DEFS = [
    (S1, "Gastric cancer tracks the usual suspects: smoking, alcohol, smoked and preservative-rich food (refrigeration protects), adenomatous polyps - the true ones that come with FAP and the APC gene - gastritis of both types, H. pylori, group A blood, Menetrier's hypertrophic folds and, years later, the stump of a previous gastric resection. Remember that the commonest gastric polyp is the innocent metaplastic one."),
    (S2, "Lauren splits adenocarcinoma into intestinal and diffuse. Intestinal is environmental - gastric atrophy and intestinal metaplasia, older men, glands on HPE, haematogenous spread, driven by microsatellite instability and APC mutations. Diffuse is familial, blood group A, younger women, poorly differentiated with signet ring cells, decreased E-cadherin and transmural/lymphatic spread."),
    (S3, "Early gastric cancer stops above the muscularis propria and is typed by the Japanese classification (I polypoid, IIa elevated, IIb flat, IIc depressed, III excavated) - and it carries the best prognosis. Once muscle is involved you switch to Bormann: I polypoid/fungating, II fungating or ulcerated with raised borders, III ulcerated and infiltrating, IV linitis plastica - the leather bottle stomach, most aggressive and worst of all - and V for whatever cannot be classified."),
    (S4, "The molecular classification adds four more labels: chromosomal instability travels with intestinal pathology and the best prognosis, microsatellite instability, genomically stable disease with diffuse pathology and the worst prognosis, and the Epstein-Barr virus subgroup."),
    (S5, "Clinical features are recalled with LOADS - Lump, gastric Outlet obstruction, Anaemia and anorexia, Dyspepsia that is really new onset GERD, and the Silent presentation that lets an advanced tumour hide."),
    (S6, "Know the named metastases: Sister Mary Joseph's periumbilical nodule (stomach more than ovary), Krukenberg's bilateral ovarian deposits full of signet ring cells (spread now thought to be retrograde lymphatic, not transcoelomic drop), Blummer's shelf in the pouch of Douglas felt on digital rectal examination, Virchow's left supraclavicular node via the thoracic duct, Irish's left axillary node, Trousseau's migratory thrombophlebitis (pancreas is the classic) and the skin clues - Leser-Trelat's seborrheic keratoses and tripe palms."),
    (S7, "Investigations split by question: endoscopic biopsy makes the diagnosis and shows a friable mass, endoscopic ultrasound gives T and N, and PET-CT does the overall staging. The antrum is still the commonest site worldwide, though the West is seeing more proximal tumours."),
    (S8, "TNM runs Tis in the lamina propria, T1a lamina propria, T1b submucosa, T2 muscularis propria, T3 into subserosal connective tissue but not through the visceral peritoneum, and T4 into serosa or adjacent structures. Do not forget the minimum nodal harvest - 15 for gastric and esophageal, 10 for breast, 12 for colorectal - and that the liver is where these tumours metastasise first."),
    (S9, "Surgery is one limb of multimodality treatment: aim for a 5 cm proximal margin and the pylorus distally, and call it R0 only when there is microscopic freedom from disease. Total gastrectomy is reconstructed with a circular-stapled esophagojejunostomy; Siewert III tumours get a subtotal gastrectomy (60-70% of the stomach) and distal lesions a distal gastrectomy (about 30%)."),
    (S10, "Clearance follows the numbered Japanese stations - 1 right and 2 left paracardial, 3 lesser and 4 greater curvature, 5 supra- and 6 infrapyloric, 7 left gastric, 8 common hepatic, 9 coeliac, 10 splenic hilum, 11 splenic artery, 12 hepatoduodenal, 13 retropancreatic. D1 takes stations 1-6; D2, the optimum, takes 1-11."),
    (S11, "Chemotherapy with 5-FU and cisplatin is used for node-positive, bulky node, T3/T4 and muscle-invasive disease, and as neoadjuvant treatment for bulky nodes. Radiotherapy is aimed at the stomach bed to cut loco-regional recurrence. In metastatic disease the newer tools are pembrolizumab and nivolumab, trastuzumab for HER2 neu, and oral S-1 - a fluoropyrimidine propped up by the enzyme inhibitors oteracil and gimeracil. Overall prognosis follows depth of invasion, but once a tumour is operable the nodes decide."),
    (S12, "GIST comes from the interstitial pacemaker cells of Cajal and likes the stomach. Sporadic disease is the rule; the familial forms are Carney's triad (gastric GIST, paraganglioma, pulmonary chondroma) and Carney-Stratakis syndrome, whose succinate dehydrogenase B mutation makes the tumour primarily resistant to imatinib."),
    (S13, "GIST usually announces itself with upper GI bleeding; it spreads locally and through blood to the liver, and nodes are involved in under 10%, so lymph node clearance is not mandatory. CECT is the radiological investigation of choice, PET-CT monitors treatment and picks up recurrence, and the biopsy is reported by the Fletcher classification - benign, intermediate or malignant - judged on size and mitotic figures."),
    (S14, "On immunohistochemistry c-KIT (CD117) is positive in over 90%, CD34 in 60-70%, and DOG-1 is the most specific marker; wild type tumours lack CD117, CD34 and PDGFRα. Benign and borderline tumours only need a wedge resection with a 1-2 cm margin; malignant or metastatic disease gets surgery plus imatinib, with sunitinib or sorafenib once imatinib fails."),
    (S15, "A stomach involved by lymphoma is far more often part of a generalised process than a primary gastric lymphoma. Primary disease is non-Hodgkin B-cell, usually DLBCL, and presents with bleeding, pain, a lump and B symptoms - fever, night sweats, pruritus and weight loss. Endoscopic biopsy diagnoses it, R-CHOP (rituximab against CD20, cyclophosphamide, hydroxydaunorubicin, oncovin and prednisolone) treats it, and surgery is kept for residual or recurrent disease."),
    (S16, "MALToma - mucosa associated lymphoid tissue lymphoma - usually sits in the stomach and follows H. pylori. Eradicate the organism for low grade disease; once it is high grade, treat it like any lymphoma with R-CHOP."),
    (S17, "Gastric volvulus is usually organoaxial: the stomach twists along its long axis, the line joining cardia and pylorus, it is the longitudinal pattern, it accompanies a rolling hiatal hernia and it strangles. Mesenteroaxial volvulus is vertical, the stomach folding on itself so the greater curvature swings over the lesser; it is chronic, intermittent and rarely has a diaphragmatic defect. Borchardt's triad is retching, pain and the Ryle's tube that will not go in. CECT for the stable patient, contrast study for the unstable - look for the cascade sign."),
    (S18, "Treatment is an exploratory laparotomy. If the stomach is still viable, de-rotate it, fix it with a gastropexy and repair the diaphragmatic defect; if it is not, resect and reconstruct."),
    (S19, "A trichobezoar is a hairball in the stomach from trichophagy, and these patients need a psychiatric referral as much as an operation. It obstructs the outlet, causes vomiting and pain, and when the tail runs into the duodenum it is called Rapunzel syndrome. Small ones come out endoscopically; large ones need surgery."),
]

UNITS = []
for i, (title, guide) in enumerate(UNIT_DEFS, 1):
    UNITS.append({"id": f"SURG-U24-{i}", "ch": 24, "n": i, "title": title,
                  "sec": f"{title} · p{first_page(title)}",
                  "qs": sec_ids(title), "guide": guide})

covered = [i for u in UNITS for i in u["qs"]]
assert covered == [x["id"] for x in Q], "units must cover questions in order"

data = {"questions": Q, "units": UNITS}
with open("data/ch24.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
print(f"ch24: {len(Q)} questions, {len(UNITS)} units")
