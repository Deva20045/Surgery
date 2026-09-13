#!/usr/bin/env python3
"""Build data/ch1.json for PULSE Surgery ch1 (Patient Safety, OT Zones and Surgery Positions, book p1-5)."""
import json

Q = []
def q(page, sec, text, opts, ans, exp):
    Q.append({"id": f"SURG-C1-{len(Q)+1:03d}", "sec": sec, "page": page,
              "q": text, "opts": opts, "ans": ans, "exp": exp})

# ---------------- p1 · CONSENTS ----------------
q(1, "Consents", "As per the book, consent before a procedure must contain all of the following components EXCEPT:",
  ["Identification and diagnosis", "Description of the procedure", "Patient-specific and procedure-specific complications", "Blood group and routine labs"], 3,
  "Components of consent = identification, diagnosis, planned procedure, surgeon, description, patient-specific complications, procedure-specific complications, benefits, alternate procedure and sign of patient, surgeon and witness. (Book p1)")
q(1, "Consents", "Which of the following is an explicit component of consent?",
  ["The surgeon performing the procedure", "Hospital bed number", "Anaesthetic equipment list", "Insurance details"], 0,
  "The planned procedure and the surgeon are explicit components of consent. (Book p1)")
q(1, "Consents", "A procedure-specific complication must be explained to the patient when its incidence is:",
  ["Greater than 1%", "Greater than 5%", "Greater than 10%", "Greater than 20%"], 0,
  "Procedure specific complications = any complication > 1% incidence. (Book p1)")
q(1, "Consents", "In addition to the planned procedure, consent must also discuss:",
  ["Benefits and alternate procedure", "Hospital charges only", "Ward amenities", "Visiting timings"], 0,
  "Consent includes benefits and the alternate procedure. (Book p1)")
q(1, "Consents", "The consent form is signed by:",
  ["Patient, surgeon and witness", "Only the patient", "Only the surgeon", "Nurse and anaesthetist"], 0,
  "Consent requires the sign of patient, surgeon and witness. (Book p1)")

# ---------------- p1 · IV LINES ----------------
q(1, "IV Lines", "In the color-coding of IV cannulas, the YELLOW cannula corresponds to gauge:",
  ["24G", "22G", "20G", "18G"], 0,
  "Yellow = 24G (max flow 13 (10) ml/min), the narrowest cannula in the chart. (Book p1)")
q(1, "IV Lines", "The BLUE IV cannula corresponds to gauge:",
  ["24G", "22G", "20G", "14G"], 1,
  "Blue = 22G with a maximal flow of 31 (30) ml/min. (Book p1)")
q(1, "IV Lines", "The PINK IV cannula corresponds to gauge:",
  ["20G", "24G", "16G", "14G"], 0,
  "Pink = 20G with a maximal flow of 67 (60) ml/min. (Book p1)")
q(1, "IV Lines", "The GREEN IV cannula corresponds to gauge:",
  ["18G", "16G", "14G", "20G"], 0,
  "Green = 18G with a maximal flow of 96 ml/min. (Book p1)")
q(1, "IV Lines", "The GRAY IV cannula corresponds to gauge:",
  ["16G", "18G", "14G", "24G"], 0,
  "Gray = 16G with a maximal flow of 236 (240 ml/min). (Book p1)")
q(1, "IV Lines", "The ORANGE IV cannula, which is used in shock, corresponds to gauge:",
  ["14G", "16G", "18G", "22G"], 0,
  "Orange (used in shock) = 14G, the widest cannula, with a maximal flow of 270 ml/min. (Book p1)")
q(1, "IV Lines", "The narrowest cannula in the color chart is:",
  ["24G yellow", "16G gray", "18G green", "14G orange"], 0,
  "The chart runs from narrow 24G (yellow) to wide 14G (orange). (Book p1)")
q(1, "IV Lines", "The widest cannula in the color chart is:",
  ["14G orange", "16G gray", "20G pink", "22G blue"], 0,
  "14G orange is the widest cannula and is the one used in shock. (Book p1)")
q(1, "IV Lines", "The maximal flow rate of the 16G gray cannula is:",
  ["236 (240 ml/min)", "96 ml/min", "67 (60) ml/min", "270 ml/min"], 0,
  "Gray 16G maximal flow = 236 (240 ml/min). (Book p1)")
q(1, "IV Lines", "The maximal flow rate of the 20G pink cannula is:",
  ["67 (60) ml/min", "31 (30) ml/min", "13 (10) ml/min", "236 (240) ml/min"], 0,
  "Pink 20G maximal flow = 67 (60) ml/min. (Book p1)")
q(1, "IV Lines", "The maximal flow rate of the 14G orange cannula is:",
  ["270 ml/min", "236 (240) ml/min", "96 ml/min", "67 (60) ml/min"], 0,
  "Orange 14G (used in shock) has the highest maximal flow of 270 ml/min. (Book p1)")
q(1, "IV Lines", "In the color chart, which group of cannulas is bracketed for paediatric patients?",
  ["Yellow, blue and pink (24G, 22G, 20G)", "Green, gray and orange", "16G and 14G only", "All gauges"], 0,
  "Yellow (24G), blue (22G) and pink (20G) are grouped together for paediatric patients. (Book p1)")
q(1, "IV Lines", "A cannula with a maximal flow of 96 ml/min is color-coded:",
  ["Green (18G)", "Blue (22G)", "Yellow (24G)", "Gray (16G)"], 0,
  "Green = 18G with maximal flow 96 ml/min. (Book p1)")

# ---------------- p1 · IV LINES: COMPLICATIONS ----------------
q(1, "IV Lines: Complications", "The most common complication of an IV line is:",
  ["Superficial thrombophlebitis", "Infiltration", "Nerve injury", "Arterial puncture"], 0,
  "Superficial thrombophlebitis is the m/c complication of IV lines. (Book p1)")
q(1, "IV Lines: Complications", "Superficial thrombophlebitis at a cannulation site presents with:",
  ["Tender, cord-like swelling", "Painless soft swelling", "Bruising only", "Systemic fever only"], 0,
  "Features of superficial thrombophlebitis: tender, cord-like swelling. (Book p1)")
q(1, "IV Lines: Complications", "The management of superficial thrombophlebitis at a cannula site is:",
  ["Topical heparinoid", "Systemic antibiotics", "Emergent thrombectomy", "Compression bandage only"], 0,
  "Management of superficial thrombophlebitis = topical heparinoid. (Book p1)")

# ---------------- p2 · SURGICAL SAFETY CHECKLIST ----------------
q(2, "Surgical Safety Checklist", "The three phases of the surgical safety checklist, in order, are:",
  ["Sign in → Time out → Sign out", "Time out → Sign in → Sign out", "Sign out → Sign in → Time out", "Sign in → Sign out → Time out"], 0,
  "The checklist flows Before induction of anaesthesia (sign in) → Before skin incision (time out) → Before patient leaves the operating room (sign out). (Book p2)")
q(2, "Surgical Safety Checklist", "'Before induction of anaesthesia' (ward to OT complex) corresponds to which phase?",
  ["Sign in", "Time out", "Sign out", "Handover"], 0,
  "Sign in happens before induction of anaesthesia, in the ward to OT complex. (Book p2)")
q(2, "Surgical Safety Checklist", "'Before skin incision' corresponds to which phase?",
  ["Time out", "Sign in", "Sign out", "Check back"], 0,
  "Time out is performed before skin incision. (Book p2)")
q(2, "Surgical Safety Checklist", "'Before patient leaves the operating room' corresponds to which phase?",
  ["Sign out", "Sign in", "Time out", "Handover"], 0,
  "Sign out is completed before the patient leaves the operating room. (Book p2)")
q(2, "Surgical Safety Checklist", "During sign in, the patient has confirmed all of the following EXCEPT:",
  ["Identity", "Marked site", "Procedure and written consent", "Fasting status"], 3,
  "At sign in the patient has confirmed identity, site (marked), procedure and written consent. (Book p2)")
q(2, "Surgical Safety Checklist", "Which of the following is checked during sign in?",
  ["Known allergies", "Specimen labelling", "Actual blood loss", "Antibiotic prophylaxis"], 0,
  "Sign in includes known allergies and the risk of >500 ml blood loss. (Book p2)")
q(2, "Surgical Safety Checklist", "During sign in, the risk of blood loss greater than how much is assessed?",
  [">500 ml", ">200 ml", ">1000 ml", ">100 ml"], 0,
  "Sign in assesses the risk of >500 ml blood loss. (Book p2)")
q(2, "Surgical Safety Checklist", "During time out, the team confirms:",
  ["Patient site, procedure name and time", "Allergies and consent", "Specimen label", "Sponge count"], 0,
  "Time out confirms patient site, procedure name and time. (Book p2)")
q(2, "Surgical Safety Checklist", "At time out, antibiotic prophylaxis must have been given within the last:",
  ["30 minutes", "10 minutes", "60 minutes", "2 hours"], 0,
  "Time out checks that antibiotic prophylaxis was given within the last 30 min. (Book p2)")
q(2, "Surgical Safety Checklist", "During time out, the anticipated blood loss is estimated by the:",
  ["Surgeon", "Anaesthetist", "Nurse", "Scrub technician"], 0,
  "Anticipated blood loss at time out is given by the surgeon (actual loss at sign out is by the anaesthetist). (Book p2)")
q(2, "Surgical Safety Checklist", "During sign out, which of the following is verified?",
  ["Instruments, sponge and needle count", "Written consent", "Patient identity", "Fasting status"], 0,
  "Sign out verifies instruments, sponge and needle count. (Book p2)")
q(2, "Surgical Safety Checklist", "Specimen labelling during sign out must include:",
  ["Patient name", "Only the specimen number", "Hospital code", "Ward number"], 0,
  "Sign out includes specimen labelling (including patient name). (Book p2)")
q(2, "Surgical Safety Checklist", "During sign out, the actual blood loss is documented by the:",
  ["Anaesthetist", "Surgeon", "Nurse", "Lab technician"], 0,
  "Actual blood loss at sign out is recorded by the anaesthetist. (Book p2)")
q(2, "Surgical Safety Checklist", "The note on the surgical safety checklist states that:",
  ["There is no time in phase", "Time out lasts exactly 5 minutes", "Sign in takes 30 minutes", "Sign out is optional"], 0,
  "The book's note: 'There is no time in phase' — time out is a pause in workflow, not a timed interval. (Book p2)")

# ---------------- p2 · ESTIMATING BLOOD LOSS ----------------
q(2, "Estimating Blood Loss", "The actual amount of blood loss is estimated as:",
  ["Blood in suction − irrigation fluid", "Blood in suction + irrigation fluid", "Dry mop weight − wet mop weight", "Sponge count × 50 cc"], 0,
  "Actual amount = blood in suction − irrigation fluid. (Book p2)")
q(2, "Estimating Blood Loss", "Alternatively, blood loss is estimated as:",
  ["Wet mop weight − dry mop weight", "Wet mop weight + dry mop weight", "Dry mop weight − wet mop weight", "Irrigation fluid − suction"], 0,
  "Blood loss can also be estimated as wet mop weight − dry mop weight. (Book p2)")
q(2, "Estimating Blood Loss", "A soaked mop represents a blood loss of:",
  ["100 cc", "500 cc", "200 cc", "1000 cc"], 0,
  "Soaked mop = 100 cc of blood. (Book p2)")
q(2, "Estimating Blood Loss", "A fist full of clots represents a blood loss of:",
  ["500 cc", "100 cc", "250 cc", "1000 cc"], 0,
  "Fist full of clots = 500 cc of blood. (Book p2)")
q(2, "Estimating Blood Loss", "Surgical mops carry a radio-opaque line so that they can be:",
  ["Picked up on X-ray", "Weighed more easily", "Sterilized faster", "Identified by color"], 0,
  "Mops have a radio-opaque line that is picked up on X-ray. (Book p2)")

# ---------------- p2 · OT ZONING ----------------
q(2, "OT Zoning", "The four OT zones are:",
  ["Protective, clean, aseptic and disposal", "Sterile, semi-sterile, dirty and waste", "Core, buffer, outer and exit", "OT, ICU, wards and entry"], 0,
  "OT zoning = 1. Protective zone, 2. Clean zone, 3. Aseptic zone, 4. Disposal zone. (Book p2)")
q(2, "OT Zoning", "Which of the following belongs to the protective zone?",
  ["Change rooms, transfer bay, pre & post op rooms, ICU/PACU", "Equipment store room", "The operating theatre itself", "Maintenance workshop"], 0,
  "Protective zone = change rooms, transfer bay, pre & post op rooms and ICU/PACU. (Book p2)")
q(2, "OT Zoning", "The clean zone connects the protective zone to the:",
  ["Aseptic zone", "Protective zone", "Disposal zone", "Ward"], 0,
  "The clean zone connects the protective zone to the aseptic zone. (Book p2)")
q(2, "OT Zoning", "The equipment store room and maintenance workshop are in the:",
  ["Clean zone", "Protective zone", "Aseptic zone", "Disposal zone"], 0,
  "Clean zone = equipment store room and maintenance workshop. (Book p2)")
q(2, "OT Zoning", "The aseptic zone of the OT complex is the:",
  ["Operating theatre (OT)", "Change room", "ICU", "Entry lobby"], 0,
  "Aseptic zone = OT itself. (Book p2)")

# ---------------- p3 · OT POSITIONS ----------------
q(3, "OT Positions", "The m/c position used for abdominal and breast surgeries is the:",
  ["Supine (neutral) position", "Lithotomy position", "Prone position", "Fowler's position"], 0,
  "Supine/neutral position is the m/c position used for abdominal and breast surgeries. (Book p3)")
q(3, "OT Positions", "The Trendelenberg position (head end low, foot end up) is used in:",
  ["Pelvic surgeries", "Upper abdominal surgeries", "Posterior cranial fossa surgery", "Rectal cancer surgery"], 0,
  "Trendelenberg position is used in pelvic surgeries. (Book p3)")
q(3, "OT Positions", "The reverse Trendelenberg position is used in:",
  ["Upper abdominal surgeries", "Pelvic surgeries", "Spinal surgery", "Posterior cranial fossa surgery"], 0,
  "Reverse Trendelenberg is used in upper abdominal surgeries and in laparoscopic cholecystometry with right side up. (Book p3)")
q(3, "OT Positions", "In laparoscopic cholecystectomy, reverse Trendelenberg is taken with the:",
  ["Right side up", "Left side up", "Head end down", "Table level"], 0,
  "Laparoscopic cholecystectomy uses reverse Trendelenberg with right side up. (Book p3)")
q(3, "OT Positions", "In laparoscopic cholecystectomy, CO2 collects below the right dome of the diaphragm, producing the m/c complication of:",
  ["Right shoulder tip pain", "Left shoulder tip pain", "Right leg pain", "Neck pain"], 0,
  "CO2 collects below the right dome of diaphragm → right shoulder tip pain, the m/c complication. (Book p3)")
q(3, "OT Positions", "Lithotomy position is used in all of the following EXCEPT:",
  ["Posterior cranial fossa surgery", "Obstetric procedures", "Gynecologic procedures", "Hemorrhoid surgeries"], 0,
  "Lithotomy is used for obstetric, gynecologic, urologic (TURP) and hemorrhoid surgeries — not posterior cranial fossa surgery. (Book p3)")
q(3, "OT Positions", "The urologic procedure performed in lithotomy position mentioned in the book is:",
  ["TURP", "Nephrectomy", "Pyelolithotomy", "Laparoscopic cholecystectomy"], 0,
  "Urologic procedures (TURP) are listed under the uses of lithotomy position. (Book p3)")
q(3, "OT Positions", "In lithotomy position, if the legs are not supported properly, the nerve commonly injured is the:",
  ["Common peroneal nerve", "Femoral nerve", "Obturator nerve", "Sciatic nerve"], 0,
  "Nerve injured if legs are not supported properly: common peroneal nerve. (Book p3)")
q(3, "OT Positions", "The lateral (kidney) position is NOT used for:",
  ["Hemorrhoid surgery", "Nephrectomy", "Thoracotomy", "Pyelolithotomy"], 0,
  "Lateral/kidney position uses: thoracotomy, pyelolithotomy, nephrolithotomy, nephrectomy and breast reconstruction (latissimus dorsi flap). (Book p3)")
q(3, "OT Positions", "A breast reconstruction operation performed in the lateral (kidney) position uses the:",
  ["Latissimus dorsi flap", "Rectus abdominis flap", "DIEP flap", "Omentum only"], 0,
  "Breast reconstruction in the lateral position uses the latissimus dorsi flap. (Book p3)")
q(3, "OT Positions", "In the lateral (kidney) position, the increased risk of brachial plexus injury is due to:",
  ["Hyperextended arm", "Compressed neck", "Tight waist belt", "Unsupported legs"], 0,
  "Lateral position carries increased risk for brachial plexus injury d/t hyperextended arm. (Book p3)")

# ---------------- p4 · OT POSITIONS ----------------
q(4, "OT Positions", "The prone position is used for:",
  ["Spinal surgery and pilonidal sinus surgery", "Pelvic surgeries", "Laparoscopic cholecystectomy", "Rectal cancer surgery"], 0,
  "Prone position uses: spinal surgery and pilonidal sinus surgery. (Book p4)")
q(4, "OT Positions", "The sitting / Fowler's position is used for:",
  ["Posterior cranial fossa surgery", "Upper abdominal surgery", "Spinal surgery", "Hemorrhoid surgery"], 0,
  "Sitting/Fowler's position is used for posterior cranial fossa surgery. (Book p4)")
q(4, "OT Positions", "An advantage of the sitting / Fowler's position is:",
  ["Bloodless field with reduced blood loss", "No risk of air embolism", "Better venous return", "Easier ventilation"], 0,
  "Advantages of Fowler's: ↓ blood loss (blood less field) and ↑ exposure. (Book p4)")
q(4, "OT Positions", "A disadvantage of the sitting / Fowler's position is:",
  ["Increased risk of air embolism", "Increased blood loss", "Worsened exposure", "Loss of muscle relaxation"], 0,
  "Disadvantage of sitting/Fowler's position: ↑ risk of air embolism. (Book p4)")
q(4, "OT Positions", "The jackknife position is:",
  ["Obsolete, previously used for hemorrhoid/fissure surgeries", "The m/c position for abdominal surgery", "Used for posterior cranial fossa surgery", "Synonymous with lithotomy"], 0,
  "Jackknife position = obsolete position, previously used for hemorrhoid fissure surgeries. (Book p4)")
q(4, "OT Positions", "A complication of the jackknife position is:",
  ["Positional asphyxia", "Air embolism", "Brachial plexus injury", "Common peroneal nerve injury"], 0,
  "Complication of the jackknife position = positional asphyxia. (Book p4)")
q(4, "OT Positions", "The Lloyd-Davis position is a combination of:",
  ["Trendelenberg + lithotomy", "Prone + lithotomy", "Fowler's + Trendelenberg", "Lateral + prone"], 0,
  "Lloyd-Davis position = Trendelenberg + lithotomy position. (Book p4)")
q(4, "OT Positions", "The Lloyd-Davis position is used in:",
  ["Rectal cancer surgery", "Nephrectomy", "Posterior cranial fossa surgery", "Breast surgery"], 0,
  "Lloyd-Davis position is used in rectal cancer surgery. (Book p4)")

# ---------------- p4 · AIR EMBOLISM ----------------
q(4, "Air Embolism", "As per the book, how much air sucked into a vein enters circulation and dysregulates cardiac functioning?",
  ["50–100 cc", "5–10 cc", "500 cc", "5000 cc"], 0,
  "Air (50-100cc) sucked into vein → enters circulation → dysregulates cardiac functioning. (Book p4)")
q(4, "Air Embolism", "Air embolism is a risk in which of the following?",
  ["Thyroid/head and neck surgeries", "Appendicectomies", "Hernia repairs", "Hemorrhoidectomies"], 0,
  "Risk factors for air embolism: thyroid/head & neck surgeries and sitting/Fowler's position. (Book p4)")
q(4, "Air Embolism", "The m/c presenting feature of an air embolism is:",
  ["Sudden desaturation", "Gradual cyanosis", "High-grade fever", "Bradycardia"], 0,
  "Clinical features: sudden desaturation, dyspnea and hypotension. (Book p4)")
q(4, "Air Embolism", "Clinical features of air embolism include all of the following EXCEPT:",
  ["High-grade fever", "Sudden desaturation", "Dyspnea", "Hypotension"], 0,
  "Features = sudden desaturation, dyspnea, hypotension — fever is not listed. (Book p4)")

# ---------------- p5 · AIR EMBOLISM: PREVENTION & MANAGEMENT ----------------
q(5, "Air Embolism", "To prevent air embolism in the Fowler's position, the vein should be:",
  ["Ligated before cutting", "Cut first, then ligated", "Dilated", "Infiltrated with adrenaline"], 0,
  "Prevention: 1. Ligate vein before cutting. (Book p5)")
q(5, "Air Embolism", "Air entry into the field is further prevented by:",
  ["Irrigating the field", "Drying the field", "Elevating the head", "Covering the field"], 0,
  "Prevention of air embolism in Fowler's position: ligate vein before cutting and irrigate field. (Book p5)")
q(5, "Air Embolism", "Management of an air embolism begins with placing the patient in the:",
  ["Durant position", "Trendelenberg position", "Fowler's position", "Lithotomy position"], 0,
  "Management starts with the Durant position, followed by aspiration of air. (Book p5)")
q(5, "Air Embolism", "The Durant position consists of:",
  ["Right side up (left lateral) + legs up", "Left side up + legs down", "Prone + Trendelenberg", "Supine + Trendelenberg"], 0,
  "Durant position = right side up (left lateral) + legs up. (Book p5)")
q(5, "Air Embolism", "After the Durant position, air is removed by:",
  ["Aspiration using direct puncture / central line", "Pericardiocentesis", "Emergent thoracotomy", "Chest tube alone"], 0,
  "Durant position is followed by aspirating air using direct puncture/central line. (Book p5)")
q(5, "Air Embolism", "The Durant position is used when:",
  ["Suspicion of air embolism is positive", "The patient is bleeding into shock", "The patient has a pneumothorax", "The patient is post-extubation"], 0,
  "The Durant position is used if suspicion of air embolism is (+). (Book p5)")

# ---------------- p5 · EVENTS IN PATIENT SAFETY ----------------
q(5, "Events in Patient Safety", "An adverse event is defined as:",
  ["An incident that results in harm to the patient", "An incident that could have harmed the patient", "An incident that never reaches the patient", "A medication error only"], 0,
  "Adverse event = an incident that results in harm to the patient. (Book p5)")
q(5, "Events in Patient Safety", "A near miss is an incident that:",
  ["Could have caused unwanted consequences but did not", "Always causes harm", "Reaches the patient and causes injury", "Is intentional"], 0,
  "Near miss = an incident that could have resulted in unwanted consequences but did not. (Book p5)")
q(5, "Events in Patient Safety", "A near miss is prevented from reaching the patient by:",
  ["Chance or timely intervention", "Patient refusal", "Hospital policy only", "Depth of anaesthesia"], 0,
  "A near miss does not reach the patient either by chance or through timely intervention. (Book p5)")
q(5, "Events in Patient Safety", "A no-harm event:",
  ["Reaches the patient but results in no injury", "Never reaches the patient", "Always causes permanent harm", "Is by definition an adverse event"], 0,
  "No-harm event = an incident that occurs and reaches the patient but results in no injury. (Book p5)")
q(5, "Events in Patient Safety", "In a no-harm event, harm is avoided by:",
  ["Chance or mitigating circumstances", "Early surgery", "Blood transfusion", "Interventional radiology"], 0,
  "In a no-harm event, harm is avoided by chance or due to mitigating circumstances. (Book p5)")

# ---------------- UNITS ----------------
def uid(n): return {"id": f"SURG-U1-{n}", "ch": 1, "n": n}
UNITS = [
    {**uid(1), "title": "Consents: Components & Signatures", "sec": "Consents · p1",
     "qs": [f"SURG-C1-{i:03d}" for i in range(1, 6)],
     "guide": "A valid consent covers identification, diagnosis, the planned procedure, the surgeon, description, patient-specific and procedure-specific complications (any complication >1% incidence), benefits and the alternate procedure — signed by patient, surgeon and witness."},
    {**uid(2), "title": "IV Lines: Color-Coding of Cannulas", "sec": "IV Lines · p1",
     "qs": [f"SURG-C1-{i:03d}" for i in range(6, 19)],
     "guide": "From narrow to wide: yellow 24G (13/10 ml/min), blue 22G (31/30), pink 20G (67/60), green 18G (96), gray 16G (236/240) and orange 14G (270) — the orange 14G is the shock cannula. The 24G/22G/20G trio is bracketed for paediatric patients."},
    {**uid(3), "title": "IV Lines: Superficial Thrombophlebitis", "sec": "IV Lines: Complications · p1",
     "qs": [f"SURG-C1-{i:03d}" for i in range(19, 22)],
     "guide": "The m/c IV complication is superficial thrombophlebitis — a tender, cord-like swelling at the cannulation site, managed with a topical heparinoid."},
    {**uid(4), "title": "Safety Checklist: Phases & Sign In", "sec": "Surgical Safety Checklist · p2",
     "qs": [f"SURG-C1-{i:03d}" for i in range(22, 29)],
     "guide": "The checklist runs sign in (before induction of anaesthesia, ward to OT complex) → time out (before skin incision) → sign out (before the patient leaves the OT). Sign in confirms identity, marked site, procedure, written consent, known allergies and risk of >500 ml blood loss."},
    {**uid(5), "title": "Safety Checklist: Time Out & Sign Out", "sec": "Surgical Safety Checklist · p2",
     "qs": [f"SURG-C1-{i:03d}" for i in range(29, 36)],
     "guide": "Time out confirms patient site, procedure name and time, checks antibiotic prophylaxis within the last 30 min and the surgeon's anticipated blood loss. Sign out verifies instruments/sponge/needle count, specimen labelling with patient name and the anaesthetist's actual blood loss — and the book's note: there is no time in phase."},
    {**uid(6), "title": "Estimating Blood Loss", "sec": "Estimating Blood Loss · p2",
     "qs": [f"SURG-C1-{i:03d}" for i in range(36, 41)],
     "guide": "Actual blood loss = blood in suction − irrigation fluid, or wet mop weight − dry mop weight. A soaked mop holds 100 cc, a fist full of clots 500 cc, and mops carry a radio-opaque line so they are picked up on X-ray."},
    {**uid(7), "title": "OT Zoning: The Four Zones", "sec": "OT Zoning · p2",
     "qs": [f"SURG-C1-{i:03d}" for i in range(41, 46)],
     "guide": "The OT complex flows through four zones: protective (change rooms, transfer bay, pre & post op rooms, ICU/PACU), clean (equipment store room, maintenance workshop — connecting protective to aseptic), aseptic (the OT itself) and disposal."},
    {**uid(8), "title": "OT Positions: Supine, Trendelenberg & Reverse Trendelenberg", "sec": "OT Positions · p3",
     "qs": [f"SURG-C1-{i:03d}" for i in range(46, 51)],
     "guide": "Supine/neutral is the m/c position for abdominal and breast surgeries. Trendelenberg (head low, feet up) serves pelvic surgery; reverse Trendelenberg with right side up is used in laparoscopic cholecystectomy, where CO2 pools under the right diaphragm dome and causes right shoulder tip pain — its m/c complication."},
    {**uid(9), "title": "OT Positions: Lithotomy & Lateral (Kidney)", "sec": "OT Positions · p3",
     "qs": [f"SURG-C1-{i:03d}" for i in range(51, 57)],
     "guide": "Lithotomy serves obstetric, gynecologic, urologic (TURP) and hemorrhoid procedures — with the common peroneal nerve at risk if legs are poorly supported. Lateral/kidney position covers thoracotomy, pyelo/nephrolithotomy, nephrectomy and breast reconstruction (latissimus dorsi flap), risking brachial plexus injury from a hyperextended arm."},
    {**uid(10), "title": "OT Positions: Prone, Fowler's, Jackknife & Lloyd-Davis", "sec": "OT Positions · p4",
     "qs": [f"SURG-C1-{i:03d}" for i in range(57, 65)],
     "guide": "Prone is for spinal and pilonidal sinus surgery. Sitting/Fowler's exposes the posterior cranial fossa in a bloodless field but invites air embolism. Jackknife — once used for hemorrhoid/fissure surgery — is obsolete, killing by positional asphyxia. Lloyd-Davis = Trendelenberg + lithotomy, the rectal cancer position."},
    {**uid(11), "title": "Air Embolism: Features, Prevention & Management", "sec": "Air Embolism · p4",
     "qs": [f"SURG-C1-{i:03d}" for i in range(65, 75)],
     "guide": "50-100 cc of air sucked into a vein dysregulates cardiac function; watch for it in thyroid/head & neck surgery and in Fowler's position. Sudden desaturation, dyspnea and hypotension are the clues — prevent by ligating the vein before cutting and irrigating the field, and treat with the Durant position (right side up/left lateral + legs up) followed by aspiration via direct puncture/central line."},
    {**uid(12), "title": "Events in Patient Safety", "sec": "Events in Patient Safety · p5",
     "qs": [f"SURG-C1-{i:03d}" for i in range(75, 80)],
     "guide": "An adverse event harms the patient; a near miss could have but didn't (stopped by chance or timely intervention); a no-harm event reaches the patient without injury, harm dodged by chance or mitigating circumstances."},
]

data = {"questions": Q, "units": UNITS}
with open("data/ch1.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
print(f"ch1: {len(Q)} questions, {len(UNITS)} units")
