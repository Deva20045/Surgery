#!/usr/bin/env python3
"""Build data/ch49.json — Minimally Invasive Surgery (Marrow Surgery Ed 8, pp371-376)."""
import json

Q = []

def q(page, sec, text, correct, wrongs, note=None):
    opts = [correct] + list(wrongs)
    assert len(opts) == 4
    Q.append({
        "id": f"SURG-C49-{len(Q)+1:03d}",
        "sec": sec,
        "page": page,
        "q": text,
        "opts": opts,
        "ans": 0,
        "exp": (note or correct) + f" (Book p{page})",
    })

# ------------------------------------------------------------------ p371
S1 = "Advantages and Basic Principle"
q(371, S1, "An advantage of minimally invasive surgery is:", "Decrease in wound size", ["Increase in wound size", "Longer hospital stay", "More wound pain"])
q(371, S1, "Minimally invasive surgery reduces:", "Wound infection", ["Wound healing", "Visualization", "Mobility"])
q(371, S1, "An advantage of minimally invasive surgery is reduction in:", "Wound dehiscence", ["Operative vision", "Instrument cost", "Learning curve"])
q(371, S1, "Minimally invasive surgery reduces:", "Bleeding", ["Visualization", "Mobility", "Insufflation"])
q(371, S1, "An advantage of minimally invasive surgery is reduction in:", "Herniation", ["Retraction", "Triangulation", "Inspection"])
q(371, S1, "Minimally invasive surgery reduces:", "Nerve entrapment", ["Wound infection only", "Operative time always", "Anaesthesia need"])
q(371, S1, "An advantage of minimally invasive surgery is:", "Decrease in wound pain", ["Increase in wound pain", "Increased heat loss", "Poor visualization"])
q(371, S1, "Minimally invasive surgery gives:", "Improved mobility", ["Reduced mobility", "Prolonged bed rest", "Delayed recovery"])
q(371, S1, "An advantage of minimally invasive surgery is:", "Decreased wound trauma", ["Increased wound trauma", "Larger incisions", "More blood loss"])
q(371, S1, "Minimally invasive surgery causes:", "Decreased heat loss", ["Increased heat loss", "Hypothermia always", "Hyperthermia"])
q(371, S1, "An advantage of minimally invasive surgery is:", "Improved visualization", ["Poor visualization", "No magnification", "Blind surgery"])
q(371, S1, "The basic principle mnemonic for minimally invasive surgery is:", "IVITROS", ["VITROS", "TROSIV", "ROSIVT"])
q(371, S1, "The first step of IVITROS is:", "Insufflate", ["Visualize", "Inspect", "Seal"])
q(371, S1, "IVITROS includes:", "Visualization", ["Ventilation", "Vaccination", "Vagotomy"])
q(371, S1, "IVITROS includes:", "Inspection", ["Insufflation only", "Incision only", "Irrigation only"])
q(371, S1, "IVITROS includes:", "Triangulation", ["Truncation", "Transplantation", "Tracheostomy"])
q(371, S1, "IVITROS includes:", "Retraction of tissues", ["Removal of organs", "Resection always", "Radiation"])
q(371, S1, "IVITROS includes:", "Operation", ["Observation only", "Obliteration", "Occlusion"])
q(371, S1, "The last step of IVITROS is:", "Seal", ["Suture only", "Staple only", "Suction"])

# ------------------------------------------------------------------ p371-372
S2 = "Pneumoperitoneum and Physiological Effects"
q(371, S2, "Pneumoperitoneum is:", "Gas inside peritoneal cavity", ["Fluid inside pleural cavity", "Air inside pericardium", "Gas inside joint"])
q(371, S2, "The most common distension medium is:", "CO2 at 10–14 mmHg", ["Air at 20 mmHg", "Oxygen at 5 mmHg", "Nitrogen at 30 mmHg"])
q(371, S2, "Sometimes used as distension medium instead of CO2 is:", "Nitrous oxide", ["Air", "Oxygen", "Helium"])
q(371, S2, "Gases not used for pneumoperitoneum are:", "Air, O2", ["CO2, nitrous oxide", "Helium, argon", "Xenon, krypton"])
q(371, S2, "Air and O2 are not used because they:", "Support combustion", ["Are too costly", "Cause hypothermia", "Are radio-opaque"])
q(371, S2, "Peritoneal stretching causes:", "Vagal stimulation", ["Sympathetic stimulation", "Phrenic stimulation", "Somatic stimulation"])
q(371, S2, "Vagal stimulation during pneumoperitoneum causes:", "Sinus bradycardia", ["Sinus tachycardia", "Atrial fibrillation", "Ventricular tachycardia"])
q(371, S2, "The most common arrhythmia in pneumoperitoneum is:", "Sinus bradycardia", ["Sinus tachycardia", "Heart block", "VF"])
q(371, S2, "Increased intra-abdominal pressure presses the:", "IVC", ["Aorta", "Portal vein", "Carotid artery"])
q(371, S2, "IVC compression decreases:", "Venous return", ["Arterial pressure directly", "Heart rate first", "Airway resistance"])
q(371, S2, "Decreased venous return decreases:", "Cardiac output (CO)", ["Airway resistance", "Intracranial tension", "Urine output first"])
q(371, S2, "With falling cardiac output, heart rate initially:", "Decreases, later hypotension + reflex tachycardia", ["Increases immediately", "Stays normal", "Becomes irregular always"])
q(372, S2, "Pneumoperitoneum pushes the diaphragm up causing:", "Decreased thoracic volume", ["Increased thoracic volume", "Decreased airway resistance", "Decreased intrathoracic pressure"])
q(372, S2, "Decreased thoracic volume increases:", "Airway Resistance", ["Lung compliance", "Tidal volume", "Venous return"])
q(372, S2, "Pneumoperitoneum increases:", "Intrathoracic pressure", ["Thoracic volume", "Lung volumes", "Cardiac output"])
q(372, S2, "In a COPD patient, pneumoperitoneum causes:", "Further reduction in lung volumes", ["Improved lung volumes", "No change", "Bronchodilatation"])
q(372, S2, "To ventilate the lung in COPD, increase:", "PEEP (Peak end expiratory pressure)", ["Tidal volume only", "Respiratory rate to zero", "FiO2 to zero"])
q(372, S2, "Decreased urine output in pneumoperitoneum is due to increased pressure over:", "Renal vessels", ["Ureters", "Bladder", "Urethra"])
q(372, S2, "Pressure over renal vessels decreases:", "Renal blood flow", ["Renal oxygen demand", "Bladder pressure", "Ureteric peristalsis"])
q(372, S2, "Pneumoperitoneum increases:", "Intracranial Tension", ["Renal blood flow", "Venous return", "Thoracic volume"])

# ------------------------------------------------------------------ p372-373
S3 = "Creating Pneumoperitoneum: Blind, Open and Trocars"
q(372, S3, "A method of creating pneumoperitoneum is the:", "Blind method", ["Sealed method", "Gasless method", "Vacuum method"])
q(372, S3, "The other method of creating pneumoperitoneum is the:", "Open method", ["Blind method", "Closed method", "Needle method"])
q(372, S3, "The blind method uses the:", "Veress needle", ["Hasson trocar", "Foley catheter", "Sengstaken tube"])
q(372, S3, "Confirmation of Veress needle position: drop of saline if sucked confirms the needle is in the:", "Peritoneal cavity", ["Bowel lumen", "Bladder", "Blood vessel"])
q(372, S3, "Confirmation of Veress needle: inject saline shows:", "No aspirate", ["Blood aspirate", "Faecal aspirate", "Bile aspirate"])
q(372, S3, "Flow of CO2 during insufflation is:", "1–4 Litres/min", ["10–14 Litres/min", "100 ml/min", "20 Litres/min"])
q(372, S3, "The most common site of Veress needle insertion is:", "Infraumbilical", ["Supraumbilical", "Palmer's point", "McBurney's point"])
q(372, S3, "Palmer's point is:", "3 cm below left costal margin (midclavicular line)", ["3 cm below right costal margin", "At the umbilicus", "In the right iliac fossa"])
q(372, S3, "The Veress needle tip has a:", "Bevelled edge", ["Blunt rounded end", "Transparent window", "Balloon tip"])
q(372, S3, "The Veress needle has an outer barrel with a:", "Sharp, bevelled point", ["Blunt plastic tip", "Lighted end", "Suction channel"])
q(372, S3, "In the open (Hasson's) method, the peritoneum is:", "Incised under vision", ["Punctured blindly", "Left intact", "Stapled"])
q(372, S3, "The advantage of the open method is:", "Less chance of injury", ["Faster technique", "No scar", "Cheaper instruments"])
q(372, S3, "The disadvantage of the open method is:", "Time consuming", ["More injuries", "Blind entry", "No visualization"])
q(372, S3, "An indication for the open method is:", "Previous abdominal Sx", ["No prior surgery", "Thin patient", "Emergency only"])
q(372, S3, "The open method is indicated in:", "Pregnant patients", ["COPD patients", "Children only", "Elderly only"])
q(372, S3, "In laparoscopy, the trocar inserted blindly is:", "Only 1st trocar", ["All trocars", "No trocar", "Only the last trocar"])
q(372, S3, "The open method uses:", "Hasson's Trocar (Blunt)", ["Sharp trocar", "Veress needle", "Optical trocar"])
q(372, S3, "The blind method uses a:", "Sharp trocar", ["Blunt trocar", "Plastic catheter", "Glass rod"])
q(373, S3, "Bowel injury during trocar insertion is managed by:", "Convert to open Sx", ["Continue laparoscopy", "Only antibiotics", "Observation"])
q(373, S3, "In bowel injury, keep the trocar in position because it:", "Seals the perforation", ["Enlarges the injury", "Prevents anaesthesia", "Causes sepsis"])
q(373, S3, "Keeping the trocar in position also:", "Helps locate injury", ["Hides the injury", "Delays surgery", "Increases bleeding"])
q(373, S3, "The bladeless optical trocar is called:", "Optiport / visiport", ["Hasson port", "SILS port", "Hand port"])
q(373, S3, "In the optical trocar, a camera is inserted giving a:", "Lesser chance of injury", ["Greater chance of injury", "Blind entry", "Longer surgery"])
q(373, S3, "The optical trocar has a:", "Transparent end", ["Bevelled sharp end", "Balloon end", "Metal blunt end"])

# ------------------------------------------------------------------ p373-374
S4 = "Laparoscopic Instruments, Angles and Limitations"
q(373, S4, "Triangulation means instruments are introduced into trocars from:", "Different angles", ["The same angle", "One port only", "Opposite organs"])
q(373, S4, "Triangulation prevents:", "Clash of instruments", ["Bleeding", "Infection", "Hernia"])
q(373, S4, "The azimuth angle is the angle between:", "Camera and instruments", ["Two instruments", "Instrument and floor", "Ports and bowel"])
q(373, S4, "The azimuth angle is:", "30°", ["60°", "90°", "15°"])
q(373, S4, "The manipulation angle is the angle between:", "Two instruments", ["Camera and instruments", "Instrument and floor", "Trocar and skin"])
q(373, S4, "The manipulation angle is:", "60°", ["30°", "90°", "120°"])
q(373, S4, "The elevation angle is:", "60°", ["30°", "90°", "10°"])
q(373, S4, "Laparoscopic instruments have:", "Insulation (black coat)", ["No insulation", "Metal exposure fully", "Glass coating"])
q(374, S4, "A limitation of laparoscopy is:", "Lack of 3D vision", ["3D vision", "Tactile feedback excess", "Low cost"])
q(374, S4, "A limitation of laparoscopy is:", "Loss of tactile feedback", ["Extra tactile feedback", "Improved haemostasis", "Short learning curve"])
q(374, S4, "A limitation of laparoscopy is:", "Haemostasis", ["Pneumoperitoneum", "Triangulation", "Insufflation"])
q(374, S4, "If bleeding occurs during laparoscopy:", "Coagulate", ["Convert always", "Abandon surgery", "Only observe"])
q(374, S4, "For laparoscopic bleeding, insert gauze and:", "Apply pressure", ["Remove ports", "Deflate abdomen", "Give heparin"])
q(374, S4, "Topical haemostats used in laparoscopy include:", "Botroclot/surgicel", ["Heparin/warfarin", "Aspirin/clopidogrel", "Streptokinase"])
q(374, S4, "A limitation of laparoscopy is:", "Extraction of large specimens", ["Small incisions", "Less pain", "Fast recovery"])
q(374, S4, "A limitation of laparoscopy is:", "Longer learning curve", ["Short learning curve", "No training needed", "Easy mastery"])
q(374, S4, "A limitation of laparoscopy is:", "Cost", ["Cheap instruments", "No equipment", "Free surgery"])
q(374, S4, "A limitation of laparoscopy is:", "Reliance on new technologies", ["No technology needed", "Open instruments only", "No electricity"])
q(374, S4, "Capacitance coupling starts with:", "Insulation break", ["Plastic trocar", "Low voltage", "Direct cut"])
q(374, S4, "Insulation break causes:", "Leak of current through trocar", ["No current flow", "Improved coagulation", "Camera failure"])
q(374, S4, "Current leak through a metallic trocar means:", "Bowel can get burnt", ["Skin gets burnt only", "No injury", "Trocar melts"])
q(374, S4, "Capacitance coupling is prevented by:", "Maintain insulation", ["Breaking insulation", "Using metallic trocars", "Increasing current"])
q(374, S4, "To prevent capacitance coupling use a:", "Plastic Trocar", ["Metallic trocar", "Sharp trocar", "Glass trocar"])
q(374, S4, "CO2 retention is seen in:", "Laparoscopic cholecystectomy", ["Open cholecystectomy", "Laparoscopic hernia only", "All open surgeries"])
q(374, S4, "The position causing CO2 retention is reverse Trendelenburg plus:", "Right side up", ["Left side up", "Head down", "Lithotomy"])
q(374, S4, "Reverse Trendelenburg means:", "Head end up, foot end low", ["Head end low, foot end up", "Lateral position", "Prone position"])
q(374, S4, "CO2 is retained beneath the:", "Right dome of diaphragm", ["Left dome of diaphragm", "Pelvis", "Liver bed"])
q(374, S4, "Retained CO2 irritates the diaphragm causing referred pain to the:", "Right shoulder tip", ["Left shoulder tip", "Chest centre", "Back"])
q(374, S4, "Right shoulder tip pain is the:", "Most common complication", ["Rarest complication", "Fatal complication", "Vascular complication"])

# ------------------------------------------------------------------ p374-375
S5 = "Trocar Bleeding, Conventional Laparoscopy, SILS and Hand Port"
q(374, S5, "Bleeding from the trocar site is managed with:", "Sutures on either side of trocar to ligate vessel", ["Only pressure forever", "Heparin infusion", "No treatment"])
q(374, S5, "For trocar site bleeding, elongate the incision to:", "Tie the vessel", ["Insert bigger trocar", "Remove the port", "Close the skin"])
q(374, S5, "Trocar site bleeding can be tamponaded with:", "Foley's catheter through port site then Inflate", ["Nasogastric tube", "Veress needle", "Drain pipe"])
q(375, S5, "Conventional laparoscopy uses:", "Multiple ports", ["Single port", "No ports", "Hand port only"])
q(375, S5, "Conventional laparoscopic ports include a:", "12 mm port", ["24 mm port", "2 mm port", "30 mm port"])
q(375, S5, "Conventional laparoscopy uses:", "5 mm ports", ["15 mm ports", "20 mm ports", "1 mm ports"])
q(375, S5, "The laparoscopy team includes the:", "Anesthesiologist", ["Cardiologist", "Nephrologist", "Dermatologist"])
q(375, S5, "The laparoscopy team setup includes:", "Surgeon and Assistant with Monitors and Mayo stand", ["Only the surgeon", "No monitors", "No assistant"])
q(375, S5, "SILS stands for:", "Single Incision Laparoscopic Sx", ["Single Instrument Liver Surgery", "Small Incision Lung Surgery", "Sterile Intraabdominal Lavage System"])
q(375, S5, "SILS uses an infraumbilical incision to insert the:", "SILS port", ["Hand port", "Veress needle", "Foley catheter"])
q(375, S5, "A disadvantage of SILS is:", "Clashing of instruments", ["Less pain", "Better cosmesis", "Fewer hernias"])
q(375, S5, "SILS increases the risk of:", "Hernia through the port site", ["Less infection", "Less bleeding", "No complications"])
q(375, S5, "An advantage of the hand port is:", "Better aid in dissection", ["Worse dissection", "No tactile feedback", "Smaller incision"])
q(375, S5, "The hand port facilitates:", "Tactile feedback", ["Loss of feedback", "Blind dissection", "Single port surgery"])
q(375, S5, "The hand port image labels the vessel as the:", "Renal artery", ["Renal vein", "Aorta", "IVC"])
q(375, S5, "The hand port image shows a:", "Stapler", ["Veress needle", "Foley catheter", "SILS port"])

# ------------------------------------------------------------------ p375-376
S6 = "NOTES and Robotic Surgery"
q(375, S6, "NOTES stands for:", "Natural Orifice Transluminal Endoscopic Sx", ["Natural Outer Tissue Excision Surgery", "Needle Operated Transverse Surgery", "Novel Organ Transplant System"])
q(375, S6, "The first NOTES step is:", "Mucosal entry", ["Submucosal tunnel", "Remove circular muscle layer", "Closure of mucosal entry"])
q(375, S6, "After mucosal entry in NOTES comes the:", "Submucosal tunnel", ["Mucosal closure", "Muscle removal", "Skin incision"])
q(375, S6, "NOTES then removes the:", "Circular muscle layer", ["Mucosa only", "Serosa only", "Skin"])
q(375, S6, "The last NOTES step is:", "Closure of mucosal entry", ["Mucosal entry", "Submucosal tunnel", "Muscle removal"])
q(376, S6, "A natural orifice for NOTES is the:", "Oral Cavity", ["Nasal cavity only", "Ear canal", "Eye"])
q(376, S6, "POEM stands for:", "Per Oral Endoscopic Myotomy", ["Peritoneal Open Excision Method", "Portal Endoscopic Mucosectomy", "Pancreatic Oral Excision Maneuver"])
q(376, S6, "POEM is done for:", "Achalasia cardia", ["Bariatric surgery", "Hysterectomy", "Cystectomy"])
q(376, S6, "TOGA stands for:", "Transoral Gastroplasty", ["Transanal Gland Ablation", "Thoracic Outlet Grafting", "Tubal Occlusion using Glue"])
q(376, S6, "TOGA is a:", "Bariatric Sx", ["Cardiac surgery", "Neurosurgery", "Transplant surgery"])
q(376, S6, "Oral cavity NOTES procedures include:", "ROSE", ["SILS", "TULIP", "HOLEP"])
q(376, S6, "Oral cavity NOTES procedures include:", "POSE", ["ROSE only", "SILS", "TURP"])
q(376, S6, "V-NOTES procedures through the vagina include:", "Cystectomy", ["Cholecystectomy", "Nephrectomy", "Splenectomy"])
q(376, S6, "V-NOTES procedures through the vagina include:", "Hysterectomy", ["Prostatectomy", "Thyroidectomy", "Mastectomy"])
q(376, S6, "Rectal NOTES is:", "TaTME (Transanal Total Mesorectal Excision)", ["TOGA", "POEM", "POSE"])
q(376, S6, "Robotic surgery is based on the:", "Master and slave concept", ["Single surgeon concept", "Blind surgery concept", "Open surgery concept"])
q(376, S6, "An advantage of robotic surgery is:", "3D vision", ["2D vision", "No vision", "Blind dissection"])
q(376, S6, "Robotic surgery gives more freedom of movement with:", "7 degrees of freedom", ["3 degrees of freedom", "2 degrees of freedom", "1 degree of freedom"])
q(376, S6, "More freedom of movement gives:", "Better dissection", ["Worse dissection", "More tremor", "Less precision"])
q(376, S6, "An advantage of robotic surgery is:", "Scaling of movement", ["Tremor increase", "Loss of vision", "High cost"])
q(376, S6, "An advantage of robotic surgery is:", "Tremor reduction", ["Tremor increase", "More bleeding", "Longer incisions"])
q(376, S6, "A disadvantage of robotic surgery is:", "High Cost", ["Low cost", "3D vision", "Tremor reduction"])
q(376, S6, "A disadvantage of robotic surgery is:", "Longer learning curve", ["Short learning curve", "Easy mastery", "No training"])
q(376, S6, "A disadvantage of robotic surgery is:", "Loss of tactile feedback", ["Extra feedback", "Better feel", "Hand port feel"])
q(376, S6, "The original robotic system is the:", "DaVinci Robotic system", ["SILS system", "NOTES system", "Hasson system"])

# ------------------------------------------------------------------ units
def first_page(title):
    return next(x["page"] for x in Q if x["sec"] == title)

UNIT_DEFS = [
    (S1, "Smaller wounds bring less infection, dehiscence, bleeding, herniation, nerve entrapment, pain, trauma and heat loss with better mobility and visualization. Memorize IVITROS in order: insufflate, visualize, inspect, triangulate, retract tissues, operate and seal."),
    (S2, "CO2 at 10–14 mmHg is the standard distension medium with nitrous oxide as backup, while air and oxygen are banned for supporting combustion. Peritoneal stretch vagally slows the heart into sinus bradycardia, IVC compression drops venous return and cardiac output with early bradycardia then hypotension and reflex tachycardia, the raised diaphragm shrinks thoracic volume and raises airway resistance and intrathoracic pressure needing extra PEEP in COPD, renal vessel pressure cuts urine output, and intracranial tension rises."),
    (S3, "Create pneumoperitoneum blind with the bevelled Veress needle confirmed by a sucked saline drop and no aspirate on injection at 1–4 L/min through an infraumbilical or Palmer's 3-cm-subcostal midclavicular entry, or open with Hasson's under-vision technique that trades time for safety in prior surgery and pregnancy. Only the first trocar goes blind with sharp blind versus blunt Hasson designs; a bowel hit means converting to open while leaving the trocar to seal and mark the hole, and optical Optiport/Visiport cameras with transparent tips cut injury further."),
    (S4, "Triangulate instruments from different angles to stop clashing, holding azimuth at 30° between camera and tools with manipulation and elevation each at 60°, and respect the black insulating coat. Laparoscopy is limited by flat vision, lost feel, haemostasis handled by coagulation, gauze pressure or Botroclot/Surgicel, big-specimen extraction, learning curve, cost and technology dependence; broken insulation leaking current through metal trocars burns bowel unless insulation is kept and plastic trocars used, and right-side-up reverse Trendelenburg traps CO2 under the right diaphragm to give the commonest complication of right shoulder-tip pain."),
    (S5, "Bleeding trocar sites are oversewn on both sides, tied through an elongated incision or tamponaded by an inflated Foley through the port. Conventional laparoscopy arrays 12-mm and 5-mm multiple ports around surgeon, assistant, anaesthesiologist, monitors and Mayo stand; SILS squeezes everything through one infraumbilical port at the price of clashing tools and port hernias, while a hand port restores dissection and tactile feedback as in the renal-artery stapler view."),
    (S6, "NOTES crosses natural orifices through mucosal entry, submucosal tunnel, circular-muscle removal and mucosal closure, reaching achalasia by POEM and bariatric work by TOGA/ROSE/POSE orally, cystectomy and hysterectomy vaginally, and total mesorectal excision transanally. Master-slave robotics adds 3D vision, seven degrees of dissecting freedom, motion scaling and tremor reduction against high cost, long learning and lost feel, originating with the DaVinci system."),
]

UNITS = []
for i, (title, guide) in enumerate(UNIT_DEFS, 1):
    UNITS.append({
        "id": f"SURG-U49-{i}",
        "ch": 49,
        "n": i,
        "title": title,
        "sec": f"{title} · p{first_page(title)}",
        "qs": [x["id"] for x in Q if x["sec"] == title],
        "guide": guide,
    })

covered = [x for u in UNITS for x in u["qs"]]
assert covered == [x["id"] for x in Q]
assert len(set(covered)) == len(covered)
with open("data/ch49.json", "w", encoding="utf-8") as f:
    json.dump({"questions": Q, "units": UNITS}, f, ensure_ascii=False, indent=1)
print(f"ch49: {len(Q)} questions, {len(UNITS)} units")
