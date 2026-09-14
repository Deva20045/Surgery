#!/usr/bin/env python3
"""Build data/ch60.json — Hernia : Part 2 (Marrow Surgery Ed 8, pp460-469)."""
import json

Q = []

def q(page, sec, text, correct, wrongs, note=None):
    opts = [correct] + list(wrongs)
    assert len(opts) == 4
    Q.append({
        "id": f"SURG-C60-{len(Q)+1:03d}",
        "sec": sec,
        "page": page,
        "q": text,
        "opts": opts,
        "ans": 0,
        "exp": (note or correct) + f" (Book p{page})",
    })

# ------------------------------------------------------------------ p460
S1 = "Femoral Hernia: Anatomy and Clinical Features"
q(460, S1, "Femoral hernia is m/c in:", "Females > males", ["Males > females", "Only infants", "Only elderly males"])
q(460, S1, "MEDIAL boundary of femoral ring:", "Lacunar ligament", ["Inguinal ligament", "Cooper's ligament", "Femoral vein"])
q(460, S1, "SUPERIOR boundary of femoral ring:", "Inguinal ligament", ["Lacunar ligament", "Pectineal ligament", "Iliopsoas"])
q(460, S1, "INFERIOR boundary of femoral ring:", "Pectineal / Cooper's ligament", ["Inguinal ligament", "Lacunar ligament", "Pubic tubercle"])
q(460, S1, "LATERAL boundary of femoral ring:", "Septum separating it from femoral vein", ["Lacunar ligament", "Iliopsoas tendon", "Pubic tubercle"])
q(460, S1, "Femoral ring is limited in expansion because rigid structures border it on:", "3 sides", ["1 side", "2 sides", "No side"])
q(460, S1, "Rigid femoral ring boundaries lead to:", "↑rate of strangulation", ["Always reducible", "No symptoms", "Bilateral hernia"])
q(460, S1, "Hernia type common in the narrow femoral ring:", "Richter's hernia", ["Maydl's hernia", "Sliding hernia", "Littre's hernia"])
q(460, S1, "Inguinal vs femoral hernia in relation to pubic tubercle:", "Inguinal above & medial; femoral below & lateral", ["Inguinal below & lateral; femoral above & medial", "Both above", "Both below"])
q(460, S1, "Clinical features of femoral hernia:", "Pain & swelling", ["Only cough impulse", "Scrotal mass", "Dysphagia"])
q(460, S1, "Psoas abscess as a D/D of femoral hernia shows:", "Fever, cross fluctuation & hip in flexion", ["Cough impulse", "Irreducibility", "Bowel sounds over swelling"])
q(460, S1, "Saphena varix is:", "Dilated terminal end of great saphenous vein", ["Enlarged lymph node", "Femoral hernia", "Lipoma"])
q(460, S1, "Ix of femoral hernia:", "USG", ["MRI", "CXR", "NCCT"])
q(460, S1, "Psoas abscess sign of the hip:", "Hip in flexion", ["Hip in extension", "Hip in abduction", "Hip fixed in adduction"])

# ------------------------------------------------------------------ p461
S2 = "Femoral Hernia: Management and Special Types"
q(461, S2, "Surgery of choice for femoral hernia:", "Laparoscopic hernioplasty", ["Lockwood repair", "McEvedy repair", "Taxis"])
q(461, S2, "LOW approach femoral hernia repair:", "Lockwood repair — below inguinal ligament — uncomplicated hernia", ["Above the ligament", "McEvedy", "For strangulation"])
q(461, S2, "HIGH approach femoral hernia repair:", "McEvedy repair — above inguinal ligament — strangulated/obstructed hernia", ["Below the ligament", "Lockwood", "Only elective"])
q(461, S2, "LAUGIER'S hernia:", "Through lacunar ligament; ↑risk of strangulation", ["Behind femoral vessels", "Through obturator canal", "In front of vessels"])
q(461, S2, "NARATH'S hernia is seen in:", "Congenital dislocation of hip", ["Cirrhosis", "Pregnancy", "Athletes"])
q(461, S2, "SERAFINI hernia:", "Retrovascular (behind femoral vessels)", ["Prevascular", "Through lacunar ligament", "Through obturator canal"])
q(461, S2, "VELPEAU hernia:", "Prevascular (in front of femoral vessels)", ["Retrovascular", "Through lacunar ligament", "Behind iliopsoas"])

# ------------------------------------------------------------------ p461-462
S3 = "Ventral Hernias: Types and EHS Classification"
q(461, S3, "Ventral hernias are:", "Abdominal wall hernias", ["Only diaphragmatic", "Intra-abdominal", "Pelvic floor"])
q(461, S3, "The m/c ventral hernia:", "Incisional", ["Umbilical", "Epigastric", "Spigelian"])
q(461, S3, "Ventral hernia types include:", "Epigastric, umbilical, paraumbilical, traumatic, Spigelian, lumbar, parastomal & incisional", ["Inguinal & femoral only", "Hiatus hernia", "Obturator"])
q(461, S3, "Inguinal hernia under ventral hernias:", "Not included", ["Included", "Subtype of lumbar", "EHS M3"])
q(461, S3, "EHS midline zones: M1-M5 are:", "Subxiphoidal, epigastric, umbilical, infraumbilical & suprapubic", ["Subcostal, flank, iliac, lumbar", "Lateral zones", "Five sacs"])
q(462, S3, "EHS lateral zones L1-L4:", "Subcostal, flank, iliac & lumbar", ["M1-M5 names", "Epigastric divisions", "Sac sizes"])
q(461, S3, "In EHS, the UMBILICAL zone is:", "M3", ["M1", "M2", "M4"])

# ------------------------------------------------------------------ p462
S4 = "Surgical Management of Ventral Hernia and Types of Repair"
q(462, S4, "Surgery of choice for ventral hernia:", "Hernioplasty", ["Tissue repair", "Taxis", "Darning"])
q(462, S4, "Tissue repair is AVOIDED in ventral hernia because:", "↑Tension → ↑Breakdown → Recurrence", ["It needs mesh", "It is costlier", "It causes infection only"])
q(462, S4, "ONLAY mesh repair:", "Over the rectus sheath", ["Behind the muscle", "In the sheath split", "Inside peritoneum"])
q(462, S4, "INLAY mesh repair:", "With the rectus sheath (bridging)", ["Over the sheath", "Behind muscle", "Over peritoneum"])
q(462, S4, "RETROMUSCULAR repair:", "Behind the muscle", ["Over the sheath", "With the sheath", "Intraperitoneal"])
q(462, S4, "PREPERITONEAL repair:", "Over the peritoneum", ["Under the peritoneum", "Behind muscle", "Over the sheath"])
q(462, S4, "The m/c intraperitoneal repair:", "IPOM (intraperitoneal placement of mesh)", ["Onlay", "Inlay", "Darning"])
q(462, S4, "Mesh used in IPOM:", "PTFE — does not adhere to bowel", ["Prolene", "Polyester", "Vicryl"])

# ------------------------------------------------------------------ p462
S5 = "Incisional Hernia"
q(462, S5, "Incisional hernia is formed:", "In the region of a scar", ["At the umbilicus only", "Through the obturator canal", "In the diaphragm"])
q(462, S5, "Incidence after OPEN abdominal surgeries:", "30-50%", ["1-5%", "70%", "0.5%"])
q(462, S5, "Incidence after LAPAROSCOPIC surgeries:", "1-5%", ["30-50%", "10-20%", "60%"])
q(462, S5, "Repair of choice in incisional hernia:", "IPOM / Hernioplasty", ["Keel repair", "Da Silva repair", "Tissue repair"])
q(462, S5, "NOT preferred in incisional hernia:", "Tissue repair (Keel & Da Silva)", ["IPOM", "Hernioplasty", "Mesh repair"])
q(462, S5, "RAMIREZ component separation uses:", "Lateral releasing incisions to avoid loss of domain", ["Mesh plug", "Tissue gluing", "Muscle cutting"])
q(462, S5, "Lateral releasing incisions prevent:", "Abdominal compartment syndrome", ["Recurrence", "Seroma", "Infection"])
q(462, S5, "Indication for Ramirez component separation:", "Hernia volume >25% abdominal volume", [">50%", ">5%", "Any size"])

# ------------------------------------------------------------------ p463
S6 = "Epigastric Hernia and Umbilical vs Paraumbilical"
q(463, S6, "Epigastric hernia is also called:", "Fatty hernia of linea alba", ["Gilmore's groin", "Petit's hernia", "Grynfeltt hernia"])
q(463, S6, "Gender predilection of epigastric hernia:", "Males > females", ["Females > males", "Equal", "Only females"])
q(463, S6, "Typical patient of epigastric hernia:", "Young, fit males", ["Obese multiparous women", "Newborns", "Elderly bedridden"])
q(463, S6, "Site of epigastric hernia:", "Anywhere b/w xiphisternum & umbilicus (m/c midline)", ["Only below umbilicus", "Lateral to rectus", "In lumbar triangle"])
q(463, S6, "Defect of epigastric hernia:", "Single/multiple transverse slits", ["Large round ring", "Oblique canal", "Femoral ring"])
q(463, S6, "M/c content of epigastric hernia:", "Pre-peritoneal fat", ["Bowel", "Omentum only", "Bladder"])
q(463, S6, "Epigastric hernia pain mimics:", "Peptic ulcer", ["Renal colic", "Appendicitis", "Cholecystitis"])
q(463, S6, "Mx of epigastric hernia:", "Open / laparoscopic (IPOM)", ["Taxis", "Truss", "Observation"])
q(463, S6, "UMBILICAL hernia defect:", "Through the umbilical ring — LARGE", ["Adjacent to umbilicus", "Narrow slit", "Subxiphoid"])
q(463, S6, "PARAUMBILICAL hernia defect:", "Adjacent to umbilicus — NARROW → strangulation / Richter's hernia", ["Large ring", "Always wide", "Through rectus only"])
q(463, S6, "Umbilicus in umbilical hernia:", "Everted", ["Forms boundary of defect", "Normal", "Absent"])
q(463, S6, "In paraumbilical hernia the umbilicus:", "Forms the boundary of the defect", ["Is everted", "Is inside the sac", "Is removed"])
q(463, S6, "Umbilical hernia is seen in:", "Newborns & ascites/cirrhosis patients", ["Only athletes", "Only elderly males", "Premature only"])
q(463, S6, "Paraumbilical hernia is seen in:", "Obese patients", ["Newborns", "Cirrhosis only", "Children"])
q(463, S6, "Mx of newborn umbilical hernia:", "Conservative x 2-3 yrs; surgery if it persists", ["Immediate surgery", "Truss", "Strapping permanent"])
q(463, S6, "Mx of paraumbilical hernia:", "Early surgery — hernioplasty", ["Conservative", "Observation", "Taxis"])

# ------------------------------------------------------------------ p464
S7 = "Omphalocele vs Gastroschisis"
q(464, S7, "Omphalocele & gastroschisis are m/c in:", "Newborn children", ["Adolescents", "Adults", "Elderly"])
q(464, S7, "Omphalocele defect:", "Through the umbilicus; bowel fails to return inside", ["Adjacent to umbilicus", "Through diaphragm", "Through linea alba above"])
q(464, S7, "Gastroschisis defect:", "Adjacent to the umbilicus", ["Through the umbilicus", "Retrosternal", "Lumbar"])
q(464, S7, "Peritoneal covering in omphalocele:", "Covered with peritoneum (membranous sac)", ["Not covered", "Skin covered only", "Partially covered"])
q(464, S7, "Covering of gastroschisis bowel:", "Not covered (exposed bowel)", ["Peritoneal sac", "Full skin", "Amnion only"])
q(464, S7, "Complications of omphalocele:", "Large defects; liver can also herniate", ["Ateresia always", "Perforation only", "Bleeding"])
q(464, S7, "Bowel exposed in gastroschisis ↑ risk of:", "Atresia, inflammation & perforation", ["Malignancy", "Cirrhosis", "Volvulus only"])
q(464, S7, "Congenital anomalies association:", "Omphalocele — associated with other congenital anomalies; gastroschisis — less", ["Gastroschisis — more anomalies", "Both equal", "Neither"])
q(464, S7, "Associations of omphalocele:", "Beckwith-Wiedemann syndrome & trisomy 13, 18, 21", ["Turner syndrome only", "Marfan syndrome", "Down only"])
q(464, S7, "Organs labelled herniating through the umbilicus in the omphalocele photo:", "Liver (under membrane)", ["Spleen", "Kidney", "Lung"])
q(464, S7, "Mx sequence of omphalocele/gastroschisis:", "Create a SILO (mesh cylinder over defect) → gradually reduce height → internalize the mesh", ["Immediate closure", "Truss", "Reimplant bowel"])

# ------------------------------------------------------------------ p465
S8 = "Lumbar Hernia and Spigelian Hernia"
q(465, S8, "1° lumbar hernia is:", "Rare", ["M/c", "Always bilateral", "Post-incisional"])
q(465, S8, "2° lumbar hernia:", "M/c; secondary to trauma/surgery/incision", ["Congenital only", "Rare", "Through Grynfeltt only"])
q(465, S8, "D/D: LIPOMA over lumbar area shows:", "Slip sign (+) & pseudofluctuation (+)", ["Cough impulse", "Bowel sounds", "Transmitted pulsation"])
q(465, S8, "Lumbar PSEUDOHERNIA is d/t:", "Muscle weakness (subcostal nerve injury)", ["True sac", "Diastasis recti", "Ascites"])
q(465, S8, "INFERIOR lumbar triangle of Petit — boundaries:", "Iliac crest (inferior), external oblique (lateral) & latissimus dorsi (medial)", ["12th rib superior", "Internal oblique lateral", "Sacospinalis medial"])
q(465, S8, "SUPERIOR lumbar triangle of Grynfeltt — boundaries:", "Internal oblique (lateral), sacrospinalis (medial) & 12th rib (superior)", ["Iliac crest inferior", "External oblique lateral", "Latissimus medial"])
q(465, S8, "Mx of lumbar hernia — open repair:", "Dowd Ponka repair (mesh hernioplasty)", ["Keel repair", "Bassini", "McVay"])
q(465, S8, "M/c approach for lumbar hernia mesh hernioplasty:", "Laparoscopic", ["Open", "Taxis", "Robotic only"])
q(465, S8, "SPIGELIAN hernia is also called:", "Intra-parietal hernia (in between abdominal muscles)", ["Little old lady's hernia", "Fatty hernia of linea alba", "Petit hernia"])
q(465, S8, "Spigelian hernia course:", "Along the outer border of rectus", ["Midline", "Below inguinal ligament", "In lumbar triangle"])
q(465, S8, "Spigelian fascia is a modification of:", "Transversalis fascia", ["External oblique", "Internal oblique aponeurosis only", "Rectus sheath only"])
q(465, S8, "Site of Spigelian hernia:", "Outer border of rectus, BELOW umbilicus, ABOVE arcuate line", ["Above umbilicus", "Below arcuate line", "Midline"])
q(466, S8, "Spigelian defect size:", "Children: small; adult: large", ["Children large", "Always small", "Always huge"])
q(466, S8, "Complication of Spigelian hernia:", "Strangulation", ["Never obstructs", "Fistula", "Malignancy"])

# ------------------------------------------------------------------ p466
S9 = "Obturator, Richter's and Maydl's Hernia"
q(466, S9, "OBTURATOR hernia is also called:", "Little old lady's hernia", ["Spigelian hernia", "Fatty hernia", "Petit hernia"])
q(466, S9, "Obturator hernia occurs through:", "Narrow defect — obturator canal (m/c in elderly multiparous women)", ["Wide ring", "Lacunar ligament", "Linea alba"])
q(466, S9, "Obturator hernia complications:", "Strangulation & Richter's hernia", ["Only irreducibility", "Meshoma", "Hydrocele"])
q(466, S9, "Clinical features of obturator hernia:", "Bowel obstruction & pain", ["Painless swelling in groin", "Scrotal mass", "Dysphagia"])
q(466, S9, "HOWSHIP ROMBERG sign:", "Shooting pain along obturator nerve on abduction & medial rotation of hip", ["Adductor reflex absent", "Patellar reflex absent", "Pain on cough"])
q(466, S9, "HANNINGTON KIFF sign:", "Adductor reflex (–) with patellar reflex (+) — d/t obturator nerve compression", ["Both reflexes absent", "Adductor +, patellar –", "Only Babinski +"])
q(466, S9, "Mx of obturator hernia:", "Hernioplasty", ["Taxis", "Truss", "Observation"])
q(466, S9, "RICHTER'S hernia defect:", "Very narrow", ["Large", "Wide canal", "No defect"])
q(466, S9, "Richter's hernia is seen in:", "Paraumbilical, femoral & obturator hernias", ["Only inguinoscrotal", "Epigastric only", "Lumbar only"])
q(466, S9, "Richter's hernia — what herniates?", "Protrusion of one wall of bowel (portion of circumference); lumen continuity preserved", ["Whole lumen", "Only omentum", "Meckel's diverticulum"])
q(466, S9, "Signs of Richter's hernia:", "Gastroenteritis → progress to strangulation/peritonitis", ["Full obstruction day 1", "Painless mass", "Jaundice"])
q(466, S9, "MAYDL'S hernia defect:", "Large (W-shaped hernia)", ["Very narrow", "Slit", "Ring only"])
q(466, S9, "In Maydl's hernia, the CONNECTING portion lies:", "Intraperitoneal (obstructed loop within peritoneal cavity)", ["In the sac always", "Extraperitoneal", "In the cord"])
q(467, S9, "Complication of Maydl's hernia affects which part FIRST?", "Connecting portion (easily missed during surgery)", ["Sac portion", "Proximal bowel", "Omentum"])

# ------------------------------------------------------------------ p467-468
S10 = "Congenital Diaphragmatic Hernia (Bochdalek vs Morgagni)"
q(467, S10, "The m/c congenital diaphragmatic hernia:", "Bochdalek", ["Morgagni", "Hiatus", "Traumatic"])
q(467, S10, "Bochdalek hernia location:", "Left postero-lateral", ["Right antero-medial", "Central", "Retrosternal"])
q(467, S10, "Morgagni hernia location:", "Right antero-medial", ["Left postero-lateral", "Esophageal", "Lumbar"])
q(467, S10, "Bochdalek defect:", "Defective development of pleuroperitoneal canal/membrane", ["Defective central tendon", "Esophageal hiatus", "Trauma"])
q(467, S10, "Morgagni defect:", "Defective central tendon of diaphragm", ["Pleuroperitoneal canal", "Aortic hiatus", "Foramen of Winslow"])
q(467, S10, "Herniated contents of BOCHDALEK:", "Stomach, spleen & transverse colon", ["Only transverse colon", "Liver only", "Kidney"])
q(467, S10, "Herniated content of MORGAGNI:", "Transverse colon", ["Stomach & spleen", "Small bowel only", "Liver"])
q(467, S10, "Maternal feature of CDH:", "Polyhydramnios in the antenatal period", ["Oligohydramnios", "Normal liquor", "Hydrops only"])
q(467, S10, "Newborn features of CDH:", "Scaphoid abdomen & respiratory distress", ["Distended abdomen", "Bilious vomiting only", "Cyanosis alone"])
q(467, S10, "M/c cause of death in CDH:", "Pulmonary hypoplasia → hypoxia", ["Pulmonary hypertension", "Sepsis", "Renal failure"])
q(467, S10, "2nd m/c cause of death in CDH:", "Pulmonary hypertension (after pulmonary vasoconstriction)", ["Pulmonary hypoplasia", "Pneumothorax", "Cardiac failure"])
q(467, S10, "Ix of CDH:", "CXR (bowel in thorax; Ryle's tube seen) & bowel sounds (+) in thoracic cavity on auscultation", ["MRI", "USG only", "CT"])
q(468, S10, "Ventilation of choice in CDH:", "IPPV (intermittent positive pressure ventilation)", ["Bag and mask", "CPAP only", "NIV"])
q(468, S10, "If IPPV fails in CDH:", "ECMO", ["Immediate surgery", "Steroids", "Surfactant only"])
q(468, S10, "C/I in CDH ventilation:", "Bag and mask ventilation", ["IPPV", "ECMO", "Nitrates"])
q(468, S10, "Inhaled nitrates in CDH are for:", "Pulmonary hypertension", ["Sedation", "Analgesia", "Infection"])
q(468, S10, "Surgery of CDH:", "Circumferential incision over diaphragm f/b mesh to cover defect", ["Thoracotomy closure only", "No surgery", "Lung transplant"])

# ------------------------------------------------------------------ p468-469
S11 = "Internal Hernias"
q(468, S11, "STEMMER'S hernia:", "Through transverse mesocolon", ["Behind Roux limb", "Through fossa of Landzert", "Behind SMA"])
q(468, S11, "PETERSEN'S hernia:", "Behind the Roux limb", ["Through transverse mesocolon", "Behind IMV", "Through Waldeyer fossa"])
q(468, S11, "LEFT paraduodenal hernia passes through:", "Fossa of Landzert", ["Fossa of Waldeyer", "Petersen defect", "Foramen of Winslow"])
q(468, S11, "Left paraduodenal hernia mechanism:", "Defective fusion of descending colon mesentery", ["Defective fusion of ascending colon", "SMA compression", "Gastrojejunostomy"])
q(468, S11, "Left paraduodenal hernia lies behind:", "Inferior mesenteric vessel", ["Superior mesenteric vessels", "Aorta", "Portal vein"])
q(468, S11, "RIGHT duodeno-jejunal hernia:", "D/t defective fusion of ascending colon mesentery; behind superior mesenteric vessels", ["Through Landzert fossa", "Behind IMV", "Through transverse mesocolon"])

# ------------------------------------------------------------------ p469
S12 = "Mesenteric Cysts"
q(469, S12, "The m/c mesenteric cyst:", "Chylolymphatic", ["Enterogenous", "Dermoid", "Hydatid"])
q(469, S12, "Wall of chylolymphatic cyst:", "Thin", ["Thick", "Calcified", "Muscular"])
q(469, S12, "Wall of enterogenous cyst:", "Thick", ["Thin", "Fibrous only", "Absent"])
q(469, S12, "Blood supply of chylolymphatic cyst:", "Independent", ["Shared with bowel", "From SMA only", "Retrograde"])
q(469, S12, "Blood supply of enterogenous cyst:", "Shared with bowel", ["Independent", "None", "Collateral only"])
q(469, S12, "Content of chylolymphatic cyst:", "Sequestered lymphatic tissue", ["Sequestered bowel tissue", "Keratin", "Lymph"])
q(469, S12, "Content of enterogenous cyst:", "Sequestered bowel tissue", ["Lymphatic tissue", "Chyle", "Pus"])
q(469, S12, "Fluid in chylolymphatic cyst:", "Clear", ["Turbid", "Hemorrhagic", "Purulent"])
q(469, S12, "Transillumination of mesenteric cysts:", "Chylolymphatic (+); enterogenous (–)", ["Both +", "Both –", "Enterogenous (+)"])
q(469, S12, "Attachment of mesentery runs between:", "DJ flexure & right sacroiliac joint", ["Pylorus & cecum", "Treitz & left sacroiliac", "DJ flexure & pubis"])
q(469, S12, "Tillaux triad (1 & 3):", "Periumbilical swelling & transverse band of resonance", ["Scaphoid abdomen", "Bowel sounds in chest", "Shifting dullness"])
q(469, S12, "Tillaux SIGN:", "Cyst moves at right angle to the attachment of mesentery", ["Moves along mesentery", "Fixed", "Moves with respiration only"])
q(469, S12, "IOC for mesenteric cyst:", "CECT", ["USG", "MRI", "X-ray"])
q(469, S12, "Surgery for chylolymphatic cyst:", "Enucleation", ["Resection + anastomosis", "Marsupialization", "Drainage"])
q(469, S12, "Surgery for enterogenous cyst:", "Resection + anastomosis", ["Enucleation", "Aspiration", "Sclerotherapy"])

# ------------------------------------------------------------------ units
UNIT_DEFS = [
    (S1, "Femoral hernia — the female-predominant one — squeezes through a ring walled by lacunar (medial), inguinal (superior) and Cooper's ligaments (inferior) with only a vein septum laterally: three rigid sides mean high strangulation rates and Richter's hernias. It sits below-lateral to the pubic tubercle; psoas abscess (fever, cross-fluctuation, flexed hip), lymph node and saphena varix crowd the differential, and USG sorts it out."),
    (S2, "Early surgery is the rule — laparoscopic hernioplasty is the choice; Lockwood goes below the inguinal ligament for uncomplicated cases while McEvedy goes above for strangulated/obstructed ones. Special escapes: Laugier through the lacunar ligament, Narath with congenital hip dislocation, Serafini behind the vessels and Velpeau in front."),
    (S3, "Ventral hernias are all abdominal-wall hernias except inguinal — incisional is the m/c. EHS maps midline M1-M5 (subxiphoid → suprapubic, umbilical = M3) and lateral L1-L4 (subcostal, flank, iliac, lumbar)."),
    (S4, "Hernioplasty wins and tissue repair loses (tension → breakdown → recurrence). Mesh sits onlay over the sheath, inlay within it, retromuscular behind muscle, preperitoneal over peritoneum, or intraperitoneally as the m/c IPOM — always with non-adherent PTFE against bowel."),
    (S5, "Incisional hernias bloom along scars — 30-50% after open and 1-5% after laparoscopic surgery. IPOM/hernioplasty is the repair of choice (Keel and Da Silva tissue repairs are out), and giant defects >25% of abdominal volume call for Ramirez component separation with lateral releasing incisions to prevent loss of domain and abdominal compartment syndrome."),
    (S6, "Epigastric hernia — the fatty hernia of linea alba in young fit males — pokes preperitoneal fat through transverse slits between xiphisternum and umbilicus and aches like a peptic ulcer; open or laparoscopic IPOM cures it. Umbilical hernia (big ring, everted umbilicus, newborns and cirrhotics, conservative to 2-3 years) contrasts with the paraumbilical (narrow, obese, Richter-prone, early hernioplasty)."),
    (S7, "Omphalocele herniates through the umbilicus under a peritoneal membrane (liver can follow), travels with Beckwith-Wiedemann and trisomies 13/18/21; gastroschisis splits beside the cord with naked bowel courting atresia, inflammation and perforation but fewer anomalies. Protect with a mesh SILO, creep the height down and internalize."),
    (S8, "Lumbar hernias: primary rare, secondary m/c after trauma or surgery; lipomas slip and pseudo-fluctuate, pseudo-hernias follow subcostal nerve injury. Petit's triangle (iliac crest, external oblique, latissimus dorsi) sits below Grynfeltt's (12th rib, internal oblique, sacrospinalis); Dowd-Ponka open or m/c laparoscopic mesh repairs. Spigelian — intraparietal along the rectus border, below the umbilicus above the arcuate line — strangulates readily."),
    (S9, "The little old lady's obturator hernia strangulates through the obturator canal — Howship-Romberg shooting pain with abduction/medial rotation and Hannington-Kiff's lost adductor with live patellar reflex. Richter's pinches one bowel wall through narrow rings (paraumbilical, femoral, obturator) masquerading as gastroenteritis until peritonitis; Maydl's W-shaped hernia kills the intraperitoneal connecting limb first — the part surgeons miss."),
    (S10, "Bochdalek (m/c, left postero-lateral, pleuroperitoneal membrane, stomach/spleen/colon) outnumbers Morgagni (right antero-medial, central tendon, transverse colon). Polyhydramnios at home, scaphoid abdomen and respiratory distress at birth; pulmonary hypoplasia and hypertension are the killers. CXR shows thoracic bowel; IPPV (never bag-mask), ECMO if refractory, inhaled nitrates for pulmonary hypertension, and diaphragmatic circumferential repair with mesh."),
    (S11, "Internal hernias hide inside: Stemmer's through transverse mesocolon, Petersen's behind the Roux limb, left paraduodenal through Landzert's fossa (descending colon fusion defect, behind the IMV) and right duodeno-jejunal behind the SMA from ascending colon fusion failure."),
    (S12, "Mesenteric cysts split chylolymphatic (m/c, thin, independent supply, clear, transilluminating, enucleate) from enterogenous (thick, bowel-shared supply, turbid, no transillumination, resect with anastomosis). The mesentery stretches DJ flexure to right sacroiliac joint, and Tillaux's triad — periumbilical swelling, right-angle movement (Tillaux sign) and transverse resonance band — is confirmed on CECT."),
]

first_page = {}
for x in Q:
    first_page.setdefault(x["sec"], x["page"])

UNITS = []
for i, (title, guide) in enumerate(UNIT_DEFS, 1):
    UNITS.append({
        "id": f"SURG-U60-{i}",
        "ch": 60,
        "n": i,
        "title": title,
        "sec": f"{title} · p{first_page[title]}",
        "qs": [x["id"] for x in Q if x["sec"] == title],
        "guide": guide,
    })

covered = [x for u in UNITS for x in u["qs"]]
assert covered == [x["id"] for x in Q]
assert len(set(covered)) == len(covered)
with open("data/ch60.json", "w", encoding="utf-8") as f:
    json.dump({"questions": Q, "units": UNITS}, f, ensure_ascii=False, indent=1)
print(f"ch60: {len(Q)} questions, {len(UNITS)} units")
