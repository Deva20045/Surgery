#!/usr/bin/env python3
"""Build data/ch30.json for PULSE Surgery ch30 (Appendix, p208-217)."""
import json

Q = []
def q(page, sec, text, opts, ans, exp):
    Q.append({"id": f"SURG-C30-{len(Q)+1:03d}", "sec": sec, "page": page,
              "q": text, "opts": opts, "ans": ans, "exp": exp})

# ---------------- p208 ----------------
S1 = "Appendix: Anatomy, Position, Blood Supply and Development"
q(208, S1, "The most common position of the appendix is:",
  ["Retrocaecal", "Pelvic", "Preileal", "Postileal"], 0,
  "The retrocaecal position is the commonest site of the appendix, accounting for about 74% of cases. (Book p208)")
q(208, S1, "The least common appendiceal position is:",
  ["Postileal", "Subcaecal", "Paracaecal", "Preileal"], 0,
  "Postileal appendix is the least common position listed on the page, around 0.5%. (Book p208)")
q(208, S1, "Which appendiceal position is present in about 21% of patients?",
  ["Pelvic", "Paracaecal", "Retrocaecal", "Preileal"], 0,
  "Pelvic appendix is shown as the second commonest position, approximately 21%. (Book p208)")
q(208, S1, "Which appendiceal position is approximately 1%?",
  ["Preileal", "Postileal", "Pelvic", "Retrocaecal"], 0,
  "Preileal appendix is labelled as about 1% in the position diagram. (Book p208)")
q(208, S1, "Which of the following correctly matches the less common positions of the appendix with their frequencies?",
  ["Paracaecal 2% and subcaecal 0.5%", "Paracaecal 21% and subcaecal 2%", "Preileal 2% and postileal 1%", "Subcaecal 5% and paracaecal 10%"], 0,
  "The diagram labels paracaecal appendix as about 2% and subcaecal appendix as about 0.5%. (Book p208)")
q(208, S1, "The appendicular base is identified intraoperatively at the:",
  ["Junction of the three taeniae coli", "Ileocecal valve", "Antimesenteric border of terminal ileum", "Tip of caecum"], 0,
  "The base of the appendix is constant in position and lies at the junction of the three taeniae coli. (Book p208)")
q(208, S1, "McBurney's point corresponds to the:",
  ["Base of appendix and point of maximum tenderness", "Tip of appendix and point of rebound", "Midpoint of the inguinal ligament", "Site of obturator tenderness"], 0,
  "McBurney's point marks the base of the appendix and is the site of maximum tenderness in appendicitis. (Book p208)")
q(208, S1, "The appendicular artery usually arises from the:",
  ["Lower division of the ileocolic artery", "Right colic artery", "Middle colic artery", "Posterior caecal artery"], 0,
  "The appendicular artery is a branch of the lower division of the ileocolic artery. (Book p208)")
q(208, S1, "A surgically important feature of the appendicular artery is that it is a:",
  ["End artery", "Paired artery", "Branch of the inferior mesenteric artery", "Terminal branch of the middle colic artery"], 0,
  "The appendicular artery is an end artery, which is why thrombosis can readily precipitate ischemia. (Book p208)")
q(208, S1, "Deficient blood supply close to the tip of appendix predisposes to:",
  ["Thrombosis and perforation", "Volvulus and intussusception", "Bleeding and pseudoaneurysm", "Lymphoma and carcinoid"], 0,
  "The page specifically notes deficient supply near the tip as the site of thrombosis and perforation. (Book p208)")
q(208, S1, "The accessory appendicular artery is also called the:",
  ["Artery of Seshachalam", "Arc of Riolan", "Marginal artery of Drummond", "Artery of Moskowitz"], 0,
  "The accessory appendicular artery is named the artery of Seshachalam. (Book p208)")
q(208, S1, "The accessory appendicular artery most commonly arises from the:",
  ["Posterior caecal artery", "Right colic artery", "Middle colic artery", "Superior rectal artery"], 0,
  "The accessory appendicular artery is described as a branch of the posterior caecal artery. (Book p208)")
q(208, S1, "At birth, the appendix is characteristically:",
  ["Short and broad at its junction with the caecum", "Long and narrow with a fixed retrocaecal position", "Absent in neonates", "Completely extraperitoneal"], 0,
  "Developmentally, the appendix is short and broad at its junction with the caecum at birth. (Book p208)")
q(208, S1, "By about what age does the appendix become tubular in structure?",
  ["2 years", "6 months", "5 years", "10 years"], 0,
  "The developmental note on the page states that by 2 years the appendix becomes a tubular structure. (Book p208)")
q(208, S1, "Growth of the caecum leads to rotation of the appendix into a predominantly __________ position.",
  ["Retrocaecal intraperitoneal", "Pelvic extraperitoneal", "Preileal retroperitoneal", "Postileal extraperitoneal"], 0,
  "With growth of the caecum, the appendix rotates into a retrocaecal, intraperitoneal position. (Book p208)")

# ---------------- p209 ----------------
S2 = "Acute Appendicitis: Types, Causes, Incidence and Classical Clinical Features"
q(209, S2, "The most common type of acute appendicitis is:",
  ["Obstructive appendicitis", "Catarrhal non-obstructive appendicitis", "Gangrenous appendicitis", "Appendicitis in pregnancy"], 0,
  "The chapter classifies obstructive appendicitis as the most common type. (Book p209)")
q(209, S2, "The most common obstructing factor in acute appendicitis is:",
  ["Fecolith", "Foreign body", "Ascariasis", "Carcinoid tumour"], 0,
  "Luminal obstruction by a fecolith is listed as the most common cause of obstructive appendicitis. (Book p209)")
q(209, S2, "All of the following may obstruct the appendiceal lumen EXCEPT:",
  ["Portal pyaemia", "Food particle", "Roundworm", "Carcinoid tumour"], 0,
  "The page lists fecolith, food particle, roundworm/ascariasis, foreign body and carcinoid tumour as obstructive causes; portal pyaemia is a complication, not a cause. (Book p209)")
q(209, S2, "Catarrhal non-obstructive appendicitis is particularly described in:",
  ["Children", "Pregnant women", "Elderly men", "Patients with Crohn's disease"], 0,
  "The non-obstructive catarrhal type is noted on the page as occurring in children. (Book p209)")
q(209, S2, "Approximately what proportion of acute appendicitis is non-obstructive (catarrhal)?",
  ["10-15%", "1-2%", "25-30%", "50-60%"], 0,
  "The chapter gives non-obstructive catarrhal appendicitis a frequency of about 10-15%. (Book p209)")
q(209, S2, "Acute appendicitis is relatively uncommon in:",
  ["Infants and the elderly", "Teenagers and young adults", "Males only", "Pregnant women only"], 0,
  "The incidence section specifically notes that appendicitis is uncommon in infants and the elderly. (Book p209)")
q(209, S2, "Peak incidence of acute appendicitis is in:",
  ["Teens and early twenties", "Neonatal period", "Fifth decade", "Seventh decade"], 0,
  "Acute appendicitis peaks in the teenage years and early twenties. (Book p209)")
q(209, S2, "Regarding sex distribution of acute appendicitis, the chapter states:",
  ["Males are affected more often than females", "Females are affected more often than males", "Both sexes are affected equally", "It occurs only in males"], 0,
  "The incidence note states males are affected more commonly than females. (Book p209)")
q(209, S2, "The most common symptom of acute appendicitis is:",
  ["Pain", "Fever", "Anorexia", "Vomiting"], 0,
  "Pain is listed as the most common symptom of acute appendicitis. (Book p209)")
q(209, S2, "Classically, appendicular pain begins in the __________ and later shifts to the __________.",
  ["Periumbilical region; right iliac fossa", "Right iliac fossa; epigastrium", "Hypogastrium; left iliac fossa", "Flank; umbilicus"], 0,
  "The classical sequence is visceral periumbilical pain followed by migration to the right iliac fossa where it becomes parietal pain. (Book p209)")
q(209, S2, "The early periumbilical pain of acute appendicitis is best described as:",
  ["Visceral pain", "Parietal pain", "Neuropathic pain", "Colicky ureteric pain"], 0,
  "Early appendicular pain is visceral and therefore felt around the umbilicus. (Book p209)")
q(209, S2, "When pain in appendicitis localizes to the right iliac fossa, it reflects:",
  ["Parietal irritation", "Mesenteric ischemia", "Portal hypertension", "Small bowel obstruction"], 0,
  "Once the parietal peritoneum becomes inflamed, the pain shifts to the right iliac fossa and becomes localized. (Book p209)")
q(209, S2, "Murphy's triad in acute appendicitis consists of pain, fever and:",
  ["Nausea/vomiting", "Jaundice", "Constipation", "Diarrhoea"], 0,
  "The triangular diagram on the page places pain, fever, and nausea with vomiting together as Murphy's triad. (Book p209)")
q(209, S2, "Which symptom is listed separately in addition to Murphy's triad in acute appendicitis?",
  ["Anorexia", "Dysphagia", "Melaena", "Jaundice"], 0,
  "Anorexia is listed as another common symptom alongside the classical triad. (Book p209)")
q(209, S2, "A patient who points precisely to McBurney's point as the site of maximum tenderness is demonstrating:",
  ["Pointing sign", "Tenhorn sign", "Aaron sign", "Dunphy sign"], 0,
  "Pointing sign refers to indicating McBurney's point as the site of maximal tenderness. (Book p209)")
q(209, S2, "Rovsing sign is considered positive when:",
  ["Pressure in the left iliac fossa causes pain in the right iliac fossa", "Extension of the hip causes right iliac fossa pain", "Internal rotation of the hip causes pelvic pain", "Coughing produces generalized abdominal pain"], 0,
  "Rovsing sign is positive when pressing the left iliac fossa produces pain in the right iliac fossa. (Book p209)")
q(209, S2, "One mechanism proposed for Rovsing sign is:",
  ["Displacement of bowel and air toward the right, irritating the appendix", "Stretch of the ureter by hip extension", "Compression of the pudendal nerve", "Twisting of the mesoappendix"], 0,
  "The page explains Rovsing sign by displacement of bowel and air to the right, thereby irritating the appendix. (Book p209)")
q(209, S2, "The Cope psoas test may be elicited by all of the following EXCEPT:",
  ["Forced internal rotation of the right hip", "Flexion of the right hip against resistance", "Hyperextension of the right hip", "Producing right iliac fossa pain"], 0,
  "Psoas sign is elicited by flexion of the right hip against resistance or by hyperextension of the right hip; internal rotation belongs to the obturator test. (Book p209)")
q(209, S2, "The obturator sign in appendicitis is produced by pain during:",
  ["Flexion and internal rotation of the right hip", "Hyperextension of the right hip", "Left iliac fossa compression", "Coughing"], 0,
  "The page defines the obturator sign as pain caused by flexion and internal rotation of the right hip. (Book p209)")

# ---------------- p210 ----------------
S3 = "Appendicitis: Location-specific Signs and Investigations"
q(210, S3, "Dunphy sign refers to:",
  ["Pain on coughing", "Pain in epigastrium on pressing RIF", "Pain on pulling the right testis", "Pain on deep inspiration"], 0,
  "Dunphy sign is pain in the right lower abdomen precipitated by coughing. (Book p210)")
q(210, S3, "Aaron sign in appendicitis is:",
  ["Epigastric pain on pressing the right iliac fossa", "Pain on cough", "Pain on hyperextension of hip", "Pain on rectal examination"], 0,
  "Aaron sign is described as pain felt in the epigastrium when the right iliac fossa is pressed. (Book p210)")
q(210, S3, "Tenhorn sign is positive when:",
  ["Pulling the right testis causes right iliac fossa pain", "The left iliac fossa is pressed", "The right hip is internally rotated", "The patient coughs"], 0,
  "Tenhorn sign is pain in the right iliac fossa produced by pulling the right testis. (Book p210)")
q(210, S3, "In retrocaecal appendicitis, abdominal rigidity is typically:",
  ["Absent", "Markedly generalized", "Always associated with guarding", "Present only in children"], 0,
  "Retrocaecal appendicitis may lack the usual anterior peritoneal irritation, so abdominal rigidity can be absent. (Book p210)")
q(210, S3, "Which sign is especially associated with retrocaecal appendicitis?",
  ["Psoas sign", "Obturator sign", "Aaron sign", "Tenhorn sign"], 0,
  "Retrocaecal appendicitis characteristically gives a positive psoas sign. (Book p210)")
q(210, S3, "Pelvic appendicitis commonly causes increased frequency of micturition because of:",
  ["Bladder irritation", "Ureteric obstruction", "Prostatic enlargement", "Detrusor denervation"], 0,
  "A pelvic appendix irritates the bladder, leading to urinary frequency. (Book p210)")
q(210, S3, "Rectal irritation by a pelvic appendix may produce:",
  ["Pelvic diarrhoea and pain on DRE", "Hematemesis and melena", "Constipation without pain", "Jaundice"], 0,
  "Pelvic appendicitis may irritate the rectum, causing pelvic diarrhoea and pain on digital rectal examination. (Book p210)")
q(210, S3, "Which form of appendicitis is described as the most difficult to diagnose because signs may be absent?",
  ["Postileal appendicitis", "Retrocaecal appendicitis", "Pelvic appendicitis", "Catarrhal appendicitis"], 0,
  "The chapter specifically states that postileal appendicitis is the most difficult to diagnose because of paucity of signs. (Book p210)")
q(210, S3, "A clue to postileal appendicitis on examination may be:",
  ["Slight pain on deep pressure", "Marked rigidity", "Visible mass", "Profuse rectal bleeding"], 0,
  "Postileal appendicitis may show little beyond slight pain on deep pressure. (Book p210)")
q(210, S3, "A typical laboratory profile in acute appendicitis includes:",
  ["Raised TLC, neutrophilia with left shift, and raised CRP", "Leukopenia with eosinophilia", "Raised bilirubin alone", "Hyperkalemia with acidosis"], 0,
  "The investigation section lists raised total leukocyte count, neutrophilia with left shift, and elevated CRP. (Book p210)")
q(210, S3, "The preferred imaging test according to age group is correctly matched in:",
  ["Children—USG; adults—CECT", "Children—CECT; adults—plain X-ray", "Children—MRI; adults—USG", "Children—barium enema; adults—USG"], 0,
  "The page advises ultrasound for children and contrast-enhanced CT for adults. (Book p210)")
q(210, S3, "In pregnant women with suspected appendicitis, the imaging options suggested are:",
  ["USG or MRI", "Barium enema or colonoscopy", "CECT only", "PET-CT only"], 0,
  "For pregnancy, the imaging section specifically mentions USG/MRI. (Book p210)")
q(210, S3, "Which ultrasound finding best supports acute appendicitis?",
  ["Blind-ending tubular structure", "Target lesion in liver", "Double bubble sign", "Apple-core lesion"], 0,
  "A blind-ending tubular structure is the classic ultrasonographic appearance of an inflamed appendix. (Book p210)")
q(210, S3, "Which of the following is NOT listed as an ultrasonographic feature of appendicitis on the page?",
  ["Portal venous gas", "Probe tenderness", "Periappendiceal fluid collection", "Appendicolith/fecolith"], 0,
  "The page lists blind-ending tubular structure, probe tenderness, periappendiceal fluid, and appendicolith/fecolith; portal venous gas is not listed. (Book p210)")

# ---------------- p211 ----------------
S4 = "Alvarado Score, Differential Diagnosis and Conservative Management"
q(211, S4, "In the Alvarado score, migration of pain to the right lower quadrant scores:",
  ["1 point", "2 points", "3 points", "0 points"], 0,
  "Migration of pain to the right lower quadrant carries 1 point in the Alvarado score. (Book p211)")
q(211, S4, "Tenderness in the right lower quadrant contributes how many Alvarado points?",
  ["2 points", "1 point", "3 points", "0 points"], 0,
  "Right lower quadrant tenderness is one of the heavier-weighted criteria and scores 2 points. (Book p211)")
q(211, S4, "Leukocytosis in the Alvarado score is worth:",
  ["2 points", "1 point", "3 points", "0 points"], 0,
  "Leukocytosis contributes 2 points in the Alvarado system. (Book p211)")
q(211, S4, "Shift of white blood cells to the left in the Alvarado score is worth:",
  ["1 point", "2 points", "3 points", "0 points"], 0,
  "A left shift contributes 1 point in the original Alvarado score. (Book p211)")
q(211, S4, "Which of the following is NOT a 1-point item in the Alvarado score?",
  ["Leukocytosis", "Migration of pain", "Anorexia", "Nausea and vomiting"], 0,
  "Migration of pain, anorexia, nausea/vomiting, rebound pain, fever, and left shift each score 1; leukocytosis scores 2. (Book p211)")
q(211, S4, "What is the maximum total Alvarado score shown in the chapter?",
  ["10", "8", "9", "12"], 0,
  "The table totals the Alvarado score to a maximum of 10. (Book p211)")
q(211, S4, "An Alvarado score below 5 is interpreted as:",
  ["Unlikely appendicitis", "Need immediate surgery", "Highly likely appendicitis", "Perforated appendix"], 0,
  "The interpretation table classifies a score below 5 as unlikely appendicitis. (Book p211)")
q(211, S4, "An Alvarado score of 5-8 suggests that appendicitis should be:",
  ["Confirmed with ultrasound", "Treated with immediate right hemicolectomy", "Managed as pancreatitis", "Considered ruled out"], 0,
  "The table advises that a score of 5-8 should be confirmed with ultrasound. (Book p211)")
q(211, S4, "An Alvarado score of 9-10 makes acute appendicitis:",
  ["Highly likely", "Unlikely", "Possible only in children", "Limited to pregnancy"], 0,
  "A score of 9-10 is interpreted as highly likely appendicitis. (Book p211)")
q(211, S4, "The Alvarado score is particularly useful because it has a high:",
  ["Negative predictive value", "Positive blood culture rate", "Rate of diagnosing carcinoid", "Need for MRI"], 0,
  "The page explicitly notes the score has a high negative predictive value. (Book p211)")
q(211, S4, "The modified Alvarado score differs from the original because it does NOT include:",
  ["Shift of white blood cells to the left", "Anorexia", "Tenderness in RLQ", "Elevated temperature"], 0,
  "The modified Alvarado score omits the left shift component. (Book p211)")
q(211, S4, "A child with right iliac fossa pain, high fever and enlarged mesenteric lymph nodes most likely has:",
  ["Mesenteric adenitis due to Yersinia", "Mittelschmerz", "Ureteric colic", "PID"], 0,
  "The differential section highlights Yersinia mesenteric adenitis in children, especially when fever is high and nodes are enlarged. (Book p211)")
q(211, S4, "A common differential diagnosis of appendicitis in infants and children is:",
  ["Intussusception", "Cervicitis", "Prostate abscess", "Diverticulosis"], 0,
  "Among children, the page lists intussusception as an important differential diagnosis. (Book p211)")
q(211, S4, "An adult woman with cyclical mid-cycle pain mimicking appendicitis is likely experiencing:",
  ["Mittelschmerz", "Torsion", "Mesenteric adenitis", "Crohn's disease"], 0,
  "Mittelschmerz is specifically described as mid-cycle ovulatory pain in adult females. (Book p211)")
q(211, S4, "Which of the following is an adult/elderly differential diagnosis for appendicitis according to the page?",
  ["Ureteric colic", "Juvenile polyp", "Pyloric stenosis", "Hirschsprung disease"], 0,
  "For adults and the elderly, the chapter lists ureteric colic among the common differentials. (Book p211)")
q(211, S4, "Conservative management of appendicitis includes all EXCEPT:",
  ["Oral laxatives and high-fibre diet", "Nil per oral", "IV fluids", "IV antibiotics"], 0,
  "The conservative plan is NPO, IV fluids, IV antibiotics with aerobic and anaerobic cover, and painkillers; laxatives/high-fibre diet are not part of this page's regimen. (Book p211)")
q(211, S4, "When nonoperative management is used for appendicitis, antibiotic coverage should include:",
  ["Aerobic and anaerobic organisms", "Only viruses", "Only fungi", "Only protozoa"], 0,
  "The chapter specifically advises IV antibiotics covering both aerobic and anaerobic organisms. (Book p211)")
q(211, S4, "The anaerobic organism specifically mentioned in the conservative antibiotic plan for appendicitis is:",
  ["Bacteroides", "Helicobacter", "Candida", "Giardia"], 0,
  "Bacteroides is named as the anaerobic target in conservative therapy. (Book p211)")
q(211, S4, "A major disadvantage of conservative management in appendicitis is:",
  ["High recurrence rate", "Inevitable sterility", "Compulsory right hemicolectomy later", "Risk of thyroid cancer"], 0,
  "The page points out the main drawback of conservative treatment is a high recurrence rate. (Book p211)")

# ---------------- p212-213 ----------------
S5 = "Appendicectomy: Incisions, Laparoscopy, Intraoperative Scenarios and Postoperative Complications"
q(212, S5, "The gridiron incision used for open appendicectomy is a:",
  ["Muscle-splitting incision", "Lower midline incision", "Muscle-cutting incision", "Subcostal incision"], 0,
  "The page identifies the gridiron incision as a muscle-splitting incision. (Book p212)")
q(212, S5, "Rutherford Morrison's incision is described as a:",
  ["Muscle-cutting incision", "Muscle-splitting incision", "Transanal incision", "Thoracoabdominal incision"], 0,
  "Rutherford Morrison's incision is specifically labeled muscle cutting. (Book p212)")
q(212, S5, "Which muscles are cut in Rutherford Morrison's incision?",
  ["External oblique, internal oblique and transversus abdominis", "Rectus abdominis only", "Psoas and iliacus", "External oblique only"], 0,
  "The page lists external oblique, internal oblique and transversus abdominis under the muscle-cutting incision. (Book p212)")
q(212, S5, "Lanz incision is also known as the:",
  ["Skin crease or bikini incision", "Kocher incision", "Chevron incision", "Pfannenstiel incision"], 0,
  "Lanz incision is described as the skin crease or bikini incision. (Book p212)")
q(212, S5, "The Lanz incision is placed approximately:",
  ["2 cm below the umbilicus", "At the tip of the 12th rib", "Along the costal margin", "At the midline above the umbilicus"], 0,
  "The page notes the Lanz incision as lying about 2 cm below the umbilicus. (Book p212)")
q(212, S5, "In appendicular perforation, the incision specifically mentioned is:",
  ["Lower midline abdominal incision", "Lanz incision", "Gridiron incision", "Rutherford Morrison only"], 0,
  "The lower midline abdominal incision is mentioned as being used in appendicular perforation. (Book p212)")
q(212, S5, "Which structure is encountered immediately after skin during open appendicectomy?",
  ["Superficial fascia", "External oblique aponeurosis", "Peritoneum", "Preperitoneal fat"], 0,
  "The listed order starts with skin followed by superficial fascia. (Book p212)")
q(212, S5, "The superficial fascia encountered in appendicectomy consists of:",
  ["Camper's and Scarpa's fascia", "Colles' and Buck's fascia", "Denonvilliers' fascia and Gerota's fascia", "Camper's fascia alone"], 0,
  "The page explicitly labels superficial fascia as Camper's and Scarpa's. (Book p212)")
q(212, S5, "How many ports are shown for laparoscopic appendicectomy?",
  ["3", "2", "4", "1"], 0,
  "The laparoscopic diagram on the page shows a three-port technique. (Book p212)")
q(212, S5, "A standard laparoscopic appendicectomy port setup includes all EXCEPT:",
  ["Right hypochondrial port", "Infraumbilical port", "Left iliac fossa port", "Suprapubic port"], 0,
  "The chapter shows infraumbilical, left iliac fossa and suprapubic ports; a right hypochondrial port is not listed. (Book p212)")
q(212, S5, "The larger laparoscopic port shown for appendicectomy is the:",
  ["Infraumbilical 12 mm port", "Left iliac fossa 12 mm port", "Suprapubic 12 mm port", "None larger than 5 mm"], 0,
  "The port diagram labels the infraumbilical port as 12 mm, with the others as 5 mm. (Book p212)")
q(212, S5, "The first operative step in appendicectomy is to locate the appendix by finding the:",
  ["Junction of the three taeniae coli", "Ileocecal valve", "Falciform ligament", "Pouch of Douglas"], 0,
  "Whether open or laparoscopic, the appendix is first identified at the convergence of the three taeniae coli. (Book p212)")
q(212, S5, "After identifying the appendix, the next essential step is to:",
  ["Ligate the appendicular artery and bare the appendix", "Perform right hemicolectomy", "Open the rectum", "Milk the caecum"], 0,
  "The stepwise sequence on the page is to ligate the appendicular artery and bare the appendix. (Book p212)")
q(212, S5, "To reduce the risk of stump appendicitis, the appendiceal stump should usually be kept:",
  ["Less than 4-5 mm", "More than 2 cm", "Exactly 1 cm", "Equal to caecal wall thickness"], 0,
  "The operative illustration specifically recommends a stump length below 4-5 mm. (Book p212)")
q(213, S5, "If the appendix cannot be found during surgery, the surgeon should:",
  ["Locate the taeniae coli and follow them to their junction", "Convert immediately to subtotal colectomy", "Search the sigmoid colon first", "Abandon the procedure"], 0,
  "When the appendix is not obvious, following the taeniae coli to their junction leads to the appendicular base. (Book p213)")
q(213, S5, "If the appendix appears normal at operation, the surgeon should inspect the:",
  ["Last 2 feet of ileum for Meckel's diverticulum", "Duodenum for ulcer", "Sigmoid for volvulus", "Omentum for hydatid cyst"], 0,
  "The chapter advises checking the last 2 feet of ileum for Meckel's diverticulum if the appendix is not inflamed. (Book p213)")
q(213, S5, "If an inflamed Meckel's diverticulum is found while the appendix is normal, the recommended treatment is:",
  ["Resection and anastomosis", "Appendicectomy alone", "Conservative treatment only", "Stricturoplasty"], 0,
  "The Meckel's algorithm on the page shows inflamed Meckel's diverticulum should be resected and anastomosed. (Book p213)")
q(213, S5, "If Meckel's diverticulum is not inflamed when the appendix is being explored, the page advises:",
  ["Appendicectomy", "Right hemicolectomy", "Ileocecal bypass", "No procedure at all"], 0,
  "The flowchart states that if Meckel's is not inflamed, appendicectomy is done. (Book p213)")
q(213, S5, "In an inflamed appendiceal base, which intraoperative maneuver should be avoided?",
  ["Crushing the base", "Burying the base", "Using a purse-string suture", "Using a linear stapler when caecal base is healthy"], 0,
  "The page clearly says not to crush an inflamed appendiceal base. (Book p213)")
q(213, S5, "If the appendiceal base is inflamed, the stump is commonly dealt with by:",
  ["Burying it with a purse-string suture or Z-stitch", "Leaving it open", "Stapling the terminal ileum", "Exteriorizing the caecum as a stoma"], 0,
  "The chapter specifically recommends burying the inflamed base with a purse-string or Z stitch. (Book p213)")
q(213, S5, "A linear stapler may be used for an inflamed appendiceal base when the:",
  ["Caecal base is healthy", "Patient is pregnant", "Appendix is pelvic", "Tip alone is gangrenous"], 0,
  "The page notes that a linear stapler is appropriate if the caecal base remains healthy. (Book p213)")
q(213, S5, "If the appendiceal base and adjacent caecal wall are gangrenous, the operation of choice is:",
  ["Right hemicolectomy", "Simple appendicectomy", "Transverse colectomy", "Ileostomy alone"], 0,
  "Gangrene involving the appendiceal base and adjoining caecal wall requires right hemicolectomy. (Book p213)")
q(213, S5, "In appendicitis associated with Crohn's disease, appendicectomy is safest when the caecum is:",
  ["Healthy", "Inflamed", "Perforated", "Retrocaecal"], 0,
  "The Crohn's algorithm says appendicectomy is done when the caecum is healthy, lowering fistula risk. (Book p213)")
q(213, S5, "When the caecum is inflamed in Crohn's disease with appendicitis, the preferred approach is:",
  ["Conservative management", "Immediate appendicectomy", "Right hemicolectomy in all", "Interval appendicectomy after 24 hours"], 0,
  "If the caecum is inflamed in Crohn's disease, the page recommends conservative management because appendicectomy raises fistula risk. (Book p213)")
q(213, S5, "The most common postoperative complication after appendicectomy is:",
  ["Wound infection", "Portal pyaemia", "Right inguinal hernia", "Stump appendicitis"], 0,
  "Wound infection is marked as the most common complication following appendicectomy. (Book p213)")
q(213, S5, "Injury to the right iliohypogastric nerve during appendicectomy predisposes to:",
  ["Right inguinal hernia", "Femoral hernia", "Stress incontinence", "Appendicular lump"], 0,
  "The page links right iliohypogastric nerve injury with later risk of right inguinal hernia. (Book p213)")
q(213, S5, "Fever with pelvic diarrhoea after appendicectomy should raise suspicion of:",
  ["Pelvic abscess", "Stump appendicitis", "Pseudomyxoma peritonei", "Carcinoid syndrome"], 0,
  "Pelvic abscess is specifically described as presenting with fever and pelvic diarrhoea. (Book p213)")
q(213, S5, "The investigation of choice for suspected postoperative pelvic abscess is:",
  ["CECT", "Barium meal", "Proctoscopy", "MRCP"], 0,
  "The note under pelvic abscess specifies CECT as the investigation. (Book p213)")
q(213, S5, "Stump appendicitis is more likely when the appendiceal stump measures:",
  [">4-5 mm", "<2 mm", "Exactly 1 mm", "0 mm"], 0,
  "A residual stump longer than 4-5 mm raises the risk of stump appendicitis. (Book p213)")
q(213, S5, "Appendicectomy performed as an emergency procedure is classified as a:",
  ["Contaminated wound", "Clean wound", "Dirty wound", "Clean-contaminated wound"], 0,
  "The wound classification note on the page labels emergency appendicectomy as contaminated. (Book p213)")
q(213, S5, "Elective appendicectomy is classified as a:",
  ["Clean-contaminated wound", "Clean wound", "Dirty wound", "Contaminated wound"], 0,
  "The note classifies elective appendicectomy as clean-contaminated. (Book p213)")
q(213, S5, "The 'policeman of the abdomen' in appendicular inflammation is the:",
  ["Greater omentum", "Lesser omentum", "Mesoappendix", "Parietal peritoneum"], 0,
  "The page calls the greater omentum the policeman of the abdomen because it walls off inflamed appendix. (Book p213)")
q(213, S5, "Which factor predisposes children to appendicular perforation?",
  ["Underdeveloped greater omentum", "Early calcification of the appendix", "Large mesoappendix", "Hyperplasia of taeniae coli"], 0,
  "Children perforate early because the protective greater omentum is underdeveloped. (Book p213)")
q(213, S5, "Appendicular perforation in the elderly is favoured by:",
  ["Atherosclerosis of the walls of the greater omentum", "Hypertrophy of the appendix", "Redundant sigmoid", "Liver cirrhosis"], 0,
  "In the elderly, atherosclerosis in the omental vessels weakens this protective barrier and promotes perforation. (Book p213)")
q(213, S5, "Which of the following is listed as a risk factor for quick appendicular perforation?",
  ["Presence of an appendicolith", "Long appendix", "Hyperplastic polyp", "Portal vein thrombosis"], 0,
  "The page states that presence of an appendicolith leads to quick perforation. (Book p213)")

# ---------------- p214-217 ----------------
S6 = "Appendicular Peritonitis, Pregnancy, Appendicular Lump and Appendicular Tumours"
q(214, S6, "Generalized peritonitis due to appendicular perforation classically shows all EXCEPT:",
  ["Shifting dullness", "Rebound tenderness", "Guarding", "Rigidity"], 0,
  "The page lists rebound tenderness, guarding, and rigidity as features of peritonitis; shifting dullness is not part of that list. (Book p214)")
q(214, S6, "The recommended incision for appendicitis presenting with diffuse peritonitis is:",
  ["Lower midline incision", "Lanz incision", "Gridiron incision", "Subcostal incision"], 0,
  "For appendicitis with peritonitis, the chapter recommends appendicectomy by lower midline incision. (Book p214)")
q(214, S6, "Appendicitis is the most common __________ abdominal emergency in pregnancy.",
  ["Non-obstetric", "Obstetric", "Hepatobiliary", "Urological"], 0,
  "The chapter explicitly labels appendicitis as the most common non-obstetric abdominal emergency in pregnancy. (Book p214)")
q(214, S6, "Pain of appendicitis in pregnancy is most commonly felt in the:",
  ["Right iliac fossa", "Epigastrium", "Left iliac fossa", "Right hypochondrium in all patients"], 0,
  "Even in pregnancy, most patients still present with pain in the right iliac fossa, though in some it may be slightly higher. (Book p214)")
q(214, S6, "If ultrasound is inconclusive in pregnant appendicitis, the next imaging study suggested is:",
  ["MRI", "CECT", "PET-CT", "Barium enema"], 0,
  "The imaging algorithm for pregnancy advises MRI when ultrasound is inconclusive. (Book p214)")
q(214, S6, "Delayed diagnosis or perforation of appendicitis in pregnancy increases the risk of:",
  ["Fetal loss and preterm labour", "Placenta accreta", "Post-term pregnancy", "Hydatidiform mole"], 0,
  "The significance note directly links untreated/perforated appendicitis in pregnancy with fetal loss and preterm labour. (Book p214)")
q(214, S6, "According to the chapter, laparoscopic appendicectomy in pregnancy is:",
  ["Allowed in all trimesters", "Restricted to the second trimester only", "Contraindicated in the first trimester", "Contraindicated throughout pregnancy"], 0,
  "The treatment line explicitly says laparoscopic appendicectomy can be done in all trimesters. (Book p214)")
q(214, S6, "In the comparison note on pregnancy-related abdominal emergencies, cholecystitis is managed by laparoscopic cholecystectomy in the:",
  ["Second trimester", "First trimester", "Third trimester", "Postpartum period only"], 0,
  "The chapter contrasts appendicitis with cholecystitis and notes laparoscopic cholecystectomy in the second trimester. (Book p214)")
q(214, S6, "In the pregnancy algorithm, diffuse peritonitis mandates:",
  ["Resuscitation followed by operation", "Observation with serial ultrasound", "MRI first", "Conservative treatment only"], 0,
  "The management flowchart directs that diffuse peritonitis in pregnancy should be resuscitated and operated upon. (Book p214)")
q(214, S6, "An appendicular lump is best described as:",
  ["A jumbled mass of omentum and bowel over the inflamed appendix", "A mucinous ovarian neoplasm", "A thrombosed hemorrhoid", "A Meckel's diverticulum"], 0,
  "The page defines appendicular lump as omentum and bowel matted over the inflamed appendix. (Book p214)")
q(215, S6, "A classical clinical clue to appendicular lump is:",
  ["Previous acute right iliac fossa pain with a palpable RIF mass", "Painless jaundice with hepatomegaly", "Mass in the left iliac fossa after constipation", "Haematemesis with epigastric lump"], 0,
  "The page describes appendicular lump by a history of acute RIF pain and a right iliac fossa mass on examination. (Book p215)")
q(215, S6, "Ochsner-Sherren regimen is essentially:",
  ["Expectant/non-operative management", "Emergency appendicectomy", "Laparoscopic drainage", "Right hemicolectomy"], 0,
  "Ochsner-Sherren regimen is the classical expectant non-operative treatment for appendicular lump. (Book p215)")
q(215, S6, "Which parameter is monitored during Ochsner-Sherren treatment of appendicular lump?",
  ["Size of lump", "Portal vein pressure", "CEA level", "Urinary ketones"], 0,
  "The monitoring list includes vitals, temperature, pain, and the size of the lump. (Book p215)")
q(215, S6, "Which of the following indicates recovery during conservative management of appendicular lump?",
  ["Fall in pulse rate, fever, lump size and TLC", "Rise in pulse rate and fever", "Development of chills and rigors", "Increasing lump size"], 0,
  "Recovery is marked by decreased pulse, lower fever, shrinking lump, and falling TLC. (Book p215)")
q(215, S6, "After recovery from an appendicular lump, interval appendicectomy is advised after:",
  ["6 weeks", "48 hours", "3 months", "1 year"], 0,
  "The page recommends interval appendicectomy 6 weeks after recovery from appendicular lump. (Book p215)")
q(215, S6, "During conservative treatment of appendicular lump, worsening with chills, rising TLC and increasing lump size suggests:",
  ["Appendicular abscess", "Recovered lump", "Pseudomyxoma peritonei", "Stump appendicitis"], 0,
  "A worsening course with fever, chills, larger lump, and rising TLC indicates appendicular abscess formation. (Book p215)")
q(215, S6, "The preferred drainage route for appendicular abscess in the chapter is:",
  ["Extraperitoneal drainage with pigtail catheter", "Transanal drainage", "Thoracic drainage", "Simple aspiration without catheter"], 0,
  "Appendicular abscess is managed by extraperitoneal drainage, often with a pigtail catheter. (Book p215)")
q(215, S6, "The most common appendicular tumour is:",
  ["Neuroendocrine tumour (carcinoid)", "Adenocarcinoma", "GIST", "Lymphoma"], 0,
  "The page states that the most common appendicular tumour is neuroendocrine tumour/carcinoid tumour. (Book p215)")
q(215, S6, "The appendix is the most common site for which tumour mentioned in the chapter?",
  ["Neuroendocrine tumour", "Lipoma", "Leiomyoma", "Hydatid cyst"], 0,
  "Under appendicular tumour, the page specifically notes the appendix as the most common site for NET/carcinoid. (Book p215)")
q(215, S6, "Most appendiceal neuroendocrine tumours arise at the:",
  ["Tip", "Base", "Mesoappendix", "Appendiceal orifice"], 0,
  "The chapter labels the tip as the site of about 70% of appendiceal NETs. (Book p215)")
q(215, S6, "The usual age group for appendiceal neuroendocrine tumour is:",
  ["40-50 years", "First decade", "Teenage years", "After 70 years"], 0,
  "Appendiceal NET is shown as a tumour of 40-50 years in this chapter. (Book p215)")
q(215, S6, "Diagnosis of appendiceal NET is often:",
  ["Incidental", "Made by barium enema", "Based on CEA elevation alone", "Clinically obvious with carcinoid syndrome"], 0,
  "The page states that appendiceal NET is often diagnosed incidentally. (Book p215)")
q(215, S6, "Immunohistochemical markers used for appendiceal NET include:",
  ["Synaptophysin and chromogranin A", "CEA and CA 19-9", "AFP and PIVKA", "S100 and HMB-45"], 0,
  "Synaptophysin and chromogranin A are the IHC stains listed for appendiceal NET. (Book p215)")
q(216, S6, "An appendiceal NET larger than 2 cm or close to the base is managed by:",
  ["Right hemicolectomy", "Simple appendicectomy alone", "Observation only", "Chemoradiation"], 0,
  "The treatment flowchart directs right hemicolectomy for tumours more than 2 cm or close to the base. (Book p216)")
q(216, S6, "A small appendiceal NET under 1 cm and away from the base is treated with:",
  ["Simple appendicectomy with removal of mesoappendix", "Right hemicolectomy", "Total colectomy", "Chemotherapy alone"], 0,
  "For NET less than 1 cm and away from the base, the chart advises simple appendicectomy and removal of mesoappendix. (Book p216)")
q(216, S6, "A 1-2 cm appendiceal NET warrants right hemicolectomy in the chapter when it is:",
  ["Poorly differentiated or stage T4", "At the tip and asymptomatic", "Associated with fever only", "Seen in a child"], 0,
  "The page specifically escalates 1-2 cm appendiceal NETs to right hemicolectomy when they are poorly differentiated or stage T4. (Book p216)")
q(216, S6, "The most important prognostic factor in appendiceal NET is:",
  ["Tumour size", "Sex of patient", "Presence of fever", "Site of pain"], 0,
  "The page clearly states that size is the most important prognostic factor. (Book p216)")
q(216, S6, "Tumour grade in appendiceal NET is determined by:",
  ["Mitotic index and Ki-67", "CEA and CA 19-9", "PT and INR", "Bilirubin and albumin"], 0,
  "Grade is determined by mitotic index and Ki-67 according to the chapter. (Book p216)")
q(216, S6, "Goblet cell carcinoma of appendix is best described as:",
  ["A rare tumour with both neuroendocrine and glandular differentiation", "A true benign NET", "A purely squamous malignancy", "A hamartomatous lesion"], 0,
  "Goblet cell carcinoma is rare, not a true NET, and shows both neuroendocrine and glandular differentiation. (Book p216)")
q(216, S6, "Compared with ordinary appendiceal NET, goblet cell carcinoma has greater tendency for:",
  ["Nodal and peritoneal dissemination", "Spontaneous regression", "Portal hypertension", "Biliary obstruction"], 0,
  "The page notes higher propensity for nodal and peritoneal dissemination in goblet cell carcinoma than in NET. (Book p216)")
q(216, S6, "Goblet cell carcinoma of the appendix is treated as:",
  ["Adenocarcinoma with right radical hemicolectomy plus chemotherapy", "Simple appendicitis", "Squamous carcinoma with radiotherapy alone", "Lymphoma with steroids"], 0,
  "Management is the same as adenocarcinoma: right radical hemicolectomy with chemotherapy. (Book p216)")
q(216, S6, "Disseminated peritoneal adenomucinosis (DPAM) is characterized in the chapter as:",
  ["Locally invasive and slow growing", "Highly metastatic to lung", "A benign self-limiting infection", "A vascular malformation"], 0,
  "DPAM is specifically described as locally invasive and slow growing. (Book p216)")
q(216, S6, "Peritoneal mucinous carcinomatosis (PMCA) differs from DPAM because it is:",
  ["More aggressive and associated with distant metastasis", "Never invasive", "Confined to the appendix", "A pseudopolyp"], 0,
  "The page contrasts PMCA with DPAM by noting PMCA is more aggressive and shows distant metastasis. (Book p216)")
q(216, S6, "Which resection status means microscopic freedom from disease?",
  ["R0", "R1", "R2", "Rx"], 0,
  "R0 resection means no microscopic residual disease remains. (Book p216)")
q(216, S6, "Which resection status indicates microscopic disease is left behind?",
  ["R1", "R0", "R2", "M1"], 0,
  "R1 means disease persists microscopically after resection. (Book p216)")
q(216, S6, "Which resection status indicates gross disease is left behind?",
  ["R2", "R1", "R0", "T4"], 0,
  "R2 resection means macroscopic or gross disease remains. (Book p216)")
q(217, S6, "Pseudomyxoma peritonei refers to:",
  ["Peritoneal cavity filled with mucin-like material", "Purulent contamination from perforated appendix", "Blood-filled peritoneal cavity", "Tuberculous ascites"], 0,
  "The chapter defines pseudomyxoma peritonei as the peritoneal cavity being filled with mucin-like substance. (Book p217)")
q(217, S6, "The commonest source of pseudomyxoma peritonei mentioned in this appendix chapter is:",
  ["Appendiceal mucinous neoplasms", "Hemorrhoids", "Gallbladder cancer", "Peptic ulcer perforation"], 0,
  "The causes listed for pseudomyxoma peritonei include appendiceal mucinous neoplasms, ovarian mucinous neoplasms, and primary peritoneal cancer. (Book p217)")
q(217, S6, "Progressive abdominal distention with bowel obstruction in a patient with appendiceal mucinous neoplasm suggests:",
  ["Pseudomyxoma peritonei", "Portal pyaemia", "Appendicular lump", "Retrocaecal appendicitis"], 0,
  "The clinical features of pseudomyxoma peritonei on this page are progressive abdominal distention and bowel obstruction. (Book p217)")
q(217, S6, "The CT finding specifically mentioned in pseudomyxoma peritonei is:",
  ["Mucin deposits in the omentum", "Gas under diaphragm", "String sign", "Target sign"], 0,
  "Investigation by CECT demonstrates mucin deposits in the omentum. (Book p217)")
q(217, S6, "A tissue diagnosis in pseudomyxoma peritonei can be obtained by:",
  ["Omental biopsy", "Thyroid FNAC", "Liver biopsy only", "Bone marrow biopsy"], 0,
  "The investigation list includes omental biopsy for diagnosis. (Book p217)")
q(217, S6, "Cytoreductive surgery for pseudomyxoma peritonei may include all EXCEPT:",
  ["Splenectomy as mandatory in every patient", "Appendicectomy", "Omentectomy", "Stripping of peritoneum and removal of mucin"], 0,
  "The page lists appendicectomy, right hemicolectomy when appendix is primarily involved, omentectomy, peritoneal stripping, and in females TAH with BSO; routine mandatory splenectomy is not listed. (Book p217)")
q(217, S6, "If the appendix is the primary site involved in pseudomyxoma peritonei, the colorectal resection advised is:",
  ["Right hemicolectomy", "Left hemicolectomy", "Sigmoidectomy", "APR"], 0,
  "Primary appendiceal involvement is treated with right hemicolectomy in the cytoreductive plan. (Book p217)")
q(217, S6, "In women undergoing cytoreduction for pseudomyxoma peritonei, the gynecologic procedure mentioned is:",
  ["TAH with bilateral salpingo-oophorectomy", "Myomectomy", "Unilateral oophorectomy only", "Cervical conization"], 0,
  "The page specifically includes total abdominal hysterectomy with bilateral salpingo-oophorectomy in females. (Book p217)")
q(217, S6, "HIPEC in pseudomyxoma peritonei uses chemotherapy heated to approximately:",
  ["40-41°C", "32-33°C", "45-46°C", "50-52°C"], 0,
  "The HIPEC note specifies heated chemotherapy at about 40-41°C. (Book p217)")
q(217, S6, "Which drugs are listed for HIPEC in this chapter?",
  ["Mitomycin C and paclitaxel", "Cisplatin and bleomycin", "5-FU and irinotecan", "Sorafenib and pembrolizumab"], 0,
  "The HIPEC regimen listed on the page uses mitomycin-C and paclitaxel. (Book p217)")
q(217, S6, "After instillation during HIPEC, the chemotherapy is drained after:",
  ["30 minutes", "5 minutes", "2 hours", "24 hours"], 0,
  "The chapter states the heated chemotherapy is drained after 30 minutes. (Book p217)")
q(217, S6, "A stated advantage of HIPEC is:",
  ["Improved local control and enhanced efficacy of chemotherapy", "Elimination of need for surgery", "Prevention of appendicitis recurrence", "Direct relief of ureteric colic"], 0,
  "The page notes HIPEC is advised for local control and to improve the efficacy of chemotherapy. (Book p217)")

# ---------------- units ----------------
def sec_ids(*labels):
    return [x["id"] for x in Q if x["sec"] in labels]

def first_page(label):
    for x in Q:
        if x["sec"] == label:
            return x["page"]
    return 0

UNIT_DEFS = [
    (S1, "Start with fixed anatomy. Retrocaecal is the common position, postileal the rare one, and the appendicular base is the dependable landmark at the meeting point of the three taeniae coli. The artery is an end artery running in the mesoappendix, so tip ischemia and perforation matter; remember also the accessory artery of Seshachalam and the developmental shift toward a retrocaecal intraperitoneal appendix."),
    (S2, "Acute appendicitis is usually obstructive and most often blocked by a fecolith, peaking in teenage and early adult males. Clinically the story is classic: visceral periumbilical pain migrates to the right iliac fossa, bringing Murphy's triad, anorexia, McBurney tenderness and the bedside signs every exam expects."),
    (S3, "Next come the subtleties - Dunphy, Aaron and Tenhorn - and then the location-specific clues. Retrocaecal appendicitis may hide rigidity, pelvic appendicitis irritates bladder and rectum, and postileal disease can be the most elusive. Support the diagnosis with leukocytosis, left shift, CRP, age-appropriate imaging, and ultrasound findings such as a blind-ending tubular structure or appendicolith."),
    (S4, "The Alvarado table must be usable, not merely memorized: tenderness and leukocytosis weigh 2 points each, the rest score 1, and the whole system totals 10 with a strong negative predictive value. The modified score drops the left shift. Finish the page by separating pediatric mimics, adult causes, female gynecologic mimics, and when conservative treatment is chosen, its elements and limitation - recurrence."),
    (S5, "Open appendicectomy lives in its incisions: gridiron splits muscle, Rutherford Morrison cuts it, Lanz is the bikini incision, and perforation may need a lower midline approach. Laparoscopy uses three ports and a short stump. Intraoperatively, follow taeniae coli if lost, check the distal ileum when the appendix is normal, respect an inflamed base, and know the complications - especially wound infection, pelvic abscess and stump appendicitis."),
    (S6, "This final run through the chapter covers the dangerous variants and the tumors. Peritonitis and pregnancy change incision choice, imaging, and urgency; appendicular lump demands disciplined Ochsner-Sherren monitoring and delayed surgery unless it suppurates. Then switch gears to appendiceal tumours: NET by size and base, goblet cell carcinoma as adenocarcinoma, and finally pseudomyxoma peritonei with cytoreduction and HIPEC."),
]

UNITS = []
for i, (title, guide) in enumerate(UNIT_DEFS, 1):
    UNITS.append({"id": f"SURG-U30-{i}", "ch": 30, "n": i, "title": title,
                  "sec": f"{title} · p{first_page(title)}", "qs": sec_ids(title),
                  "guide": guide})

covered = [i for u in UNITS for i in u["qs"]]
assert covered == [x["id"] for x in Q], "units must cover questions in order"

data = {"questions": Q, "units": UNITS}
with open("data/ch30.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
print(f"ch30: {len(Q)} questions, {len(UNITS)} units")
