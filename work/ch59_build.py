#!/usr/bin/env python3
"""Build data/ch59.json — Hernia : Part 1 (Marrow Surgery Ed 8, pp451-459)."""
import json

Q = []

def q(page, sec, text, correct, wrongs, note=None):
    opts = [correct] + list(wrongs)
    assert len(opts) == 4
    Q.append({
        "id": f"SURG-C59-{len(Q)+1:03d}",
        "sec": sec,
        "page": page,
        "q": text,
        "opts": opts,
        "ans": 0,
        "exp": (note or correct) + f" (Book p{page})",
    })

# ------------------------------------------------------------------ p451
S1 = "Definition, Parts and Types of Hernia"
q(451, S1, "Definition of hernia:", "Protrusion of viscus or part of viscus through the wall containing it", ["Protrusion of fat through fascia", "Rupture of muscle", "Prolapse of organ through its opening"])
q(451, S1, "Parts of a hernia shown in the diagram:", "Sac, content, defect & blood supply", ["Sac, neck, body & tail", "Ring, cord, sac & fluid", "Neck, fundus, body & wall"])
q(451, S1, "UNCOMPLICATED hernia features:", "Reducible with cough impulse (+)", ["Irreducible, cough impulse (–)", "Skin inflamed", "Compromised blood supply"])
q(451, S1, "REDUCIBILITY differs from compressibility because it needs:", "Counter force to reproduce the swelling after pushing it down", ["No counterforce", "Only gravity", "Suction"])
q(451, S1, "COMPRESSIBILITY (no counterforce needed) is seen in:", "Vascular swellings / cystic hygromas", ["Hernias only", "Lipomas", "Neurofibromas"])
q(451, S1, "OBSTRUCTED hernia was previously known as:", "Incarcerated hernia", ["Strangulated hernia", "Reduced hernia", "Sliding hernia"])
q(451, S1, "Features of obstructed hernia:", "Irreducible, cough impulse (–) but INTACT blood supply", ["Compromised blood supply", "Inflamed skin", "Reducible"])
q(451, S1, "Dilatation of bowel proximal to a hernia occurs d/t:", "Obstruction", ["Ischemia", "Infection", "Adhesions alone"])
q(451, S1, "STRANGULATED hernia is defined as:", "Obstructed hernia + compromised blood supply", ["Irreducible hernia with intact supply", "Reducible hernia", "Hernia with hydrocele"])
q(451, S1, "Overlying skin in strangulated hernia is:", "Inflamed", ["Normal", "Cold", "Ulcerated"])
q(451, S1, "Golden rule of hernia emergencies:", "All obstructed hernias should be treated as strangulated unless proven otherwise", ["All strangulated are only obstructed", "Obstruction always spares blood supply", "Strangulation needs no surgery"])

# ------------------------------------------------------------------ p452
S2 = "Taxis, Reduction en Masse and Content-Based Types"
q(452, S2, "Taxis is:", "Process of reduction of hernia", ["Opening the sac", "Cutting the ring", "Strapping the swelling"])
q(452, S2, "Taxis is contraindicated in:", "Obstructed & strangulated hernia", ["Infantile hernia", "Femoral hernia only", "Reducible hernia"])
q(452, S2, "REDUCTION EN MASSE is:", "Reduction of contents + ring causing obstruction", ["Reduction with the sac", "Failure of taxis", "Surgical reduction"])
q(452, S2, "Zollinger classification VIII (combined type) hernia has:", "Direct + indirect portions", ["Two sacs side by side", "Femoral + obturator", "Sliding + strangulated"])
q(452, S2, "OMENTOCELE content and percussion:", "Omentum; dull note", ["Bowel; tympanic", "Bladder; dull", "Ovary; tympanic"])
q(452, S2, "ENTEROCELE shows peristalsis and bowel sounds:", "(+) and (+)", ["(–) and (–)", "(+) and (–)", "(–) and (+)"])
q(452, S2, "Consistency & reducibility of omentocele:", "Doughy consistency; easy to reduce 1st part", ["Tympanic; difficult", "Hard; irreducible", "Cystic; compressible"])
q(452, S2, "Reducibility of enterocele:", "Difficult to reduce 1st part but 2nd part easy", ["Easy 1st part", "Never reducible", "Reducible only lying down"])
q(452, S2, "Hernia containing bowel is named:", "Enterocele", ["Omentocele", "Cystocele", "Sarcocele"])
q(452, S2, "Hernia containing APPENDIX is called:", "Amyand's hernia", ["Littre's hernia", "Gibbon hernia", "Richter's hernia"])
q(452, S2, "Hernia containing MECKEL'S diverticulum is called:", "Littre's hernia", ["Amyand's hernia", "Pantaloon hernia", "Sliding hernia"])

# ------------------------------------------------------------------ p452-453
S3 = "Basics of Hernia Surgery: Herniotomy, Herniorrhaphy, Hernioplasty"
q(452, S3, "The three basic hernia operations:", "Herniotomy, herniorrhaphy & hernioplasty", ["Herniotomy, taxis & plasty", "Rhaphy, pexy & tomy", "Open, lap & mesh"])
q(452, S3, "Herniotomy step 1 — the sac is identified as:", "Glistening white", ["Grey & dull", "Yellow lobulated", "Dark red"])
q(452, S3, "Herniotomy steps after opening the sac:", "Push contents down, cut the excess sac & close the sac", ["Excise cord structures", "Repair the defect", "Place mesh"])
q(452, S3, "Herniotomy leaves the defect:", "Intact", ["Closed", "Reinforced", "Duplicated"])
q(453, S3, "Disadvantage of herniotomy:", "Highest recurrence rate", ["Highest infection", "Longest surgery", "Needs mesh"])
q(453, S3, "Herniotomy is the surgery of choice in:", "Congenital inguinal hernia, congenital hydrocele & inguinal hernia in children", ["Adult direct hernia", "Femoral hernia", "Incisional hernia"])
q(453, S3, "Why does herniotomy NOT recur in children?", "High muscle tone spontaneously blocks the defect", ["Mesh prevents it", "Sac regrows", "Ring ossifies"])
q(453, S3, "HERNIORRHAPHY is:", "Suturing two edges of the defect together", ["Mesh coverage", "Sac excision only", "Laparoscopic repair"])
q(453, S3, "Indications of herniorrhaphy:", "Infected & strangulated hernias (synthetic mesh cannot be used)", ["All primary hernias", "Only pediatric", "Only femoral"])
q(453, S3, "HERNIOPLASTY is:", "Mesh placed to cover the defect", ["Suture repair", "Sac removal", "Taxis under anesthesia"])
q(453, S3, "Hernioplasty is:", "Surgery of choice with LEAST recurrence rate", ["Highest recurrence", "Reserved for children", "C/I in clean cases"])
q(453, S3, "Contraindication of hernioplasty:", "Infected hernias", ["Femoral hernia", "Recurrent hernia", "Elderly patients"])

# ------------------------------------------------------------------ p453-454
S4 = "Types and Materials of Mesh"
q(453, S4, "The two families of hernia mesh:", "Synthetic & biological", ["Absorbable & permanent only", "Metal & plastic", "Flat & plug only"])
q(453, S4, "Synthetic mesh is contraindicated in:", "Infection / strangulation", ["Obesity", "Children", "Recurrence"])
q(453, S4, "Biological mesh can be used:", "When infection (+)", ["Never in infection", "Only in children", "Only laparoscopically"])
q(453, S4, "Examples of SYNTHETIC mesh:", "Prolene, Vipro (Vicryl + Prolene) & PTFE", ["Alloderm & porcine dermis", "SIS only", "Permacol only"])
q(453, S4, "Which synthetic mesh can be placed in the intraperitoneal space (no adherence)?", "PTFE (polytetrafluoroethylene)", ["Prolene", "Polyester", "Vipro"])
q(453, S4, "Examples of BIOLOGICAL mesh:", "Acellular human dermis (Alloderm) & acellular porcine dermis", ["Prolene & PTFE", "Vipro & Dacron", "Polyglactin only"])
q(453, S4, "Fibrous ingrowth in fenestrated mesh:", "Occurs through the holes and anchors the mesh in place", ["Weakens the mesh", "Causes meshoma", "Blocks the pores"])
q(453, S4, "Preferred pore size of fenestrated mesh:", "Larger pores (strong fibrous pillars)", ["Smallest pores", "No pores", "Micro pores"])
q(454, S4, "Prolene mesh property:", "Hydrophobic → less bacterial contamination", ["Hydrophilic → faster ingrowth", "Adheres to bowel", "Absorbable"])
q(454, S4, "Polyester mesh property:", "Hydrophilic → faster cellular ingrowth", ["Hydrophobic", "Anti-bacterial", "Intraperitoneal safe"])
q(454, S4, "PTFE mesh special property:", "Does not adhere to bowel inside the peritoneal cavity", ["Fastest ingrowth", "Strongest", "Cheapest"])
q(454, S4, "Ideal mesh OVERLAP beyond the defect:", "5 cm in all directions (prevents recurrence when mesh shrinks)", ["1 cm", "10 cm", "No overlap"])
q(454, S4, "LOW weight mesh is:", "<40 gm/m² — less shrinkage", [">80 gm/m²", "=100 gm/m²", "40-80 gm/m²"])
q(454, S4, "HIGH weight mesh is:", ">80 gm/m² — more shrinkage", ["<40 gm/m²", "50-60 gm/m²", "Always better"])
q(454, S4, "Properties of the IDEAL hernia mesh:", "Low weight, thin fibers & large pores", ["High weight, thick fibers, small pores", "Heavy & dense", "Thin fibers, small pores"])
q(454, S4, "Complication of PLUG mesh:", "Meshoma d/t excessive collagen deposition", ["Fistula", "Herniation", "Hydrocele"])
q(454, S4, "Meshoma leads to pain d/t:", "Nerve entrapment", ["Infection", "Ischemia", "Seroma"])

# ------------------------------------------------------------------ p454
S5 = "Inguinal Hernia and Anatomy"
q(454, S5, "The m/c hernia overall:", "Inguinal hernia", ["Femoral", "Umbilical", "Incisional"])
q(454, S5, "The m/c hernia in BOTH males & females:", "Indirect inguinal hernia", ["Direct inguinal", "Femoral", "Obturator"])
q(454, S5, "INTERNAL inguinal ring is a modification of:", "Fascia transversalis", ["External oblique aponeurosis", "Internal oblique", "Conjoint tendon"])
q(454, S5, "EXTERNAL inguinal ring is a modification of:", "External oblique aponeurosis", ["Fascia transversalis", "Transversus abdominis", "Inguinal ligament"])
q(454, S5, "DIRECT hernia passes:", "Through Hesselbach's triangle", ["Through deep ring lateral to the triangle", "Femoral canal", "Obturator canal"])
q(454, S5, "INDIRECT hernia passes:", "Lateral to Hesselbach's triangle, through the deep inguinal ring", ["Through the triangle", "Below the inguinal ligament", "Through the lacunar ligament"])
q(454, S5, "Boundaries of HESSELBACH's triangle (as drawn):", "Inferior epigastric vessels, inguinal ligament & outer border of rectus", ["Vas deferens & testicular vessels", "Cooper's ligament & iliopsoas", "Rectus & linea alba only"])

# ------------------------------------------------------------------ p455
S6 = "Myopectineal Orifice of Fruchaud"
q(455, S6, "SUPERIOR boundary of myopectineal orifice:", "Arching fibers of internal oblique", ["Cooper's ligament", "Tendon of iliopsoas", "Outer border of rectus"])
q(455, S6, "MEDIAL boundary of myopectineal orifice:", "Outer border of rectus", ["Internal oblique fibers", "Iliopsoas tendon", "Lacunar ligament"])
q(455, S6, "LATERAL boundary of myopectineal orifice:", "Tendon of iliopsoas", ["Rectus border", "Cooper's ligament", "Internal oblique"])
q(455, S6, "INFERIOR boundary of myopectineal orifice:", "Pectineal / Cooper's ligament", ["Inguinal ligament only", "Iliopsoas", "Pubic tubercle"])
q(455, S6, "Myopectineal orifice covers the defects of:", "Inguinal, femoral & obturator hernias", ["Umbilical & epigastric", "Lumbar & Spigelian", "Incisional hernias"])

# ------------------------------------------------------------------ p455-456
S7 = "Clinical Examination, Degrees and Tests"
q(455, S7, "Hernia is examined in the position:", "Standing & lying down", ["Only supine", "Only lateral", "Sitting"])
q(455, S7, "Standing vs lying examination helps differentiate:", "Inguinal (above & medial to pubic tubercle) vs femoral (below & lateral)", ["Direct vs sliding", "Obstructed vs strangulated", "Congenital vs acquired"])
q(455, S7, "INGUINAL hernia lies in relation to the pubic tubercle:", "Above & medial", ["Below & lateral", "Above & lateral", "Below & medial"])
q(455, S7, "FEMORAL hernia lies in relation to the pubic tubercle:", "Below & lateral", ["Above & medial", "Above & lateral", "Below & medial"])
q(455, S7, "Other goals of examination (besides differentiation):", "Appreciate cough impulse, assess abdominal muscle tone & complete vs incomplete hernia", ["Only measure size", "Only auscultate", "Biopsy the sac"])
q(455, S7, "Sac that does NOT cross the superficial ring:", "Bubonocele", ["Funicular", "Inguinoscrotal", "Complete"])
q(455, S7, "Sac that JUST crosses the superficial ring:", "Funicular", ["Bubonocele", "Complete", "Sliding"])
q(455, S7, "Sac that crosses the superficial ring & reaches the scrotum:", "Inguinoscrotal / complete", ["Bubonocele", "Funicular", "Infantile"])
q(455, S7, "The SINGLE BEST clinical test for hernia:", "Deep ring occlusion test", ["Ring invagination", "Zieman 3 finger test", "Cough impulse only"])
q(455, S7, "Ring invagination test — little finger in the superficial ring through the scrotum: TIP of finger touches:", "Indirect hernia", ["Direct hernia", "Femoral hernia", "Hydrocele"])
q(455, S7, "Ring invagination test — PULP of finger touches:", "Direct hernia", ["Indirect hernia", "Obturator hernia", "Varicocele"])
q(455, S7, "Sensitivity of ring invagination test:", "Low", ["High", "100%", "Moderate"])
q(456, S7, "Zieman 3 finger test:", "1 finger each at superficial, deep & femoral ring; the respective finger lifts when patient coughs", ["Only tests the deep ring", "Palpates the spermatic cord", "Measures the defect size"])
q(456, S7, "Sensitivity of Zieman 3 finger test:", "Low", ["High", "Best single test", "Diagnostic"])
q(456, S7, "Indications for USG in hernia:", "Doubtful diagnosis & non-palpable hernia", ["All hernias", "Only strangulation", "Only post-op"])

# ------------------------------------------------------------------ p456
S8 = "Management of Inguinal Hernia: Open Surgery"
q(456, S8, "The m/c surgical approach for inguinal hernia:", "Laparoscopic inguinal hernia surgery", ["Open surgery", "Taxis", "Truss"])
q(456, S8, "Open surgery options:", "Herniotomy, herniorrhaphy & Lichtenstein's tension free mesh hernioplasty", ["Only mesh", "Only Bassini", "Stoppa only"])
q(456, S8, "BASSINI repair:", "Reflected portion of inguinal ligament sutured with conjoint tendon", ["Double breasting of fascia transversalis", "Mesh plug", "Pre-peritoneal mesh"])
q(456, S8, "SHOULDICE repair — 1st layer:", "Double breasting of fascia transversalis", ["Inguinal ligament", "External oblique", "Conjoint tendon alone"])
q(456, S8, "SHOULDICE repair — 2nd layer:", "Double breasting of inguinal ligament with conjoint tendon (corresponds to Bassini)", ["Fascia transversalis", "External oblique", "Mesh fixation"])
q(456, S8, "SHOULDICE repair — 3rd layer:", "Double breasting of external oblique aponeurosis", ["Fascia transversalis", "Cooper's ligament", "Transversalis fascia"])
q(456, S8, "Shouldice repair is also called:", "3/6 layer repair", ["4/7 layer repair", "Single layer", "Mesh repair"])
q(456, S8, "M/c NERVE INJURED in open inguinal surgery:", "Ilioinguinal nerve", ["Iliohypogastric", "Genitofemoral", "Lateral cutaneous nerve of thigh"])
q(456, S8, "M/c nerve ENTRAPPED in open inguinal surgery:", "Iliohypogastric nerve", ["Ilioinguinal", "Femoral", "Obturator"])
q(456, S8, "Chronic inguinal pain after open surgery is d/t:", "Nerve entrapment beneath mesh / pubis osteitis", ["Recurrence always", "Seroma", "Hydrocele"])
q(456, S8, "Recurrence is LEAST (<2%) with:", "Hernioplasty", ["Herniotomy", "Bassini", "Shouldice"])

# ------------------------------------------------------------------ p457
S9 = "Laparoscopic Inguinal Hernia Surgery (TEP / TAPP) and Stoppa's"
q(457, S9, "Indications for laparoscopic inguinal hernia surgery:", "Can be done in all hernias, B/L inguinal hernia & recurrent inguinal hernia", ["Only children", "Only unilateral", "Strangulation only"])
q(457, S9, "In TEP, the peritoneum:", "Remains intact", ["Is breached", "Is excised", "Is duplicated"])
q(457, S9, "In TAPP, the peritoneum:", "Is breached", ["Remains intact", "Is never touched", "Is sutured to mesh"])
q(457, S9, "Space created in TEP:", "Extraperitoneal space", ["Pre-peritoneal only after breach", "Intraperitoneal", "Subcutaneous"])
q(457, S9, "Space created in TAPP:", "Pre-peritoneal space", ["Extraperitoneal only", "Retrorectus only", "Subfascial"])
q(457, S9, "TEP advantage over TAPP:", "Technically better", ["Easier to learn", "Faster always", "No mesh needed"])
q(457, S9, "TAPP advantage over TEP:", "Less technically demanding", ["Better cosmesis", "Peritoneum intact", "Higher recurrence"])
q(457, S9, "TEP disadvantage:", "More demanding, requires high precision", ["Bowel injury guaranteed", "Cannot use mesh", "Needs open conversion always"])
q(457, S9, "STOPPA'S repair:", "Open pre-peritoneal repair; mesh held in place d/t Pascal's law; used in recurrent inguinal hernia", ["Laparoscopic repair", "Suture only repair", "Plug repair"])

# ------------------------------------------------------------------ p457-458
S10 = "Triangle of Doom & Pain; Corona Mortis"
q(457, S10, "Triangle of DOOM boundaries: MEDIAL and LATERAL:", "Vas deferens (medial) & testicular vessels (lateral)", ["Testicular vessels medial", "Peritoneal reflection lateral", "Iliopubic tract inferior"])
q(458, S10, "Triangle of doom INFERIOR boundary:", "Peritoneal reflection", ["Iliopubic tract", "Cooper's ligament", "Vas deferens"])
q(458, S10, "Contents of triangle of doom:", "External iliac artery, external iliac vein & genital branch of genitofemoral nerve", ["Femoral nerve & lateral cutaneous nerve", "Testicular vessels only", "Obturator nerve"])
q(458, S10, "Complication of stapling in triangle of doom:", "Bleeding", ["Nerve pain", "Ischemic orchitis", "Recurrence"])
q(458, S10, "Triangle of PAIN boundaries:", "Medial testicular vessels, lateral peritoneal reflection & superior iliopubic tract", ["Vas deferens medial", "Inferior peritoneal reflection", "Inguinal ligament only"])
q(458, S10, "Contents of triangle of pain:", "Lateral cutaneous nerve of thigh, femoral nerve & femoral branch of genitofemoral nerve", ["External iliac vessels", "Vas deferens", "Inferior epigastrics"])
q(458, S10, "Meralgia paresthetica after laparoscopic hernia surgery:", "Shooting pain along lateral aspect of thigh d/t entrapment of lateral cutaneous nerve of thigh (m/c)", ["Femoral nerve injury", "Vas injury", "Medial thigh pain"])
q(458, S10, "Why NO cautery in triangle of pain?", "Electrical hazard zone — to prevent thermal injury to nerves", ["Bleeding risk", "Mesh melts", "Causes recurrence"])
q(458, S10, "TRAPEZOID of disaster consists of:", "Triangle of doom (medial) + triangle of pain (lateral)", ["Two triangles lateral only", "Doom + Hesselbach", "Pain + triangle of Petit"])
q(458, S10, "CORONA MORTIS / circle of death connects:", "Inferior epigastric artery (branch of external iliac) with obturator artery (branch of internal iliac) via aberrant obturator artery", ["Femoral & profunda", "Iliolumbar & lateral sacral", "Inferior epigastric & femoral directly"])
q(458, S10, "The aberrant obturator artery of corona mortis lies:", "Behind the pubic tubercle", ["Above the umbilicus", "In the scrotal wall", "Lateral to ASIS"])
q(458, S10, "Injury to corona mortis causes:", "Torrential bleeding", ["Nothing", "Ischemic orchitis", "Nerve palsy"])

# ------------------------------------------------------------------ p458-459
S11 = "Classifications of Inguinal Hernia (EHS & Nyhus)"
q(458, S11, "EHS classification uses location codes:", "L (lateral/indirect), M (medial/direct) & F (femoral)", ["I, II, III, IV", "A, B, C, D", "1, 2, 3 only"])
q(458, S11, "In EHS, the size code counts:", "Fingerbreadths (FB): 0 no hernia, 1 one FB, 2 two FB, 3 >2 FB, X not investigated", ["Centimeters", "Grades I-IV", "Weight of content"])
q(458, S11, "EHS example: lateral hernia of 2 FB (primary or recurrent):", "L2", ["L3", "M2", "L-X"])
q(458, S11, "EHS example: femoral hernia not investigated for FB:", "F-X", ["F3", "F0", "M-X"])
q(459, S11, "NYHUS Type I:", "Indirect inguinal hernia with a normal ring; sac in the canal", ["Indirect with enlarged ring", "Direct hernia", "Femoral hernia"])
q(459, S11, "NYHUS Type II:", "Indirect hernia with enlarged internal ring but posterior wall intact; inferior deep epigastric vessels not displaced; sac not in scrotum", ["Direct posterior floor defect", "Sac in scrotum", "Femoral"])
q(459, S11, "NYHUS Type 3a:", "Direct hernia with a posterior floor defect only", ["Indirect enlarged ring", "Femoral", "Recurrent"])
q(459, S11, "NYHUS Type 3b:", "Indirect hernia with enlargement of internal ring AND posterior floor defect", ["Direct only", "Femoral only", "Recurrent indirect"])
q(459, S11, "NYHUS Type 3c:", "Femoral hernia", ["Direct", "Indirect", "Sliding"])
q(459, S11, "NYHUS Type 4 subtypes:", "Recurrent hernia — A direct, B indirect, C femoral, D combinations of A-B-C", ["Sliding types", "Congenital types", "Femoral variants"])

# ------------------------------------------------------------------ p459
S12 = "Special Types of Inguinal Hernia"
q(459, S12, "GIBBON hernia:", "Inguinal hernia + hydrocele", ["Direct + indirect", "Hernia + varicocele", "Bilateral inguinal"])
q(459, S12, "PANTALOON hernia:", "Direct + indirect components (m/c in elderly patients)", ["Bilateral direct", "Sliding sigmoid", "Femoral + obturator"])
q(459, S12, "SLIDING hernia is also called:", "Hernia en glissade", ["Gilmore's groin", "Maydl's hernia", "Richter's hernia"])
q(459, S12, "Sliding hernia is common in:", "Elderly males", ["Children", "Females", "Neonates"])
q(459, S12, "POSTERIOR boundary of the sac in sliding hernia:", "A visceral structure (can be injured during surgery)", ["Only omentum", "Peritoneal fold", "Fascia transversalis"])
q(459, S12, "Side predominance of sliding hernia:", "Left > Right", ["Right > Left", "Equal", "Always bilateral"])
q(459, S12, "M/c structure in a sliding hernia:", "Sigmoid colon > bladder", ["Cecum > appendix", "Ovary", "Small bowel"])
q(459, S12, "SPORTSMAN hernia is also called:", "Gilmore's groin", ["Hernia en glissade", "Gibbon hernia", "Bubonocele"])
q(459, S12, "Sportsman hernia is m/c seen in:", "Athletes", ["Elderly females", "Infants", "Couch workers"])
q(459, S12, "Sportsman hernia mechanism:", "Tear in posterior wall muscle → pain", ["Ring dilatation", "Sac sliding", "Nerve entrapment only"])
q(459, S12, "Sac in sportsman hernia on examination:", "Not palpable (extremely small)", ["Large & scrotal", "Always strangulated", "Cystic"])
q(459, S12, "IOC for sportsman hernia:", "MRI", ["USG", "CT", "Herniography"])
q(459, S12, "Mx of sportsman hernia:", "Laparoscopic repair using mesh", ["Taxis", "Truss", "Open suture only"])
q(459, S12, "During sliding hernia surgery, the neck of the sac is NEVER opened because:", "Sudden reduction of contents converts localized hernia to generalized", ["It bleeds torrentially", "Recurrence increases", "Nerve injury"])

# ------------------------------------------------------------------ units
UNIT_DEFS = [
    (S1, "A hernia pushes viscus through the wall containing it, carrying sac, content, defect and blood supply. Reducible with a positive cough impulse is uncomplicated; obstruction (old 'incarceration') keeps the supply intact while strangulation adds compromised blood supply and inflamed skin — and every obstruction is treated as strangulation until proven otherwise."),
    (S2, "Taxis reduces a hernia — banned in obstruction/strangulation because contents can slip back en masse along with the obstructing ring. Omentocele is doughy and dull with no peristalsis; enterocele is tympanic, peristalsing and harder to reduce first. Bowel = enterocele, appendix = Amyand's, Meckel's = Littre's, and Zollinger VIII combines direct with indirect sacs."),
    (S3, "Herniotomy finds the glistening-white sac, empties it, trims and closes it — defect left untouched, so recurrence is highest, but it is the operation for congenital hernia/hydrocele and children whose high muscle tone blocks the defect. Herniorrhaphy sutures the edges together where mesh is forbidden (infected/strangulated); hernioplasty covers the defect with mesh — the surgery of choice with the least recurrence, avoiding infected fields."),
    (S4, "Synthetic mesh (Prolene, Vipro, PTFE) shuns infection and strangulation; biological (Alloderm, porcine dermis) works in its presence. Prolene repels bacteria (hydrophobic), polyester ingrows fastest (hydrophilic), PTFE spares the bowel intraperitoneally. Cover 5 cm beyond the defect; prefer low weight (<40 g/m²), thin fibers, large pores — and beware the plug's collagenous meshoma entrapping nerves."),
    (S5, "Inguinal hernia is the commonest hernia overall and the indirect type leads in both sexes. The deep ring is fascia transversalis fashion, the superficial external oblique; direct hernias vault through Hesselbach's triangle while indirects enter through the deep ring lateral to it."),
    (S6, "Fruchaud's myopectineal orifice — superior arching internal oblique, medial rectus border, lateral iliopsoas tendon, inferior Cooper's ligament — is the single gate through which inguinal, femoral and obturator hernias pass."),
    (S7, "Examine standing and lying: inguinal swellings sit above-medial to the pubic tubercle, femoral below-lateral; note cough impulse, tone and whether the sac stops at the ring (bubonocele), just crosses (funicular) or reaches the scrotum (inguinoscrotal/complete). Deep ring occlusion is the single best test; ring invagination (tip = indirect, pulp = direct) and Zieman's three fingers are low-sensitivity; USG answers doubt and non-palpable lumps."),
    (S8, "Open surgery spans herniotomy, herniorrhaphy (Bassini: reflected inguinal ligament to conjoint tendon; Shouldice 3/6 layers — transversalis double-breasting, then ligament-plus-conjoint matching Bassini, then external oblique) and Lichtenstein tension-free mesh. Watch the ilioinguinal nerve (m/c injury), iliohypogastric (m/c entrapment), chronic pain from meshed nerves or pubic osteitis, and recurrence <2% with hernioplasty."),
    (S9, "Laparoscopy suits all hernias, bilateral and recurrent ones. TEP keeps peritoneum intact creating an extraperitoneal space — technically better but precision-hungry; TAPP breaches peritoneum into the pre-peritoneal plane and is less demanding. Stoppa's open pre-peritoneal giant mesh leans on Pascal's law for recurrent hernias."),
    (S10, "Laparoscopic anatomy is a minefield: doom (vas medially, testicular vessels laterally, peritoneal reflection below) hides external iliac vessels and the genital branch — staple and it bleeds; pain (testicular vessels medial, peritoneal reflection lateral, iliopubic tract above) carries the lateral femoral cutaneous, femoral and femoral-genitofemoral branches — no cautery, or meralgia paresthetica. Doom + pain = trapezoid of disaster; the corona mortis (aberrant obturator behind the pubic tubercle joining external-iliac epigastric to internal-iliac obturator) bleeds torrentially."),
    (S11, "EHS codes site (L/M/F) by fingerbreadths (0/1/2/3/X) — an L2 is a two-FB indirect; F-X means uninvestigated femoral. Nyhus climbs from Type I (normal ring indirect) through II (enlarged ring, intact floor), IIIa direct floor defect, IIIb indirect ring-plus-floor, IIIc femoral, to Type IV recurrent (A/B/C/D)."),
    (S12, "Special inguinal hernias: Gibbon (with hydrocele), pantaloon (direct + indirect, elderly), sliding en glissade — elderly males, left > right, sigmoid colon > bladder forming the sac's posterior wall, so never open the neck lest contents scatter — and sportsman's Gilmore's groin of athletes: posterior wall tear, invisible sac, MRI IOC, laparoscopic mesh repair."),
]

first_page = {}
for x in Q:
    first_page.setdefault(x["sec"], x["page"])

UNITS = []
for i, (title, guide) in enumerate(UNIT_DEFS, 1):
    UNITS.append({
        "id": f"SURG-U59-{i}",
        "ch": 59,
        "n": i,
        "title": title,
        "sec": f"{title} · p{first_page[title]}",
        "qs": [x["id"] for x in Q if x["sec"] == title],
        "guide": guide,
    })

covered = [x for u in UNITS for x in u["qs"]]
assert covered == [x["id"] for x in Q]
assert len(set(covered)) == len(covered)
with open("data/ch59.json", "w", encoding="utf-8") as f:
    json.dump({"questions": Q, "units": UNITS}, f, ensure_ascii=False, indent=1)
print(f"ch59: {len(Q)} questions, {len(UNITS)} units")
