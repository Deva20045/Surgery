#!/usr/bin/env python3
"""Build data/ch29.json for PULSE Surgery ch29 (Benign Conditions of Small & Large Bowel, p197-207)."""
import json

Q = []
def q(page, sec, text, opts, ans, exp):
    Q.append({"id": f"SURG-C29-{len(Q)+1:03d}", "sec": sec, "page": page,
              "q": text, "opts": opts, "ans": ans, "exp": exp})

# ---------------- p197 · ILEOSTOMY vs COLOSTOMY ----------------
S1 = "Stomas: Ileostomy v/s Colostomy"
q(197, S1, "Compared with a colostomy, an ileostomy has __________ output.",
  ["More and more liquid", "Less and more solid", "The same", "None"], 0,
  "Ileostomy: output more (liquid); colostomy: less (semisolid). (Book p197)")
q(197, S1, "Skin excoriation is more common with a:",
  ["Ileostomy", "Colostomy", "Both equally", "Neither"], 0,
  "Skin excoriation: ileostomy more; colostomy less. (Book p197)")
q(197, S1, "Fluid and electrolyte imbalance is more of a problem with a:",
  ["Ileostomy", "Colostomy", "Both equally", "Neither"], 0,
  "Fluid & electrolyte imbalance: ileostomy more; colostomy less. (Book p197)")
q(197, S1, "Which stoma is easier to manage?",
  ["Colostomy", "Ileostomy", "Both are equally difficult", "Neither - both need a stoma therapist"], 0,
  "Ease of management: colostomy - easier. (Book p197)")
q(197, S1, "Technically, an ileostomy is:",
  ["Raised above the skin surface (pouting)", "Flushed with the skin",
   "Buried below the skin", "Sutured flat to the fascia"], 0,
  "Technical difference: ileostomy raised above the skin surface (pouting); colostomy at the same level (flushed with the skin). (Book p197)")
q(197, S1, "A colostomy is technically:",
  ["At the same level as the skin (flushed)", "Raised above the skin",
   "Buried below the skin", "Everted into a spout"], 0,
  "Colostomy: at the same level (flushed with the skin). (Book p197)")
q(197, S1, "An ileostomy is usually sited in the:",
  ["Left or right iliac fossa", "Epigastrium", "Left hypochondrium", "Umbilicus"], 0,
  "Site: ileostomy - left/right iliac fossa. (Book p197)")
q(197, S1, "A sigmoid colostomy is sited in the __________ and a transverse colostomy in the __________.",
  ["Left iliac fossa; epigastrium", "Right iliac fossa; left iliac fossa",
   "Epigastrium; left iliac fossa", "Umbilicus; right iliac fossa"], 0,
  "Colostomy - sigmoid: left iliac fossa; transverse: epigastrium. (Book p197)")
q(197, S1, "A stoma should be positioned:",
  ["Away from bony landmarks, along the outer border of the rectus",
   "Over the anterior superior iliac spine", "Over the costal margin",
   "Through the rectus muscle laterally"], 0,
  "Position: away from bony landmarks; taken along the outer border of rectus. (Book p197)")
q(197, S1, "An ileostomy is matured by:",
  ["Suturing the everted free end of the proximal ileum to the skin edges to form a spout",
   "Suturing the bowel flush with the skin",
   "Leaving the bowel open without suturing",
   "Anchoring the bowel to the peritoneum only"], 0,
  "Ileostomy formation: suturing the free extremity of the proximal ileum to the skin edges after eversion to form a spout. (Book p197)")

# ---------------- p197 · TYPES OF STOMAS ----------------
S2 = "Types of Stomas"
q(197, S2, "In an end (single barrel) stoma:",
  ["Only one end of bowel is brought out", "Both ends are brought out",
   "A loop of bowel is brought out", "Two separate loops are brought out"], 0,
  "Single barrel/end stoma: only one end is taken out; not joined; single opening. (Book p197)")
q(197, S2, "In a double barrel stoma:",
  ["Two separate ends (proximal and distal) are brought out and are not joined to each other",
   "A single loop is brought out", "One end is brought out",
   "The two ends are joined to each other"], 0,
  "Double barrel: two separate ends are taken out (proximal and distal), not joined to each other like a loop stoma - 2 openings not joined with each other. (Book p197)")
q(197, S2, "In a loop stoma:",
  ["A loop is brought out, so proximal and distal openings are seen joined with each other",
   "Two separate ends are brought out", "Only one end is brought out",
   "The bowel is closed completely"], 0,
  "Loop stoma: loop taken out, so proximal and distal opening is seen - 2 openings joined with each other; flushed with the skin. (Book p197)")
q(197, S2, "A loop stoma is:",
  ["Flushed with the skin", "Raised above the skin level",
   "Buried below the skin", "Everted into a spout"], 0,
  "Loop stoma: flushed with the skin. (Book p197)")
q(197, S2, "An end stoma is:",
  ["Raised above the skin level", "Flushed with the skin",
   "At the same level as the skin", "Below the skin"], 0,
  "End stoma: raised above skin level. (Book p197)")

# ---------------- p198 · TEMPORARY / PERMANENT & COMPLICATIONS ----------------
S3 = "Temporary and Permanent Stomas, and their Complications"
q(198, S3, "A temporary stoma is done to:",
  ["Protect a fresh anastomosis", "Replace the rectum permanently",
   "Treat a stoma prolapse", "Reduce the operative time"], 0,
  "Temporary stomas: done to protect fresh anastomosis. (Book p198)")
q(198, S3, "A temporary ileostomy protecting a colon-to-colon anastomosis is closed after:",
  ["8-10 weeks", "2 weeks", "6 months", "1 year"], 0,
  "Temporary ileostomy to protect the anastomosis: closed after 8-10 wks. (Book p198)")
q(198, S3, "A permanent stoma is usually a:",
  ["Permanent end colostomy", "Loop ileostomy", "Double barrel ileostomy",
   "Loop colostomy"], 0,
  "Permanent stomas: permanent end-colostomy done. (Book p198)")
q(198, S3, "The m/c complication of a stoma is:",
  ["Skin excoriation", "Prolapse", "Retraction", "Parastomal hernia"], 0,
  "Complications: skin excoriation - m/c. (Book p198)")
q(198, S3, "The m/c long term complication of a colostomy is:",
  ["Parastomal herniation", "Skin excoriation", "Retraction", "Necrosis"], 0,
  "Parastomal herniation: m/c long term complication of colostomy. (Book p198)")
q(198, S3, "Parastomal herniation is more common with a:",
  ["Loop stoma than an end stoma", "End stoma than a loop stoma",
   "Both equally", "Neither"], 0,
  "Parastomal herniation: m/c - loop > end stoma. (Book p198)")
q(198, S3, "A parastomal hernia is corrected by:",
  ["Mesh repair", "Resection of the stoma", "Simple suturing of the defect",
   "Relocation of the stoma only"], 0,
  "Parastomal herniation: corrected by mesh repair. (Book p198)")
q(198, S3, "Complications of a stoma include all EXCEPT:",
  ["Short bowel syndrome", "Prolapse", "Retraction", "Skin excoriation"], 0,
  "Stoma complications: skin excoriation (m/c), prolapse, retraction, parastomal herniation. (Book p198)")

# ---------------- p198-199 · SHORT BOWEL SYNDROME ----------------
S4 = "Short Bowel Syndrome"
q(198, S4, "Short bowel syndrome is defined as a remnant of:",
  ["<200 cm of small intestine", "<100 cm of small intestine",
   "<50 cm of small intestine", "<300 cm of small intestine"], 0,
  "Short bowel syndrome: <200 cm of small intestine (S.I.). (Book p198)")
q(198, S4, "A patient with __________ of small intestine is a net secretor.",
  ["<100 cm", ">100 cm", "<200 cm", ">200 cm"], 0,
  "Net secretors: <100 cm of S.I.; net absorbers: >100 cm of S.I. (Book p198)")
q(198, S4, "A patient with __________ of small intestine is a net absorber.",
  [">100 cm", "<100 cm", "<50 cm", ">200 cm"], 0,
  "Net absorbers: >100 cm of S.I. (Book p198)")
q(198, S4, "The m/c cause of short bowel syndrome is:",
  ["Superior mesenteric artery embolism", "Crohn's disease", "Radiation enteritis",
   "Trauma"], 0,
  "Causes: superior mesenteric artery embolism - m/c. (Book p198)")
q(198, S4, "Causes of short bowel syndrome include all EXCEPT:",
  ["Peptic ulcer disease", "Crohn's disease", "Malrotation/atresia in children",
   "SMA embolism"], 0,
  "Causes: SMA embolism (m/c); Crohn's disease; malrotation/atresia (children). (Book p198)")
q(199, S4, "Features of short bowel syndrome include all EXCEPT:",
  ["Constipation", "Malabsorption", "Diarrhoea due to rapid transit",
   "Bacterial overgrowth"], 0,
  "Features: malabsorption; diarrhoea (d/t rapid transit); weight loss; bacterial overgrowth. (Book p199)")
q(199, S4, "When the ileum is preserved and the jejunum is lost:",
  ["The ileum can adapt", "Vitamin B12 and other nutrient deficiencies occur",
   "TPN is always required", "Transplantation is mandatory"], 0,
  "Ileum (+), jejunum (-): ileum can adapt. (Book p199)")
q(199, S4, "When the jejunum is preserved and the ileum is lost:",
  ["Vitamin B12 and nutrient deficiencies occur",
   "The bowel adapts completely", "No supplementation is needed",
   "Bile salt absorption is normal"], 0,
  "Jejunum (+), ileum (-): vit B12 & nutrient deficiencies (+). (Book p199)")

# ---------------- p199 · SBS MANAGEMENT & LENGTHENING ----------------
S5 = "Management of Short Bowel Syndrome and Bowel Lengthening"
q(199, S5, "The mainstay of management of short bowel syndrome is:",
  ["Long term total parenteral nutrition (TPN)", "Oral rehydration alone",
   "Elemental diet only", "Prokinetics"], 0,
  "Management: long term TPN (total parenteral nutrition). (Book p199)")
q(199, S5, "The definitive treatment option for short bowel syndrome is:",
  ["Small intestine transplantation", "Bypass grafting", "Long term steroids",
   "Bowel plication"], 0,
  "Management: long term TPN; small intestine transplantation. (Book p199)")
q(199, S5, "Teduglutide used in short bowel syndrome is a:",
  ["GLP-2 analogue", "GLP-1 analogue", "Somatostatin analogue", "Bile acid sequestrant"], 0,
  "Drugs: teduglutide (GLP 2 analogue); cholestyramine. (Book p199)")
q(199, S5, "The Bianchi procedure for short bowel syndrome consists of:",
  ["Longitudinal splitting of the bowel with linear staplers along the mesenteric border and an end to end anastomosis (zig-zag bowel)",
   "Serial transverse stapling to lengthen the bowel",
   "Reversed jejunal segment interposition", "Longitudinal lengthening with a patch"], 0,
  "Bianchi procedure: longitudinally split the bowel with linear staplers along the mesenteric border, end to end anastomosis → zig-zag bowel. (Book p199)")
q(199, S5, "Serial transverse enteroplasty (STEP) results in:",
  ["Increased length and better absorption", "A zig-zag bowel",
   "A reversed segment", "Shortening of the bowel"], 0,
  "Serial transverse enteroplasty (STEP): ↑ length, better absorption. (Book p199)")

# ---------------- p199-200 · DIVERTICULAR DISEASE ----------------
S6 = "Diverticular Disease"
q(199, S6, "Colonic diverticula are __________ diverticulae.",
  ["False (only the mucosa bulges out)", "True (all layers bulge out)",
   "Congenital", "Acquired traction"], 0,
  "Features: false diverticulae (only mucosa bulges out). (Book p199)")
q(199, S6, "The m/c site affected by diverticular disease is the:",
  ["Sigmoid colon", "Caecum", "Transverse colon", "Rectum"], 0,
  "m/c site affected: sigmoid colon. (Book p199)")
q(199, S6, "Diverticular disease is most common in the __________ decade and is associated with:",
  ["4th-5th; constipation", "1st-2nd; diarrhoea", "8th-9th; diarrhoea",
   "2nd-3rd; vomiting"], 0,
  "Age group: 4th-5th decade; associated with constipation. (Book p199)")
q(200, S6, "Diverticulosis is:",
  ["Multiple diverticulae without inflammation", "A single inflamed diverticulum",
   "Diverticulae with perforation", "A congenital condition"], 0,
  "Diverticulosis: multiple diverticulae with no inflammation. (Book p200)")
q(200, S6, "Clinical features of diverticulosis include:",
  ["Constipation and bleeding", "Jaundice", "Steatorrhoea", "Tenesmus only"], 0,
  "Clinical features of diverticulosis: constipation; bleeding. (Book p200)")
q(200, S6, "The investigation of choice for uncomplicated diverticulosis is:",
  ["Barium enema (saw tooth appearance)", "CECT abdomen", "Colonoscopy",
   "CT angiography"], 0,
  "IOC: barium enema - saw tooth appearance. (Book p200)")

# ---------------- p200 · COMPLICATIONS & HINCHEY ----------------
S7 = "Complications of Diverticular Disease and Hinchey's Staging"
q(200, S7, "Bleeding from diverticular disease is more common on the:",
  ["Right side", "Left side", "Both sides equally", "Rectum"], 0,
  "Bleeding: right side bleed m/c. (Book p200)")
q(200, S7, "The investigation used to diagnose bleeding from diverticular disease is:",
  ["CT angiography", "Barium enema", "Plain X-ray", "Colonoscopy"], 0,
  "Diagnosis of diverticular bleeding: CT angiography. (Book p200)")
q(200, S7, "The management of diverticular bleeding is:",
  ["Embolization followed by resection (definitive management)",
   "Immediate laparotomy", "Conservative management only", "Endoscopic banding"], 0,
  "Management: embolization f/b resection (definitive management). (Book p200)")
q(200, S7, "Diverticulitis most commonly presents with pain on the:",
  ["Left side (left > right)", "Right side", "Epigastrium", "Perineum"], 0,
  "Diverticulitis: pain abdomen (left side > right side). (Book p200)")
q(200, S7, "Clinical features of diverticulitis include:",
  ["Pain abdomen, diarrhoea and fever", "Painless jaundice",
   "Haematemesis and melaena", "Constipation only"], 0,
  "Features of diverticulitis: pain abdomen; diarrhea; fever. (Book p200)")
q(200, S7, "The investigation of choice in acute diverticulitis is:",
  ["CECT abdomen", "Barium enema", "Plain X-ray abdomen", "Colonoscopy"], 0,
  "Investigations: ↑ TLC; CECT - IOC (pericolic abscess). (Book p200)")
q(200, S7, "Hinchey stage I diverticulitis on CT is:",
  ["Colonic inflammation with a pericolic abscess",
   "Colonic inflammation with a pelvic abscess", "Purulent peritonitis",
   "Fecal peritonitis"], 0,
  "Hinchey staging: stage I - colonic inflammation with pericolic abscess. (Book p200)")
q(200, S7, "Hinchey stage II diverticulitis on CT is:",
  ["Colonic inflammation with a pelvic abscess",
   "Colonic inflammation with a pericolic abscess", "Fecal peritonitis",
   "A localized perforation"], 0,
  "Hinchey stage II: colonic inflammation with pelvic abscess. (Book p200)")
q(200, S7, "Hinchey stage IV diverticulitis is:",
  ["Fecal peritonitis", "Pericolic abscess", "Pelvic abscess",
   "Purulent peritonitis"], 0,
  "Hinchey stage IV: fecal peritonitis. (Book p200)")
q(200, S7, "The management of Hinchey stage I and II diverticulitis is:",
  ["IV antibiotics, analgesics and pigtail catheter drainage",
   "Emergency laparotomy", "Hartmann's procedure", "Resection and anastomosis"], 0,
  "Management - stage I & II: IV antibiotics; analgesics; drainage using pigtail catheter. (Book p200)")
q(200, S7, "The management of Hinchey stage III and IV diverticulitis is:",
  ["Emergency laparotomy with Hartmann's procedure", "Conservative management",
   "Pigtail catheter drainage only", "Endoscopic stenting"], 0,
  "Management - stage III & IV: emergency laparotomy; Hartmann's procedure. (Book p200)")
q(200, S7, "A long standing complication of diverticular disease is:",
  ["Colorectal cancer", "Small bowel lymphoma", "Gastric cancer", "GIST"], 0,
  "Complication: colorectal cancer in long standing cases. (Book p200)")

# ---------------- p201 · ANGIODYSPLASIA ----------------
S8 = "Angiodysplasia"
q(201, S8, "Angiodysplasia is typically seen in:",
  ["Elderly patients in the 7th decade", "Children", "Young adults",
   "Neonates"], 0,
  "Angiodysplasia: elderly patient - 7th decade. (Book p201)")
q(201, S8, "Angiodysplasia is most commonly located on the __________ side of the colon.",
  ["Right", "Left", "Both equally", "Rectal"], 0,
  "m/c on right > left side. (Book p201)")
q(201, S8, "The m/c site of angiodysplasia is the:",
  ["Caecum", "Sigmoid colon", "Rectum", "Splenic flexure"], 0,
  "m/c site: caecum. (Book p201)")
q(201, S8, "Angiodysplasia is the __________ m/c cause of massive lower GI haemorrhage.",
  ["2nd", "1st", "3rd", "5th"], 0,
  "2nd m/c cause of massive lower GI hemorrhage. (Book p201)")
q(201, S8, "Angiodysplasia is associated with a deficiency/abnormality of:",
  ["von Willebrand factor", "Factor VIII alone", "Vitamin K", "Platelet GPIIb/IIIa"], 0,
  "Angiodysplasia: associated with vWF. (Book p201)")
q(201, S8, "The diagnosis of angiodysplasia is made by:",
  ["Colonoscopy and capsule endoscopy", "Barium enema", "Plain X-ray",
   "CT angiography alone"], 0,
  "Diagnosis: colonoscopy; capsule endoscopy. (Book p201)")
q(201, S8, "The treatment of angiodysplasia is:",
  ["Endoscopic/colonoscopic ligation of vessels", "Segmental colectomy always",
   "Embolization alone", "Anticoagulation"], 0,
  "Management: endoscopic/colonoscopic ligation of vessels. (Book p201)")

# ---------------- p201 · WORK UP OF LOWER GI HAEMORRHAGE ----------------
S9 = "Work-up of Lower GI Haemorrhage"
q(201, S9, "Frank blood in the stools is called:",
  ["Haematochezia", "Melaena", "Occult bleed", "Haematemesis"], 0,
  "Work up of lower GI hemorrhage: frank blood in stools (hematochezia). (Book p201)")
q(201, S9, "The first step in the work-up of lower GI haemorrhage is to:",
  ["Rule out local causes - haemorrhoids, fissures and polyps",
   "Do an urgent laparotomy", "Start a contrast enema", "Do an upper GI endoscopy"], 0,
  "1. Rule out local causes → hemorrhoids, fissures, polyps. (Book p201)")
q(201, S9, "The second step in the work-up of lower GI haemorrhage is to:",
  ["Stabilize the patient with IV fluids and keep nil per oral",
   "Arrange a colonoscopy", "Give a blood transfusion", "Do a CT angiogram"], 0,
  "2. Stabilize patient: IV fluids + NPO. (Book p201)")
q(201, S9, "In the work-up of lower GI haemorrhage, an upper GI endoscopy/NG tube is used to:",
  ["Detect bleeding from the stomach or duodenum",
   "Detect colonic bleeding", "Treat the bleeding", "Measure the portal pressure"], 0,
  "Upper GI endoscopy/NG tube: bleeding in stomach/duodenum → appropriate management. (Book p201)")
q(201, S9, "When upper GI endoscopy is negative in a patient with GI bleeding, the bleeding is termed:",
  ["Obscure GI haemorrhage (small intestinal bleed)",
   "Occult GI haemorrhage", "Overt upper GI bleed", "A spurious bleed"], 0,
  "Negative → obscure GI hemorrhage (small intestine bleed). (Book p201)")
q(201, S9, "Investigations for obscure (small intestinal) GI haemorrhage include all EXCEPT:",
  ["Barium enema", "PillCam capsule endoscopy", "CT angiography",
   "Technetium-99m pertechnetate scan"], 0,
  "Obscure GI hemorrhage: PillCam capsule endoscopy; CT angiography; Tc99m pertechnetate scan (most sensitive, up to 0.1 ml/min). (Book p201)")

# ---------------- p202 · IBD: CROHN'S vs UC ----------------
S10 = "Inflammatory Bowel Disease: Crohn's v/s Ulcerative Colitis"
q(202, S10, "Inflammatory bowel disease is:",
  ["An autoimmune condition", "An infectious condition", "A neoplastic condition",
   "A degenerative condition"], 0,
  "Inflammatory bowel disease: autoimmune conditions. (Book p202)")
q(202, S10, "The age distribution of Crohn's disease shows:",
  ["A first peak at 20-40 years and a second peak at around 70 years",
   "A single peak at 25-40 years", "A peak in the first decade",
   "No age predilection"], 0,
  "Crohn's - age: 1st peak 20-40 yrs, 2nd peak 70 yrs. (Book p202)")
q(202, S10, "The age group typically affected by ulcerative colitis is:",
  ["25-40 years", "1-10 years", "60-80 years", "All ages equally"], 0,
  "Ulcerative colitis: 25-40 yrs. (Book p202)")
q(202, S10, "In Crohn's disease the gender distribution is:",
  ["Females > males", "Males > females", "Equal", "Only males"], 0,
  "Crohn's disease: F > M. (Book p202)")
q(202, S10, "Risk factors for Crohn's disease include all EXCEPT:",
  ["Smoking cessation", "Smoking", "A refined diet", "NOD2/CARD15"], 0,
  "Risk factors (Crohn's): smoking; refined diet; NOD2/CARD15. (Book p202)")
q(202, S10, "In ulcerative colitis, smoking is:",
  ["Protective", "A strong risk factor", "Irrelevant", "A cause of relapse"], 0,
  "Ulcerative colitis: smoking is protective. (Book p202)")
q(202, S10, "The bowel involvement in Crohn's disease is:",
  ["Any portion of the bowel with skip lesions",
   "Continuous from the rectum upwards", "Limited to the colon",
   "Limited to the rectum"], 0,
  "Crohn's: any portion of bowel; skip lesions (+). (Book p202)")
q(202, S10, "The spread in ulcerative colitis is:",
  ["Continuous, with no skip lesions", "Patchy with skip lesions",
   "Limited to the terminal ileum", "Segmental"], 0,
  "Ulcerative colitis: continuous spread; skip lesions (-). (Book p202)")
q(202, S10, "The m/c presentation of ulcerative colitis is:",
  ["Proctitis", "Pancolitis", "Backwash ileitis", "Ileitis"], 0,
  "Ulcerative colitis: m/c - proctitis; also pancolitis and backwash ileitis. (Book p202)")
q(202, S10, "Backwash ileitis is a feature of:",
  ["Ulcerative colitis", "Crohn's disease", "Intestinal tuberculosis",
   "Coeliac disease"], 0,
  "Backwash ileitis: ulcerative colitis. (Book p202)")
q(202, S10, "Anal involvement with sinuses and abscesses is common in:",
  ["Crohn's disease", "Ulcerative colitis", "Both equally", "Neither"], 0,
  "Crohn's: anal involvement - common (sinuses/abscesses); UC: anal sparing (+). (Book p202)")
q(202, S10, "The rectum is relatively spared in:",
  ["Crohn's disease", "Ulcerative colitis", "Both", "Neither"], 0,
  "Crohn's: relative rectal sparing; UC: rectum commonly involved. (Book p202)")
q(202, S10, "The inflammation of ulcerative colitis involves the:",
  ["Mucosa and submucosa", "Full thickness of the bowel wall",
   "Muscularis only", "Serosa only"], 0,
  "Ulcerative colitis: mucosa + submucosal inflammation. (Book p202)")
q(202, S10, "Healing of the inflamed mucosa/submucosa in Crohn's disease leads to:",
  ["Stricture formation", "Pseudopolyps", "Backwash ileitis", "Toxic megacolon"], 0,
  "Crohn's: healing of mucosa/submucosa → leads to stricture formation. (Book p202)")
q(202, S10, "Fistulae such as colovesical and colovaginal fistulae occur in:",
  ["Crohn's disease", "Ulcerative colitis", "Both equally", "Neither"], 0,
  "Crohn's: → colovesical, → colovaginal fistulae. (Book p202)")
q(202, S10, "Creeping fat and a cobblestone appearance are features of:",
  ["Crohn's disease", "Ulcerative colitis", "Intestinal tuberculosis",
   "Coeliac disease"], 0,
  "Additional features (Crohn's): creeping fat; cobble stone appearance. (Book p202)")
q(202, S10, "Non-caseating granulomas on microscopy are seen in:",
  ["Crohn's disease", "Ulcerative colitis", "Intestinal tuberculosis",
   "Sarcoidosis of the colon"], 0,
  "Microscopy (Crohn's): non caseating granulomas. (Book p202)")
q(202, S10, "Pseudopolyps and crypt abscesses are features of:",
  ["Ulcerative colitis", "Crohn's disease", "Both equally", "Neither"], 0,
  "Ulcerative colitis: pseudopolyps; crypt abscess (+). (Book p202)")
q(202, S10, "The risk of toxic megacolon is higher in:",
  ["Ulcerative colitis", "Crohn's disease", "Both equally", "Neither"], 0,
  "Ulcerative colitis: ↑ risk of toxic megacolon. (Book p202)")
q(202, S10, "Toxic megacolon is defined as a large bowel diameter of:",
  [">6 cm", ">3 cm", ">10 cm", ">15 cm"], 0,
  "Toxic megacolon: large bowel diameter > 6 cm. (Book p202)")

# ---------------- p202-203 · C/F, RADIOLOGY, SEVERITY ----------------
S11 = "Clinical Features, Radiological Signs and Severity of IBD"
q(202, S11, "Clinical features of inflammatory bowel disease include:",
  ["Pain, fever, a raised TLC and a risk of perforation",
   "Jaundice and pruritus", "Haematuria", "Chest pain"], 0,
  "Clinical features: pain, fever, ↑ TLC; risk of perforation (+). (Book p202)")
q(203, S11, "Crohn's disease of the terminal ileum may clinically mimic:",
  ["Acute appendicitis", "Acute cholecystitis", "Acute pancreatitis",
   "Diverticulitis"], 0,
  "Crohn's: mimics acute appendicitis. (Book p203)")
q(203, S11, "The presenting feature of ulcerative colitis is:",
  ["Bloody diarrhoea", "Non-bilious vomiting", "Constipation", "Jaundice"], 0,
  "UC: bloody diarrhoea. (Book p203)")
q(203, S11, "The string sign of Kantor is seen in:",
  ["Both Crohn's disease and bowel tuberculosis", "Only ulcerative colitis",
   "Only diverticulitis", "Only coeliac disease"], 0,
  "Radiological signs: string sign of Kantor (also seen in bowel TB). (Book p203)")
q(203, S11, "Aphthous ulcers producing a target sign are seen in:",
  ["Crohn's disease", "Ulcerative colitis", "Diverticulitis", "Ischaemic colitis"], 0,
  "Aphthous ulcers: target sign. (Book p203)")
q(203, S11, "According to the modified Montreal classification, mild disease means:",
  ["<4 stools/day", ">4 stools/day with systemic signs", ">6 stools/day",
   ">10 stools/day"], 0,
  "Severity: 1. mild - <4 stools/day. (Book p203)")
q(203, S11, "Moderate disease in the modified Montreal classification means:",
  ["≥4 stools/day with no systemic signs", "<4 stools/day",
   ">6 stools/day with systemic signs", ">10 stools/day"], 0,
  "2. moderate: ≥4 stools/day, no systemic signs. (Book p203)")
q(203, S11, "Severe disease in the modified Montreal classification means:",
  [">6 stools/day with systemic signs", "<4 stools/day",
   ">10 stools/day with toxic megacolon", "≥4 stools/day without systemic signs"], 0,
  "3. severe: >6 stools/day with systemic signs. (Book p203)")
q(203, S11, "Fulminant disease in the modified Montreal classification means:",
  [">10 stools/day with toxic megacolon", ">6 stools/day", "<4 stools/day",
   "≥4 stools/day"], 0,
  "4. fulminant: >10 stools with toxic megacolon. (Book p203)")
q(203, S11, "The initial management of a severe attack/toxic megacolon includes:",
  ["IV fluids and IV antibiotics", "Oral steroids alone",
   "Immediate colectomy", "Antidiarrhoeals"], 0,
  "Management: IV fluids; IV antibiotics. (Book p203)")

# ---------------- p203 · CROHN'S MANAGEMENT ----------------
S12 = "Management of Crohn's Disease"
q(203, S12, "Medical management of Crohn's disease includes all EXCEPT:",
  ["Vitamin C supplements", "Steroids", "5-ASA derivatives (sulfasalazine)",
   "Monoclonal antibodies"], 0,
  "Medical management: steroids; 5 ASA derivatives (sulfasalazine); infliximab; vedolizumab. (Book p203)")
q(203, S12, "The drug used for perianal Crohn's disease is:",
  ["Infliximab", "Sulfasalazine", "Cholestyramine", "Teduglutide"], 0,
  "Infliximab: perianal disease. (Book p203)")
q(203, S12, "Vedolizumab used in inflammatory bowel disease is a:",
  ["Monoclonal antibody", "5-ASA derivative", "GLP-2 analogue",
   "TNF alpha converting enzyme"], 0,
  "Vedolizumab: monoclonal antibodies. (Book p203)")
q(203, S12, "Regarding surgery for Crohn's disease:",
  ["There is no definitive surgery", "Total proctocolectomy is curative",
   "Segmental resection is curative", "Colectomy is always required"], 0,
  "Surgical management of Crohn's: no definitive surgery. (Book p203)")
q(203, S12, "Perianal disease in Crohn's is managed with:",
  ["Setons", "Immediate proctectomy", "Fistulectomy in all cases",
   "Topical antibiotics only"], 0,
  "Perianal disease: setons. (Book p203)")
q(203, S12, "Indications for surgery in Crohn's disease include all EXCEPT:",
  ["Asymptomatic gallstones", "Steroid side effects",
   "Not responding to medical treatment", "Complications and extraintestinal manifestations"], 0,
  "Indications for surgery: steroid side effects; not responding to medicine; complications; extraintestinal manifestations. (Book p203)")

# ---------------- p204 · UC MANAGEMENT & EIMs ----------------
S13 = "Ulcerative Colitis: Management, Surgery and Extraintestinal Manifestations"
q(204, S13, "Medical management of ulcerative colitis includes:",
  ["Steroids, 5-ASA derivatives and monoclonal antibodies",
   "Steroids and antibiotics only", " Immunosuppression alone",
   "Antibiotics alone"], 0,
  "Medical management (UC): steroids; 5 ASA derivative (sulfasalazine); monoclonal antibodies. (Book p204)")
q(204, S13, "Indications for surgery in ulcerative colitis include all EXCEPT:",
  ["Incidental diverticulosis", "Steroid side effects",
   "Complications - toxic megacolon, obstruction, cancer",
   "Not responding to medical treatment"], 0,
  "Indications: steroid side effects; complications (toxic megacolon/obstruction/cancer); not responding to medicine; extra intestinal manifestations. (Book p204)")
q(204, S13, "The surgery performed for ulcerative colitis creates a:",
  ["\"J\" shaped pouch (ileal pouch-anal anastomosis)", "Straight ileoanal anastomosis",
   "Permanent ileostomy in all cases", "Kock's continent ileostomy only"], 0,
  "Surgery: \"J\" shaped pouch. (Book p204)")
q(204, S13, "The m/c complication after an ileal pouch is:",
  ["Pouchitis", "Dehydration", "Bleeding", "Small bowel obstruction"], 0,
  "Complications: m/c - pouchitis. (Book p204)")
q(204, S13, "The m/c cause of death in patients with an ileal pouch is:",
  ["Adhesive obstruction", "Pouchitis", "Pouch failure", "Malignancy"], 0,
  "m/c cause of death: adhesive obstruction. (Book p204)")
q(204, S13, "Dermatological extraintestinal manifestations of IBD include:",
  ["Erythema nodosum, pyoderma gangrenosum and oral ulcers",
   "Vitiligo and alopecia", "Psoriasis alone", "Eczema"], 0,
  "Dermatologic: erythema nodosum, pyoderma gangrenosum, oral ulcers (eg aphthous stomatitis). (Book p204)")
q(204, S13, "The hepatobiliary extraintestinal manifestation of IBD is:",
  ["Primary sclerosing cholangitis", "Primary biliary cirrhosis",
   "Gallbladder carcinoma", "Portal vein thrombosis"], 0,
  "Hepatobiliary: primary sclerosing cholangitis (PSC), fatty liver, autoimmune liver disease, cholelithiasis. (Book p204)")
q(204, S13, "Ophthalmological extraintestinal manifestations of IBD include:",
  ["Episcleritis, scleritis, uveitis, iritis and conjunctivitis",
   "Cataract and glaucoma", "Retinal detachment", "Optic neuritis"], 0,
  "Ophthalmologic: episcleritis, scleritis, uveitis, iritis, conjunctivitis. (Book p204)")
q(204, S13, "The renal manifestation associated with Crohn's disease is:",
  ["Calcium oxalate nephrolithiasis", "Urate nephropathy",
   "Amyloidosis of the kidney", "Renal cell carcinoma"], 0,
  "Renal: calcium oxalate nephrolithiasis (Crohn's disease). (Book p204)")
q(204, S13, "Musculoskeletal associations of IBD include:",
  ["Ankylosing spondylitis", "Osteoarthritis of the hip",
   "Rheumatoid arthritis", "Gout"], 0,
  "Musculoskeletal: note - ankylosing spondylitis (along with PSC). (Book p204)")
q(204, S13, "Haematological manifestations of IBD include:",
  ["Anaemia of chronic disease and iron deficiency anaemia",
   "Polycythaemia", "Haemophilia", "Thrombocytosis only"], 0,
  "Hematologic: anemia of chronic disease, iron-deficiency anemia. (Book p204)")

# ---------------- p205 · BOWEL TB ----------------
S14 = "Bowel Tuberculosis"
q(205, S14, "Abdominal tuberculosis may involve the:",
  ["Bowel, omentum and other abdominal organs",
   "Only the terminal ileum", "Only the peritoneum", "Only the liver"], 0,
  "Abdominal TB: bowel, omentum, organs. (Book p205)")
q(205, S14, "Caking of the omentum in abdominal tuberculosis:",
  ["Produces a mass mimicking cancer, diagnosed by biopsy and treated with ATT",
   "Is a clinical emergency", "Requires immediate laparotomy",
   "Is treated with steroids"], 0,
  "Caking of omentum → mass mimicking cancer → diagnosed by biopsy → ATT. (Book p205)")
q(205, S14, "Tuberculous pyoperitoneum presents with peritonitis and is treated by:",
  ["Emergency laparotomy plus ATT", "ATT alone", "Steroids alone",
   "Repeated aspiration"], 0,
  "Pyoperitoneum: clinical emergency - presents with peritonitis → emergency laparotomy + ATT. (Book p205)")
q(205, S14, "The immune response in ulcerative bowel TB is __________ and in hyperplastic bowel TB it is __________.",
  ["Weak; strong", "Strong; weak", "Absent; absent", "Moderate; strong"], 0,
  "Types: ulcerative - weak immune response; hyperplastic - strong immune response. (Book p205)")
q(205, S14, "The m/c site of ulcerative bowel TB is the:",
  ["Terminal ileum", "Caecum", "Jejunum", "Rectum"], 0,
  "Ulcerative bowel TB - site: terminal ileum (m/c). (Book p205)")
q(205, S14, "Hyperplastic bowel TB involves the:",
  ["Terminal ileum and ileocaecal junction", "Jejunum only",
   "Sigmoid colon", "Stomach"], 0,
  "Hyperplastic bowel TB - site: terminal ileum, ileocaecal junction (IC). (Book p205)")
q(205, S14, "A tuberculous ulcer of the bowel is:",
  ["Transverse and heals with a stricture", "Longitudinal and perforates",
   "Longitudinal and heals with a stricture", "Transverse and perforates"], 0,
  "Tubercular ulcer: transverse ulcer; heals with stricture. (Book p205)")
q(205, S14, "A typhoid ulcer of the bowel is:",
  ["Longitudinal and perforates in the 2nd/3rd week",
   "Transverse and heals with a stricture", "Transverse and perforates",
   "Longitudinal and heals with a stricture"], 0,
  "Typhoid ulcer: longitudinal ulcer; perforates in 2nd/3rd week. (Book p205)")
q(205, S14, "The diagnosis of typhoid perforation is supported by an X-ray showing:",
  ["Gas under the diaphragm", "A soap-bubble appearance",
   "A double bubble", "Multiple air-fluid levels"], 0,
  "Typhoid: X-ray - gas under diaphragm. (Book p205)")
q(205, S14, "The management of typhoid perforation is:",
  ["Emergency laparotomy with resection and anastomosis",
   "Conservative management with antibiotics", "Stricturoplasty",
   "Right hemicolectomy"], 0,
  "Typhoid: emergency laparotomy; resection anastomosis. (Book p205)")
q(205, S14, "Strictures of the bowel due to tuberculosis that lie close together are treated by:",
  ["Resection and anastomosis", "Stricturoplasty", "Bypass alone",
   "Dilatation"], 0,
  "Ulcerative bowel TB: resection & anastomosis (close strictures)/stricturoplasty (far strictures). (Book p205)")
q(205, S14, "Tubercular strictures that are far apart are treated by:",
  ["Stricturoplasty", "Resection and anastomosis", "Right hemicolectomy",
   "Dilatation alone"], 0,
  "Stricturoplasty for far strictures. (Book p205)")

# ---------------- p206 · HYPERPLASTIC BOWEL TB ----------------
S15 = "Hyperplastic Bowel Tuberculosis"
q(206, S15, "Clinical features of hyperplastic bowel TB include:",
  ["Pain and a mass in the right iliac fossa with weight loss",
   "Bilious vomiting", "Haematemesis", "Left iliac fossa mass"], 0,
  "Clinical features: pain, mass in RIF; weight loss. (Book p206)")
q(206, S15, "The main differential diagnosis of hyperplastic bowel TB is:",
  ["Cancer (caecal carcinoma)", "Crohn's disease", "Amoeboma",
   "Appendicular abscess"], 0,
  "D/o: cancer. (Book p206)")
q(206, S15, "The diagnosis of hyperplastic bowel TB is established by:",
  ["Colonoscopic biopsy", "Sputum AFB", "Mantoux test alone", "CECT alone"], 0,
  "Diagnosis: colonoscopic biopsy. (Book p206)")
q(206, S15, "Hyperplastic bowel TB that persists as a mass or causes obstruction is treated by:",
  ["Right hemicolectomy", "Stricturoplasty", "ATT alone",
   "Total colectomy"], 0,
  "Management: mass persists/obstruction → right hemicolectomy. (Book p206)")
q(206, S15, "The goose neck/swan neck deformity on a barium meal follow through is seen in:",
  ["Bowel tuberculosis", "Crohn's disease only", "Ulcerative colitis",
   "Coeliac disease"], 0,
  "Barium meal follow through: goose neck/swan neck deformity (bowel TB). (Book p206)")
q(206, S15, "The radiological signs of hyperplastic bowel TB include all EXCEPT:",
  ["A double bubble sign", "A pulled up ileocaecal junction",
   "The string sign of Kantor", "A stricture"], 0,
  "Signs: goose neck/swan neck deformity; string sign of Kantor; ↑ pulled up ICJ; stricture. (Book p206)")

# ---------------- p206-207 · FAECAL FISTULA ----------------
S16 = "Faecal Fistula: Types and Chance of Closure"
q(206, S16, "Clinical features of a faecal fistula include all EXCEPT:",
  ["Weight gain", "Faecal matter discharging from the main wound",
   "Skin excoriation", "Malnutrition and pain"], 0,
  "Clinical features: faecal matter discharging from main wound; skin excoriations (+); malnourished patient; excruciating pain. (Book p206)")
q(207, S16, "A high output fistula is defined as an output of:",
  [">500 cc/day", "<200 cc/day", ">1000 cc/day", ">100 cc/day"], 0,
  "High output: >500 cc/day. (Book p207)")
q(207, S16, "A low output fistula is defined as an output of:",
  ["<200 cc/day", ">500 cc/day", "<50 cc/day", ">200 cc/day"], 0,
  "Low output: <200 cc/day. (Book p207)")
q(207, S16, "Which fistula is most likely to close spontaneously?",
  ["One with an enteric wall defect <1 cm", "One with an enteric wall defect >1 cm",
   "One with an open abdomen", "One with a FRIEND factor"], 0,
  "Spontaneous closure: enteric wall defects <1 cm. (Book p207)")
q(207, S16, "A fistula with a tract longer than 2 cm:",
  ["Is more likely to close spontaneously", "Will not close spontaneously",
   "Always needs surgery", "Is always malignant"], 0,
  "Spontaneous closure: fistula tract >2 cm. (Book p207)")
q(207, S16, "An albumin level of __________ favours spontaneous closure of a fistula.",
  [">25 g/L", "<25 g/L", ">50 g/L", "<10 g/L"], 0,
  "Spontaneous closure: albumin >25 g/L. (Book p207)")
q(207, S16, "An output of __________ favours spontaneous closure of a fistula.",
  ["<200 ml/day", ">200 ml/day", ">500 ml/day", ">1000 ml/day"], 0,
  "Spontaneous closure: output <200 ml/day. (Book p207)")
q(207, S16, "Fistulae arising from the __________ are less likely to close spontaneously.",
  ["Stomach, ligament of Treitz or ileum", "Oesophagus",
   "Duodenal stump", "Jejunum"], 0,
  "No spontaneous closure: gastric, ligament of Treitz, ileal fistulae. (Book p207)")
q(207, S16, "FRIEND factors in a fistula are associated with:",
  ["Failure of spontaneous closure", "Spontaneous closure",
   "A better prognosis", "A low output fistula"], 0,
  "FRIEND factor (+) → no spontaneous closure. (Book p207)")

# ---------------- p207 · FISTULA MANAGEMENT & PROGNOSIS ----------------
S17 = "Management and Prognosis of Faecal Fistula"
q(207, S17, "FRIEND stands for all of the following EXCEPT:",
  ["Vitamin deficiency", "Foreign body", "Radiation", "Epithelialization of the tract"], 0,
  "FRIEND: foreign body, radiation, inflammation/IBD, infection, epithelialization of fistula tract, neoplasms, distal obstruction. (Book p207)")
q(207, S17, "The SNAP principle in the management of a faecal fistula includes:",
  ["Skin excoriation control and sepsis control",
   "Immediate definitive surgery", "Bowel rest alone", "Antibiotics alone"], 0,
  "SNAP: skin excoriation control, sepsis control; nutritional build up (TPN); anatomical delineation; planned surgery. (Book p207)")
q(207, S17, "Nutritional build up in a patient with a faecal fistula is achieved with:",
  ["TPN", "Oral feeds alone", "Nasogastric feeds", "Enteral supplements only"], 0,
  "Nutritional build up: TPN. (Book p207)")
q(207, S17, "The 'A' in the SNAP principle of fistula management stands for:",
  ["Anatomical delineation", "Antibiotics", "Analgesia", "Anastomosis"], 0,
  "Anatomical delineation. (Book p207)")
q(207, S17, "The 'P' in the SNAP principle of fistula management stands for:",
  ["Planned surgery", "Parenteral nutrition", "Peritoneal lavage", "Prokinetics"], 0,
  "Planned surgery. (Book p207)")
q(207, S17, "In the prognostic grouping of faecal fistulae, a group I (simple) fistula has:",
  ["An exceptional (very low) mortality and is expected to close spontaneously",
   "A mortality of 10-25%", "A mortality above 25%",
   "No chance of closure"], 0,
  "Prognostic group I: spontaneous closure; exceptional mortality. (Book p207)")
q(207, S17, "A group II (intermediate complexity) fistula is managed by __________ and has a mortality of __________.",
  ["Early surgical closure; 10-25%", "Spontaneous closure; <5%",
   "Late surgical closure; >25%", "Conservative management; 50%"], 0,
  "Prognostic group II: early surgical closure; mortality 10-25%. (Book p207)")
q(207, S17, "A group III (high complexity) fistula is managed by __________ and has a mortality of __________.",
  ["Late surgical closure; >25%", "Early surgical closure; 10-25%",
   "Spontaneous closure; <5%", "Conservative management alone; 100%"], 0,
  "Prognostic group III: late surgical closure; mortality >25%. (Book p207)")

# ---------------- units ----------------
def sec_ids(*labels):
    return [x["id"] for x in Q if x["sec"] in labels]
def first_page(label):
    for x in Q:
        if x["sec"] == label:
            return x["page"]
    return 0

UNIT_DEFS = [
    (S1, "An ileostomy pours out liquid effluent, so it excoriates the skin and deranges fluids and electrolytes far more than a colostomy does - but it is matured as a spout, everted and sutured above the skin level. A colostomy is semisolid, easier to live with, and sits flush with the skin. Site both away from bony landmarks along the outer border of the rectus: ileostomy in either iliac fossa, sigmoid colostomy in the left iliac fossa and a transverse colostomy in the epigastrium."),
    (S2, "Three shapes to recognise: an end (single barrel) stoma brings out one opening raised above the skin; a double barrel brings out the proximal and distal ends separately, two openings that do not touch; and a loop stoma brings out a loop so the two openings sit side by side, joined and flush with the skin."),
    (S3, "A temporary stoma is built to protect a fresh anastomosis and is closed 8-10 weeks later; a permanent one is usually an end colostomy. Excoriations are the commonest problem, and prolapse and retraction the other mechanical ones, while a parastomal hernia is the commonest late problem of a colostomy - commoner with a loop than an end stoma - and is repaired with mesh."),
    (S4, "Less than 200 cm of small bowel is short bowel syndrome; under 100 cm the patient is a net secretor and above it a net absorber. Superior mesenteric artery embolism is the commonest cause, followed by Crohn's disease and, in children, malrotation or atresia. The patient malabsorbs, loses weight and has rapid-transit diarrhoea with bacterial overgrowth. Keep the ileum if you can - it adapts - because losing it costs you vitamin B12 and a string of other nutrients."),
    (S5, "Long term parenteral nutrition keeps these patients alive and intestinal transplantation is the definitive option. Teduglutide, a GLP-2 analogue, and cholestyramine help, and when anatomy allows, the bowel can be lengthened: the Bianchi procedure splits it longitudinally with staplers along the mesenteric border and re-anastomoses it end to end to make a zig-zag, while serial transverse enteroplasty simply increases the length."),
    (S6, "Colonic diverticula are false - only mucosa herniates - and they cluster in the sigmoid of constipated patients in their fourth and fifth decades. Diverticulosis is many diverticula without inflammation and shows the saw tooth pattern on a barium enema."),
    (S7, "Bleeding is usually from the right side, found on CT angiography and treated by embolization with resection as the definitive step. Diverticulitis gives left-sided pain, diarrhoea and fever with a raised count, and CECT is the investigation of choice. Grade it with Hinchey: pericolic abscess is stage I, pelvic abscess stage II, faecal peritonitis stage IV. Stages I and II settle with antibiotics, analgesia and pigtail drainage; stages III and IV go to theatre for a Hartmann's. Long standing disease also predisposes to colorectal cancer."),
    (S8, "Angiodysplasia belongs to the elderly - seventh decade - sits on the right side and above all in the caecum, and is the second commonest cause of massive lower GI bleeding. It is linked with von Willebrand factor, found on colonoscopy or capsule endoscopy, and treated by endoscopic ligation of the vessels."),
    (S9, "Work up haematochezia in order: exclude the local causes - piles, fissures, polyps - then resuscitate with fluids and keep the patient nil by mouth, then look proximally with an endoscope or NG tube, because blood from the stomach or duodenum changes everything. If that is negative you have an obscure, small intestinal bleed and the tools are capsule endoscopy, CT angiography and the technetium pertechnetate scan, sensitive to 0.1 ml/min."),
    (S10, "Two autoimmune diseases, one table. Crohn's peaks at 20-40 and again at 70, is commoner in women, follows smoking, refined diets and NOD2/CARD15, involves any part of the gut with skip lesions and relative rectal sparing, fistulates into bladder and vagina, heals by stricturing, and shows creeping fat, cobblestoning and non-caseating granulomas. Ulcerative colitis presents at 25-40, is protected by smoking, spreads continuously from the rectum with proctitis, pancolitis and backwash ileitis, keeps the anus, is confined to mucosa and submucosa with pseudopolyps and crypt abscesses, and carries the higher risk of toxic megacolon - a colon wider than 6 cm."),
    (S11, "Both cause pain, fever, a raised count and a risk of perforation; terminal ileal Crohn's apes appendicitis while ulcerative colitis declares itself with bloody diarrhoea. The string sign of Kantor is shared with intestinal tuberculosis, and aphthous ulcers give the target sign. Severity is counted in stools: fewer than four a day is mild, four or more without systemic signs moderate, more than six with systemic signs severe, and more than ten with toxic megacolon fulminant. The acute attack is treated with IV fluids and IV antibiotics."),
    (S12, "Crohn's is controlled with steroids, 5-ASA drugs such as sulfasalazine, infliximab for perianal disease and monoclonal antibodies like vedolizumab. There is no definitive operation - you operate for steroid side effects, failure of medical treatment, complications or extraintestinal disease - and perianal sepsis is managed with setons."),
    (S13, "Ulcerative colitis uses the same medical ladder - steroids, 5-ASA and monoclonals - and surgery is indicated for the same reasons plus the complications of toxic megacolon, obstruction and cancer. The operation creates a J pouch; pouchitis is its commonest problem and adhesive obstruction its commonest cause of death. Look beyond the bowel too: erythema nodosum, pyoderma gangrenosum and mouth ulcers; primary sclerosing cholangitis; episcleritis and uveitis; anaemia of chronic disease; calcium oxalate stones in Crohn's; and remember ankylosing spondylitis alongside PSC."),
    (S14, "Abdominal tuberculosis touches bowel, omentum and organs. A caked omentum mimics a cancer, is diagnosed on biopsy and treated with antituberculous therapy, while tuberculous pyoperitoneum is a surgical emergency needing laparotomy plus ATT. Ulcerative disease is the weak immune response and sits in the terminal ileum; hyperplastic disease is the strong response and sits at the ileocaecal junction. Remember the ulcer geometry - tuberculous ulcers are transverse and heal by stricturing, typhoid ulcers are longitudinal and perforate in the second or third week with gas under the diaphragm. Close strictures are resected and anastomosed, distant ones are dealt with by stricturoplasty."),
    (S15, "Hyperplastic disease presents with pain, a right iliac fossa mass and weight loss and is mistaken for cancer; colonoscopic biopsy makes the diagnosis and a right hemicolectomy is needed if the mass persists or obstructs. On a barium follow through look for the goose neck or swan neck deformity, the string sign of Kantor, a pulled up ileocaecal junction and strictures."),
    (S16, "A faecal fistula discharges stool from the wound, excoriates the skin and leaves the patient malnourished and in pain. Above 500 cc a day it is a high output fistula; below 200 cc a day it is low. Spontaneous closure is favoured by a defect under 1 cm, a tract longer than 2 cm, a closed abdomen, albumin above 25 g/L, an output under 200 ml a day and the absence of FRIEND factors - and by a jejunal, duodenal stump or oesophageal origin rather than a gastric, ligament of Treitz or ileal one."),
    (S17, "FRIEND lists everything that keeps a fistula open: foreign body, radiation, inflammation or inflammatory bowel disease, infection, epithelialization of the tract, neoplasms and distal obstruction. Treat by SNAP - control the skin and the sepsis, build the patient up with parenteral nutrition, delineate the anatomy and then operate when planned. Prognosis runs in three groups: simple fistulae close by themselves with exceptional mortality, intermediate ones need early surgery with 10-25% mortality, and complex ones need late surgery with mortality beyond 25%."),
]

UNITS = []
for i, (title, guide) in enumerate(UNIT_DEFS, 1):
    UNITS.append({"id": f"SURG-U29-{i}", "ch": 29, "n": i, "title": title,
                  "sec": f"{title} · p{first_page(title)}",
                  "qs": sec_ids(title), "guide": guide})

covered = [i for u in UNITS for i in u["qs"]]
assert covered == [x["id"] for x in Q], "units must cover questions in order"

data = {"questions": Q, "units": UNITS}
with open("data/ch29.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
print(f"ch29: {len(Q)} questions, {len(UNITS)} units")
