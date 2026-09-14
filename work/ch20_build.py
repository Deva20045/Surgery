#!/usr/bin/env python3
"""Build data/ch20.json for PULSE Surgery ch20 (Esophagus : Part 2, book p135-144)."""
import json

Q = []
def q(page, sec, text, opts, ans, exp):
    Q.append({"id": f"SURG-C20-{len(Q)+1:03d}", "sec": sec, "page": page,
              "q": text, "opts": opts, "ans": ans, "exp": exp})

# ---------------- p135 · ESOPHAGEAL INFECTIONS ----------------
S1 = "Esophageal Infections"
q(135, S1, "Esophageal candidiasis is associated with:",
  ["Oral thrush", "Herpes labialis", "Graft versus host disease", "Corkscrew esophagus"], 0,
  "Esophageal candidiasis: associated with oral thrush, seen in immunocompromised patients. (Book p135)")
q(135, S1, "Endoscopy in esophageal candidiasis shows:",
  ["Shaggy deposits", "Geographical ulcers", "Small ulcers with raised margins", "Corkscrew appearance"], 0,
  "Investigations: endoscopy shows shaggy deposits. (Book p135)")
q(135, S1, "Barium swallow in esophageal candidiasis shows:",
  ["Worm like ulcers", "Corkscrew appearance", "Bird beak appearance", "Rosary bead appearance"], 0,
  "Barium swallow in candidiasis: worm like ulcers. (Book p135)")
q(135, S1, "The treatment of esophageal candidiasis is:",
  ["Antifungals", "Acyclovir", "Ganciclovir", "Proton pump inhibitors alone"], 0,
  "Management of esophageal candidiasis: antifungals. (Book p135)")
q(135, S1, "CMV esophagitis is typically seen in:",
  ["Post transplant patients on immunosuppressants", "Healthy young adults",
   "Patients with achalasia", "Patients with Zenker's diverticulum"], 0,
  "CMV: post transplant (immunosuppressants). (Book p135)")
q(135, S1, "CMV esophagitis is associated with:",
  ["Graft versus host disease", "Herpes labialis", "Oral thrush", "Barrett's esophagus"], 0,
  "CMV: associated with GvHD (graft versus host disease). (Book p135)")
q(135, S1, "The endoscopic appearance of CMV esophagitis is:",
  ["Geographical / serpiginous ulcers", "Shaggy white deposits",
   "Small ulcers with raised margins", "Linear furrows"], 0,
  "CMV appearance: geographical / serpiginous ulcers. (Book p135)")
q(135, S1, "Herpes esophagitis is associated with:",
  ["Herpes labialis", "Oral thrush", "Graft versus host disease", "Food allergies"], 0,
  "Herpes infection: associated with herpes labialis. (Book p135)")
q(135, S1, "The endoscopic appearance of herpes esophagitis is:",
  ["Small ulcers with raised margins", "Large geographical ulcers", "Shaggy deposits",
   "Cobblestone mucosa"], 0,
  "Herpes infection: small ulcers with raised margins. (Book p135)")

# ---------------- p135-136 · FELINE ESOPHAGUS & EOSINOPHILIC ESOPHAGITIS ----------------
S2 = "Feline Esophagus & Eosinophilic Esophagitis"
q(135, S2, "Feline esophagus (stacked up transverse folds) is seen in:",
  ["GERD and eosinophilic esophagitis", "Achalasia cardia", "Barrett's esophagus",
   "Zenker's diverticulum"], 0,
  "Feline esophagus: seen in GERD and eosinophilic esophagitis. (Book p135)")
q(135, S2, "The site of feline esophagus is the:",
  ["Upper one third of the esophagus", "Lower one third", "Whole esophagus", "Gastroesophageal junction only"], 0,
  "Feline esophagus: site is the upper 1/3rd, with a stacked up appearance. (Book p135)")
q(135, S2, "The m/c cause of changes in the lower one third in this context is:",
  ["GERD", "Eosinophilic esophagitis", "Candidiasis", "Scleroderma"], 0,
  "Lower 1/3rd changes: m/c cause is GERD. (Book p135)")
q(135, S2, "Eosinophilic esophagitis is a:",
  ["Chronic immune mediated disease with esophageal dysfunction",
   "Acute infective esophagitis", "Congenital motility disorder", "Complication of Barrett's esophagus"], 0,
  "Eosinophilic esophagitis: chronic immune mediated disease with esophageal dysfunction. (Book p135)")
q(135, S2, "Eosinophilic esophagitis is initiated by food antigens leading to:",
  ["Eosinophilia and fibrosis", "Neutrophilic infiltration only", "Caseating granulomas",
   "Mucosal calcification"], 0,
  "Food antigen initiation: eosinophilia and fibrosis. (Book p135)")
q(135, S2, "The peak age of presentation of eosinophilic esophagitis is:",
  ["20-30 years", "1-5 years", "60-70 years", "Above 80 years"], 0,
  "Peak age: 20-30 years. (Book p135)")
q(135, S2, "Endoscopic findings in eosinophilic esophagitis include all of the following EXCEPT:",
  ["Bird beak appearance", "Crepe paper mucosa", "Furrows", "Rings"], 0,
  "Endoscopy: crepe paper mucosa, furrows, rings. (Book p135)")
q(135, S2, "The diagnostic criterion on biopsy in eosinophilic esophagitis is:",
  ["Eosinophilia > 15-20 eosinophils per HPF", "Neutrophils > 50 per HPF",
   "Lymphocytes > 20 per HPF", "Presence of granulomas"], 0,
  "Biopsy (taken from 2 fields): eosinophilia > 15-20 eosinophils/HPF. (Book p135)")
q(136, S2, "The goals of treatment of eosinophilic esophagitis are:",
  ["Reduce eosinophilia and control symptoms", "Eradicate Helicobacter pylori",
   "Restore peristalsis by myotomy", "Dilate the stricture endoscopically"], 0,
  "Goal: reduce eosinophilia, control symptoms. (Book p136)")
q(136, S2, "Treatment options for eosinophilic esophagitis include:",
  ["Topical steroids and proton pump inhibitors", "Systemic antifungals", "Antivirals",
   "Botulinum toxin injection"], 0,
  "Treatment: topical steroids and PPIs. (Book p136)")

# ---------------- p136 · MOTILITY DISORDERS: CHICAGO 4.0 & HRM ----------------
S3 = "Motility Disorders: Chicago 4.0 & HRM Metrics"
q(136, S3, "The Chicago 4.0 classification of esophageal motility disorders is based on:",
  ["High resolution manometry", "Barium swallow", "Endoscopy", "24 hour pH monitoring"], 0,
  "Chicago 4.0: based on high resolution manometry (HRM). (Book p136)")
q(136, S3, "An elevated integrated relaxation pressure (IRP) above normal indicates:",
  ["Lack of LES relaxation", "Excessive LES relaxation", "Hypercontractile peristalsis",
   "Esophageal shortening"], 0,
  "IRP elevated above normal defines lack of LES relaxation. (Book p136)")
q(136, S3, "The distal contractile integral (DCI) measures:",
  ["Strength of distal esophageal contraction", "Resting LES pressure", "Length of the esophagus",
   "Gastric emptying"], 0,
  "DCI (mmHg-s-cm): amplitude x duration x length of the distal esophageal contraction - measures strength. (Book p136)")
q(136, S3, "A decreased distal latency (< 4.5 sec) indicates:",
  ["A spastic esophageal motor disorder", "Achalasia type II", "Normal peristalsis",
   "Ineffective swallowing"], 0,
  "Decreased DL (< 4.5 sec) is an indicator of a spastic esophageal motor disorder. (Book p136)")

# ---------------- p136 · ACHALASIA: PATHOPHYSIOLOGY & TYPES ----------------
S4 = "Achalasia Cardia: Pathophysiology & Types"
q(136, S4, "The m/c esophageal motility disorder is:",
  ["Achalasia cardia", "Diffuse esophageal spasm", "Nutcracker esophagus",
   "Ineffective esophageal motility"], 0,
  "Achalasia cardia: m/c motility disorder, with increased risk of squamous cell carcinoma of the esophagus. (Book p136)")
q(136, S4, "Achalasia cardia is characterised by:",
  ["Failure of the lower esophageal sphincter to relax", "Excessive LES relaxation",
   "Absence of the esophagus", "Hypertrophy of the cricopharyngeus"], 0,
  "Achalasia: failure of LES to relax. (Book p136)")
q(136, S4, "The pathophysiology of achalasia cardia is loss of ganglion cells in the:",
  ["Myenteric (Auerbach's) plexus of the lower half of the esophagus",
   "Submucosal (Meissner's) plexus of the whole esophagus",
   "Dorsal motor nucleus of the vagus", "Celiac ganglion"], 0,
  "Pathophysiology: loss of ganglion cells in the myenteric/Auerbach plexus (lower half). (Book p136)")
q(136, S4, "Hirschsprung disease, quoted alongside achalasia, is due to:",
  ["Congenital absence of ganglion cells", "Hypertrophy of ganglion cells",
   "Viral destruction of ganglion cells", "Autoimmune ganglionitis"], 0,
  "Hirschsprung disease: congenital absence of ganglion cells. (Book p136)")
q(136, S4, "Primary achalasia is due to:",
  ["Loss of ganglion cells", "Chaga's disease", "Malignancy", "Radiation"], 0,
  "1 degree achalasia: loss of ganglion cells. (Book p136)")
q(136, S4, "Secondary achalasia is classically due to:",
  ["Chaga's disease (Trypanosoma cruzi)", "Herpes infection", "Candidiasis", "Tuberculosis"], 0,
  "2 degrees achalasia: secondary to Chaga's disease (Trypanosoma cruzi). (Book p136)")
q(136, S4, "Vigorous achalasia is:",
  ["Rapidly progressive", "Asymptomatic", "A variant of Zenker's diverticulum",
   "Due to malignancy"], 0,
  "Vigorous achalasia: rapidly progressive. (Book p136)")
q(136, S4, "Pseudoachalasia is associated with:",
  ["Malignancy", "Chaga's disease", "GERD", "Candidiasis"], 0,
  "Pseudoachalasia: associated with malignancy. (Book p136)")

# ---------------- p137 · ACHALASIA: FEATURES, INVESTIGATIONS & CHICAGO TYPES ----------------
S5 = "Achalasia: Features, Investigations & Chicago Types"
q(137, S5, "In achalasia cardia, dysphagia is typically:",
  ["Initially for liquids more than solids", "Only for solids", "Only for bread",
   "Absent"], 0,
  "Dysphagia: initially liquids > solids (solids relax the sphincter by their weight). (Book p137)")
q(137, S5, "The earliest feature of achalasia cardia is:",
  ["Regurgitation", "Weight loss", "Chest pain", "Hematemesis"], 0,
  "Regurgitation: earliest feature. (Book p137)")
q(137, S5, "Other clinical features of achalasia include all of the following EXCEPT:",
  ["Hematemesis", "Nocturnal coughing", "Post prandial choking", "Weight loss"], 0,
  "Other features: nocturnal coughing, post prandial choking, weight loss. (Book p137)")
q(137, S5, "The m/c complication of achalasia cardia is:",
  ["Aspiration pneumonia", "Esophageal carcinoma", "Liver abscess", "Perforation"], 0,
  "Complications: aspiration pneumonia (m/c), lung abscess. (Book p137)")
q(137, S5, "The investigation of choice for achalasia cardia is:",
  ["Manometry", "Barium swallow", "Upper GI endoscopy", "CT chest"], 0,
  "Manometry: IOC; shows increased IRP and failure of LES relaxation. (Book p137)")
q(137, S5, "Endoscopy in a patient with suspected achalasia is done to:",
  ["Rule out cancer", "Measure pressures", "Perform dilatation", "Take a biopsy of the plexus"], 0,
  "Endoscopy: rule out cancer. (Book p137)")
q(137, S5, "The barium swallow appearance in achalasia cardia is:",
  ["Bird beak appearance", "Corkscrew appearance", "Rosary bead appearance",
   "Worm like ulcers"], 0,
  "Barium swallow: bird beak appearance. (Book p137)")
q(137, S5, "Chicago type I achalasia is characterised by:",
  ["100% failed peristalsis with absent peristalsis", "Panesophageal pressurisation in >= 20% swallows",
   "Premature spastic contractions in >= 20% swallows", "Normal peristalsis with high DCI"], 0,
  "Type I: elevated median IRP with 100% failed peristalsis. (Book p137)")
q(137, S5, "Chicago type II achalasia shows:",
  ["Panesophageal pressurisation in >= 20% of swallows",
   "Premature spastic contractions in >= 20% of swallows",
   "Normal peristalsis", "Absent contractions with normal IRP"], 0,
  "Type II: 100% failed peristalsis with panesophageal pressurisation (POP) in >= 20% swallows. (Book p137)")
q(137, S5, "Chicago type III achalasia shows:",
  [">= 20% swallows with premature (spastic) contractions",
   "Panesophageal pressurisation in all swallows", "Normal peristalsis", "Absent IRP"], 0,
  "Type III: >= 20% swallows with premature contractions - spastic. (Book p137)")
q(137, S5, "The Eckardt score for achalasia includes all of the following EXCEPT:",
  ["Hematemesis", "Weight loss", "Dysphagia", "Retrosternal pain"], 0,
  "Eckardt score: 4 parameters - weight loss, dysphagia, retrosternal pain, regurgitation. (Book p137)")
q(137, S5, "Each parameter of the Eckardt score is scored from:",
  ["0-3", "0-1", "1-10", "0-100"], 0,
  "Each parameter of the Eckardt score is scored 0-3. (Book p137)")

# ---------------- p138 · ACHALASIA: MANAGEMENT ----------------
S6 = "Achalasia: Management"
q(138, S6, "Botulinum toxin injection in achalasia causes relaxation; its main drawback is:",
  ["Highest rate of recurrence", "Highest risk of perforation", "Severe bleeding",
   "Permanent fibrosis of the esophagus"], 0,
  "Botox: causes relaxation; adverse effects - highest rate of recurrence. (Book p138)")
q(138, S6, "Repeated administration of botulinum toxin in achalasia leads to:",
  ["Fibrosis", "Malignant transformation", "Complete cure", "Stricture formation"], 0,
  "Repeat administration of botox: fibrosis. (Book p138)")
q(138, S6, "Botulinum toxin is preferred in:",
  ["Elderly patients with co-morbidities", "Young patients with type III achalasia",
   "Patients with Chaga's disease", "Patients with Barrett's esophagus"], 0,
  "Indications for botox: elderly patients with co-morbidities. (Book p138)")
q(138, S6, "Serial pneumatic balloon dilatations in achalasia have efficacy:",
  ["Similar to surgical myotomy", "Far superior to surgery", "Far inferior to botox",
   "Only in type III disease"], 0,
  "Serial dilatations: similar efficacy to surgical myotomy. (Book p138)")
q(138, S6, "The best responders to pneumatic dilatation in achalasia are:",
  ["Patients > 45 years, females, previously undilated esophagus and type II achalasia",
   "Children with type III disease", "Patients with prior Heller's myotomy",
   "Patients with pseudoachalasia"], 0,
  "Best responders: > 45 years, females, previously undilated esophagus, type 2 achalasia. (Book p138)")
q(138, S6, "The risk of perforation during pneumatic dilatation is reduced by using a balloon:",
  ["< 30 mm", "> 40 mm", "Exactly 35 mm", "Any size - size makes no difference"], 0,
  "Risk of perforation is reduced with balloon < 30 mm. (Book p138)")
q(138, S6, "Heller's myotomy involves cutting the muscle:",
  ["6 cm proximal and 2-3 cm distal to the gastroesophageal junction",
   "Only 1 cm above the GE junction", "The whole length of the esophagus",
   "Only the circular muscle of the stomach"], 0,
  "Heller's myotomy: cut muscle 6 cm proximal and 2-3 cm distal to the GE junction. (Book p138)")
q(138, S6, "The m/c complication of Heller's myotomy is:",
  ["GERD", "Dysphagia", "Perforation", "Bleeding"], 0,
  "Surgical myotomy: m/c complication is GERD (prevented by fundoplication). (Book p138)")
q(138, S6, "GERD after Heller's myotomy is prevented by:",
  ["Adding a fundoplication", "Giving botox", "Postoperative dilatation",
   "Total parenteral nutrition"], 0,
  "GERD after myotomy is prevented by fundoplication. (Book p138)")
q(138, S6, "POEM (per oral endoscopic myotomy) is a type of:",
  ["NOTES procedure", "Laparoscopic surgery", "Open thoracotomy", "Radiological intervention"], 0,
  "POEM: per oral endoscopic myotomy - a type of NOTES procedure. (Book p138)")
q(138, S6, "During POEM the layer removed is the:",
  ["Circular muscle layer", "Longitudinal muscle layer", "Mucosa", "Serosa"], 0,
  "POEM: remove the circular muscle layer then close the mucosal entry/tunnel. (Book p138)")
q(138, S6, "Which achalasia types respond best to surgery (myotomy)?",
  ["Type I and type II", "Type III only", "Pseudoachalasia only", "Vigorous achalasia only"], 0,
  "Surgical outcome: type 1 and 2 respond best; type 3 and other spastic conditions respond less well. (Book p138)")
q(138, S6, "The preferred management of type I achalasia is:",
  ["Heller's myotomy", "Pneumatic dilation", "POEM alone", "Botulinum toxin"], 0,
  "Best management: type 1 - Heller's myotomy; type 2 - pneumatic dilation; type 3 - POEM. (Book p138)")
q(138, S6, "The preferred management of type II achalasia is:",
  ["Pneumatic dilation", "Heller's myotomy", "Botulinum toxin", "No treatment"], 0,
  "Best management: type 2 - pneumatic dilation. (Book p138)")
q(138, S6, "The preferred management of type III achalasia is:",
  ["POEM", "Pneumatic dilation", "Botulinum toxin", "Observation"], 0,
  "Best management: type 3 - POEM. (Book p138)")

# ---------------- p139 · DES & APPROACH ----------------
S7 = "Diffuse Esophageal Spasm & Approach to Motility Disorders"
q(139, S7, "Diffuse esophageal spasm is:",
  ["Less common than achalasia", "More common than achalasia",
   "The m/c motility disorder", "Seen only in children"], 0,
  "DES: symptoms less common than achalasia. (Book p139)")
q(139, S7, "Diffuse esophageal spasm is a motor abnormality of the:",
  ["Esophageal body (lower two thirds)", "Upper esophageal sphincter only",
   "Cricopharyngeus", "Stomach"], 0,
  "DES: motor abnormality of the esophageal body (lower 2/3rd). (Book p139)")
q(139, S7, "Manometry in diffuse esophageal spasm shows contractions that are:",
  ["Repetitive, simultaneous and of high amplitude (raised DCI)",
   "Absent with a high IRP", "Normal in amplitude but slow", "Confined to the UES"], 0,
  "DES contractions: repetitive, simultaneous and high amplitude (increased DCI). (Book p139)")
q(139, S7, "Acid reflux in diffuse esophageal spasm is:",
  ["Negative", "The dominant feature", "Universal", "The cause of the spasm"], 0,
  "DES: acid reflux is negative. (Book p139)")
q(139, S7, "The presenting features of diffuse esophageal spasm are:",
  ["Chest pain (angina like) and dysphagia", "Hematemesis and melena",
   "Jaundice and fever", "Hoarseness and stridor"], 0,
  "Clinical features: chest pain (angina like) and dysphagia. (Book p139)")
q(139, S7, "Diffuse esophageal spasm is more common in:",
  ["Females", "Males", "Children", "The elderly only"], 0,
  "DES: females > males. (Book p139)")
q(139, S7, "The barium swallow appearance in diffuse esophageal spasm is:",
  ["Rosary bead / corkscrew appearance", "Bird beak appearance", "Worm like ulcers",
   "Apple core lesion"], 0,
  "Barium swallow in DES: rosary bead / corkscrew appearance. (Book p139)")
q(139, S7, "The confirmatory investigation for diffuse esophageal spasm is:",
  ["Manometry", "Barium swallow", "ECG", "Endoscopy"], 0,
  "Investigations: ECG to rule out angina, barium swallow, manometry is confirmatory. (Book p139)")
q(139, S7, "In a patient with angina-like chest pain, the first investigation to be done is:",
  ["ECG to rule out angina", "Manometry", "Barium swallow", "Coronary angiography"], 0,
  "ECG: rule out angina before attributing chest pain to esophageal spasm. (Book p139)")
q(139, S7, "Treatment of diffuse esophageal spasm includes all of the following EXCEPT:",
  ["Botulinum toxin as first line", "POEM - very good response",
   "Calcium channel blockers", "Nitrates"], 0,
  "Treatment: POEM gives a very good response; calcium channel blockers and nitrates are used. (Book p139)")
q(139, S7, "A patient with chest pain resembling angina but normal cardiac enzymes is evaluated with:",
  ["ECG followed by manometry", "Immediate coronary angiography", "Laparoscopy", "CT brain"], 0,
  "Approach: chest pain similar to angina with normal cardiac enzymes - ECG, then manometry. (Book p139)")

# ---------------- p139 · ESOPHAGEAL DIVERTICULAE ----------------
S8 = "Esophageal Diverticulae"
q(139, S8, "Zenker's diverticulum is located in the:",
  ["Upper esophagus", "Mid esophagus", "Lower esophagus", "Stomach"], 0,
  "Types: upper esophageal (Zenker's), mid esophageal (para-bronchial), lower esophageal (epiphrenic). (Book p139)")
q(139, S8, "The mid esophageal or para-bronchial diverticulum is:",
  ["The only true diverticulum (contains all layers)", "A false diverticulum",
   "A traction diverticulum caused by candida", "Always malignant"], 0,
  "Mid esophageal (para-bronchial): traction, only true diverticulum of the esophagus (all layers). (Book p139)")
q(139, S8, "Mid esophageal traction diverticulae are associated with:",
  ["Tuberculosis and histoplasmosis", "Chaga's disease", "Scleroderma", "Barrett's esophagus"], 0,
  "Mid esophageal diverticulum: TB, histoplasmosis. (Book p139)")
q(139, S8, "Epiphrenic diverticula are located:",
  ["In the lower esophagus close to the diaphragm", "In the upper esophagus",
   "At the cricopharyngeus", "In the gastric fundus"], 0,
  "Lower esophageal (epiphrenic): pulsion, false diverticulum, close to the diaphragm. (Book p139)")
q(139, S8, "The mechanism of formation of Zenker's and epiphrenic diverticula is:",
  ["Pulsion from increased intraluminal pressure", "Traction from outside",
   "Congenital weakness", "Ischaemic necrosis"], 0,
  "Zenker's and epiphrenic: pulsion (increased pressure) - false diverticula. (Book p139)")

# ---------------- p140 · ZENKER'S DIVERTICULUM ----------------
S9 = "Zenker's Diverticulum"
q(140, S9, "Zenker's diverticulum is also known as:",
  ["Cricopharyngeal achalasia", "Boerhaave syndrome", "Mallory Weiss syndrome",
   "Schatzki ring"], 0,
  "Zenker's diverticulum: AKA cricopharyngeal achalasia. (Book p140)")
q(140, S9, "Zenker's diverticulum carries an increased risk of:",
  ["Squamous cell carcinoma", "Adenocarcinoma", "Leiomyoma", "Melanoma"], 0,
  "Zenker's diverticulum: increased risk of squamous cell carcinoma. (Book p140)")
q(140, S9, "Zenker's diverticulum herniates through:",
  ["Killian's dehiscence between thyropharyngeus and cricopharyngeus",
   "The diaphragmatic hiatus", "The cricothyroid membrane", "The esophageal hiatus"], 0,
  "Outpouches through Killian's dehiscence - the potential space between thyropharyngeus and cricopharyngeus. (Book p140)")
q(140, S9, "Zenker's diverticulum begins in the midline posteriorly and finally lies:",
  ["To the left of the midline", "To the right of the midline",
   "In the midline anteriorly", "In the posterior triangle"], 0,
  "Begins midline posteriorly; final position is to the left of the midline. (Book p140)")
q(140, S9, "The earliest symptom of Zenker's diverticulum is:",
  ["Regurgitation", "Dysphagia", "Hematemesis", "Hoarseness"], 0,
  "Regurgitation is the earliest symptom; also halitosis and dysphagia. (Book p140)")
q(140, S9, "Halitosis (bad oral odour) is a recognised feature of:",
  ["Zenker's diverticulum", "Achalasia cardia", "Schatzki ring", "Barrett's esophagus"], 0,
  "Halitosis (bad oral odor) is a feature of Zenker's diverticulum. (Book p140)")
q(140, S9, "Regurgitation of food in Zenker's diverticulum is relieved when the patient:",
  ["Shifts position", "Lies flat", "Drinks cold water", "Holds the breath"], 0,
  "Food in the diverticulum causes regurgitation; patients shift position to relieve it. (Book p140)")
q(140, S9, "The m/c complication of Zenker's diverticulum is:",
  ["Aspiration pneumonia", "Perforation", "Hemorrhage", "Stricture"], 0,
  "Complications: aspiration pneumonia (m/c), lung abscess. (Book p140)")
q(140, S9, "The investigation of choice for Zenker's diverticulum is:",
  ["Barium swallow", "CT scan", "Manometry", "Endoscopy"], 0,
  "IOC: barium swallow. (Book p140)")
q(140, S9, "Surgery for Zenker's diverticulum is indicated for:",
  ["Large (> 2 cm) and symptomatic diverticula", "All asymptomatic diverticula",
   "Diverticula smaller than 5 mm", "Only when carcinoma is proven"], 0,
  "Management: large (> 2 cm) and symptomatic - surgery. (Book p140)")
q(140, S9, "Surgical treatment of Zenker's diverticulum combines diverticulectomy with:",
  ["Cricopharyngeal myotomy", "Fundoplication", "Total esophagectomy", "Heller's myotomy"], 0,
  "Surgery: diverticulectomy (linear stapler > LASER) with cricopharyngeal myotomy - reduces recurrence. (Book p140)")
q(140, S9, "The additional procedure that reduces recurrence after diverticulectomy is:",
  ["Cricopharyngeal myotomy", "Fundoplication", "Pyloroplasty", "Gastrostomy"], 0,
  "Cricopharyngeal myotomy added to diverticulectomy reduces recurrence. (Book p140)")
q(140, S9, "The endoscopic option for Zenker's diverticulum is:",
  ["Endoscopic diverticulopexy with cricopharyngeal myotomy", "Endoscopic dilatation alone",
   "Endoscopic mucosal resection", "Endoscopic sclerotherapy"], 0,
  "Management: endoscopic diverticulopexy with cricopharyngeal myotomy. (Book p140)")

# ---------------- p141-142 · HIATAL HERNIA ----------------
S10 = "Hiatal Hernia"
q(141, S10, "The m/c type of hiatal hernia is:",
  ["Type I sliding hiatal hernia", "Type II rolling hernia", "Type III mixed hernia",
   "Type IV hernia"], 0,
  "Sliding hiatal hernia: type I and the m/c type. (Book p141)")
q(141, S10, "The pathophysiology of a sliding hiatal hernia is:",
  ["Upward sliding of the gastroesophageal junction", "Herniation of the fundus with a normal GE junction",
   "Herniation of the colon through the hiatus", "Defect in the pleural space"], 0,
  "Sliding hernia: upward sliding of the GE junction. (Book p141)")
q(141, S10, "Sliding hiatal hernias are:",
  ["Asymptomatic or present with GERD and are not life threatening",
   "Always life threatening", "Always associated with volvulus", "Always surgical emergencies"], 0,
  "Sliding hernia: asymptomatic or GERD; not life threatening. (Book p141)")
q(141, S10, "The investigation of choice for a hiatal hernia is:",
  ["CT with oral contrast", "Plain X-ray abdomen", "Ultrasound", "MRI"], 0,
  "Investigations: CT with oral contrast is the IOC; barium swallow also used. (Book p141)")
q(141, S10, "Symptomatic or large sliding hiatal hernias are treated by:",
  ["Fundoplication", "Observation alone", "Gastrectomy", "Total parenteral nutrition"], 0,
  "Symptomatic or large sliding hernia: fundoplication. (Book p141)")
q(141, S10, "A rolling / paraesophageal hernia is a:",
  ["Type II hernia", "Type I hernia", "Type III hernia", "Type IV hernia"], 0,
  "Rolling / paraesophageal hernia: type II. (Book p141)")
q(141, S10, "In a rolling hernia the portion of stomach herniates into the thoracic cavity through the hiatal opening while the:",
  ["GE junction remains normal", "GE junction slides upwards", "Esophagus shortens",
   "Fundus remains intra-abdominal"], 0,
  "Rolling hernia: part of stomach herniates into the thoracic cavity; GE junction is normal. (Book p141)")
q(141, S10, "A rolling / paraesophageal hernia is dangerous because the herniated part may undergo:",
  ["Volvulus and necrosis", "Malignant transformation", "Calcification", "Intussusception"], 0,
  "Complications of rolling hernia: volvulus/necrosis - life threatening. (Book p141)")
q(141, S10, "The management of a rolling / paraesophageal hernia is:",
  ["Surgery", "Observation", "Proton pump inhibitors alone", "Endoscopic dilatation"], 0,
  "Rolling hernia: management is surgery. (Book p141)")
q(142, S10, "A type III hiatal hernia is:",
  ["Mixed sliding and rolling", "A paraesophageal hernia with contents other than stomach",
   "A pure sliding hernia", "A congenital diaphragmatic hernia"], 0,
  "Type III: mixed sliding + rolling; management governed by the rolling component. (Book p142)")
q(142, S10, "A type IV hiatal hernia is:",
  ["Paraesophageal hernia with contents other than the stomach", "A pure sliding hernia",
   "A mixed sliding and rolling hernia", "A traumatic diaphragmatic rupture"], 0,
  "Type IV: paraesophageal hernia with content other than the stomach. (Book p142)")

# ---------------- p142 · IATROGENIC ESOPHAGEAL PERFORATION ----------------
S11 = "Iatrogenic Esophageal Perforation"
q(142, S11, "The m/c type of esophageal perforation is:",
  ["Iatrogenic", "Spontaneous", "Traumatic", "Foreign body related"], 0,
  "Esophageal perforation types: iatrogenic (m/c) and spontaneous. (Book p142)")
q(142, S11, "Iatrogenic esophageal perforation is m/c located in the:",
  ["Upper one third of the esophagus", "Lower one third", "Mid esophagus", "Stomach"], 0,
  "Iatrogenic: post endoscopy; site upper 1/3rd (m/c). (Book p142)")
q(142, S11, "Risk factors for iatrogenic esophageal perforation include all of the following EXCEPT:",
  ["Diagnostic upperGI endoscopy alone in a normal esophagus",
   "Therapeutic endoscopy", "Lack of skill", "Endoscopy in cancer"], 0,
  "Risk factors: therapeutic endoscopy, lack of skill, endoscopy in cancer. (Book p142)")
q(142, S11, "The typical presentation of iatrogenic esophageal perforation is:",
  ["Chest pain after endoscopy", "Hematemesis after endoscopy",
   "Hoarseness after endoscopy", "Asymptomatic presentation"], 0,
  "C/F: chest pain after endoscopy. (Book p142)")
q(142, S11, "The investigation of choice for esophageal perforation is:",
  ["CECT", "Plain X-ray", "Barium swallow", "Endoscopy"], 0,
  "Ix: CECT is the IOC. (Book p142)")
q(142, S11, "In a stable patient with a small iatrogenic perforation, management includes all of the following EXCEPT:",
  ["Blind NG tube insertion", "Endoscopic sealing with clips or SEMS", "IV fluids", "IV antibiotics"], 0,
  "Stable patient / small perforation: endoscopic sealing with clips or SEMS, IV fluids, IV antibiotics, pain management; no blind NG tube as it increases perforation. (Book p142)")
q(142, S11, "Self expanding metallic stents (SEMS) in esophageal perforation are used to:",
  ["Seal the perforation endoscopically", "Dilate a stricture", "Measure pressures",
   "Deliver radiotherapy"], 0,
  "Endoscopic sealing with clips or SEMS (self expanding metallic stent). (Book p142)")
q(142, S11, "A large perforation or a patient with sepsis is managed by:",
  ["Surgical repair", "Discharge with oral antibiotics", "Observation alone",
   "Endoscopic dilatation"], 0,
  "Large perforation or sepsis: surgical repair. (Book p142)")

# ---------------- p142-143 · BOERHAAVE SYNDROME ----------------
S12 = "Boerhaave Syndrome"
q(142, S12, "Spontaneous esophageal perforation is also known as:",
  ["Boerhaave syndrome", "Mallory Weiss syndrome", "Plummer-Vinson syndrome",
   "Zollinger-Ellison syndrome"], 0,
  "Spontaneous perforation: AKA Boerhaave syndrome. (Book p142)")
q(142, S12, "Spontaneous esophageal perforation occurs in the:",
  ["Lower one third, left posterolateral wall", "Upper one third, anterior wall",
   "Mid esophagus, right wall", "Cervical esophagus"], 0,
  "Spontaneous: site lower 1/3rd (left posterolateral wall). (Book p142)")
q(142, S12, "The classic history in Boerhaave syndrome is:",
  ["Vomiting against a closed glottis in an alcoholic", "Swallowing a fish bone",
   "Chronic heartburn", "Blunt chest trauma"], 0,
  "History: vomiting against a closed glottis; typically an alcoholic. (Book p142)")
q(143, S12, "Mackler's triad of Boerhaave syndrome includes all of the following EXCEPT:",
  ["Hemoptysis", "Chest pain", "Retching", "Subcutaneous emphysema"], 0,
  "Mackler's triad: chest pain, retching, subcutaneous emphysema (crackling on soft tissue palpation). (Book p143)")
q(143, S12, "Hamman's crunch is heard in:",
  ["Boerhaave syndrome on auscultation of the heart", "Achalasia cardia",
   "Zenker's diverticulum", "Barrett's esophagus"], 0,
  "O/E: Hamman's crunch on auscultation of the heart (surgical emphysema). (Book p143)")
q(143, S12, "A Mallory Weiss tear differs from Boerhaave syndrome in that the pathology is:",
  ["A split in mucosa +/- submucosa without perforation",
   "A full thickness perforation", "A muscular tear of the stomach",
   "A rupture of the diaphragm"], 0,
  "Mallory Weiss: split in mucosa +/- submucosal layers; Boerhaave: perforation. (Book p143)")
q(143, S12, "Mallory Weiss syndrome presents with:",
  ["Upper GI haemorrhage", "Mackler's triad", "Subcutaneous emphysema", "Peritonitis"], 0,
  "Mallory Weiss tear: upper GI hemorrhage; Boerhaave: Mackler's triad. (Book p143)")
q(143, S12, "In an unstable patient with suspected Boerhaave syndrome, the investigation done is:",
  ["Contrast study with iohexol (safer than barium if there is a leak)",
   "Barium swallow", "MRI", "Manometry"], 0,
  "Unstable: contrast study (iohexol > diatrizoate) - safer than barium in case of leak through the perforation. (Book p143)")
q(143, S12, "Naclerio's V sign on chest X-ray is seen in:",
  ["Boerhaave syndrome (pneumomediastinum)", "Achalasia cardia", "Schatzki ring",
   "Hiatal hernia"], 0,
  "X-ray: pneumomediastinum, Naclerio's V sign, pleural effusion. (Book p143)")
q(143, S12, "The objectives of management of esophageal perforation are:",
  ["To seal the perforation and provide adequate drainage", "To resect the whole esophagus",
   "To dilate the esophagus", "To perform a gastrostomy only"], 0,
  "Objectives: seal the perforation, adequate drainage. (Book p143)")
q(143, S12, "Management options for large or unstable esophageal perforations include all of the following EXCEPT:",
  ["Immediate primary anastomosis of the two ends",
   "Cervical esophagostomy", "T-tube placement and repair", "Gastrostomy with delayed reconstruction"], 0,
  "Unstable/large: cervical esophagostomy, T-tube placement and repair, esophagostomy plus gastrostomy and delayed anastomosis of the two ends. (Book p143)")

# ---------------- p144 · OTHER ESOPHAGEAL DISORDERS ----------------
S13 = "Other Esophageal Disorders: Schatzki Ring & Dysphagia Lusoria"
q(144, S13, "A Schatzki ring is predominantly composed of:",
  ["Mucosa (mucosal much more than submucosal)", "Muscle", "Fibrous tissue",
   "Cartilage"], 0,
  "Schatzki ring: mucosal >>> submucosal ring. (Book p144)")
q(144, S13, "The site of a Schatzki ring is the:",
  ["Lower esophagus", "Upper esophagus", "Mid esophagus", "Stomach"], 0,
  "Site: lower esophagus. (Book p144)")
q(144, S13, "The typical symptom of a Schatzki ring is:",
  ["Intermittent, non-progressive dysphagia", "Progressive dysphagia with weight loss",
   "Hematemesis", "Odynophagia with fever"], 0,
  "C/F: intermittent, non-progressive dysphagia. (Book p144)")
q(144, S13, "The investigation of choice for a Schatzki ring is:",
  ["Barium swallow", "Manometry", "CT scan", "Endoscopic ultrasound"], 0,
  "Ix: IOC is barium swallow. (Book p144)")
q(144, S13, "The treatment of a Schatzki ring is:",
  ["Balloon dilatation", "Esophagectomy", "Fundoplication", "Botulinum toxin"], 0,
  "Treatment: balloon dilatation. (Book p144)")
q(144, S13, "The C ring described in the lower esophageal rings is associated with:",
  ["Sliding hiatal hernia", "Barrett's esophagus", "Achalasia", "Zenker's diverticulum"], 0,
  "C ring: associated with sliding hiatal hernia. (Book p144)")
q(144, S13, "Dysphagia lusoria is caused by:",
  ["Esophageal compression by an aberrant right subclavian artery",
   "A stricture after corrosive ingestion", "Achalasia cardia", "An esophageal web"], 0,
  "Dysphagia lusoria: esophageal compression due to an aberrant (right) subclavian artery. (Book p144)")

# ---------------- units ----------------
def sec_ids(*labels):
    return [x["id"] for x in Q if x["sec"] in labels]
def first_page(label):
    for x in Q:
        if x["sec"] == label:
            return x["page"]
    return 0

UNIT_DEFS = [
    (S1, "Three infective esophagitides, three looks: candida in the immunocompromised with oral thrush gives shaggy white deposits and worm-like ulcers on barium (treat with antifungals); CMV after transplant or with GvHD gives large geographical/serpiginous ulcers; herpes, with herpes labialis, gives small ulcers with raised margins."),
    (S2, "Feline esophagus - stacked transverse folds in the upper third - is the endoscopic signature of eosinophilic esophagitis (and GERD, which dominates the lower third). Eosinophilic esophagitis is a chronic immune-mediated, food-antigen-driven disease of young adults (20-30 years) showing crepe-paper mucosa, furrows and rings, with > 15-20 eosinophils/HPF on biopsy; treat with topical steroids and PPIs to settle eosinophilia and symptoms."),
    (S3, "Chicago 4.0 classifies motility by high-resolution manometry using three numbers: IRP (raised when the LES will not relax), DCI (amplitude x duration x length - how strong the distal contraction is) and distal latency (below 4.5 s means a spastic disorder)."),
    (S4, "Achalasia - the commonest motility disorder and a premalignant one for squamous carcinoma - is failure of the LES to relax from loss of ganglion cells in Auerbach's plexus of the lower esophagus (the Hirschsprung analogy). Primary is idiopathic ganglion loss; secondary is Chaga's disease; vigorous is rapidly progressive; pseudoachalasia means an underlying malignancy."),
    (S5, "Dysphagia is paradoxically worse for liquids (solid food's own weight opens the sphincter), regurgitation comes first, then weight loss, nocturnal cough and post-prandial choking; aspiration pneumonia is the commonest complication. Manometry is the IOC (raised IRP, failed relaxation), endoscopy rules out cancer, barium shows the bird beak. Chicago: type I no peristalsis, type II panesophageal pressurisation in >= 20% of swallows, type III premature spastic contractions - severity scored by the 4-item Eckardt score (0-3 each)."),
    (S6, "Three tools: botox (relaxes but recurs most, and repeat dosing fibroses - keep it for frail elderly patients), pneumatic dilatation (serial dilatations match myotomy; best in patients over 45, women, a virgin esophagus and type II disease; keep the balloon under 30 mm to limit perforation) and myotomy - Heller's (6 cm above and 2-3 cm below the junction, GERD is the usual price, so add a fundoplication) or POEM (NOTES, circular muscle only, more reflux). Type I prefers Heller's, type II dilatation, type III POEM."),
    (S7, "Diffuse esophageal spasm is a body-of-esophagus disorder (lower two thirds), more often in women, with repetitive simultaneous high-amplitude contractions and no acid reflux: angina-like chest pain and dysphagia, corkscrew/rosary-bead barium, confirmed on manometry. Exclude angina with an ECG first; treat with calcium channel blockers or nitrates, and POEM responds very well."),
    (S8, "Upper third Zenker's and lower third epiphrenic diverticula are pulsion false diverticula; only the mid-esophageal para-bronchial pouch is a true diverticulum containing all layers, dragged out by healed TB or histoplasmosis. Symptomatic or large ones go to surgery."),
    (S9, "Zenker's - cricopharyngeal achalasia - pushes through Killian's dehiscence between thyropharyngeus and cricopharyngeus, starting in the posterior midline and ending up on the left; it raises squamous carcinoma risk. Regurgitation is the earliest symptom, halitosis the give-away, aspiration pneumonia the commonest complication; barium is the IOC, and surgery (diverticulectomy with a linear stapler, or endoscopic diverticulopexy) must be paired with cricopharyngeal myotomy or it comes back."),
    (S10, "Type I sliding hernias slide the GE junction up, are usually silent or just reflux, and are not dangerous - operate (fundoplication) only if symptomatic or large. Type II rolling hernias send stomach alongside a normally positioned GE junction into the chest and can strangulate, so they are always repaired; type III is mixed (the rolling component dictates management) and type IV contains something other than stomach."),
    (S11, "Most perforations are iatrogenic and in the upper third - therapeutic endoscopy, inexperience and cancerous esophagus are the risks; suspect it when chest pain follows endoscopy, confirm with CECT. Small contained leaks in stable patients can be clipped or stented with IV fluids and antibiotics - but never pass a NG tube blind; large leaks or sepsis need surgical repair or T-tube drainage."),
    (S12, "Boerhaave is bursting the lower third on the left posterolateral wall when an alcoholic vomits against a closed glottis: Mackler's triad of chest pain, retching and subcutaneous emphysema, Hamman's crunch over the heart, pneumomediastinum and Naclerio's V sign. Unlike a Mallory-Weiss mucosal split that bleeds, this is a full perforation - CT if stable, iohexol if unstable (it leaks more safely than barium), then seal the hole and drain."),
    (S13, "Schatzki's B ring is a thin mucosal ring low in the esophagus causing intermittent, non-progressive dysphagia - barium shows it and balloon dilatation fixes it (the C ring below is the one seen with a sliding hiatal hernia). Dysphagia lusoria is compression from an aberrant right subclavian artery."),
]

UNITS = []
for i, (title, guide) in enumerate(UNIT_DEFS, 1):
    UNITS.append({"id": f"SURG-U20-{i}", "ch": 20, "n": i, "title": title,
                  "sec": f"{title} · p{first_page(title)}",
                  "qs": sec_ids(title), "guide": guide})

covered = [i for u in UNITS for i in u["qs"]]
assert covered == [x["id"] for x in Q], "units must cover questions in order"

data = {"questions": Q, "units": UNITS}
with open("data/ch20.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
print(f"ch20: {len(Q)} questions, {len(UNITS)} units")
