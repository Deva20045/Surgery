#!/usr/bin/env python3
"""Build data/ch26.json for PULSE Surgery ch26 (Bariatric Surgery, book p179-183)."""
import json

Q = []
def q(page, sec, text, opts, ans, exp):
    Q.append({"id": f"SURG-C26-{len(Q)+1:03d}", "sec": sec, "page": page,
              "q": text, "opts": opts, "ans": ans, "exp": exp})

# ---------------- p179 · INDICATIONS ----------------
S1 = "Indications for Bariatric Surgery"
q(179, S1, "In the general population, bariatric surgery is indicated at a BMI of:",
  ["≥40 kg/m²", "≥30 kg/m²", "≥25 kg/m²", "≥50 kg/m²"], 0,
  "Indications - BMI in general population: ≥40 kg/m². (Book p179)")
q(179, S1, "In the general population, bariatric surgery is indicated at a BMI of ≥35 kg/m² when:",
  ["Obesity related complications are present", "The patient requests it",
   "The patient is over 50 years old", "There is a family history of obesity"], 0,
  "Indications: ≥35 kg/m² with obesity complications. (Book p179)")
q(179, S1, "Obesity related complications that justify surgery at a BMI of ≥35 kg/m² include all EXCEPT:",
  ["Peptic ulcer disease", "Diabetes mellitus",
   "Obstructive sleep apnoea / Pickwickian syndrome", "Hyperlipidemia"], 0,
  "Obesity complications: DM, obstructive sleep apnea (OSA)/Pickwickian syndrome, hyperlipidemia, osteoarthritis. (Book p179)")
q(179, S1, "In the general population, surgery is also indicated at a BMI of 30-34.9 kg/m² when:",
  ["Type 2 diabetes mellitus is present (within 10 years)",
   "There is hypertension alone", "There is osteoarthritis", "The patient is a smoker"], 0,
  "Indications: 30-34.9 kg/m² with type 2 DM within 10 years. (Book p179)")
q(179, S1, "In the Asian population, bariatric surgery is indicated at a BMI of:",
  ["≥37.5 kg/m²", "≥40 kg/m²", "≥30 kg/m²", "≥45 kg/m²"], 0,
  "BMI in Asian population: ≥37.5 kg/m². (Book p179)")
q(179, S1, "In the Asian population, bariatric surgery is indicated at a BMI of ≥32.5 kg/m² when:",
  ["Obesity related complications are present", "There is no complication",
   "The patient is above 60 years", "There is a history of smoking"], 0,
  "BMI in Asian population: ≥32.5 kg/m² with complications. (Book p179)")

# ---------------- p179 · PRE-OP ----------------
S2 = "Pre-operative Considerations"
q(179, S2, "Before bariatric surgery a liver shrinkage diet is advised. It is:",
  ["Low carbohydrate and high protein", "High carbohydrate and low protein",
   "High fat and low protein", "A pure liquid fat free diet"], 0,
  "Liver shrinkage diet: low carbohydrate, high protein (at least 2 weeks). (Book p179)")
q(179, S2, "The liver shrinkage diet is given for at least:",
  ["2 weeks", "1 day", "6 weeks", "3 months"], 0,
  "Liver shrinkage diet: low carbohydrate, high protein (at least 2 weeks). (Book p179)")
q(179, S2, "A patient who is non-adherent to the pre-operative diet should be:",
  ["Referred for psychotherapy", "Operated on immediately", "Given a larger calorie allowance",
   "Started on TPN"], 0,
  "Refer to psychotherapy if inadherent to diet. (Book p179)")
q(179, S2, "Smoking cessation before bariatric surgery should be done at least:",
  ["4-6 weeks prior", "1 day prior", "2 days prior", "24 hours prior"], 0,
  "Smoking cessation: at least 4-6 weeks prior. (Book p179)")
q(179, S2, "Obstructive sleep apnoea in a bariatric patient is:",
  ["An independent risk factor for cardiac mortality", "Irrelevant to outcome",
   "Only a marker of obesity", "A contra-indication to surgery"], 0,
  "OSA patients: independent risk factor for cardiac mortality. (Book p179)")
q(179, S2, "After bariatric surgery, patients with obstructive sleep apnoea have an increased risk of:",
  ["Anastomotic leak", "Bleeding", "Wound infection", "Incisional hernia"], 0,
  "Post Sx: ↑ risk of anastomotic leak in OSA patients. (Book p179)")
q(179, S2, "Pre-operative preparation for bariatric surgery includes all EXCEPT:",
  ["Routine total parenteral nutrition", "Proper counselling",
   "Dietary and lifestyle changes", "Smoking cessation"], 0,
  "Pre-op considerations: proper counselling; dietary & lifestyle changes; liver shrinkage diet; smoking cessation; oxygen in OSA patients. (Book p179)")

# ---------------- p179 · OS-MRS ----------------
S3 = "OS-MRS: Obesity Surgery Mortality Risk Score"
q(179, S3, "OS-MRS stands for:",
  ["Obesity surgery mortality risk score", "Obesity surgery morbidity risk score",
   "Operative surgical mortality risk score", "Obesity surgical morbidity rating score"], 0,
  "OS-MRS: obesity surgery mortality risk score. (Book p179)")
q(179, S3, "Risk factors included in the OS-MRS include all EXCEPT:",
  ["Diabetes mellitus", "Arterial hypertension", "Age > 45 years", "Male gender"], 0,
  "OS-MRS risk factors: arterial hypertension, age > 45, male gender, BMI > 50 kg/m², risk factors for pulmonary thromboembolism. (Book p179)")
q(179, S3, "The BMI cut-off used in the OS-MRS is:",
  [">50 kg/m²", ">40 kg/m²", ">35 kg/m²", ">30 kg/m²"], 0,
  "OS-MRS: body mass index > 50 kg/m². (Book p179)")
q(179, S3, "The age cut-off used in the OS-MRS is:",
  [">45 years", ">60 years", ">35 years", ">50 years"], 0,
  "OS-MRS: age > 45. (Book p179)")

# ---------------- p180 · MECHANISMS & IRREVERSIBLE SURGERIES ----------------
S4 = "Mechanisms of Weight Loss and Irreversible Procedures"
q(180, S4, "Bariatric surgery produces weight loss by all of the following EXCEPT:",
  ["Increasing gastric acid secretion", "Malabsorption", "Restriction of volume",
   "Hormonal changes with a decrease in ghrelin"], 0,
  "Bariatric Sx causes weight loss through: malabsorption; restriction of volume; hormonal changes - ↓ ghrelin. (Book p180)")
q(180, S4, "The hormonal change responsible for weight loss after bariatric surgery is:",
  ["A decrease in ghrelin", "An increase in ghrelin", "A decrease in insulin",
   "An increase in gastrin"], 0,
  "Hormonal changes: ↓ ghrelin. (Book p180)")
q(180, S4, "Irreversible bariatric procedures include:",
  ["Biliopancreatic division (BPD) and duodenal switch (DS)",
   "Adjustable gastric banding and intragastric balloon",
   "Sleeve gastrectomy only", "Roux-en-Y gastric bypass"], 0,
  "Irreversible surgeries: biliopancreatic division (BPD) & duodenal switch (DS). (Book p180)")
q(180, S4, "Biliopancreatic division and duodenal switch give:",
  ["Maximum weight loss and resolution of diabetes, but the most post-operative complications",
   "The least weight loss and the fewest complications",
   "No metabolic benefit", "Weight loss only without metabolic change"], 0,
  "BPD/DS: max weight loss & resolution of DM; ↑↑ malabsorption; max post Sx complications - hence not done anymore. (Book p180)")
q(180, S4, "Biliopancreatic division and duodenal switch are now:",
  ["Not done anymore", "The procedures of choice", "Done only as revisional surgery",
   "Done only in adolescents"], 0,
  "BPD/DS: max post Sx complications - hence not done anymore. (Book p180)")
q(180, S4, "The length of the common channel in a biliopancreatic division is:",
  ["50 cm", "100 cm", "150 cm", "200 cm"], 0,
  "Bilio-pancreatic division: common channel 50 cm. (Book p180)")
q(180, S4, "The length of the common channel in a duodenal switch is:",
  ["100 cm", "50 cm", "150 cm", "200 cm"], 0,
  "Duodenal switch: common channel 100 cm. (Book p180)")

# ---------------- p181 · RYGB / MGB ----------------
S5 = "Roux-en-Y Gastric Bypass and Mini Gastric Bypass"
q(181, S5, "A Roux-en-Y gastric bypass consists of all of the following EXCEPT:",
  ["An ileo-colic anastomosis", "A gastric pouch", "A gastrojejunostomy",
   "A jejunojejunostomy"], 0,
  "Roux en Y: gastric pouch, gastro jejunostomy, jejuno jejunostomy. (Book p181)")
q(181, S5, "The mini gastric bypass is a:",
  ["Single anastomosis gastrojejunostomy", "Roux-en-Y reconstruction",
   "Sleeve gastrectomy with bypass", "Biliopancreatic division"], 0,
  "Mini gastric bypass: single gastro jejunostomy. (Book p181)")
q(181, S5, "The limb of a Roux-en-Y gastric bypass that carries bile and pancreatic juice is the:",
  ["Biliopancreatic limb", "Roux limb", "Common channel", "Alimentary limb"], 0,
  "Roux en Y gastric bypass: bilio pancreatic limb and Roux limb. (Book p181)")
q(181, S5, "In a Roux-en-Y reconstruction done for peptic ulcer disease, the Roux limb is:",
  ["50 cm", "100 cm", "150 cm", "25 cm"], 0,
  "Length of Roux en limb: peptic ulcer - 50 cm. (Book p181)")
q(181, S5, "In a Roux-en-Y reconstruction done for bariatric surgery, the Roux limb is:",
  ["100 cm", "50 cm", "150 cm", "25 cm"], 0,
  "Length of Roux en limb: bariatric Sx - 100 cm. (Book p181)")
q(181, S5, "In a superobese patient the Roux limb used is:",
  ["150 cm", "50 cm", "100 cm", "25 cm"], 0,
  "Length of Roux en limb: superobese - 150 cm. (Book p181)")

# ---------------- p181 · COMPLICATIONS ----------------
S6 = "Complications of Bariatric Surgery"
q(181, S6, "The m/c cause of mortality after bariatric surgery is:",
  ["DVT leading to pulmonary embolism", "Anastomotic leak", "Bleeding",
   "Nutritional deficiency"], 0,
  "Complications: DVT → pulmonary embolism (PE) - m/c cause of mortality. (Book p181)")
q(181, S6, "The risk of DVT and pulmonary embolism after bariatric surgery is highest in the:",
  ["1st month", "6th month", "2nd year", "5th year"], 0,
  "DVT → PE: ↑ risk in 1st month. (Book p181)")
q(181, S6, "The clinical features of an anastomotic leak after bariatric surgery include:",
  ["Pain abdomen, fever and peritonitis with rebound tenderness, guarding and rigidity",
   "Asymptomatic weight gain", "Diarrhoea alone", "Jaundice alone"], 0,
  "Anastomotic leak: pain abdomen, fever, peritonitis (rebound tenderness, guarding, rigidity). (Book p181)")
q(181, S6, "On ultrasound, an anastomotic leak after bariatric surgery shows:",
  ["A collection of fluid in the abdomen", "A dilated bowel loop",
   "A normal study", "Free air in the pleural cavity"], 0,
  "On USG: collection of fluid in abdomen. (Book p181)")
q(181, S6, "The investigation that confirms an anastomotic leak after bariatric surgery is:",
  ["CECT", "Ultrasound", "Plain X-ray", "Upper GI endoscopy"], 0,
  "CECT: confirm leak → re-explore. (Book p181)")
q(181, S6, "Once an anastomotic leak is confirmed, the management is:",
  ["Re-exploration", "Conservative management with antibiotics",
   "Endoscopic stenting", "Percutaneous drainage alone"], 0,
  "CECT: confirm leak → re explore. (Book p181)")
q(181, S6, "Nutritional complications after bariatric surgery include:",
  ["Malnutrition and calcium deficiency", "Vitamin A excess", "Iron overload",
   "Hypernatremia"], 0,
  "Nutritional complications: malnutrition; Ca²⁺ deficiency. (Book p181)")
q(181, S6, "Late complications of bariatric surgery include:",
  ["Anastomotic ulcer/stricture", "Hyperthyroidism", "Duodenal atresia", "Pancreatitis"], 0,
  "Complications: anastomotic ulcer/stricture. (Book p181)")

# ---------------- p182 · SLEEVE GASTRECTOMY ----------------
S7 = "Sleeve Gastrectomy"
q(182, S7, "Sleeve gastrectomy produces weight loss by:",
  ["Causing early satiety and reducing food consumption", "Malabsorption",
   "Bypassing the duodenum", "Reducing bile secretion"], 0,
  "Sleeve gastrectomy: causes early satiety → ↓ consumption of food → weight loss. (Book p182)")
q(182, S7, "Nutritional deficiencies after sleeve gastrectomy include:",
  ["Iron, vitamin B12 and calcium deficiency", "Iron deficiency only",
   "Vitamin A excess", "Zinc excess"], 0,
  "Complications - nutritional: iron, vit B12 & Ca²⁺ deficiency. (Book p182)")
q(182, S7, "The m/c complication of sleeve gastrectomy is:",
  ["Bleeding from the staple line", "Leak from the angle of His",
   "DVT/PE", "Gastro-oesophageal reflux"], 0,
  "Bleeding from staple line: m/c complication. (Book p182)")
q(182, S7, "The most distressing complication of sleeve gastrectomy is:",
  ["Leak from the angle of His", "Bleeding from the staple line",
   "DVT/PE", "Reflux"], 0,
  "Leak from angle of His: most distressing complication. (Book p182)")
q(182, S7, "A persistent leak from the angle of His after sleeve gastrectomy requires:",
  ["Revision surgery", "Conservative management only", "Endoscopic dilatation",
   "Total gastrectomy"], 0,
  "Leak from angle of His: requires revision Sx if persistent. (Book p182)")
q(182, S7, "Late complications of sleeve gastrectomy include:",
  ["Gastro-oesophageal reflux and Barrett's oesophagus",
   "Dumping syndrome", "Afferent loop syndrome", "Bile reflux gastritis"], 0,
  "Complications: gastro-esophageal reflux; Barrett's esophagus. (Book p182)")
q(182, S7, "Weight gain after sleeve gastrectomy is due to:",
  ["Re-distension of the sleeve", "Non-compliance with vitamins",
   "Development of a stricture", "Excess bile secretion"], 0,
  "Weight gain: d/t re-distension of sleeve. (Book p182)")
q(182, S7, "Weight gain after sleeve gastrectomy is treated by:",
  ["ROSE - restorative obesity surgery endoscopically", "Revisional gastric bypass",
   "Total gastrectomy", "Intragastric balloon"], 0,
  "Rx: ROSE - restorative obesity surgery endoscopically. (Book p182)")

# ---------------- p182 · ENDOSCOPIC PROCEDURES ----------------
S8 = "Endoscopic Bariatric Procedures (ROSE / NOTES)"
q(182, S8, "ROSE in bariatric surgery stands for:",
  ["Restorative obesity surgery endoscopically", "Restrictive obesity surgery endoscopically",
   "Revision obesity surgery endoscopically", "Revisional obesity sleeve endoscopically"], 0,
  "ROSE - restorative obesity surgery endoscopically. (Book p182)")
q(182, S8, "ROSE is a type of __________ procedure.",
  ["NOTES (natural orifice transluminal endoscopic surgery)", "Laparoscopic",
   "Open", "Robotic"], 0,
  "Type of NOTES procedure: natural orifice transluminal endoscopic surgery. (Book p182)")
q(182, S8, "POSE in bariatric surgery stands for:",
  ["Primary obesity surgery endoscopically", "Primary obesity sleeve endoscopically",
   "Post operative surgery endoscopically", "Proximal obesity surgery endoscopically"], 0,
  "POSE - primary obesity surgery endoscopically. (Book p182)")
q(182, S8, "TOGA in bariatric surgery stands for:",
  ["Transoral gastroplasty", "Transoral gastric bypass", "Total gastric plication",
   "Transoral gastropexy"], 0,
  "TOGA - transoral gastroplasty (type of ROSE). (Book p182)")
q(182, S8, "Endocinch is:",
  ["An endoscopic bariatric procedure", "A type of gastric band",
   "A stapling device", "A nutritional supplement"], 0,
  "Endocinch: an endoscopic bariatric/ROSE procedure. (Book p182)")

# ---------------- p183 · ADJUSTABLE GASTRIC BAND ----------------
S9 = "Adjustable Gastric Banding"
q(183, S9, "An adjustable gastric band is placed at the:",
  ["Gastroesophageal junction", "Pylorus", "Angle of His", "D2 of duodenum"], 0,
  "Adjustable band: placed at the GE junction. (Book p183)")
q(183, S9, "The adjustable gastric band creates a virtual stomach pouch of about:",
  ["10 cm", "50 cm", "100 cm", "5 cm"], 0,
  "Virtual stomach pouch: 10 cm. (Book p183)")
q(183, S9, "The size of an adjustable gastric band is adjusted through:",
  ["A port placed at the umbilicus", "A second operation", "An endoscopic balloon",
   "A nasogastric tube"], 0,
  "Port used to adjust the size of the band - at the umbilicus. (Book p183)")
q(183, S9, "An adjustable gastric band produces weight loss by causing:",
  ["Early satiety", "Malabsorption", "Dumping", "Decreased ghrelin alone"], 0,
  "Adjustable band: early satiety → weight loss. (Book p183)")
q(183, S9, "Complications of adjustable gastric banding include all EXCEPT:",
  ["Anastomotic leak", "Access port infection", "Band infection", "Tubing leak"], 0,
  "Complications: access port infection, DVT/PE, band infection, tubing leak, slippage of band, stomach erosion, band intolerance, weight regain. (Book p183)")
q(183, S9, "Slippage of the gastric band leads to:",
  ["Weight gain", "Weight loss", "Perforation", "Dumping syndrome"], 0,
  "Slippage of band → weight gain. (Book p183)")
q(183, S9, "Erosion of the stomach by a gastric band is:",
  ["A known complication of the band", "Due to over-inflation of the balloon",
   "Seen only with the intragastric balloon", "Always fatal"], 0,
  "Complication: stomach erosion (d/t band). (Book p183)")
q(183, S9, "Band intolerance as a complication of gastric banding means the band:",
  ["Is not tolerated by the patient and needs removal", "Slips upward",
   "Causes malabsorption", "Causes reflux only"], 0,
  "Complication: band intolerance. (Book p183)")

# ---------------- p183 · INTRAGASTRIC BALLOON ----------------
S10 = "Intragastric Balloon"
q(183, S10, "The Allurion balloon is:",
  ["A self dissolving intragastric balloon", "An adjustable gastric band",
   "A permanent gastric balloon", "A duodenal balloon"], 0,
  "Allurion: self dissolving balloon. (Book p183)")
q(183, S10, "An intragastric balloon is placed as part of:",
  ["Endoscopic bariatric therapy", "Open bariatric surgery",
   "A biliopancreatic division", "A Roux-en-Y reconstruction"], 0,
  "Intra gastric balloon placement - an endoscopic bariatric procedure. (Book p183)")

# ---------------- p183 · NUTRITION ----------------
S11 = "Nutritional Guidelines after Bariatric Surgery"
q(183, S11, "After gastric banding, supplements are advised if the patient has:",
  ["Vomiting (+)", "Diarrhoea", "Constipation", "Reflux"], 0,
  "Nutritional guidelines: gastric banding - supplement if vomiting (+). (Book p183)")
q(183, S11, "Minerals supplemented after sleeve gastrectomy and gastric bypass include:",
  ["Thiamine, selenium, copper and zinc", "Iron alone", "Sodium and potassium",
   "Magnesium alone"], 0,
  "Nutritional guidelines: minerals - thiamine, selenium, copper, zinc. (Book p183)")
q(183, S11, "Vitamins supplemented after sleeve gastrectomy and gastric bypass include:",
  ["Vitamin A, D, E, K, B12 and folic acid", "Vitamin C alone", "Vitamin A alone",
   "No vitamins are needed"], 0,
  "Nutritional guidelines: folic acid, vit B12, A, D, E, K. (Book p183)")
q(183, S11, "Bariatric surgery leads to remission of:",
  ["Diabetes mellitus, hypertension and hyperlipidemia", "Diabetes only",
   "Hypertension only", "No comorbidities"], 0,
  "Note: DM, HTN, hyperlipidemia - remission. (Book p183)")

# ---------------- units ----------------
def sec_ids(*labels):
    return [x["id"] for x in Q if x["sec"] in labels]
def first_page(label):
    for x in Q:
        if x["sec"] == label:
            return x["page"]
    return 0

UNIT_DEFS = [
    (S1, "The thresholds differ by population: 40, or 35 with complications such as diabetes, obstructive sleep apnoea or Pickwickian syndrome, hyperlipidemia and osteoarthritis, and even 30-34.9 when type 2 diabetes has appeared within ten years. Asians are operated at lower numbers - 37.5, or 32.5 once complications set in."),
    (S2, "Prepare the patient as carefully as you operate: counsel properly, change the diet and lifestyle, and put them on a low carbohydrate, high protein liver shrinkage diet for at least two weeks. Anyone who cannot stick to that diet needs psychotherapy first. Smoking must stop 4-6 weeks before surgery, and the patient with obstructive sleep apnoea - an independent risk factor for cardiac death - needs oxygen and a watch for an anastomotic leak afterwards."),
    (S3, "The obesity surgery mortality risk score adds a point each for arterial hypertension, age over 45, male gender, BMI above 50 and any risk factor for pulmonary thromboembolism."),
    (S4, "Every operation works through some combination of malabsorption, restriction of volume and hormonal change - chiefly the fall in ghrelin. The irreversible malabsorptive operations, biliopancreatic division with a 50 cm common channel and the duodenal switch with a 100 cm channel, produce the greatest weight loss and diabetes resolution but also the most complications, which is why they are no longer done."),
    (S5, "Roux-en-Y gastric bypass builds a small gastric pouch, joins it to jejunum and then rejoins jejunum to jejunum, leaving a biliopancreatic limb and a Roux limb. The mini gastric bypass does the whole job with a single gastrojejunostomy. Size the Roux limb by indication: 50 cm for peptic ulcer, 100 cm for bariatric surgery and 150 cm in the superobese."),
    (S6, "The commonest cause of death is pulmonary embolism from a DVT, and the first month is the dangerous one. A leak presents with pain, fever and peritonitis; ultrasound shows the collection and CECT confirms it, after which the patient goes back to theatre. Malnutrition and calcium deficiency follow later, as do anastomotic ulcers and strictures."),
    (S7, "Sleeve gastrectomy works by causing early satiety, so the patient simply eats less. Bleeding from the staple line is the commonest complication, but a leak at the angle of His is the most distressing and needs revision surgery if it persists. Iron, B12 and calcium run low, reflux and Barrett's oesophagus appear late, and weight can return once the sleeve re-distends."),
    (S8, "Weight regain after a sleeve can be treated endoscopically: ROSE, restorative obesity surgery endoscopically, which is a NOTES (natural orifice transluminal endoscopic surgery) procedure. Its family includes Endocinch, POSE - primary obesity surgery endoscopically - TOGA, the transoral gastroplasty, and ESG."),
    (S9, "The adjustable band sits at the gastroesophageal junction, creating a 10 cm virtual pouch with a port at the umbilicus to tighten or loosen it, and works purely by producing early satiety. Its problems are mechanical and infective: port infection, DVT/PE, band infection, tubing leak, slippage with weight gain, erosion of the stomach, intolerance and ultimately weight regain."),
    (S10, "The intragastric balloon is the least invasive option, and the Allurion balloon is the one that dissolves by itself so it never has to be removed endoscopically."),
    (S11, "Supplement by the operation: after banding only if the patient is vomiting; after sleeve gastrectomy or gastric bypass the full list - thiamine, selenium, copper and zinc with folic acid and vitamins B12, A, D, E and K. The reward is remission of diabetes, hypertension and hyperlipidemia."),
]

UNITS = []
for i, (title, guide) in enumerate(UNIT_DEFS, 1):
    UNITS.append({"id": f"SURG-U26-{i}", "ch": 26, "n": i, "title": title,
                  "sec": f"{title} · p{first_page(title)}",
                  "qs": sec_ids(title), "guide": guide})

covered = [i for u in UNITS for i in u["qs"]]
assert covered == [x["id"] for x in Q], "units must cover questions in order"

data = {"questions": Q, "units": UNITS}
with open("data/ch26.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
print(f"ch26: {len(Q)} questions, {len(UNITS)} units")
