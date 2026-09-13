#!/usr/bin/env python3
"""Build data/ch8.json for PULSE Surgery ch8 (Shock : Part 2, book p44-48)."""
import json

Q = []
def q(page, sec, text, opts, ans, exp):
    Q.append({"id": f"SURG-C8-{len(Q)+1:03d}", "sec": sec, "page": page,
              "q": text, "opts": opts, "ans": ans, "exp": exp})

# ---------------- p44 · MVOS ----------------
q(44, "MVOS", "Mixed venous oxygen saturation (MVOS) represents:",
  ["The unutilised O2 returning back to the heart", "The O2 consumed by tissues", "Arterial O2 content", "Alveolar O2"], 0,
  "MVOS: Represents the unutilised O2 returning back to the heart. (Book p44)")
q(44, "MVOS", "The normal value of MVOS is:",
  ["50-70%", "20-40%", "70-90%", "95-100%"], 0,
  "MVOS: Normal value: 50 - 70%. (Book p44)")
q(44, "MVOS", "MVOS is measured via a catheter placed in the:",
  ["Right atrium", "Left atrium", "Aorta", "Pulmonary vein"], 0,
  "MVOS: Measured via a catheter in the Right Atrium. (Book p44)")
q(44, "MVOS", "Low MVOS is seen in:",
  ["Low cardiac output and reduced O2 pump (hypovolemic shock)", "Distributive shock", "Warm septic shock", "Arteriovenous fistula"], 0,
  "Low MVOS: Low cardiac output; Reduced O2 pump (Hypovolemic shock). (Book p44)")
q(44, "MVOS", "High MVOS is characteristic of:",
  ["Distributive shock", "Hypovolemic shock", "Cardiogenic shock", "Haemorrhagic shock"], 0,
  "High MVOS: Distributive shock. (Book p44)")

# ---------------- p44 · CARDIOGENIC SHOCK ----------------
q(44, "Cardiogenic Shock", "Examples of cardiogenic shock include all of the following EXCEPT:",
  ["Massive pulmonary embolism", "Myocardial infarction", "Cardiac tamponade", "Arrhythmias"], 0,
  "Cardiogenic shock examples: Myocardial Infarction, Cardiac Tamponade, Arrhythmias (massive PE is obstructive). (Book p44)")
q(44, "Cardiogenic Shock", "In cardiogenic shock the primary defect is that the:",
  ["Heart does not function properly", "Vessels dilate", "Blood volume falls", "Lungs fail"], 0,
  "Pathophysiology: Heart does not function properly. (Book p44)")
q(44, "Cardiogenic Shock", "In cardiogenic shock, decreased cardiac output leads to:",
  ["O2 not pumped and ↓ MVOS", "↑ MVOS", "↑ SBP", "↓ PVR"], 0,
  "↓ CO -> O2 not pumped -> ↓ MVOS. (Book p44)")
q(44, "Cardiogenic Shock", "In cardiogenic shock the SBP and PVR changes are:",
  ["↓ SBP and ↑ PVR with cold extremities", "↑ SBP and ↓ PVR with warm extremities", "↓ SBP and ↓ PVR", "Normal SBP and PVR"], 0,
  "↓ SBP -> ↑ PVR (Cold extremities). (Book p44)")
q(44, "Cardiogenic Shock", "In cardiogenic shock, accumulating preload causes:",
  ["↑ JVP", "↓ JVP", "Normal JVP", "↑ urine output"], 0,
  "Preload accumulates -> ↑ JVP. (Book p44)")
q(44, "Cardiogenic Shock", "Extremities in cardiogenic shock are:",
  ["Cold", "Warm", "Flushed", "Sweaty and warm"], 0,
  "Cardiogenic shock: ↑ PVR (Cold extremities). (Book p44)")

# ---------------- p44-45 · NEUROGENIC SHOCK ----------------
q(44, "Neurogenic Shock", "The classic example of neurogenic shock is:",
  ["Spinal cord injury above T6 level", "Spinal cord injury below L1", "Isolated head injury", "Femoral nerve injury"], 0,
  "Neurogenic shock example: Spinal cord injury above T6 level. (Book p44)")
q(44, "Neurogenic Shock", "The pathophysiology of neurogenic shock begins with:",
  ["Loss of sympathetic drive", "Histamine release", "Cardiac pump failure", "Hypovolemia"], 0,
  "Pathophysiology: Loss of sympathetic drive. (Book p44)")
q(44, "Neurogenic Shock", "Loss of sympathetic drive causes vasodilation with:",
  ["PVR ↓↓ and warm extremities", "PVR ↑↑ and cold extremities", "PVR normal", "↑ CO"], 0,
  "Vasodilation -> PVR ↓↓ (Warm extremities). (Book p44)")
q(44, "Neurogenic Shock", "The heart rate change in neurogenic shock is:",
  ["Bradycardia (↓ HR)", "Tachycardia", "Normal", "Variable ↑/↓"], 0,
  "Loss of sympathetic drive -> Bradycardia (↓ HR). (Book p44)")
q(45, "Neurogenic Shock", "In neurogenic shock, peripheral pooling of blood causes:",
  ["↓ JVP, ↓ CO, ↓ SBP", "↑ JVP, ↑ CO, ↑ SBP", "↑ JVP with ↓ CO", "Normal JVP and CO"], 0,
  "D/t peripheral pooling of blood -> ↓ JVP, ↓ CO, ↓ SBP. (Book p45)")
q(45, "Neurogenic Shock", "The combination characteristic of neurogenic shock is:",
  ["Bradycardia + hypotension", "Tachycardia + hypotension", "Bradycardia + hypertension", "Tachycardia + hypertension"], 0,
  "Neurogenic shock: Bradycardia + Hypotension. (Book p45)")

# ---------------- p45 · ANAPHYLACTIC SHOCK ----------------
q(45, "Anaphylactic Shock", "The example of anaphylactic shock given is:",
  ["Mismatched blood transfusion", "Spinal anaesthesia", "MI", "Pulmonary embolism"], 0,
  "Anaphylactic shock example: Mismatched blood transfusion. (Book p45)")
q(45, "Anaphylactic Shock", "In anaphylactic shock, the potent vasodilator released is:",
  ["Histamine", "Noradrenaline", "Angiotensin", "Endothelin"], 0,
  "Histamine release (Potent vasodilator). (Book p45)")
q(45, "Anaphylactic Shock", "Histamine release causes vasodilation and pooling of blood leading to:",
  ["↓ PVR with warm extremities", "↑ PVR with cold extremities", "↑ JVP", "↑ SBP"], 0,
  "Vasodilation -> Pooling of blood -> ↓ PVR (Warm extremities). (Book p45)")
q(45, "Anaphylactic Shock", "In anaphylactic shock, JVP, SBP and CO all:",
  ["Decrease", "Increase", "Stay normal", "Become non-recordable only"], 0,
  "Pooling of blood -> ↓ JVP, ↓ SBP, ↓ CO. (Book p45)")
q(45, "Anaphylactic Shock", "Because the sympathetic system is normal in anaphylactic shock, ↓ CO equals:",
  ["↑ HR x ↓ SV", "↓ HR x ↑ SV", "↑ HR x ↑ SV", "↓ HR x ↓ SV"], 0,
  "But, d/t normal sympathetic system: ↓ CO = ↑ HR x ↓ SV. (Book p45)")

# ---------------- p45 · SEPTIC SHOCK WARM & COLD ----------------
q(45, "Septic Shock: Warm & Cold", "Warm septic shock shows a hyperdynamic circulation with:",
  ["↑ CO, ↑ HR, ↑ SBP", "↓ CO, ↓ HR, ↓ SBP", "↑ CO with ↓ SBP", "↓ CO with ↑ SBP"], 0,
  "Warm septic shock: Hyperdynamic circulation -> ↑ CO, ↑ HR, ↑ SBP. (Book p45)")
q(45, "Septic Shock: Warm & Cold", "MVOS is raised in warm septic shock because of:",
  ["Inability of tissues to utilize O2", "Low cardiac output", "Hypovolemia", "Increased O2 pump"], 0,
  "Raised MVOS d/t inability of tissues to utilize O2. (Book p45)")
q(45, "Septic Shock: Warm & Cold", "Cold septic shock occurs in the:",
  ["Late phase of sepsis", "Early phase of sepsis", "Recovery phase", "Incubation phase"], 0,
  "Cold septic shock: Late phase of sepsis. (Book p45)")
q(45, "Septic Shock: Warm & Cold", "In cold septic shock, toxins inhibit the myocardium making it similar to:",
  ["Cardiogenic shock", "Hypovolemic shock", "Neurogenic shock", "Anaphylactic shock"], 0,
  "Toxins inhibit myocardium -> similar to cardiogenic shock. (Book p45)")

# ---------------- p45 · SHOCK COMPARISON TABLE ----------------
q(45, "Shock Comparison Table", "In the shock comparison table, pulse rate is ↑↑ (maximum) in:",
  ["Anaphylactic shock", "Hypovolemic (Class III)", "Neurogenic shock", "Warm septic shock"], 0,
  "Table: PR: Anaphylactic = ↑↑. (Book p45)")
q(45, "Shock Comparison Table", "Pulse rate is ↓ in which shock?",
  ["Neurogenic shock", "Hypovolemic (Class III)", "Anaphylactic shock", "Warm septic shock"], 0,
  "Table: PR: Neurogenic = ↓. (Book p45)")
q(45, "Shock Comparison Table", "Pulse rate is ↑/↓ (variable) in:",
  ["Cardiogenic and cold septic shock", "Hypovolemic and warm septic", "Neurogenic and anaphylactic", "Only anaphylactic"], 0,
  "Table: PR: Cardiogenic = ↑/↓; Septic cold = ↑/↓. (Book p45)")
q(45, "Shock Comparison Table", "Cardiac output is ↑ only in:",
  ["Warm septic shock", "Cold septic shock", "Cardiogenic shock", "Anaphylactic shock"], 0,
  "Table: CO: Septic warm = ↑ (all others ↓). (Book p45)")
q(45, "Shock Comparison Table", "SBP is ↑ only in:",
  ["Warm septic shock", "Hypovolemic shock", "Cardiogenic shock", "Neurogenic shock"], 0,
  "Table: SBP: Septic warm = ↑ (others ↓). (Book p45)")
q(45, "Shock Comparison Table", "PVR is ↑↑ (maximum) in:",
  ["Hypovolemic (Class III)", "Cardiogenic shock", "Cold septic shock", "Warm septic shock"], 0,
  "Table: PVR: Hypovolemic (Class III) = ↑↑. (Book p45)")
q(45, "Shock Comparison Table", "PVR is ↑ (single up) in which shocks?",
  ["Cardiogenic and cold septic", "Warm septic and anaphylactic", "Neurogenic and warm septic", "Hypovolemic and neurogenic"], 0,
  "Table: PVR: Cardiogenic = ↑; Septic cold = ↑. (Book p45)")
q(45, "Shock Comparison Table", "JVP is ↑ in:",
  ["Cardiogenic and cold septic shock", "Hypovolemic and anaphylactic", "Neurogenic and warm septic", "All shocks"], 0,
  "Table: JVP: Cardiogenic = ↑; Septic cold = ↑; others ↓ or normal. (Book p45)")
q(45, "Shock Comparison Table", "JVP is normal in:",
  ["Warm septic shock", "Cardiogenic shock", "Cold septic shock", "Hypovolemic shock"], 0,
  "Table: JVP: Septic warm = Normal. (Book p45)")
q(45, "Shock Comparison Table", "MVOS is ↑↑ in:",
  ["Warm septic shock", "Cold septic shock", "Hypovolemic shock", "Cardiogenic shock"], 0,
  "Table: MVOS: Septic warm = ↑↑. (Book p45)")
q(45, "Shock Comparison Table", "MVOS is ↓ in which shocks?",
  ["Hypovolemic, cardiogenic and cold septic", "Warm septic only", "Neurogenic and anaphylactic", "All shocks"], 0,
  "Table: MVOS: Hypovolemic ↓, Cardiogenic ↓, Septic cold ↓; neurogenic and anaphylactic = -. (Book p45)")
q(45, "Shock Comparison Table", "Acidosis in the comparison table is present (+) in:",
  ["All listed shocks", "Only hypovolemic shock", "Only septic shocks", "Only cardiogenic shock"], 0,
  "Table: Acidosis: + in every column. (Book p45)")

# ---------------- p46 · OBSTRUCTIVE, DISTRIBUTIVE & ENDOCRINE SHOCK ----------------
q(46, "Obstructive, Distributive & Endocrine", "Obstructive shock is a type of:",
  ["Cardiogenic shock", "Distributive shock", "Hypovolemic shock", "Endocrine shock"], 0,
  "Obstructive shock: Type of cardiogenic shock. (Book p46)")
q(46, "Obstructive, Distributive & Endocrine", "In obstructive shock, preload falls because of:",
  ["Improper filling of heart", "Vasodilation", "Blood loss", "Myocardial infarction"], 0,
  "Preload ↓ d/t improper filling of heart. (Book p46)")
q(46, "Obstructive, Distributive & Endocrine", "Examples of obstructive shock are:",
  ["Cardiac tamponade and massive pulmonary embolism", "MI and arrhythmias", "Spinal injury and anaphylaxis", "Adrenal insufficiency"], 0,
  "Obstructive shock examples: Cardiac Tamponade; massive pulmonary embolism. (Book p46)")
q(46, "Obstructive, Distributive & Endocrine", "Distributive shock is caused by:",
  ["Redistribution of blood to the peripheries decreasing cardiac output", "Pump failure", "Obstruction to filling", "Blood loss"], 0,
  "Distributive shock: Redistribution of blood to the peripheries -> ↓ Cardiac Output. (Book p46)")
q(46, "Obstructive, Distributive & Endocrine", "Examples of distributive shock with warm extremities (+) are:",
  ["Neurogenic, anaphylactic and warm septic shock", "Cardiogenic and obstructive", "Cold septic only", "Hypovolemic and cardiogenic"], 0,
  "Distributive examples: Neurogenic shock, Anaphylactic shock, Warm septic shock -> Warm extremities (+). (Book p46)")
q(46, "Obstructive, Distributive & Endocrine", "Endocrine shock is a combination of:",
  ["Cardiac and distributive shock", "Hypovolemic and obstructive", "Septic and anaphylactic", "Neurogenic and obstructive"], 0,
  "Endocrine shock: Combination of cardiac and distributive shock. (Book p46)")
q(46, "Obstructive, Distributive & Endocrine", "Examples of endocrine shock include:",
  ["Hypo/hyperthyroidism and adrenal insufficiency", "Diabetes insipidus only", "Cushing syndrome only", "Addison disease only"], 0,
  "Endocrine shock examples: Hypo/hyperthyroidism; Adrenal insufficiency. (Book p46)")

# ---------------- p46 · SIRS & TERMINOLOGIES ----------------
q(46, "SIRS & Terminologies", "SIRS stands for and means:",
  ["Systemic inflammatory response syndrome; body's response to inflammation", "Septic immune response state; infection only", "Systemic infection response score; bacterial count", "Severe inflammatory reaction syndrome; fever only"], 0,
  "SIRS (Systemic inflammatory response syndrome): Body's response to inflammation. (Book p46)")
q(46, "SIRS & Terminologies", "The etiology of inflammation in SIRS can be:",
  ["Infective and non-infective", "Only infective", "Only non-infective", "Only traumatic"], 0,
  "Etiology of inflammation: Infective; Non-Infective. (Book p46)")
q(46, "SIRS & Terminologies", "Mediators of SIRS include:",
  ["IL-1, IL-6, TNF-alpha", "IL-2, IL-4, IL-10", "Histamine only", "Prostaglandins only"], 0,
  "Mediators: IL-1, IL-6, TNF-alpha. (Book p46)")
q(46, "SIRS & Terminologies", "The temperature parameter of SIRS is:",
  ["> 38°C or < 36°C", "> 39°C or < 35°C", "> 37.5°C only", "< 37°C only"], 0,
  "SIRS parameters: a. Temperature > 38°C or < 36°C. (Book p46)")
q(46, "SIRS & Terminologies", "The heart rate parameter of SIRS is:",
  ["> 90 bpm", "> 100 bpm", "> 110 bpm", "> 120 bpm"], 0,
  "SIRS parameters: b. Heart rate > 90 bpm. (Book p46)")
q(46, "SIRS & Terminologies", "The respiratory parameter of SIRS is:",
  ["Respiratory rate > 20/min or PaCO2 < 32 torr", "Respiratory rate > 30/min or PaCO2 < 25 torr", "Respiratory rate > 12/min", "PaCO2 > 45 torr"], 0,
  "SIRS parameters: c. Respiratory rate > 20/min or PaCO2 < 32 torr. (Book p46)")
q(46, "SIRS & Terminologies", "The WBC parameter of SIRS is:",
  ["WBC > 12000/mm3 or < 4000/mm3 or > 10% band forms in peripheral smear", "WBC > 15000/mm3 only", "WBC < 8000/mm3", "> 5% band forms"], 0,
  "SIRS parameters: d. WBC > 12000/mm3 or < 4000/mm3 or > 10% band forms in peripheral smear. (Book p46)")
q(46, "SIRS & Terminologies", "SIRS is defined when how many parameters are present?",
  ["Any 2 parameters", "All 4 parameters", "Any 1 parameter", "Any 3 parameters"], 0,
  "Any 2 parameters present: SIRS. (Book p46)")

# ---------------- p47 · SEPSIS DEFINITIONS & SCORES ----------------
q(47, "Sepsis Definitions & Scores", "The old definition of sepsis was:",
  ["SIRS + known foci of infection", "SOFA ≥ 2", "qSOFA ≥ 2", "SIRS + organ failure"], 0,
  "Sepsis: Old definition: SIRS + Known foci of infection. (Book p47)")
q(47, "Sepsis Definitions & Scores", "The new definition of sepsis is:",
  ["SOFA score ≥ 2 + documented infection", "SIRS + fever", "qSOFA ≥ 1", "Blood culture positive only"], 0,
  "New definition: SOFA score ≥ 2 + Documented infection. (Book p47)")
q(47, "Sepsis Definitions & Scores", "SOFA stands for:",
  ["Sequential organ failure assessment", "Systemic organ failure analysis", "Sepsis organ function audit", "Sequential oxygen failure assessment"], 0,
  "SOFA score (Sequential organ failure assessment). (Book p47)")
q(47, "Sepsis Definitions & Scores", "A SOFA score of ≥ 2 indicates:",
  ["Sepsis", "SIRS", "MODS", "Septic shock"], 0,
  "SOFA score: ≥ 2 -> Sepsis. (Book p47)")
q(47, "Sepsis Definitions & Scores", "qSOFA parameters include all of the following EXCEPT:",
  ["Heart rate > 90 bpm", "SBP < 100 mmHg", "RR > 22/min (tachypnea)", "Altered mental state"], 0,
  "qSOFA parameters: a. SBP < 100 mmHg; b. RR > 22/min (Tachypnea); c. Altered mental state. (Book p47)")
q(47, "Sepsis Definitions & Scores", "The qSOFA SBP cutoff is:",
  ["< 100 mmHg", "< 90 mmHg", "< 110 mmHg", "< 120 mmHg"], 0,
  "qSOFA: a. SBP < 100 mmHg. (Book p47)")
q(47, "Sepsis Definitions & Scores", "The qSOFA respiratory rate cutoff is:",
  ["> 22/min", "> 20/min", "> 24/min", "> 30/min"], 0,
  "qSOFA: b. RR > 22/min (Tachypnea). (Book p47)")
q(47, "Sepsis Definitions & Scores", "A qSOFA score ≥ 2 predicts:",
  ["Poor outcome", "Good outcome", "SIRS", "Fever"], 0,
  "qSOFA ≥ 2: Poor outcome. (Book p47)")
q(47, "Sepsis Definitions & Scores", "The qSOFA sofa graphic lists hypotension (systolic BP <100 mm Hg), altered mental status and:",
  ["Tachypnea RR > 22/min", "Tachycardia HR > 90", "Fever > 38°C", "Urine output < 0.5 mL/kg/hr"], 0,
  "qSOFA score graphic: Hypotension SBP <100 mm Hg; Altered mental status; Tachypnea RR > 22/min; Score of ≥2 criteria suggests a poor outcome. (Book p47)")
q(47, "Sepsis Definitions & Scores", "Septic shock is defined as sepsis with:",
  ["Fluid unresponsive hypotension", "Fever only", "Tachycardia only", "Raised WBC"], 0,
  "Septic Shock: Sepsis with fluid unresponsive hypotension. (Book p47)")
q(47, "Sepsis Definitions & Scores", "MODS (multiorgan dysfunction syndrome) is:",
  ["Failure of 2 or more organ systems", "Failure of 1 organ", "Failure of 4 or more organs", "Renal failure only"], 0,
  "MODS: Failure of 2 or more organ systems. (Book p47)")

# ---------------- p47 · SEPSIS 3.0 ----------------
q(47, "Sepsis 3.0", "As per Sepsis 3.0, sepsis is:",
  ["Life-threatening organ dysfunction caused by a dysregulated host response to infection", "SIRS plus infection", "Fever with tachycardia", "qSOFA ≥ 1 with fever"], 0,
  "Sepsis 3.0: Life-threatening organ dysfunction caused by a dysregulated host response to infection. (Book p47)")
q(47, "Sepsis 3.0", "As per Sepsis 3.0, septic shock needs vasopressors/inotropes plus lactate greater than:",
  ["2 mmol/L", "1 mmol/L", "4 mmol/L", "0.5 mmol/L"], 0,
  "Septic Shock: Need for vasopressors/ionotropers + Lactate > 2 mmol/L. (Book p47)")
q(47, "Sepsis 3.0", "Which term is OUT as per the update?",
  ["Severe sepsis", "Septic shock", "qSOFA", "SOFA"], 0,
  "Note: The term severe sepsis is out. (Book p47)")
q(47, "Sepsis 3.0", "As per the update:",
  ["SIRS is out; qSOFA/SOFA are in", "SIRS is in; qSOFA is out", "Both SIRS and SOFA are out", "qSOFA is out; SIRS is in"], 0,
  "Note: SIRS is out qSOFA/SOFA are in. (Book p47)")

# ---------------- p48 · SEPSIS SIX ----------------
q(48, "Sepsis Six", "The sepsis six are six things to be done in:",
  ["60 mins", "30 mins", "3 hours", "6 hours"], 0,
  "Sepsis Six: Six things to be done in 60 mins. (Book p48)")
q(48, "Sepsis Six", "The 'Give 3' of the sepsis six are:",
  ["I/V antibiotics, I/V fluids, O2", "Cultures, urine output, lactate", "Vasopressors, fluids, O2", "Antibiotics, cultures, O2"], 0,
  "Give 3: I/V antibiotics, I/V fluids, O2. (Book p48)")
q(48, "Sepsis Six", "The 'Take 3' of the sepsis six are:",
  ["Cultures, urine output, serum lactate", "Antibiotics, fluids, O2", "BP, HR, RR", "Blood, urine, sputum"], 0,
  "Take 3: Cultures, Urine output, Serum lactate. (Book p48)")
q(48, "Sepsis Six", "The mnemonic for the sepsis six is:",
  ["Think FABULOS", "Think SEPSIS", "FAST HUG", "SIX PACK"], 0,
  "Mnemonic: Think FABULOS. (Book p48)")
q(48, "Sepsis Six", "In the FABULOS mnemonic, the letters stand for Fluid, Antibiotics, Blood cultures, Urine output, Lactate, Oxygen and:",
  ["In Sixty minutes", "In Sepsis", "Immediate Support", "Intravenous Steroids"], 0,
  "FABULOS: Fluid, Antibiotics, Blood cultures, Urine Output, Lactate, Oxygen, In Sixty minutes. (Book p48)")

# ---------------- p48 · SURVIVING SEPSIS GUIDELINES / SEPSIS BUNDLE ----------------
q(48, "Sepsis Bundle", "Within 3 hours of the sepsis bundle, the first step is to:",
  ["Measure lactate", "Start vasopressors", "Give FFP", "Insert arterial line"], 0,
  "Within 3 hours: 1. Measure lactate. (Book p48)")
q(48, "Sepsis Bundle", "Blood cultures in the sepsis bundle are taken:",
  ["Prior to antibiotics", "After antibiotics", "Only if fever persists", "Never"], 0,
  "Within 3 hours: 2. Blood culture prior to antibiotics. (Book p48)")
q(48, "Sepsis Bundle", "Within 3 hours the bundle gives:",
  ["Broad spectrum antibiotics", "Narrow spectrum antibiotics", "Antifungals only", "Antivirals"], 0,
  "Within 3 hours: 3. Broad spectrum antibiotics. (Book p48)")
q(48, "Sepsis Bundle", "30 mL/kg crystalloid within 3 hours is indicated for:",
  ["Hypotension or lactate ≥ 4 mmol/L", "Fever only", "Tachycardia only", "Lactate ≥ 2 mmol/L only"], 0,
  "Within 3 hours: 4. 30 ml/Kg crystalloid for: Hypotension or Lactate ≥ 4 mmol/L. (Book p48)")
q(48, "Sepsis Bundle", "Within 6 hours, vasopressors for refractory hypotension target a MAP of:",
  ["≥ 65 mmHg", "≥ 50 mmHg", "≥ 80 mmHg", "≥ 90 mmHg"], 0,
  "Within 6 hours: 5. Vasopressors for refractory hypotension -> Target MAP ≥ 65 mmHg. (Book p48)")
q(48, "Sepsis Bundle", "Persistent arterial hypotension/lactate ≥ 4 mmol/L within 6 hours prompts measurement of:",
  ["CVP and central venous O2 saturation (ScvO2)", "Only urine output", "Only Hb", "PCWP only"], 0,
  "6. Persistent arterial hypotension/Lactate ≥ 4 mmol/L -> measure: a. CVP; b. Central venous O2 saturation (ScvO2). (Book p48)")
q(48, "Sepsis Bundle", "Within 6 hours the bundle also advises to:",
  ["Remeasure lactate if initially elevated", "Stop antibiotics", "Transfuse blood always", "Give steroids always"], 0,
  "Within 6 hours: 7. Remeasure lactate (if initially elevated). (Book p48)")
q(48, "Sepsis Bundle", "The bundle targets are CVP and ScvO2 of:",
  ["CVP ≥ 8 mm Hg, ScvO2 ≥ 70%", "CVP ≥ 12 mm Hg, ScvO2 ≥ 50%", "CVP ≥ 5 mm Hg, ScvO2 ≥ 90%", "CVP ≥ 15 mm Hg, ScvO2 ≥ 60%"], 0,
  "Target CVP: ≥ 8 mm Hg, ScvO2 ≥ 70%. (Book p48)")

# ---------------- UNITS ----------------
def sec_ids(*labels):
    ids = [x["id"] for x in Q if x["sec"] in labels]
    assert ids, labels
    return ids

def first_page(label):
    for x in Q:
        if x["sec"] == label:
            return x["page"]

UNIT_DEFS = [
    ("MVOS: Meaning, Value & Types", ("MVOS",),
     "MVOS is the unutilised oxygen returning to the heart - normally 50-70%, read from a right atrial catheter. Low values mean a low cardiac output or a reduced O2 pump (hypovolemic shock); a high value points to distributive shock."),
    ("Cardiogenic Shock", ("Cardiogenic Shock",),
     "MI, tamponade and arrhythmias stop the heart functioning properly: CO and MVOS fall, SBP falls with PVR rising into cold extremities, while accumulating preload raises the JVP."),
    ("Neurogenic Shock", ("Neurogenic Shock",),
     "Spinal cord injury above T6 switches off sympathetic drive: vasodilation drops PVR into warm extremities while bradycardia and peripheral pooling pull JVP, CO and SBP down - bradycardia with hypotension is the giveaway."),
    ("Anaphylactic Shock", ("Anaphylactic Shock",),
     "Histamine - a potent vasodilator - pools blood in anaphylaxis (classically a mismatched transfusion), dropping PVR, JVP, SBP and CO with warm extremities; an intact sympathetic system compensates with ↓CO = ↑HR x ↓SV."),
    ("Septic Shock: Warm & Cold", ("Septic Shock: Warm & Cold",),
     "Warm septic shock is hyperdynamic (↑CO, ↑HR, ↑SBP) with a raised MVOS because tissues cannot use O2; cold septic shock is the late phase where toxins inhibit the myocardium, mimicking cardiogenic shock."),
    ("Shock Comparison Table", ("Shock Comparison Table",),
     "Across the table: PR peaks (↑↑) in anaphylaxis and falls in neurogenic; CO and SBP rise only in warm sepsis; PVR is ↑↑ in hypovolemia and ↑ in cardiogenic/cold sepsis; JVP rises in cardiogenic/cold sepsis but stays normal in warm sepsis; MVOS is ↑↑ in warm sepsis, ↓ in hypovolemic/cardiogenic/cold sepsis; acidosis is positive everywhere."),
    ("Obstructive, Distributive & Endocrine Shock", ("Obstructive, Distributive & Endocrine",),
     "Obstructive shock is a cardiogenic variant where tamponade or massive PE blocks filling and preload falls. Distributive shock redistributes blood peripherally (neurogenic, anaphylactic, warm septic - all warm), while endocrine shock mixes cardiac and distributive patterns in thyroid disease or adrenal insufficiency."),
    ("SIRS: Terminologies & Parameters", ("SIRS & Terminologies",),
     "SIRS is the body's response to infective or non-infective inflammation through IL-1, IL-6 and TNF-alpha. Any two of: temperature >38/<36°C, HR >90, RR >20 or PaCO2 <32 torr, WBC >12000/<4000 or >10% bands - and SIRS is declared."),
    ("Sepsis: Definitions, Scores & Sepsis 3.0", ("Sepsis Definitions & Scores", "Sepsis 3.0",),
     "Old sepsis was SIRS plus a known focus; new sepsis is SOFA ≥2 with documented infection, and qSOFA (SBP <100, RR >22, altered mentation) ≥2 forecasts poor outcome. Sepsis 3.0 calls it life-threatening organ dysfunction from a dysregulated host response, septic shock adds vasopressors plus lactate >2 mmol/L - severe sepsis and SIRS are out."),
    ("Sepsis Six", ("Sepsis Six",),
     "Six things in sixty minutes - give I/V antibiotics, I/V fluids and O2; take cultures, urine output and serum lactate - remembered as Think FABULOS."),
    ("Surviving Sepsis Guidelines / Sepsis Bundle", ("Sepsis Bundle",),
     "Within 3 hours: measure lactate, culture before antibiotics, broad spectrum antibiotics and 30 mL/kg crystalloid for hypotension or lactate ≥4. Within 6 hours: vasopressors to MAP ≥65, measure CVP and ScvO2 for persistent hypotension/lactate ≥4, remeasure lactate - targeting CVP ≥8 mm Hg and ScvO2 ≥70%."),
]

UNITS = []
for i, (title, labels, guide) in enumerate(UNIT_DEFS, 1):
    UNITS.append({"id": f"SURG-U8-{i}", "ch": 8, "n": i, "title": title,
                  "sec": f"{labels[0]} \u00b7 p{first_page(labels[0])}",
                  "qs": sec_ids(*labels), "guide": guide})

covered = [i for u in UNITS for i in u["qs"]]
assert covered == [x["id"] for x in Q], "units must cover questions in order"

data = {"questions": Q, "units": UNITS}
with open("data/ch8.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
print(f"ch8: {len(Q)} questions, {len(UNITS)} units")
