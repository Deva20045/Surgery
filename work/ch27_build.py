#!/usr/bin/env python3
"""Build data/ch27.json for PULSE Surgery ch27 (Bowel Obstruction : Part 1, book p184-190)."""
import json

Q = []
def q(page, sec, text, opts, ans, exp):
    Q.append({"id": f"SURG-C27-{len(Q)+1:03d}", "sec": sec, "page": page,
              "q": text, "opts": opts, "ans": ans, "exp": exp})

# ---------------- p184 · TYPES ----------------
S1 = "Types of Bowel Obstruction"
q(184, S1, "Bowel obstruction is broadly classified into:",
  ["Dynamic and adynamic obstruction", "Acute and chronic only",
   "Simple and complicated only", "High and low only"], 0,
  "Types of bowel obstruction: dynamic (mechanical) and adynamic. (Book p184)")
q(184, S1, "Dynamic bowel obstruction is associated with:",
  ["Mechanical obstruction and increased bowel contractions",
   "No mechanical obstruction", "Absent bowel contractions",
   "A silent abdomen"], 0,
  "Dynamic: mechanical obstruction (+); bowel contraction (+). (Book p184)")
q(184, S1, "Hyperdynamic bowel sounds are heard in __________ obstruction.",
  ["Dynamic", "Adynamic", "Paralytic ileus", "Both types"], 0,
  "Dynamic: hyperdynamic sounds (+). (Book p184)")
q(184, S1, "Adynamic obstruction is characterised by:",
  ["No mechanical obstruction and a silent abdomen",
   "Mechanical obstruction with hyperdynamic sounds",
   "Increased bowel contractions", "Visible peristalsis"], 0,
  "Adynamic: no mechanical obstruction; bowel contraction (-); no hyperdynamic sounds; silent abdomen (+). (Book p184)")
q(184, S1, "Dynamic obstruction, if untreated, may progress to:",
  ["Perforation/strangulation", "Spontaneous resolution always",
   "Adynamic obstruction", "Malabsorption"], 0,
  "Dynamic obstruction → perforation/strangulation. (Book p184)")

# ---------------- p184 · CLINICAL FEATURES ----------------
S2 = "Clinical Features of Bowel Obstruction"
q(184, S2, "Clinical features common to both types of bowel obstruction include all EXCEPT:",
  ["Haematuria", "Abdominal pain", "Distension", "Non-passage of flatus and faeces"], 0,
  "Common to both types: abdominal pain; distension; obstruction (non-passage of flatus + faeces). (Book p184)")
q(184, S2, "Distension in bowel obstruction is most commonly due to:",
  ["Swallowed air", "Secretion of fluid", "Bacterial fermentation", "Ascites"], 0,
  "Distension (m/c d/t swallowed air). (Book p184)")
q(184, S2, "Obstruction is defined clinically as:",
  ["Non-passage of flatus and faeces", "Non-passage of urine",
   "Vomiting alone", "Abdominal pain alone"], 0,
  "Obstruction: non-passage of flatus + faeces. (Book p184)")
q(184, S2, "The order of appearance of symptoms in bowel obstruction:",
  ["Varies with the site of obstruction", "Is always the same",
   "Always begins with distension", "Always begins with obstipation"], 0,
  "Order of appearance varies with the site of obstruction. (Book p184)")
q(184, S2, "An obstruction in the lower GI tract presents first with:",
  ["Distension and obstipation", "Vomiting", "Haematemesis", "Jaundice"], 0,
  "Obstruction in lower GI tract → presents with distension/obstipation first. (Book p184)")

# ---------------- p184-185 · INVESTIGATIONS ----------------
S3 = "Investigations in Bowel Obstruction"
q(184, S3, "The initial investigation in suspected bowel obstruction is:",
  ["X-ray abdomen", "CECT abdomen", "USG abdomen", "MRI abdomen"], 0,
  "Initial investigation: X-ray abdomen. (Book p184)")
q(184, S3, "After the X-ray, the investigation of choice in adults with suspected bowel obstruction is:",
  ["CECT abdomen", "USG abdomen", "Barium meal", "MRI"], 0,
  "Adults: CECT abdomen. (Book p184)")
q(184, S3, "After the X-ray, the investigation of choice in children with suspected bowel obstruction is:",
  ["USG abdomen", "CECT abdomen", "Barium enema", "MRI"], 0,
  "Children: USG abdomen. (Book p184)")
q(184, S3, "On an erect X-ray abdomen, the finding suggestive of obstruction is:",
  [">3 air-fluid levels", "A single air-fluid level", "Free gas under the diaphragm",
   "Calcification"], 0,
  "Erect X-ray: >3 air-fluid levels s/o obstruction. (Book p184)")
q(184, S3, "A supine X-ray abdomen in bowel obstruction is used to:",
  ["Note the site of obstruction", "Detect free gas", "Assess liver size",
   "Look for renal stones"], 0,
  "Supine X-ray: used to note the site of obstruction. (Book p184)")
q(184, S3, "On a supine X-ray, the bowel proximal to the obstruction is __________ and the bowel distal to it is __________.",
  ["Dilated; collapsed", "Collapsed; dilated", "Dilated; dilated", "Collapsed; collapsed"], 0,
  "Supine X-ray: proximal dilated, distal collapsed. (Book p184)")

# ---------------- p185 · X-RAY DIFFERENTIATION & CRITICAL DIAMETERS ----------------
S4 = "Small v/s Large Bowel on X-ray and Critical Diameters"
q(185, S4, "On an X-ray abdomen, the jejunum is characterised by:",
  ["Complete valvulae conniventes giving a feathery appearance",
   "Incomplete valvulae conniventes", "Peripheral arrangement",
   "Incomplete haustrations"], 0,
  "Jejunum: complete valvulae conniventes - feathery appearance. (Book p185)")
q(185, S4, "The ileum shows __________ valvulae conniventes.",
  ["Incomplete", "Complete", "No", "Prominent and complete"], 0,
  "Complete volvulae in the jejunum; incomplete volvulae in the ileum. (Book p185)")
q(185, S4, "On an X-ray abdomen, the large bowel is:",
  ["Peripherally arranged with incomplete haustrations",
   "Centrally placed with complete valvulae",
   "Centrally placed with haustrations", "Always collapsed"], 0,
  "Large bowel: peripherally arranged; incomplete haustrations. (Book p185)")
q(185, S4, "The critical diameter of the small intestine is:",
  ["3 cm", "6 cm", "9 cm", "12 cm"], 0,
  "Critical diameters: small intestine - 3 cm. (Book p185)")
q(185, S4, "The critical diameter of the large intestine is:",
  ["6 cm", "3 cm", "9 cm", "12 cm"], 0,
  "Critical diameters: large intestine - 6 cm. (Book p185)")
q(185, S4, "The critical diameter of the caecum is:",
  ["9 cm", "3 cm", "6 cm", "15 cm"], 0,
  "Critical diameters: caecum - 9 cm (impending perforation). (Book p185)")
q(185, S4, "A caecal diameter beyond the critical value indicates:",
  ["Impending perforation", "Impending obstruction", "A normal variant",
   "Impending intussusception"], 0,
  "Caecum 9 cm: impending perforation. (Book p185)")

# ---------------- p185 · MANAGEMENT ----------------
S5 = "Management of Bowel Obstruction"
q(185, S5, "Initial conservative management of bowel obstruction includes all EXCEPT:",
  ["Immediate laparotomy", "Nil per oral", "IV fluids (Ringer's lactate)",
   "Ryle's tube/NG tube decompression"], 0,
  "Initial conservative mx: nil per oral; IV fluids (Ringer's lactate); Ryle's tube/NG tube decompression; IV antibiotics; IV painkillers. (Book p185)")
q(185, S5, "The IV fluid used in the initial management of bowel obstruction is:",
  ["Ringer's lactate", "Dextrose 5%", "Normal saline with potassium", "Dextrose saline"], 0,
  "IV fluids: Ringer's lactate. (Book p185)")
q(185, S5, "The Ryle's tube/NG tube is used in bowel obstruction for:",
  ["Decompression", "Feeding", "Lavage only", "Drug administration"], 0,
  "Ryle tube/NG tube → decompression. (Book p185)")
q(185, S5, "Intravenous antibiotics in bowel obstruction should cover:",
  ["Aerobes, anaerobes and gram negative organisms", "Gram positives only",
   "Fungi only", "Anaerobes only"], 0,
  "IV antibiotics: aerobic, anaerobic and gram negative cover. (Book p185)")
q(185, S5, "On imaging, if the caecum is visualized and is collapsed, the obstruction is:",
  ["Small intestinal", "Large intestinal", "Gastric", "Oesophageal"], 0,
  "Caecum visualized first: collapsed → small intestinal obstruction. (Book p185)")
q(185, S5, "On imaging, if the caecum is visualized and is distended, the obstruction is:",
  ["Large intestinal", "Small intestinal", "Gastric", "Oesophageal"], 0,
  "Caecum visualized first: distended → large intestinal obstruction. (Book p185)")
q(185, S5, "At surgery, if the bowel is found to be non-viable the treatment is:",
  ["Resection and anastomosis (+/- stoma)", "Retain the bowel",
   "Biopsy and closure", "Bypass only"], 0,
  "Check for viability: viable - retain; non-viable - resection and anastomosis (± stoma). (Book p185)")

# ---------------- p186 · VIABLE VS NON-VIABLE ----------------
S6 = "Viable v/s Non-viable Bowel"
q(186, S6, "A viable bowel loop with a dark colour:",
  ["Becomes lighter on handling", "Remains dark", "Turns black", "Becomes green"], 0,
  "Viable bowel: dark colour → becomes lighter. (Book p186)")
q(186, S6, "In non-viable bowel, the dark colour:",
  ["Remains dark", "Becomes lighter", "Turns pink", "Disappears"], 0,
  "Non-viable bowel: dark colour remains. (Book p186)")
q(186, S6, "Visible mesenteric artery pulsations indicate:",
  ["Viable bowel", "Non-viable bowel", "Strangulated bowel", "Perforation"], 0,
  "Viable: visible mesenteric artery pulsations; non-viable: pulsations (-). (Book p186)")
q(186, S6, "The general appearance of viable bowel is:",
  ["Shiny and firm", "Dull and lustreless", "Flabby and thin", "Friabile"], 0,
  "Viable: shiny; firm. Non-viable: dull and lustreless; flabby, thin and friable. (Book p186)")
q(186, S6, "Peristalsis may be observed in:",
  ["Viable bowel", "Non-viable bowel", "Gangrenous bowel", "Strangulated bowel"], 0,
  "Viable: peristalsis (may be observed); non-viable: no peristalsis. (Book p186)")

# ---------------- p186 · DUODENAL ATRESIA ----------------
S7 = "Duodenal Atresia"
q(186, S7, "Duodenal atresia is:",
  ["One of the m/c causes of bowel obstruction in neonates",
   "A cause of obstruction in adults", "Due to malrotation",
   "Due to volvulus"], 0,
  "Duodenal atresia: one of the m/c causes of bowel obstruction in neonates. (Book p186)")
q(186, S7, "Duodenal atresia is due to:",
  ["Non-canalisation of the duodenum", "Failure of rotation",
   "Persistence of the vitelline duct", "Annular pancreas"], 0,
  "Duodenal atresia: d/t non-canalisation of duodenum. (Book p186)")
q(186, S7, "Duodenal atresia is most commonly associated with:",
  ["Down's syndrome", "Turner's syndrome", "Edward's syndrome", "Klinefelter's syndrome"], 0,
  "Duodenal atresia: m/c in Down's syndrome (mothers → polyhydramnios). (Book p186)")
q(186, S7, "The mother of a fetus with duodenal atresia often has:",
  ["Polyhydramnios", "Oligohydramnios", "Pre-eclampsia", "Gestational diabetes"], 0,
  "Mothers → polyhydramnios. (Book p186)")
q(186, S7, "The m/c type of duodenal atresia is:",
  ["Type I", "Type II", "Type III", "Type IV"], 0,
  "Three types of duodenal atresia: type I m/c. (Book p186)")
q(186, S7, "The vomiting in duodenal atresia is present:",
  ["Since birth and is bilious", "After a few weeks and is non-bilious",
   "Only after feeds are stopped", "Only on lying down"], 0,
  "Clinical features: vomiting since birth; bilious vomiting. (Book p186)")
q(186, S7, "The treatment of duodenal atresia is:",
  ["Diamond duodeno-duodenostomy", "Ramstedt's pyloromyotomy",
   "Duodenojejunostomy", "Gastrojejunostomy"], 0,
  "Mx: diamond duodeno-duodenostomy. (Book p186)")
q(186, S7, "The double bubble sign is also seen in:",
  ["Annular pancreas", "Malrotation", "Hirschsprung's disease", "Meconium ileus"], 0,
  "Note: double bubble sign also seen in annular pancreas. (Book p186)")

# ---------------- p186 · DUODENAL ATRESIA vs CHPS ----------------
S8 = "Duodenal Atresia v/s Congenital Hypertrophic Pyloric Stenosis"
q(186, S8, "In congenital hypertrophic pyloric stenosis the child is:",
  ["Normal at birth with vomiting after a few weeks",
   "Symptomatic from birth", "Born with bile stained vomiting",
   "Born with abdominal distension"], 0,
  "CHPS: normal at birth; non-bilious projectile vomiting after a few weeks. (Book p186)")
q(186, S8, "The vomiting of congenital hypertrophic pyloric stenosis is:",
  ["Non-bilious and projectile", "Bilious and projectile", "Bilious and non-projectile",
   "Effortless"], 0,
  "CHPS: non-bilious, projectile vomiting after a few weeks. (Book p186)")
q(186, S8, "Congenital hypertrophic pyloric stenosis classically affects the:",
  ["First born male child", "First born female child", "Preterm female child",
   "Adolescent"], 0,
  "CHPS: first born male child. (Book p186)")
q(186, S8, "The investigation of choice in congenital hypertrophic pyloric stenosis is:",
  ["USG abdomen", "X-ray abdomen", "CECT abdomen", "Barium meal"], 0,
  "CHPS - IOC: USG abdomen. (Book p186)")
q(186, S8, "The investigation of choice in duodenal atresia is:",
  ["X-ray abdomen (double bubble sign)", "USG abdomen", "CECT abdomen", "Contrast enema"], 0,
  "Duodenal atresia - IOC: X-ray (double bubble). (Book p186)")
q(186, S8, "The treatment of congenital hypertrophic pyloric stenosis is:",
  ["Ramstedt's pyloromyotomy", "Diamond duodeno-duodenostomy",
   "Pyloroplasty", "Antrectomy"], 0,
  "Mx of CHPS: Ramstedt pyloromyotomy. (Book p186)")
q(186, S8, "The single bubble sign on X-ray is seen in:",
  ["Congenital hypertrophic pyloric stenosis", "Duodenal atresia",
   "Jejunal atresia", "Annular pancreas"], 0,
  "Note: single-bubble sign seen in CHPS. (Book p186)")

# ---------------- p187 · JEJUNAL ATRESIA & TYPES ----------------
S9 = "Jejunal Atresia and the Types of Intestinal Atresia"
q(187, S9, "Jejunal atresia presents with:",
  ["Bilious vomiting", "Non-bilious projectile vomiting",
   "Haematemesis", "Chronic diarrhoea"], 0,
  "Jejunal atresia - clinical features: bilious vomiting. (Book p187)")
q(187, S9, "The radiological sign seen in jejunal atresia is the:",
  ["Triple-bubble sign", "Double-bubble sign", "Single-bubble sign",
   "Coffee bean sign"], 0,
  "Jejunal atresia: triple-bubble sign. (Book p187)")
q(187, S9, "Type I intestinal atresia is:",
  ["A mucosal web or diaphragm", "An atretic cord with intact mesentery",
   "Blind ends with a V-shaped mesenteric gap", "Multiple atresias"], 0,
  "Type I: mucosal web or diaphragm. (Book p187)")
q(187, S9, "Type II intestinal atresia is:",
  ["An atretic cord with an intact mesentery", "A mucosal web",
   "Multiple atresias", "A large mesenteric gap"], 0,
  "Type II: atretic cord; intact mesentery. (Book p187)")
q(187, S9, "Type IIIa intestinal atresia consists of:",
  ["Blind ends of bowel with a V-shaped mesenteric gap",
   "A large mesenteric gap with an apple peel deformity",
   "Multiple atresias", "A mucosal web"], 0,
  "Type IIIa: blind ends of bowel; V-shaped mesenteric gap. (Book p187)")
q(187, S9, "The apple peel or Christmas tree deformity is seen in:",
  ["Type IIIb intestinal atresia", "Type I atresia", "Type II atresia", "Type IV atresia"], 0,
  "Type IIIb: large mesenteric gap - apple peel or Christmas tree deformity. (Book p187)")
q(187, S9, "Multiple atresias with a string of sausage appearance is:",
  ["Type IV intestinal atresia", "Type IIIa atresia", "Type II atresia", "Type I atresia"], 0,
  "Type IV: multiple atresia or string of sausage appearance. (Book p187)")

# ---------------- p187 · INTUSSUSCEPTION BASICS ----------------
S10 = "Intussusception: Definition and Types"
q(187, S10, "Intussusception is:",
  ["Telescoping of one bowel loop into another", "Twisting of the bowel around its vessels",
   "A congenital web in the bowel", "An outpouching of the bowel wall"], 0,
  "Intussusception: telescoping of one bowel loop into the other. (Book p187)")
q(187, S10, "The intussuscipiens is the:",
  ["Receiving portion of bowel", "Telescoping portion of bowel",
   "Lead point", "Meckel's diverticulum"], 0,
  "Intussuscipiens: receiving portion; intussusceptum: telescoping portion. (Book p187)")
q(187, S10, "The intussusceptum is the:",
  ["Telescoping portion of bowel", "Receiving portion of bowel",
   "Meckel's diverticulum", "Pathological lead point"], 0,
  "Intussusceptum: telescoping portion. (Book p187)")
q(187, S10, "The part of the intussusception that is most prone to ischemia is the:",
  ["Head", "Neck", "Tail", "Apex of the intussuscipiens"], 0,
  "Head: m/c site of ischemia; neck: narrowest part. (Book p187)")
q(187, S10, "The narrowest part of an intussusception is the:",
  ["Neck", "Head", "Tail", "Base"], 0,
  "Neck: narrowest part. (Book p187)")
q(187, S10, "Primary intussusception occurs in:",
  ["Children and is associated with hypertrophy of Peyer's patches",
   "Adults with a polyp", "Adults with cancer", "Patients with Meckel's diverticulum"], 0,
  "Primary: children; hypertrophy of Peyer's patches. (Book p187)")
q(187, S10, "The m/c type of primary intussusception is:",
  ["Ileocolic (ileum → colon)", "Colo-colic", "Ileo-ileal", "Jejuno-jejunal"], 0,
  "Primary: ileocolic (ileum → colon). (Book p187)")
q(187, S10, "Secondary intussusception is due to:",
  ["A pathological lead point", "Hypertrophy of Peyer's patches", "Viral infection",
   "Congenital bands"], 0,
  "Secondary: 2° to a pathological lead point. (Book p187)")
q(187, S10, "The m/c pathological lead point for secondary intussusception is a:",
  ["Polyp", "Cancer", "Meckel's diverticulum", "Duplication cyst"], 0,
  "Pathological lead point: polyp (m/c); cancer; Meckel's diverticulum. (Book p187)")
q(187, S10, "Colo-colic intussusception is:",
  ["Colon → colon", "Ileum → colon", "Jejunum → ileum", "Ileum → ileum"], 0,
  "Colo-colic: colon → colon. (Book p187)")

# ---------------- p188 · INTUSSUSCEPTION: C/F & IX ----------------
S11 = "Intussusception: Clinical Features and Investigations"
q(188, S11, "In children with intussusception, pain typically causes:",
  ["Drawing up of the legs", "Extension of the legs", "Back arching", "Neck stiffness"], 0,
  "In children: drawing up of legs d/t pain. (Book p188)")
q(188, S11, "Red currant jelly stools consist of:",
  ["Blood and mucus without fecal matter", "Pure blood", "Mucus only",
   "Altered blood with stool"], 0,
  "Red currant jelly stools: blood + mucus (no fecal matter). (Book p188)")
q(188, S11, "Sign of Dance in intussusception refers to:",
  ["A sausage-shaped mass in the right lumbar region with an empty right iliac fossa",
   "A mass in the left iliac fossa", "Visible peristalsis",
   "A tympanic swelling over the caecum"], 0,
  "Sign of Dance: sausage-shaped mass in right lumbar region with empty RIF. (Book p188)")
q(188, S11, "The investigation of choice for intussusception in children is:",
  ["USG abdomen", "CECT abdomen", "X-ray abdomen", "Barium meal follow through"], 0,
  "USG abdomen: IOC in children. (Book p188)")
q(188, S11, "The target/donut sign on ultrasound in intussusception represents:",
  ["One bowel loop seen inside another", "The mesenteric vessels inside the bowel",
   "A collection of fluid", "An enlarged lymph node"], 0,
  "Target/donut sign: one bowel loop seen inside another. (Book p188)")
q(188, S11, "The pseudokidney sign on ultrasound in intussusception is due to:",
  ["Mesenteric vessels seen inside the bowel", "One loop inside another",
   "A thickened bowel wall", "Free fluid in the abdomen"], 0,
  "Pseudokidney sign: mesenteric vessels seen inside the bowel. (Book p188)")
q(188, S11, "A contrast enema in intussusception is:",
  ["Both diagnostic and therapeutic", "Diagnostic only", "Therapeutic only",
   "Contraindicated in all cases"], 0,
  "Contrast enema: both diagnostic and therapeutic. (Book p188)")
q(188, S11, "The sign of intussusception seen on a contrast enema is the:",
  ["Claw/pincer sign", "Target sign", "Pseudokidney sign", "Coffee bean sign"], 0,
  "Contrast enema: claw/pincer sign. (Book p188)")
q(188, S11, "Contraindications to a contrast enema in intussusception include all EXCEPT:",
  ["A first episode without complications", "Recurrent intussusception",
   "A pathological lead point", "Strangulation or perforation"], 0,
  "Contraindications: recurrent intussusception; pathological lead point; strangulation; perforation. (Book p188)")
q(188, S11, "The investigation of choice for intussusception in adults is:",
  ["CECT abdomen", "USG abdomen", "X-ray abdomen", "Contrast enema"], 0,
  "CECT abdomen: IOC in adults. (Book p188)")

# ---------------- p188 · INTUSSUSCEPTION: MANAGEMENT ----------------
S12 = "Management of Intussusception"
q(188, S12, "During surgery for intussusception, reduction is done by:",
  ["Pushing, never pulling", "Pulling, never pushing", "Both pushing and pulling",
   "Resection without reduction"], 0,
  "Reduction of intussusception: always pushed, not pulled. (Book p188)")
q(188, S12, "Resection and anastomosis is required in intussusception when there is:",
  ["Perforation, strangulation or a pathological lead point",
   "A first episode in a child", "Red currant jelly stools", "A positive Donut sign"], 0,
  "If perforation/strangulation/pathological lead point (+): resection and anastomosis. (Book p188)")

# ---------------- p188-189 · SIGMOID VOLVULUS ----------------
S13 = "Sigmoid Volvulus"
q(188, S13, "Volvulus is:",
  ["Twisting of a bowel loop around its vessels", "Telescoping of one loop into another",
   "A congenital web", "An adhesion band"], 0,
  "Volvulus: twisting of a bowel loop around its vessels. (Book p188)")
q(188, S13, "Predisposing factors for sigmoid volvulus include all EXCEPT:",
  ["A short broad mesentery", "A long and narrow mesentery",
   "A redundant (long) sigmoid", "A loaded constipated sigmoid"], 0,
  "Predisposing factors: long and narrow mesentery; redundant sigmoid (↑ length); loaded sigmoid (constipated). (Book p188)")
q(188, S13, "Sigmoid volvulus is more common in:",
  ["Patients on anti-psychotic medications and institutionalized patients",
   "Young athletes", "Pregnant women", "Children under five"], 0,
  "Predisposing factors: patient on anti-psychotic medications; institutionalized patients. (Book p188)")
q(188, S13, "Sigmoid volvulus is an example of:",
  ["Closed loop obstruction", "Open loop obstruction", "Partial obstruction",
   "Functional obstruction"], 0,
  "Sigmoid volvulus: closed loop obstruction. (Book p188)")
q(188, S13, "In sigmoid volvulus the most prominent feature is:",
  ["Distension", "Vomiting", "Diarrhoea", "Haematemesis"], 0,
  "Clinical features: distension is prominent. (Book p188)")
q(188, S13, "A closed loop obstruction carries:",
  ["High chances of strangulation", "No risk of strangulation",
   "A low risk of perforation", "A good prognosis"], 0,
  "Closed loop obstruction → high chances of strangulation. (Book p188)")
q(189, S13, "The coffee bean sign on X-ray is seen in:",
  ["Sigmoid volvulus", "Caecal volvulus", "Intussusception", "Duodenal atresia"], 0,
  "Coffee bean sign: seen in sigmoid volvulus. (Book p189)")
q(189, S13, "In sigmoid volvulus, the apex of the distended loop points to the:",
  ["Right shoulder", "Left shoulder tip", "Pelvis", "Right iliac fossa"], 0,
  "Sigmoid volvulus: apex → (R) shoulder. (Book p189)")
q(189, S13, "In caecal volvulus, the apex of the distended loop points to the:",
  ["Left shoulder tip", "Right shoulder", "Pelvis", "Left iliac fossa"], 0,
  "In caecal volvulus: apex → (L) shoulder tip; small intestine distended. (Book p189)")
q(189, S13, "The investigation of choice in sigmoid volvulus is:",
  ["CECT abdomen", "X-ray abdomen", "USG abdomen", "Barium meal"], 0,
  "CECT abdomen: IOC in sigmoid volvulus. (Book p189)")
q(189, S13, "The bird's beak or ace of spades appearance in sigmoid volvulus is seen on:",
  ["Contrast enema", "X-ray abdomen erect", "CECT abdomen", "Ultrasound"], 0,
  "Contrast enema: bird's beak/ace of spades appearance. (Book p189)")

# ---------------- p189 · MANAGEMENT OF SIGMOID VOLVULUS ----------------
S14 = "Management of Sigmoid Volvulus and Hartmann's Procedure"
q(189, S14, "A patient with sigmoid volvulus without signs of peritonitis is managed by:",
  ["Decompression followed by definitive surgery",
   "Emergency laparotomy", "Hartmann's procedure", "Conservative management only"], 0,
  "No c/f of peritonitis → decompression → definitive Sx (sigmoidopexy/sigmoidectomy). (Book p189)")
q(189, S14, "Definitive surgery for sigmoid volvulus after decompression is:",
  ["Sigmoidopexy or sigmoidectomy", "Right hemicolectomy",
   "Hartmann's procedure", "Total colectomy"], 0,
  "Definitive Sx: sigmoidopexy (derotate clockwise) / sigmoidectomy (cut excess sigmoid). (Book p189)")
q(189, S14, "During sigmoidopexy for sigmoid volvulus, the loop is de-rotated:",
  ["Clockwise", "Anti-clockwise", "Upwards", "Downwards"], 0,
  "Sigmoidopexy: derotate clockwise. (Book p189)")
q(189, S14, "A patient with sigmoid volvulus who has peritonitis, sepsis or perforation needs:",
  ["Emergency laparotomy", "Endoscopic decompression",
   "A contrast enema", "Conservative management"], 0,
  "Peritonitis/sepsis/perforation (+) → emergency laparotomy. (Book p189)")
q(189, S14, "Hartmann's procedure consists of:",
  ["Resection of the segment with creation of a stoma (colostomy)",
   "Resection with primary anastomosis", "A defunctioning ileostomy only",
   "A total colectomy"], 0,
  "Hartmann's procedure: creation of stoma (colostomy). (Book p189)")
q(189, S14, "After a Hartmann's procedure, re-anastomosis is done:",
  ["After 6-8 weeks, once the patient has healed", "After 6 months",
   "After 1 year", "Within 48 hours"], 0,
  "Re-anastomosis: 6-8 weeks (once healed). (Book p189)")

# ---------------- p190 · CAECAL VOLVULUS ----------------
S15 = "Caecal Volvulus"
q(190, S15, "Predisposing factors for caecal volvulus include:",
  ["A mobile caecum and caecal bascule", "A long narrow mesentery",
   "A loaded sigmoid", "Anti-psychotic medication"], 0,
  "Predisposing factors: mobile caecum; caecal bascule (type of mobile caecum). (Book p190)")
q(190, S15, "Caecal bascule is:",
  ["A type of mobile caecum", "A type of sigmoid volvulus",
   "A congenital atresia", "An intussusception"], 0,
  "Caecal bascule: a type of mobile caecum. (Book p190)")
q(190, S15, "The caecum in caecal volvulus rotates:",
  ["Clockwise", "Anti-clockwise", "Upwards only", "Not at all"], 0,
  "Clinical features: clockwise rotation of caecum. (Book p190)")
q(190, S15, "The initial investigation in caecal volvulus is:",
  ["X-ray abdomen (erect and supine)", "CECT abdomen", "USG abdomen",
   "Contrast enema"], 0,
  "X-ray abdomen (erect and supine): initial investigation. (Book p190)")
q(190, S15, "The investigation of choice in caecal volvulus is:",
  ["CECT abdomen", "X-ray abdomen", "USG abdomen", "Barium enema"], 0,
  "CECT abdomen: IOC in caecal volvulus. (Book p190)")
q(190, S15, "A patient with caecal volvulus without peritonitis is treated by:",
  ["Caecopexy (de-rotation anti-clockwise)", "Emergency right hemicolectomy",
   "Hartmann's procedure", "Conservative management alone"], 0,
  "No peritonitis → caecopexy (derotate anti-clockwise). (Book p190)")
q(190, S15, "A patient with caecal volvulus with peritonitis is treated by:",
  ["Right hemicolectomy after laparotomy", "Caecopexy", "Decompression",
   "Sigmoidectomy"], 0,
  "Peritonitis → laparotomy → (R) hemicolectomy. (Book p190)")

# ---------------- p190 · INTESTINAL STRICTURES ----------------
S16 = "Intestinal Strictures"
q(190, S16, "Causes of intestinal strictures include all EXCEPT:",
  ["Diverticulosis", "Cancer", "Post radiotherapy", "TB and Crohn's disease"], 0,
  "Causes: cancer; post radiotherapy; TB; Crohn's. (Book p190)")
q(190, S16, "Subacute intestinal obstruction presents with:",
  ["Intermittent symptoms until complete obstruction eventually develops",
   "Sudden complete obstruction", "No symptoms at all", "Only bleeding"], 0,
  "Subacute obstruction: intermittent symptoms → until complete obstruction eventually. (Book p190)")
q(190, S16, "The initial investigation in a patient with an intestinal stricture is:",
  ["X-ray abdomen (erect and supine)", "CECT abdomen", "USG abdomen", "Colonoscopy"], 0,
  "X-ray abdomen (erect & supine): initial investigation. (Book p190)")
q(190, S16, "The investigation of choice for intestinal strictures in adults is:",
  ["CECT abdomen", "USG abdomen", "X-ray abdomen", "MRI enterography"], 0,
  "CECT abdomen: IOC in adults. (Book p190)")
q(190, S16, "The investigation of choice for intestinal strictures in children is:",
  ["USG abdomen", "CECT abdomen", "X-ray abdomen", "Barium follow through"], 0,
  "USG abdomen: IOC in children. (Book p190)")
q(190, S16, "Multiple strictures lying close to each other are treated by:",
  ["Resection and anastomosis", "Stricturoplasty", "Dilatation alone", "Bypass"], 0,
  "If multiple strictures close to each other → resection + anastomosis. (Book p190)")
q(190, S16, "Strictures that are far apart from each other are treated by:",
  ["Stricturoplasty", "Resection and anastomosis", "Total colectomy", "Dilatation"], 0,
  "If strictures are far apart → stricturoplasty (2 types). (Book p190)")
q(190, S16, "The Heineke-Mikulicz stricturoplasty is a:",
  ["Longitudinal stricturoplasty sutured transversely",
   "Side to side anastomosis", "Segmental resection", "End to end anastomosis"], 0,
  "Heineke-Mikulicz stricturoplasty: longitudinal stricturoplasty, suture transversely. (Book p190)")
q(190, S16, "Finney's stricturoplasty is a:",
  ["Side to side anastomosis", "Longitudinal stricturoplasty sutured transversely",
   "End to end anastomosis", "Segmental resection"], 0,
  "Finney's stricturoplasty: side to side anastomosis. (Book p190)")
q(190, S16, "Tuberculous ulcers in the intestine are __________ and give rise to __________.",
  ["Transverse; strictures", "Longitudinal; perforation", "Longitudinal; strictures",
   "Transverse; perforation"], 0,
  "Note: TB ulcers are transverse and give rise to strictures. (Book p190)")
q(190, S16, "Typhoid ulcers in the intestine are __________ and give rise to __________.",
  ["Longitudinal; perforation", "Transverse; strictures", "Transverse; perforation",
   "Longitudinal; strictures"], 0,
  "Note: typhoid ulcers are longitudinal and give rise to perforation. (Book p190)")

# ---------------- units ----------------
def sec_ids(*labels):
    return [x["id"] for x in Q if x["sec"] in labels]
def first_page(label):
    for x in Q:
        if x["sec"] == label:
            return x["page"]
    return 0

UNIT_DEFS = [
    (S1, "Split obstruction in two at the bedside: dynamic means a mechanical block with the bowel fighting it - contractions and hyperdynamic sounds, and if it goes on, strangulation or perforation. Adynamic means no mechanical block at all, no contractions and a silent abdomen."),
    (S2, "Pain, distension and absolute constipation are common to both types. The distension is mostly swallowed air, the order in which symptoms appear tells you how low the block is, and a lower obstruction declares itself with distension and obstipation first."),
    (S3, "Start with a plain X-ray - erect for the tell-tale more-than-three air-fluid levels, supine to locate the level by finding where the bowel changes from proximally dilated to distally collapsed. After that, adults go to CECT and children to ultrasound."),
    (S4, "On the film the jejunum shows complete valvulae conniventes and a feathery pattern, the ileum incomplete ones, and the large bowel sits peripherally with incomplete haustrations. Critical diameters are the numbers to remember: 3 cm for small bowel, 6 cm for large bowel and 9 cm for the caecum, beyond which perforation is imminent."),
    (S5, "Conservative treatment first: nil by mouth, Ringer's lactate, an NG or Ryle's tube for decompression, antibiotics covering aerobes, anaerobes and gram negatives, and analgesia. Then look at the caecum - collapsed means small bowel obstruction, distended means large bowel - and at surgery decide whether the bowel can be kept or has to go."),
    (S6, "Viability is a judgement at the table: viable bowel lightens in colour, shows mesenteric pulsations, looks shiny and firm and may be seen to peristalse. Dead bowel stays dark, has no pulsations, looks dull and flabby and lies still."),
    (S7, "Duodenal atresia - one of the commonest neonatal obstructions - comes from failure of recanalisation, is the classic partner of Down's syndrome and of polyhydramnios in the mother, is usually type I, and gives bilious vomiting from day one. The operation is a diamond duodeno-duodenostomy, and remember that the double bubble is shared with annular pancreas."),
    (S8, "Set it against pyloric stenosis: the atresia child vomits bile from birth and needs an X-ray, while the child with congenital hypertrophic pyloric stenosis is normal at birth, is a first born boy, starts projectile non-bilious vomiting a few weeks later and is diagnosed on ultrasound and cured by Ramstedt's pyloromyotomy. Single bubble is CHPS, double bubble is atresia."),
    (S9, "Jejunal atresia also gives bilious vomiting, but with a triple bubble. Learn the Grosfeld typing: a mucosal web (I), an atretic cord with intact mesentery (II), blind ends with a V-shaped gap (IIIa), the apple peel or Christmas tree deformity of a large mesenteric gap (IIIb) and multiple atresias like a string of sausages (IV)."),
    (S10, "One loop telescopes into another: the intussuscipiens receives, the intussusceptum travels, the head is where ischemia strikes first and the neck is the narrowest part. Primary disease belongs to children with hypertrophic Peyer's patches and is usually ileocolic; secondary disease follows a lead point - most often a polyp - and is often colo-colic."),
    (S11, "The child draws up the legs with colicky pain, passes red currant jelly stools of blood and mucus without faeces, and the abdomen shows Dance's sign - a sausage mass in the right lumbar region with an empty right iliac fossa. Ultrasound is the investigation of choice in children and shows the target or donut sign and the pseudokidney; a contrast enema both diagnoses and treats and shows the claw or pincer, but is forbidden when there is recurrence, a lead point, strangulation or perforation. Adults go straight to CECT."),
    (S12, "Reduce by pushing, never pulling, and reserve resection and anastomosis for perforation, strangulation or a pathological lead point."),
    (S13, "Volvulus is a loop twisting around its own vessels. The sigmoid variety comes from a long narrow mesentery, a redundant loaded sigmoid and, classically, from antipsychotic drugs and institutional care; it is a closed loop with striking distension, obstipation and a high chance of strangulation. The coffee bean points to the right shoulder, the contrast enema shows a bird's beak or ace of spades, and CECT is the investigation of choice. In caecal volvulus the apex swings to the left shoulder tip and the small bowel is distended."),
    (S14, "Without peritonitis, decompress and then do the definitive operation - sigmoidopexy after clockwise de-rotation, or sigmoidectomy to remove the excess. With peritonitis, sepsis or perforation it is an emergency laparotomy and a Hartmann's: resect, bring out a colostomy and come back to re-anastomose 6-8 weeks later."),
    (S15, "Caecal volvulus needs a mobile caecum - often a caecal bascule - and twists clockwise. Film first, CECT to confirm; caecopexy with anti-clockwise de-rotation when the abdomen is quiet, and a right hemicolectomy once peritonitis declares itself."),
    (S16, "Strictures come from cancer, radiotherapy, tuberculosis and Crohn's, and announce themselves as intermittent subacute obstruction that eventually becomes complete. Film first, then CECT in adults or ultrasound in children. Multiple strictures close together are resected and anastomosed; those far apart are dealt with by stricturoplasty - Heineke-Mikulicz when you open longitudinally and close transversely, Finney when you fashion a side to side anastomosis. Finally, remember the ulcer geometry: tuberculous ulcers are transverse and stenose, typhoid ulcers are longitudinal and perforate."),
]

UNITS = []
for i, (title, guide) in enumerate(UNIT_DEFS, 1):
    UNITS.append({"id": f"SURG-U27-{i}", "ch": 27, "n": i, "title": title,
                  "sec": f"{title} · p{first_page(title)}",
                  "qs": sec_ids(title), "guide": guide})

covered = [i for u in UNITS for i in u["qs"]]
assert covered == [x["id"] for x in Q], "units must cover questions in order"

data = {"questions": Q, "units": UNITS}
with open("data/ch27.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
print(f"ch27: {len(Q)} questions, {len(UNITS)} units")
