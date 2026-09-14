#!/usr/bin/env python3
"""Build data/ch21.json for PULSE Surgery ch21 (Esophagus : Part 3, book p145-149)."""
import json

Q = []
def q(page, sec, text, opts, ans, exp):
    Q.append({"id": f"SURG-C21-{len(Q)+1:03d}", "sec": sec, "page": page,
              "q": text, "opts": opts, "ans": ans, "exp": exp})

# ---------------- p145 · TYPES & RISK FACTORS ----------------
S1 = "Esophageal Cancer: Types & Risk Factors"
q(145, S1, "Overall, the m/c esophageal cancer worldwide is:",
  ["Squamous cell carcinoma", "Adenocarcinoma", "Leiomyosarcoma", "Melanoma"], 0,
  "Types: squamous cell carcinoma (overall m/c) versus adenocarcinoma. (Book p145)")
q(145, S1, "The m/c esophageal cancer in the western world is:",
  ["Adenocarcinoma", "Squamous cell carcinoma", "Small cell carcinoma", "Lymphoma"], 0,
  "Adenocarcinoma: m/c in the western world. (Book p145)")
q(145, S1, "Squamous cell carcinoma of the esophagus is typically located in the:",
  ["Middle one third", "Lower one third", "Upper one third", "Whole esophagus"], 0,
  "SCC: middle 1/3rd; adenocarcinoma: lower 1/3rd. (Book p145)")
q(145, S1, "Adenocarcinoma of the esophagus is typically located in the:",
  ["Lower one third", "Middle one third", "Upper one third", "Cervical esophagus"], 0,
  "Adenocarcinoma: lower 1/3rd of the esophagus. (Book p145)")
q(145, S1, "The risk factors shared by both squamous carcinoma and adenocarcinoma of the esophagus include:",
  ["Smoking and alcohol", "Barrett's esophagus alone", "Obesity alone", "Gastroesophageal reflux alone"], 0,
  "Risk factors: smoking (++) and alcohol (++) are listed for esophageal cancer. (Book p145)")
q(145, S1, "N-nitroso containing foods implicated in esophageal cancer include:",
  ["Pickled vegetables", "Fresh citrus fruits", "Milk products", "Rice"], 0,
  "N-nitroso-containing food (e.g. pickled vegetables) is a risk factor. (Book p145)")
q(145, S1, "Drinking yerba mate is a risk factor for:",
  ["Esophageal cancer", "Gastric lymphoma", "Pancreatic cancer", "Colonic polyps"], 0,
  "Drinking yerba mate: risk factor for esophageal cancer. (Book p145)")
q(145, S1, "Plummer-Vinson syndrome is also known as:",
  ["Paterson-Kelly-Brown syndrome", "Zollinger-Ellison syndrome",
   "Mallory-Weiss syndrome", "Peutz-Jeghers syndrome"], 0,
  "Plummer-Vinson syndrome (Paterson-Kelly-Brown syndrome): risk factor. (Book p145)")
q(145, S1, "Tylosis, a risk factor for esophageal cancer, is:",
  ["Palmar-plantar keratoderma", "Palmar erythema", "Clubbing", "Xanthelasma"], 0,
  "Tylosis: palmar-plantar keratoderma. (Book p145)")
q(145, S1, "Scleroderma (CREST syndrome) is a risk factor for:",
  ["Esophageal cancer", "Carcinoid tumor", "Achalasia only", "Zenker's diverticulum"], 0,
  "Scleroderma (CREST syndrome): risk factor for esophageal cancer. (Book p145)")
q(145, S1, "The strongest risk factor listed for adenocarcinoma of the esophagus is:",
  ["Barrett's esophagus", "Smoking", "Alcohol", "Betel nut chewing"], 0,
  "Barrett's esophagus: ++++ - the strongest risk factor for adenocarcinoma. (Book p145)")
q(145, S1, "Gastro-esophageal reflux disease as a risk factor for adenocarcinoma is graded:",
  ["+++", "+", "-", "Not a risk factor"], 0,
  "Gastro-oesophageal reflux: +++ for adenocarcinoma. (Book p145)")
q(145, S1, "Obesity is a risk factor predominantly for:",
  ["Adenocarcinoma of the esophagus", "Squamous carcinoma of the esophagus",
   "Leiomyoma of the esophagus", "Esophageal web"], 0,
  "Obesity: negative for SCC, ++ for adenocarcinoma. (Book p145)")
q(145, S1, "A lye corrosive stricture predisposes to:",
  ["Squamous cell carcinoma", "Adenocarcinoma", "Leiomyoma", "Barrett's esophagus"], 0,
  "Lye corrosive stricture: risk factor for esophageal (squamous) cancer. (Book p145)")
q(145, S1, "A history of upper aerodigestive malignancy carries which grade of risk?",
  ["+++", "+", "-", "No risk"], 0,
  "History of upper aerodigestive malignancy: +++ risk. (Book p145)")

# ---------------- p146 · CLINICAL FEATURES & INVESTIGATIONS ----------------
S2 = "Esophageal Cancer: Features & Investigations"
q(146, S2, "The earliest and m/c symptom of esophageal cancer is:",
  ["Progressive dysphagia (solids > liquids)", "Hematemesis", "Hoarseness", "Cough"], 0,
  "Earliest / m/c symptom: progressive dysphagia (solids > liquids). (Book p146)")
q(146, S2, "Weight loss in esophageal cancer indicates:",
  ["Advanced disease", "Early curable disease", "Benign stricture", "Co-existent achalasia"], 0,
  "Clinical features: progressive dysphagia and weight loss. (Book p146)")
q(146, S2, "Hoarseness in esophageal cancer is due to involvement of the:",
  ["Left recurrent laryngeal nerve", "Right recurrent laryngeal nerve",
   "Vagus at the diaphragm", "Phrenic nerve"], 0,
  "Signs of advanced disease: left RLN involvement causing hoarseness. (Book p146)")
q(146, S2, "Chronic cough in esophageal cancer may indicate:",
  ["A malignant fistula with the trachea", "Aspiration of a Zenker's diverticulum",
   "Bronchiectasis", "Cardiac failure"], 0,
  "Signs of advanced disease: malignant fistula with the trachea - chronic cough. (Book p146)")
q(146, S2, "The investigation of choice to diagnose esophageal cancer is:",
  ["Endoscopic biopsy", "Barium swallow", "PET-CT", "Endoscopic ultrasound"], 0,
  "IOC to diagnose: endoscopic biopsy. (Book p146)")
q(146, S2, "The investigation of choice for overall staging of esophageal cancer is:",
  ["PET-CT", "Endoscopic biopsy", "Barium swallow", "CT chest alone"], 0,
  "IOC for overall staging: PET-CT (18-FDG compound, half-life 110 mins). (Book p146)")
q(146, S2, "The investigation of choice for T and N staging of esophageal cancer is:",
  ["Endoscopic ultrasound (EUS)", "PET-CT", "Barium swallow", "Bronchoscopy"], 0,
  "IOC for T and N staging: EUS (endoscopic ultrasound). (Book p146)")
q(146, S2, "The barium swallow appearance of esophageal cancer is:",
  ["Rat tail / apple core appearance", "Bird beak appearance", "Corkscrew appearance",
   "Punched out appearance"], 0,
  "Barium swallow: rat tail / apple core appearance with shouldering and irregular margins. (Book p146)")

# ---------------- p147 · TNM CLASSIFICATION & SIEWERT ----------------
S3 = "Esophageal Cancer: TNM & Siewert Classification"
q(147, S3, "Tis in esophageal cancer denotes:",
  ["High grade dysplasia", "Invasion into the submucosa", "Invasion into muscularis propria",
   "Invasion into adventitia"], 0,
  "T status: Tis = high-grade dysplasia. (Book p147)")
q(147, S3, "T1 esophageal cancer means invasion into:",
  ["Lamina propria, muscularis mucosae or submucosa", "Muscularis propria",
   "Adventitia", "Adjacent organs"], 0,
  "T1: invasion into lamina propria, muscularis mucosae or submucosa. (Book p147)")
q(147, S3, "T2 esophageal cancer invades the:",
  ["Muscularis propria", "Adventitia", "Submucosa", "Aorta"], 0,
  "T2: invasion into muscularis propria. (Book p147)")
q(147, S3, "T3 esophageal cancer invades the:",
  ["Adventitia", "Muscularis propria", "Pleura", "Aorta"], 0,
  "T3: invasion into adventitia. (Book p147)")
q(147, S3, "T4a esophageal cancer invades:",
  ["Resectable adjacent structures - pleura, pericardium, diaphragm",
   "Unresectable structures such as the aorta",
   "The muscularis propria", "The submucosa"], 0,
  "T4a: invades resectable adjacent structures (pleura, pericardium, diaphragm). (Book p147)")
q(147, S3, "T4b esophageal cancer invades:",
  ["Unresectable adjacent structures - aorta, vertebral body, trachea",
   "The pleura only", "The pericardium only", "The submucosa"], 0,
  "T4b: invades unresectable adjacent structures (aorta, vertebral body, trachea). (Book p147)")
q(147, S3, "N1 nodal status in esophageal cancer means:",
  ["1 to 2 positive regional lymph nodes", "3 to 6 positive nodes",
   "7 or more positive nodes", "No nodes involved"], 0,
  "N status: N1 = 1 to 2 positive regional lymph nodes. (Book p147)")
q(147, S3, "N2 nodal status in esophageal cancer means:",
  ["3 to 6 positive regional lymph nodes", "1 to 2 positive nodes",
   "7 or more positive nodes", "No nodes involved"], 0,
  "N2: 3 to 6 positive regional lymph nodes. (Book p147)")
q(147, S3, "N3 nodal status in esophageal cancer means:",
  ["7 or more positive regional lymph nodes", "3 to 6 positive nodes",
   "1 to 2 positive nodes", "Positive coeliac nodes only"], 0,
  "N3: 7 or more positive regional lymph nodes. (Book p147)")
q(147, S3, "The m/c site of distant metastases in esophageal cancer is:",
  ["Liver", "Brain", "Bone", "Spleen"], 0,
  "M1: distant metastases, m/c site is the liver. (Book p147)")
q(147, S3, "The Siewert classification is used for:",
  ["Gastro-esophageal junction tumors", "Cervical esophageal tumors",
   "Carcinoid tumors", "Zenker's diverticulum"], 0,
  "Siewert classification for GE junction tumors. (Book p147)")
q(147, S3, "Siewert type I and type II junction tumors are managed as:",
  ["Esophageal cancer", "Gastric cancer", "Lymphoma", "Benign tumors"], 0,
  "Type I and II are managed as esophageal cancer. (Book p147)")
q(147, S3, "Siewert type III junction tumors are managed as:",
  ["Gastric cancer", "Esophageal cancer", "Pancreatic cancer", "Mediastinal tumors"], 0,
  "Type III is managed as gastric cancer. (Book p147)")

# ---------------- p147 · MANAGEMENT ----------------
S4 = "Management of Esophageal Cancer"
q(147, S4, "T1a esophageal cancer (above the submucosa, metastasis rare) is treated by:",
  ["Endoscopic mucosal resection (EMR)", "Esophagectomy", "Chemoradiotherapy",
   "Observation"], 0,
  "T1a: above submucosa, metastasis rare - endoscopic mucosal resection (EMR). (Book p147)")
q(147, S4, "T1b N0 / T2 N0 esophageal cancer is treated by:",
  ["Esophagectomy", "Endoscopic mucosal resection", "Chemotherapy alone", "Radiotherapy alone"], 0,
  "T1b N0 / T2 N0: esophagectomy. (Book p147)")
q(147, S4, "T3 / T4 (advanced stage) esophageal cancer is treated by:",
  ["Chemotherapy and radiotherapy (neoadjuvant) followed by surgery",
   "Endoscopic mucosal resection", "Surgery alone", "Nothing"], 0,
  "T3/T4: advanced stage - chemotherapy + radiotherapy (neoadjuvant therapy) followed by surgery. (Book p147)")
q(147, S4, "Cervical esophageal tumors are best treated with:",
  ["Definitive chemoradiotherapy (preserves the larynx)", "Trans-hiatal esophagectomy",
   "Endoscopic mucosal resection", "Laser ablation"], 0,
  "Cervical esophageal tumors: definitive chemoradiotherapy (preserves the larynx). (Book p147)")
q(147, S4, "R0 resection means:",
  ["Microscopic freedom from cancer", "Microscopic disease left behind",
   "Gross disease present", "Inoperable disease"], 0,
  "Margins: R0 = microscopic freedom from cancer; R1 = microscopic disease left behind; R2 = gross disease present. (Book p147)")
q(147, S4, "R1 resection means:",
  ["Microscopic disease left behind", "Microscopic freedom from cancer",
   "Gross disease present", "No residual disease"], 0,
  "R1: microscopic disease left behind. (Book p147)")
q(147, S4, "R2 resection means:",
  ["Gross disease present", "Microscopic freedom from cancer",
   "Microscopic disease left behind", "Complete response to chemoradiotherapy"], 0,
  "R2: gross disease (+). (Book p147)")
q(147, S4, "The proximal margin recommended during esophagectomy is:",
  ["10 cm", "5 cm", "2 cm", "1 cm"], 0,
  "Margins: proximal margin 10 cm and distal margin 5 cm (due to lymphatic skip lesions). (Book p147)")
q(147, S4, "The distal margin of 5 cm in esophagectomy is required because of:",
  ["Lymphatic skip lesions", "Blood supply of the stomach", "Risk of chylothorax",
   "Postoperative reflux"], 0,
  "Distal margin 5 cm: due to lymphatic skip lesions. (Book p147)")

# ---------------- p148 · TYPES OF ESOPHAGECTOMY ----------------
S5 = "Types of Esophagectomy"
q(148, S5, "McKeown's esophagectomy is a:",
  ["Three field esophagectomy", "Two field trans-thoracic esophagectomy",
   "Trans-hiatal esophagectomy", "Endoscopic resection"], 0,
  "Types: McKeown's (3 field esophagectomy), trans-hiatal (Orringer) and Ivor Lewis. (Book p148)")
q(148, S5, "The best operation for lymph node clearance in esophageal cancer is:",
  ["McKeown's three field esophagectomy", "Trans-hiatal esophagectomy",
   "Ivor Lewis esophagectomy", "Endoscopic mucosal resection"], 0,
  "McKeown's (3 field esophagectomy): best for lymph node clearance. (Book p148)")
q(148, S5, "McKeown's esophagectomy is suited to tumors of the:",
  ["Middle one third", "Lower one third", "Cervical esophagus", "Gastric cardia"], 0,
  "McKeown's: middle 1/3rd tumors (best for LN clearance). (Book p148)")
q(148, S5, "The incisions used in McKeown's esophagectomy are:",
  ["Midline abdomen, right thorax and left side of neck", "Midline abdomen and left neck only",
   "Midline abdomen and right thorax only", "Left thoracotomy alone"], 0,
  "McKeown's: midline abdomen, right thorax, left side of neck. (Book p148)")
q(148, S5, "Trans-hiatal (Orringer) esophagectomy is suited to tumors of the:",
  ["Lower one third", "Middle one third", "Upper one third", "Cervical esophagus"], 0,
  "Trans-hiatal (Orringer): lower 1/3rd. (Book p148)")
q(148, S5, "The incisions used in a trans-hiatal (Orringer) esophagectomy are:",
  ["Midline abdomen and left side of neck", "Midline abdomen and right thorax",
   "Right thorax and left neck", "Three separate incisions"], 0,
  "Trans-hiatal: midline abdomen and left neck. (Book p148)")
q(148, S5, "The Ivor Lewis esophagectomy is suited to tumors of the:",
  ["Middle one third", "Lower one third", "Cervical esophagus", "Cardia"], 0,
  "Ivor Lewis: middle 1/3rd. (Book p148)")
q(148, S5, "The site of anastomosis in an Ivor Lewis esophagectomy is the:",
  ["Thorax", "Neck", "Abdomen", "Chest wall"], 0,
  "Ivor Lewis: anastomosis in the thorax. (Book p148)")
q(148, S5, "The site of anastomosis in McKeown's and trans-hiatal esophagectomy is the:",
  ["Neck", "Thorax", "Abdomen", "Mediastinum"], 0,
  "McKeown's and trans-hiatal: anastomosis in the neck. (Book p148)")
q(148, S5, "An anastomotic leak after esophagectomy leads to:",
  ["Mediastinitis - the m/c cause of death", "Chylothorax", "Stricture", "Dumping syndrome"], 0,
  "Anastomotic leak leads to mediastinitis, which is the m/c cause of death. (Book p148)")
q(148, S5, "The m/c long term complication after esophagectomy is:",
  ["Stricture", "Anastomotic leak", "Chylothorax", "Recurrent laryngeal nerve palsy"], 0,
  "M/c long term complication: stricture. (Book p148)")
q(148, S5, "The minimum number of lymph nodes that should be removed during esophagectomy is:",
  ["15", "5", "30", "50"], 0,
  "Minimum number of lymph nodes removed: 15. (Book p148)")

# ---------------- p148 · ESOPHAGEAL REPLACEMENT & COMPLICATIONS ----------------
S6 = "Esophageal Replacement & Complications"
q(148, S6, "The m/c and best conduit for esophageal replacement is:",
  ["Stomach tube", "Jejunum", "Ileum", "Sigmoid"], 0,
  "Esophageal replacement: m/c and best is the stomach tube. (Book p148)")
q(148, S6, "The stomach tube used for esophageal replacement is based on the:",
  ["Right gastroepiploic artery", "Left gastric artery", "Splenic artery",
   "Short gastric arteries"], 0,
  "Based on the right gastric epiploic (gastroepiploic) artery > right gastric artery. (Book p148)")
q(148, S6, "If the stomach cannot be used for esophageal replacement, the conduit used is the:",
  ["Colon", "Duodenum", "Ileum", "Appendix"], 0,
  "If the stomach is involved: colon. (Book p148)")
q(148, S6, "Complications of esophageal replacement include all of the following EXCEPT:",
  ["Cholecystitis", "Atelectasis", "Pneumonia", "Anastomotic leak"], 0,
  "Complications: atelectasis, pneumonia, anastomotic leak, chylothorax. (Book p148)")
q(148, S6, "Comparing anastomotic leaks, a neck anastomosis leaks:",
  ["More often than a thoracic anastomosis but is less dangerous",
   "Less often and is more dangerous",
   "Never", "With the same frequency and severity"], 0,
  "Anastomotic leak: neck anastomosis leaks more often than thoracic (thoracic leak is more dangerous). (Book p148)")
q(148, S6, "Chylothorax after esophagectomy is due to injury to the:",
  ["Thoracic duct", "Azygos vein", "Thoracic sympathetic chain", "Aortic duct"], 0,
  "Chylothorax: injury to the thoracic duct - turbid fluid in the drain; usually subsides spontaneously. (Book p148)")

# ---------------- p148-149 · CHEMORADIOTHERAPY & STENTS ----------------
S7 = "Chemoradiotherapy, Stents & Malignant TEF"
q(148, S7, "Combined chemoradiation in esophageal cancer has:",
  ["A better effect than either modality alone", "No advantage over radiotherapy alone",
   "A worse outcome than surgery for cervical tumors", "No role in esophageal cancer"], 0,
  "Combined chemoradiation: better effect. (Book p148)")
q(148, S7, "Chemotherapeutic drugs used in esophageal cancer include all of the following EXCEPT:",
  ["Doxorubicin", "Gemcitabine", "Cisplatin", "5-FU"], 0,
  "Chemotherapeutic drugs: gemcitabine, cisplatin, 5-FU. (Book p148)")
q(149, S7, "A malignant tracheo-esophageal fistula presents with:",
  ["Cough and pneumonia", "Hematemesis", "Hoarseness", "Dysphagia alone"], 0,
  "Malignant TEF: presentation is cough and pneumonia. (Book p149)")
q(149, S7, "The m/c complication of a self expanding metallic stent (SEMS) placed for malignant TEF is:",
  ["Migration of the stent", "Perforation", "Chylothorax", "Stent fracture"], 0,
  "Complications of SEMS: m/c is migration of the stent; also bleeding and regrowth of tumor into the stent. (Book p149)")

# ---------------- p149 · BENIGN TUMORS ----------------
S8 = "Benign Tumors of the Esophagus"
q(149, S8, "The m/c benign tumor of the esophagus is:",
  ["Leiomyoma", "Lipoma", "Fibroma", "Hemangioma"], 0,
  "Leiomyoma: m/c benign tumor of the esophagus. (Book p149)")
q(149, S8, "Esophageal leiomyoma is typically located in the:",
  ["Mid and distal esophagus", "Cervical esophagus", "Upper third only",
   "Gastroesophageal junction"], 0,
  "Site: mid-distal esophagus. (Book p149)")
q(149, S8, "The male to female incidence ratio of esophageal leiomyoma is:",
  ["2:1", "1:1", "1:2", "10:1"], 0,
  "Incidence: M:F = 2:1. (Book p149)")
q(149, S8, "Small esophageal leiomyomas are usually:",
  ["Asymptomatic", "Causing severe dysphagia", "Causing hematemesis", "Causing hoarseness"], 0,
  "Clinical features: asymptomatic; large tumors cause dysphagia. (Book p149)")
q(149, S8, "The barium swallow appearance of an esophageal leiomyoma is:",
  ["Punched out appearance", "Rat tail appearance", "Apple core appearance",
   "Bird beak appearance"], 0,
  "Barium swallow: punched out appearance. (Book p149)")
q(149, S8, "The standard surgical treatment of an esophageal leiomyoma is:",
  ["Enucleation", "Esophagectomy", "Endoscopic mucosal resection", "Laser ablation"], 0,
  "Management: enucleation (or STER). (Book p149)")
q(149, S8, "STER in the management of esophageal leiomyoma stands for:",
  ["Submucosal tunneling endoscopic resection", "Subtotal endoscopic resection",
   "Stent guided tumor excision", "Subserosal tumor enucleation and repair"], 0,
  "STER: submucosal tunneling endoscopic resection. (Book p149)")

# ---------------- units ----------------
def sec_ids(*labels):
    return [x["id"] for x in Q if x["sec"] in labels]
def first_page(label):
    for x in Q:
        if x["sec"] == label:
            return x["page"]
    return 0

UNIT_DEFS = [
    (S1, "Two diseases: squamous carcinoma, still the commonest worldwide and sitting in the middle third, driven by smoking, alcohol, hot drinks, nitrosamines from pickled food, betel nut, yerba mate, poor diet, fungal toxins, mediastinal radiation, lye strictures, aerodigestive primaries, Plummer-Vinson, achalasia, tylosis, CREST and Zenker's; adenocarcinoma, the western-world leader, sits in the lower third on the reflux-Barrett's-obesity axis (Barrett's ++++ beats everything else)."),
    (S2, "Progressive dysphagia to solids more than liquids plus weight loss is the presentation; hoarseness means left recurrent laryngeal nerve and chronic cough means a malignant tracheo-esophageal fistula - both advanced. Diagnose by endoscopic biopsy, stage the body with PET-CT (18-FDG, half-life 110 min), stage the wall and nodes with EUS, and expect a rat-tail or apple-core barium."),
    (S3, "TNM: Tis is high-grade dysplasia, T1 lamina propria/muscularis mucosae/submucosa, T2 muscularis propria, T3 adventitia, T4a resectable neighbours (pleura, pericardium, diaphragm) and T4b unresectable ones (aorta, vertebral body, trachea). Nodes run N1 = 1-2, N2 = 3-6, N3 = 7 or more; liver is the commonest site of distant spread. Siewert types I and II of the GE junction behave like esophageal cancer, type III like gastric cancer."),
    (S4, "Stage decides: T1a above the submucosa is cured by EMR, T1b/T2 node-negative goes straight to esophagectomy, T3/T4 gets neoadjuvant chemoradiation then surgery, and cervical tumors get definitive chemoradiotherapy to save the larynx. Resections are graded R0 (microscopically clear), R1 (microscopic disease left) and R2 (gross disease left), with 10 cm proximal and 5 cm distal margins because skip lesions travel."),
    (S5, "Three operations: McKeown's three-field (abdomen, right chest, left neck - best node clearance, for middle third), trans-hiatal Orringer (abdomen and left neck, no thoracotomy, for lower third) and Ivor Lewis (abdomen and right chest, anastomosis in the chest). Anastomotic leak causing mediastinitis is the commonest cause of death, stricture the commonest late problem, and at least 15 nodes should come out."),
    (S6, "The stomach tube, pedicled on the right gastroepiploic artery, is the conduit of choice; colon if the stomach is unusable. Expect atelectasis and pneumonia; a neck anastomosis leaks more often but a thoracic leak kills more often; turbid drain fluid means thoracic duct injury - chylothorax usually settles on its own."),
    (S7, "Combined chemoradiation works better than either alone, using gemcitabine, cisplatin and 5-FU. A malignant tracheo-esophageal fistula presents with cough and pneumonia and is palliated with a SEMS - though migration is the commonest problem, followed by bleeding and tumour regrowth through the mesh."),
    (S8, "Leiomyoma is the commonest benign esophageal tumor - mid-distal, twice as common in men, usually silent until it is big enough to cause dysphagia. Barium shows a punched-out filling defect and treatment is enucleation (or submucosal tunnelling endoscopic resection, STER)."),
]

UNITS = []
for i, (title, guide) in enumerate(UNIT_DEFS, 1):
    UNITS.append({"id": f"SURG-U21-{i}", "ch": 21, "n": i, "title": title,
                  "sec": f"{title} · p{first_page(title)}",
                  "qs": sec_ids(title), "guide": guide})

covered = [i for u in UNITS for i in u["qs"]]
assert covered == [x["id"] for x in Q], "units must cover questions in order"

data = {"questions": Q, "units": UNITS}
with open("data/ch21.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
print(f"ch21: {len(Q)} questions, {len(UNITS)} units")
