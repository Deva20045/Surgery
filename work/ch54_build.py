#!/usr/bin/env python3
"""Build data/ch54.json — Basics of Trauma Management (Marrow Surgery Ed 8, pp410-416)."""
import json

Q = []

def q(page, sec, text, correct, wrongs, note=None):
    opts = [correct] + list(wrongs)
    assert len(opts) == 4
    Q.append({
        "id": f"SURG-C54-{len(Q)+1:03d}",
        "sec": sec,
        "page": page,
        "q": text,
        "opts": opts,
        "ans": 0,
        "exp": (note or correct) + f" (Book p{page})",
    })

# ------------------------------------------------------------------ p410
S1 = "Pre-Hospital Care: Approach, MIST/AMPLE, Transport and Helmet Removal"
q(410, S1, "The chapter 'Basics of Trauma Management' belongs to which book section?", "Trauma", ["Speciality Surgery", "Vascular Surgery", "Neurosurgery"])
q(410, S1, "The first step of the initial pre-hospital approach is:", "Evaluate the scene", ["Initial assessment", "Decide triage transport", "Critical investigations"])
q(410, S1, "The second step of the initial pre-hospital approach is:", "Initial assessment", ["Evaluate the scene", "Decide triage transport", "Patient transport"])
q(410, S1, "The third step of the initial pre-hospital approach is:", "Decide triage transport", ["Initial assessment", "Evaluate the scene", "Critical investigations"])
q(410, S1, "The fourth step of the initial pre-hospital approach is:", "Initial critical investigations + patient transport", ["Decide triage transport", "Helmet removal", "Splintage"])
q(410, S1, "Information from the driver/responder is collected as:", "MIST", ["AMPLE", "START", "AVPU"])
q(410, S1, "In MIST, the 'M' stands for:", "Mechanism", ["Medication", "Morbidity", "Mode"])
q(410, S1, "In MIST, the 'I' stands for:", "Injuries", ["Intoxication", "Incision", "Incident"])
q(410, S1, "In MIST, the 'S' stands for:", "Signs & symptoms", ["Scene", "Surgery", "Shock"])
q(410, S1, "In MIST, the 'T' stands for:", "Treatment given", ["Time of injury", "Transport", "Triage"])
q(410, S1, "Information from the patient is collected as:", "AMPLE", ["MIST", "SAMPLE", "OPQRST"])
q(410, S1, "In AMPLE, the 'A' stands for:", "Allergies", ["Airway", "Age", "Antibiotics"])
q(410, S1, "In AMPLE, the 'M' stands for:", "Medical conditions", ["Mechanism", "Medications only", "Morbidity"])
q(410, S1, "In AMPLE, the 'P' stands for:", "Past history", ["Pulse", "Pain", "Position"])
q(410, S1, "In AMPLE, the 'L' (last meal) is important for:", "Intubation", ["Surgery timing", ["Aspiration risk only"] , "NG tube"])
q(410, S1, "In AMPLE, the 'E' stands for:", "Events leading to trauma", ["Examination", ["Evacuation"] , "Episodes"])
q(410, S1, "For transport, a supine patient is placed on:", "A hard board with head + thorax + pelvis strapped (immobilize)", ["A soft stretcher", ["A vacuum mattress only"] , "A scoop stretcher only"])
q(410, S1, "A prone transport position is used to:", "Prevent aspiration", ["Prevent hypothermia", ["Improve ventilation"] , "Splint the spine"])
q(410, S1, "Patients should NOT be transported in the lateral position because:", "C-spine stabilization is not possible", ["It causes aspiration", ["It worsens shock"] , "It blocks airway"])
q(410, S1, "In two-person helmet removal, person 1:", "Restricts movement of cervical spine", ["Removes the helmet", ["Straps the board"] , "Opens the visor"])
q(410, S1, "In two-person helmet removal, person 2:", "Removes the helmet and then assists with C-spine stabilisation", ["Restricts cervical movement", ["Cuts the strap"] , "Holds the jaw"])

# ------------------------------------------------------------------ p411
S2 = "Timeline Concept, Golden Hour and Triage"
q(411, S2, "The timeline concept of trauma mortality is also known as the:", "Trimodal distribution of mortality", ["Bimodal distribution", ["Unimodal curve"] , "Tetramodal curve"])
q(411, S2, "The first (immediate) peak of trauma mortality is due to:", "Massive head injury", ["Airway obstruction", ["Cardiac tamponade"] , "Infections"])
q(411, S2, "Deaths within 1 hour of injury are potentially saveable; airway causes here include airway obstruction and:", "Tracheobronchial injury", ["Laryngeal edema only", ["Epistaxis"] , "Facial fracture"])
q(411, S2, "Breathing causes of death within the first hour include tension pneumothorax, open pneumothorax and:", "Acute circulatory arrest", ["Cardiac tamponade", ["Hemothorax"] , "Massive head injury"])
q(411, S2, "Circulation causes of death within the first hour include cardiac tamponade and:", "Hemothorax", ["Tension pneumothorax", ["Airway obstruction"] , "Infection"])
q(411, S2, "The third (days/weeks) peak of trauma mortality is due to:", "Infections and delayed head injury", ["Massive head injury", ["Cardiac tamponade"] , "Tension pneumothorax"])
q(411, S2, "The golden hour is the:", "1st hour following trauma", ["1st 30 minutes", ["First 2 hours"] , "First 6 hours"])
q(411, S2, "Care provided during the golden hour:", "↓ mortality", ["↑ mortality", ["No effect"] , "Only ↓ morbidity"])
q(411, S2, "The golden hour is used as:", "A performance metric in trauma centers", ["A teaching tool only", ["A legal standard"] , "A triage colour"])
q(411, S2, "Triage literally means:", "Sort out", ["Prioritize surgery", ["Stabilize"] , "Transport"])
q(411, S2, "Triage is done in:", "Mass casualty events to prioritize treatment", ["Single victim events", ["OPD queues"] , "Ward rounds"])
q(411, S2, "The standard triage system uses how many colour codes?", "Four", ["Three", ["Five"] , "Six"])
q(411, S2, "Triage P1 (Emergency) is coded:", "Red", ["Yellow", ["Green"] , "Blue"])
q(411, S2, "Red (P1) triage includes:", "Causes which kill within 1 hour (immediate Rx required)", ["All fractures", ["Walking wounded"] , "Moribund patients"])
q(411, S2, "Triage P2 (Urgent) is coded:", "Yellow", ["Red", ["Green"] , "Blue"])
q(411, S2, "Yellow (P2) triage includes:", "All fractures (definitive Rx can wait)", ["Causes killing within 1 hour", ["Minor bruises"] , "Dead bodies"])
q(411, S2, "Triage P3 (Delayed) is coded:", "Green", ["Yellow", ["Blue"] , "Black"])
q(411, S2, "Green (P3) triage includes:", "Walking, wounded patients with minor bruises/lacerations (first aid)", ["All fractures", ["Moribund patients"] , "Airway obstruction"])
q(411, S2, "Triage P4 (Expectant) is coded:", "Blue", ["Green", ["Black"] , "Yellow"])
q(411, S2, "Blue (P4) triage includes:", "Moribund patients (alleviation of pain done; definitive Rx not possible)", ["Walking wounded", ["All fractures"] , "Red category"])
q(411, S2, "Dead bodies in triage are coded:", "Black", ["Blue", ["Grey"] , "Purple"])

# ------------------------------------------------------------------ p412
S3 = "ATLS: Surveys, C-spine (NEXUS) and Airway"
q(412, S3, "ATLS follows the sequence:", "ABCD: Airway → Breathing → Circulation → Disability", ["CABD", ["ABDC"] , "DCBA"])
q(412, S3, "In the field (accident) setting the sequence becomes CABCDE, where C stands for:", "Control of exsanguinating hemorrhage", ["Cervical spine", ["Circulation"] , "Compressions"])
q(412, S3, "BLS (basic life support) follows:", "CAB (for cardiac arrest/collapse)", ["ABC", ["ABCD"] , "DRSABC"])
q(412, S3, "The primary survey covers:", "ABCD + life threatening injuries (red category)", ["Detailed survey for injuries", ["Post-extubation review"] , "Only imaging"])
q(412, S3, "The secondary survey is:", "Detailed survey for injuries", ["ABCD + red category", ["Post extubation survey"] , "Scene survey"])
q(412, S3, "The tertiary survey is done:", "Post extubation of intubated patient", ["At admission", ["In the field"] , "Before primary survey"])
q(412, S3, "A pro of whole body CT over 2° survey is:", "Quick assessment", ["Less radiation", ["Cheaper"] , "No contrast"])
q(412, S3, "Cons of whole body CT include ↑ amount of radiation and:", "Only done in stable patients", ["Slow", ["Cannot see bone"] , "Needs MRI backup"])
q(412, S3, "In the primary survey, examination of the C-spine must be done:", "Before airway", ["After breathing", ["After circulation"] , "Last"])
q(412, S3, "The C-spine clearance criteria used are the:", "NEXUS criteria", ["Canadian CT head rules", ["PECARN rules"] , "MIST criteria"])
q(412, S3, "NEXUS stands for National Emergency X-Radiography Utilisation Study; its 'N' component is:", "Neuro deficit", ["Nausea", ["Neck pain only"] , "Numbness"])
q(412, S3, "The 'E' in the NEXUS list refers to:", "Ethanol (alcohol intoxication)", ["Emesis", ["Epilepsy"] , "Edema"])
q(412, S3, "The 'X' in the NEXUS list refers to:", "eXtreme distracting injury", ["X-ray abnormality", ["Crossed signs"] , "Exsanguination"])
q(412, S3, "The 'U' in the NEXUS list refers to:", "Unable to provide history (altered consciousness)", ["Unconscious only", ["Unstable vitals"] , "Unwitnessed event"])
q(412, S3, "The 'S' in the NEXUS list refers to:", "Spinal tenderness (midline)", ["Sensory loss", ["Seatbelt sign"] , "Swelling"])
q(412, S3, "If any NEXUS sign is +ve, apply a Philadelphia collar plus:", "C-spine imaging", ["MRI brain", ["CT chest"] , "No imaging"])
q(412, S3, "If all NEXUS signs are −ve:", "No imaging required", ["X-ray mandatory", ["CT mandatory"] , "MRI mandatory"])
q(412, S3, "The easiest method of airway assessment is to:", "Ask the patient to speak", ["Look for stridor", ["Use capnography"] , "Attempt intubation"])
q(412, S3, "A sign of compromised airway (indication for intubation) is:", "Unable to speak", ["Speaking in full sentences", ["Coughing effectively"] , "Hoarse but speaking"])
q(412, S3, "Another indication for intubation is GCS:", "≤8", ["≤10", ["≤12"] , "≤6"])
q(412, S3, "Unexplained confusion and coma are also:", "Indications for intubation", ["Contraindications to intubation", ["Indications for NIV"] , "Indications for tracheostomy"])
q(412, S3, "The device shown to assist intubation is the:", "Videolaryngoscope", ["Fibroscope", ["Bougie"] , "Laryngeal mask"])
q(412, S3, "The supraglottic device illustrated on p412 is the:", "Laryngeal mask airway", ["Combitube", ["King LT"] , "Endotracheal tube"])

# ------------------------------------------------------------------ p413
S4 = "Definitive Airway, Breathing Adjuncts and Circulation"
q(413, S4, "When endotracheal intubation is possible, the m/c route is:", "Orotracheal", ["Nasotracheal", ["Tracheostomy"] , "Cricothyroidotomy"])
q(413, S4, "Nasotracheal intubation is C/I in:", "Skull base fractures", ["Facial soft tissue injury", ["Trismus"] , "Cervical spine injury"])
q(413, S4, "When endotracheal intubation is not possible, the emergency intervention is:", "Needle cricothyroidotomy", ["Surgical tracheostomy", ["Retrograde intubation"] , "Bag-mask forever"])
q(413, S4, "Needle cricothyroidotomy is followed by definitive management with:", "Tracheostomy", ["Orotracheal intubation", ["LMA"] , "Observation"])
q(413, S4, "Needle cricothyroidotomy is performed through the:", "Cricothyroid membrane", ["Thyrohyoid membrane", ["Tracheal rings 2-3"] , "Cricoid cartilage"])
q(413, S4, "In needle cricothyroidotomy, high flow O2 via Y-connector is given:", "1 sec on + 4 sec off", ["2 sec on + 2 sec off", ["Continuous"] , "5 sec on + 5 sec off"])
q(413, S4, "Needle cricothyroidotomy can be maintained for:", "Up to 15-30 min", ["Up to 5 min", ["Up to 2 hours"] , "Up to 6 hours"])
q(413, S4, "Beyond 15-30 min of needle cricothyroidotomy, what accumulates?", "CO2 (retention takes place)", ["O2", ["Nitrogen"] , "Secretions only"])
q(413, S4, "Breathing assessment includes chest examination with auscultation and:", "Pulse oximetry", ["Capnography only", ["ABG only"] , "Peak flow"])
q(413, S4, "The breathing adjunct imaging includes chest AP views plus pelvic and:", "Cervical X-ray", ["Lumbar X-ray", ["Skull X-ray"] , "Shoulder X-ray"])
q(413, S4, "eFAST stands for:", "Focused Assessment Sonography in Trauma (extended)", ["Fast Assessment Sonography in Trauma", ["Focused Abdominal Sonography in Trauma"] , "Extended Fast Abdominal Scan"])
q(413, S4, "Pulse oximetry, imaging and eFAST in the breathing step are classed as:", "Adjuncts", ["Primary steps", ["Definitive steps"] , "Tertiary steps"])
q(413, S4, "Minimum IV access in the circulation step is:", "Two 16G IV lines", ["One 18G line", ["Two 14G lines"] , "One 16G line"])
q(413, S4, "After securing IV lines, the initial fluid given is:", "1 litre of fluid", ["2 litres", ["500 mL"] , "3 litres"])
q(413, S4, "If IV access is not possible, an emergency option is:", "Intraosseous infusion", ["Central line first", ["Venous cut-down first"] , "Oral fluids"])
q(413, S4, "Intraosseous infusion in trauma is inserted:", "Just below the tibial tuberosity", ["Above the tibial tuberosity", ["Distal tibia"] , "Proximal humerus only"])
q(413, S4, "The other emergency vascular access is venous cut-down of the:", "Great saphenous vein at the medial malleolus", ["Cephalic vein at wrist", ["Femoral vein at groin"] , "Basilic vein at elbow"])
q(413, S4, "The definitive vascular intervention in the circulation step is a:", "Central line", ["Arterial line", ["Midline catheter"] , "PICC"])
q(413, S4, "In trauma, the m/c central line site is the:", "IJV", ["Subclavian vein", ["Femoral vein"] , "PICC"])

# ------------------------------------------------------------------ p414
S5 = "ATLS Updates, Disability and GCS"
q(414, S5, "ATLS 10th edition advises a fluid bolus of:", "1 litre instead of 2 litres (more judicious)", ["2 litres instead of 1", ["500 mL only"] , "3 litres"])
q(414, S5, "The CRASH-2 trial trigger for tranexamic acid is SBP <90 mmHg and/or HR:", ">110/min", [">90/min", [">130/min"] , ">100/min"])
q(414, S5, "CRASH-2 TXA regimen to reduce mortality is:", "1 gm over 10 mins f/b 1 gm over 8 hours", ["1 gm over 1 hour f/b 1 gm over 24 hours", ["2 gm bolus only"] , "500 mg tds"])
q(414, S5, "The 'Disability' step of ATLS uses the:", "GCS (Glasgow Coma Scale)", ["Pupils only", ["AVPU only"] , "NIHSS"])
q(414, S5, "GCS eye opening spontaneously scores:", "4", ["3", ["2"] , "1"])
q(414, S5, "GCS eye opening to speech scores:", "3", ["4", ["2"] , "1"])
q(414, S5, "GCS eye opening to pain scores:", "2", ["3", ["1"] , "4"])
q(414, S5, "GCS best verbal oriented to time, place and person scores:", "5", ["4", ["6"] , "3"])
q(414, S5, "GCS best verbal 'confused' scores:", "4", ["5", ["3"] , "2"])
q(414, S5, "GCS best verbal 'inappropriate words' scores:", "3", ["4", ["2"] , "1"])
q(414, S5, "GCS best verbal 'incomprehensible sounds' scores:", "2", ["3", ["1"] , "4"])
q(414, S5, "GCS best motor 'obeys commands' scores:", "6", ["5", ["4"] , "3"])
q(414, S5, "GCS best motor 'moves to localised pain' scores:", "5", ["6", ["4"] , "3"])
q(414, S5, "GCS best motor 'flexion withdrawal from pain' scores:", "4", ["5", ["3"] , "2"])
q(414, S5, "GCS best motor abnormal flexion (decorticate) scores:", "3", ["4", ["2"] , "1"])
q(414, S5, "GCS best motor abnormal extension (decerebrate) scores:", "2", ["3", ["1"] , "4"])
q(414, S5, "The motor score is recorded using the:", "Single best criteria", ["Sum of both sides", ["Worst side"] , "Average"])
q(414, S5, "Mild head injury corresponds to GCS:", "13-15", ["9-12", ["≤8"] , "15 only"])
q(414, S5, "Moderate head injury corresponds to GCS:", "9-12", ["13-15", ["≤8"] , "6-8"])
q(414, S5, "Severe head injury corresponds to GCS:", "≤8", ["9-12", ["13-15"] , "<5"])
q(414, S5, "GCS has to be measured:", "Serially", ["Once only", ["Only at discharge"] , "Only pre-hospital"])
q(414, S5, "If eye and motor responses are not testable, they are recorded as:", "E_NT and M_NT", ["E0 and M0", ["E1 and M1"] , "Ex and Mx"])
q(414, S5, "If the patient is intubated, the verbal score is recorded as:", "V_NT (not V_T)", ["V1", ["V0"] , "V_T"])
q(414, S5, "GCS(P) score equals:", "GCS − PRS", ["GCS + PRS", ["GCS × PRS"] , "GCS ÷ PRS"])
q(414, S5, "PRS (pupil reactivity score) when both pupils are unreactive to light is:", "2", ["1", ["0"] , "3"])
q(414, S5, "PRS when one pupil is unreactive to light is:", "1", ["2", ["0"] , "3"])
q(414, S5, "PRS when neither pupil is unreactive is:", "0", ["1", ["2"] , "−1"])

# ------------------------------------------------------------------ p415-416
S6 = "Log Roll, Pelvic Binder and Severity Scores"
q(415, S6, "Log roll is done to:", "Examine a patient's back", ["Move the patient to trolley", ["Apply a binder"] , "Check pelvic stability"])
q(415, S6, "Number of people required for a log roll is:", "4 people", ["3 people", ["5 people"] , "6 people"])
q(415, S6, "If a limb fracture is present, log roll requires:", "5 people", ["4 people", ["6 people"] , "3 people"])
q(415, S6, "Log roll has minimal role in pelvic fracture because it may:", "Dislodge clot and cause bleed", ["Cause pain only", ["Worsen spinal injury"] , "Delay imaging"])
q(415, S6, "Log roll also has minimal role in:", "Abdominal trauma", ["Thoracic trauma", ["Head trauma"] , "Limbs trauma"])
q(415, S6, "The exception where log roll helps in abdominal trauma is:", "Penetrating abdominal injury, to check if the wound has gone through", ["Blunt solid organ injury", ["Pelvic hematoma"] , "Retroperitoneal bleed"])
q(415, S6, "A pelvic binder is used in trauma patients with:", "Suspected pelvic fractures", ["Confirmed isolated hip fracture", ["Suspected rib fractures"] , "Suspected femur fracture"])
q(415, S6, "A pelvic binder must be kept until:", "The fracture has been ruled out", ["X-ray is done only", ["24 hours"] , "Surgery"])
q(415, S6, "If a pelvic binder is unavailable:", "Tie a long cloth around the hip", ["Use a thoracic bandage", ["Apply traction"] , "Leave unpadded"])
q(415, S6, "The Injury Severity Score (ISS) is calculated from:", "Abbreviated injury score (AIS) of top 3 injuries squared and added", ["AIS of all injuries added", ["GCS + AIS"] , "AIS of worst injury squared"])
q(415, S6, "The Revised Trauma Score (RTS) measures:", "Glasgow Coma Scale, systolic BP and respiratory rate", ["GCS, HR and temperature", ["GCS, ISS and age"] , "BP, HR and urine output"])
q(415, S6, "The score that gives information about survival of a trauma patient is:", "TRISS (Trauma Score and Injury Severity Score)", ["ISS", ["RTS"] , "MESS"])
q(415, S6, "TRISS parameters include RTS, ISS, mechanism of injury and:", "Age", ["Sex", ["Comorbidity"] , "Weight"])
q(415, S6, "MESS stands for:", "Mangled Extremity Severity Score", ["Major Extremity Severity Score", ["Mangled Extremity Salvage Score"] , "Multiple Extremity Severity Score"])
q(415, S6, "MESS parameters include type of injury, ischemia group, shock group and:", "Age group", ["Weight group", ["Sex"] , "Comorbidity group"])
q(416, S6, "A MESS score of ≤6 is consistent with:", "A salvageable limb", ["Amputation", ["Infection"] , "Non-union"])
q(416, S6, "A MESS score of ≥7 means the eventual result is:", "Amputation", ["Salvage", ["Arthrodesis"] , "Grafting"])

# ------------------------------------------------------------------ p416
S7 = "Metabolic Response to Trauma: Ebb and Flow"
q(416, S7, "The metabolic response to trauma is described as:", "Ebb and flow", ["Fight and flight", ["Shock and recovery"] , "Catabolism only"])
q(416, S7, "The ebb phase lasts:", "<24 hrs", ["3-10 days", ["10-60 days"] , "48-72 hrs"])
q(416, S7, "The role of the ebb phase is:", "Maintaining blood volume", ["Maintenance of energy", ["Replacement of lost tissue"] , "Wound healing"])
q(416, S7, "Physiologically the ebb phase shows:", "↓ BMR, temp, O2 consumption with vasoconstriction", ["↑ BMR, temp, O2 consumption", ["+ve N2 balance"] , "Hypermetabolism"])
q(416, S7, "The ebb phase also shows ↑ CO2, HR and:", "Acute phase proteins", ["Albumin", ["Transferrin"] , "Prealbumin"])
q(416, S7, "Hormones of the ebb phase are:", "Catecholamines, cortisol, aldosterone", ["Insulin, glucagon", ["Growth hormone, IGF"] , "Thyroxine, insulin"])
q(416, S7, "The catabolic phase lasts:", "3-10 days", ["<24 hrs", ["10-60 days"] , "1-2 days"])
q(416, S7, "The role of the catabolic phase is:", "Maintenance of energy", ["Maintaining blood volume", ["Replacement of lost tissue"] , "Coagulation"])
q(416, S7, "Physiologically the catabolic phase shows ↑ BMR, temp, O2 consumption and:", "−ve N2 balance", ["+ve N2 balance", ["Zero N2 balance"] , "Vasoconstriction"])
q(416, S7, "Hormones of the catabolic phase include ↑ insulin, glucagon, cortisol and catecholamines with:", "Insulin resistance", ["Insulin sensitivity", ["Hypoglycemia"] , "Lipogenesis"])
q(416, S7, "The anabolic phase is also called the:", "Moore phase", ["Cuthbertson phase", ["Flow phase"] , "Recovery phase"])
q(416, S7, "The anabolic (Moore) phase lasts:", "10-60 days", ["3-10 days", ["<24 hrs"] , "60-90 days"])
q(416, S7, "The role of the anabolic phase is:", "Replacement of lost tissue", ["Maintaining blood volume", ["Maintenance of energy"] , "Hemostasis"])
q(416, S7, "The anabolic phase shows:", "+ve N2 balance", ["−ve N2 balance", ["↑ BMR"] , "Vasoconstriction"])
q(416, S7, "Hormones of the anabolic phase are:", "Growth hormone and IGF", ["Catecholamines and cortisol", ["Insulin and glucagon"] , "Aldosterone and renin"])
q(416, S7, "Adequate resuscitation can ↓ the duration and extent of the:", "Ebb phase", ["Catabolic phase", ["Anabolic phase"] , "Flow phase"])
q(416, S7, "Patients in the catabolic phase require ↑:", "Protein intake", ["Fat intake", ["Carbohydrate only"] , "Fluid restriction"])

# ------------------------------------------------------------------ units
def first_page(title):
    return next(x["page"] for x in Q if x["sec"] == title)

UNIT_DEFS = [
    (S1, "Pre-hospital care starts by evaluating the scene, initial assessment, deciding triage transport and pairing critical investigations with patient transport. Responders hand over MIST (mechanism, injuries, signs & symptoms, treatment given) while the patient gives AMPLE (allergies, medical conditions, past history, last meal — vital for intubation — and events leading to trauma). Patients travel supine on a hard board with head, thorax and pelvis strapped, prone only to prevent aspiration and never lateral because the C-spine cannot be stabilised; helmets come off with two people, one restricting cervical movement while the other removes the helmet then helps stabilise the spine."),
    (S2, "Trauma deaths follow a trimodal curve: immediate deaths from massive head injury, a saveable first-hour wave from airway obstruction and tracheobronchial injury (airway), tension/open pneumothorax and acute circulatory arrest (breathing) or cardiac tamponade and hemothorax (circulation), and a late days-to-weeks peak from infections and delayed head injury. The golden hour — the first hour after trauma — cuts mortality when care is delivered and benchmarks trauma centers. Triage sorts mass casualties into red P1 emergencies that kill within an hour, yellow P2 urgents including all fractures, green P3 delayed walking wounded, blue P4 expectant moribund patients given pain relief only, and black for the dead."),
    (S3, "ATLS runs ABCD (airway, breathing, circulation, disability), becomes CABCDE in the field with C for control of exsanguinating hemorrhage, while BLS for arrest uses CAB. The primary survey hunts ABCD plus life-threatening red-category injuries, the secondary survey details all injuries and the tertiary survey repeats after extubation; whole body CT is quick but radiation-heavy and only for stable patients. C-spine is examined before the airway using NEXUS (neuro deficit, ethanol, extreme distracting injury, unable to give history, midline spinal tenderness): any positive mandates a Philadelphia collar and C-spine imaging, all negative needs none. Asking the patient to speak is the easiest airway test; inability to speak, GCS ≤8, unexplained confusion or coma indicate intubation, assisted by videolaryngoscopy or bridged with a laryngeal mask airway."),
    (S4, "A definitive airway is orotracheal intubation (m/c) when possible, nasotracheal being contraindicated in skull base fractures; when impossible, needle cricothyroidotomy through the cricothyroid membrane buys 15-30 minutes of high-flow O2 given 1 sec on and 4 sec off via a Y-connector before CO2 retention, with tracheostomy as definitive management. Breathing is checked by chest auscultation and pulse oximetry with adjunct imaging (chest AP, pelvic and cervical X-rays) and eFAST (focused assessment sonography in trauma). Circulation demands two 16G lines and 1 litre of fluid; failing that, intraosseous infusion just below the tibial tuberosity or great saphenous cut-down at the medial malleolus bridge to a definitive central line, internal jugular in trauma."),
    (S5, "ATLS 10th edition trims the bolus to 1 litre instead of 2, and CRASH-2 gives tranexamic acid 1 gm over 10 minutes then 1 gm over 8 hours when SBP <90 mmHg or HR >110/min to cut mortality. Disability is graded by GCS: eyes 4-1, verbal 5-1, motor 6-1 (single best response), totalling 13-15 mild, 9-12 moderate and ≤8 severe, measured serially; untestable eye/motor components are tagged NT and an intubated patient's verbal score is V_NT. The GCS(P) subtracts the pupil reactivity score — 2 for both pupils unreactive, 1 for one, 0 for neither — from the GCS."),
    (S6, "Log rolling exposes the back with four people (five with a limb fracture) but has minimal role in pelvic fracture, where it may dislodge clot and restart bleeding, and in blunt abdominal trauma — except penetrating wounds, where it checks through-and-through track. Suspected pelvic fractures get a binder kept until fracture is excluded, or a long cloth tied around the hips if none exists. Severity scoring: ISS squares and sums the AIS of the top three injuries; RTS uses GCS, systolic BP and respiratory rate; TRISS (RTS, ISS, mechanism, age) predicts survival; MESS (type of injury, ischemia, shock, age groups) guides limbs — ≤6 salvageable, ≥7 destined for amputation."),
    (S7, "The metabolic response to trauma ebbs then flows: the ebb phase (<24 h) preserves blood volume with lowered BMR, temperature and O2 consumption, vasoconstriction and raised CO2, heart rate and acute phase proteins under catecholamines, cortisol and aldosterone. The catabolic phase (3-10 days) maintains energy with raised BMR, temperature and O2 consumption and negative nitrogen balance driven by insulin, glucagon, cortisol and catecholamines amid insulin resistance, needing extra protein; the anabolic Moore phase (10-60 days) replaces lost tissue with positive nitrogen balance under growth hormone and IGF. Good resuscitation shortens the ebb phase."),
]

UNITS = []
for i, (title, guide) in enumerate(UNIT_DEFS, 1):
    UNITS.append({
        "id": f"SURG-U54-{i}",
        "ch": 54,
        "n": i,
        "title": title,
        "sec": f"{title} · p{first_page(title)}",
        "qs": [x["id"] for x in Q if x["sec"] == title],
        "guide": guide,
    })

covered = [x for u in UNITS for x in u["qs"]]
assert covered == [x["id"] for x in Q]
assert len(set(covered)) == len(covered)
with open("data/ch54.json", "w", encoding="utf-8") as f:
    json.dump({"questions": Q, "units": UNITS}, f, ensure_ascii=False, indent=1)
print(f"ch54: {len(Q)} questions, {len(UNITS)} units")
