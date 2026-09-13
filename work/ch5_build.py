#!/usr/bin/env python3
"""Build data/ch5.json for PULSE Surgery ch5 (Day Care Surgery, book p25-27)."""
import json

Q = []
def q(page, sec, text, opts, ans, exp):
    Q.append({"id": f"SURG-C5-{len(Q)+1:03d}", "sec": sec, "page": page,
              "q": text, "opts": opts, "ans": ans, "exp": exp})

# ---------------- p25 · DEFINITION & EXAMPLES ----------------
q(25, "Definition", "Day care surgery is defined as: the patient is admitted and discharged within:",
  ["6 hours", "12 hours", "24 hours", "48 hours"], 1,
  "Definition: The patient is admitted and discharged within 12 hours. (Book p25)")
q(25, "Examples: Abdominal", "Abdominal day care procedures include all of the following EXCEPT:",
  ["Haemorrhoidectomy", "Laparoscopic cholecystectomy", "Laparoscopic fundoplication", "Whipple's procedure"], 3,
  "Abdominal day care: anal lesions, haemorrhoidectomy, inguinal/femoral hernia, lap cholecystectomy, lap fundoplication, pilonidal sinus Sx. (Book p25)")
q(25, "Examples: Abdominal", "Which hernia repairs are listed as day care surgery?",
  ["Primary and recurrent inguinal/femoral hernia", "Only primary umbilical hernia", "Only hiatus hernia", "Only incisional hernia"], 0,
  "Abdominal day care: primary and recurrent inguinal/femoral hernia. (Book p25)")
q(25, "Examples: Abdominal", "Pilonidal sinus surgery is listed as a day care procedure of the:",
  ["Breast region", "Abdominal region", "Vascular region", "Orthopedic region"], 1,
  "Abdominal day care includes pilonidal sinus surgery. (Book p25)")
q(25, "Examples: Breast", "Breast day care procedures listed are:",
  ["Mastectomy and axillary clearance", "Excision/biopsy breast lesion, sentinel node excision", "Breast reconstruction", "Bilateral mastectomy"], 1,
  "Breast day care: Excision/biopsy breast lesion, sentinel node excision. (Book p25)")
q(25, "Examples: GU", "Genitourinary day care procedures include all of the following EXCEPT:",
  ["Laser prostatectomy", "Orchidectomy", "Circumcision", "Radical cystectomy"], 3,
  "GU day care: Laser prostatectomy, orchidectomy, circumcision, hydrocele/varicocele/epididymis excision, TURP. (Book p25)")
q(25, "Examples: GU", "TURP is listed as a day care procedure of the:",
  ["Abdominal region", "Genitourinary region", "Vascular region", "Breast region"], 1,
  "GU day care includes TURP. (Book p25)")
q(25, "Examples: Ortho", "Orthopedic day care procedures include all of the following EXCEPT:",
  ["Dupuytren's fasciotomy", "Carpal tunnel release", "Therapeutic arthroscopy of knee or shoulder", "Total hip replacement"], 3,
  "Orthopedic day care: Dupuytren's fasciotomy, carpal tunnel release, arthroscopy knee/shoulder, bunion ops, metalwork removal. (Book p25)")
q(25, "Examples: Ortho", "Removal of metalwork is listed as a day care procedure of the:",
  ["Vascular region", "Orthopedic region", "Abdominal region", "Breast region"], 1,
  "Orthopedic day care includes removal of metalwork. (Book p25)")
q(25, "Examples: Vascular", "Vascular day care procedures listed are:",
  ["Aortic aneurysm repair", "Varicose vein procedures, thoracoscopic sympathectomy", "Carotid endarterectomy", "Femoral bypass"], 1,
  "Vascular day care: Varicose vein procedures, thoracoscopic sympathectomy. (Book p25)")

# ---------------- p25 · SELECTION: MEDICAL ----------------
q(25, "Selection: Medical", "For day care selection, one must use:",
  ["Chronological age > physiological age", "Physiological age > chronological age", "Only chronological age", "Only BMI"], 1,
  "Selection Medical: use physiological age > Chronological age. (Book p25)")
q(25, "Selection: Medical", "ASA Class I & II patients are fit for a:",
  ["Stand alone day care centre", "Integrated day care unit (Hospital)", "ICU", "Emergency OT only"], 0,
  "ASA: Class I & II: Stand alone day care centre; Class III: Integrated day care unit (Hospital). (Book p25)")
q(25, "Selection: Medical", "ASA Class III patients need an:",
  ["Stand alone day care centre", "Integrated day care unit (Hospital)", "Home surgery", "No surgery"], 1,
  "ASA Class III: Integrated day care unit (Hospital). (Book p25)")
q(25, "Selection: Medical", "For laparoscopic day care procedures, BMI must be:",
  ["<= 38", "<= 40", "<= 45", "<= 30"], 0,
  "BMI: <=38: Laparoscopic procedures; <=40: Surface procedures. (Book p25)")
q(25, "Selection: Medical", "For surface day care procedures, BMI must be:",
  ["<= 38", "<= 40", "<= 45", "<= 30"], 1,
  "BMI: <=40: Surface procedures. (Book p25)")

# ---------------- p26 · SELECTION CONTINUED ----------------
q(26, "Selection: Medical", "A diabetic with HbA1C < 8.5 posted for day care surgery is advised to:",
  ["Double the OHA dose", "Skip morning dose of OHA", "Stop all drugs for a week", "Take insulin instead"], 1,
  "HbA1C < 8.5: Advice to skip morning dose of OHA. (Book p26)")
q(26, "Selection: Medical", "For day care surgery, blood pressure must be below:",
  ["140/90", "180/100", "200/120", "160/110"], 1,
  "BP < 180/100. (Book p26)")
q(26, "Selection: Medical", "Which epilepsy patients are fit for day care surgery?",
  ["All epilepsy patients", "Well controlled cases of epilepsy", "Only new cases", "None"], 1,
  "Well controlled cases of epilepsy. (Book p26)")
q(26, "Selection: Social", "Social selection for day care needs responsible adult care availability for:",
  ["6 hours", "12 hours", "24 hours", "1 week"], 2,
  "Social: Responsible adult care availability for 24 hours. (Book p26)")
q(26, "Selection: Social", "Social selection for day care includes all of the following EXCEPT:",
  ["Responsible adult for 24 hours", "Suitable home conditions", "Ability to contact hospital in emergency", "Owning a car"], 3,
  "Social: Responsible adult 24h; Suitable home conditions; Ability to contact hospital in emergency. (Book p26)")
q(26, "Selection: Surgical", "Day care operations must be doable within up to:",
  ["30 minutes", "2 hours", "6 hours", "12 hours"], 1,
  "Surgical: Operations upto 2 hours. (Book p26)")
q(26, "Selection: Surgical", "Surgical selection needs the ability to:",
  ["Eat & drink within a reasonable timescale", "Fast for 3 days", "Stay in ICU", "Walk 10 km"], 0,
  "Surgical: Ability to eat & drink within a reasonable timescale. (Book p26)")

# ---------------- p26 · SCHEDULING & ANAESTHESIA ----------------
q(26, "Scheduling", "In a stand alone day care unit, priority is given to:",
  ["Healthy patients", "Comorbid patients", "Emergency cases", "Children only"], 1,
  "Stand alone day care unit: Priority for comorbid patients. (Book p26)")
q(26, "Scheduling", "In a mixed OT list:",
  ["Day care Sx done first", "Day care Sx done last", "Day care Sx cancelled", "Order is random"], 0,
  "Mixed list: Day care Sx done first. (Book p26)")
q(26, "Anaesthesia", "Anaesthesia of choice for day care surgery is TIVA using:",
  ["Ketamine", "Propofol", "Thiopentone", "Etomidate"], 1,
  "TIVA (Total intravenous anaesthesia): using Propofol. (Book p26)")
q(26, "Anaesthesia", "TIVA with propofol causes:",
  ["More post-op nausea & vomiting", "Less post-op nausea & vomiting", "More pain", "Delayed recovery"], 1,
  "TIVA using Propofol: Less post-op nausea & vomiting. (Book p26)")
q(26, "Anaesthesia", "Analgesia for day care surgery is by infiltration of:",
  ["Lidocaine spray", "Bupivacane", "Morphine IV", "Oral paracetamol only"], 1,
  "Analgesia: Infiltration of Bupivacane. (Book p26)")

# ---------------- p26 · COMPLICATIONS ----------------
q(26, "Complications", "The most common complication requiring re-admission after day care surgery is:",
  ["Pain", "Haemorrhage", "PONV", "Fever"], 1,
  "Haemorrhage: m/c complication requiring re-admission. (Book p26)")
q(26, "Complications", "Primary haemorrhage occurs:",
  ["During Sx", "4 to 24 hours after Sx", "Few days after Sx", "After 1 month"], 0,
  "Primary: During Sx; Reactionary: 4 to 24 hours; Secondary: Few days after Sx. (Book p26)")
q(26, "Complications", "Reactionary haemorrhage occurs:",
  ["During Sx", "4 to 24 hours after Sx", "Few days after Sx", "After 1 month"], 1,
  "Reactionary: 4 to 24 hours after Sx. (Book p26)")
q(26, "Complications", "Secondary haemorrhage occurs a few days after surgery due to:",
  ["Hypertension", "Infection", "Coughing", "Heparin"], 1,
  "Secondary: Few days after Sx (d/t infection). (Book p26)")
q(26, "Complications", "The most common complication after day care surgery overall is:",
  ["Haemorrhage", "Post-op nausea & vomiting (PONV)", "Burst abdomen", "DVT"], 1,
  "Post-op nausea & vomiting (PONV): m/c Complication. (Book p26)")
q(26, "Complications", "The score used to predict PONV is the:",
  ["Apfel score", "Apgar score", "Alvarado score", "Child-Pugh score"], 0,
  "Apfel score: used to predict PONV. (Book p26)")
q(26, "Complications", "Which of the following is listed as a post-op complication of day care surgery?",
  ["Pain", "Burst abdomen", "Fistula", "Stricture"], 0,
  "Post-op complications: Haemorrhage; PONV; Pain. (Book p26)")

# ---------------- p27 · DISCHARGE CRITERIA ----------------
q(27, "Discharge", "Vital signs must be stable for at least ___ before day care discharge:",
  ["15 minutes", "1 hour", "6 hours", "24 hours"], 1,
  "Discharge: Vital signs stable for at least 1 hour. (Book p27)")
q(27, "Discharge", "Before discharge, the patient must be oriented to:",
  ["Time only", "Time, place, and person", "Person only", "Hospital only"], 1,
  "Discharge: Oriented to time, place, and person. (Book p27)")
q(27, "Discharge", "Pain control at discharge needs:",
  ["IV morphine pump", "Adequate pain control with a supply of oral analgesia", "No analgesia", "Epidural catheter"], 1,
  "Discharge: Adequate pain control with a supply of oral analgesia. (Book p27)")
q(27, "Discharge", "The patient must understand:",
  ["How to use oral analgesia supplied", "Surgical technique", "Drug manufacturing", "Hospital billing"], 0,
  "Discharge: Understands how to use oral analgesia supplied. (Book p27)")
q(27, "Discharge", "Before discharge, the patient must have the ability to:",
  ["Run a mile", "Dress and walk where appropriate", "Drive home alone", "Cook a meal"], 1,
  "Discharge: Ability to dress and walk where appropriate. (Book p27)")
q(27, "Discharge", "At discharge there must be minimal:",
  ["Pain only", "Nausea, vomiting or dizziness", "Urine output", "Sleep"], 1,
  "Discharge: minimal nausea, vomiting or dizziness. (Book p27)")
q(27, "Discharge", "Before discharge, the patient must have:",
  ["Taken oral fluids", "Fasted 24 hours", "Passed stool", "Donated blood"], 0,
  "Discharge: Has taken oral fluids. (Book p27)")
q(27, "Discharge", "At discharge there must be minimal:",
  ["Urine output", "Bleeding or wound drainage", "Oral intake", "Movement"], 1,
  "Discharge: minimal bleeding or wound drainage. (Book p27)")
q(27, "Discharge", "Before discharge, the patient must have passed urine:",
  ["Always in all cases", "If appropriate", "Never needed", "Only after 24 hours"], 1,
  "Discharge: Has passed urine (if appropriate). (Book p27)")
q(27, "Discharge", "For discharge, the patient must have:",
  ["A responsible adult to take them home", "A personal car", "A smartphone", "Insurance papers"], 0,
  "Discharge: Has a responsible adult to take them home. (Book p27)")
q(27, "Discharge", "Instructions about postoperative care must be given:",
  ["Only verbally", "Written and verbal", "Only written", "Not needed"], 1,
  "Discharge: Written and verbal instructions given about postoperative care. (Book p27)")
q(27, "Discharge", "The patient must know when to come back for follow-up:",
  ["Always", "If appropriate", "Never", "After 1 year only"], 1,
  "Discharge: Knows when to come back for follow-up (if appropriate). (Book p27)")
q(27, "Discharge", "Before leaving, the patient must be supplied with:",
  ["Emergency contact number", "Hospital map", "Free medicines for a year", "A wheelchair"], 0,
  "Discharge: Emergency contact number supplied. (Book p27)")

# ---------------- p27 · ERAS ----------------
q(27, "ERAS", "ERAS protocol stands for:",
  ["Emergency recovery after Sx", "Enhanced recovery after Sx", "Early re-admission after Sx", "Extended rest after Sx"], 1,
  "ERAS protocol (Enhanced recovery after Sx). (Book p27)")
q(27, "ERAS: Preop", "Preoperative ERAS includes:",
  ["Mechanical bowel preparation", "Patient counselling & expectations", "Prolonged fasting", "No counselling"], 1,
  "ERAS Preoperative: Patient counselling & expectations; Avoid mechanical bowel preparation. (Book p27)")
q(27, "ERAS: Preop", "Preoperative ERAS advises to:",
  ["Do mechanical bowel preparation", "Avoid mechanical bowel preparation", "Give enemas hourly", "Fast for 24 hours"], 1,
  "ERAS Preoperative: Avoid mechanical bowel preparation. (Book p27)")
q(27, "ERAS: Preop", "As per ERAS, solids are allowed up to:",
  ["2 hours prior to Sx", "6 hours prior to Sx", "12 hours prior to Sx", "24 hours prior to Sx"], 1,
  "ERAS: Solids up to 6 hours prior to Sx. (Book p27)")
q(27, "ERAS: Preop", "As per ERAS, carbohydrate loading is done:",
  ["2 to 3 hours before Sx", "12 hours before Sx", "During Sx", "After Sx"], 0,
  "ERAS: Carbohydrate loading: 2 to 3 hours before Sx. (Book p27)")
q(27, "ERAS: Preop", "As per ERAS, clear liquids are allowed up to:",
  ["2 hours prior to Sx", "6 hours prior to Sx", "12 hours prior to Sx", "1 hour prior to Sx"], 0,
  "ERAS: Clear liquids up to 2 hours prior to Sx. (Book p27)")
q(27, "ERAS: Preop", "Preoperative ERAS considers all of the following EXCEPT:",
  ["Acetaminophen", "Pregabalin / gabapentin", "Celecoxib", "IV morphine load"], 3,
  "ERAS: Consider acetaminophen, pregabalin, gabapentin or celecoxib prior to Sx. (Book p27)")
q(27, "ERAS: Intraop", "Intraoperative ERAS prefers a:",
  ["Open approach", "Minimally invasive surgical approach", "Emergency approach", "Staged approach"], 1,
  "ERAS Intraoperative: minimally invasive surgical approach. (Book p27)")
q(27, "ERAS: Intraop", "Intraoperative ERAS uses local anesthetic or long acting local like:",
  ["Plain lidocaine only", "Liposomal bupivacaine", "IV paracetamol", "Oral ibuprofen"], 1,
  "ERAS: Local anesthetic or long acting local (liposomal bupivacaine). (Book p27)")
q(27, "ERAS: Intraop", "Intraoperative ERAS advises to:",
  ["Cool the patient", "Keep patient warm", "Restrict all fluids", "Avoid monitoring"], 1,
  "ERAS Intraoperative: Keep patient warm; IV fluid maintenance. (Book p27)")
q(27, "ERAS: Intraop", "ERAS prophylaxis for nausea & vomiting must cover at least:",
  ["1 class of medications", "2 classes of medications", "4 classes of medications", "No prophylaxis"], 1,
  "ERAS: Prophylaxis for nausea & vomiting (At least 2 classes of medications). (Book p27)")
q(27, "ERAS: Intraop", "Which drug is listed 'if appropriate' intraoperatively in ERAS?",
  ["Morphine", "Toradol", "Ketamine", "Steroid"], 1,
  "ERAS Intraoperative: Toradol (if appropriate). (Book p27)")
q(27, "ERAS: Postop", "Postoperative ERAS analgesia uses:",
  ["Opioids first", "NSAIDS, acetaminophen, gabapentin", "Only IV morphine", "No analgesia"], 1,
  "ERAS Postoperative: NSAIDS, acetaminophen, gabapentin. (Book p27)")
q(27, "ERAS: Postop", "In postoperative ERAS, opioids are used:",
  ["As first line", "Only for breakthrough pain", "Continuously", "Never"], 1,
  "ERAS: Opioids only for breakthrough pain. (Book p27)")
q(27, "ERAS: Postop", "As per ERAS, regular diet is resumed:",
  ["Within 24 hours", "After 1 week", "After 1 month", "Immediately on table"], 0,
  "ERAS: Regular diet within 24 hours. (Book p27)")
q(27, "ERAS: Postop", "As per ERAS, IV fluids are discontinued:",
  ["Within 24 hours", "After 1 week", "After 1 month", "Never"], 0,
  "ERAS: Discontinue IV fluids within 24 hours. (Book p27)")
q(27, "ERAS: Postop", "As per ERAS, the patient must ambulate:",
  ["Within 24 hours", "After 1 week", "After 1 month", "On day 7"], 0,
  "ERAS: Ambulate within 24 hours. (Book p27)")

# ---------------- UNITS ----------------
def uid(n): return {"id": f"SURG-U5-{n}", "ch": 5, "n": n}
def rng(a, b): return [f"SURG-C5-{i:03d}" for i in range(a, b + 1)]
UNITS = [
    {**uid(1), "title": "Definition & Day-Care Examples", "sec": "Definition \u00b7 p25",
     "qs": rng(1, 10),
     "guide": "Day care means in and out within 12 hours - from haemorrhoids, hernias and lap cholecystectomy to breast biopsy, TURP, carpal tunnel release and varicose vein procedures."},
    {**uid(2), "title": "Selection: Medical Criteria", "sec": "Selection \u00b7 p25",
     "qs": rng(11, 15),
     "guide": "Physiological age trumps chronological age: ASA I-II patients suit stand-alone centres while ASA III needs a hospital unit, with BMI capped at 38 for laparoscopic and 40 for surface procedures."},
    {**uid(3), "title": "Selection: Diabetes, Social & Surgical", "sec": "Selection \u00b7 p26",
     "qs": rng(16, 22),
     "guide": "Diabetics under HbA1C 8.5 skip the morning OHA, blood pressure stays below 180/100, and epilepsy must be well controlled. Behind every day-care patient stands a responsible adult for 24 hours, a suitable home, operations under 2 hours, and a quick return to eating and drinking."},
    {**uid(4), "title": "Scheduling & Anaesthesia", "sec": "Scheduling \u00b7 p26",
     "qs": rng(23, 27),
     "guide": "Comorbid patients get priority in stand-alone units, and day cases lead mixed lists. Propofol TIVA keeps nausea away while bupivacaine infiltration handles the pain."},
    {**uid(5), "title": "Post-op Complications", "sec": "Complications \u00b7 p26",
     "qs": rng(28, 34),
     "guide": "Haemorrhage - primary during surgery, reactionary within 4-24 hours, secondary days later from infection - is the commonest cause of re-admission. PONV, predicted by the Apfel score, is the commonest complication overall, followed by pain."},
    {**uid(6), "title": "Discharge Criteria", "sec": "Discharge \u00b7 p27",
     "qs": rng(35, 47),
     "guide": "Discharge demands an hour of stable vitals, full orientation, controlled pain with oral analgesia in hand, the ability to dress and walk, minimal nausea or bleeding, sips of fluid, passed urine, a responsible escort, clear written and verbal instructions, a follow-up plan and an emergency number."},
    {**uid(7), "title": "ERAS Protocol", "sec": "ERAS \u00b7 p27",
     "qs": rng(48, 64),
     "guide": "ERAS fast-tracks recovery: counselled patients skip bowel prep, take solids till 6 hours and carb drinks till 2-3 hours, glide through minimally invasive surgery kept warm with multimodal antiemetics, then eat, walk and leave IV fluids behind - all within 24 hours on non-opioid analgesia."},
]

data = {"questions": Q, "units": UNITS}
with open("data/ch5.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
print(f"ch5: {len(Q)} questions, {len(UNITS)} units")
