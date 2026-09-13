#!/usr/bin/env python3
"""Build data/ch2.json for PULSE Surgery ch2 (Surgical Blades and Energy Sources, book p6-9)."""
import json

Q = []
def q(page, sec, text, opts, ans, exp):
    Q.append({"id": f"SURG-C2-{len(Q)+1:03d}", "sec": sec, "page": page,
              "q": text, "opts": opts, "ans": ans, "exp": exp})

# ---------------- p6 · BLADES ----------------
q(6, "Blades", "The use of surgical blades, as stated in the book, is to:",
  ["Make incisions", "Control bleeding", "Close wounds", "Retract tissues"], 0,
  "Uses: make Incisions. (Book p6)")
q(6, "Blades", "The sharpest part of a surgical blade is its:",
  ["Back edge", "Slot", "Belly", "Shank"], 2,
  "Belly of the blade: Sharpest. (Book p6)")
q(6, "Blades", "The No. 11 blade is described as a:",
  ["Curved blade", "Pointed / stab blade", "Broad spade blade", "Hooked blade"], 1,
  "No 11 Blade: Pointed/Stab blade. (Book p6)")
q(6, "Blades", "Incision and drainage (I & D) of an abscess is a listed use of the:",
  ["No. 12 blade", "No. 10 blade", "No. 11 blade", "No. 22 blade"], 2,
  "No 11 Blade uses: Incision & drainage (I & D) of abscess. (Book p6)")
q(6, "Blades", "Arteriotomy is a listed use of the:",
  ["No. 12 blade", "No. 11 blade", "No. 15 blade", "No. 23 blade"], 1,
  "No 11 Blade uses: I & D of abscess and Arteriotomy. (Book p6)")
q(6, "Blades", "The No. 12 blade is:",
  ["Straight", "Pointed", "Serrated", "Curved"], 3,
  "No 12 Blade: Curved. (Book p6)")
q(6, "Blades", "Suture removal is the listed use of the:",
  ["No. 12 blade", "No. 11 blade", "No. 10 blade", "No. 15 blade"], 0,
  "No 12 Blade uses: Suture removal. (Book p6)")
q(6, "Blades", "The book's Types of Blades diagram includes all of the following EXCEPT:",
  ["No. 10", "No. 15", "No. 20", "No. 22"], 2,
  "The diagram shows No. 10, 11, 15, 22, 23 and the curved No. 12 - there is no No. 20. (Book p6)")

# ---------------- p6 · BLADE HANDLING ----------------
q(6, "Blade Handling", "While passing, a blade is passed:",
  ["Hand to hand", "On a sponge", "In a kidney tray", "In a gallipot"], 2,
  "Passed in kidney tray / pointed end facing towards self. (Book p6)")
q(6, "Blade Handling", "While passing a blade, its pointed end faces:",
  ["Towards the surgeon", "Upwards", "Downwards", "Towards self (the passer)"], 3,
  "Passed in kidney tray / pointed end facing towards self. (Book p6)")
q(6, "Blade Handling", "Blades are mounted on the:",
  ["Mayo handle", "BP (Bard Parker) handle", "Kocher handle", "Allis handle"], 1,
  "Mounted on BP (Bard Parker) handle. (Book p6)")

# ---------------- p6 · INCISIONS ----------------
q(6, "Incisions", "Skin incisions are made:",
  ["Parallel to skin", "Perpendicular to skin", "At 45 degrees to skin", "Tangential to skin"], 1,
  "Incisions: Perpendicular to skin. (Book p6)")
q(6, "Incisions", "An incision proceeds:",
  ["Far to near", "Near to far", "Left to right", "Deep to superficial"], 0,
  "Go far to Near. (Book p6)")
q(6, "Incisions", "Langer's lines are also called:",
  ["Relaxed pressure lines", "Dermal grid lines", "Relaxed tension lines", "Collagen cleft lines"], 2,
  "Langer's lines (Relaxed tension lines). (Book p6)")
q(6, "Incisions", "Langer's lines represent the orientation of:",
  ["Muscle fibres", "Dermal collagen fibres", "Cutaneous nerves", "Subdermal vessels"], 1,
  "Langer's lines: orientation of dermal collagen fibers. (Book p6)")
q(6, "Incisions", "An incision placed parallel to Langer's lines gives a:",
  ["Wide scar", "Good scar", "Hypertrophic scar", "Contracted scar"], 1,
  "Incision placed parallel: Good scar. (Book p6)")
q(6, "Incisions", "Muscle fibre action runs _____ to Langer's lines:",
  ["Parallel", "Perpendicular", "Oblique", "Spiral"], 1,
  "Muscle fibre action is perpendicular. (Book p6)")
q(6, "Incisions", "While planning an incision, one must avoid injury to:",
  ["Skin creases", "Langer's lines", "Anatomical structures", "Scar tissue"], 2,
  "Avoid injury to anatomical structures. (Book p6)")
q(6, "Incisions", "For a good cosmetic result, incisions are placed parallel to Langer's lines or:",
  ["Across skin creases", "Over bony points", "Through hair-bearing skin", "Hidden in skin creases"], 3,
  "Cosmetic factor: Parallel to Langer's lines / hidden in skin creases. (Book p6)")
q(6, "Incisions", "Which of the following is a factor while planning an incision?",
  ["Adequate access", "Maximum length", "Maximum depth", "Avoiding Langer's lines"], 0,
  "Factors while planning an incision include adequate access. (Book p6)")

# ---------------- p7 · MONOPOLAR CIRCUIT & PAD ----------------
q(7, "Monopolar Cautery", "In monopolar cautery, current flows from the machine to the:",
  ["Pad", "Tip (Bovie tip)", "Earth wire", "Patient skin directly"], 1,
  "Machine Current -> Tip (Bovie tip). (Book p7)")
q(7, "Monopolar Cautery", "The tip used in monopolar cautery is called the:",
  ["Bovie tip", "Mayo tip", "Ligasure tip", "CUSA tip"], 0,
  "Tip (Bovie tip). (Book p7)")
q(7, "Monopolar Cautery", "The correct order of the monopolar circuit is:",
  ["Machine -> Tip -> Cut/Coagulate -> Body -> Pad -> Machine",
   "Machine -> Pad -> Body -> Tip -> Cut/Coagulate -> Machine",
   "Tip -> Machine -> Pad -> Body -> Cut/Coagulate -> Tip",
   "Machine -> Body -> Tip -> Pad -> Cut/Coagulate -> Machine"], 0,
  "Circuit: machine -> Tip -> Cut/Coagulate -> to body -> Pad -> machine. (Book p7)")
q(7, "Monopolar Cautery", "The cautery handpiece carries buttons for:",
  ["Irrigation and suction", "Cutting and coagulation", "Cutting only", "Coagulation only"], 1,
  "The handpiece is labelled Coagulation and Cutting. (Book p7)")
q(7, "Cautery Pad", "The cautery pad is placed over a:",
  ["Bony prominence", "Scarred area", "Poorly perfused area", "Well-vascularized area"], 3,
  "Cautery pad: Placed over well-vascularized area. (Book p7)")
q(7, "Cautery Pad", "The cautery pad must have:",
  ["Point contact", "Wide area of contact", "Minimal contact", "No direct skin contact"], 1,
  "Have wide area of contact. (Book p7)")
q(7, "Cautery Pad", "A small cautery pad causes:",
  ["Faster cutting", "Better coagulation", "Burns at site", "No effect"], 2,
  "Small cautery pad: Burns at site. (Book p7)")
q(7, "Cautery Pad", "With no cautery pad, the circuit is incomplete and:",
  ["Only cutting works", "Only coagulation works", "Bipolar takes over", "Monopolar will not work"], 3,
  "No cautery pad: Circuit incomplete -> monopolar will not work. (Book p7)")

# ---------------- p7 · MONOPOLAR HAZARDS / USES / AVOIDANCE ----------------
q(7, "Monopolar Cautery", "Lateral spread of current in monopolar cautery causes:",
  ["Thermal damage to nearby structures", "Faster healing", "Reduced bleeding elsewhere", "Cooling of the field"], 0,
  "Disadvantage: Lateral spread of current -> Thermal damage to nearby structures. (Book p7)")
q(7, "Monopolar Cautery", "Monopolar current interferes with:",
  ["Renal function", "Hepatic blood flow", "Cardiac conduction", "Gut motility"], 2,
  "Current interferes with cardiac conduction. (Book p7)")
q(7, "Monopolar Cautery", "Because it interferes with cardiac conduction, monopolar cautery is avoided in patients with:",
  ["Diabetes", "Hypertension", "Cardiac pacemakers", "Asthma"], 2,
  "Avoid in patients with cardiac pacemakers. (Book p7)")
q(7, "Monopolar Cautery", "Current applied over a pedicle undergoes:",
  ["Dissipation", "Channelisation of current", "Reflection", "Absorption"], 1,
  "Pedicle -> Channelisation of current. (Book p7)")
q(7, "Monopolar Cautery", "In a pedicle, the channelled current:",
  ["Stays at the tip", "Returns directly to the machine", "Spreads to the skin", "Runs to base"], 3,
  "Current runs to base. (Book p7)")
q(7, "Monopolar Cautery", "Monopolar cautery is avoided close to:",
  ["Large veins", "End arteries", "Skin surface", "Fat planes"], 1,
  "Avoid close to end arteries. (Book p7)")
q(7, "Monopolar Cautery", "The uses of monopolar cautery are:",
  ["Cutting and coagulation", "Coagulation only", "Cutting only", "Vessel sealing only"], 0,
  "Uses: Cutting and Coagulation. (Book p7)")
q(7, "Monopolar Cautery", "Monopolar cautery is avoided in all of the following EXCEPT:",
  ["CNS surgery", "Parotid / Thyroid surgery", "Ear lobule", "Subcutaneous lipoma excision"], 3,
  "Avoided in: CNS Sx, Parotid/Thyroid Sx, Ear lobule, Penile region, Patient with Pacemakers. (Book p7)")
q(7, "Monopolar Cautery", "Which of the following regions is listed for avoidance of monopolar cautery?",
  ["Abdominal wall", "Thigh", "Back", "Penile region"], 3,
  "Avoided in: CNS Sx, Parotid/Thyroid Sx, Ear lobule, Penile region, Patient with Pacemakers. (Book p7)")
q(7, "Monopolar Cautery", "Parotid / Thyroid surgery appears in the book under:",
  ["Sites where monopolar cautery is avoided", "Uses of bipolar cautery", "Uses of the harmonic scalpel", "Sites for the grounding pad"], 0,
  "Avoided in: CNS Sx, Parotid/Thyroid Sx, Ear lobule, Penile region, Patient with Pacemakers. (Book p7)")

# ---------------- p7-p8 · BIPOLAR ----------------
q(7, "Bipolar Cautery", "In bipolar cautery, the circuit is:",
  ["Completed via a pad", "Completed via earth", "Completed locally", "Left open"], 2,
  "Bipolar cautery: Circuit completed locally. (Book p7)")
q(7, "Bipolar Cautery", "The bipolar instrument has:",
  ["One prong", "Two prongs", "A pad", "A grounding wire"], 1,
  "Two prongs complete the circuit locally. (Book p7)")
q(8, "Bipolar Cautery", "An advantage of bipolar cautery is:",
  ["Grounding pad needed", "Two pads needed", "No cautery pad required", "Works only with large pads"], 2,
  "Advantages: No cautery pad required. (Book p8)")
q(8, "Bipolar Cautery", "Bipolar cautery is safe:",
  ["Only on skin", "Only in open surgery", "Close to vital structures and end arteries", "Only for large vessels"], 2,
  "Safe close to vital structure and end arteries. (Book p8)")
q(8, "Bipolar Cautery", "Bipolar cautery is used for:",
  ["Cutting only", "Cutting and coagulation", "Coagulation only", "Fulguration only"], 2,
  "Uses: Coagulation only. (Book p8)")

# ---------------- p8 · CURRENTS & WAVEFORMS ----------------
q(8, "Currents", "The cutting mode is a:",
  ["Low voltage, continuous current", "High voltage, alternating current", "Low voltage, interrupted current", "High voltage, continuous current"], 0,
  "Cutting mode: Low voltage, continuous current. (Book p8)")
q(8, "Currents", "Blend mode is a combination of:",
  ["Two cutting modes", "Two coagulation modes", "Cutting & coagulation mode", "Cutting & fulguration only"], 2,
  "Blend mode: Combination of cutting & coagulation mode. (Book p8)")
q(8, "Currents", "The coagulation mode is a:",
  ["Low voltage, continuous current", "High voltage, alternating current", "Low voltage, direct current", "High voltage, direct current"], 1,
  "Coagulation mode: High voltage, alternating current. (Book p8)")
q(8, "Currents", "Fulguration mode is:",
  ["A cutting mode", "A type of coagulation with higher voltage peaks", "A blend of two cutting modes", "An ultrasonic mode"], 1,
  "Fulguration mode: Type of coagulation with higher voltage peaks. (Book p8)")
q(8, "Currents", "The fulguration waveform is labelled with:",
  ["Peak voltage and average voltage", "Current and resistance", "Frequency and wavelength", "Power and energy"], 0,
  "Fulguration waveform labels Peak voltage and Average voltage. (Book p8)")
q(8, "Currents", "Cutting current acts by heat causing:",
  ["Dehydration + protein denaturation", "Slow desiccation", "Cell water explosion", "Protein cross-linking only"], 2,
  "Cutting current: Heat -> Cell water explosion. (Book p8)")
q(8, "Currents", "Coagulation current causes:",
  ["Cell water explosion", "Dehydration + protein denaturation", "Slow vaporization", "Tissue freezing"], 1,
  "Coagulation current: Dehydration + Protein Denaturation. (Book p8)")
q(8, "Currents", "Dehydration + protein denaturation by coagulation current leads to:",
  ["Cell swelling", "Cell division", "Cell repair", "Cell death"], 3,
  "Dehydration + Protein Denaturation -> Cell death. (Book p8)")

# ---------------- p8 · LIGASURE ----------------
q(8, "Ligasure", "Ligasure works by:",
  ["Ultrasound alone", "Cold + pressure", "Heat + pressure", "Microwaves"], 2,
  "Ligasure: Heat + pressure. (Book p8)")
q(8, "Ligasure", "Ligasure uses the body's _____ to seal & divide:",
  ["Water & fat", "Collagen & elastin", "Calcium & iron", "Fibrin & platelets"], 1,
  "Uses body collagen & elastin to seal & divide. (Book p8)")
q(8, "Ligasure", "The feedback mechanism in Ligasure:",
  ["Cools the tissue", "Regulates energy delivery", "Increases smoke", "Delays sealing"], 1,
  "Feedback mechanism: Regulate energy delivery. (Book p8)")
q(8, "Ligasure", "On seal closure, Ligasure shows:",
  ["Continued heating", "Alarm only", "Manual reset need", "Automatic discontinuation"], 3,
  "Automatic discontinuation on seal closure. (Book p8)")
q(8, "Ligasure", "Ligasure is used for vessels till _____ diameter:",
  ["3 mm", "3 cm", "7 mm", "14 mm"], 2,
  "Used till 7mm diameter. (Book p8)")
q(8, "Ligasure", "A disadvantage of Ligasure is that it:",
  ["Needs a grounding pad", "Cannot be used close to vital structures", "Works only in open surgery", "Cannot seal vessels"], 1,
  "Disadvantage: cannot be used close to vital structures. (Book p8)")

# ---------------- p8-p9 · HARMONIC SCALPEL ----------------
q(8, "Harmonic Scalpel", "The harmonic scalpel works on the:",
  ["Electrocautery principle", "Ultrasonic principle", "Laser principle", "Cryotherapy principle"], 1,
  "Works on ultrasonic principle. (Book p8)")
q(8, "Harmonic Scalpel", "The oscillatory blade oscillates between:",
  ["2000-50000 Hz", "50-60 Hz", "500-1000 Hz", "1-2 MHz"], 0,
  "Oscillatory blade: Oscillates between 2000-50000 Hz. (Book p8)")
q(8, "Harmonic Scalpel", "The harmonic scalpel produces:",
  ["Heat + cell water explosion", "Protein denaturation + coagulation without heat production", "Dehydration with high heat", "Char + smoke"], 1,
  "Protein denaturation + coagulation without heat production. (Book p8)")
q(9, "Harmonic Scalpel", "An advantage of the harmonic scalpel is that it:",
  ["Needs a grounding pad", "Can be used close to vital structures", "Seals 7 mm vessels", "Works by heat + pressure"], 1,
  "Advantages: Can be used close to vital structures. (Book p9)")
q(9, "Harmonic Scalpel", "Which of the following is an advantage of the harmonic scalpel?",
  ["Precise cuts", "Needs large pads", "High heat spread", "Slow sealing only"], 0,
  "Advantages: Precise cuts. (Book p9)")
q(9, "Harmonic Scalpel", "The harmonic scalpel can:",
  ["Cut through scar tissue", "Replace all sutures", "Work without power", "Ablate 3 cm tumours"], 0,
  "Advantages: Cut through scar tissue. (Book p9)")
q(9, "Harmonic Scalpel", "A disadvantage of the harmonic scalpel is that it is:",
  ["Unsafe near vital structures", "Imprecise", "Time consuming", "Heat producing"], 2,
  "Disadvantages: Time consuming. (Book p9)")

# ---------------- p9 · CUSA & THUNDERBEAT ----------------
q(9, "CUSA", "CUSA is a type of:",
  ["Monopolar cautery", "Bipolar cautery", "Harmonic scalpel", "Laser"], 2,
  "CUSA: Type of harmonic scalpel. (Book p9)")
q(9, "CUSA", "CUSA is used for:",
  ["Thyroid surgery", "CNS surgery", "Liver resection", "Skin incisions"], 2,
  "Used for liver resection. (Book p9)")
q(9, "CUSA", "During CUSA, hepatocytes are susceptible to oscillatory fragmentation because of their:",
  ["High fat content", "Low blood supply", "Dense fibrosis", "High water content and collagen"], 3,
  "Hepatocytes susceptible to oscillatory fragmentation d/t high water content and collagen. (Book p9)")
q(9, "CUSA", "CUSA works better in:",
  ["Cirrhotic liver", "Non-cirrhotic liver", "Fatty pancreas", "Fibrotic lung"], 1,
  "Better in non-cirrhotic liver. (Book p9)")
q(9, "CUSA", "CUSA can also:",
  ["Coagulate bone", "Aspirate gases", "Cut metal", "Place sutures"], 1,
  "Can aspirate gases as well. (Book p9)")
q(9, "CUSA", "Which of the following is a labelled part of the CUSA handpiece?",
  ["Power cable", "Laser fibre", "Bovie tip", "Grounding pad"], 0,
  "CUSA handpiece: CUSA tip, Irrigation port, Suction port, Power cable. (Book p9)")
q(9, "Thunderbeat S", "Thunderbeat S combines features of:",
  ["Monopolar + Bipolar", "Ligasure + Harmonic Scalpel", "RFA + Microwave", "CUSA + Laser"], 1,
  "Features of both Ligasure + Harmonic Scalpel. (Book p9)")

# ---------------- p9 · RFA & MICROWAVE ----------------
q(9, "RFA", "Radio Frequency Ablation uses:",
  ["Low voltage continuous current", "Ultrasonic oscillation", "Microwaves", "High frequency, alternating current"], 3,
  "RFA: High frequency, alternating current. (Book p9)")
q(9, "RFA", "Similar to electrocautery, RFA needs a:",
  ["Kidney tray", "Second surgeon", "Grounding pad", "Cooling jacket"], 2,
  "Similar to electrocautery: Grounding pad needed. (Book p9)")
q(9, "RFA", "RFA is used for liver tumour resection upto:",
  ["3 mm", "7 mm", "3 cm", "10 cm"], 2,
  "Use: Liver tumor resection upto 3 cm. (Book p9)")
q(9, "Microwave", "Microwaves lie between:",
  ["X-rays & gamma rays", "Infra-red & radiowaves", "UV & visible light", "Sound & ultrasound"], 1,
  "Between infra-red & radiowaves. (Book p9)")
q(9, "Microwave", "Microwave ablation acts by:",
  ["Cell water explosion", "Protein freezing", "Ionizing radiation", "Oscillation & frictional heat"], 3,
  "Oscillation & frictional heat. (Book p9)")
q(9, "Microwave", "An advantage of microwave ablation is:",
  ["Grounding pad needed", "No grounding pad required", "Longer time than RFA", "Patchy ablation"], 1,
  "Advantages: No grounding pad required. (Book p9)")
q(9, "Microwave", "Compared to RFA, microwave ablation takes:",
  ["More time", "Equal time", "Less time than RFA", "Double the time"], 2,
  "Advantages: Less time than RFA. (Book p9)")
q(9, "Microwave", "Microwave ablation produces a:",
  ["Patchy zone of ablation", "Narrow line burn", "Surface burn only", "Homogenous zone of ablation"], 3,
  "Homogenous zone of ablation. (Book p9)")

# ---------------- UNITS ----------------
def uid(n): return {"id": f"SURG-U2-{n}", "ch": 2, "n": n}
def rng(a, b): return [f"SURG-C2-{i:03d}" for i in range(a, b + 1)]
UNITS = [
    {**uid(1), "title": "Types of Surgical Blades", "sec": "Blades \u00b7 p6",
     "qs": rng(1, 8),
     "guide": "Blades exist to make incisions, and the belly is the sharpest part. The pointed No. 11 stab blade opens abscesses and arteries, while the curved No. 12 slips under sutures to remove them - with No. 10, 15, 22 and 23 completing the tray."},
    {**uid(2), "title": "Blade Handling & the BP Handle", "sec": "Blade Handling \u00b7 p6",
     "qs": rng(9, 11),
     "guide": "Sharps travel safely in a kidney tray with the pointed end facing the passer, never the surgeon. Every blade clicks onto the familiar BP (Bard Parker) handle before it touches skin."},
    {**uid(3), "title": "Incisions & Langer's Lines", "sec": "Incisions \u00b7 p6",
     "qs": rng(12, 20),
     "guide": "Cut perpendicular to skin, travelling far to near. Respect Langer's relaxed tension lines - the grain of dermal collagen - because parallel incisions heal into fine scars, hide in creases, spare anatomical structures and still give adequate access."},
    {**uid(4), "title": "Monopolar Cautery: Circuit & Cautery Pad", "sec": "Monopolar Cautery \u00b7 p7",
     "qs": rng(21, 28),
     "guide": "Current sprints from machine to Bovie tip, through tissue, body and pad, then home to the machine. That pad must sit broad on well-vascularized skin - shrink it and you burn the patient, skip it and monopolar simply will not work."},
    {**uid(5), "title": "Monopolar Cautery: Hazards, Uses & Avoidance", "sec": "Monopolar Cautery \u00b7 p7",
     "qs": rng(29, 38),
     "guide": "Monopolar cuts and coagulates, but its current wanders - scorching neighbours, confusing pacemakers and channelling down pedicles to their base. Keep it away from end arteries, the CNS, parotid and thyroid, the ear lobule, the penis and any paced heart."},
    {**uid(6), "title": "Bipolar Cautery", "sec": "Bipolar Cautery \u00b7 p7",
     "qs": rng(39, 43),
     "guide": "Bipolar current hops between two prongs and finishes its circuit right there in the forceps tips. With no pad and no stray current, it coagulates safely beside vital structures and end arteries - but it only coagulates, never cuts."},
    {**uid(7), "title": "Currents & Waveforms", "sec": "Currents \u00b7 p8",
     "qs": rng(44, 51),
     "guide": "Low-voltage continuous waves slice by exploding cell water; high-voltage interrupted waves desiccate and denature protein until the cell dies. Blend mixes the two, while fulguration spikes the voltage peaks higher still."},
    {**uid(8), "title": "Ligasure", "sec": "Ligasure \u00b7 p8",
     "qs": rng(52, 57),
     "guide": "Ligasure squeezes vessels with heat plus pressure, melting the body's own collagen and elastin into a seal, then stops itself the instant the seal closes. A live feedback loop meters every joule - good till 7 mm, but keep it away from vital structures."},
    {**uid(9), "title": "Harmonic Scalpel", "sec": "Harmonic Scalpel \u00b7 p8",
     "qs": rng(58, 64),
     "guide": "The harmonic blade shivers 2,000 to 50,000 times a second, denaturing protein and coagulating without heat. It carves precisely, even through scar and beside vital structures - at the price of patience, because it is slow."},
    {**uid(10), "title": "CUSA & Thunderbeat S", "sec": "CUSA \u00b7 p9",
     "qs": rng(65, 71),
     "guide": "CUSA is a harmonic scalpel that crumbles watery hepatocytes for liver resection - happiest in a soft, non-cirrhotic liver - while sucking debris and even gases away. Thunderbeat S then marries Ligasure's sealing to the harmonic's cut in one jaw."},
    {**uid(11), "title": "RFA & Microwave Ablation", "sec": "RFA & Microwave \u00b7 p9",
     "qs": rng(72, 79),
     "guide": "RFA burns liver tumours up to 3 cm with high-frequency alternating current, grounding pad and all. Microwaves, humming between infra-red and radiowaves, need no pad, finish faster and leave a smooth homogenous kill zone."},
]

data = {"questions": Q, "units": UNITS}
with open("data/ch2.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
print(f"ch2: {len(Q)} questions, {len(UNITS)} units")
