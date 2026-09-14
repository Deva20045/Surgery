#!/usr/bin/env python3
"""Build data/ch28.json for PULSE Surgery ch28 (Bowel Obstruction : Part 2, book p191-196)."""
import json

Q = []
def q(page, sec, text, opts, ans, exp):
    Q.append({"id": f"SURG-C28-{len(Q)+1:03d}", "sec": sec, "page": page,
              "q": text, "opts": opts, "ans": ans, "exp": exp})

# ---------------- p191 · MECKEL'S: FEATURES ----------------
S1 = "Meckel's Diverticulum: Features and the Rule of Two"
q(191, S1, "Meckel's diverticulum is a:",
  ["True diverticulum containing all layers of the bowel wall",
   "False diverticulum containing only mucosa",
   "Congenital duplication cyst", "An acquired pulsion diverticulum"], 0,
  "Features: true diverticulum - all layers (+). (Book p191)")
q(191, S1, "Meckel's diverticulum occurs in approximately:",
  ["2% of the population", "20% of the population", "0.2% of the population",
   "50% of the population"], 0,
  "Rule of 2: 2% population. (Book p191)")
q(191, S1, "The length of a Meckel's diverticulum is about:",
  ["2 inches", "2 cm", "2 feet", "20 cm"], 0,
  "Rule of 2: 2 inches long. (Book p191)")
q(191, S1, "A Meckel's diverticulum is located about __________ from the ileocaecal junction.",
  ["2 feet", "2 inches", "20 cm", "2 cm"], 0,
  "Rule of 2: 2 feet from ileocaecal junction (ICJ). (Book p191)")
q(191, S1, "Heterotopic mucosa in a Meckel's diverticulum is most commonly:",
  ["Gastric, followed by pancreatic", "Pancreatic, followed by gastric",
   "Colonic", "Small intestinal"], 0,
  "Heterotopic mucosa (stomach > pancreatic) - can bleed. (Book p191)")

# ---------------- p191 · ASYMPTOMATIC / DIVERTICULITIS ----------------
S2 = "Meckel's Diverticulum: Asymptomatic Disease and Diverticulitis"
q(191, S2, "An asymptomatic Meckel's diverticulum found incidentally with a wide mouth/broad base should be managed:",
  ["Conservatively", "By diverticulectomy", "By resection and anastomosis",
   "By endoscopic removal"], 0,
  "Asymptomatic (incidentally detected): wide mouth/broad base → conservative. (Book p191)")
q(191, S2, "An incidentally detected Meckel's diverticulum with a narrow mouth/base is treated by:",
  ["Diverticulectomy", "Conservative management", "Observation alone",
   "Right hemicolectomy"], 0,
  "Narrow mouth/base → ↑ chance of obstruction/inflammation → diverticulectomy. (Book p191)")
q(191, S2, "Meckel's diverticulitis clinically mimics:",
  ["Acute appendicitis", "Acute cholecystitis", "Diverticulitis of the colon",
   "Acute pancreatitis"], 0,
  "Meckel's diverticulitis: mimics acute appendicitis. (Book p191)")
q(191, S2, "The pain of Meckel's diverticulitis classically:",
  ["Starts peri-umbilically and radiates to the right iliac fossa",
   "Starts in the left iliac fossa", "Starts in the epigastrium and radiates to the back",
   "Is confined to the left upper quadrant"], 0,
  "Peri-umbilical pain radiating to the right iliac fossa. (Book p191)")
q(191, S2, "The treatment of Meckel's diverticulitis is:",
  ["Diverticulectomy", "Conservative management", "Right hemicolectomy",
   "Appendicectomy alone"], 0,
  "Mx of Meckel's diverticulitis: diverticulectomy. (Book p191)")

# ---------------- p191-192 · OTHER PRESENTATIONS ----------------
S3 = "Meckel's Diverticulum: Perforation, Bleeding, Obstruction and Malignancy"
q(191, S3, "A perforated Meckel's diverticulum is treated by:",
  ["Diverticulectomy or resection and anastomosis", "Conservative management",
   "Drainage alone", "Appendicectomy"], 0,
  "Perforation: diverticulectomy / resection + anastomosis. (Book p191)")
q(191, S3, "Littre's hernia is a hernia containing a:",
  ["Meckel's diverticulum", "Appendix", "Ovary", "Urinary bladder"], 0,
  "Littre's hernia: a hernia containing Meckel's diverticulum. (Book p191)")
q(192, S3, "The investigation that confirms a bleeding Meckel's diverticulum is the:",
  ["Technetium-99m pertechnetate scan", "Plain X-ray abdomen",
   "Barium meal follow through", "CT enterography"], 0,
  "Confirmation of Dx: Tc99m pertechnetate scan. (Book p192)")
q(192, S3, "The technetium scan is sensitive for bleeding at a rate as low as:",
  ["0.1 ml/min", "1 ml/min", "10 ml/min", "100 ml/min"], 0,
  "Most sensitive for bleeds: 0.1 ml/min. (Book p192)")
q(192, S3, "The drawback of a technetium scan in bleeding is that it:",
  ["Cannot detect the site of the bleed", "Cannot be done in children",
   "Is very expensive", "Requires anaesthesia"], 0,
  "Drawback: cannot detect site of bleed. (Book p192)")
q(192, S3, "The m/c presentation of Meckel's diverticulum in adults is:",
  ["Obstruction", "Bleeding", "Perforation", "Malignancy"], 0,
  "Obstruction: m/c presentation in adults. (Book p192)")
q(192, S3, "Obstruction due to a Meckel's diverticulum in adults is usually due to:",
  ["Meckel's volvulus or intussusception", "A tight stricture", "Carcinoid tumour",
   "Adhesions"], 0,
  "Obstruction d/t Meckel's volvulus or intussusception (rare). (Book p192)")
q(192, S3, "The treatment of obstruction caused by a Meckel's diverticulum is:",
  ["Resection and anastomosis", "Conservative management", "Diverticulectomy alone",
   "Endoscopic reduction"], 0,
  "Obstruction: mx - resection + anastomosis. (Book p192)")
q(192, S3, "Malignancy in a Meckel's diverticulum is usually due to a:",
  ["Neuroendocrine (carcinoid) tumour", "Adenocarcinoma", "Lymphoma", "GIST"], 0,
  "Malignancy: d/t neuroendocrine tumor/carcinoid tumor (rare). (Book p192)")

# ---------------- p192 · ADHESIVE OBSTRUCTION ----------------
S4 = "Adhesive Obstruction"
q(192, S4, "The m/c cause of bowel obstruction overall is:",
  ["Adhesions", "Hernia", "Malignancy", "Volvulus"], 0,
  "Adhesive obstruction: m/c cause for bowel obstruction (overall). (Book p192)")
q(192, S4, "The m/c cause of adhesions is:",
  ["Previous surgery", "Tuberculosis", "Endometriosis", "Radiotherapy"], 0,
  "Causes of adhesions: post Sx (m/c). (Book p192)")
q(192, S4, "Non-surgical causes of adhesive obstruction include all EXCEPT:",
  ["Nephrolithiasis", "Tuberculosis", "Crohn's disease",
   "Pelvic inflammatory disease"], 0,
  "Non-surgical causes: tuberculosis, Crohn's disease, pelvic inflammatory disease (PID), endometriosis, post radiotherapy. (Book p192)")
q(192, S4, "The initial investigation in adhesive obstruction is:",
  ["X-ray abdomen (erect + supine)", "CECT abdomen", "USG abdomen", "MRI"], 0,
  "Initial: X-ray abdomen (erect + supine). (Book p192)")
q(192, S4, "The investigation of choice in adults with adhesive obstruction is:",
  ["CECT abdomen", "USG abdomen", "Barium study", "X-ray alone"], 0,
  "IOC: adults → CECT abdomen; children → USG abdomen. (Book p192)")
q(192, S4, "The investigation of choice in children with adhesive obstruction is:",
  ["USG abdomen", "CECT abdomen", "Barium study", "X-ray alone"], 0,
  "IOC: children → USG abdomen. (Book p192)")
q(192, S4, "Conservative management of adhesive obstruction is continued for:",
  ["48 to 72 hours", "6 hours", "12 hours", "1 week"], 0,
  "Conservative mx → 48 to 72 hours. (Book p192)")
q(192, S4, "The operative treatment of adhesive obstruction is:",
  ["Adhesiolysis", "Resection and anastomosis", "Bypass", "Stoma formation"], 0,
  "Surgery: adhesiolysis. (Book p192)")

# ---------------- p193 · MECONIUM ILEUS ----------------
S5 = "Meconium Ileus"
q(193, S5, "Meconium ileus is associated with:",
  ["Cystic fibrosis", "Hirschsprung's disease", "Down's syndrome",
   "Congenital hypothyroidism"], 0,
  "Meconium ileus: associated with cystic fibrosis. (Book p193)")
q(193, S5, "The differential diagnosis of meconium ileus is:",
  ["Hirschsprung's disease", "Duodenal atresia", "Intussusception",
   "Malrotation"], 0,
  "D/d: Hirschsprung's disease. (Book p193)")
q(193, S5, "The X-ray findings in meconium ileus include:",
  ["A soap-bubble appearance and a microcolon", "A double bubble",
   "A coffee bean sign", "Free gas under the diaphragm"], 0,
  "X-ray: soap-bubble appearance; microcolon. (Book p193)")
q(193, S5, "The confirmatory test for cystic fibrosis is the:",
  ["Sweat chloride test", "Stool trypsin test", "Serum immunoreactive trypsinogen",
   "Genetic testing for CFTR only"], 0,
  "Sweat chloride test: confirmatory for cystic fibrosis. (Book p193)")
q(193, S5, "In the sweat chloride test for cystic fibrosis:",
  ["Chloride levels in sweat are raised", "Sodium levels in sweat are low",
   "Chloride levels in sweat are low", "Sweat chloride is normal"], 0,
  "↑ Cl levels in sweat. (Book p193)")
q(193, S5, "The initial treatment of meconium ileus is a:",
  ["Gastrograffin enema", "Laparotomy", "Ileostomy", "Stool softeners"], 0,
  "Gastrograffin enema: water soluble. (Book p193)")
q(193, S5, "A Gastrograffin enema works in meconium ileus because it:",
  ["Mixes with meconium, forms a bulk and loosens the meconium",
   "Dissolves the meconium chemically", "Stimulates peristalsis",
   "Is hypertonic and draws in water"], 0,
  "Gastrograffin: mixes with meconium → forms a bulk → loosens the meconium. (Book p193)")
q(193, S5, "The surgery used if meconium ileus does not respond to an enema is:",
  ["Bishop-Koop surgery", "Ladd's procedure", "Duhamel pull-through",
   "Right hemicolectomy"], 0,
  "Bishop-Koop surgery: indicated if non-responsive to enema. (Book p193)")
q(193, S5, "In the Bishop-Koop procedure:",
  ["An ileostomy is made to manually irrigate the bowel",
   "The meconium is aspirated and the bowel closed primarily",
   "An end ileostomy is fashioned", "The ileum is resected"], 0,
  "Bishop-Koop: ileostomy made to manually irrigate the bowel with an end to side ileoileostomy. (Book p193)")

# ---------------- p193-194 · SMA SYNDROME ----------------
S6 = "Superior Mesenteric Artery (SMA) Syndrome"
q(193, S6, "SMA syndrome is also known as:",
  ["Cast syndrome or Wilkie syndrome", "Ogilvie's syndrome", "Ladd's syndrome",
   "Banti's syndrome"], 0,
  "SMA syndrome: AKA Cast syndrome/Wilkie syndrome. (Book p193)")
q(193, S6, "The obstruction in SMA syndrome is at the level of:",
  ["D3 (third part of the duodenum)", "D1", "D2", "D4"], 0,
  "SMA syndrome: D3 obstruction. (Book p193)")
q(193, S6, "In SMA syndrome the duodenum is compressed between the:",
  ["Superior mesenteric artery and the aorta", "Aorta and the vertebral column",
   "SMA and the left renal vein", "Coeliac trunk and the aorta"], 0,
  "Pathophysiology: SMA-aortic angle narrows and the duodenum is compressed - D3 obstruction. (Book p193)")
q(194, S6, "A clinical feature of SMA syndrome is:",
  ["Weight loss", "Haematemesis", "Jaundice", "Diarrhoea"], 0,
  "Clinical features: weight loss. (Book p194)")
q(194, S6, "The investigation of choice in SMA syndrome is:",
  ["CT angiography to measure the SMA-aortic angle", "Barium meal",
   "Upper GI endoscopy", "Plain X-ray"], 0,
  "IOC: CT angiography to measure SMA-aortic angle. (Book p194)")
q(194, S6, "The initial management of SMA syndrome is:",
  ["Weight gain with nutritional support", "Emergency duodenojejunostomy",
   "Total parenteral nutrition only", "Gastrojejunostomy"], 0,
  "Management: weight gain → nutrition. (Book p194)")
q(194, S6, "The Strong procedure for SMA syndrome is:",
  ["Duodenal derotation by cutting the ligament of Treitz",
   "A duodenojejunostomy", "A gastrojejunostomy", "Resection of D3"], 0,
  "Strong procedure: duodenal derotation (cutting the ligament of Treitz). (Book p194)")
q(194, S6, "A duodenojejunostomy in SMA syndrome is done to:",
  ["Bypass D3", "Bypass D1", "Relieve gastric outlet obstruction",
   "Prevent reflux"], 0,
  "Duodeno-jejunostomy: to bypass D3. (Book p194)")

# ---------------- p194 · LADD'S BAND ----------------
S7 = "Ladd's Bands"
q(194, S7, "Ladd's bands are:",
  ["The m/c intestinal malrotation abnormality", "Congenital duodenal webs",
   "Adhesions after appendicectomy", "Bands in the pelvis"], 0,
  "Ladd's band: m/c intestinal malrotation abnormality. (Book p194)")
q(194, S7, "Ladd's bands extend from:",
  ["The right hypochondrium to the caecum", "The left hypochondrium to the sigmoid",
   "The duodenum to the liver", "The stomach to the transverse colon"], 0,
  "Extends from Rt. hypochondrium → caecum. (Book p194)")
q(194, S7, "Ladd's bands cause obstruction by compressing the:",
  ["Duodenum", "Jejunum", "Ileum", "Stomach"], 0,
  "Compresses duodenum. (Book p194)")
q(194, S7, "The clinical feature of obstruction by Ladd's bands is:",
  ["Bilious vomiting", "Non-bilious projectile vomiting", "Haematemesis",
   "Constipation only"], 0,
  "C/F: bilious vomiting. (Book p194)")
q(194, S7, "The investigation of choice for Ladd's bands is:",
  ["CECT abdomen", "X-ray abdomen", "USG abdomen", "Contrast enema"], 0,
  "IOC: CECT abdomen. (Book p194)")
q(194, S7, "The treatment of Ladd's bands is:",
  ["Excision of the band (Ladd's procedure)", "Duodenojejunostomy",
   "Gastrojejunostomy", "Conservative management"], 0,
  "Mx: excision of Ladd's band (Ladd's procedure). (Book p194)")

# ---------------- p194 · PARALYTIC ILEUS ----------------
S8 = "Paralytic Ileus"
q(194, S8, "Paralytic ileus is:",
  ["Non-contraction of the bowel (adynamic obstruction)",
   "A mechanical obstruction", "Twisting of the bowel",
   "Telescoping of the bowel"], 0,
  "Paralytic ileus: non-contraction of the bowel. (Book p194)")
q(194, S8, "Surgical causes of paralytic ileus include all EXCEPT:",
  ["Hypertension", "Bowel handling", "Anastomosis", "Abscess or pus"], 0,
  "Surgical causes: bowel handling; anastomosis; abscess/pus. (Book p194)")
q(194, S8, "The m/c non-surgical (metabolic) cause of prolonged paralytic ileus is:",
  ["Hypokalemia", "Hypernatremia", "Hypercalcemia", "Hypoglycaemia"], 0,
  "Non-surgical causes: anaesthesia, hypothyroidism, hypokalemia (m/c), uraemia, hypothermia. (Book p194)")
q(194, S8, "Non-surgical causes of paralytic ileus include all EXCEPT:",
  ["Hypermagnesemia", "Anaesthesia", "Hypothyroidism", "Uraemia"], 0,
  "Non-surgical causes: anaesthesia, hypothyroidism, hypokalemia (m/c), uraemia, hypothermia. (Book p194)")
q(194, S8, "A CT scan in paralytic ileus is done to:",
  ["Rule out other (mechanical) causes", "Confirm the diagnosis of ileus",
   "Measure the bowel diameter only", "Plan the stoma site"], 0,
  "Investigation: CECT to r/o other causes. (Book p194)")
q(194, S8, "The management of paralytic ileus is:",
  ["Supportive with IV fluids", "Emergency laparotomy", "Laparoscopic adhesiolysis",
   "Nasogastric decompression alone"], 0,
  "Mx: supportive + IV fluids. (Book p194)")
q(194, S8, "A prolonged paralytic ileus is managed with:",
  ["Total parenteral nutrition (TPN)", "Early enteral feeding",
   "Intravenous antibiotics", "Prokinetic drugs alone"], 0,
  "Prolonged ileus → total parenteral nutrition (TPN). (Book p194)")

# ---------------- p194-195 · HIRSCHSPRUNG'S ----------------
S9 = "Hirschsprung's Disease"
q(194, S9, "Hirschsprung's disease is also known as:",
  ["Congenital megacolon", "Acquired megacolon", "Toxic megacolon", "Microcolon"], 0,
  "Hirschsprung's disease: AKA congenital megacolon. (Book p194)")
q(194, S9, "Hirschsprung's disease is characterised by the absence of ganglion cells in the:",
  ["Auerbach's/myenteric plexus of the large bowel",
   "Meissner's plexus of the small bowel", "Submucosa of the stomach",
   "Myenteric plexus of the oesophagus"], 0,
  "Absence of ganglion cells in Auerbach/myenteric plexus of large bowel. (Book p194)")
q(194, S9, "Hirschsprung's disease is a neurocristopathy because the affected cells are derived from the:",
  ["Neural crest", "Endoderm", "Mesoderm", "Notochord"], 0,
  "Neural crest derived cells → neurocristopathy. (Book p194)")
q(195, S9, "Hirschsprung's disease is associated with:",
  ["Down's syndrome and MEN 2A/2B", "Turner's syndrome", "Klinefelter's syndrome",
   "Marfan's syndrome"], 0,
  "Associations: Down's syndrome, MEN 2A & 2B. (Book p195)")
q(195, S9, "Clinical features of Hirschsprung's disease include:",
  ["Abdominal distension, passage of meconium on DRE and constipation in the young child",
   "Bilious vomiting since birth", "Blood and mucus in the stools",
   "Projectile non-bilious vomiting"], 0,
  "Clinical features: abdominal distension; on DRE → passes meconium; young child - constipation. (Book p195)")
q(195, S9, "On rectal examination in Hirschsprung's disease the finger:",
  ["Is followed by the passage of meconium", "Finds an impacted mass only",
   "Finds a stricture", "Finds a normal rectum with no stool"], 0,
  "On DRE → passes meconium. (Book p195)")
q(195, S9, "Histopathology of the affected segment in Hirschsprung's disease shows:",
  ["Loss of ganglion cells and hypertrophied nerve trunks",
   "Increased ganglion cells", "Normal ganglia", "Absent smooth muscle"], 0,
  "Findings: loss of ganglion cells; hypertrophied nerve trunks. (Book p195)")
q(195, S9, "The immunohistochemical marker positive in Hirschsprung's disease is:",
  ["Acetylcholinesterase", "S-100", "CD117", "Chromogranin"], 0,
  "IHC → acetylcholinesterase (+). (Book p195)")
q(195, S9, "A barium enema in Hirschsprung's disease shows:",
  ["Three zones - dilated, transitional and constricted",
   "A microcolon", "A soap-bubble appearance", "A coffee bean sign"], 0,
  "Barium enema - 3 zones: dilated, transitional, constricted. (Book p195)")
q(195, S9, "In Hirschsprung's disease the zones that lack ganglion cells are the:",
  ["Transitional and constricted zones", "Dilated zone only",
   "Dilated and transitional zones", "All three zones"], 0,
  "Transitional and constricted zones lack ganglion cells. (Book p195)")

# ---------------- p195 · HIRSCHSPRUNG'S MANAGEMENT ----------------
S10 = "Management of Hirschsprung's Disease"
q(195, S10, "In severe/extensive Hirschsprung's disease, surgery is done in:",
  ["Two stages - a colostomy first, then definitive surgery",
   "A single stage only", "Three stages", "Four stages"], 0,
  "Two stages (severe extension): 1st stage → colostomy; 2nd stage → definitive Sx. (Book p195)")
q(195, S10, "In the two-stage management of Hirschsprung's disease, the first stage is a:",
  ["Colostomy", "Ileostomy", "Pull-through", "Resection and anastomosis"], 0,
  "1st stage → colostomy. (Book p195)")
q(195, S10, "Principles of surgery for Hirschsprung's disease include all EXCEPT:",
  ["Resection of the entire colon always", "Bypass of the abnormal segment",
   "Resection and anastomosis",
   "Intra-operative frozen section to confirm the margin of resection"], 0,
  "Principles of Sx: bypass abnormal segment; resection and anastomosis; intra-operative frozen section done to confirm margin of resection. (Book p195)")
q(195, S10, "An intra-operative frozen section in surgery for Hirschsprung's disease is used to:",
  ["Confirm the margin of resection", "Confirm the diagnosis of cancer",
   "Look for ectopic mucosa", "Assess vascularity"], 0,
  "Intra-operative frozen section done to confirm margin of resection. (Book p195)")

# ---------------- p195 · MESENTERIC ISCHEMIA: VENOUS ----------------
S11 = "Mesenteric Ischemia: Venous and Non-occlusive Types"
q(195, S11, "The thumbprinting sign on imaging is seen in:",
  ["Bowel ischemia", "Bowel obstruction", "Intussusception", "Volvulus"], 0,
  "Thumbprinting sign - bowel ischemia. (Book p195)")
q(195, S11, "Venous mesenteric thrombosis is related to:",
  ["Virchow's triad - stasis, endothelial injury and a hypercoagulable state",
   "Atherosclerosis", "Atrial fibrillation", "Polycythaemia alone"], 0,
  "Venous: Virchow's triad - stasis, endothelial injury, hypercoagulable state. (Book p195)")
q(196, S11, "The treatment of venous mesenteric thrombosis is:",
  ["Anticoagulation", "Embolectomy", "Bypass grafting", "Bowel resection alone"], 0,
  "Venous: mx - anticoagulation. (Book p196)")
q(195, S11, "Non-occlusive mesenteric ischemia due to cardiac failure is treated by:",
  ["Correction of cardiac failure", "Embolectomy", "Bypass grafting",
   "Immediate laparotomy"], 0,
  "Non-occlusive mesenteric ischemia: mx - correction of CHF. (Book p195)")

# ---------------- p196 · SMA EMBOLISM ----------------
S12 = "Arterial Mesenteric Ischemia: SMA Embolism"
q(196, S12, "The source of an embolus blocking the superior mesenteric artery is usually the:",
  ["Heart - atrial fibrillation or ischaemic heart disease",
   "Atherosclerotic plaque in the aorta", "Deep veins of the leg",
   "Carotid artery"], 0,
  "Source of embolus → heart (atrial fibrillation/IHD) → blocks SMA. (Book p196)")
q(196, S12, "The clinical feature of acute SMA embolism is:",
  ["Severe abdominal pain (bowel attack)", "Painless jaundice",
   "Chronic diarrhoea", "Haematemesis"], 0,
  "C/F: severe abdominal pain (bowel attack). (Book p196)")
q(196, S12, "The investigation of choice in acute SMA embolism is:",
  ["CT angiography", "Plain X-ray abdomen", "USG abdomen", "Upper GI endoscopy"], 0,
  "IOC: CT angiography. (Book p196)")
q(196, S12, "The management of acute SMA embolism is:",
  ["Exploration", "Conservative management", "Anticoagulation alone",
   "Thrombolysis alone"], 0,
  "Mx: exploration. (Book p196)")
q(196, S12, "SMA embolism is a common cause of:",
  ["Short bowel syndrome", "Long bowel syndrome", "Blind loop syndrome",
   "Dumping syndrome"], 0,
  "Note: SMA embolism - m/c cause of short bowel syndrome (SBS). (Book p196)")
q(196, S12, "In acute SMA embolism, if the patient is operated on within 6-8 hours:",
  ["The bowel is viable and embolectomy is done",
   "The bowel is gangrenous and needs resection",
   "No intervention is needed", "Anticoagulation is started"], 0,
  "Within 6-8 hours: bowel viable → embolectomy. (Book p196)")
q(196, S12, "In acute SMA embolism presenting after 6-8 hours:",
  ["The bowel is gangrenous and needs resection",
   "Embolectomy alone is sufficient", "The bowel is still viable",
   "Conservative management is preferred"], 0,
  ">6-8 hours: gangrenous bowel → bowel resection → short bowel syndrome (SBS). (Book p196)")

# ---------------- p196 · AMAT ----------------
S13 = "Acute Mesenteric Artery Thrombosis (AMAT)"
q(196, S13, "Acute mesenteric artery thrombosis is due to:",
  ["Atherosclerosis", "An embolus from the heart", "Fibromuscular dysplasia",
   "Vasculitis"], 0,
  "AMAT - cause: atherosclerosis. (Book p196)")
q(196, S13, "The vessel involved in acute mesenteric artery thrombosis is the:",
  ["Superior mesenteric artery", "Inferior mesenteric artery", "Coeliac trunk",
   "Aorta"], 0,
  "AMAT - site: SMA. (Book p196)")
q(196, S13, "The pain of chronic mesenteric ischemia (bowel angina) comes on:",
  ["20-30 minutes after food and lasts 2-3 hours",
   "Immediately after food and lasts 10 minutes",
   "Only at night", "Only on fasting"], 0,
  "Post-prandial abdominal pain (20-30 mins after food; lasts 2-3 hrs): bowel angina. (Book p196)")
q(196, S13, "Weight loss in chronic mesenteric ischemia is due to:",
  ["Reduced food consumption because of fear of pain", "Malabsorption",
   "Hyperthyroidism", "Malignancy"], 0,
  "↓ food consumption → weight loss (D/d: cancer). (Book p196)")
q(196, S13, "The investigation of choice in acute mesenteric artery thrombosis is:",
  ["CECT/CT angiography", "Plain X-ray", "USG abdomen", "Diagnostic laparoscopy"], 0,
  "IOC: CECT/CT angiography. (Book p196)")
q(196, S13, "The definitive treatment of acute mesenteric artery thrombosis is:",
  ["Bypass grafting", "Embolectomy", "Anticoagulation alone", "Bowel resection"], 0,
  "Mx: bypass grafting. (Book p196)")

# ---------------- p196 · OGILVIE'S ----------------
S14 = "Colonic Pseudo-obstruction (Ogilvie's Syndrome)"
q(196, S14, "Colonic pseudo-obstruction is also known as:",
  ["Ogilvie's syndrome", "Wilkie's syndrome", "Cast syndrome",
   "Banti's syndrome"], 0,
  "Colonic pseudo-obstruction: AKA Ogilvie's syndrome. (Book p196)")
q(196, S14, "Associations of Ogilvie's syndrome include all EXCEPT:",
  ["Inflammatory bowel disease", "Psychiatric medications",
   "Neurological disorders such as Alzheimer's and Parkinson's disease",
   "Retroperitoneal haematoma after trauma or vertebral fracture"], 0,
  "Associations: psychiatric medications; neurological disorders (Alzheimer's/Parkinson's); post retroperitoneal hematoma (trauma/vertebral fracture) → compresses splanchnic nerves. (Book p196)")
q(196, S14, "In Ogilvie's syndrome, bowel sounds are:",
  ["Heard, because the small intestine is normal", "Absent throughout",
   "Hyperdynamic", "High pitched and tinkling"], 0,
  "Clinical features: distension and obstipation; bowel sounds heard (small intestine normal). (Book p196)")
q(196, S14, "In Ogilvie's syndrome a CECT abdomen is done to:",
  ["Rule out a dynamic (mechanical) obstruction", "Confirm the diagnosis",
   "Assess the colon length", "Look for free gas"], 0,
  "Investigations: rule out dynamic obstruction → CECT abdomen. (Book p196)")
q(196, S14, "The drug used to treat Ogilvie's syndrome is:",
  ["IV neostigmine (Catchpole regime)", "IV erythromycin", "Oral lactulose",
   "IV metoclopramide"], 0,
  "Mx: IV neostigmine (Catchpole regime). (Book p196)")
q(196, S14, "Meteorism refers to:",
  ["Colonic distension 3-4 days after retroperitoneal trauma",
   "Gastric distension after surgery", "Dilatation of the oesophagus",
   "A distended bladder"], 0,
  "Note: meteorism - colonic distension 3-4 days after retroperitoneal trauma. (Book p196)")

# ---------------- units ----------------
def sec_ids(*labels):
    return [x["id"] for x in Q if x["sec"] in labels]
def first_page(label):
    for x in Q:
        if x["sec"] == label:
            return x["page"]
    return 0

UNIT_DEFS = [
    (S1, "Meckel's diverticulum is a true diverticulum - all layers are present - and it obeys the rule of two: two per cent of people, two inches long, two feet from the ileocaecal junction. Heterotopic mucosa, gastric more often than pancreatic, is what makes it bleed."),
    (S2, "Most are silent and found by accident. A broad-based one can be left alone, but a narrow base means trouble later - obstruction or inflammation - so take it out. When it inflames it apes acute appendicitis, with peri-umbilical pain shifting to the right iliac fossa, and the treatment is diverticulectomy."),
    (S3, "Perforation needs diverticulectomy or resection and anastomosis, and a Meckel's caught in a hernia sac is Littre's hernia. Bleeding is confirmed by a technetium pertechnetate scan, sensitive down to 0.1 ml/min but blind as to where the blood is coming from. In adults obstruction is the commonest presentation - usually from a Meckel's volvulus or intussusception, treated by resection - and rarely a carcinoid tumour turns up in it."),
    (S4, "Adhesions are the commonest cause of bowel obstruction overall, and previous surgery is the commonest cause of adhesions - with tuberculosis, Crohn's, pelvic inflammatory disease, endometriosis and radiotherapy making up the non-surgical list. Film first, then CECT in adults or ultrasound in children, and give conservative treatment 48 to 72 hours before resorting to adhesiolysis."),
    (S5, "Meconium ileus is cystic fibrosis presenting in the newborn, and Hirschsprung's is the differential. The film shows a soap-bubble pattern and a microcolon, and the diagnosis is confirmed by a sweat chloride test with raised chloride. A water soluble Gastrograffin enema mixes with the meconium, bulks it and loosens it; if that fails, the Bishop-Koop operation creates an ileostomy through which the bowel can be irrigated by hand."),
    (S6, "Cast or Wilkie syndrome is the duodenum nipped between the superior mesenteric artery and the aorta, obstructing D3 and wasting the patient. CT angiography measures the SMA-aortic angle. Build the patient up with nutrition first; if that fails, the Strong procedure de-rotates the duodenum by dividing the ligament of Treitz, or a duodenojejunostomy bypasses D3."),
    (S7, "Ladd's bands are the commonest malrotation abnormality, running from the right hypochondrium to the caecum and pressing on the duodenum. The infant vomits bile, CECT shows it, and dividing the band - Ladd's procedure - is the cure."),
    (S8, "Paralytic ileus is the bowel that will not contract: after handling, anastomosis or abscess, or from anaesthesia, hypothyroidism, uraemia, hypothermia and above all hypokalemia. It looks like obstruction, so CECT is done to rule the mechanical causes out. Treatment is supportive - fluids, and TPN if it drags on."),
    (S9, "Congenital megacolon is the absence of ganglion cells in the myenteric plexus of the large bowel, a failure of neural crest migration and therefore a neurocristopathy, linked with Down's syndrome and MEN 2A/2B. The child is distended, the examining finger releases a gush of meconium, and the older child is simply constipated. Biopsy shows no ganglion cells but hypertrophied nerve trunks and positive acetylcholinesterase staining, and the barium enema shows the three zones - dilated, transitional and constricted - of which the last two are aganglionic."),
    (S10, "Limited disease is dealt with in one stage, but extensive disease is staged: a colostomy first, definitive surgery later. The principles are to bypass or resect the abnormal segment and anastomose, using intra-operative frozen section to be certain the proximal margin contains ganglion cells."),
    (S11, "Thumbprinting on the film means the bowel is ischemic. Venous thrombosis follows Virchow's triad - stasis, endothelial injury, hypercoagulability - and is treated with anticoagulation; the non-occlusive form that accompanies cardiac failure is treated by correcting the failure."),
    (S12, "An embolus from a fibrillating or ischaemic heart lodges in the SMA and produces the classic bowel attack - severe pain out of proportion to findings. CT angiography confirms it and the patient goes to theatre. Time decides the outcome: within 6-8 hours the bowel is viable and an embolectomy saves it, after that the bowel is gangrenous, resection follows, and short bowel syndrome is the legacy - which is why SMA embolism is the commonest cause of SBS."),
    (S13, "Thrombosis is an atherosclerotic disease of the SMA and announces itself more slowly as bowel angina - pain 20-30 minutes after eating that lasts two to three hours - so the patient eats less and loses weight, mimicking cancer. CECT or CT angiography shows it, and bypass grafting is the treatment."),
    (S14, "Ogilvie's syndrome is a colon that behaves as if obstructed without being obstructed: psychiatric drugs, neurological disease and retroperitoneal haematoma compressing the splanchnic nerves are the associations. The patient is distended and constipated but bowel sounds are still heard because the small bowel works normally. Exclude a mechanical block with CECT and give IV neostigmine by the Catchpole regime - and remember meteorism, the colonic distension that appears three or four days after retroperitoneal trauma."),
]

UNITS = []
for i, (title, guide) in enumerate(UNIT_DEFS, 1):
    UNITS.append({"id": f"SURG-U28-{i}", "ch": 28, "n": i, "title": title,
                  "sec": f"{title} · p{first_page(title)}",
                  "qs": sec_ids(title), "guide": guide})

covered = [i for u in UNITS for i in u["qs"]]
assert covered == [x["id"] for x in Q], "units must cover questions in order"

data = {"questions": Q, "units": UNITS}
with open("data/ch28.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
print(f"ch28: {len(Q)} questions, {len(UNITS)} units")
