#!/usr/bin/env python3
"""Build data/ch25.json for PULSE Surgery ch25 (Upper GI Haemorrhage, book p170-178)."""
import json

Q = []
def q(page, sec, text, opts, ans, exp):
    Q.append({"id": f"SURG-C25-{len(Q)+1:03d}", "sec": sec, "page": page,
              "q": text, "opts": opts, "ans": ans, "exp": exp})

# ---------------- p170 · DEFINITION & CAUSES ----------------
S1 = "Upper GI Haemorrhage: Definition and Causes"
q(170, S1, "Upper GI haemorrhage is defined as bleeding:",
  ["Above the ligament of Treitz", "Below the ligament of Treitz",
   "Beyond the ileocaecal junction", "From the rectum"], 0,
  "Upper GI hemorrhage: bleeding above the ligament of Treitz. (Book p170)")
q(170, S1, "The proportion of upper GI haemorrhage that is non-variceal is:",
  ["80%", "20%", "50%", "10%"], 0,
  "Causes: non-variceal (80%); variceal (20%). (Book p170)")
q(170, S1, "Variceal upper GI haemorrhage is due to:",
  ["Portal hypertension", "Peptic ulcer disease", "Gastritis", "Mallory-Weiss tear"], 0,
  "Variceal (20%): portal hypertension. (Book p170)")

# ---------------- p170 · PEPTIC ULCER ----------------
S2 = "Peptic Ulcer Bleeding"
q(170, S2, "The m/c cause of upper GI haemorrhage is:",
  ["Peptic ulcer", "Gastritis", "Mallory-Weiss tear", "Oesophageal varices"], 0,
  "1. Peptic ulcer: m/c cause of upper GI hemorrhage. (Book p170)")
q(170, S2, "Among bleeding peptic ulcers:",
  ["Duodenal ulcers bleed more often than gastric ulcers",
   "Gastric ulcers bleed more often than duodenal ulcers",
   "Both bleed equally", "Only gastric ulcers bleed"], 0,
  "Peptic ulcer: duodenal > gastric. (Book p170)")
q(170, S2, "The duodenal ulcer that classically bleeds is the:",
  ["Posterior duodenal ulcer", "Anterior duodenal ulcer", "Pyloric ulcer",
   "Superior duodenal ulcer"], 0,
  "Posterior duodenal ulcer → bleeding. (Book p170)")
q(170, S2, "The vessel that most commonly bleeds in a bleeding duodenal ulcer is the:",
  ["Gastroduodenal artery", "Left gastric artery", "Splenic artery",
   "Short gastric artery"], 0,
  "Gastroduodenal artery: m/c vessel that bleeds (duodenal ulcer). (Book p170)")
q(170, S2, "The vessel that most commonly bleeds in a bleeding gastric ulcer is the:",
  ["Left gastric artery", "Gastroduodenal artery", "Right gastroepiploic artery",
   "Splenic artery"], 0,
  "Left gastric artery: m/c vessel of gastric ulcer that bleeds. (Book p170)")

# ---------------- p170 · GASTRITIS ----------------
S3 = "Gastritis: Type A, Type B and Stress Ulcers"
q(170, S3, "Type A gastritis is:",
  ["Autoimmune, with antibodies against parietal cells and intrinsic factor",
   "Bacterial (H. pylori) induced", "Due to NSAIDs", "Due to bile reflux"], 0,
  "Type A: autoimmune - antibodies against parietal cells, intrinsic factor. (Book p170)")
q(170, S3, "Type B gastritis is:",
  ["Bacterial (H. pylori) induced and affects the antrum",
   "Autoimmune and spares the antrum", "Due to stress", "Due to Crohn's disease"], 0,
  "Type B: bacterial (H. pylori) induced; affects antrum - antral gastritis. (Book p170)")
q(170, S3, "In type A gastritis:",
  ["The antrum is spared", "The antrum is predominantly affected",
   "The whole stomach is uniformly involved", "The duodenum is involved"], 0,
  "Type A: antrum is spared. (Book p170)")
q(170, S3, "Type A gastritis is associated with:",
  ["Vitiligo", "Down's syndrome", "Sarcoidosis", "Coeliac disease"], 0,
  "Type A gastritis: associated with vitiligo. (Book p170)")
q(170, S3, "The clinical features of type A gastritis include:",
  ["Pernicious anaemia and achlorhydria", "Diarrhoea and steatorrhoea",
   "Hyperchlorhydria", "Gastric outlet obstruction"], 0,
  "C/F of type A gastritis: pernicious anemia, achlorhydria. (Book p170)")
q(170, S3, "Which type of gastritis carries an increased risk of gastric cancer?",
  ["Type A", "Type B only", "Neither type", "Only stress gastritis"], 0,
  "Type A gastritis: ↑ risk of gastric cancer. (Book p170)")
q(170, S3, "Stress gastritis most commonly affects the:",
  ["Stomach mucosa, which is most sensitive to hypovolemia", "Duodenum",
   "Oesophagus", "Jejunum"], 0,
  "Stress gastritis: most sensitive to hypovolemia - stomach mucosa. (Book p170)")
q(170, S3, "Cushing's ulcer is seen in:",
  ["Head injury", "Burns", "Sepsis", "Renal failure"], 0,
  "Cushing's ulcer: seen in head injury. (Book p170)")
q(170, S3, "Curling's ulcer is seen in:",
  ["Burns", "Head injury", "Pancreatitis", "Myocardial infarction"], 0,
  "Curling ulcer: seen in burns. (Book p170)")
q(170, S3, "The m/c site of a Curling's ulcer is the:",
  ["First part of the duodenum", "Fundus of the stomach", "Oesophagus", "Jejunum"], 0,
  "Curling ulcer: m/c site - first part of duodenum. (Book p170)")
q(170, S3, "Cushing's ulcer occurs in the:",
  ["Acid producing area of the stomach", "Antrum", "Pylorus", "Oesophagus"], 0,
  "Cushing's ulcer: acid producing area of stomach. (Book p170)")
q(170, S3, "Drug induced gastritis is classically caused by:",
  ["NSAIDs", "Beta blockers", "Antibiotics", "Antacids"], 0,
  "NSAID induced gastritis is a cause of upper GI hemorrhage. (Book p170)")
q(170, S3, "In patients with AIDS, gastritis may be caused by:",
  ["Cryptosporidia", "Ascaris", "Giardia", "Taenia"], 0,
  "AIDS: cryptosporidia can cause gastritis. (Book p170)")

# ---------------- p171 · MALLORY-WEISS vs BOERHAAVE ----------------
S4 = "Mallory-Weiss Tear v/s Boerhaave Syndrome"
q(171, S4, "A Mallory-Weiss tear extends from:",
  ["The gastroesophageal junction to below the cardia", "The pylorus to the duodenum",
   "The mid oesophagus upwards", "The fundus to the antrum"], 0,
  "Mallory weiss tear - extent: GE junction to below cardia. (Book p171)")
q(171, S4, "The vessel implicated in a Mallory-Weiss tear is the:",
  ["Left gastric artery", "Gastroduodenal artery", "Splenic artery", "Aorta"], 0,
  "Vessels implicated: (L) gastric artery. (Book p171)")
q(171, S4, "The investigation for a Mallory-Weiss tear is:",
  ["Upper GI endoscopy", "Barium swallow", "CT angiography", "Laparoscopy"], 0,
  "Ix: UGI endoscopy. (Book p171)")
q(171, S4, "Mallory-Weiss tears are typically seen in:",
  ["Alcoholic patients after forceful vomiting", "Children after foreign body ingestion",
   "Postoperative patients", "Patients with scleroderma"], 0,
  "Mallory weiss: seen in alcoholic patients, after forceful vomiting. (Book p171)")
q(171, S4, "The tear in Mallory-Weiss syndrome is:",
  ["A longitudinal tear of the mucosa and submucosa", "A full thickness perforation",
   "A transverse tear of the muscle", "A circular ulcer"], 0,
  "Mallory weiss: longitudinal tear in mucosa/submucosa. (Book p171)")
q(171, S4, "Mallory-Weiss syndrome presents with:",
  ["Upper GI haemorrhage", "Chest pain and surgical emphysema", "Mackler's triad",
   "Shock without bleeding"], 0,
  "Presentation of Mallory weiss: upper GI hemorrhage. (Book p171)")
q(171, S4, "The management of a Mallory-Weiss tear is usually:",
  ["Self limiting (conservative)", "Emergency surgery", "Oesophagectomy", "Stenting"], 0,
  "Mx of Mallory weiss: self limiting. (Book p171)")
q(171, S4, "Boerhaave syndrome is:",
  ["Spontaneous oesophageal perforation", "A mucosal tear of the cardia",
   "A perforated duodenal ulcer", "Oesophageal varices"], 0,
  "Boerhaave syndrome: spontaneous esophageal perforation. (Book p171)")
q(171, S4, "The perforation in Boerhaave syndrome is:",
  ["Full thickness", "Mucosal only", "Submucosal only", "Muscularis only"], 0,
  "Boerhaave syndrome: full thickness perforation. (Book p171)")
q(171, S4, "Boerhaave syndrome presents with:",
  ["Chest pain, Mackler's triad and surgical emphysema",
   "Painless hematemesis", "Chronic dysphagia", "Jaundice"], 0,
  "Boerhaave syndrome: chest pain, Mackler's triad, surgical emphysema. (Book p171)")
q(171, S4, "The management of Boerhaave syndrome is:",
  ["Intervention (surgical)", "Self limiting - no treatment",
   "Endoscopic banding", "Proton pump inhibitors alone"], 0,
  "Mx of Boerhaave syndrome: intervention. (Book p171)")

# ---------------- p171 · GAVE / PORTAL GASTROPATHY / DIEULAFOY ----------------
S5 = "GAVE, Portal Gastropathy and Dieulafoy Lesion"
q(171, S5, "Gastric antral vascular ectasia (GAVE) consists of:",
  ["Dilated venules in the antrum", "Dilated arterioles in the fundus",
   "Varices in the oesophagus", "Angiodysplasia of the colon"], 0,
  "GAVE: dilated venules; site - antrum. (Book p171)")
q(171, S5, "GAVE is more common in:",
  ["Females > males", "Males > females", "Children", "Equal in both sexes"], 0,
  "GAVE: F > M. (Book p171)")
q(171, S5, "GAVE is associated with:",
  ["Collagen vascular diseases", "Cirrhosis of the liver", "Crohn's disease",
   "Coeliac disease"], 0,
  "GAVE: associated with collagen vascular diseases. (Book p171)")
q(171, S5, "The treatment of GAVE is:",
  ["Argon photocoagulation (APC)", "Sclerotherapy", "Banding of varices",
   "Antrectomy"], 0,
  "Mx of GAVE: argon photocoagulation (APC). (Book p171)")
q(171, S5, "The endoscopic appearance of GAVE is called:",
  ["Watermelon stomach", "Snake skin appearance", "Strawberry stomach",
   "Leather bottle stomach"], 0,
  "GAVE: watermelon stomach on endoscopy. (Book p171)")
q(171, S5, "Portal gastropathy consists of dilated vessels in the:",
  ["Body of the stomach", "Antrum", "Fundus only", "Duodenum"], 0,
  "Portal gastropathy: dilated vessels in body of stomach. (Book p171)")
q(171, S5, "The endoscopic appearance of portal gastropathy is described as:",
  ["Snake skin appearance / strawberry stomach", "Watermelon stomach",
   "Leather bottle appearance", "Cobblestone appearance"], 0,
  "Portal gastropathy: snake skin appearance/strawberry stomach. (Book p171)")
q(171, S5, "A Dieulafoy lesion is:",
  ["A dilated submucosal arteriole that bleeds", "A dilated venule in the antrum",
   "A mucosal tear at the cardia", "An angiodysplastic lesion of the colon"], 0,
  "Diewlafoy lesions: dilated submucosal arterioles → bleeding. (Book p171)")
q(171, S5, "Dieulafoy lesions are typically seen in:",
  ["Elderly patients", "Children", "Young women", "Neonates"], 0,
  "Diewlafoy lesions: seen in elderly patients. (Book p171)")
q(171, S5, "The treatment of a Dieulafoy lesion is:",
  ["Coagulation of the vessel", "Argon photocoagulation of the whole antrum",
   "Antrectomy", "Balloon tamponade"], 0,
  "Mx of Diewlafoy lesion: coagulation of vessels. (Book p171)")

# ---------------- p172 · OTHER CAUSES ----------------
S6 = "Other Causes: Angiodysplasia, Menetrier's Disease and GIST"
q(172, S6, "Angiodysplasia, a cause of lower GI haemorrhage, is most commonly located in the:",
  ["Right side of the colon", "Left side of the colon", "Rectum", "Stomach"], 0,
  "Note - lower GI hemorrhage: angiodysplasia; seen in adults; m/c in Rt. side of colon. (Book p172)")
q(172, S6, "Menetrier's disease is due to overexpression of:",
  ["TGFα", "EGF receptors", "VEGF", "Somatostatin"], 0,
  "Menetrier's disease: d/t overexpression of TGF α. (Book p172)")
q(172, S6, "Clinical features of Menetrier's disease include:",
  ["Upper GI haemorrhage and an increased risk of cancer", "Diarrhoea and steatorrhoea",
   "Gastric outlet obstruction", "Jaundice"], 0,
  "C/F: upper GI hemorrhage; ↑ risk of cancer. (Book p172)")
q(172, S6, "The medical treatment of Menetrier's disease is:",
  ["Cetuximab (anti-EGFR)", "Imatinib", "Octreotide", "Ranitidine"], 0,
  "Mx: cetuximab (anti EGFR). (Book p172)")
q(172, S6, "Menetrier's disease not responding to medical treatment is treated by:",
  ["Total gastrectomy", "Antrectomy", "Vagotomy and pyloroplasty", "Wedge resection"], 0,
  "Not responding: total gastrectomy. (Book p172)")

# ---------------- p172 · PORTAL HYPERTENSION MEASUREMENT ----------------
S7 = "Portal Hypertension: Measurement"
q(172, S7, "The portal pressure is measured by the:",
  ["Hepatic venous pressure gradient (HVPG)", "Central venous pressure",
   "Direct splenic puncture", "Arterial line"], 0,
  "Portal hypertension measured by: hepatic venous pressure gradient (HVPG). (Book p172)")
q(172, S7, "The hepatic venous pressure gradient is:",
  ["Wedged hepatic venous pressure (balloon inflated) − free pressure (balloon deflated)",
   "Wedged pressure (balloon deflated) − free pressure (balloon inflated)",
   "Portal vein pressure − hepatic artery pressure", "Splenic pulp pressure alone"], 0,
  "HVPG = wedge hepatic venous pressure (balloon inflated) − free pressure (balloon deflated). (Book p172)")
q(172, S7, "Apart from HVPG, portal hypertension can also be assessed by:",
  ["Doppler", "Plain X-ray", "MRI alone", "Liver biopsy"], 0,
  "Measured by: hepatic venous pressure gradient (HVPG); Doppler. (Book p172)")
q(172, S7, "A normal hepatic venous pressure gradient is:",
  ["1-5 mm Hg", "6-9 mm Hg", "10-12 mm Hg", "More than 12 mm Hg"], 0,
  "1-5 mm Hg: normal. (Book p172)")
q(172, S7, "An HVPG of 6-9 mm Hg indicates:",
  ["Preclinical sinusoidal portal hypertension", "Normal pressure",
   "Clinically significant portal hypertension", "Impending variceal rupture"], 0,
  "6-9 mm Hg: preclinical sinusoidal portal hypertension. (Book p172)")
q(172, S7, "The HVPG value associated with an increased risk of rupture of varices is:",
  ["≥12 mm Hg", "1-5 mm Hg", "6-9 mm Hg", "Exactly 10 mm Hg"], 0,
  "≥12 mm Hg: ↑ risk of rupture of varices. (Book p172)")

# ---------------- p172-173 · PORTO-SYSTEMIC SHUNTS ----------------
S8 = "Porto-systemic Shunts: Sites and Clinical Features"
q(172, S8, "The m/c site of a porto-systemic shunt is the:",
  ["Lower oesophagus", "Rectum", "Umbilicus", "Retroperitoneum"], 0,
  "Porto-systemic shunts - sites: lower esophagus. (Book p172)")
q(172, S8, "In the lower oesophagus, the portal circulation communicates with the systemic circulation through the:",
  ["Left gastric (coronary) vein and short gastric veins → oesophageal/paraesophageal veins",
   "Superior rectal vein → middle and inferior rectal veins",
   "Paraumbilical veins → epigastric veins", "Splenic vein → renal vein"], 0,
  "(L) gastric (coronary) vein, short gastric veins → esophageal/paraesophageal veins. (Book p172)")
q(173, S8, "Caput medusae refers to:",
  ["Outward radiation of veins from the umbilicus", "Dilated veins in the lower oesophagus",
   "Dilated rectal veins", "A splenic arteriovenous fistula"], 0,
  "Umbilicus - caput medusae: outward radiation of veins. (Book p173)")
q(173, S8, "Clinical features of portal hypertension include:",
  ["Splenomegaly and ascites", "Hepatomegaly alone", "Jaundice alone",
   "Peripheral oedema alone"], 0,
  "Clinical features: splenomegaly; ascites. (Book p173)")

# ---------------- p173 · CAUSES OF PORTAL HYPERTENSION ----------------
S9 = "Causes of Portal Hypertension"
q(173, S9, "Portal vein thrombosis is a cause of __________ portal hypertension.",
  ["Pre-hepatic", "Intra-hepatic", "Post-hepatic", "Sinusoidal"], 0,
  "Pre-hepatic causes: portal vein thrombosis. (Book p173)")
q(173, S9, "Splenic vein thrombosis causes:",
  ["Left sided (sinistral) portal hypertension", "Intra-hepatic portal hypertension",
   "Post-hepatic portal hypertension", "Budd-Chiari syndrome"], 0,
  "Pre-hepatic: splenic vein thrombosis. (Book p173)")
q(173, S9, "Cirrhosis due to alcohol, NAFLD, viral hepatitis and cryptogenic cirrhosis causes __________ portal hypertension.",
  ["Sinusoidal intra-hepatic", "Pre-sinusoidal intra-hepatic", "Post-sinusoidal intra-hepatic",
   "Pre-hepatic"], 0,
  "Intra-hepatic, sinusoidal: cirrhosis d/t various causes - alcoholic liver disease, NAFLD, viral hepatitis, cryptogenic cirrhosis. (Book p173)")
q(173, S9, "Pre-sinusoidal intra-hepatic causes of portal hypertension include:",
  ["Sarcoidosis and schistosomiasis", "Cirrhosis and amyloidosis",
   "Budd-Chiari syndrome", "Constrictive pericarditis"], 0,
  "Presinusoidal: sarcoidosis, schistosomiasis. (Book p173)")
q(173, S9, "Budd-Chiari syndrome is a __________ cause of portal hypertension.",
  ["Post-sinusoidal intra-hepatic", "Pre-hepatic", "Pre-sinusoidal intra-hepatic",
   "Post-hepatic"], 0,
  "Post sinusoidal: Budd chiari syndrome - hepatic vein outflow obstruction. (Book p173)")
q(173, S9, "Hepatic sinusoidal obstruction syndrome is also known as:",
  ["Veno-occlusive disease", "Budd-Chiari syndrome", "Banti's syndrome",
   "Cruveilhier-Baumgarten syndrome"], 0,
  "Post sinusoidal: hepatic sinusoidal obstruction (venoocclusive syndrome). (Book p173)")
q(173, S9, "Inferior vena caval obstruction is a __________ cause of portal hypertension.",
  ["Post-hepatic", "Pre-hepatic", "Intra-hepatic sinusoidal", "Pre-sinusoidal"], 0,
  "Post-hepatic: inferior vena caval obstruction. (Book p173)")
q(173, S9, "Cardiac causes of portal hypertension include all EXCEPT:",
  ["Systemic hypertension", "Restrictive cardiomyopathy", "Constrictive pericarditis",
   "Severe tricuspid regurgitation"], 0,
  "Cardiac causes: restrictive cardiomyopathy, constrictive pericarditis, severe congestive heart failure, severe tricuspid regurgitation. (Book p173)")
q(173, S9, "Schistosomiasis as a cause of portal hypertension typically presents in the:",
  ["1st-2nd decade with a gradual course", "6th decade acutely", "Neonatal period",
   "8th decade"], 0,
  "Schistosomiasis: 1st-2nd decade; gradual course - portal hypertension, variceal bleed, splenomegaly, ascites. (Book p173)")
q(173, S9, "Amyloidosis causes portal hypertension by a __________ mechanism.",
  ["Sinusoidal intra-hepatic", "Pre-hepatic", "Post-hepatic", "Pre-sinusoidal"], 0,
  "Sinusoidal: amyloidosis. (Book p173)")

# ---------------- p174 · SPLENIC VEIN THROMBOSIS & BUDD-CHIARI ----------------
S10 = "Splenic Vein Thrombosis and Budd-Chiari Syndrome"
q(174, S10, "Splenic vein thrombosis causes:",
  ["Left sided portal hypertension (sinistral portal hypertension)",
   "Right sided portal hypertension", "Budd-Chiari syndrome", "Porto-systemic encephalopathy"], 0,
  "Splenic vein thrombosis: (L) sided portal hypertension (HTN), aka sinistral portal HTN. (Book p174)")
q(174, S10, "Splenic vein thrombosis is most commonly secondary to:",
  ["Pancreatitis", "Cholecystitis", "Peptic ulcer", "Diverticulitis"], 0,
  "Splenic vein thrombosis: 2° to pancreatitis. (Book p174)")
q(174, S10, "The treatment of left sided portal hypertension due to splenic vein thrombosis is:",
  ["Splenectomy", "TIPSS", "Distal splenorenal shunt", "Liver transplantation"], 0,
  "Mx of splenic vein thrombosis: splenectomy. (Book p174)")
q(174, S10, "Budd-Chiari syndrome is:",
  ["Hepatic vein outflow obstruction", "Portal vein thrombosis",
   "Inferior vena caval obstruction", "Sinusoidal obstruction from amyloid"], 0,
  "Budd chiari syndrome: hepatic venous outflow obstruction. (Book p174)")
q(174, S10, "In Budd-Chiari syndrome, blockage of the hepatic veins leads to:",
  ["Accumulation of blood in the liver", "Shrinkage of the liver",
   "Dilatation of the bile ducts", "Calcification of the liver"], 0,
  "Blockage of hepatic veins → accumulation of blood in liver. (Book p174)")
q(174, S10, "Budd-Chiari syndrome may present with:",
  ["Gradual progression to portal hypertension and liver failure, or a fulminant course",
   "Only as an incidental finding", "Only with variceal bleeding",
   "Only with ascites"], 0,
  "Budd chiari: gradual progression - portal HTN, liver failure; or fulminant progression. (Book p174)")
q(174, S10, "A predisposing factor for Budd-Chiari syndrome is:",
  ["Pregnancy", "Old age", "Male sex", "Diabetes mellitus"], 0,
  "Predisposing factors: pregnancy. (Book p174)")
q(174, S10, "Segment I (the caudate lobe) is not affected in Budd-Chiari syndrome because:",
  ["It has independent venous drainage directly into the IVC",
   "It has a separate arterial supply", "It is supplied by the portal vein alone",
   "It regenerates faster"], 0,
  "Segment I (caudate lobe): independent venous drainage directly into IVC; not affected in Budd chiari → hypertrophy. (Book p174)")
q(174, S10, "In Budd-Chiari syndrome the caudate lobe:",
  ["Hypertrophies", "Atrophies", "Becomes calcified", "Is resected routinely"], 0,
  "Not affected in Budd chiari → hypertrophy. (Book p174)")

# ---------------- p174 · MANAGEMENT ALGORITHM ----------------
S11 = "Management Algorithm for Variceal Haemorrhage"
q(174, S11, "In a patient with upper GI haemorrhage, IV fluids should be given:",
  ["Judiciously - aiming for permissive hypotension", "Aggressively to a normal pressure",
   "Only after endoscopy", "Not at all"], 0,
  "Judicious IV fluids (permissive hypotension). (Book p174)")
q(174, S11, "In the management of upper GI haemorrhage the airway is managed in order to:",
  ["Prevent aspiration", "Give oxygen", "Allow endoscopy only", "Prevent shock"], 0,
  "Airway management: to prevent aspiration. (Book p174)")
q(174, S11, "The best intravenous agent used in variceal haemorrhage is:",
  ["Terlipressin", "Octreotide", "Propranolol", "Vitamin K"], 0,
  "IV agents: terlipressin - best. (Book p174)")
q(174, S11, "The m/c used intravenous agent in variceal haemorrhage is:",
  ["Octreotide", "Terlipressin", "Vasopressin", "Somatostatin"], 0,
  "IV agents: octreotide - m/c used. (Book p174)")
q(174, S11, "In the acute management of variceal haemorrhage, propranolol is:",
  ["Avoided", "The drug of choice", "Given intravenously", "Given after endoscopy"], 0,
  "Propranolol: avoided in the acute setting. (Book p174)")
q(174, S11, "Proton pump inhibitors in upper GI haemorrhage are:",
  ["Given after endoscopy", "Given before endoscopy", "Not useful",
   "Given only in variceal bleeding"], 0,
  "PPI: given after endoscopy. (Book p174)")
q(174, S11, "Endoscopic treatment of bleeding oesophageal varices is:",
  ["Banding or sclerotherapy", "Argon photocoagulation", "Coagulation of vessels",
   "Endoscopic mucosal resection"], 0,
  "Endoscopy: varices → banding; sclerotherapy. (Book p174)")

# ---------------- p175 · SCLEROTHERAPY & AFTERCARE ----------------
S12 = "Sclerotherapy and Post-procedure Care"
q(175, S12, "The m/c used sclerosing agent for oesophageal varices is:",
  ["Sodium tetradecyl sulfate", "Polidocanol", "Ethanolamine oleate",
   "Sodium morrhuate"], 0,
  "Sclerosing agents: sodium tetradecyl sulfate (m/c used). (Book p175)")
q(175, S12, "Other sclerosing agents used for varices include all EXCEPT:",
  ["Sodium bicarbonate", "Polidocanol", "Ethanolamine oleate", "Sodium morrhuate"], 0,
  "Sclerosing agents: sodium tetradecyl sulfate, polidocanol, ethanolamine oleate, sodium morrhuate. (Book p175)")
q(175, S12, "During sclerotherapy, deep injection should be avoided because it can cause:",
  ["Perforation and chest pain", "Portal vein thrombosis", "Encephalopathy",
   "Aspiration"], 0,
  "Avoid deep injection → perforation → chest pain. (Book p175)")
q(175, S12, "Sclerotherapy stops variceal bleeding by producing:",
  ["Fibrosis", "Thrombosis of the portal vein", "Vasoconstriction only",
   "Necrosis of the liver"], 0,
  "Mechanism of sclerotherapy: fibrosis. (Book p175)")
q(175, S12, "After banding or sclerotherapy the patient is monitored for rebleeding for:",
  ["24 hours", "6 hours", "72 hours", "1 week"], 0,
  "Post banding/sclerotherapy, once bleeding stops: monitor for 24 hours for rebleeding. (Book p175)")
q(175, S12, "After successful banding/sclerotherapy, prophylaxis is given with:",
  ["Oral propranolol", "Oral terlipressin", "Oral octreotide", "Oral PPI alone"], 0,
  "No rebleed: discharge + oral propranolol - prophylaxis. (Book p175)")
q(175, S12, "If bleeding continues or rebleeding occurs after a trial of endoscopy, the next step is:",
  ["Prepare for TIPSS", "Repeat sclerotherapy indefinitely", "Liver transplantation",
   "Splenectomy"], 0,
  "Bleeding continues/rebleeding + trial of endoscopy - fails: prepare for TIPSS. (Book p175)")
q(175, S12, "TIPSS stands for:",
  ["Trans jugular intrahepatic portosystemic shunt", "Trans ileal portosystemic shunt",
   "Trans jugular intrahepatic portal shunt", "Trans hepatic inferior portosystemic shunt"], 0,
  "TIPSS: trans jugular intrahepatic portosystemic shunt. (Book p175)")
q(175, S12, "While preparing a bleeding patient for TIPSS, the following should be corrected:",
  ["Deranged coagulation", "Hypocalcaemia", "Hypokalaemia", "Anaemia by transfusion to normal"], 0,
  "Prepare for TIPSS: correct deranged coagulation. (Book p175)")
q(175, S12, "Bleeding is stopped temporarily, while preparing for TIPSS, with:",
  ["Tubes (balloon tamponade)", "Intravenous propranolol", "Nasogastric lavage",
   "Emergency surgery"], 0,
  "Temporarily bleeding is stopped with tubes. (Book p175)")

# ---------------- p175-176 · BALLOON TUBES ----------------
S13 = "Balloon Tamponade Tubes"
q(175, S13, "The m/c used balloon tamponade tube is the:",
  ["Sengstaken-Blakemore tube", "Minnesota tube", "Linton tube", "Salem sump tube"], 0,
  "Sengstaken-Blakemore tube: m/c used. (Book p175)")
q(175, S13, "The Sengstaken-Blakemore tube has:",
  ["3 channels and 2 balloons", "4 channels and 2 balloons", "3 channels and 1 balloon",
   "2 channels and 1 balloon"], 0,
  "Sengstaken-Blakemore tube: 3 channels, 2 balloons. (Book p175)")
q(175, S13, "The channels of the Sengstaken-Blakemore tube are for:",
  ["The gastric balloon, the oesophageal balloon and gastric aspiration",
   "Two balloons and oesophageal aspiration", "Gastric and oesophageal aspiration only",
   "Two aspiration ports and a feeding port"], 0,
  "Channels: gastric balloon channel, esophageal balloon channel, aspiration from stomach. (Book p175)")
q(175, S13, "In the Sengstaken-Blakemore tube, the balloon that is inserted and inflated first is the:",
  ["Gastric balloon, inflated with 300 cc of saline", "Oesophageal balloon, inflated with 300 cc of saline",
   "Gastric balloon, inflated with 100 cc of air", "Oesophageal balloon, inflated with 50 cc of air"], 0,
  "Steps: 1. gastric balloon is inserted; 2. gastric balloon is inflated with 300 cc of saline. (Book p175)")
q(175, S13, "The tamponade effect of the Sengstaken-Blakemore tube is produced by:",
  ["Pulling up the inflated gastric balloon", "Inflating the oesophageal balloon first",
   "Traction on the oesophagus", "Inflating both balloons simultaneously"], 0,
  "Tamponade effect d/t pulling up of balloon. (Book p175)")
q(175, S13, "If bleeding does not stop after inflation of the gastric balloon, the next step is to:",
  ["Inflate the oesophageal balloon", "Remove the tube", "Give intravenous propranolol",
   "Proceed to immediate surgery"], 0,
  "If bleeding does not stop: esophageal balloon is inflated. (Book p175)")
q(175, S13, "The oesophageal balloon of the Sengstaken-Blakemore tube should be deflated:",
  ["Every 12 hours, to prevent oesophageal necrosis", "Every hour", "Every 24 hours",
   "Only when bleeding stops"], 0,
  "Deflated every 12 hrs to prevent esophageal necrosis. (Book p175)")
q(176, S13, "The Minnesota balloon tube has:",
  ["4 channels and 2 balloons", "3 channels and 2 balloons", "4 channels and 1 balloon",
   "3 channels and 1 balloon"], 0,
  "Minnesota balloon: 2 balloon channels & 2 aspiration channels - 4 channels. (Book p176)")
q(176, S13, "The Minnesota tube has 4 channels for:",
  ["Two balloons, oesophageal aspiration and gastric aspiration",
   "One balloon and three aspirations", "Three balloons and one aspiration",
   "Two aspirations and two feeds"], 0,
  "Minnesota balloon: 4 channels - 2 balloon channels & aspiration channels (esophageal and gastric aspiration). (Book p176)")
q(176, S13, "The Linton tube has:",
  ["1 balloon and 3 channels", "2 balloons and 4 channels", "2 balloons and 3 channels",
   "1 balloon and 2 channels"], 0,
  "Linton tube: 1 balloon, 3 channels. (Book p176)")
q(176, S13, "The channels of the Linton tube are for:",
  ["Oesophageal aspiration, gastric aspiration and the balloon",
   "Two balloons and gastric aspiration", "Gastric aspiration and feeding",
   "Oesophageal aspiration and two balloons"], 0,
  "Linton tube: 3 channels - esophageal aspiration, gastric aspiration, balloon channel. (Book p176)")

# ---------------- p176 · TIPSS ----------------
S14 = "TIPSS (Transjugular Intrahepatic Portosystemic Shunt)"
q(176, S14, "The m/c used shunt for portal hypertension is:",
  ["TIPSS", "Warren shunt", "Linton shunt", "Eck fistula"], 0,
  "TIPSS: m/c used shunt. (Book p176)")
q(176, S14, "TIPSS is a __________ shunt.",
  ["Non-selective (non-specific)", "Selective", "Splenic only", "Mesocaval"], 0,
  "TIPSS: non-specific (non-selective) shunt. (Book p176)")
q(176, S14, "Shunts used for portal hypertension act by:",
  ["Lowering the portal pressure", "Increasing the portal flow",
   "Increasing the hepatic arterial flow", "Reducing the splenic size"], 0,
  "Shunts: ↓ portal pressure. (Book p176)")
q(176, S14, "An early complication of TIPSS is:",
  ["Rupture of the liver capsule", "Renal failure", "Splenic infarction",
   "Bowel perforation"], 0,
  "Complications - early: rupture of liver capsule. (Book p176)")
q(176, S14, "Encephalopathy after a shunt occurs because:",
  ["Toxin laden gut blood bypasses the liver and enters the systemic circulation",
   "The shunt blocks the hepatic artery", "The shunt causes hypoglycaemia",
   "The shunt raises the portal pressure"], 0,
  "Gut blood: toxin + non-selective shunt → systemic circulation, liver detoxification bypassed → encephalopathy. (Book p176)")
q(176, S14, "Indications for TIPSS include:",
  ["Variceal bleeding and intractable ascites related to portal hypertension",
   "Uncomplicated cirrhosis", "Hepatocellular carcinoma", "Splenic vein thrombosis"], 0,
  "Indications: variceal bleeding; intractable ascites related to portal HTN. (Book p176)")

# ---------------- p177 · TYPES OF SHUNTS & SUGIURA ----------------
S15 = "Types of Shunts and the Sugiura Procedure"
q(177, S15, "A non-selective shunt shunts:",
  ["Both gut and splenic blood", "Only splenic blood", "Only mesenteric blood",
   "Only portal blood"], 0,
  "Non-selective: shunting of gut & splenic blood. (Book p177)")
q(177, S15, "A selective shunt shunts __________ and therefore carries a low risk of encephalopathy.",
  ["Only splenic blood", "Both gut and splenic blood", "Only mesenteric blood",
   "Only portal blood"], 0,
  "Selective: shunting of splenic blood (only) - low risk of encephalopathy. (Book p177)")
q(177, S15, "The Linton shunt is a:",
  ["Proximal lienorenal shunt", "Distal lienorenal shunt", "Portocaval shunt",
   "Mesocaval shunt"], 0,
  "Linton shunt: proximal lienorenal shunt. (Book p177)")
q(177, S15, "An end to side portocaval shunt is also called the:",
  ["Eck fistula", "Warren shunt", "Inokuchi shunt", "Linton shunt"], 0,
  "End to side portocaval shunt (ECK fistula). (Book p177)")
q(177, S15, "The Inokuchi shunt is a:",
  ["Left gastric venocaval shunt", "Distal lienorenal shunt", "Proximal lienorenal shunt",
   "Mesocaval shunt"], 0,
  "Inokuchi: (L) gastric venocaval shunt. (Book p177)")
q(177, S15, "The Warren shunt is a:",
  ["Distal lienorenal (splenorenal) shunt", "Proximal lienorenal shunt",
   "Portocaval shunt", "Left gastric venocaval shunt"], 0,
  "Warren shunt: distal lienorenal shunt. (Book p177)")
q(177, S15, "The Sugiura procedure is:",
  ["An oesophageal devascularization procedure", "A portocaval shunt",
   "A splenorenal shunt", "An oesophageal resection"], 0,
  "Sugiura procedure: esophageal devascularization procedure. (Book p177)")
q(177, S15, "In the Sugiura procedure, the length of oesophagus devascularised is:",
  ["5-10 cm of the lower oesophagus", "1-2 cm", "The whole thoracic oesophagus",
   "20 cm"], 0,
  "Lower esophagus (5-10 cm) is devascularised. (Book p177)")
q(177, S15, "The Sugiura procedure additionally includes:",
  ["Oesophageal transection, selective vagotomy, pyloroplasty and splenectomy",
   "Total gastrectomy and splenectomy", "Liver transplantation", "TIPSS"], 0,
  "Sugiura procedure: esophageal transection, selective vagotomy, pyloroplasty, splenectomy. (Book p177)")
q(177, S15, "The Sugiura procedure is:",
  ["A rare procedure", "The commonest shunt", "Done for ascites", "Done for peptic ulcer"], 0,
  "Sugiura procedure: rare procedure. (Book p177)")

# ---------------- p178 · CHILD PUGH ----------------
S16 = "Child-Pugh Score"
q(178, S16, "In the Child-Pugh score, encephalopathy is graded as:",
  ["None, mild to moderate (grade 1 or 2), severe (grade 3 or 4)",
   "None, mild, severe", "Grade 1, 2, 3 only", "Present or absent"], 0,
  "Encephalopathy: none; mild to moderate (grade 1 or 2); severe (grade 3 or 4). (Book p178)")
q(178, S16, "In the Child-Pugh score, ascites is graded as:",
  ["None, mild to moderate (diuretic responsive), severe (diuretic refractory)",
   "Mild, moderate, severe", "Absent or present", "By the volume of ascitic fluid"], 0,
  "Ascites: none; mild to moderate (diuretic responsive); severe (diuretic refractory). (Book p178)")
q(178, S16, "In the Child-Pugh score, the bilirubin cut-offs (mg/dL) are:",
  ["<2, 2-3, >3", "<1, 1-2, >2", "<2.8, 2.8-3.5, >3.5", "<5, 5-10, >10"], 0,
  "Bilirubin: <2, 2-3, >3 mg/dL. (Book p178)")
q(178, S16, "In the Child-Pugh score, the albumin cut-offs (g/dL) are:",
  [">3.5, 2.8-3.5, <2.8", ">4, 3-4, <3", ">3, 2-3, <2", ">5, 3-5, <3"], 0,
  "Albumin: >3.5, 2.8-3.5, <2.8 g/dL. (Book p178)")
q(178, S16, "In the Child-Pugh score, the prolongation of prothrombin time in seconds is scored as:",
  ["<4, 4-6, >6", "<1, 1-3, >3", "<10, 10-15, >15", "<2, 2-4, >4"], 0,
  "Prothrombin time: <4, 4-6, >6 seconds. (Book p178)")
q(178, S16, "In the Child-Pugh score, the INR cut-offs are:",
  ["<1.7, 1.7-2.3, >2.3", "<1, 1-2, >2", "<1.5, 1.5-2.5, >2.5", "<2, 2-3, >3"], 0,
  "INR: <1.7, 1.7-2.3, >2.3. (Book p178)")
q(178, S16, "Child-Pugh class A corresponds to a score of:",
  ["5-6 with mild liver dysfunction", "7-9 with moderate dysfunction",
   "10-15 with severe dysfunction", "More than 15"], 0,
  "Class A: score 5-6 - mild liver dysfunction. (Book p178)")
q(178, S16, "Child-Pugh class B corresponds to a score of:",
  ["7-9 with moderate liver dysfunction", "5-6 with mild dysfunction",
   "10-15 with severe dysfunction", "1-4"], 0,
  "Class B: score 7-9 - moderate liver dysfunction. (Book p178)")
q(178, S16, "Child-Pugh class C corresponds to a score of:",
  ["10-15 with severe liver dysfunction", "7-9 with moderate dysfunction",
   "5-6 with mild dysfunction", "More than 15"], 0,
  "Class C: score 10-15 - severe liver dysfunction. (Book p178)")

# ---------------- p178 · PROGNOSTIC SCORES & FORREST ----------------
S17 = "Prognostic Scores and Forrest Classification"
q(178, S17, "The Bleed criteria score denotes:",
  ["The outcome", "The risk of rebleeding", "The need for surgery", "The portal pressure"], 0,
  "Prognostic scores: bleed criteria - denotes outcome. (Book p178)")
q(178, S17, "Forrest's endoscopic classification denotes:",
  ["The risk of rebleeding", "The outcome", "The portal pressure", "The liver reserve"], 0,
  "Forrest's endoscopic classification: denotes risk of rebleeding. (Book p178)")
q(178, S17, "In Forrest's classification, class Ia is:",
  ["Spurting bleeding", "Oozing bleeding", "A non-bleeding visible vessel",
   "An adherent clot"], 0,
  "Class Ia: spurting. (Book p178)")
q(178, S17, "In Forrest's classification, class Ib is:",
  ["Oozing bleeding", "Spurting bleeding", "A clean ulcer base",
   "A flat pigmented spot"], 0,
  "Class Ib: oozing. (Book p178)")
q(178, S17, "In Forrest's classification, class IIa is:",
  ["A non-bleeding visible vessel", "An adherent clot", "A flat pigmented spot",
   "A clean ulcer base"], 0,
  "Class IIa: non-bleeding visible vessel. (Book p178)")
q(178, S17, "In Forrest's classification, class IIb is:",
  ["An adherent clot", "A non-bleeding visible vessel", "A flat pigmented spot",
   "Spurting bleeding"], 0,
  "Class IIb: adherent clot. (Book p178)")
q(178, S17, "In Forrest's classification, class IIc is:",
  ["A flat pigmented spot", "A clean ulcer base", "Spurting bleeding", "An adherent clot"], 0,
  "Class IIc: flat pigmented spot. (Book p178)")
q(178, S17, "In Forrest's classification, class III is:",
  ["A clean ulcer base", "A flat pigmented spot", "An adherent clot", "Oozing"], 0,
  "Class III: clean ulcer base. (Book p178)")
q(178, S17, "The Forrest classes carrying a high risk of rebleeding are:",
  ["Ia and Ib", "IIa and IIb", "IIc and III", "III only"], 0,
  "Risk: high - Ia (spurting), Ib (oozing). (Book p178)")
q(178, S17, "The Forrest classes carrying an intermediate risk of rebleeding are:",
  ["IIa and IIb", "Ia and Ib", "IIc and III", "III only"], 0,
  "Risk: intermediate - IIa (non-bleeding visible vessel), IIb (adherent clot). (Book p178)")
q(178, S17, "The Forrest classes carrying a low risk of rebleeding are:",
  ["IIc and III", "Ia and Ib", "IIa and IIb", "Ib and IIa"], 0,
  "Risk: low - IIc (flat pigmented spot), III (clean ulcer base). (Book p178)")
q(178, S17, "Other prognostic scores used in upper GI haemorrhage include all EXCEPT:",
  ["Child-Pugh score", "Rockall scoring system", "Glasgow Blatchford score", "AIMS65"], 0,
  "Prognostic scores: Rockall scoring system, Glasgow Blatchford, AIMS65. (Book p178)")

# ---------------- units ----------------
def sec_ids(*labels):
    return [x["id"] for x in Q if x["sec"] in labels]
def first_page(label):
    for x in Q:
        if x["sec"] == label:
            return x["page"]
    return 0

UNIT_DEFS = [
    (S1, "Upper GI haemorrhage means bleeding above the ligament of Treitz, and four out of five patients are bleeding from something other than varices. The variceal fifth is the portal hypertension group - and it is the one that kills."),
    (S2, "Peptic ulcer is the single commonest cause, duodenal more than gastric. Think anatomy when it bleeds: a posterior duodenal ulcer eats into the gastroduodenal artery, while a bleeding gastric ulcer is usually the left gastric artery."),
    (S3, "Type A gastritis is autoimmune - antibodies against parietal cells and intrinsic factor, vitiligo as a companion, the antrum spared, pernicious anaemia with achlorhydria, and a higher risk of cancer. Type B is H. pylori in the antrum. Stress gastritis hits the stomach mucosa, which is the tissue most sensitive to hypovolemia, and shows up as Cushing's ulcer after head injury in the acid-producing area or Curling's ulcer after burns in the first part of the duodenum."),
    (S4, "Both follow forceful vomiting in an alcoholic, but Mallory-Weiss is a longitudinal mucosal tear from the gastroesophageal junction down below the cardia that bleeds from the left gastric artery and usually settles by itself, whereas Boerhaave is a full thickness spontaneous perforation with chest pain, Mackler's triad and surgical emphysema that needs intervention."),
    (S5, "Three vascular lesions to separate: GAVE - dilated venules in the antrum, female preponderance, collagen vascular disease, watermelon stomach, treated with argon photocoagulation; portal gastropathy - dilated vessels in the body with the snake skin or strawberry appearance; and the Dieulafoy lesion, a dilated submucosal arteriole in an elderly patient that is treated by coagulating the vessel."),
    (S6, "Two odds and ends close the non-variceal list: angiodysplasia, which belongs to lower GI bleeding and sits on the right side of the colon, and Menetrier's disease, driven by TGFα overexpression, which bleeds, predisposes to cancer, is treated with the anti-EGFR antibody cetuximab and needs a total gastrectomy if that fails."),
    (S7, "Portal pressure is measured as the hepatic venous pressure gradient - wedged pressure with the balloon inflated minus the free pressure with it deflated - and can also be followed with Doppler. One to five is normal, six to nine is preclinical sinusoidal disease, and once you reach twelve the varices are at real risk of rupture."),
    (S8, "Blood escapes through porto-systemic shunts, most importantly at the lower oesophagus where the left gastric and short gastric veins meet the oesophageal and paraesophageal veins. It also opens up at the rectum and at the umbilicus, where the radiating veins are called caput medusae. Splenomegaly and ascites are the clinical company these shunts keep."),
    (S9, "Classify the causes by where the block sits: pre-hepatic (portal or splenic vein thrombosis), intra-hepatic pre-sinusoidal (sarcoidosis, schistosomiasis), sinusoidal (every kind of cirrhosis, amyloidosis, hepatocellular carcinoma), post-sinusoidal (Budd-Chiari, veno-occlusive disease) and post-hepatic (IVC obstruction and the cardiac causes - restrictive cardiomyopathy, constrictive pericarditis, severe failure and severe tricuspid regurgitation)."),
    (S10, "Splenic vein thrombosis, usually after pancreatitis, gives left sided or sinistral portal hypertension and is cured by splenectomy. Budd-Chiari blocks hepatic venous outflow so blood accumulates in the liver, running a gradual course into portal hypertension and liver failure or a fulminant one; pregnancy predisposes. The caudate lobe drains straight into the IVC, so it is spared - and hypertrophies."),
    (S11, "Resuscitate first but not too much: cross match, secure the airway to prevent aspiration, and run the patient at a permissive hypotension. Terlipressin is the best drug and octreotide the most used, propranolol is avoided acutely and the PPI comes after endoscopy. Endoscopy then deals with the varices by banding or sclerotherapy."),
    (S12, "Sclerotherapy is usually done with sodium tetradecyl sulfate; polidocanol, ethanolamine oleate and sodium morrhuate are alternatives. Inject superficially - a deep injection perforates and causes chest pain - and the aim is fibrosis. Watch the patient for 24 hours; if there is no rebleed, discharge on oral propranolol. If bleeding continues despite a further endoscopic attempt, correct the coagulation and move on to TIPSS."),
    (S13, "Balloon tamponade buys time. The Sengstaken-Blakemore tube, the one you will use, has three channels and two balloons: pass it, inflate the gastric balloon with 300 cc of saline, pull it up for tamponade, and only inflate the oesophageal balloon if bleeding continues - deflating it every 12 hours to avoid oesophageal necrosis. The Minnesota tube has four channels (two balloons, two aspirations) and the Linton tube a single balloon with three channels."),
    (S14, "TIPSS is the most used shunt and a non-selective one: it lowers portal pressure but lets toxic gut blood bypass the liver, so encephalopathy is the price, and the liver capsule can rupture early on. It is indicated for variceal bleeding and for ascites that will not respond despite portal hypertension."),
    (S15, "Non-selective shunts divert both gut and splenic blood - TIPSS, the Linton proximal lienorenal shunt and the end-to-side portocaval Eck fistula. Selective shunts take only splenic blood, so encephalopathy is less likely: Inokuchi's left gastric venocaval shunt and Warren's distal lienorenal shunt. The Sugiura procedure is a rare alternative that devascularises the lower 5-10 cm of oesophagus, combined with oesophageal transection, selective vagotomy, pyloroplasty and splenectomy."),
    (S16, "Child-Pugh grades five things in threes - encephalopathy none to grade 3-4, ascites none to diuretic refractory, bilirubin under 2 to over 3, albumin above 3.5 to below 2.8, and prothrombin prolongation under 4 to over 6 seconds or an INR from under 1.7 to over 2.3. Add the points: 5-6 is class A and mild, 7-9 is class B and moderate, 10-15 is class C and severe."),
    (S17, "Bleed criteria tell you the outcome, while Forrest's endoscopic classification tells you the risk of rebleeding: spurting (Ia) and oozing (Ib) are high risk, a non-bleeding visible vessel (IIa) and an adherent clot (IIb) are intermediate, and a flat pigmented spot (IIc) or clean ulcer base (III) are low. Rockall, Glasgow Blatchford and AIMS65 are the named prognostic scores."),
]

UNITS = []
for i, (title, guide) in enumerate(UNIT_DEFS, 1):
    UNITS.append({"id": f"SURG-U25-{i}", "ch": 25, "n": i, "title": title,
                  "sec": f"{title} · p{first_page(title)}",
                  "qs": sec_ids(title), "guide": guide})

covered = [i for u in UNITS for i in u["qs"]]
assert covered == [x["id"] for x in Q], "units must cover questions in order"

data = {"questions": Q, "units": UNITS}
with open("data/ch25.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
print(f"ch25: {len(Q)} questions, {len(UNITS)} units")
