#!/usr/bin/env python3
"""Build data/ch19.json for PULSE Surgery ch19 (Esophagus : Part 1, book p126-134)."""
import json

Q = []
def q(page, sec, text, opts, ans, exp):
    Q.append({"id": f"SURG-C19-{len(Q)+1:03d}", "sec": sec, "page": page,
              "q": text, "opts": opts, "ans": ans, "exp": exp})

# ---------------- p126 · SURGICAL ANATOMY: CONSTRICTIONS ----------------
S1 = "Surgical Anatomy: Constrictions & Diaphragmatic Openings"
q(126, S1, "The first constriction of the esophagus is at the level of:",
  ["C6 - pharyngoesophageal junction", "T4 - arch of aorta", "T10 - diaphragm", "T8 - IVC opening"], 0,
  "1st constriction: C6 (pharyngoesophageal junction). (Book p126)")
q(126, S1, "The narrowest portion of the whole gastrointestinal tract is:",
  ["Cricopharyngeal/pharyngoesophageal junction (4 mm)", "Pylorus", "Ileocaecal valve",
   "Anal canal"], 0,
  "C6 junction: narrowest portion of the GIT (4 mm diameter). (Book p126)")
q(126, S1, "Foreign body impaction in the esophagus is m/c at the:",
  ["C6 constriction", "Aortic constriction", "Diaphragmatic constriction", "Cardia"], 0,
  "C6 constriction: site of foreign body impaction. (Book p126)")
q(126, S1, "The m/c site of iatrogenic esophageal perforation is:",
  ["C6 constriction", "Mid esophagus", "Lower esophagus", "Stomach"], 0,
  "C6 constriction: m/c site of iatrogenic esophageal perforation. (Book p126)")
q(126, S1, "The second constriction of the esophagus is caused by:",
  ["Arch of aorta and left main stem bronchus", "Left atrium only", "Azygos vein", "Thoracic duct"], 0,
  "2nd constriction: arch of aorta + left main stem bronchus (T4). (Book p126)")
q(126, S1, "The third constriction of the esophagus is at the:",
  ["Diaphragm (T10)", "Cricoid cartilage", "Carina", "Gastroesophageal junction"], 0,
  "3rd constriction: diaphragm (T10). (Book p126)")
q(126, S1, "The diaphragmatic opening at T8 transmits the:",
  ["IVC and phrenic nerve", "Esophagus and vagus", "Aorta and thoracic duct", "Azygos vein"], 0,
  "T8: IVC and phrenic nerve. (Book p126)")
q(126, S1, "Structures passing through the esophageal hiatus at T10 are:",
  ["Esophagus, vagus and left gastric artery", "Aorta and thoracic duct",
   "IVC and phrenic nerve", "Sympathetic chain"], 0,
  "T10: esophagus, vagus, left gastric artery. (Book p126)")
q(126, S1, "The aortic opening of the diaphragm at T12 transmits:",
  ["Aorta and thoracic duct", "Esophagus and vagus", "IVC", "Azygos vein"], 0,
  "T12: aorta + thoracic duct. (Book p126)")

# ---------------- p126 · BLOOD SUPPLY, LYMPHATICS & LAYERS ----------------
S2 = "Blood Supply, Lymphatics & Layers"
q(126, S2, "The arterial supply of the esophagus is:",
  ["Segmental in nature", "From a single axial vessel", "From the coeliac trunk alone",
   "From the internal thoracic artery alone"], 0,
  "Blood supply of the esophagus: segmental in nature. (Book p126)")
q(126, S2, "The upper one third of the esophagus is supplied by the:",
  ["Inferior thyroid artery", "Left gastric artery", "Bronchial artery", "Splenic artery"], 0,
  "Upper 1/3rd: inferior thyroid artery. (Book p126)")
q(126, S2, "The middle one third of the esophagus is supplied by:",
  ["Descending thoracic aorta and bronchial arteries", "Inferior thyroid artery",
   "Left gastric artery", "Coeliac axis"], 0,
  "Middle 1/3rd: descending thoracic aorta and bronchial artery. (Book p126)")
q(126, S2, "The lower one third of the esophagus is supplied by the:",
  ["Left gastric artery", "Inferior thyroid artery", "Superior mesenteric artery", "Splenic artery"], 0,
  "Lower 1/3rd: left gastric artery. (Book p126)")
q(126, S2, "The artery involved in a Mallory Weiss tear is the:",
  ["Left gastric artery", "Inferior thyroid artery", "Bronchial artery", "Splenic artery"], 0,
  "Left gastric artery is involved in Mallory Weiss tear. (Book p126)")
q(126, S2, "The venous drainage of the lower esophagus:",
  ["Joins the portal circulation and is the site of porto-systemic varices",
   "Drains entirely into the azygos system",
   "Drains into the internal jugular vein",
   "Drains into the inferior vena cava directly"], 0,
  "Lower 1/3rd: left gastric vein joins the portal circulation - site of porto-systemic varices. (Book p126)")
q(126, S2, "Lymphatic spread in esophageal cancer is characterised by:",
  ["Longitudinal spread with skip metastasis", "Only transverse spread",
   "Spread confined to the mucosa", "No lymphatic spread"], 0,
  "Lymphatics: longitudinal spread, skip metastasis. (Book p126)")
q(126, S2, "The layer absent in the esophagus is the:",
  ["Serosa", "Mucosa", "Submucosa", "Muscularis propria"], 0,
  "Esophagus lacks serosa. (Book p126)")
q(126, S2, "The strongest layer of the esophagus is the:",
  ["Submucosa", "Mucosa", "Muscularis", "Adventitia"], 0,
  "Strongest layer: submucosa. (Book p126)")
q(126, S2, "A long proximal margin is taken during esophagectomy in order to:",
  ["Prevent recurrence", "Avoid anastomotic leak", "Reduce blood loss", "Preserve the vagus"], 0,
  "Esophagectomy: long proximal margin to prevent recurrence. (Book p126)")

# ---------------- p127 · SPHINCTERS & PERISTALSIS ----------------
S3 = "Esophageal Sphincters & Peristalsis"
q(127, S3, "The lower esophageal sphincter is:",
  ["Only a physiological entity", "Both an anatomical narrowing and a physiological entity",
   "A well developed anatomical ring", "A fibrous band"], 0,
  "LES: only a physiological entity (unlike the UES). (Book p127)")
q(127, S3, "The upper esophageal sphincter is:",
  ["Both an anatomical narrowing and a physiological high pressure entity",
   "Only a physiological entity", "Only a mucosal fold", "A true anatomical valve"], 0,
  "UES: both anatomical (narrowing) and physiological (high pressure) entity. (Book p127)")
q(127, S3, "The length of the LES and its abdominal component are:",
  ["3-5 cm total, with 2-4 cm lying in the abdomen", "1-2 cm total, entirely in the abdomen",
   "10 cm total, entirely thoracic", "8-10 cm, with no abdominal part"], 0,
  "Length: 3-5 cm (abdominal length 2-4 cm). (Book p127)")
q(127, S3, "The two parts of the inferior constrictor forming the UES are the thyropharyngeus and:",
  ["Cricopharyngeus", "Stylopharyngeus", "Palatopharyngeus", "Salpingopharyngeus"], 0,
  "Parts of inferior constrictor: thyropharyngeus (oblique fibres) and cricopharyngeus (horizontal fibres). (Book p127)")
q(127, S3, "The horizontal fibres of the inferior constrictor belong to the:",
  ["Cricopharyngeus", "Thyropharyngeus", "Stylopharyngeus", "Palatopharyngeus"], 0,
  "Cricopharyngeus - horizontal fibres. (Book p127)")
q(127, S3, "Killian's dehiscence is the site of:",
  ["Zenker's diverticulum", "Esophageal atresia", "Boerhaave's perforation", "Schatzki's ring"], 0,
  "Killian's dehiscence: site for Zenker's diverticulum. (Book p127)")
q(127, S3, "Frequent relaxation of the LES results in:",
  ["GERD", "Achalasia cardia", "Zenker's diverticulum", "Esophageal web"], 0,
  "Frequent relaxation of the LES - GERD. (Book p127)")
q(127, S3, "Failure of the LES to relax causes:",
  ["Achalasia cardia", "GERD", "Diffuse esophageal spasm", "Nutcracker esophagus"], 0,
  "LES does not relax - achalasia cardia. (Book p127)")
q(127, S3, "Primary peristalsis of the esophagus is a:",
  ["Propulsive wave that pushes food down", "Non-propulsive wave between meals",
   "Wave generated only after a swallow fails", "Retrograde wave"], 0,
  "Primary peristalsis: propulsive wave which pushes food down. (Book p127)")
q(127, S3, "If primary peristalsis fails, food is pushed down by:",
  ["Secondary peristalsis", "Tertiary peristalsis", "Retrograde peristalsis", "Segmentation"], 0,
  "If primary peristalsis fails, the secondary wave pushes food down (propulsive). (Book p127)")
q(127, S3, "Tertiary peristalsis of the esophagus is:",
  ["Non-propulsive, occurs between meals and increases in frequency with age",
   "The main propulsive wave after swallowing",
   "A wave seen only in achalasia",
   "A retrograde wave causing vomiting"], 0,
  "Tertiary peristalsis: non-propulsive wave in between meals, frequency increases with age. (Book p127)")

# ---------------- p127 · FOREIGN BODY ----------------
S4 = "Foreign Body in the Esophagus"
q(127, S4, "Esophageal foreign bodies are m/c seen in:",
  ["Children", "Young adults", "Pregnant women", "The elderly"], 0,
  "Foreign body: m/c in children. (Book p127)")
q(127, S4, "A coin lodged in the esophagus appears in which orientation on an AP view of the neck/chest?",
  ["Side face on", "End face on", "Oblique only", "Invisible"], 0,
  "Coin in esophagus: side face on in AP view, end face on in lateral view. (Book p127)")
q(127, S4, "A coin in the trachea appears in which orientation on an AP view?",
  ["End face on", "Side face on", "Oblique", "Not visible"], 0,
  "Coin in trachea: end face on in AP view, side face on in lateral. (Book p127)")
q(127, S4, "The presenting feature of an esophageal foreign body is:",
  ["Dysphagia", "Stridor", "Hemoptysis", "Hoarseness"], 0,
  "Esophageal foreign body: C/F is dysphagia. (Book p127)")
q(127, S4, "A foreign body in the respiratory tract presents with:",
  ["Choking and stridor", "Dysphagia alone", "Hematemesis", "Silent abdomen"], 0,
  "Respiratory tract foreign body: choking; O/E stridor. (Book p127)")
q(127, S4, "The investigation for a suspected esophageal foreign body is:",
  ["X-ray", "CT scan", "Barium swallow", "MRI"], 0,
  "Ix for foreign body: X-ray. (Book p127)")
q(127, S4, "An esophageal foreign body impacted at C6 in a symptomatic patient is treated by:",
  ["Endoscopic removal", "Observation", "Laparotomy", "Barium follow-through"], 0,
  "Impacted at C6 and symptomatic: endoscopic removal. (Book p127)")
q(127, S4, "A foreign body that has traversed beyond C6 in an asymptomatic child is managed by:",
  ["Observation", "Immediate endoscopy", "Emergency surgery", "Barium meal"], 0,
  "Traversed beyond C6 and asymptomatic: observation. (Book p127)")
q(127, S4, "Button batteries in the esophagus are managed by:",
  ["Endoscopic removal irrespective of site", "Observation for 48 hours",
   "Oral proton pump inhibitors alone", "Barium swallow and discharge"], 0,
  "Button batteries: endoscopic removal irrespective of site - they corrode and perforate. (Book p127)")

# ---------------- p128 · CORROSIVE INJURY ----------------
S5 = "Corrosive Injury of the Esophagus"
q(128, S5, "Alkali ingestion damages the esophagus by:",
  ["Saponification - penetrating deeper and causing more damage",
   "Coagulation of proteins limiting depth", "Immediate pyloric relaxation",
   "Neutralisation by gastric acid"], 0,
  "Alkali: due to saponification - penetrates deeper, more damage. (Book p128)")
q(128, S5, "Acid ingestion causes injury by:",
  ["Coagulation of proteins and does not penetrate deep",
   "Saponification with deep penetration", "Liquefaction necrosis of muscle",
   "Fat necrosis"], 0,
  "Acid: coagulation of proteins - do not penetrate deep. (Book p128)")
q(128, S5, "More gastric damage after acid ingestion is due to:",
  ["Pylorospasm holding the acid in the stomach", "Rapid gastric emptying",
   "Alkaline gastric secretions", "Increased gastric motility"], 0,
  "Acid: pylorospasm in the stomach - more gastric damage. (Book p128)")
q(128, S5, "In corrosive injury of the esophagus, blind insertion of a NG tube:",
  ["Should be avoided as it can cause perforation", "Is mandatory in all patients",
   "Is the definitive treatment", "Is used to neutralise the alkali"], 0,
  "Avoid blind insertion of NG tube: can cause perforation. (Book p128)")
q(128, S5, "Regarding antibiotics in corrosive esophageal injury:",
  ["No role of prophylactic antibiotics", "Prophylactic antibiotics are mandatory",
   "Antibiotics are given for 6 weeks", "Only antifungals are used"], 0,
  "No use of prophylactic antibiotics in corrosive injury. (Book p128)")
q(128, S5, "The most important investigation in acute corrosive esophageal injury is:",
  ["Early skilled endoscopy within 48 hours", "Barium swallow after 1 week",
   "CT chest", "Manometry"], 0,
  "Early skilled endoscopy within 48 hrs is most important. (Book p128)")
q(128, S5, "The role of steroids in corrosive esophageal injury is:",
  ["No role", "Definitive treatment", "Prevents all strictures", "Given for 6 months"], 0,
  "No role of steroids in corrosive injury. (Book p128)")
q(128, S5, "Definitive management of a corrosive esophageal stricture is:",
  ["Dilatation or esophagectomy", "Long term steroids", "Radiotherapy", "Observation only"], 0,
  "Stricture management: dilatation or esophagectomy. (Book p128)")
q(128, S5, "Perforation following corrosive injury is managed by:",
  ["Emergency surgery", "Oral steroids", "Outpatient dilatation", "Antibiotics alone"], 0,
  "Perforation: emergency surgery. (Book p128)")
q(128, S5, "The grading system used for corrosive esophageal injury is:",
  ["Zargar's classification", "Savary-Miller classification", "Los Angeles classification",
   "Forrest classification"], 0,
  "Grading of injury: Zargar's classification. (Book p128)")
q(128, S5, "In Zargar's classification, grade 2B injury is:",
  ["Deep or circumferential ulceration", "Normal mucosa", "Superficial edema/erythema",
   "Perforation"], 0,
  "Zargar: 2A superficial ulceration; 2B deep or circumferential ulceration. (Book p128)")
q(128, S5, "Extensive necrosis in Zargar's classification is graded as:",
  ["3B", "3A", "2B", "4"], 0,
  "Zargar: 3A focal necrosis, 3B extensive necrosis, 4 perforation. (Book p128)")

# ---------------- p129 · TEF: TYPES & DIAGNOSIS ----------------
S6 = "Tracheo-Esophageal Fistula: Types & Diagnosis"
q(129, S6, "The m/c type of tracheo-esophageal fistula is:",
  ["Type C - proximal esophageal atresia with distal TEF",
   "Type A - esophageal atresia without fistula",
   "Type B - proximal TEF with distal esophageal atresia",
   "Type E - H type fistula"], 0,
  "Type C (proximal EA with distal TEF) is the m/c type. (Book p129)")
q(129, S6, "Type A tracheo-esophageal anomaly is:",
  ["Esophageal atresia without any fistula", "Proximal TEF with distal atresia",
   "H type fistula", "Both proximal and distal fistulae"], 0,
  "Type A: esophageal atresia only. (Book p129)")
q(129, S6, "Type B TEF consists of:",
  ["Proximal TEF with distal esophageal atresia", "Distal TEF with proximal atresia",
   "Both proximal and distal TEF", "Isolated esophageal stenosis"], 0,
  "Type B: proximal TEF with distal EA. (Book p129)")
q(129, S6, "Type D TEF consists of:",
  ["Both proximal and distal TEF", "No fistula at all",
   "Proximal atresia with distal fistula", "Isolated esophageal stenosis"], 0,
  "Type D: proximal and distal TEF. (Book p129)")
q(129, S6, "The H type of TEF is:",
  ["TEF without esophageal atresia", "Atresia with no fistula",
   "Proximal atresia with distal fistula", "Esophageal stenosis with fistula"], 0,
  "H type: TEF without esophageal atresia (esophagus is patent). (Book p129)")
q(129, S6, "Tracheo-esophageal fistula is associated with mutation of the:",
  ["N-myc gene", "RET gene", "NF1 gene", "p53 gene"], 0,
  "TEF is associated with N-myc gene mutation. (Book p129)")
q(129, S6, "Before birth, TEF is suggested by:",
  ["Polyhydramnios", "Oligohydramnios", "Intrauterine growth restriction", "Placenta praevia"], 0,
  "Intra-uterine: associated with polyhydramnios; can be detected on pre-natal scan. (Book p129)")
q(129, S6, "After birth, the earliest sign of esophageal atresia is:",
  ["Excessive drooling of saliva", "Projectile vomiting", "Abdominal distension", "Jaundice"], 0,
  "After birth: excessive drooling of saliva. (Book p129)")
q(129, S6, "Coiling of the orogastric tube on insertion in a newborn suggests:",
  ["Esophageal atresia (m/c with type C)", "Duodenal atresia", "Pyloric stenosis",
   "Malrotation"], 0,
  "Coiling of OG tube on insertion - typical of type C (m/c). (Book p129)")
q(129, S6, "The confirmatory test for TEF is:",
  ["Contrast study (iohexol preferred over diatrizoate)", "Plain X-ray alone",
   "CT chest", "Esophageal manometry"], 0,
  "Confirmatory test: contrast study (iohexol > diatrizoate). (Book p129)")
q(129, S6, "The investigation of choice for H type TEF is:",
  ["Combined tracheo-esophagoscopy", "Barium meal", "MRI neck", "Ultrasound"], 0,
  "IOC for H type: combined tracheo-esophagoscopy. (Book p129)")
q(129, S6, "Gas in the stomach on X-ray in a neonate with TEF indicates:",
  ["A distal TEF", "Pure esophageal atresia with no fistula", "Duodenal atresia",
   "Diaphragmatic hernia"], 0,
  "X-ray showing stomach gas indicates a distal TEF. (Book p129)")

# ---------------- p130 · TEF: ASSOCIATED ANOMALIES & MANAGEMENT ----------------
S7 = "TEF: Associated Anomalies & Management"
q(130, S7, "The mnemonic for anomalies associated with TEF is:",
  ["VACTERL", "CHARGE", "CATCH 22", "TORCH"], 0,
  "Associated anomalies: VACTERL. (Book p130)")
q(130, S7, "In the VACTERL association, the letter A stands for:",
  ["Anorectal malformations", "Anal atresia with fistula", "Appendicular anomalies",
   "Aortic anomalies"], 0,
  "VACTERL: vertebral defects, anorectal malformations, cardiac abnormalities, TE fistula, renal, limb abnormalities. (Book p130)")
q(130, S7, "The 'TE' in VACTERL stands for:",
  ["Tracheo-esophageal fistula", "Tracheal atresia", "Thymic enlargement",
   "Thoracic ectopia"], 0,
  "TE: tracheo-esophageal fistula. (Book p130)")
q(130, S7, "According to the Waterston criteria, a baby with TEF weighing >= 2.5 kg is managed by:",
  ["Upfront surgery", "Gastrostomy and delayed surgery", "Antibiotics and delayed surgery",
   "Conservative management"], 0,
  "Waterston: >= 2.5 kg - upfront surgery. (Book p130)")
q(130, S7, "A baby with TEF weighing 1.8-2.5 kg with pneumonia is managed by:",
  ["Antibiotics followed by delayed surgery", "Immediate upfront surgery",
   "Gastrostomy alone", "No intervention"], 0,
  "Waterston: 1.8-2.5 kg +/- pneumonia - antibiotics, build weight, then delayed surgery. (Book p130)")
q(130, S7, "A baby with TEF weighing < 1.8 kg is managed by:",
  ["Gastrostomy, treatment of pneumonia and delayed surgery", "Upfront surgery",
   "Endoscopic dilation", "Conservative feeding"], 0,
  "Waterston: < 1.8 kg - gastrostomy, increase weight, treat pneumonia, delayed surgery. (Book p130)")
q(130, S7, "In type A esophageal atresia with the two ends far apart, the options include gastrostomy and the:",
  ["Flourish device - magnets at both ends to hasten growth",
   "Immediate primary anastomosis", "Total esophagectomy", "Roux-en-Y reconstruction"], 0,
  "If ends are far apart: gastrostomy or Flourish device (magnets at both ends to hasten growth). (Book p130)")
q(130, S7, "Types B, C, D and E of TEF are approached through a:",
  ["Posterolateral thoracotomy", "Laparotomy", "Cervical incision alone",
   "Median sternotomy"], 0,
  "Type B, C, D and E: posterolateral thoracotomy to identify the fistulous area. (Book p130)")
q(130, S7, "During repair of a TEF, the trachea is repaired with:",
  ["PDS (polydioxanone suture)", "Silk", "Catgut", "Steel wire"], 0,
  "Repair trachea with PDS (polydioxanone suture). (Book p130)")

# ---------------- p131 · GERD: PATHOGENESIS ----------------
S8 = "GERD: Pathogenesis & Protective Factors"
q(131, S8, "The most important protective factor against GERD is:",
  ["Angle of His", "Arrangement of mucosal folds", "Length of the esophagus",
   "Salivary bicarbonate"], 0,
  "Protective factors: angle of His is the most important. (Book p131)")
q(131, S8, "The normal length of the intra-abdominal esophagus is:",
  ["3-5 cm", "1 cm", "8-10 cm", "10-12 cm"], 0,
  "Protective factor: intra-abdominal esophagus 3-5 cm. (Book p131)")
q(131, S8, "The protective factor contributing the least to GERD prevention is:",
  ["Arrangement of mucosal folds", "Angle of His", "Intra-abdominal esophagus length",
   "Pinching effect of diaphragmatic crura"], 0,
  "Arrangement of mucosal fold: least contribution. (Book p131)")
q(131, S8, "An intra-abdominal esophageal length less than which value predisposes to GERD?",
  ["Less than 2 cm", "Less than 5 cm", "Less than 8 cm", "Less than 1 cm"], 0,
  "Pathogenesis: intra-abdominal esophagus length < 2 cm. (Book p131)")
q(131, S8, "A lower esophageal sphincter pressure below which value predisposes to GERD?",
  ["Less than 10 mmHg", "Less than 30 mmHg", "Less than 50 mmHg", "Less than 100 mmHg"], 0,
  "Pathogenesis: LES pressure < 10 mmHg. (Book p131)")
q(131, S8, "Transient lower esophageal sphincter relaxations (TLOSR) in GERD are:",
  ["Increased", "Decreased", "Absent", "Unchanged"], 0,
  "Pathogenesis: increased TLOSR (transient lower esophageal sphincter relaxation). (Book p131)")
q(131, S8, "The pinching effect of the diaphragmatic crura is a:",
  ["Protective factor against GERD", "Cause of achalasia", "Cause of Barrett's esophagus",
   "Cause of Boerhaave's syndrome"], 0,
  "Protective factor: pinching effect of diaphragmatic crura. (Book p131)")
q(131, S8, "Central obesity increases the risk of:",
  ["Barrett's esophagus and adenocarcinoma", "Achalasia cardia", "Esophageal web",
   "Zenker's diverticulum"], 0,
  "Central obesity: increased risk of Barrett's esophagus and adenocarcinoma. (Book p131)")
q(131, S8, "Falling H. pylori rates are noted in the risk factor discussion of:",
  ["GERD", "Peptic ulcer disease", "Carcinoid syndrome", "Achalasia"], 0,
  "Risk factors for GERD include obesity; note the decreasing H. pylori rates. (Book p131)")

# ---------------- p131 · GERD: CLINICAL FEATURES & INVESTIGATIONS ----------------
S9 = "GERD: Clinical Features & Investigations"
q(131, S9, "The m/c symptom of GERD is:",
  ["Retrosternal burning (heartburn)", "Water brash", "Dysphagia", "Hematemesis"], 0,
  "Clinical features: retrosternal burn (heartburn) is the m/c. (Book p131)")
q(131, S9, "Water brash refers to:",
  ["Sudden excessive salivation with reflux", "Vomiting of blood",
   "Nocturnal cough", "Pain on swallowing"], 0,
  "Water brash is a recognised feature of GERD. (Book p131)")
q(131, S9, "Extra-esophageal manifestations of GERD include all of the following EXCEPT:",
  ["Hematuria", "Pharyngitis / laryngitis", "Dental caries", "Chronic cough and wheezing"], 0,
  "Features: pharyngitis/laryngitis, dental caries, chronic cough and wheezing. (Book p131)")
q(131, S9, "The investigation of choice for GERD is:",
  ["Upper GI endoscopy", "24 hour pH monitoring", "Barium swallow", "Manometry"], 0,
  "IOC: upper GI endoscopy. (Book p131)")
q(131, S9, "The gold standard investigation for GERD is:",
  ["24 hour pH monitoring", "Upper GI endoscopy", "Barium swallow", "CT scan"], 0,
  "Gold standard: 24 hr pH monitoring. (Book p131)")
q(131, S9, "24 hour pH monitoring is indicated when:",
  ["Endoscopy is inconclusive or an intervention is planned",
   "The patient has dysphagia", "There is hematemesis", "There is weight loss"], 0,
  "Indications for pH monitoring: endoscopy inconclusive or intervention planned. (Book p131)")
q(131, S9, "The pH probe in 24 hour pH monitoring is placed:",
  ["5 cm proximal to the gastroesophageal junction", "At the cricopharyngeus",
   "In the gastric antrum", "10 cm above the diaphragm"], 0,
  "pH probe: 5 cm proximal to the GE junction. (Book p131)")
q(131, S9, "Proton pump inhibitors should be stopped before pH monitoring for:",
  ["5-10 days", "24 hours", "1 month", "They need not be stopped"], 0,
  "Stop PPI 5-10 days before pH monitoring for accuracy. (Book p131)")
q(131, S9, "A DeMeester score above which value is diagnostic of GERD?",
  ["> 14.72", "> 4.7", "> 1.4", "> 40"], 0,
  "DeMeester score > 14.72 indicates GERD. (Book p131)")

# ---------------- p131-132 · GERD: TREATMENT ----------------
S10 = "GERD: Lifestyle & Medical Treatment"
q(131, S10, "Lifestyle modification for GERD includes all of the following EXCEPT:",
  ["Large meals at bedtime", "Weight reduction",
   "Avoiding fried, fatty and spicy food, citrus, chocolate and mint",
   "Small, frequent meals"], 0,
  "Lifestyle: weight reduction, avoid fried/fatty/spicy food, citrus, chocolate, mint; small frequent meals; dine 2-3 hrs before sleeping. (Book p131)")
q(131, S10, "Patients with GERD are advised to have dinner how long before sleeping?",
  ["2-3 hours", "Immediately before sleep", "6-8 hours", "30 minutes"], 0,
  "Dine 2-3 hrs before sleeping. (Book p131)")
q(132, S10, "Medical management of GERD includes:",
  ["Proton pump inhibitors, prokinetics and antacids",
   "Proton pump inhibitors only", "Antibiotics and steroids", "H2 blockers with chemotherapy"], 0,
  "Medications: PPI, prokinetics, antacids. (Book p132)")

# ---------------- p132 · GERD: SURGERY & FUNDOPLICATION ----------------
S11 = "GERD: Surgical Management & Fundoplication"
q(132, S11, "Surgery for GERD is indicated in all of the following EXCEPT:",
  ["Asymptomatic patients on no medication",
   "Patients not responding to medical management",
   "Complications of GERD such as Barrett's esophagus, strictures or adenocarcinoma",
   "Patients with an associated sliding hiatal hernia"], 0,
  "Indications for surgery: failed medical management, GERD complications (Barrett's, stricture, adenocarcinoma), associated sliding hiatal hernia, patient wants to stop medication. (Book p132)")
q(132, S11, "The two operations described for GERD are fundoplication and:",
  ["Collis gastroplasty", "Heller's myotomy", "Nissen's cardioplasty", "Ramstedt's pyloromyotomy"], 0,
  "Surgery for GERD: fundoplication or Collis gastroplasty. (Book p132)")
q(132, S11, "During fundoplication the intra-abdominal esophageal length restored should be at least:",
  ["3 cm", "1 cm", "10 cm", "8 cm"], 0,
  "Principles: restore intra-abdominal esophagus length >= 3 cm. (Book p132)")
q(132, S11, "Nissen's fundoplication is a:",
  ["Complete 360 degree wrap", "180 degree anterior wrap", "270 degree posterior wrap",
   "180 degree posterior wrap"], 0,
  "Complete wrap (Nissen's): 360 degrees. (Book p132)")
q(132, S11, "The m/c complication of Nissen's fundoplication is:",
  ["Gas bloat syndrome", "Dumping syndrome", "Blind loop syndrome", "Short bowel syndrome"], 0,
  "Complete wrap (Nissen's 360): m/c complication is gas bloat syndrome. (Book p132)")
q(132, S11, "Dor fundoplication is a:",
  ["180 degree anterior wrap", "180-270 degree posterior wrap", "270 degree anterior wrap",
   "Complete 360 degree wrap"], 0,
  "Partial wrap: Dor = 180 degrees anterior. (Book p132)")
q(132, S11, "Toupet fundoplication is a:",
  ["180-270 degree posterior wrap", "180 degree anterior wrap", "Complete 360 degree wrap",
   "270 degree anterior wrap"], 0,
  "Toupet: 180-270 degrees posterior wrap. (Book p132)")
q(132, S11, "Belsey Mark fundoplication is a:",
  ["270 degree anterior wrap", "180 degree posterior wrap", "Complete 360 degree wrap",
   "90 degree lateral wrap"], 0,
  "Belsey Mark: 270 degrees anterior. (Book p132)")
q(132, S11, "Preservation of which structure is a principle of fundoplication?",
  ["Vagus nerve", "Phrenic nerve", "Thoracic duct", "Azygos vein"], 0,
  "Principles of fundoplication include preserving the vagus nerve. (Book p132)")
q(132, S11, "Re-establishing the angle of His is one of the principles of:",
  ["Fundoplication", "Heller's myotomy", "Esophagectomy", "Cardiomyotomy"], 0,
  "Principle of fundoplication: re-establish the angle of His. (Book p132)")
q(132, S11, "Tightening of the diaphragmatic crura around the esophagus is done during:",
  ["Fundoplication", "Esophagectomy", "Heller's myotomy", "Zenker's diverticulectomy"], 0,
  "Principle: tighten diaphragmatic crura around the esophagus. (Book p132)")

# ---------------- p132-133 · COLLIS GASTROPLASTY & NEWER MODALITIES ----------------
S12 = "Collis Gastroplasty & Newer Modalities"
q(132, S12, "The indication for Collis gastroplasty is:",
  ["Esophageal shortening", "Achalasia cardia", "Barrett's esophagus", "Esophageal web"], 0,
  "Collis gastroplasty: indication is esophageal shortening. (Book p132)")
q(132, S12, "The neo-esophagus is created in:",
  ["Collis gastroplasty", "Nissen's fundoplication", "Heller's myotomy", "Toupet fundoplication"], 0,
  "Collis gastroplasty creates a neo-esophagus. (Book p132)")
q(133, S12, "Polymer injection around the LES to tighten the sphincter is:",
  ["Not preferred because of a high recurrence rate", "The gold standard treatment",
   "Preferred over fundoplication", "Used only in achalasia"], 0,
  "Newer modality: polymer injection around LES - high recurrence rate, not preferred. (Book p133)")
q(133, S12, "Transoral incisionless fundoplication is a:",
  ["NOTES (natural orifice transluminal endoscopic surgery) procedure",
   "Laparoscopic procedure", "Open thoracic procedure", "Radiological procedure"], 0,
  "Transoral incisionless fundoplication: NOTES procedure. (Book p133)")
q(133, S12, "Transoral incisionless fundoplication gives good long term results in patients with:",
  ["Minimal or no hiatus hernia", "Large paraesophageal hernia", "Barrett's esophagus",
   "Previous esophagectomy"], 0,
  "Transoral incisionless fundoplication: good long-term results in patients with minimal/no hiatus hernia. (Book p133)")

# ---------------- p133 · BARRETT'S ESOPHAGUS ----------------
S13 = "Barrett's Esophagus: Diagnosis & Types"
q(133, S13, "Barrett's esophagus is:",
  ["Specialised intestinal metaplasia with squamous epithelium replaced by columnar epithelium",
   "Congenital columnar lining of the esophagus",
   "Squamous metaplasia of the stomach",
   "Hypertrophy of the muscularis mucosa"], 0,
  "Barrett's esophagus: specialised intestinal metaplasia - squamous to columnar epithelium. (Book p133)")
q(133, S13, "The pathognomonic endoscopic finding in Barrett's esophagus is:",
  ["Red velvety mucosa", "White plaques", "Blue rubber bleb nodules", "Black necrotic patches"], 0,
  "Pathognomonic finding: red velvety mucosa. (Book p133)")
q(133, S13, "The diagnostic cell on biopsy in Barrett's esophagus is the:",
  ["Goblet cell", "Parietal cell", "Kupffer cell", "Paneth cell"], 0,
  "On biopsy of Barrett's esophagus: goblet cells. (Book p133)")
q(133, S13, "Barrett's esophagus is a complication of:",
  ["GERD", "Achalasia", "Corrosive stricture", "Esophageal web"], 0,
  "Barrett's esophagus: C/F same as GERD but do not respond to treatment. (Book p133)")
q(133, S13, "Barrett's esophagus increases the risk of:",
  ["Adenocarcinoma of the esophagus", "Squamous cell carcinoma only",
   "Esophageal varices", "Achalasia"], 0,
  "Barrett's esophagus: increased risk of adenocarcinoma. (Book p133)")
q(133, S13, "Long segment Barrett's esophagus measures:",
  [">= 3 cm", "< 3 cm", "> 10 cm", "The whole esophagus"], 0,
  "Types: long segment >= 3 cm; short segment < 3 cm. (Book p133)")
q(133, S13, "Microscopic Barrett's is also called:",
  ["Cardia metaplasia", "Fundic metaplasia", "Pyloric metaplasia", "Antral metaplasia"], 0,
  "Types: cardia metaplasia / microscopic Barrett's. (Book p133)")
q(133, S13, "Barrett's esophagus is identified at endoscopy using:",
  ["Chromoendoscopy", "Narrow band imaging only", "Capsule endoscopy", "Endoscopic ultrasound"], 0,
  "Identification: chromoendoscopy. (Book p133)")
q(133, S13, "Lugol's iodine stains:",
  ["Squamous epithelium", "Barrett's esophagus", "Adenocarcinoma", "Goblet cells"], 0,
  "Lugol's iodine: squamous epithelium. (Book p133)")
q(133, S13, "Methylene blue stains:",
  ["Barrett's esophagus and adenocarcinoma", "Normal squamous epithelium",
   "Submucosal vessels", "Lymphoid tissue"], 0,
  "Methylene blue stains Barrett's esophagus and adenocarcinoma. (Book p133)")

# ---------------- p134 · SURVEILLANCE: PRAGUE & SEATTLE ----------------
S14 = "Barrett's Surveillance: Prague Criteria & Seattle Protocol"
q(134, S14, "In the Prague C & M criteria, M stands for:",
  ["Maximum extent of Barrett's in cm", "Minimal extent", "Mucosal thickness", "Metaplastic grade"], 0,
  "Prague C & M criteria: M = maximum extent (cm). (Book p134)")
q(134, S14, "Increasing maximum extent (M) of Barrett's esophagus is associated with:",
  ["Increased risk of cancer", "Decreased risk of cancer", "No change in risk",
   "Spontaneous regression"], 0,
  "M: maximum extent - increasing extent increases the risk of cancer. (Book p134)")
q(134, S14, "The Seattle biopsy protocol recommends 4 quadrant biopsies every:",
  ["2 cm", "1 cm", "5 cm", "10 cm"], 0,
  "Seattle biopsy protocol: 4 quadrant biopsy every 2 cm. (Book p134)")
q(134, S14, "Dysplasia in Barrett's esophagus should be confirmed by:",
  ["Two independent pathologists", "A single pathologist", "The endoscopist alone",
   "Frozen section only"], 0,
  "Dysplasia confirmed by two independent pathologists. (Book p134)")
q(134, S14, "In the Seattle protocol, the biopsy technique recommended is:",
  ["Systematic cold biopsy", "Hot biopsy with cautery", "Brush cytology alone",
   "Fine needle aspiration"], 0,
  "Seattle protocol: systematic cold biopsy. (Book p134)")
q(134, S14, "A patient with Barrett's esophagus and no dysplasia is followed by repeat OGD and biopsy every:",
  ["3-5 years", "3 months", "6 months", "10 years"], 0,
  "No dysplasia: repeat OGD + biopsy every 3-5 years. (Book p134)")
q(134, S14, "Low grade dysplasia in Barrett's esophagus is followed up with OGD:",
  ["Every 6 months until two consecutive examinations show non-dysplastic Barrett's",
   "Every 3-5 years", "Every 10 years", "Once, then discharge"], 0,
  "LGD: OGD every 6 months until two consecutive evidence of non-dysplastic Barrett's. (Book p134)")
q(134, S14, "High grade dysplasia or cancer in Barrett's esophagus is managed after:",
  ["MDT discussion", "Immediate discharge", "Repeat biopsy after 5 years", "Antibiotics"], 0,
  "HGD or cancer: MDT discussion then therapeutic intervention. (Book p134)")
q(134, S14, "Therapeutic interventions for high grade dysplasia in Barrett's are:",
  ["Esophagectomy or endoscopic radiofrequency ablation",
   "Antireflux surgery alone", "Dilatation alone", "Chemotherapy alone"], 0,
  "Therapeutic intervention: surgery (esophagectomy) or endoscopic RFA. (Book p134)")

# ---------------- units ----------------
def sec_ids(*labels):
    return [x["id"] for x in Q if x["sec"] in labels]
def first_page(label):
    for x in Q:
        if x["sec"] == label:
            return x["page"]
    return 0

UNIT_DEFS = [
    (S1, "Three constrictions to memorise: C6 at the pharyngoesophageal junction (the narrowest point in the whole GIT at 4 mm - where foreign bodies stick and scopes perforate), T4 from the aortic arch and left main bronchus, T10 at the diaphragm. Diaphragm openings run T8 = IVC + phrenic nerve, T10 = esophagus, vagus and left gastric artery, T12 = aorta + thoracic duct."),
    (S2, "Segmental blood supply: upper third from the inferior thyroid, middle from the descending thoracic aorta and bronchial branches, lower from the left gastric artery (the vessel that bleeds in a Mallory-Weiss tear). The lower esophageal veins join the portal system, which is why they become porto-systemic varices. No serosa, submucosa is the strongest layer, and skip metastases travel longitudinally - hence the long proximal margin at esophagectomy."),
    (S3, "The UES is both anatomical and physiological; the LES is purely physiological (3-5 cm long, 2-4 cm of it below the diaphragm). Cricopharyngeus horizontal fibres sit just above Killian's dehiscence, the weak spot behind Zenker's diverticulum. Relax too often and you get reflux; fail to relax and you get achalasia. Peristalsis: primary propulsive, secondary rescue wave, tertiary non-propulsive and more common with age."),
    (S4, "Coins read differently depending on where they are: a coin in the esophagus lies side-face-on in the AP view, in the trachea end-face-on (the sagittal plate of the trachea forces that orientation). Dysphagia means esophagus, choking and stridor means airway. Impacted at C6 and symptomatic → endoscopy; past C6 and asymptomatic → observe; button batteries → endoscopy whatever the site, because they corrode through."),
    (S5, "Alkali liquefies by saponification and bores deep; acid coagulates protein, so damage is shallower but pylorospasm pools it in the stomach. Resuscitate with IV fluids, never pass a NG tube blind, no prophylactic antibiotics and no steroids - get an expert endoscopy within 48 hours and grade with Zargar (2B deep/circumferential ulcer, 3B extensive necrosis, 4 perforation). Strictures are dilated or resected; perforation goes to theatre."),
    (S6, "Know the alphabet: A = pure atresia, B = proximal fistula with distal atresia, C = proximal atresia with distal fistula (commonest), D = both fistulae, H = fistula with a patent esophagus. Antenatal polyhydramnios, postnatal drooling and a coiled OG tube. Contrast study (iohexol preferred) confirms; combined tracheo-esophagoscopy is the IOC for the H type."),
    (S7, "Look for the VACTERL partners (vertebral, anorectal, cardiac, TEF, renal, limb) and stage the baby with Waterston: >= 2.5 kg goes straight to surgery, 1.8-2.5 kg gets antibiotics and building up first, < 1.8 kg gets a gastrostomy and delayed repair. Long-gap atresia may need a gastrostomy and the Flourish magnetic device; the rest are repaired through a posterolateral thoracotomy - divide the fistula, close the trachea with PDS, anastomose the ends."),
    (S8, "Reflux is a barrier failure: the angle of His guards the junction (the single most important factor, with the mucosal folds contributing least), an intra-abdominal length under 2 cm, a LES pressure under 10 mmHg and too many transient relaxations all let acid through; central obesity pushes it towards Barrett's and adenocarcinoma."),
    (S9, "Heartburn is the classic symptom; look also for water brash, pharyngitis, dental caries and chronic cough or wheeze. Endoscopy is the IOC, but 24-hour pH monitoring remains the gold standard when endoscopy is inconclusive or before intervention: probe 5 cm above the GE junction, PPIs stopped 5-10 days beforehand, DeMeester score above 14.72 is GERD."),
    (S10, "Start with lifestyle: lose weight, avoid fried, fatty and spicy food, citrus, chocolate and mint, eat small frequent meals and finish dinner 2-3 hours before bed. Drugs are PPIs, prokinetics and antacids."),
    (S11, "Operate when drugs fail, when complications appear (Barrett's, stricture, adenocarcinoma), when a sliding hiatus hernia accompanies it, or when the patient wants off medication. Fundoplication restores 3 cm of intra-abdominal esophagus, tightens the crura, re-creates the angle of His, wraps the fundus and spares the vagus. Nissen 360 (gas bloat is its bugbear), Dor 180 anterior, Toupet 180-270 posterior, Belsey Mark 270 anterior."),
    (S12, "Collis gastroplasty builds a neo-esophagus when the esophagus is short. Polymer injection around the LES has a high recurrence rate and is not preferred; transoral incisionless fundoplication (a NOTES procedure) does well in patients with minimal or no hiatus hernia."),
    (S13, "Barrett's is specialised intestinal metaplasia - squamous turns columnar, seen as red velvety mucosa and proved by goblet cells on biopsy. Symptoms mirror GERD but stop responding to treatment, some are silent, and adenocarcinoma risk climbs. Long segment >= 3 cm, short segment < 3 cm, microscopic disease = cardia metaplasia; chromoendoscopy with Lugol's iodine (squamous) and methylene blue (Barrett's and cancer) helps target biopsies."),
    (S14, "Measure with Prague (C and M in cm; longer segments mean more cancer risk) and sample with the Seattle protocol - 4-quadrant cold biopsies every 2 cm, dysplasia confirmed by two independent pathologists. No dysplasia: OGD every 3-5 years; low-grade dysplasia: OGD every 6 months until two consecutive clean scopes; high-grade dysplasia or cancer goes to MDT for esophagectomy or endoscopic RFA."),
]

UNITS = []
for i, (title, guide) in enumerate(UNIT_DEFS, 1):
    UNITS.append({"id": f"SURG-U19-{i}", "ch": 19, "n": i, "title": title,
                  "sec": f"{title} · p{first_page(title)}",
                  "qs": sec_ids(title), "guide": guide})

covered = [i for u in UNITS for i in u["qs"]]
assert covered == [x["id"] for x in Q], "units must cover questions in order"

data = {"questions": Q, "units": UNITS}
with open("data/ch19.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
print(f"ch19: {len(Q)} questions, {len(UNITS)} units")
