#!/usr/bin/env python3
"""Build data/ch56.json — Thoracic Trauma (Marrow Surgery Ed 8, pp426-434)."""
import json

Q = []

def q(page, sec, text, correct, wrongs, note=None):
    opts = [correct] + list(wrongs)
    assert len(opts) == 4
    Q.append({
        "id": f"SURG-C56-{len(Q)+1:03d}",
        "sec": sec,
        "page": page,
        "q": text,
        "opts": opts,
        "ans": 0,
        "exp": (note or correct) + f" (Book p{page})",
    })

# ------------------------------------------------------------------ p426
S1 = "Thoracic Trauma: Overview and Life-Threatening Injuries"
q(426, S1, "Thoracic trauma is m/c seen in:", "Polytrauma patients", ["Isolated assault victims", "Burns patients", "Post-operative ICU patients"])
q(426, S1, "The m/c cause of death in blunt thoracic trauma is:", "Tracheobronchial injury", ["Hemothorax", "Rib fracture", "Pulmonary contusion"])
q(426, S1, "The m/c cause of death in penetrating thoracic trauma is:", "Hemothorax 2° to pulmonary laceration", ["Tracheobronchial injury", "Cardiac tamponade", "Airway obstruction"])
q(426, S1, "Which life-threatening AIRWAY injuries are looked for during the 1° survey?", "Airway obstruction & tracheobronchial tree injury", ["Tension pneumothorax & open pneumothorax", "Massive hemothorax & tamponade", "Pulmonary contusion & flail chest"])
q(426, S1, "Which life-threatening BREATHING injuries are looked for during the 1° survey?", "Tension pneumothorax & open pneumothorax", ["Airway obstruction & tracheobronchial injury", "Massive hemothorax & cardiac tamponade", "Traumatic circulatory arrest & tamponade"])
q(426, S1, "Which life-threatening CIRCULATION injuries are looked for during the 1° survey?", "Massive hemothorax, cardiac tamponade & traumatic circulatory arrest", ["Tension & open pneumothorax", "Airway obstruction & tracheobronchial injury", "Rib fracture & flail chest"])
q(426, S1, "The 1st investigation in thoracic trauma is:", "Chest X-ray (AP view)", ["CT chest", "eFAST", "Pulse oximetry"])
q(426, S1, "The 2nd investigation in thoracic trauma is:", "eFAST (extended focused assessment sonogram in trauma)", ["Chest X-ray (AP view)", "CT angiography", "Pulse oximetry"])
q(426, S1, "The 3rd investigation in thoracic trauma is:", "Pulse oximetry", ["eFAST", "Chest X-ray", "ABG"])
q(426, S1, "The majority of thoracic trauma is managed:", "Conservatively with chest tubes", ["By emergency thoracotomy", "By sternotomy", "With IPPV"])
q(426, S1, "In eFAST, the epigastric/subxiphoid probe gives the:", "Pericardial window", ["Perisplenic window", "Perihepatic window", "Pelvic window"])
q(426, S1, "In eFAST, the suprapubic probe looks for fluid collection in the:", "Pelvis", ["Pericardium", "Left chest", "Right chest"])
q(426, S1, "The RUQ and LUQ probes in eFAST look for collections around the liver and:", "Spleen", ["Kidneys", "Pancreas", "Pericardium"])

# ------------------------------------------------------------------ p426-427
S2 = "Rib Fractures"
q(426, S2, "The m/c type of thoracic trauma is:", "Rib fractures", ["Pneumothorax", "Hemothorax", "Flail chest"])
q(426, S2, "The m/c ribs fractured during CPR are the:", "3-5th ribs", ["1st-2nd ribs", "8-10th ribs", "11-12th ribs"])
q(426, S2, "High velocity impact (RTA) leads to fractures of the:", "1st / 10-12th ribs", ["3-5th ribs only", "6-8th ribs only", "Only the sternum"])
q(426, S2, "Structures associated with 1st rib fracture are:", "Apex of lung, brachial plexus & subclavian vessels", ["Spleen and liver", "Trachea and esophagus", "Diaphragm and colon"])
q(427, S2, "Injury to the 10-12th (floating) ribs on the LEFT suggests:", "Splenic injury", ["Liver injury", "Renal injury", "Cardiac injury"])
q(427, S2, "Injury to the 10-12th (floating) ribs on the RIGHT suggests:", "Liver injury", ["Splenic injury", "Duodenal injury", "Bladder injury"])
q(427, S2, "ANTERIOR aspect of the rib on CXR is located:", "Away from the midline", ["Closer to the midline", "Over the spine", "Below the clavicle"])
q(427, S2, "POSTERIOR aspect of the rib on CXR is located:", "Closer to the midline", ["Away from the midline", "Near the axilla", "Below the scapula"])
q(427, S2, "ANTERIOR ribs are oriented:", "Obliquely", ["Horizontally", "Vertically", "Spirally"])
q(427, S2, "POSTERIOR ribs are oriented:", "Horizontally", ["Obliquely", "Vertically", "Randomly"])
q(427, S2, "Rib fractures are m/c seen in:", "Adults", ["Children", "Neonates", "Elderly only"])
q(427, S2, "In children the ribs are pliable, so chest trauma tends to:", "Damage the underlying organs without fracture", ["Always fracture upper ribs", "Cause flail chest", "Spare all intrathoracic organs"])
q(427, S2, "Clinical features of rib fracture include pain and:", "Bruising on the chest", ["Paradoxical movement", "Tracheal shift", "Muffled heart sounds"])
q(427, S2, "Treatment of an isolated rib fracture is:", "Adequate analgesia", ["Strapping of chest", "Rib fixation", "IPPV"])
q(426, S2, "CXR shows ribs 1-11; rib fractures missing on CXR suggest injury to the:", "12th rib (rarely fractured)", ["1st rib", "4th rib", "7th rib"])

# ------------------------------------------------------------------ p427-428
S3 = "Flail Chest"
q(427, S3, "Flail chest is defined as fracture of:", "≥2 consecutive ribs at ≥2 places", ["≥3 ribs at 1 place", "1 rib at 2 places", "≥2 ribs anywhere"])
q(427, S3, "The leading cause of death in flail chest is:", "Underlying pulmonary contusion", ["Paradoxical movement", "Pneumothorax", "Aortic injury"])
q(427, S3, "Paradoxical chest movement in flail chest means the flail segment:", "Moves in the opposite direction of the chest wall", ["Moves with the chest wall", "Is completely immobile", "Moves only on coughing"])
q(427, S3, "During INSPIRATION the flail segment:", "Moves in", ["Moves out", "Does not move", "Moves up"])
q(427, S3, "During EXPIRATION the flail segment:", "Moves out", ["Moves in", "Does not move", "Moves down"])
q(428, S3, "The Ix of flail chest is:", "Chest X-ray", ["CT chest", "USG chest", "Fluoroscopy"])
q(428, S3, "Initial mx of flail chest is:", "O2 + adequate analgesia (thoracic epidural)", ["Immediate surgical fixation", "Chest strapping", "Tracheostomy"])
q(428, S3, "The preferred mode of analgesia in flail chest is:", "Thoracic epidural", ["NSAIDs only", "Intercostal block only", "IV opioids only"])
q(428, S3, "IPPV is indicated in flail chest when:", "RR > 30/min & pO2 < 60 mmHg", ["RR > 10/min & pO2 < 90 mmHg", "RR < 12/min & pCO2 > 45 mmHg", "RR > 40/min & pO2 > 80 mmHg"])
q(428, S3, "IPPV in flail chest serves as:", "Internal splinting", ["External splinting", "Secretion clearance", "Analgesia"])
q(428, S3, "Surgical fixation of flail chest is done when despite IPPV:", "RR > 30/min & pO2 < 60 mmHg persist", ["Pain is mild", "CXR is normal", "Patient is asymptomatic"])

# ------------------------------------------------------------------ p428
S4 = "Pneumothorax: Definition, Types and Tension Etiology/Mechanism"
q(428, S4, "Pneumothorax is accumulation of air in the:", "Pleural space", ["Pericardial space", "Peritoneal space", "Mediastinum"])
q(428, S4, "The two types of pneumothorax are:", "Simple and Tension", ["Open and Closed only", "Wet and Dry", "Acute and Chronic"])
q(428, S4, "In SIMPLE pneumothorax there is:", "No change in hemodynamic status", ["Altered hemodynamic status", "Always shock", "Tracheal shift to same side"])
q(428, S4, "In TENSION pneumothorax there is:", "Altered hemodynamic status", ["No change in hemodynamics", "Only mild dyspnea", "Normal JVP"])
q(428, S4, "Etiology of tension pneumothorax (1):", "Tracheobronchial injury", ["Esophageal rupture", "Diaphragmatic injury", "Sternal fracture"])
q(428, S4, "Etiology of tension pneumothorax (2):", "Large pulmonary laceration with air leak", ["Small hemothorax", "Rib bruising", "Cardiac contusion"])
q(428, S4, "Etiology of tension pneumothorax (3):", "Penetrating wound in the chest wall (open pneumothorax)", ["Blunt abdominal trauma", "CPR fractures", "Whiplash injury"])
q(428, S4, "A stab wound to the chest wall acts as a:", "Sucking wound (one-way valve)", ["Two-way valve", "Self-sealing wound", "Vacuum"])
q(428, S4, "The immediate effect of a one-way valve chest wound is:", "Collapse of affected lung & hyperinflation of opposite lung", ["Bilateral collapse", "Collapse of opposite lung", "No lung change"])
q(428, S4, "As tension pneumothorax progresses (mins/hours):", "Trachea shifts to opposite side & heart gets compressed", ["Trachea shifts to same side", "Trachea & heart unaffected", "Heart gets dilated"])

# ------------------------------------------------------------------ p429
S5 = "Tension Pneumothorax: Clinical Features, Differentials and Management"
q(429, S5, "Tension pneumothorax is a:", "Clinical diagnosis", ["Radiological diagnosis", "CT-based diagnosis", "Laboratory diagnosis"])
q(429, S5, "Clinical features of tension pneumothorax include all EXCEPT:", "Bradycardia", ["Tachypnea (↑RR)", "Tachycardia (↑HR)", "↓SBP"])
q(429, S5, "JVP in tension pneumothorax is:", "↑ (raised)", ["Normal", "Absent", "Low"])
q(429, S5, "Breath sounds in tension pneumothorax are:", "Absent", ["Normal", "Bronchial", "Vesicular"])
q(429, S5, "Percussion note in tension pneumothorax is:", "Hyperresonant", ["Dull", "Normal", "Stony dull"])
q(429, S5, "Cardiac sounds in tension pneumothorax are:", "Normal", ["Muffled", "Loud", "Absent"])
q(429, S5, "vs cardiac tamponade: breath sounds and percussion note are:", "Normal", ["Absent and hyperresonant", "Absent and dull", "Bronchial and dull"])
q(429, S5, "vs cardiac tamponade: the distinguishing cardiac finding is:", "Muffled cardiac sounds", ["Normal cardiac sounds", "Accentuated S1", "Pericardial knock"])
q(429, S5, "In hemothorax the percussion note is:", "Dull", ["Hyperresonant", "Normal", "Tympanic"])
q(429, S5, "In hemothorax the JVP is:", "Normal (–)", ["Raised", "Collapsed", "Bilaterally raised"])
q(429, S5, "Breath sounds in hemothorax are:", "Absent", ["Normal", "Bronchial", "Amphoric"])
q(429, S5, "The only pneumothorax with NO change in hemodynamic status is:", "Simple pneumothorax", ["Tension pneumothorax", "Open pneumothorax", "Hydropneumothorax"])
q(429, S5, "The 1st Ix of tension pneumothorax is:", "Chest X-ray", ["CT chest", "eFAST", "ECG"])
q(429, S5, "eFAST in pneumothorax (M-mode) shows:", "Loss of seashore/barcode/stratosphere sign", ["Normal seashore sign", "Gliding sign increase", "No change"])
q(429, S5, "eFAST additionally helps in ruling out:", "Cardiac tamponade", ["Rib fracture", "Diaphragmatic injury", "Aortic injury"])
q(429, S5, "Emergency mx of tension pneumothorax is:", "Needle thoracocentesis", ["Chest tube immediately", "Thoracotomy", "IPPV"])
q(429, S5, "Needle thoracocentesis site in ADULTS is:", "5th intercostal space, mid axillary line", ["2nd intercostal space, mid clavicular line", "5th ICS, mid clavicular line", "2nd ICS, mid axillary line"])
q(429, S5, "Needle thoracocentesis site in CHILDREN is:", "2nd intercostal space, mid clavicular line", ["5th intercostal space, mid axillary line", "3rd ICS, mid axillary line", "4th ICS, mid clavicular line"])
q(429, S5, "Definitive mx of tension pneumothorax is:", "Tube thoracocentesis (chest tube)", ["Needle thoracocentesis", "Thoracotomy", "Sternotomy"])
q(429, S5, "The chest tube for tension pneumothorax is placed in the:", "Triangle of safety", ["2nd ICS mid-clavicular", "1st ICS mid-line", "9th ICS posteriorly"])
q(429, S5, "An open chest wound is covered with:", "3-sided occlusive dressing", ["4-sided occlusive dressing", "Wet gauze only", "No dressing"])
q(429, S5, "The 3-sided occlusive dressing works by:", "Reversing the flow of one-way valve", ["Sealing completely", "Sucking air in", "Applying pressure"])
q(429, S5, "Mx of SIMPLE (symptomatic) pneumothorax is:", "Chest tube placement", ["Observation only", "Needle aspiration only", "Thoracotomy"])

# ------------------------------------------------------------------ p430
S6 = "Hemothorax"
q(430, S6, "Hemothorax is accumulation of blood in the pleural space, most commonly d/t:", "Intercostal vessels injury", ["Aortic injury", "Pulmonary vein injury", "Coronary vessel injury"])
q(430, S6, "Symptoms of hemothorax include:", "Tachypnoea, ↓cardiac output, ↓SBP, tachycardia", ["Bradypnea and hypertension", "Bradycardia and flushing", "Fever and rigors"])
q(430, S6, "Signs of hemothorax are:", "Percussion dull note & absent breath sounds", ["Hyperresonant note & absent sounds", "Dull note & bronchial breathing", "Hyperresonant note & normal sounds"])
q(430, S6, "Ix of hemothorax:", "Chest X-ray & eFAST", ["CT chest & MRI", "CXR & bronchoscopy", "USG & DPL"])
q(430, S6, "CXR findings in hemothorax include:", "Air-fluid level, white-out lung & blunting of costophrenic angle", ["Tracheal pull to same side", "Ring shadow", "Barrel chest"])
q(430, S6, "Mx of hemothorax is:", "Chest tube insertion in triangle of safety", ["Needle aspiration", "Observation", "Thoracotomy in all"])
q(430, S6, "Emergency thoracotomy is indicated when chest tube releases bleeding of:", ">1-1.5 L", [">500 ml", ">2-3 L", "Any amount"])
q(430, S6, "Emergency thoracotomy is indicated for continued bleeding of:", ">200 cc/hr for ≥3 consecutive hours", [">100 cc/hr for 6 hours", ">500 cc/hr for 1 hour", ">200 cc/day"])
q(430, S6, "Which great vessel injury mandates emergency thoracotomy?", "Aortic injury", ["Femoral artery", "Subclavian vein", "Carotid injury"])
q(430, S6, "Which paired organ injuries mandate emergency thoracotomy?", "Tracheobronchial / esophageal injury", ["Rib fractures", "Sternal fracture", "Clavicle fracture"])
q(430, S6, "Cardiac condition that mandates emergency thoracotomy:", "Cardiac tamponade", ["Myocardial contusion", "Atrial fibrillation", "Pericardial cyst"])
q(430, S6, "Emergency thoracotomy for trauma is done through the:", "Anterolateral approach", ["Posterolateral approach", "Median sternotomy only", "Thoracoabdominal approach"])
q(430, S6, "Emergency ROOM thoracotomy is:", "Obsolete now", ["First line", "Done in all arrest cases", "Preferred over OT thoracotomy"])
q(430, S6, "Disadvantages of ER thoracotomy:", "Open cardiac massage (contaminated wound) & high mortality", ["Low yield of CT", "Needs anaesthesia", "Long incision"])

# ------------------------------------------------------------------ p430-431
S7 = "Chest Tube: Triangle of Safety and Insertion"
q(430, S7, "Site of chest tube insertion is:", "Triangle of safety", ["2nd ICS mid-clavicular line", "Posterior axillary line 9th ICS", "Any intercostal space"])
q(430, S7, "Within the triangle of safety the tube is placed over the:", "Upper border of lower rib", ["Lower border of upper rib", "Middle of the space", "Rib itself"])
q(431, S7, "The tube goes over the upper border of the lower rib because the lower border has:", "The neurovascular border (bundle)", ["No structures", "Lymphatics only", "Fat only"])
q(431, S7, "The APEX of the triangle of safety is the:", "Axilla", ["Nipple", "Xiphisternum", "Clavicle"])
q(431, S7, "The POSTERIOR boundary of the triangle of safety is the:", "Mid axillary line", ["Anterior axillary line", "Mid clavicular line", "Vertebral line"])
q(431, S7, "The ANTERIOR boundary of the triangle of safety is the anterior axillary line, formed by:", "Pectoralis major", ["Latissimus dorsi", "Serratus anterior", "Rectus abdominis"])
q(431, S7, "The BASE of the triangle of safety is the:", "5th intercostal space", ["2nd intercostal space", "4th lumbar space", "6th rib margin"])
q(431, S7, "Structures pierced during chest tube insertion (1-4):", "Skin, superficial fascia, deep fascia & serratus anterior", ["Pec major, ribs, pleura, lung", "Skin, muscle, rib, pleura", "Fascia, rib, lung, pleura"])
q(431, S7, "Structures pierced during chest tube insertion (5-7):", "3 layers of intercostal muscles, endothoracic fascia & parietal pleura", ["Serratus, rib, lung", "Pec major, pericardium, lung", "External oblique, pleura, lung"])
q(431, S7, "During chest tube insertion, ALL layers from skin to parietal pleura must be:", "Anesthetized", ["Avoided", "Cut without anesthesia", "Sutured"])
q(431, S7, "The underwater seal is filled with water to:", "Prevent suction of air during inspiration", ["Detect bleeding", "Lubricate the tube", "Sterilize the system"])
q(431, S7, "Functioning of a chest tube is assessed by:", "Movement of the water column", ["Bubbling sound", "Tube length", "Daily X-ray only"])

# ------------------------------------------------------------------ p432
S8 = "Chest Tube: Positioning and Removal"
q(432, S8, "Positioning of the chest tube is assessed by:", "X-ray chest", ["USG chest", "CT chest", "Auscultation only"])
q(432, S8, "A normally positioned chest tube on CXR shows:", "A break in the radio-opaque line", ["A continuous radio-opaque line", "No tube shadow", "A pleural ring"])
q(432, S8, "Chest tube is removed when the lung is expanded, which is confirmed by:", "CXR + normal breath sounds", ["Only auscultation", "Only patient comfort", "CT scan"])
q(432, S8, "Chest tube output criterion for removal:", "<100 cc/24 hours", ["<500 cc/24 hours", "<100 cc/hour", "<1 L/day"])
q(432, S8, "Chest tube is removed at the peak of inspiration with patient holding breath to:", "Prevent suction of air", ["Reduce pain", "Avoid bleeding", "Prevent cough"])

# ------------------------------------------------------------------ p432-433
S9 = "Cardiac Tamponade"
q(432, S9, "Cardiac tamponade is rapid accumulation of blood in the pericardial space, minimum volume:", "60-70 cc", ["200-300 cc", "500 cc", "1 L"])
q(432, S9, "Cardiac tamponade m/c follows:", "Penetrating trauma >> blunt injury", ["Blunt injury >> penetrating", "Burns", "Falls"])
q(432, S9, "Beck's triad consists of:", "Hypotension, ↑JVP/distended neck veins & muffled heart sounds", ["Hypertension, ↑JVP & loud sounds", "Tachycardia, ↓JVP & muffled sounds", "Hypotension, ↓JVP & click"])
q(432, S9, "Presentation of cardiac tamponade is similar to tension pneumothorax, with:", "Deteriorating cyanosis, tachycardia & agitation", ["Bradycardia & comfort", "Paradoxical movement", "Bowel sounds in chest"])
q(432, S9, "Cardiac tamponade is a clinical diagnosis supported by:", "FAST/eFAST", ["MRI", "CXR only", "ECG only"])
q(432, S9, "FAST in cardiac tamponade shows:", "Hypoechoic collection in subxiphoid (cardiac window)", ["Hyperechoic collection", "Pleural fluid only", "Free air"])
q(432, S9, "Definitive mx of traumatic cardiac tamponade:", "Left anterolateral thoracotomy/sternotomy + evacuation of haematoma & myocardial repair + pericardial drain", ["Pericardiocentesis", "Observation", "Chest tube only"])
q(433, S9, "Role of pericardiocentesis in traumatic cardiac tamponade:", "No role", ["First line", "Definitive", "Preferred in children"])

# ------------------------------------------------------------------ p433
S10 = "Traumatic Thoracic Aortic Injury (TTAI)"
q(433, S10, "The m/c site of traumatic thoracic aortic injury is:", "Distal to ligamentum arteriosum", ["Proximal to left subclavian", "At the diaphragm", "Abdominal aorta"])
q(433, S10, "Clinical features of TTAI include:", "Chest pain, BP difference b/w 2 limbs & absent pulsations in one limb", ["Abdominal pain & hematuria", "Dysphagia & hoarseness only", "Fever & cough"])
q(433, S10, "The screening Ix of TTAI is:", "Chest X-ray", ["CT angio", "Aortography", "MRI"])
q(433, S10, "IOC of TTAI in a STABLE patient:", "CT angiography", ["Transesophageal echo", "CXR", "Angiography"])
q(433, S10, "IOC of TTAI in an UNSTABLE patient:", "Transesophageal ECHO", ["CT angiography", "Aortography", "MRI"])
q(433, S10, "CXR findings of TTAI:", "Widened mediastinum & ↓(Lt) main stem bronchus", ["Narrow mediastinum & ↑Lt bronchus", "Pleural effusion only", "Normal CXR in all"])
q(433, S10, "First line drug mx of TTAI:", "Short acting β blocker (Esmolol)", ["Vasopressor", "Long acting β blocker", "CCB"])
q(433, S10, "The goal of drug mx in TTAI is:", "Permissive hypotension (MAP: 60-70 mmHg)", ["Normal BP 120/80", "MAP > 100 mmHg", "Tachycardia"])
q(433, S10, "Definitive mx of TTAI:", "Graft repair — open or endovascular", ["Balloon only", "Medical mx alone", "Observation"])

# ------------------------------------------------------------------ p433
S11 = "Sternal Fractures"
q(433, S11, "Sternal fracture occurs 2° to high velocity impact and one should suspect:", "Myocardial contusion", ["Aortic injury", "Tracheal injury", "Esophageal injury"])
q(433, S11, "Monitoring done in sternal fracture:", "Cardiac enzymes & 12 lead ECG", ["Serial CXR", "Cardiac MRI", "Troponin only"])
q(433, S11, "Surgical intervention in isolated sternal fracture:", "Not required", ["Always needed", "Plating in all", "Wiring in all"])

# ------------------------------------------------------------------ p433-434
S12 = "Diaphragmatic Injuries"
q(433, S12, "Diaphragmatic injury site:", "Left > Right (right is protected by liver)", ["Right > Left", "Equal bilaterally", "Always central"])
q(434, S12, "Etiology of diaphragmatic injury:", "Penetrating trauma > blunt abdominal trauma", ["Blunt > penetrating", "Only iatrogenic", "Only blast"])
q(434, S12, "Clinical features of diaphragmatic injury:", "Breathlessness & bowel sounds heard in thoracic cavity", ["Bowel sounds in flank", "Hematemesis", "Constipation"])
q(434, S12, "What is NEVER done in diaphragmatic injury?", "Insert intercostal tube blindly", ["Repair with prolene", "Do laparotomy", "Insert chest tube under vision"])
q(434, S12, "Mx sequence of diaphragmatic injury:", "Laparotomy → bring down bowel → repair diaphragm with prolene sutures → insert chest tube under vision", ["Chest tube first → thoracotomy", "Observation", "Thoracoscopy repair"])

# ------------------------------------------------------------------ p434
S13 = "Neck Trauma: Zones and Hard Signs"
q(434, S13, "Zone I of neck trauma extends from:", "Thoracic inlet to cricoid cartilage", ["Cricoid to angle of mandible", "Angle of mandible to base of skull", "Clavicle to thyroid"])
q(434, S13, "Feature of Zone I neck trauma:", "Max mortality (d/t vital structures)", ["Most exposed", "M/c injured", "Most accessible"])
q(434, S13, "Intervention for Zone I neck trauma:", "Angiography & embolization", ["Conservative only", "Surgical exploration always", "Observation"])
q(434, S13, "Zone II of neck trauma extends from:", "Cricoid cartilage to angle of mandible", ["Thoracic inlet to cricoid", "Angle of mandible to skull base", "Hyoid to thyroid"])
q(434, S13, "Zone II of neck trauma is:", "Most exposed, m/c injured & most surgically accessible", ["Least accessible", "Max mortality", "Never explored"])
q(434, S13, "Majority of Zone II neck injuries are managed:", "Conservatively", ["By mandatory exploration", "By embolization", "By radiotherapy"])
q(434, S13, "Zone III of neck trauma extends from:", "Angle of mandible to base of skull", ["Cricoid to mandible", "Inlet to cricoid", "Mandible to orbit"])
q(434, S13, "Intervention for Zone III neck trauma:", "Angiography & embolization", ["Conservative only", "Sternotomy", "Tracheostomy"])
q(434, S13, "Hard signs of neck trauma (indications for intervention) include:", "Subcutaneous emphysema, air bubbling from wound, expanding haematoma & hoarseness", ["Small contusion", "Mild pain", "Fever"])
q(434, S13, "The image of neck zones labels the cricoid cartilage at the boundary between:", "Zone I and Zone II", ["Zone II and III", "Zone III and skull", "Zones I and III"])

# ------------------------------------------------------------------ units
UNIT_DEFS = [
    (S1, "Thoracic trauma is m/c in polytrauma: blunt deaths come from tracheobronchial injury, penetrating deaths from hemothorax 2° to pulmonary laceration. The 1° survey hunts airway obstruction, tracheobronchial injury, tension/open pneumothorax, massive hemothorax, tamponade and traumatic circulatory arrest. Ix is CXR (AP view) → eFAST → pulse oximetry, and the majority is managed conservatively with chest tubes."),
    (S2, "Rib fracture is the m/c thoracic trauma: CPR cracks the 3-5th ribs while high-velocity impact breaks the 1st (lung apex, brachial plexus, subclavian vessels) and floating 10-12th ribs — left means spleen, right means liver. Anterior ribs sit away from the midline and run oblique; posterior ribs sit close to the midline and run horizontal. Adults fracture; pliable children's ribs spare bone and hammer the underlying organs; mx is adequate analgesia."),
    (S3, "Flail chest = ≥2 consecutive ribs fractured at ≥2 places; the hidden killer is the underlying pulmonary contusion. The segment falls in on inspiration and balloons out on expiration — paradoxical movement. Mx climbs from O2 + thoracic epidural analgesia to IPPV (internal splinting) when RR > 30/min or pO2 < 60 mmHg, and on to surgical fixation if those thresholds persist."),
    (S4, "Pneumothorax is air in the pleural space: simple leaves hemodynamics untouched, tension alters them. Tension follows tracheobronchial injury, a large air-leaking pulmonary laceration or an open chest wound that sucks air through a one-way valve. The lung collapses (opposite lung hyperinflates), then the trachea shifts across and the heart gets compressed."),
    (S5, "Tension pneumothorax is a bedside diagnosis — tachypnea, tachycardia, ↓SBP, ↓CO and ↑JVP. Versus tamponade (absent breath sounds + hyperresonance here; normal chest + muffled sounds there) and hemothorax (dull note), CXR and loss of the seashore/barcode/stratosphere sign on eFAST confirm. Decompress first with needle thoracocentesis (adults 5th ICS mid-axillary; children 2nd ICS mid-clavicular), then a triangle-of-safety chest tube; an open wound gets a 3-sided occlusive dressing."),
    (S6, "Hemothorax is blood in the pleural space, usually from torn intercostal vessels — dull percussion, absent breath sounds, CXR showing air-fluid level, white-out and blunted costophrenic angle; drain via triangle of safety. Emergency anterolateral thoracotomy is for >1-1.5 L immediately, >200 cc/hr × ≥3 h, aortic, tracheobronchial/esophageal injury, or tamponade. ER thoracotomy is obsolete — open cardiac massage contaminates the wound and mortality is high."),
    (S7, "The chest tube enters the triangle of safety — apex at the axilla, posterior edge mid-axillary line, anterior edge the pec-major-formed anterior axillary line, base the 5th ICS — riding the upper border of the lower rib to dodge the neurovascular bundle. Skin, superficial and deep fascia, serratus anterior, the three intercostal muscle layers, endothoracic fascia and parietal pleura all get anesthetized. The underwater seal's water stops air being sucked in on inspiration, and the swinging water column proves the drain works."),
    (S8, "Tube position is read off a chest X-ray — a break in the radio-opaque line means it is correctly placed; films also expose anterior and intrapleural misplacements. Pull the tube once the lung is expanded (CXR + normal breath sounds) and output is <100 cc/24 h. The moment of removal is peak inspiration with the patient holding their breath, so no air sneaks in."),
    (S9, "Cardiac tamponade is rapid pericardial blood — as little as 60-70 cc — with penetrating trauma far outstripping blunt. Beck's triad (hypotension, raised JVP, muffled heart sounds) mimics tension pneumothorax with cyanosis, tachycardia and agitation; FAST shows a hypoechoic subxiphoid collection. Definitive care is left anterolateral thoracotomy or sternotomy with clot evacuation, myocardial repair and a pericardial drain — pericardiocentesis has no role in traumatic tamponade."),
    (S10, "Traumatic thoracic aortic injury tears most often just distal to the ligamentum arteriosum; chest pain, inter-limb BP difference or a pulseless limb are the clues. CXR screens (widened mediastinum, descended left main bronchus); stable patients go to CT angio, unstable ones to transesophageal echo. Esmolol (short-acting β blocker) titrates to permissive hypotension (MAP 60-70 mmHg) before open or endovascular graft repair."),
    (S11, "A sternal fracture means high-velocity impact — suspect myocardial contusion underneath. Watch with cardiac enzymes and a 12-lead ECG; the bone itself needs no surgery."),
    (S12, "The diaphragm tears more often on the left — the liver shields the right — and penetrating trauma beats blunt as the cause. Breathlessness plus bowel sounds in the chest gives it away. Never insert an intercostal tube blindly: do a laparotomy, bring the bowel down, repair with prolene and place the chest tube under vision."),
    (S13, "Neck trauma has three zones: I (thoracic inlet→cricoid) kills most — angiography & embolization; II (cricoid→angle of mandible) is most exposed, most injured and most accessible — usually conservative or exploration; III (mandible angle→skull base) again gets angiography & embolization. Hard signs — subcutaneous emphysema, air bubbling from the wound, an expanding haematoma, hoarseness — are the indications to intervene."),
]

first_page = {}
for x in Q:
    first_page.setdefault(x["sec"], x["page"])

UNITS = []
for i, (title, guide) in enumerate(UNIT_DEFS, 1):
    UNITS.append({
        "id": f"SURG-U56-{i}",
        "ch": 56,
        "n": i,
        "title": title,
        "sec": f"{title} · p{first_page[title]}",
        "qs": [x["id"] for x in Q if x["sec"] == title],
        "guide": guide,
    })

covered = [x for u in UNITS for x in u["qs"]]
assert covered == [x["id"] for x in Q]
assert len(set(covered)) == len(covered)
with open("data/ch56.json", "w", encoding="utf-8") as f:
    json.dump({"questions": Q, "units": UNITS}, f, ensure_ascii=False, indent=1)
print(f"ch56: {len(Q)} questions, {len(UNITS)} units")
