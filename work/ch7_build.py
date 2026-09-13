#!/usr/bin/env python3
"""Build data/ch7.json for PULSE Surgery ch7 (Shock : Part 1, book p37-43)."""
import json

Q = []
def q(page, sec, text, opts, ans, exp):
    Q.append({"id": f"SURG-C7-{len(Q)+1:03d}", "sec": sec, "page": page,
              "q": text, "opts": opts, "ans": ans, "exp": exp})

# ---------------- p37 · HYPOVOLEMIC/HEMORRHAGIC SHOCK: TYPES ----------------
q(37, "Hypovolemic Shock: Types", "The m/c type of shock is:",
  ["Hypovolemic/hemorrhagic shock", "Cardiogenic shock", "Septic shock", "Neurogenic shock"], 0,
  "Hypovolemic/Hemorrhagic Shock: m/c type of shock. (Book p37)")
q(37, "Hypovolemic Shock: Types", "Overt/visible hemorrhage is:",
  ["Easy to diagnose and treat", "Difficult to diagnose", "Always concealed", "Seen only in pelvis"], 0,
  "Overt/visible hemorrhage: Easy to diagnose and treat. (Book p37)")
q(37, "Hypovolemic Shock: Types", "Concealed hemorrhage is:",
  ["Difficult to diagnose", "Easy to diagnose", "Always visible externally", "Never causes shock"], 0,
  "Concealed hemorrhage: Difficult to diagnose. (Book p37)")
q(37, "Hypovolemic Shock: Types", "Sites of concealed hemorrhage include all of the following EXCEPT:",
  ["Neck", "Thorax", "Abdomen", "Skin surface"], 3,
  "Concealed hemorrhage site: Neck/thorax/abdomen/pelvis/long bones. (Book p37)")
q(37, "Hypovolemic Shock: Types", "Which injury does NOT give rise to hypovolemic shock?",
  ["Isolated head injury", "Pelvic fracture", "Long bone fracture", "Massive hemothorax"], 0,
  "Note: Isolated head injury doesn't give rise to hypovolemic shock. (Book p37)")
q(37, "Hypovolemic Shock: Types", "Hypotension in a head injury patient makes you suspect all of the following EXCEPT:",
  ["Hypovolemic shock from the head injury itself", "Brain herniation", "Neurogenic shock", "Polytrauma"], 0,
  "Hypotension in head injury, suspect: Brain herniation, Neurogenic shock, Polytrauma (not the isolated head injury itself). (Book p37)")
q(37, "Hypovolemic Shock: Types", "Neurogenic shock causing hypotension in head injury occurs with injury above which level?",
  ["T6 level", "T10 level", "L1 level", "C7 level only"], 0,
  "Neurogenic shock (Injury above T6 level). (Book p37)")

# ---------------- p37 · ARTERIAL VS VENOUS BLEED ----------------
q(37, "Arterial vs Venous Bleed", "An arterial bleed characteristically:",
  ["Spurts", "Oozes gradually", "Never causes hypotension", "Stops always on its own"], 0,
  "Arterial vs venous bleed: Bleed: Arterial = Spurter. (Book p37)")
q(37, "Arterial vs Venous Bleed", "A venous bleed characteristically:",
  ["Gradual ooze of blood", "Spurts", "Causes early hypotension", "Needs early prevention"], 0,
  "Arterial vs venous bleed: Bleed: Venous = Gradual ooze of blood. (Book p37)")
q(37, "Arterial vs Venous Bleed", "Hypotension in arterial bleed occurs:",
  ["Early", "Late due to compensation", "Never", "Only after 24 hours"], 0,
  "Arterial vs venous bleed: Hypotension: Arterial = Occurs early. (Book p37)")
q(37, "Arterial vs Venous Bleed", "Hypotension in venous bleed occurs late because of:",
  ["Compensation", "Vasoconstriction failure", "Early blood loss", "Cardiac failure"], 0,
  "Venous bleed: Hypotension occurs late (d/t compensation). (Book p37)")
q(37, "Arterial vs Venous Bleed", "Types of arterial bleed are:",
  ["Laceration and transection", "Ooze and spurt", "Capillary and venous", "Primary and secondary"], 0,
  "Types of arterial bleed: Laceration, Transection. (Book p37)")
q(37, "Arterial vs Venous Bleed", "In a lacerated artery, vasoconstriction leads to:",
  ["Increase in tear size and more bleeding", "Decreased bleeding", "Complete hemostasis", "Spasm that seals the artery"], 0,
  "Laceration: Vasoconstriction leads to ↑ in tear size -> Bleeds more. (Book p37)")
q(37, "Arterial vs Venous Bleed", "Which arterial bleed bleeds less?",
  ["Transection", "Laceration", "Both equally", "Neither bleeds"], 0,
  "Transection: Bleeds less. (Book p37)")

# ---------------- p38 · HEMORRHAGE IN SURGERY ----------------
q(38, "Hemorrhage in Surgery", "Primary hemorrhage occurs:",
  ["During Sx", "Within 24 hours", "After 7-14 days", "After 1 month"], 0,
  "1° hemorrhage: Occurs during Sx. (Book p38)")
q(38, "Hemorrhage in Surgery", "Reactionary hemorrhage occurs:",
  ["Within 24 hours", "During Sx", "After 7-14 days", "After 48 hours"], 0,
  "Reactionary hemorrhage: Within 24 hours. (Book p38)")
q(38, "Hemorrhage in Surgery", "The reasons for reactionary hemorrhage are:",
  ["Dislodgement of clot and slippage of knot (Granny's knot)", "Infection of the wound", "Sloughing of the vessel wall", "Hypertension"], 0,
  "Reactionary hemorrhage reason: Dislodgement of clot; Slippage of knot (Granny's knot). (Book p38)")
q(38, "Hemorrhage in Surgery", "Secondary hemorrhage occurs:",
  ["After 7-14 days", "Within 24 hours", "During Sx", "On day 2"], 0,
  "2° hemorrhage: After 7-14 days. (Book p38)")
q(38, "Hemorrhage in Surgery", "The reason for secondary hemorrhage is:",
  ["Sloughing of wall due to infection", "Slippage of knot", "Dislodgement of clot", "Trauma"], 0,
  "2° hemorrhage: Sloughing of wall d/t infection. (Book p38)")

# ---------------- p38 · CLASSIFICATION OF HYPOVOLEMIC SHOCK ----------------
q(38, "Classification of Hypovolemic Shock", "Class I hypovolemic shock corresponds to blood loss of:",
  ["0-15% (0.5 litre)", "15-30% (1 litre)", "30-40% (1.5 litre)", ">40% (>2 litres)"], 0,
  "Class I: 0-15%, 0.5 litre. (Book p38)")
q(38, "Classification of Hypovolemic Shock", "Class II (mild) hypovolemic shock corresponds to blood loss of:",
  ["15-30% (1 litre)", "0-15% (0.5 litre)", "30-40% (1.5 litre)", ">40% (>2 litres)"], 0,
  "Class II (Mild): 15-30%, 1 litre. (Book p38)")
q(38, "Classification of Hypovolemic Shock", "Class III (moderate) hypovolemic shock corresponds to blood loss of:",
  ["30-40% (1.5 litre)", "15-30% (1 litre)", ">40% (>2 litres)", "0-15% (0.5 litre)"], 0,
  "Class III (Moderate): 30-40%, 1.5 litre. (Book p38)")
q(38, "Classification of Hypovolemic Shock", "Class IV (severe) hypovolemic shock corresponds to blood loss of:",
  [">40% (>2 litres)", "30-40% (1.5 litre)", "15-30% (1 litre)", "20-25% (1 litre)"], 0,
  "Class IV (Severe): >40%, >2 litres. (Book p38)")
q(38, "Classification of Hypovolemic Shock", "Heart rate in Class IV shock is:",
  ["Non-recordable", "Normal", "Mildly raised", "Raised"], 0,
  "Class IV: Heart rate non-recordable. (Book p38)")
q(38, "Classification of Hypovolemic Shock", "Blood pressure begins to fall (SBP ↓↓) from which class?",
  ["Class III", "Class I", "Class II", "Only Class IV"], 0,
  "BP: Class I & II normal; Class III SBP ↓↓; Class IV non-recordable. (Book p38)")
q(38, "Classification of Hypovolemic Shock", "Pulse pressure (SBP-DBP) becomes narrow in Class II and narrower in Class III; in Class IV it is:",
  ["Decreased (↓)", "Normal", "Wide", "Unchanged"], 0,
  "Pulse pressure: Normal, Narrow, Narrower, ↓ (Class IV). (Book p38)")
q(38, "Classification of Hypovolemic Shock", "Respiratory rate is ↑↑ (double up arrow) in which class?",
  ["Class IV", "Class II", "Class I", "Class III"], 0,
  "Respiratory rate: Class III ↑; Class IV ↑↑. (Book p38)")
q(38, "Classification of Hypovolemic Shock", "Urine output in Class III and Class IV shock respectively is:",
  ["↓↓ and anuria", "Normal and ↓", "Anuria and ↓↓", "Normal and normal"], 0,
  "Urine output: Class III ↓↓; Class IV anuria. (Book p38)")
q(38, "Classification of Hypovolemic Shock", "Mental status in Class II shock is:",
  ["Anxious, thirsty", "Confused", "Coma", "Normal"], 0,
  "Mental status: Class II anxious, thirsty. (Book p38)")
q(38, "Classification of Hypovolemic Shock", "Mental status in Class III and Class IV shock respectively is:",
  ["Confused and coma", "Anxious and confused", "Coma and confused", "Normal and confused"], 0,
  "Mental status: Class III confused; Class IV coma. (Book p38)")
q(38, "Classification of Hypovolemic Shock", "Base deficit in Class II shock is:",
  ["-2 to -6 mEq/L", "Normal", "-6 to -10 mEq/L", ">-10 mEq/L"], 0,
  "Base deficit: Class II -2 to -6 mEq/L. (Book p38)")
q(38, "Classification of Hypovolemic Shock", "Base deficit >-10 mEq/L corresponds to:",
  ["Class IV", "Class I", "Class II", "Class III"], 0,
  "Base deficit: Class IV >-10 mEq/L. (Book p38)")
q(38, "Classification of Hypovolemic Shock", "Fluid replacement for Class I and Class II shock respectively is:",
  ["Oral liquids and IV crystalloids", "IV crystalloids and colloids", "Massive transfusion and oral liquids", "IV colloids only"], 0,
  "Fluid replacement: Class I oral liquids; Class II IV crystalloids. (Book p38)")
q(38, "Classification of Hypovolemic Shock", "Fluid replacement for Class III shock is:",
  ["IV crystalloids + colloid", "Oral liquids", "IV crystalloids only", "Massive blood transfusion"], 0,
  "Fluid replacement: Class III IV crystalloids + colloid. (Book p38)")
q(38, "Classification of Hypovolemic Shock", "Massive blood transfusion is the fluid replacement for:",
  ["Class IV", "Class I", "Class II", "Class III"], 0,
  "Fluid replacement: Class IV massive blood transfusion. (Book p38)")
q(38, "Classification of Hypovolemic Shock", "Class III shock is the:",
  ["Decompensated phase", "Compensated phase", "Pre-shock phase", "Recovery phase"], 0,
  "Class III: Decompensated phase. (Book p38)")
q(38, "Classification of Hypovolemic Shock", "In Class III shock:",
  ["SBP starts falling and the patient is confused", "SBP is normal and patient anxious", "BP is non-recordable", "Urine output is normal"], 0,
  "Class III: SBP starts falling; Confused patient. (Book p38)")

# ---------------- p38 · PATHOPHYSIOLOGY OF CLASS II SHOCK & RESPONSE ----------------
q(38, "Pathophysiology & Response", "Class II shock is also known as:",
  ["Compensated shock", "Decompensated shock", "Irreversible shock", "Septic shock"], 0,
  "Pathophysiology of Class II shock: AKA compensated shock. (Book p38)")
q(38, "Pathophysiology & Response", "Blood loss activates the sympathetic system releasing:",
  ["Noradrenaline, adrenaline", "Insulin", "Histamine", "Acetylcholine"], 0,
  "Blood loss -> Activation of sympathetic system -> Noradrenaline, Adrenaline. (Book p38)")
q(38, "Pathophysiology & Response", "The earliest sign of Class II (compensated) shock is:",
  ["Tachycardia (↑ HR)", "Hypotension", "Anuria", "Coma"], 0,
  "Tachycardia: ↑ HR (Earliest sign). (Book p38)")
q(38, "Pathophysiology & Response", "Peripheral vasoconstriction in compensated shock serves to:",
  ["Shunt blood to vital organs", "Increase skin temperature", "Cause bleeding", "Lower peripheral vascular resistance"], 0,
  "Peripheral vasoconstriction (Shunts blood to vital organs). (Book p38)")
q(38, "Pathophysiology & Response", "Clinical features of the compensated phase include cold extremities and:",
  ["↑ peripheral vascular resistance", "↓ peripheral vascular resistance", "Warm flushed skin", "Bradycardia"], 0,
  "Cold extremities; ↑ peripheral vascular resistance. (Book p38)")
q(38, "Pathophysiology & Response", "To check the response in shock, one gives:",
  ["500 mL-1 L crystalloid and checks response", "2 L colloid bolus", "Oral fluids only", "Blood immediately always"], 0,
  "Response and management of shock: 500 mL-1 L crystalloid given -> Response checked. (Book p38)")

# ---------------- p39 · DYNAMIC FLUID RESPONSE ----------------
q(39, "Dynamic Fluid Response", "In a responder, pulse rate, SBP and JVP show:",
  ["PR ↓↓, SBP ↑↑, JVP ↑↑ with persistent changes", "PR ↑, SBP ↓, JVP ↓", "No change at all", "Changes that reverse within 5 minutes"], 0,
  "Responder: PR ↓↓, SBP ↑↑, JVP ↑↑; the above changes are persistent. (Book p39)")
q(39, "Dynamic Fluid Response", "A transient responder shows improvement but after 15-20 minutes:",
  ["Parameters worsen (ongoing losses)", "Parameters stay normal forever", "PR falls to zero", "JVP becomes non-recordable"], 0,
  "Transient responder: After 15-20 mins parameters worsen (Ongoing losses). (Book p39)")
q(39, "Dynamic Fluid Response", "In a non responder, PR, SBP and JVP respectively:",
  ["↑, ↓, ↓", "↓↓, ↑↑, ↑↑", "Normal, normal, normal", "↓, ↑, ↑"], 0,
  "Non responder: PR ↑, SBP ↓, JVP ↓. (Book p39)")
q(39, "Dynamic Fluid Response", "A non responder implies:",
  ["Ongoing losses", "Complete hemostasis", "Over-transfusion", "Compensated shock"], 0,
  "Non responder: Implication = Ongoing losses. (Book p39)")

# ---------------- p39 · MANAGEMENT: RESUSCITATION STRATEGIES ----------------
q(39, "Management: Resuscitation", "Active bleeding is recognised by:",
  ["Hypotension and transient/non-responder status", "Normal BP and responder status", "Fever", "Bradycardia"], 0,
  "Recognise active bleeding: Hypotension, transient/non-responder. (Book p39)")
q(39, "Management: Resuscitation", "Before hemostasis, resuscitation prioritises:",
  ["Coagulation", "Perfusion", "Diuresis", "Sedation"], 0,
  "Before hemostasis: Prioritise coagulation. (Book p39)")
q(39, "Management: Resuscitation", "After hemostasis, resuscitation prioritises:",
  ["Perfusion", "Coagulation", "Hypothermia", "Hemoconcentration"], 0,
  "After hemostasis: Prioritise perfusion. (Book p39)")
q(39, "Management: Resuscitation", "Damage control resuscitation is used in:",
  ["Active bleeding (hypotension, transient/non-responder)", "Stable responders", "Elective surgery", "Anaemia only"], 0,
  "Recognise active bleeding -> Damage control resuscitation. (Book p39)")
q(39, "Management: Resuscitation", "The goal of damage control resuscitation is:",
  ["Coagulation function and coronary perfusion", "End-organ perfusion", "Normalisation of Hb", "Full blood pressure immediately"], 0,
  "Damage control resuscitation goal: Coagulation function, coronary perfusion. (Book p39)")
q(39, "Management: Resuscitation", "Damage control resuscitation includes all of the following EXCEPT:",
  ["Permissive hypertension", "Damage control surgery", "Balanced transfusion (1:1 RBC and FFP)", "Treating coagulopathy with tranexamic acid, platelets, fibrinogen"], 0,
  "DCR: Damage control surgery; Permissive hypotension (keep BP at lower limit of normal); Balanced transfusion (1:1 RBC and FFP); Treat coagulopathy (Tranexamic acid, platelets, fibrinogen). (Book p39)")
q(39, "Management: Resuscitation", "Permissive hypotension means keeping the BP at:",
  ["The lower limit of normal", "The upper limit of normal", "Above 140 mmHg", "Zero"], 0,
  "Permissive hypotension (keep BP at lower limit of normal). (Book p39)")
q(39, "Management: Resuscitation", "Balanced transfusion in damage control resuscitation uses RBC and FFP in the ratio:",
  ["1:1", "2:1", "4:1", "1:4"], 0,
  "Balanced transfusion (1:1 RBC and FFP). (Book p39)")
q(39, "Management: Resuscitation", "Coagulopathy in damage control resuscitation is treated with:",
  ["Tranexamic acid, platelets, fibrinogen", "Heparin", "Warfarin", "Vitamin K only"], 0,
  "Treat coagulopathy (Tranexamic acid, platelets, fibrinogen). (Book p39)")
q(39, "Management: Resuscitation", "Monitoring in damage control resuscitation includes coagulation parameters:",
  ["PT, fibrinogen, ROTEM/TEG", "Only Hb", "Only platelet count", "Bleeding time only"], 0,
  "DCR monitor: Coagulation: PT, fibrinogen, ROTEM/TEG. (Book p39)")
q(39, "Management: Resuscitation", "Monitoring in damage control resuscitation includes electrolytes:",
  ["Ca2+, K+", "Na+ only", "Mg2+ only", "Phosphate only"], 0,
  "DCR monitor: Electrolytes: Ca2+, K+. (Book p39)")
q(39, "Management: Resuscitation", "Perfusion monitoring in damage control resuscitation uses:",
  ["pH, base excess, lactate, temperature", "Urine culture", "CXR", "GCS only"], 0,
  "DCR monitor: Perfusion: pH, base excess, lactate, temperature. (Book p39)")
q(39, "Management: Resuscitation", "A responder after hemostasis receives:",
  ["Perfusion-targeted resuscitation", "Damage control resuscitation", "No fluids ever", "Only colloids"], 0,
  "Responder -> Perfusion-targeted resuscitation. (Book p39)")
q(39, "Management: Resuscitation", "The goal of perfusion-targeted resuscitation is:",
  ["End-organ perfusion", "Coagulation function", "Hypothermia", "Hemoconcentration"], 0,
  "Perfusion-targeted resuscitation goal: End-organ perfusion. (Book p39)")
q(39, "Management: Resuscitation", "Perfusion-targeted resuscitation ensures adequate preload and afterload using:",
  ["Fluids and pressors", "Diuretics", "Beta blockers", "Sedatives"], 0,
  "Adequate preload and afterload (Fluids and pressors). (Book p39)")
q(39, "Management: Resuscitation", "Perfusion-targeted resuscitation also includes:",
  ["Thromboprophylaxis", "Anticoagulation avoidance always", "Routine FFP", "Permissive hypotension"], 0,
  "Perfusion-targeted resuscitation: Thromboprophylaxis. (Book p39)")
q(39, "Management: Resuscitation", "Cardiovascular monitoring in perfusion-targeted resuscitation includes:",
  ["BP, HR, CO, SVR", "BP and HR only", "JVP only", "ECG only"], 0,
  "PTR monitor: Cardiovascular: BP, HR, CO, SVR. (Book p39)")
q(39, "Management: Resuscitation", "Perfusion monitoring in perfusion-targeted resuscitation includes:",
  ["Base excess, lactate, SvO2", "Only temperature", "Only pH", "Hb only"], 0,
  "PTR monitor: Perfusion: Base excess, lactate, SvO2. (Book p39)")
q(39, "Management: Resuscitation", "Organ function monitoring in perfusion-targeted resuscitation includes:",
  ["PaO2/FiO2, UO, GCS", "Only GCS", "Only urine output", "Liver biopsy"], 0,
  "PTR monitor: Organ function: PaO2/FiO2, UO, GCS. (Book p39)")
q(39, "Management: Resuscitation", "The abdominal compartment is monitored in perfusion-targeted resuscitation by:",
  ["IAP (intra abdominal pressure)", "UO", "SvO2", "CO"], 0,
  "PTR monitor: Abdominal compartment: IAP. (Book p39)")
q(39, "Management: Resuscitation", "ROTEM and TEG stand for:",
  ["Rotational thromboelastometry and thromboelastography", "Rotational thromboembolism test and tissue elastography", "Routine thrombin estimation and tissue coagulography", "Rotational temperature estimation and thrombin elasticity graph"], 0,
  "ROTEM: Rotational thromboelastometry; TEG: Thromboelastography. (Book p39)")

# ---------------- p40 · OCCULT HYPOPERFUSION & MONITORING INDICATORS ----------------
q(40, "Occult Hypoperfusion", "Occult hypoperfusion shows CVS parameters (HR, SBP) that are:",
  ["Normal", "Grossly deranged", "Non-recordable", "High"], 0,
  "Occult hypoperfusion: Normal CVS parameters: HR, SBP normal. (Book p40)")
q(40, "Occult Hypoperfusion", "Urine output in occult hypoperfusion is:",
  ["Normal", "Absent", "Decreased", "Increased"], 0,
  "Occult hypoperfusion: Normal urine output. (Book p40)")
q(40, "Occult Hypoperfusion", "Occult hypoperfusion is revealed by:",
  ["Low MVOS (mixed venous oxygen saturation) and acidosis", "High MVOS and alkalosis", "Normal lactate", "Normal base excess"], 0,
  "Occult hypoperfusion: Low MVOS (mixed venous oxygen saturation); Acidosis. (Book p40)")
q(40, "Monitoring Indicators", "The best indicator of initial fluid requirement is:",
  ["PCWP > CVP", "CVP > PCWP", "Urine output", "Shock index"], 0,
  "Initial fluid requirement: Best indicator: PCWP > CVP. (Book p40)")
q(40, "Monitoring Indicators", "PCWP stands for and reflects:",
  ["Pulmonary capillary wedge pressure; left-sided heart pressure (more accurate)", "Peripheral central wedge pressure; right heart", "Pulmonary circulatory wedge pressure; RV pressure", "Peak capillary wedge pressure; skin perfusion"], 0,
  "PCWP: (Pulmonary capillary wedge pressure); Left-sided heart pressure (more accurate). (Book p40)")
q(40, "Monitoring Indicators", "PCWP is measured using a:",
  ["Swan-Ganz catheter", "Foley catheter", "PICC line", "Arterial line only"], 0,
  "PCWP: Swan-Ganz catheter used. (Book p40)")
q(40, "Monitoring Indicators", "The drawback of PCWP monitoring is that it is:",
  ["Difficult to monitor", "Inaccurate for left heart", "Non-invasive", "Cheapest"], 0,
  "PCWP: Difficult to monitor. (Book p40)")
q(40, "Monitoring Indicators", "CVP reflects:",
  ["Right-sided heart pressure and is m/c used", "Left-sided heart pressure", "Pulmonary artery pressure only", "Portal pressure"], 0,
  "CVP: (Central venous pressure); Right-sided heart pressure; m/c used. (Book p40)")
q(40, "Monitoring Indicators", "The best indicator of fluid resuscitation is:",
  ["Urine output", "CVP", "PCWP", "Heart rate"], 0,
  "Fluid resuscitation: Best indicator: Urine output. (Book p40)")
q(40, "Monitoring Indicators", "Urine output target in adults during resuscitation is:",
  [">0.5 mL/kg/hour", ">1 mL/kg/hour", ">2 mL/kg/hour", ">0.1 mL/kg/hour"], 0,
  "Urine output: Adults: >0.5 mL/kg/hour. (Book p40)")
q(40, "Monitoring Indicators", "Urine output target in children during resuscitation is:",
  [">1 mL/kg/hour", ">0.5 mL/kg/hour", ">0.25 mL/kg/hour", ">3 mL/kg/hour"], 0,
  "Urine output: Children: >1 mL/kg/hour. (Book p40)")

# ---------------- p40-41 · INDICES ----------------
q(40, "Indices", "Shock index is calculated as:",
  ["Heart rate (HR) / Systolic BP (SBP)", "SBP / HR", "HR / DBP", "MAP / HR"], 0,
  "Shock Index: Heart rate (HR)/Systolic BP (SBP). (Book p40)")
q(40, "Indices", "A shock index >0.9 indicates:",
  ["Higher mortality rate", "Stable patient", "Compensated shock", "Normal perfusion"], 0,
  "Shock index >0.9: Higher mortality rate. (Book p40)")
q(40, "Indices", "Modified shock index is calculated as:",
  ["HR / MAP (mean arterial pressure)", "HR / SBP", "HR / PP", "MAP / HR"], 0,
  "Modified shock index: HR/MAP (mean arterial pressure). (Book p40)")
q(40, "Indices", "The most sensitive shock index is the:",
  ["Modified shock index", "Shock index", "ROPE", "CVP"], 0,
  "Modified shock index: most sensitive. (Book p40)")
q(41, "Indices", "Rate over pressure evaluation (ROPE) is calculated as:",
  ["HR / PP (pulse pressure)", "HR / SBP", "HR / MAP", "PP / HR"], 0,
  "ROPE: HR/PP (Pulse pressure). (Book p41)")
q(41, "Indices", "A ROPE value <3 indicates:",
  ["Stable patient", "Decompensated shock", "High mortality", "Ongoing bleeding"], 0,
  "ROPE <3: Stable patient. (Book p41)")
q(41, "Indices", "A ROPE value >3 indicates the patient:",
  ["May develop decompensated shock", "Is stable", "Needs no monitoring", "Is a responder"], 0,
  "ROPE >3: May develop decompensated shock. (Book p41)")

# ---------------- p41 · MONITORS FOR ORGAN/SYSTEMIC PERFUSION ----------------
q(41, "Monitors for Organ/Systemic Perfusion", "Systemic perfusion is investigated by base deficit and lactate, which are:",
  ["Signs of acidosis", "Signs of alkalosis", "Signs of infection", "Signs of anemia"], 0,
  "Systemic perfusion investigations: Base deficit, Lactate = Signs of acidosis. (Book p41)")
q(41, "Monitors for Organ/Systemic Perfusion", "The best end point of resuscitation is:",
  ["Mixed venous oxygen saturation (MVOS)", "Urine output", "Heart rate", "CVP"], 0,
  "Mixed venous oxygen saturation (MVOS): Best end point of resuscitation. (Book p41)")
q(41, "Monitors for Organ/Systemic Perfusion", "Muscle perfusion is monitored by:",
  ["Near-infrared spectroscopy and tissue oxygen electrode", "Urine output", "Consciousness level", "Sublingual capnometry"], 0,
  "Muscle: Near-infrared spectroscopy; Tissue oxygen electrode. (Book p41)")
q(41, "Monitors for Organ/Systemic Perfusion", "The tissue most sensitive to hypovolemic insult is the:",
  ["Gut mucosa", "Muscle", "Brain", "Kidney"], 0,
  "Gut mucosa: Most sensitive to hypovolemic insult. (Book p41)")
q(41, "Monitors for Organ/Systemic Perfusion", "Hypovolemic insult to gut mucosa leads to formation of:",
  ["Stress ulcers", "Polyps", "Diverticula", "Villous atrophy"], 0,
  "Gut mucosa: Forms stress ulcers. (Book p41)")
q(41, "Monitors for Organ/Systemic Perfusion", "Gut perfusion is monitored by:",
  ["Sublingual capnometry, gut mucosal pH, laser doppler flowmetry", "Urine output", "NIRS only", "Consciousness level"], 0,
  "Gut: Sublingual capnometry; Gut mucosal pH; Laser doppler flowmetry. (Book p41)")
q(41, "Monitors for Organ/Systemic Perfusion", "Kidney perfusion is monitored clinically by:",
  ["Urine output", "Consciousness level", "Base deficit", "Laser doppler"], 0,
  "Kidney: Clinical = Urine output. (Book p41)")
q(41, "Monitors for Organ/Systemic Perfusion", "Brain perfusion is monitored clinically by and investigated with:",
  ["Consciousness level; tissue oxygen electrode and NIRS", "Urine output; capnometry", "HR; lactate", "BP; MVOS"], 0,
  "Brain: Clinical = Consciousness level; Investigations = Tissue oxygen electrode, Near-infrared spectroscopy (NIRS). (Book p41)")

# ---------------- p41-42 · MASSIVE BLOOD TRANSFUSION & COMPLICATIONS ----------------
q(41, "Massive Blood Transfusion", "Massive blood transfusion includes any of the following EXCEPT:",
  [">4 units in 24 hours", "Replace entire circulating volume in 24 hrs", ">10 units of blood in 24 hrs", ">4 units in one hour"], 0,
  "Massive blood transfusion: Replace entire circulating volume in 24 hrs; >10 units of blood in 24 hrs; >4 units in one hour. (Book p41)")
q(41, "Massive Blood Transfusion", "The first listed complication of massive transfusion is:",
  ["Hypothermia", "Hyperthermia", "Hypoglycemia", "Hypertension"], 0,
  "Complications: 1. Hypothermia. (Book p41)")
q(41, "Massive Blood Transfusion", "Hypocalcemia/hypomagnesemia in massive transfusion occurs because:",
  ["Citrate (anticoagulant) chelates Ca2+ and Mg2+", "Heparin binds calcium", "Blood is acidic", "Kidneys excrete calcium"], 0,
  "Reason: Citrate (Anticoagulant) -> Chelates Ca2+ and Mg2+. (Book p41)")
q(41, "Massive Blood Transfusion", "Metabolic alkalosis in massive transfusion is due to:",
  ["Citrate toxicity", "Lactic acidosis", "Hypothermia", "Hyperkalemia"], 0,
  "Metabolic alkalosis: Reason: Citrate toxicity. (Book p41)")
q(41, "Massive Blood Transfusion", "The potassium disturbance seen in massive transfusion is:",
  ["Hyperkalemia >> hypokalemia", "Hypokalemia >> hyperkalemia", "Only hypokalemia", "No change"], 0,
  "Hyperkalemia >> hypokalemia. (Book p41)")
q(41, "Massive Blood Transfusion", "Hyperkalemia in massive transfusion occurs because:",
  ["Stored blood -> RBC lysed -> K+ released -> ↑ serum K+", "Citrate releases potassium", "Renal failure always", "Platelet lysis"], 0,
  "Reason: Stored blood -> RBC lysed -> K+ released -> ↑ serum K+. (Book p41)")
q(42, "Massive Blood Transfusion", "The m/c cause of death in massive transfusion is:",
  ["Coagulopathy", "Hypothermia", "Hyperkalemia", "TRALI"], 0,
  "5. Coagulopathy (m/c cause of death). (Book p42)")
q(42, "Massive Blood Transfusion", "Reasons for coagulopathy in massive transfusion include all of the following EXCEPT:",
  ["Hyperthermia", "Dilutional coagulopathy", "Acidosis", "Hypothermia"], 0,
  "Coagulopathy reasons: a. Dilutional coagulopathy; b. Acidosis; c. Hypothermia. (Book p42)")
q(42, "Massive Blood Transfusion", "Prevention of coagulopathy in massive transfusion includes limiting crystalloids and giving PRBC : Platelet : FFP in the ratio:",
  ["1:1:1", "2:1:1", "1:2:4", "4:1:1"], 0,
  "Prevention: Limit crystalloids; PRBC : Platelet : FFP -> 1:1:1 ratio. (Book p42)")
q(42, "Massive Blood Transfusion", "Haemolytic reaction during transfusion is due to:",
  ["Mismatched transfusion", "Citrate toxicity", "Leukocytes", "Iron overload"], 0,
  "Haemolytic reaction: Reason: Mismatched transfusion. (Book p42)")
q(42, "Massive Blood Transfusion", "The m/c transfusion reaction is:",
  ["Febrile reactions", "Haemolytic reaction", "TRALI", "TACO"], 0,
  "Febrile reactions (m/c reaction). (Book p42)")
q(42, "Massive Blood Transfusion", "Febrile transfusion reactions are prevented by using:",
  ["A leukoreduction filter", "Warming blood", "Citrate", "Diuretics"], 0,
  "Prevention: use of a leukoreduction filter. (Book p42)")
q(42, "Massive Blood Transfusion", "TRALI stands for:",
  ["Transfusion related acute lung injury", "Transfusion related acute liver injury", "Transfusion related acute limb ischemia", "Total respiratory and lung insufficiency"], 0,
  "Transfusion related acute lung injury (TRALI). (Book p42)")
q(42, "Massive Blood Transfusion", "TACO stands for:",
  ["Transfusion associated cardiac overload", "Transfusion associated cerebral oedema", "Total acute cardiac occlusion", "Transfusion acidosis and cardiac output fall"], 0,
  "Transfusion associated cardiac overload (TACO). (Book p42)")

# ---------------- p42 · TACO VS TRALI ----------------
q(42, "TACO vs TRALI", "The mechanism of TACO is:",
  ["Cardiac overload", "Antibody against HLA antigen", "Sepsis", "Citrate toxicity"], 0,
  "TACO mechanism: D/t cardiac overload. (Book p42)")
q(42, "TACO vs TRALI", "The mechanism of TRALI is:",
  ["Antibody against HLA antigen causing non-cardiogenic pulmonary edema within 6 hours", "Cardiac overload", "Fluid overload of kidneys", "Bacterial contamination"], 0,
  "TRALI mechanism: Antibody against HLA antigen -> Non-cardiogenic pulmonary edema (within 6 hours). (Book p42)")
q(42, "TACO vs TRALI", "TRALI pulmonary edema appears within:",
  ["6 hours", "24 hours", "48 hours", "1 week"], 0,
  "Non-cardiogenic pulmonary edema (within 6 hours). (Book p42)")
q(42, "TACO vs TRALI", "Implicated donors in TRALI include:",
  ["Multiparous women and patients receiving FFP", "Young male donors", "First-time donors only", "O-negative donors"], 0,
  "TRALI implicated donors: Multiparous women; Patient receiving FFP. (Book p42)")
q(42, "TACO vs TRALI", "Clinical features of TACO include all of the following EXCEPT:",
  ["Patchy infiltrates on X-ray", "Facial puffiness", "Pedal edema", "Breathlessness"], 0,
  "TACO clinical features: Facial puffiness, Pedal edema, Breathlessness, X-ray: Normal. (Book p42)")
q(42, "TACO vs TRALI", "The chest X-ray in TACO is:",
  ["Normal", "ARDS with patchy infiltrates", "Pneumothorax", "Cardiomegaly always"], 0,
  "TACO: X-ray: Normal. (Book p42)")
q(42, "TACO vs TRALI", "TRALI clinically shows breathlessness and on CXR:",
  ["ARDS with pulmonary edema and patchy infiltrates", "Normal film", "Pleural effusion only", "Cardiomegaly"], 0,
  "TRALI: CXR: ARDS (Acute respiratory distress syndrome); Pulmonary edema; Patchy infiltrates. (Book p42)")
q(42, "TACO vs TRALI", "Management of TACO is:",
  ["Lasix/diuretics", "No specific management listed", "Antibiotics", "Intubation always"], 0,
  "TACO management: Lasix/diuretics. (Book p42)")
q(42, "TACO vs TRALI", "Management of TRALI as per the book is:",
  ["- (none listed)", "Lasix/diuretics", "Steroids", "FFP infusion"], 0,
  "TRALI management: - (none listed in table). (Book p42)")

# ---------------- p43 · TRANSFUSION CRITERIA, SUBSTITUTES, GARMENT ----------------
q(43, "Perioperative RBC Transfusion Criteria", "A perioperative hemoglobin <6 g/dL:",
  ["Probably will benefit from transfusion", "Benefits only if ongoing losses", "Not indicated if risk factors absent", "Needs no transfusion"], 0,
  "Hb <6: Probably will benefit from transfusion. (Book p43)")
q(43, "Perioperative RBC Transfusion Criteria", "A perioperative hemoglobin of 6-8 g/dL benefits from transfusion only if:",
  ["Ongoing losses (+)/impending surgery", "Patient is young", "Surgery is minor", "Risk factors absent"], 0,
  "Hb 6-8: Benefit only if ongoing losses (+)/impending surgery. (Book p43)")
q(43, "Perioperative RBC Transfusion Criteria", "A perioperative hemoglobin >8 g/dL:",
  ["Not indicated if risk factors absent", "Always transfuse", "Probably will benefit", "Transfuse only before surgery"], 0,
  "Hb >8: Not indicated if risk factors absent. (Book p43)")
q(43, "Blood Substitutes", "First generation blood substitute is:",
  ["Perfluorocarbon", "Stroma free hemoglobin", "Hemospan", "PHP"], 0,
  "First generation: Perfluorocarbon. (Book p43)")
q(43, "Blood Substitutes", "Second generation blood substitute is:",
  ["Stroma free hemoglobin", "Perfluorocarbon", "PEG hemoglobin", "MP4OX"], 0,
  "Second generation: Stroma free hemoglobin. (Book p43)")
q(43, "Blood Substitutes", "Next generation blood substitutes include all of the following EXCEPT:",
  ["Perfluorocarbon", "Polyethylene glycol (PEG) hemoglobin", "Hemospan (AKA MP4OX)", "Pyridoxylated hemoglobin polyoxyethylene conjugate (PHP)"], 0,
  "Next generation: PEG hemoglobin; Hemospan (AKA MP4OX); Pyridoxylated hemoglobin polyoxyethylene conjugate (PHP). (Book p43)")
q(43, "Blood Substitutes", "Hemospan is also known as:",
  ["MP4OX", "PHP", "PEG-Hb", "TRALI"], 0,
  "Hemospan (AKA MP4OX). (Book p43)")
q(43, "Anti-shock Garment", "The anti-shock garment is used for:",
  ["Hypovolemic shock in peripheral locations (Eg: Women with PPH in rural areas)", "Cardiogenic shock in ICU", "Septic shock in OT", "Neurogenic shock only"], 0,
  "Anti-shock garment: used for hypovolemic shock in peripheral locations (Eg: Women with PPH in rural areas). (Book p43)")
q(43, "Anti-shock Garment", "The anti-shock garment applies:",
  ["Maximum compression over the legs and least over the upper body", "Equal compression everywhere", "Maximum compression over the chest", "Least compression over the legs"], 0,
  "Anti-shock garment: Maximum compression (lower body), Least compression (upper body). (Book p43)")

# ---------------- UNITS (grouped by contiguous sec blocks) ----------------
def sec_ids(*labels):
    ids = [x["id"] for x in Q if x["sec"] in labels]
    assert ids, labels
    return ids

UNIT_DEFS = [
    ("Hypovolemic Shock: Types & Head-Injury Notes", "Hypovolemic Shock: Types",
     "Hypovolemic/hemorrhagic shock is the m/c shock: overt bleeding is easy to catch while concealed bleeding hides in neck, thorax, abdomen, pelvis and long bones. An isolated head injury never causes it, so a hypotensive head-injury patient makes you suspect brain herniation, neurogenic shock above T6 or polytrauma."),
    ("Arterial vs Venous Bleed", "Arterial vs Venous Bleed",
     "Arterial bleeds spurt, drop the pressure early and are prevented early; lacerated arteries bleed more because vasoconstriction widens the tear, while a clean transection bleeds less. Venous bleeds ooze gradually and hide hypotension late behind compensation."),
    ("Hemorrhage in Surgery", "Hemorrhage in Surgery",
     "Primary hemorrhage bleeds during surgery, reactionary hemorrhage within 24 hours from a dislodged clot or slipped granny's knot, and secondary hemorrhage after 7-14 days when infection sloughs the vessel wall."),
    ("Classification of Hypovolemic Shock", "Classification of Hypovolemic Shock",
     "Four classes climb from 0-15% (0.5 L, all normal, oral liquids) through 15-30% (1 L, tachycardia, anxious and thirsty) and 30-40% (1.5 L, falling SBP, confused, decompensated) to >40% (>2 L, non-recordable pulse and BP, anuria, coma, massive transfusion)."),
    ("Compensated Shock & Fluid Response Check", "Pathophysiology & Response",
     "Class II is compensated shock: sympathetic noradrenaline and adrenaline drive tachycardia - the earliest sign - with peripheral vasoconstriction shunting blood to vital organs, cold extremities and raised peripheral resistance. Give 500 mL-1 L crystalloid and check the response."),
    ("Dynamic Fluid Response & Resuscitation Strategies", "Dynamic Fluid Response", "Management: Resuscitation",
     "Responders keep their improved PR, SBP and JVP; transient responders worsen after 15-20 minutes and non responders never improve - both mean ongoing losses. Before hemostasis use damage control resuscitation (damage control surgery, permissive hypotension, 1:1 RBC:FFP, tranexamic acid/platelets/fibrinogen); after hemostasis switch to perfusion-targeted resuscitation with pressors, thromboprophylaxis and end-organ monitoring."),
    ("Occult Hypoperfusion & Monitoring Indicators", "Occult Hypoperfusion", "Monitoring Indicators",
     "Occult hypoperfusion hides behind normal HR, SBP and urine output but betrays itself with low MVOS and acidosis. PCWP (Swan-Ganz, left heart, more accurate but difficult) outranks CVP (right heart, m/c used) for initial fluid requirement, while urine output (>0.5 mL/kg/hr adult, >1 mL/kg/hr child) is the best resuscitation indicator."),
    ("Shock Indices", "Indices",
     "Shock index = HR/SBP with >0.9 meaning higher mortality; the modified shock index = HR/MAP is the most sensitive; ROPE = HR/pulse pressure with <3 stable and >3 warning of decompensated shock."),
    ("Monitors for Organ/Systemic Perfusion", "Monitors for Organ/Systemic Perfusion",
     "Base deficit and lactate flag acidosis for systemic perfusion while MVOS is the best end point of resuscitation. Muscle reads NIRS and tissue oxygen electrodes, gut mucosa - the most sensitive, forming stress ulcers - reads sublingual capnometry, mucosal pH and laser doppler, kidney reads urine output and brain reads consciousness with tissue oxygen electrode/NIRS."),
    ("Massive Blood Transfusion & Complications", "Massive Blood Transfusion",
     "Massive transfusion = whole circulating volume or >10 units in 24 hrs or >4 units in one hour. It brings hypothermia, citrate-driven hypocalcemia/hypomagnesemia and metabolic alkalosis, hyperkalemia from lysed stored RBCs, and coagulopathy - the m/c cause of death - prevented by limiting crystalloids and giving 1:1:1 PRBC:platelet:FFP; febrile reactions are m/c overall and leukoreduction filters prevent them."),
    ("TACO vs TRALI", "TACO vs TRALI",
     "TACO is cardiac overload with facial puffiness, pedal edema, breathlessness but a normal X-ray, treated with Lasix. TRALI is anti-HLA antibody driven non-cardiogenic pulmonary edema within 6 hours from multiparous donors or FFP, showing ARDS and patchy infiltrates."),
    ("Transfusion Criteria, Blood Substitutes & Anti-shock Garment", "Perioperative RBC Transfusion Criteria", "Blood Substitutes", "Anti-shock Garment",
     "Transfuse below Hb 6, individualise 6-8 with ongoing losses or impending surgery, and withhold above 8 without risk factors. Perfluorocarbon and stroma free hemoglobin were first and second generation; PEG hemoglobin, Hemospan (MP4OX) and PHP are next generation, and the anti-shock garment squeezes the legs hardest to hold up rural PPH patients."),
]

UNITS = []
for i, (title, *rest) in enumerate(UNIT_DEFS, 1):
    labels = tuple(rest[:-1])
    guide = rest[-1]
    UNITS.append({"id": f"SURG-U7-{i}", "ch": 7, "n": i, "title": title,
                  "sec": f"{Q[[x['sec'] for x in Q].index(labels[0])]['sec']} \u00b7 p{Q[[x['sec'] for x in Q].index(labels[0])]['page']}",
                  "qs": sec_ids(*labels), "guide": guide})

# contiguity + order check for unit qs
covered = [i for u in UNITS for i in u["qs"]]
assert covered == [x["id"] for x in Q], "units must cover questions in order"

data = {"questions": Q, "units": UNITS}
with open("data/ch7.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
print(f"ch7: {len(Q)} questions, {len(UNITS)} units")
