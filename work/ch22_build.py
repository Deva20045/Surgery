#!/usr/bin/env python3
"""Build data/ch22.json for PULSE Surgery ch22 (Stomach : Part 1, book p150-156)."""
import json

Q = []
def q(page, sec, text, opts, ans, exp):
    Q.append({"id": f"SURG-C22-{len(Q)+1:03d}", "sec": sec, "page": page,
              "q": text, "opts": opts, "ans": ans, "exp": exp})

# ---------------- p150 · RELEVANT ANATOMY ----------------
S1 = "Stomach: Relevant Anatomy"
q(150, S1, "The parts of the stomach are:",
  ["Cardia, fundus, body, antrum and pylorus", "Cardia, body and duodenum",
   "Fundus, body and jejunum", "Cardia, antrum and ileum"], 0,
  "Parts of stomach: cardia, fundus, body, antrum, pylorus. (Book p150)")
q(150, S1, "The left gastric artery is a branch of the:",
  ["Coeliac axis", "Common hepatic artery", "Gastroduodenal artery", "Splenic artery"], 0,
  "Left gastric artery: branch of the coeliac axis. (Book p150)")
q(150, S1, "The dominant artery of the stomach is the:",
  ["Left gastric artery", "Right gastric artery", "Right gastroepiploic artery",
   "Short gastric artery"], 0,
  "Left gastric artery: dominant artery of the stomach. (Book p150)")
q(150, S1, "The artery involved in a type IV gastric ulcer and in a Mallory Weiss tear is the:",
  ["Left gastric artery", "Gastroduodenal artery", "Splenic artery", "Right gastroepiploic artery"], 0,
  "Left gastric artery: involved in type IV gastric ulcer and Mallory Weiss tear. (Book p150)")
q(150, S1, "The right gastric artery is a branch of the:",
  ["Common hepatic artery", "Coeliac axis", "Splenic artery", "Superior mesenteric artery"], 0,
  "Right gastric artery: branch of the common hepatic artery. (Book p150)")
q(150, S1, "The right gastroepiploic artery is a branch of the:",
  ["Gastroduodenal artery", "Splenic artery", "Coeliac axis", "Left hepatic artery"], 0,
  "Right gastroepiploic artery: branch of the gastroduodenal artery. (Book p150)")
q(150, S1, "The short gastric arteries are branches of the:",
  ["Splenic artery", "Common hepatic artery", "Coeliac axis", "Left gastric artery"], 0,
  "Short gastric arteries: branches of the splenic artery. (Book p150)")
q(150, S1, "The stomach tolerates ligation of several of its arteries because of:",
  ["Extensive submucosal anastomoses between the vessels",
   "A rich intramuscular plexus", "Collaterals from the superior mesenteric artery",
   "Its dual venous drainage"], 0,
  "Extensive submucosal anastomosis between the vessels - the stomach does not necrose even if vessels are ligated. (Book p150)")

# ---------------- p151 · VENOUS DRAINAGE ----------------
S2 = "Venous Drainage of the Stomach"
q(151, S2, "The veins of the stomach:",
  ["Correspond to the arteries", "Drain entirely into the inferior vena cava",
   "Are absent in the antrum", "Drain into the azygos system"], 0,
  "Venous supply: veins corresponding to the arteries. (Book p151)")
q(151, S2, "The vein responsible for metastases into the liver from the stomach is the:",
  ["Left gastric (coronary) vein", "Right gastroepiploic vein", "Short gastric vein",
   "Splenic vein"], 0,
  "Left gastric vein / coronary vein: responsible for metastases into the liver. (Book p151)")

# ---------------- p151 · CHPS: FEATURES ----------------
S3 = "Congenital Hypertrophic Pyloric Stenosis: Features"
q(151, S3, "Congenital hypertrophic pyloric stenosis is also known as:",
  ["Idiopathic hypertrophic pyloric stenosis", "Acquired pyloric stenosis",
   "Congenital pyloric atresia", "Infantile hypertrophic gastropathy"], 0,
  "CHPS: AKA idiopathic hypertrophic pyloric stenosis. (Book p151)")
q(151, S3, "The pathophysiology of CHPS is thickened pyloric muscle leading to:",
  ["Gastric outlet obstruction and vomiting", "Duodenal obstruction",
   "Intussusception", "Volvulus"], 0,
  "Thickened pyloric muscle → gastric outlet obstruction → vomiting. (Book p151)")
q(151, S3, "CHPS m/c affects:",
  ["First born male child", "First born female child", "Preterm female child",
   "Adolescent boys"], 0,
  "Features: m/c affects the first born male child. (Book p151)")
q(151, S3, "CHPS is associated with all of the following EXCEPT:",
  ["Down syndrome", "Apert syndrome", "Cornelia de Lange syndrome",
   "Erythromycin intake early in life"], 0,
  "Associations: Apert syndrome, Cornelia de Lange syndrome, decreased nitric oxide synthase levels, erythromycin intake early in life. (Book p151)")
q(151, S3, "Nitric oxide synthase levels in CHPS are:",
  ["Decreased", "Increased", "Normal", "Absent"], 0,
  "Association: decreased nitric oxide synthase levels. (Book p151)")
q(151, S3, "Infants with CHPS are typically asymptomatic for the:",
  ["First 2-3 weeks", "First 2-3 days", "First 6 months", "First year"], 0,
  "Presentation: asymptomatic during the first 2-3 weeks, followed by projectile non-bilious vomiting. (Book p151)")
q(151, S3, "The characteristic vomiting of CHPS is:",
  ["Projectile and non-bilious", "Projectile and bilious", "Small and bilious",
   "Effortless and faeculent"], 0,
  "Projectile, non-bilious vomiting is the hallmark of CHPS. (Book p151)")
q(151, S3, "The abdominal examination in CHPS is best performed:",
  ["During feeding", "After a bath", "During sleep", "After vomiting"], 0,
  "Examination: best done during feeding; palpate an olive shaped swelling. (Book p151)")
q(151, S3, "The palpable mass in CHPS is described as:",
  ["Olive shaped swelling", "Sausage shaped mass", "Cystic swelling", "Irregular hard mass"], 0,
  "Olive shaped swelling is palpated in CHPS. (Book p151)")
q(151, S3, "Visible peristalsis in CHPS moves:",
  ["From left to right", "From right to left", "From above downwards", "From below upwards"], 0,
  "Peristalsis: visible, left to right. (Book p151)")

# ---------------- p152 · CHPS: DIFFERENTIALS & INVESTIGATIONS ----------------
S4 = "CHPS: Differentials & Investigations"
q(152, S4, "Unlike CHPS, duodenal atresia presents with:",
  ["Bilious vomiting since birth", "Non bilious projectile vomiting after a few weeks",
   "No vomiting at all", "Haematemesis"], 0,
  "Duodenal atresia: bilious vomiting since birth; CHPS: non-bilious projectile vomiting after a few weeks. (Book p152)")
q(152, S4, "The X-ray sign of duodenal atresia is:",
  ["Double bubble sign", "Single bubble sign", "String sign", "Apple core sign"], 0,
  "Duodenal atresia: X-ray shows the double bubble sign. (Book p152)")
q(152, S4, "The investigation of choice for CHPS is:",
  ["Ultrasound", "Contrast study", "CT scan", "Plain X-ray alone"], 0,
  "Evaluation: IOC is USG. (Book p152)")
q(152, S4, "The ultrasound criterion for pyloric muscle thickness in CHPS is:",
  [">= 4 mm", ">= 10 mm", ">= 2 mm", ">= 20 mm"], 0,
  "USG: thickness >= 4 mm and increased pyloric channel length. (Book p152)")
q(152, S4, "The contrast study findings in CHPS include all of the following EXCEPT:",
  ["Double bubble sign", "String sign", "Mushroom sign", "Double tract sign"], 0,
  "Contrast study: string sign, mushroom sign, double tract sign. (Book p152)")
q(152, S4, "The plain X-ray finding in CHPS is:",
  ["Single bubble sign", "Double bubble sign", "Coffee bean sign", "Rigler's sign"], 0,
  "X-ray: single bubble sign. (Book p152)")

# ---------------- p152 · CHPS: METABOLIC ABNORMALITIES ----------------
S5 = "CHPS: Metabolic Abnormalities"
q(152, S5, "The metabolic abnormality in CHPS results from loss of:",
  ["Hydrochloric acid in the vomitus", "Bile in the vomitus", "Bicarbonate in the stool",
   "Potassium in the urine alone"], 0,
  "CHPS: loss of HCl due to vomiting (loss of H+ and Cl-). (Book p152)")
q(152, S5, "The acid base disturbance in CHPS is:",
  ["Metabolic alkalosis", "Metabolic acidosis", "Respiratory alkalosis",
   "Respiratory acidosis"], 0,
  "Loss of H+ and Cl- produces a metabolic alkalosis. (Book p152)")
q(152, S5, "Initially, the kidney compensates for the metabolic alkalosis of CHPS by:",
  ["Increased elimination of NaHCO3 in the urine", "Retaining bicarbonate",
   "Excreting hydrogen ions", "Excreting chloride"], 0,
  "Compensatory increase in elimination of NaHCO3 in the urine. (Book p152)")
q(152, S5, "Aldosterone release in CHPS occurs through activation of:",
  ["The renin angiotensin system", "The sympathetic nervous system", "Antidiuretic hormone",
   "The kallikrein system"], 0,
  "Activation of RAS (renin angiotensin system) causes aldosterone release. (Book p152)")
q(152, S5, "Paradoxical aciduria in CHPS means:",
  ["Acidic urine despite systemic metabolic alkalosis", "Alkaline urine with acidosis",
   "Absence of urine output", "Proteinuria with alkalosis"], 0,
  "H+ ions are eliminated in the urine initially with secretion of K+ into urine: paradoxical aciduria. (Book p152)")
q(152, S5, "The electrolyte and acid base picture in CHPS is:",
  ["Hypokalemia, hyponatremia, hypochloremia, metabolic alkalosis with paradoxical aciduria",
   "Hyperkalemia, hypernatremia, hyperchloremia and metabolic acidosis",
   "Hyperkalemia with metabolic acidosis", "Normal electrolytes with acidosis"], 0,
  "Hypokalemia, hyponatremia, hypochloremia, metabolic alkalosis with paradoxical aciduria. (Book p152)")

# ---------------- p153 · CHPS: MANAGEMENT ----------------
S6 = "CHPS: Management"
q(153, S6, "The intravenous fluid used for resuscitation in CHPS is:",
  ["Ringer lactate", "Normal saline alone", "Dextrose 5%", "Half normal saline"], 0,
  "Management: Ringer lactate. (Book p153)")
q(153, S6, "After an uneventful Ramstedt's pyloromyotomy, feeding is started at:",
  ["4-6 hours", "24-48 hours", "5 days", "2 weeks"], 0,
  "Uneventful surgery: feeding started in 4-6 hrs. (Book p153)")
q(153, S6, "If the mucosa is injured during pyloromyotomy, feeding is started at:",
  ["24-48 hours", "4-6 hours", "Immediately", "After 1 week"], 0,
  "Mucosal injury: feeding started in 24-48 hrs. (Book p153)")
q(153, S6, "The operation performed for CHPS is:",
  ["Ramstedt's pyloromyotomy", "Gastrojejunostomy", "Antrectomy", "Pyloroplasty"], 0,
  "Ramstedt's pyloromyotomy: muscle is split and the mucosa bulges out. (Book p153)")

# ---------------- p153 · PEPTIC ULCERS: TYPES ----------------
S7 = "Peptic Ulcers: Types"
q(153, S7, "The m/c peptic ulcer is:",
  ["Duodenal ulcer", "Gastric ulcer", "Esophageal ulcer", "Meckel's diverticulum ulcer"], 0,
  "Peptic ulcers: duodenal ulcer is the m/c type. (Book p153)")
q(153, S7, "The proportion of duodenal ulcers attributable to H. pylori is:",
  ["90-95%", "60-65%", "30-40%", "Less than 10%"], 0,
  "Duodenal ulcer: 90-95% due to H. pylori. (Book p153)")
q(153, S7, "The proportion of gastric ulcers attributable to H. pylori is:",
  ["60-65%", "90-95%", "100%", "Less than 10%"], 0,
  "Gastric ulcer: 60-65% due to H. pylori. (Book p153)")
q(153, S7, "Duodenal ulcers are characterised by:",
  ["Acid hypersecretion", "Normal acid production", "Hypochlorhydria", "Achlorhydria"], 0,
  "Duodenal ulcer: acid hypersecretion. (Book p153)")
q(153, S7, "Type I and type II gastric ulcers are associated with:",
  ["Normal acid production", "Acid hypersecretion", "Achlorhydria", "Pernicious anaemia"], 0,
  "Gastric ulcer type I and II: normal acid production. (Book p153)")
q(153, S7, "The m/c site of a duodenal ulcer is:",
  ["First part of the duodenum (D1)", "Second part of the duodenum",
   "Third part of the duodenum", "Duodenojejunal flexure"], 0,
  "Duodenal ulcers: m/c site is D1, the first part of the duodenum. (Book p153)")
q(153, S7, "Pain of a duodenal ulcer is classically:",
  ["Relieved with food", "Worsened with food", "Unrelated to food", "Worse at night only"], 0,
  "Duodenal ulcer: upper abdominal pain relieved with food. (Book p153)")

# ---------------- p154 · BLEEDING PEPTIC ULCER ----------------
S8 = "Peptic Ulcer: Bleeding"
q(154, S8, "The m/c complication of a peptic ulcer is:",
  ["Bleeding", "Perforation", "Gastric outlet obstruction", "Malignant transformation"], 0,
  "Complications: bleeding is the m/c. (Book p154)")
q(154, S8, "Bleeding from a duodenal ulcer commonly arises from a:",
  ["Posterior ulcer", "Anterior ulcer", "Pyloric canal ulcer", "Fundal ulcer"], 0,
  "Bleeding: posterior ulcers are commonly involved. (Book p154)")
q(154, S8, "The vessel implicated in bleeding from a duodenal ulcer is the:",
  ["Gastroduodenal artery", "Left gastric artery", "Splenic artery", "Short gastric artery"], 0,
  "Implicated vessel: gastroduodenal artery. (Book p154)")
q(154, S8, "Peptic ulcer disease is the m/c cause of:",
  ["Upper GI haemorrhage", "Lower GI haemorrhage", "Occult colonic bleeding",
   "Splenic rupture"], 0,
  "Bleeding peptic ulcer: m/c cause of upper GI hemorrhage. (Book p154)")
q(154, S8, "First line management of a bleeding peptic ulcer is:",
  ["Endoscopic management with adrenaline and coagulation",
   "Immediate laparotomy", "Angiographic embolisation", "Total gastrectomy"], 0,
  "Management: endoscopic management - adrenaline, coagulation. (Book p154)")
q(154, S8, "After a re-bleed from a peptic ulcer, the next step is:",
  ["A second trial of endoscopy", "Immediate gastrectomy", "Discharge with oral PPI",
   "Angiography only"], 0,
  "Re-bleeds: second trial of endoscopy. (Book p154)")
q(154, S8, "If endoscopic management of a bleeding peptic ulcer fails, the treatment is:",
  ["Surgery with under-running (ligation) of the vessel",
   "Continued medical management", "Radiotherapy", "Observation"], 0,
  "If endoscopy fails: surgery and under-run the vessel (ligate). (Book p154)")
q(154, S8, "After a bleeding peptic ulcer is controlled, the additional step advised is:",
  ["H. pylori eradication", "Long term steroids", "Repeat endoscopy every month",
   "Total parenteral nutrition"], 0,
  "Once bleeding stops: H. pylori eradication. (Book p154)")

# ---------------- p154 · PERFORATED PEPTIC ULCER ----------------
S9 = "Peptic Ulcer: Perforation"
q(154, S9, "Perforation of a duodenal ulcer is m/c seen with:",
  ["Anterior ulcers", "Posterior ulcers", "Pyloric ulcers", "Fundal ulcers"], 0,
  "Perforation: anterior ulcers (m/c). (Book p154)")
q(154, S9, "Perforation of an anterior duodenal ulcer presents with:",
  ["Peritonitis with guarding, rigidity and rebound tenderness",
   "Retroperitoneal gas", "Haematemesis", "Gastric outlet obstruction"], 0,
  "Anterior ulcer perforation: peritonitis - rebound tenderness, guarding, rigidity. (Book p154)")
q(154, S9, "The X-ray finding in a perforated peptic ulcer is:",
  ["Gas under the diaphragm", "Double bubble sign", "Coffee bean sign", "Air fluid levels only"], 0,
  "X-ray: gas under the diaphragm (hollow viscus perforation). (Book p154)")
q(154, S9, "The initial management of perforation peritonitis includes all of the following EXCEPT:",
  ["Immediate oral feeding", "IV fluids", "IV antibiotics with aerobic and anaerobic cover",
   "Analgesics"], 0,
  "Management of perforation peritonitis: IV fluids, preparation for emergency laparotomy, IV antibiotics (aerobic + anaerobic cover), analgesics. (Book p154)")
q(154, S9, "The definitive surgery for a perforated duodenal ulcer is:",
  ["Omental (Graham's) patch repair", "Total gastrectomy", "Gastrojejunostomy",
   "Vagotomy alone"], 0,
  "Definitive management: omental patch repair / Graham's patch repair. (Book p154)")
q(154, S9, "A posterior duodenal ulcer that perforates does so into the:",
  ["Retroperitoneum", "Peritoneal cavity", "Pleural cavity", "Lesser sac"], 0,
  "Posterior ulcer (rare): perforates into the retroperitoneum. (Book p154)")
q(154, S9, "Valentino syndrome, seen with a leaking posterior duodenal ulcer, mimics:",
  ["Acute appendicitis", "Acute cholecystitis", "Renal colic", "Pancreatitis"], 0,
  "Valentino syndrome: mimics acute appendicitis. (Book p154)")
q(154, S9, "Kocherisation is done in posterior duodenal ulcer surgery to:",
  ["Mobilise the duodenum to visualise the posterior ulcer",
   "Divide the gastroduodenal artery", "Close the perforation", "Perform a pyloroplasty"], 0,
  "Kocherisation: mobilisation of the duodenum to view the posterior ulcer. (Book p154)")

# ---------------- p155 · GASTRIC ULCERS: JOHNSON CLASSIFICATION ----------------
S10 = "Gastric Ulcers: Johnson's Classification"
q(155, S10, "Johnson's type I gastric ulcer is located:",
  ["Along the lesser curvature close to the incisura", "In the prepyloric region",
   "High in the body of the stomach", "In the fundus"], 0,
  "Type I: m/c type, along the lesser curvature (close to the incisura). (Book p155)")
q(155, S10, "The m/c type of gastric ulcer in Johnson's classification is:",
  ["Type I", "Type II", "Type III", "Type IV"], 0,
  "Type I is the m/c type of gastric ulcer. (Book p155)")
q(155, S10, "Johnson's type II gastric ulcer is:",
  ["A prepyloric ulcer associated with a duodenal ulcer", "A prepyloric ulcer alone",
   "An ulcer high in the body", "An NSAID induced ulcer"], 0,
  "Type II: prepyloric ulcer plus duodenal ulcer. (Book p155)")
q(155, S10, "Johnson's type III gastric ulcer is located:",
  ["In the prepyloric region", "Along the lesser curvature", "High in the body",
   "In the fundus"], 0,
  "Type III: prepyloric ulcer. (Book p155)")
q(155, S10, "Johnson's type IV gastric ulcer is located:",
  ["High up in the body of the stomach", "In the antrum", "In the pylorus", "In the fundus"], 0,
  "Type IV: high up in the body; the left gastric artery is the implicated vessel. (Book p155)")
q(155, S10, "Type IV gastric ulcers characteristically bleed from the:",
  ["Left gastric artery", "Gastroduodenal artery", "Splenic artery", "Short gastric artery"], 0,
  "Type IV: vessel is the left gastric artery; bleeds. (Book p155)")
q(155, S10, "Johnson's type V gastric ulcer is caused by:",
  ["NSAIDs", "H. pylori alone", "Radiotherapy", "Crohn's disease"], 0,
  "Type V: NSAID induced ulcer, diffuse. (Book p155)")
q(155, S10, "Bleeding is a feature mainly of Johnson's type:",
  ["IV and V", "I and II", "II and III", "III only"], 0,
  "Type IV and V: bleeding +/-. (Book p155)")

# ---------------- p155-156 · GASTRIC ULCER: DIAGNOSIS & MANAGEMENT ----------------
S11 = "Gastric Ulcer: Diagnosis & Management"
q(155, S11, "Pain in a gastric ulcer classically:",
  ["Worsens with food", "Is relieved with food", "Is unrelated to meals",
   "Occurs only at night"], 0,
  "Clinical features: pain worsens with food. (Book p155)")
q(155, S11, "The m/c complication of a gastric ulcer is:",
  ["Perforation", "Bleeding", "Gastric outlet obstruction", "Malignant transformation"], 0,
  "Gastric ulcer: m/c complication is perforation. (Book p155)")
q(155, S11, "The investigation used to diagnose a gastric ulcer is:",
  ["Upper GI endoscopy", "Barium swallow", "CT abdomen", "Ultrasound"], 0,
  "Diagnosis: upper GI endoscopy. (Book p155)")
q(155, S11, "The U or J manoeuvre during endoscopy is done to visualise:",
  ["A fundal ulcer", "A duodenal ulcer", "The pylorus", "The cardia"], 0,
  "U or J manoeuvre: to visualise a fundal ulcer. (Book p155)")
q(155, S11, "All gastric ulcers should be biopsied because:",
  ["Of the risk of an underlying cancer", "H. pylori can only be seen on biopsy",
   "It is the only way to stop bleeding", "Biopsy is therapeutic"], 0,
  "All gastric ulcers should be biopsied (risk of cancer). (Book p155)")
q(155, S11, "The vessel most often implicated in bleeding from a gastric ulcer is the:",
  ["Left gastric artery", "Gastroduodenal artery", "Right gastric artery",
   "Right gastroepiploic artery"], 0,
  "Gastric ulcer bleeding: left gastric artery; peptic (duodenal) ulcer bleeding: gastroduodenal artery. (Book p155)")
q(155, S11, "Johnson's type I gastric ulcer is managed by:",
  ["Distal gastrectomy with reconstruction (Billroth I or II)",
   "Proximal gastrectomy", "Total gastrectomy", "Vagotomy alone"], 0,
  "Type I: distal gastrectomy + reconstruction (Billroth I or II). (Book p155)")
q(156, S11, "Surgical options for a type IV (high) gastric ulcer include all of the following EXCEPT:",
  ["Total colectomy", "Pauchet procedure", "Kelling-Madlener procedure", "Csendes procedure"], 0,
  "Type IV operations: Pauchet procedure, Kelling-Madlener procedure, Csendes procedure. (Book p156)")
q(156, S11, "The Csendes procedure for a high gastric ulcer is a:",
  ["Roux-en-Y esophagogastrojejunostomy", "Subtotal gastrectomy with Roux-en-Y gastrojejunostomy",
   "Distal gastrectomy with Billroth I", "Local excision of the ulcer"], 0,
  "Csendes procedure: Roux-en-Y esophagogastrojejunostomy. (Book p156)")

# ---------------- p156 · H. PYLORI ----------------
S12 = "Helicobacter pylori"
q(156, S12, "H. pylori is the common cause of:",
  ["Gastric ulcer disease", "Esophageal candidiasis", "Achalasia cardia", "Zenker's diverticulum"], 0,
  "H. pylori: common cause of gastric ulcer disease. (Book p156)")
q(156, S12, "The genes of H. pylori that encode for toxins are:",
  ["CagA and VacA", "UreA and UreB", "ToxA and ToxB", "FlaA and FlaB"], 0,
  "CagA, VacA: genes that encode for toxins. (Book p156)")
q(156, S12, "The enzyme that allows H. pylori to survive the acidic environment is:",
  ["Urease", "Catalase", "Oxidase", "Protease"], 0,
  "Urease enzyme (+): survives acidic environment. (Book p156)")
q(156, S12, "H. pylori pathogenicity includes all of the following EXCEPT:",
  ["Crohn's disease", "Peptic ulcer", "Type B gastritis", "Gastric cancer"], 0,
  "Pathogenicity: peptic ulcer, type B gastritis, gastric cancer, MALTomas. (Book p156)")
q(156, S12, "MALTomas associated with H. pylori are:",
  ["Mucosal associated lymphoid tissue tumors", "Mucosal adenocarcinoma of the stomach",
   "Metastatic liver tumors", "Mesenchymal tumors"], 0,
  "MALTomas: mucosal associated lymphoid tissue tumors. (Book p156)")
q(156, S12, "H. pylori infection is thought to be:",
  ["Slightly protective against esophageal adenocarcinoma and GERD",
   "A strong risk factor for esophageal adenocarcinoma",
   "The cause of Barrett's esophagus",
   "Protective against gastric cancer"], 0,
  "H. pylori is slightly protective against adenocarcinoma of the esophagus and GERD. (Book p156)")

# ---------------- units ----------------
def sec_ids(*labels):
    return [x["id"] for x in Q if x["sec"] in labels]
def first_page(label):
    for x in Q:
        if x["sec"] == label:
            return x["page"]
    return 0

UNIT_DEFS = [
    (S1, "Four arteries feed the stomach - left gastric (direct off the coeliac axis, the dominant vessel, and the one that bleeds in a type IV gastric ulcer or a Mallory-Weiss tear), right gastric (common hepatic), right gastroepiploic (gastroduodenal) and the short gastrics (splenic). Because they anastomose freely in the submucosa, the stomach survives ligation of most of them."),
    (S2, "Gastric veins mirror the arteries, and the left gastric or coronary vein is the route by which gastric cancer seeds the liver."),
    (S3, "CHPS - idiopathic hypertrophic pyloric stenosis - is pyloric muscle hypertrophy causing gastric outlet obstruction, classically in a first-born boy between two and three weeks old, linked to Apert and Cornelia de Lange syndromes, low nitric oxide synthase and early erythromycin exposure. Feed the baby and watch: an olive mass is felt and peristaltic waves roll left to right."),
    (S4, "Bilious vomiting from birth with a double bubble means duodenal atresia; non-bilious projectile vomiting after a few weeks means CHPS. Ultrasound is the IOC (muscle thickness >= 4 mm, elongated channel); contrast shows the string, mushroom and double-tract signs and the X-ray a single bubble."),
    (S5, "Vomiting hydrochloric acid leaves behind hypochloraemic, hypokalaemic, hyponatraemic metabolic alkalosis. The kidney first spills bicarbonate, then the renin-angiotensin system drives aldosterone, sodium is reabsorbed at the cost of potassium and hydrogen - so the urine turns acid despite the alkalosis: paradoxical aciduria."),
    (S6, "Correct with Ringer lactate before Ramstedt's pyloromyotomy (split the muscle until the mucosa bulges). Feed at 4-6 hours if the operation was clean, at 24-48 hours if the mucosa was breached."),
    (S7, "Duodenal ulcers are the commonest peptic ulcers: 90-95% H. pylori, acid hypersecretion, first part of the duodenum, pain that food relieves. Gastric ulcers are 60-65% H. pylori with normal acid output in types I and II."),
    (S8, "Bleeding is the commonest complication and comes from posterior duodenal ulcers eroding the gastroduodenal artery - the commonest cause of upper GI haemorrhage. Endoscopic adrenaline and coagulation first, repeat endoscopy once for a re-bleed, then surgery to under-run the vessel; eradicate H. pylori once it is quiet."),
    (S9, "Perforation favours anterior ulcers and presents as peritonitis with gas under the diaphragm: resuscitate, antibiotics covering aerobes and anaerobes, analgesia and emergency Graham's omental patch. A posterior ulcer leaks backwards into the retroperitoneum - gas under the right kidney, Valentino syndrome mimicking appendicitis, and Kocherisation to see it."),
    (S10, "Johnson's classification: type I along the lesser curvature near the incisura (commonest), type II prepyloric plus duodenal, type III prepyloric, type IV high in the body eroding the left gastric artery, type V NSAID-related and diffuse; types IV and V bleed."),
    (S11, "Gastric ulcer pain worsens with food and perforates more often than it bleeds. Endoscopy (with the U/J manoeuvre for fundal ulcers) must biopsy every gastric ulcer to exclude cancer. Type I needs a distal gastrectomy with Billroth I or II; high type IV ulcers need Pauchet, Kelling-Madlener or a Csendes Roux-en-Y esophagogastrojejunostomy."),
    (S12, "H. pylori drives gastric ulcer disease through CagA and VacA toxins and urease, which lets it live in acid; it causes peptic ulceration, type B gastritis, gastric cancer and MALTomas - yet is slightly protective against esophageal adenocarcinoma and reflux."),
]

UNITS = []
for i, (title, guide) in enumerate(UNIT_DEFS, 1):
    UNITS.append({"id": f"SURG-U22-{i}", "ch": 22, "n": i, "title": title,
                  "sec": f"{title} · p{first_page(title)}",
                  "qs": sec_ids(title), "guide": guide})

covered = [i for u in UNITS for i in u["qs"]]
assert covered == [x["id"] for x in Q], "units must cover questions in order"

data = {"questions": Q, "units": UNITS}
with open("data/ch22.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
print(f"ch22: {len(Q)} questions, {len(UNITS)} units")
