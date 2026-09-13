#!/usr/bin/env python3
"""Build data/ch6.json for PULSE Surgery ch6 (Surgical Nutrition, book p28-36)."""
import json

Q = []
def q(page, sec, text, opts, ans, exp):
    Q.append({"id": f"SURG-C6-{len(Q)+1:03d}", "sec": sec, "page": page,
              "q": text, "opts": opts, "ans": ans, "exp": exp})

# ---------------- p28 · NUTRITIONAL ASSESSMENT : INDICATORS ----------------
q(28, "Nutritional Assessment: Indicators", "Regarding biochemical markers to identify malnutrition, the book states:",
  ["No single reliable biochemical marker exists", "Serum albumin is the single reliable marker", "Serum transferrin is the single reliable marker", "CRP is the single reliable marker"], 0,
  "Indicators: No single reliable biochemical marker to identify malnutrition. (Book p28)")
q(28, "Nutritional Assessment: Indicators", "Low albumin is an indicator of:",
  ["Good outcome", "Poor outcome", "Body fat", "Muscle mass"], 1,
  "Low albumin: Indicator of poor outcome. (Book p28)")
q(28, "Nutritional Assessment: Indicators", "Which is a better marker than albumin for nutritional assessment?",
  ["Pre albumin", "Hemoglobin", "Platelet count", "Serum sodium"], 0,
  "S. pre albumin: Better marker. (Book p28)")
q(28, "Nutritional Assessment: Indicators", "Significant weight loss is defined as unintentional weight loss of:",
  [">5% of weight in 3 months", ">10% of weight in 6 months", ">15% of weight in 12 months", ">20% of weight in 1 month"], 1,
  "Significant weight loss: Unintentional weight loss >10% of weight in 6 months. (Book p28)")
q(28, "Nutritional Assessment: Indicators", "Significant weight loss is an indicator of:",
  ["Good prognosis", "Poor prognosis", "Body fat", "Fluid overload"], 1,
  "Significant weight loss: Indicator of poor prognosis. (Book p28)")
q(28, "Nutritional Assessment: Indicators", "Which BMI value indicates poor outcome?",
  ["BMI <15", "BMI <20", "BMI <25", "BMI <30"], 0,
  "BMI <15: Poor outcome. (Book p28)")
q(28, "Nutritional Assessment: Indicators", "Skin fold thickness is an indicator of:",
  ["Muscle mass", "Body fat", "Bone density", "Fluid status"], 1,
  "Skin fold thickness: Indicator of body fat. (Book p28)")
q(28, "Nutritional Assessment: Indicators", "Mid arm circumference is used as an indicator of:",
  ["Body fat", "Muscle mass", "Hydration", "Visceral protein"], 1,
  "Mid arm circumference: Muscle mass. (Book p28)")

# ---------------- p28 · MALNUTRITION UNIVERSAL SCREENING TOOL ----------------
q(28, "Malnutrition Universal Screening Tool", "The malnutrition universal screening tool combines BMI score, unintentional weight loss and:",
  ["Acute disease affect score", "Serum albumin score", "Age score", "Functional score"], 0,
  "MUST: BMI score + Unintentional weight loss + Acute disease affect score. (Book p28)")
q(28, "Malnutrition Universal Screening Tool", "The three components of the malnutrition universal screening tool together give the:",
  ["Overall risk of malnutrition", "Daily calorie target", "Nitrogen balance", "Refeeding risk grade"], 0,
  "BMI score + unintentional weight loss + acute disease affect score -> Overall risk of malnutrition. (Book p28)")

# ---------------- p28 · NUTRITIONAL REQUIREMENT (REE TABLE) ----------------
q(28, "Nutritional Requirement: REE", "The resting energy expenditure (REE) multiplier for a normal sedentary life is:",
  ["1", "1.4", "1.8", "2"], 0,
  "REE table: Normal (Sedentary life) = 1. (Book p28)")
q(28, "Nutritional Requirement: REE", "Calorie requirement for a normal sedentary person is:",
  ["20 Kcal/kg/day", "25 Kcal/kg/day", "30 Kcal/kg/day", "40 Kcal/kg/day"], 0,
  "REE table: Normal (Sedentary life): 20 Kcal/kg/day. (Book p28)")
q(28, "Nutritional Requirement: REE", "The REE multiplier for mild/moderate sepsis is:",
  ["1", "1.4", "1.8", "2"], 1,
  "REE table: Mild/moderate sepsis = 1.4. (Book p28)")
q(28, "Nutritional Requirement: REE", "The REE multiplier for severe sepsis is:",
  ["1", "1.4", "1.8", "2"], 2,
  "REE table: Severe sepsis = 1.8. (Book p28)")
q(28, "Nutritional Requirement: REE", "Severe burns have an REE multiplier and calorie requirement of:",
  ["1.4 and 25 Kcal/kg/day", "1.8 and 30 Kcal/kg/day", "2 and 40 Kcal/kg/day", "2 and 20 Kcal/kg/day"], 2,
  "REE table: Severe burns = 2, 40 Kcal/kg/day. (Book p28)")

# ---------------- p28 · ENTERAL AND PARENTERAL NUTRITION ----------------
q(28, "Enteral and Parenteral Nutrition", "Between enteral and parenteral nutrition, the preferred route is:",
  ["Enteral (oral) > parenteral", "Parenteral (I/V) > enteral", "Both are equal", "Peripheral I/V first"], 0,
  "Enteral (Oral) > Parenteral (I/V). (Book p28)")
q(28, "Enteral and Parenteral Nutrition", "Advantages of enteral nutrition include all of the following EXCEPT:",
  ["Physiological", "Cheap", "Maintains enterohepatic circulation", "Causes stasis of gut bacteria"], 3,
  "Enteral: 1. Physiological. 2. Cheap. 3. Maintains enterohepatic circulation. 4. Prevents translocation of gut bacteria. (Book p28)")
q(28, "Enteral and Parenteral Nutrition", "Enteral feeding prevents:",
  ["Translocation of gut bacteria", "Enterohepatic circulation", "Gastric emptying", "Bile secretion"], 0,
  "Enteral nutrition prevents translocation of gut bacteria. (Book p28)")
q(28, "Enteral and Parenteral Nutrition", "Parenteral nutrition is given by the I/V route and leads to:",
  ["Stasis", "Enterohepatic circulation", "Bacterial translocation prevention", "Cheaper costs"], 0,
  "Parenteral: I/V : Stasis. (Book p28)")

# ---------------- p29 · ENTERAL NUTRITION ALGORITHM ----------------
q(29, "Enteral Nutrition: Route Algorithm", "The best route of enteral nutrition is:",
  ["Oral", "Nasogastric", "Gastrostomy", "Jejunostomy"], 0,
  "Enteral nutrition: Best route: Oral. (Book p29)")
q(29, "Enteral Nutrition: Route Algorithm", "When oral nutrition is not possible, the next deciding factor is:",
  ["Duration of requirement", "Patient's age", "Serum albumin", "BMI"], 0,
  "Oral nutrition not possible -> decide by Duration of requirement. (Book p29)")
q(29, "Enteral Nutrition: Route Algorithm", "Enteral feeding needed for <3 weeks with good gastric emptying is best given by:",
  ["Nasogastric tube / Ryles tube", "Nasojejunal tube", "Feeding gastrostomy", "Feeding jejunostomy"], 0,
  "<3 weeks + gastric emptying good -> Nasogastric tube, Ryles tube. (Book p29)")
q(29, "Enteral Nutrition: Route Algorithm", "Enteral feeding needed for <3 weeks with poor gastric emptying (nausea, vomiting) is given by:",
  ["Nasogastric tube", "Nasojejunal tube", "Feeding gastrostomy", "Ryles tube"], 1,
  "<3 weeks + gastric emptying poor (nausea, vomiting) -> Nasojejunal tube. (Book p29)")
q(29, "Enteral Nutrition: Route Algorithm", "Enteral feeding needed for >3 weeks with good gastric emptying is given by:",
  ["Nasogastric tube", "Nasojejunal tube", "Feeding gastrostomy", "Feeding jejunostomy"], 2,
  ">3 weeks + gastric emptying good -> Feeding gastrostomy. (Book p29)")
q(29, "Enteral Nutrition: Route Algorithm", "Enteral feeding needed for >3 weeks with poor gastric emptying is given by:",
  ["Nasogastric tube", "Ryles tube", "Feeding gastrostomy", "Feeding jejunostomy"], 3,
  ">3 weeks + gastric emptying poor -> Feeding jejunostomy. (Book p29)")

# ---------------- p29 · RYLES TUBE ----------------
q(29, "Ryles Tube", "Best position for Ryles tube insertion is:",
  ["Supine with neck extended", "Sitting with neck slightly flexed", "Left lateral", "Prone"], 1,
  "Ryles tube: Best position: Sitting with neck slightly flexed. (Book p29)")
q(29, "Ryles Tube", "Assessment of Ryles tube placement includes:",
  ["Aspiration of gastric contents", "Aspiration of bile only", "Abdominal ultrasound", "Serum gastrin"], 0,
  "Assessment of placement: Aspiration of gastric contents. (Book p29)")
q(29, "Ryles Tube", "Pushing air through the Ryles tube while auscultating confirms placement over the:",
  ["Hypochondrium", "Epigastrium", "Suprapubic region", "Flank"], 1,
  "Push air -> Auscultate in epigastrium. (Book p29)")
q(29, "Ryles Tube", "The length of a Ryles tube is measured from the nose to the ear and then to the:",
  ["Umbilicus", "Xiphisternum", "Iliac crest", "Pubic symphysis"], 1,
  "Ryles tube measurement: Nose - Ear - Xiphisternum. (Book p29)")

# ---------------- p29 · NASOJEJUNAL TUBE ----------------
q(29, "Nasojejunal Tube", "A nasojejunal tube is inserted into the jejunum under:",
  ["Fluoroscopic guidance", "Direct vision", "Blind bedside technique only", "MRI guidance"], 0,
  "Nasojejunal tube: Inserted into jejunum under fluoroscopic guidance. (Book p29)")
q(29, "Nasojejunal Tube", "The nasojejunal tube has the advantage that it:",
  ["Bypasses the stomach", "Bypasses the jejunum", "Requires gastrostomy", "Needs no guidance"], 0,
  "Nasojejunal tube: Bypasses stomach. (Book p29)")

# ---------------- p29-30 · INVASIVE FEEDING TUBES ----------------
q(29, "Invasive Feeding Tubes", "Feeding gastrostomy can be performed by all of the following EXCEPT:",
  ["Stamm", "Witzel", "PEG/RIG", "Seldinger jejunostomy"], 3,
  "Feeding gastrostomy: Stamm, Witzel, PEG/RIG. (Book p29)")
q(29, "Invasive Feeding Tubes", "Feeding jejunostomy is performed by which techniques?",
  ["Stamm and Witzel", "PEG and RIG", "Witzel only", "Stamm only"], 0,
  "Feeding jejunostomy: Stamm, Witzel. (Book p29)")
q(30, "Invasive Feeding Tubes", "Compared with jejunostomy, gastrostomy feeding is:",
  ["More physiological but with increased risk of aspiration", "Less physiological with less aspiration", "More physiological with less aspiration", "Less physiological with more aspiration"], 0,
  "Gastrostomy: more physiological; ↑ risk of aspiration. (Book p30)")
q(30, "Invasive Feeding Tubes", "The main disadvantage of gastrostomy feeding compared to jejunostomy is:",
  ["Increased risk of aspiration", "Less physiological", "Cannot use a tube", "Needs fluoroscopy always"], 0,
  "Gastrostomy: ↑ risk of aspiration. (Book p30)")
q(30, "Stamm vs Witzel", "Stamm gastrostomy/jejunostomy is associated with:",
  ["Peridrain leakage", "Less peridrain leakage", "No leakage at all", "Biliary leakage"], 0,
  "Stamm: Peridrain leakage. (Book p30)")
q(30, "Stamm vs Witzel", "Witzel gastrostomy/jejunostomy is associated with:",
  ["More peridrain leakage", "Less peridrain leakage", "No tunnel", "Gastric outlet obstruction"], 1,
  "Witzel: Less peridrain leakage. (Book p30)")
q(30, "Stamm vs Witzel", "In Stamm technique, the tube used and the suture material are:",
  ["Red Robinson tube and non-absorbable suture", "Foley catheter and absorbable suture", "Ryles tube and absorbable suture", "PEG tube only"], 0,
  "Stamm: Red Robinson tube, Non-absorbable suture. (Book p30)")
q(30, "Stamm vs Witzel", "The steps of Stamm technique are:",
  ["1. Stab incision, 2. Purse string suture", "1. Tunnel, 2. Anastomosis", "1. Purse string, 2. Resection", "1. Stab incision, 2. Tunnel over distal jejunum"], 0,
  "Stamm: 1. Stab incision; 2. Purse string suture (small bowel). (Book p30)")
q(30, "Stamm vs Witzel", "In Witzel technique the tube is buried in a tunnel made in the:",
  ["Distal jejunum", "Proximal duodenum", "Stomach fundus", "Transverse colon"], 0,
  "Witzel: Tunnel in distal jejunum. (Book p30)")

# ---------------- p31 · TECHNIQUE OF PEG ----------------
q(31, "Technique of PEG", "In PEG technique, step A is:",
  ["Endoscope is advanced transorally into the stomach with insufflation", "Transillumination of the abdominal wall", "Seldinger puncture", "Transgastric suture fixation"], 0,
  "PEG step A: Endoscope is advanced transorally into the stomach with insufflation. (Book p31)")
q(31, "Technique of PEG", "Steps B and C of PEG technique are:",
  ["Transillumination and finger indentation of the anterior abdominal wall", "Balloon dilatation of the esophagus", "Laparoscopic port insertion", "Needle jejunostomy"], 0,
  "PEG steps B, C: Transillumination and finger indentation of the anterior abdominal wall. (Book p31)")
q(31, "Technique of PEG", "Steps D to G of PEG technique represent:",
  ["Transgastric suture fixation of stomach to the abdominal wall", "Seldinger gastrostomy", "Tube removal", " Jejunal extension placement"], 0,
  "PEG steps D-G: Transgastric suture fixation of stomach to the abdominal wall. (Book p31)")
q(31, "Technique of PEG", "Steps H to K of PEG technique use which method to create the gastrostomy?",
  ["Seldinger technique", "Open Stamm technique", "Witzel tunnel", "Laparoscopic stapling"], 0,
  "PEG steps H-K: Seldinger technique used to create a gastrostomy. (Book p31)")

# ---------------- p31 · RIG ----------------
q(31, "Radiologically Inserted Gastrostomy", "Radiologically inserted gastrostomy (RIG) is indicated in:",
  ["Patients where endoscopy is not possible", "Patients needing jejunostomy", "Patients with normal anatomy", "Short-term feeding <1 week"], 0,
  "RIG indications: Patients where endoscopy is not possible. (Book p31)")
q(31, "Radiologically Inserted Gastrostomy", "Which respiratory situation favours RIG over PEG?",
  ["Compromised respiratory function", "Normal spirometry", "Asthma on inhalers", "Recent cough"], 0,
  "RIG indications: Compromised respiratory function. (Book p31)")
q(31, "Radiologically Inserted Gastrostomy", "Compromised oropharyngeal anatomy is an indication for:",
  ["RIG", "Ryles tube", "Nasojejunal tube", "Oral feeds"], 0,
  "RIG indications: Compromised oropharyngeal anatomy. (Book p31)")

# ---------------- p31 · ENTERAL NUTRITION: PRINCIPLE ----------------
q(31, "Enteral Nutrition: Principle", "Enteral feeding rate is started gradually at:",
  ["10-20 mL/hr", "50-60 mL/hr", "75-100 mL/hr", "150 mL/hr"], 0,
  "Rate of feeding: Started gradually: 10-20 mL/hr. (Book p31)")
q(31, "Enteral Nutrition: Principle", "If tolerated, the enteral feeding rate is increased up to:",
  ["40 mL/hr", "60 mL/hr", "75 mL/hr", "120 mL/hr"], 2,
  "Increased upto 75 mL/hr, if tolerated. (Book p31)")
q(31, "Enteral Nutrition: Principle", "Before a subsequent enteral meal one should aspirate; the next feed is withheld if the aspirate is:",
  [">25-50 cc", ">75-100 cc", ">150-200 cc", ">300 cc"], 1,
  "Aspirate before subsequent meal: If aspirate is >75-100 cc: withhold next feed. (Book p31)")
q(31, "Enteral Nutrition: Principle", "Withholding the feed for a large gastric aspirate avoids aspiration due to:",
  ["Over distention of stomach", "Under feeding", "Tube blockage", "Hypokalemia"], 0,
  "Withhold next feed (To avoid aspiration d/t over distention of stomach). (Book p31)")

# ---------------- p32 · COMPLICATIONS OF ENTERAL NUTRITION ----------------
q(32, "Complications of Enteral Nutrition", "The most common (m/c) category of enteral nutrition complications is:",
  ["Tube related", "Feeding regime related", "Metabolic", "Cardiac"], 0,
  "Complications: a. Tube related: m/c. (Book p32)")
q(32, "Complications of Enteral Nutrition", "Tube related complications include all of the following EXCEPT:",
  ["Blockage", "Migration", "Leakage", "Hyperglycemia"], 3,
  "Tube related: Blockage, migration, leakage. (Book p32)")
q(32, "Complications of Enteral Nutrition", "The m/c feeding regime related complication of enteral nutrition is:",
  ["Osmotic diarrhoea", "Constipation", "Hyperglycemia", "Hypophosphatemia"], 0,
  "Feeding regime related: Osmotic diarrhoea: m/c. (Book p32)")
q(32, "Complications of Enteral Nutrition", "A hyperosmolar feed causes diarrhoea because of:",
  ["Rapid transit", "Slow transit", "Bacterial overgrowth", "Tube migration"], 0,
  "Hyperosmolar feed: Rapid transit -> Diarrhoea. (Book p32)")
q(32, "Complications of Enteral Nutrition", "Overfeeding during enteral nutrition causes:",
  ["Aspiration", "Constipation", "Hypoglycemia", "Tube blockage"], 0,
  "Overfeeding causes aspiration. (Book p32)")

# ---------------- p32 · PARENTERAL NUTRITION: INDICATIONS ----------------
q(32, "Parenteral Nutrition: Indications", "Parenteral nutrition is indicated in prolonged paralytic ileus lasting more than:",
  ["24 hrs", "48 hrs", "72 hrs", "1 week"], 2,
  "Indication: Prolonged paralytic ileus >72 hrs. (Book p32)")
q(32, "Parenteral Nutrition: Indications", "A non-contracting bowel causes no transit of food leading to:",
  ["Obstruction, vomiting", "Diarrhoea", "Hyperglycemia", "Refeeding syndrome"], 0,
  "Non-contracting bowel -> No transit of food -> Obstruction, vomiting. (Book p32)")
q(32, "Parenteral Nutrition: Indications", "Which syndrome of the small bowel is an indication for parenteral nutrition?",
  ["Short bowel syndrome", "Irritable bowel syndrome", "Dumping syndrome", "Zollinger-Ellison syndrome"], 0,
  "Indication: Short bowel syndrome. (Book p32)")
q(32, "Parenteral Nutrition: Indications", "High output faecal fistula requiring parenteral nutrition is defined as output greater than:",
  [">200 cc/24 hrs", ">350 cc/24 hrs", ">500 cc/24 hrs", ">1000 cc/24 hrs"], 2,
  "Indication: High output faecal fistula (>500 cc/24 hrs). (Book p32)")
q(32, "Parenteral Nutrition: Indications", "In an acute episode of inflammatory bowel disease, parenteral nutrition is used because of:",
  ["Malabsorption and need for bowel rest", "Hyperglycemia", "Tube blockage", "Aspiration risk"], 0,
  "Acute episode of IBD: Malabsorption; Need for bowel rest. (Book p32)")
q(32, "Parenteral Nutrition: Indications", "Parenteral nutrition is indicated in which phase of acute severe pancreatitis?",
  ["Initial phase", "Recovery phase", "Chronic phase", "Never indicated"], 0,
  "Initial phase of acute severe pancreatitis. (Book p32)")

# ---------------- p32 · ROUTES OF TPN ----------------
q(32, "Routes of TPN", "The best route of total parenteral nutrition is:",
  ["Central line", "PICC", "Peripheral I/V line", "Oral"], 0,
  "Routes of TPN: Central line = Best. (Book p32)")
q(32, "Routes of TPN", "PICC stands for:",
  ["Peripherally inserted central catheter", "Percutaneous internal central catheter", "Peripheral insulin control catheter", "Peritoneal inserted central catheter"], 0,
  "Peripherally inserted central catheter (PICC). (Book p32)")
q(32, "Routes of TPN", "The least preferred route of TPN is the:",
  ["Peripheral I/V line", "Central line", "PICC", "Subclavian line"], 0,
  "Peripheral I/V line: Least preferred. (Book p32)")
q(32, "Routes of TPN", "Peripheral I/V TPN carries an increased risk of:",
  ["Thrombophlebitis", "Pneumothorax", "Air embolism", "Arrhythmia"], 0,
  "Peripheral I/V line: ↑ risk of thrombophlebitis. (Book p32)")

# ---------------- p32 · CENTRAL LINE TABLE ----------------
q(32, "Central Line: Vein Comparison", "Risk of thrombosis and infection is LEAST with which central venous access?",
  ["Subclavian vein", "Internal jugular vein", "Femoral vein", "Peripheral vein"], 0,
  "Central line table: Risk of thrombosis & infection: Subclavian = Least. (Book p32)")
q(32, "Central Line: Vein Comparison", "Risk of thrombosis and infection is MAXIMUM with which vein?",
  ["Subclavian vein", "Internal jugular vein", "Femoral vein", "Cephalic vein"], 2,
  "Central line table: Risk of thrombosis & infection: Femoral = Max. (Book p32)")
q(32, "Central Line: Vein Comparison", "Risk of pneumothorax is maximum with which central line?",
  ["Subclavian vein", "Internal jugular vein", "Femoral vein", "PICC"], 0,
  "Central line table: Risk of pneumothorax: Subclavian = Max. (Book p32)")
q(32, "Central Line: Vein Comparison", "Risk of pneumothorax is least with which central line?",
  ["Subclavian vein", "Internal jugular vein", "Femoral vein", "PICC"], 2,
  "Central line table: Risk of pneumothorax: Femoral = Least. (Book p32)")
q(32, "Central Line: Vein Comparison", "Ease of insertion is maximum for which vein?",
  ["Subclavian vein", "Internal jugular vein", "Femoral vein", "External jugular"], 1,
  "Central line table: Ease of insertion: Internal jugular = Max. (Book p32)")
q(32, "Central Line: Vein Comparison", "The vein most commonly used in TPN is the:",
  ["Subclavian vein", "Internal jugular vein", "Femoral vein", "Basilic vein"], 0,
  "Central line table: Other features: Subclavian = m/c used in TPN. (Book p32)")
q(32, "Central Line: Vein Comparison", "The most commonly used central vein overall is the:",
  ["Subclavian vein", "Internal jugular vein", "Femoral vein", "Brachial vein"], 1,
  "Central line table: Other features: Internal jugular = m/c used vein overall. (Book p32)")
q(32, "Central Line: Assessment", "After central line insertion, the tip should be located in the:",
  ["Superior vena cava just above right atrium", "Right atrium", "Right ventricle", "Innominate vein"], 0,
  "Assessment: Tip located in the superior vena cava just above right atrium. (Book p32)")
q(32, "Central Line: Assessment", "A central line tip lying inside the right atrium can cause:",
  ["Ectopic beats/arrhythmia", "Pneumothorax", "Thrombophlebitis", "Diarrhoea"], 0,
  "Tip in right atrium -> Ectopic beats/Arrhythmia. (Book p32)")
q(32, "Central Line: Assessment", "A chest X-ray after central line insertion is done to visualize the tip and to:",
  ["Rule out pneumothorax", "Check gastric emptying", "Measure cardiac size", "Confirm bowel contractility"], 0,
  "Assessment after insertion: To visualize the tip; To r/o pneumothorax. (Book p32)")

# ---------------- p33 · PICC LINE ----------------
q(33, "PICC Line", "A PICC line is inserted with which guidance into a peripheral vessel?",
  ["Ultrasound guidance", "Fluoroscopy only", "CT guidance", "Blind landmark only"], 0,
  "PICC line: Inserted with ultrasound guidance in peripheral vessel. (Book p33)")
q(33, "PICC Line", "The tip of a PICC line lies:",
  ["Just above right atrium", "In the right ventricle", "In the femoral vein", "In the peripheral vein itself"], 0,
  "PICC line: Tip just above right atrium. (Book p33)")
q(33, "PICC Line", "The duration a PICC line can remain is:",
  ["2-3 months", "2-3 days", "2-3 weeks", "1 year"], 0,
  "PICC line: Duration: 2-3 months. (Book p33)")
q(33, "PICC Line", "Uses of a PICC line include all of the following EXCEPT:",
  ["Chemotherapy", "TPN", "Prolonged antibiotics", "Routine blood donation"], 3,
  "PICC uses: Chemotherapy, TPN, Prolonged antibiotics. (Book p33)")
q(33, "PICC Line", "A PICC line requires:",
  ["Regular dressing and management", "No maintenance", "Daily replacement", "Heparin lock only"], 0,
  "PICC line: Regular dressing & management is required. (Book p33)")

# ---------------- p33 · TPN SOLUTION ----------------
q(33, "TPN Solution", "The amount of TPN solution given is:",
  ["1-2 litres over 24 hrs", "3-4 litres over 12 hrs", "500 mL over 48 hrs", "5 litres over 24 hrs"], 0,
  "TPN solution: Amount: 1-2 litres over 24 hrs. (Book p33)")
q(33, "TPN Solution", "The TPN composition ratio 20:30:50 corresponds to:",
  ["Protein : Fat : Carbohydrate", "Fat : Protein : Carbohydrate", "Carbohydrate : Fat : Protein", "Protein : Carbohydrate : Fat"], 0,
  "Composition: 20 : 30 : 50 = Protein : Fat : Carbohydrate. (Book p33)")
q(33, "TPN Solution", "A '3 in 1' TPN bag contains:",
  ["All three components", "Fat and carbohydrates only", "Protein and fat only", "Only carbohydrates"], 0,
  "3 in 1: All three components. (Book p33)")
q(33, "TPN Solution", "A '2 in 1' TPN bag contains:",
  ["Fat and carbohydrates", "Protein and fat", "Protein and carbohydrates", "Vitamins and minerals"], 0,
  "2 in 1: Fat & carbohydrates. (Book p33)")
q(33, "TPN Solution", "Which of the following can be added to a TPN solution?",
  ["Trace elements and vitamins", "Fibre", "Enteral formula", "Bile salts"], 0,
  "Trace elements, vitamins can be added. (Book p33)")
q(33, "TPN Solution", "TPN solution contains:",
  ["No fibre", "High fibre", "Whole protein only", "Only lactate"], 0,
  "TPN composition: No fibre. (Book p33)")
q(33, "TPN Types", "High osmolar TPN has increased carbohydrates leading to increased:",
  ["CO2 and H2O", "Urea only", "Bile", "Fibre"], 0,
  "High osmolar: ↑ carbohydrates -> ↑ CO2, H2O. (Book p33)")
q(33, "TPN Types", "High osmolar TPN carries an increased risk of:",
  ["Thrombosis", "Hypoglycemia", "Diarrhoea", "Aspiration"], 0,
  "High osmolar TPN: ↑ risk of thrombosis. (Book p33)")
q(33, "TPN Types", "Low osmolar TPN decreases CO2 production and is therefore used in:",
  ["Pulmonary failure", "Renal failure", "Liver failure", "Cardiac failure"], 0,
  "Low osmolar: ↓ CO2 production -> used in pulmonary failure. (Book p33)")
q(33, "TPN Types", "Low volume, low protein TPN is used in:",
  ["Renal failure", "Pulmonary failure", "Short bowel syndrome", "Pancreatitis"], 0,
  "Low volume, Low protein: Used in renal failure. (Book p33)")

# ---------------- p34 · DAILY MONITORING ----------------
q(34, "Daily Monitoring", "Daily monitoring on nutritional support includes all of the following EXCEPT:",
  ["Pulse, BP, temperature", "Body weight, abdominal gain", "Fluid balance input-output charting", "Weekly endoscopy"], 3,
  "Daily monitoring: Pulse, BP, temperature; Body weight, abdominal gain; Fluid balance: Input-output charting; Type & quantity of food consumed. (Book p34)")
q(34, "Daily Monitoring", "The earliest sign of overfeeding is:",
  [">1 Kg/day weight gain", ">1 Kg/week weight gain", "Hyperglycemia", "Diarrhoea"], 0,
  "Earliest sign of overfeeding: If >1 Kg/day weight gain. (Book p34)")
q(34, "Daily Monitoring", "Fluid balance during nutritional support is monitored by:",
  ["Input-output charting", "Daily X-ray", "Serum albumin", "Ultrasound"], 0,
  "Fluid balance: Input - output charting. (Book p34)")
q(34, "Daily Monitoring", "Daily monitoring also records the:",
  ["Type and quantity of food consumed", "Daily endoscopy findings", "Central line pressure", "Stool culture"], 0,
  "Daily monitoring: Type & quantity of food consumed. (Book p34)")

# ---------------- p34 · PLASMA MONITORING ----------------
q(34, "Plasma Monitoring", "Plasma monitoring includes sodium, potassium, urea, creatinine, blood glucose and:",
  ["Magnesium, phosphate", "Calcium only", "Serum amylase", "Coagulation profile"], 0,
  "Plasma monitoring: Sodium, potassium, urea, creatinine; Blood glucose; Magnesium, phosphate. (Book p34)")
q(34, "Plasma Monitoring", "Which additional test is part of plasma monitoring on TPN?",
  ["Liver function test", "Thyroid profile", "Serum cortisol", "Blood group"], 0,
  "Plasma monitoring: Liver function test. (Book p34)")
q(34, "Plasma Monitoring", "Once a stable feeding regime is established, plasma monitoring is done:",
  ["Once weekly", "Every hour", "Twice daily", "Once monthly"], 0,
  "Once weekly after establishing a stable feeding regime. (Book p34)")

# ---------------- p34 · COMPLICATIONS OF TPN ----------------
q(34, "Complications of TPN: Line", "The m/c central line related complication of TPN is:",
  ["Catheter related sepsis", "Pneumothorax", "Air embolism", "Migration of line"], 0,
  "Central line related: Catheter related sepsis (m/c). (Book p34)")
q(34, "Complications of TPN: Line", "Catheter related sepsis is confirmed by blood cultures from the peripheral line and central line showing:",
  ["Same organism", "Different organisms", "Sterile growth", "Fungal growth only"], 0,
  "Confirmation: Blood culture from 1. Peripheral line, 2. Central line -> Same organism. (Book p34)")
q(34, "Complications of TPN: Line", "Other confirmation methods for catheter related sepsis include:",
  ["Endoluminal brush and catheter tip culture by removing the line", "Wound swab only", "Urine culture", "Stool culture"], 0,
  "Confirmation: b. Endoluminal brush; c. Catheter tip culture by removing the line. (Book p34)")
q(34, "Complications of TPN: Line", "Central line related complications of TPN include all of the following EXCEPT:",
  ["Pneumothorax", "Arrhythmias", "Thrombosis", "Osmotic diarrhoea"], 3,
  "Central line related: Pneumothorax, Arrhythmias, Thrombosis, Air embolism, Migration of line. (Book p34)")
q(34, "Complications of TPN: Line", "Air embolism and migration of line are complications of TPN related to:",
  ["The central line", "The feeding regime", "The liver", "The kidney"], 0,
  "Central line related complications: Air embolism, Migration of line. (Book p34)")

# ---------------- p34 · FEEDING REGIME COMPLICATIONS ----------------
q(34, "Complications of TPN: Regime", "The m/c feeding regime related complication of TPN is:",
  ["Hyperglycemia", "Cholestasis", "Refeeding syndrome", "Zinc deficiency"], 0,
  "Feeding regime: Hyperglycemia (m/c). (Book p34)")
q(34, "Complications of TPN: Regime", "Weight gain on TPN typically starts after:",
  ["5-7 days", "24 hours", "48 hours", "3 months"], 0,
  "Weight gain: Starts after 5-7 days. (Book p34)")
q(34, "Complications of TPN: Regime", "Cholestasis on TPN presents with deranged liver function and jaundice; the management is to:",
  ["Withhold TPN", "Double the TPN", "Add lipid emulsion", "Give steroids"], 0,
  "Cholestasis: Deranged liver function, Jaundice -> Withhold TPN. (Book p34)")
q(34, "Complications of TPN: Regime", "The m/c micronutrient deficiency on TPN is:",
  ["Zinc", "Copper", "Selenium", "Iron"], 0,
  "Micronutrient deficiency: Zinc: m/c. (Book p34)")
q(34, "Complications of TPN: Regime", "Feeding regime related complications of TPN include refeeding syndrome and:",
  ["Electrolyte imbalance", "Pneumothorax", "Air embolism", "Catheter sepsis"], 0,
  "Feeding regime: Refeeding syndrome; Electrolyte imbalance. (Book p34)")

# ---------------- p34 · DERANGED LIVER ENZYME ----------------
q(34, "Deranged Liver Enzyme", "Deranged liver enzymes on TPN are seen in what percentage of long term TPN use?",
  ["25%", "5%", "50%", "75%"], 0,
  "Deranged liver enzyme: Seen in 25% of long term TPN use. (Book p34)")
q(34, "Deranged Liver Enzyme", "Deranged liver enzymes on TPN are common in:",
  ["Children", "Elderly", "Pregnant women", "Athletes"], 0,
  "Deranged liver enzyme: Common in children. (Book p34)")
q(34, "Deranged Liver Enzyme", "Which hepatic change may be seen on long term TPN?",
  ["Fatty liver", "Cirrhosis only", "Hepatitis A", "Liver abscess"], 0,
  "Fatty liver: May be seen. (Book p34)")
q(34, "Deranged Liver Enzyme", "Fibrosis on long term TPN is described as which associated disease (IFALD)?",
  ["Intestinal (interstitial) failure associated disease", "Insulin failure associated disease", "Immune failure associated disease", "Iron failure associated disease"], 0,
  "Fibrosis: Interstitial failure associated disease (IFALD) may be seen. (Book p34)")
q(34, "Deranged Liver Enzyme", "Management of TPN-related deranged liver enzymes/fibrosis is:",
  ["Lipid free solutions", "High lipid solutions", "Steroids", "Liver transplant always"], 0,
  "Mx: Lipid free solutions. (Book p34)")

# ---------------- p35 · REFEEDING SYNDROME ----------------
q(35, "Refeeding Syndrome", "Refeeding syndrome occurs when:",
  ["Large quantities of nutrition are given to a chronically malnourished patient", "Small feeds are given to an obese patient", "Enteral feed is given post-op day 1", "TPN is stopped abruptly"], 0,
  "Refeeding syndrome: Large quantities of nutrition given to chronically malnourished patient. (Book p35)")
q(35, "Refeeding Syndrome", "In refeeding syndrome, giving TPN in large quantity shifts the patient from a catabolic state to:",
  ["An anabolic state", "A catabolic state", "A starved state", "A septic state"], 0,
  "Pathogenesis: Catabolic state (malnourished) + TPN (large quantity) -> Anabolic state. (Book p35)")
q(35, "Refeeding Syndrome", "The anabolic shift in refeeding syndrome causes influx of which ions into cells?",
  ["PO4 3-, Mg 2+, K+, Ca 2+", "Na+ and Cl- only", "Only H+", "Fe 2+ and Zn 2+"], 0,
  "Influx of PO4^3-, Mg^2+, K+, Ca^2+ into cell. (Book p35)")
q(35, "Refeeding Syndrome", "Which hormone is released during the anabolic shift of refeeding syndrome?",
  ["Insulin", "Glucagon", "Cortisol", "Adrenaline"], 0,
  "Release of insulin. (Book p35)")
q(35, "Refeeding Syndrome", "Refeeding syndrome produces which electrolyte picture?",
  ["Hypophosphatemia, hypocalcemia, hypomagnesemia, hypokalemia + fluid overload", "Hyperphosphatemia and hyperkalemia", "Hypercalcemia and dehydration", "Only hyponatremia"], 0,
  "Hypophosphatemia, Hypocalcemia, Hypomagnesemia, Hypokalemia + Fluid overload. (Book p35)")
q(35, "Refeeding Syndrome", "The electrolyte derangement of refeeding syndrome leads to:",
  ["CHF and arrhythmia", "Pneumothorax", "Fistula formation", "Cholestasis"], 0,
  "Hypophosphatemia etc -> CHF, Arrhythmia. (Book p35)")
q(35, "Refeeding Syndrome", "The m/c cause of death in refeeding syndrome is:",
  ["CHF/arrhythmia", "Sepsis", "Aspiration", "Liver failure"], 0,
  "CHF, Arrhythmia -> m/c cause of death. (Book p35)")
q(35, "Refeeding Syndrome", "The main driver of metabolic derangement in refeeding syndrome is:",
  ["Hypophosphatemia", "Hypokalemia", "Hypocalcemia", "Hyponatremia"], 0,
  "Hypophosphatemia: Main driver of metabolic derangement. (Book p35)")
q(35, "Refeeding Syndrome: Risk Factors", "A BMI below which value is a risk factor for refeeding syndrome?",
  ["<16 Kg/m2", "<20 Kg/m2", "<25 Kg/m2", "<30 Kg/m2"], 0,
  "Risk factors: BMI <16 Kg/m2. (Book p35)")
q(35, "Refeeding Syndrome: Risk Factors", "Unintentional weight loss of >15% in the last how many months is a refeeding risk factor?",
  ["3-6 months", "1 month", "12-24 months", "1 week"], 0,
  "Risk factors: Unintentional weight loss >15% in last 3-6 months. (Book p35)")
q(35, "Refeeding Syndrome: Risk Factors", "Little or no nutritional intake for how long is a refeeding risk factor?",
  [">10 days", ">24 hours", ">48 hours", ">5 days"], 0,
  "Risk factors: Little or no nutritional intake for >10 days. (Book p35)")
q(35, "Refeeding Syndrome: Risk Factors", "Which pre-feeding laboratory pattern is a refeeding risk factor?",
  ["Low potassium, phosphate or magnesium levels", "High potassium and phosphate", "High magnesium", "Low sodium only"], 0,
  "Risk factors: Low potassium, phosphate or magnesium levels prior to feeding. (Book p35)")
q(35, "Refeeding Syndrome: Prevention", "Prevention of refeeding syndrome includes gradual increase of feeds up to a maximum of:",
  ["10 Kcal/kg/day initially, reaching full needs in 4-7 days", "40 Kcal/kg/day on day 1", "20 Kcal/kg/day in 24 hours", "Full needs on day 1"], 0,
  "Prevention: Gradual increase of quantity of feeds; max 10 Kcal/kg/day -> 4-7 days -> Full needs. (Book p35)")
q(35, "Refeeding Syndrome: Prevention", "Prevention of refeeding syndrome includes strict electrolyte monitoring and:",
  ["Thiamine supplementation", "Insulin infusion", "Calcium bolus", "Sodium restriction"], 0,
  "Prevention: Strict electrolyte monitoring; Thiamine supplementation. (Book p35)")

# ---------------- p35 · POST OPERATIVE FLUID REQUIREMENT ----------------
q(35, "Post Operative Fluid Requirement", "Post operative fluid replacement follows:",
  ["Goal directed therapy", "Fixed 5 litres for everyone", "No fluids for 3 days", "Oral fluids only"], 0,
  "Post Operative Fluid Requirement: Goal directed therapy. (Book p35)")
q(35, "Post Operative Fluid Requirement", "Insensible losses (breathing, sweating) are replaced with:",
  ["30-40 mL/kg/day", "10 mL/kg/day", "100 mL/kg/day", "5 mL/kg/day"], 0,
  "Loss/Replacement table: Insensible losses (Breathing, sweating) -> 30-40 mL/kg/day. (Book p35)")
q(35, "Post Operative Fluid Requirement", "Ryles tube aspirate losses are replaced with:",
  ["NS + KCl", "RL", "DNS only", "Colloids"], 0,
  "Loss/Replacement table: Ryles tube aspirate -> NS + KCl. (Book p35)")
q(35, "Post Operative Fluid Requirement", "Drain losses are replaced with:",
  ["RL", "NS + KCl", "DNS", "Half normal saline"], 0,
  "Loss/Replacement table: Drains -> RL. (Book p35)")
q(35, "Post Operative Fluid Requirement", "Urine losses are replaced with:",
  ["NS/DNS", "RL", "Colloids", "D5W only"], 0,
  "Loss/Replacement table: Urine -> NS/DNS. (Book p35)")

# ---------------- p36 · K+ REPLACEMENT & ELECTROLYTES ----------------
q(36, "K+ Replacement", "Potassium replacement in the post operative period is:",
  ["Not given on day 1", "Given on day 1", "Given only intra-operatively", "Never given"], 0,
  "K+ replacement: Not on day 1. (Book p36)")
q(36, "K+ Replacement", "Surgery causes injury to cells leading to:",
  ["Efflux of K+ from cells", "Influx of K+ into cells", "No K+ movement", "Loss of K+ in sweat"], 0,
  "Sx -> Injury to cell -> Efflux of K+ from cell. (Book p36)")
q(36, "K+ Replacement", "Potassium is replaced from which post operative day?",
  ["Day 2", "Day 1", "Day 5", "Day 7"], 0,
  "K+ replacement: Replaced from day 2. (Book p36)")
q(36, "Daily Electrolyte Requirements", "Daily sodium requirement is:",
  ["50-90 mmol/day", "10-20 mmol/day", "150-200 mmol/day", "300 mmol/day"], 0,
  "Daily electrolyte requirements: Sodium: 50-90 mmol/day. (Book p36)")
q(36, "Daily Electrolyte Requirements", "Daily potassium requirement is:",
  ["50 mmol/day", "20 mmol/day", "100 mmol/day", "5 mmol/day"], 0,
  "Daily electrolyte requirements: Potassium: 50 mmol/day. (Book p36)")
q(36, "Daily Electrolyte Requirements", "Daily calcium requirement is:",
  ["5 mmol/day", "1 mmol/day", "20 mmol/day", "50 mmol/day"], 0,
  "Daily electrolyte requirements: Calcium: 5 mmol/day. (Book p36)")
q(36, "Daily Electrolyte Requirements", "Daily magnesium requirement is:",
  ["1 mmol/day", "5 mmol/day", "10 mmol/day", "50 mmol/day"], 0,
  "Daily electrolyte requirements: Magnesium: 1 mmol/day. (Book p36)")

# ---------------- p36 · FLUIDS ----------------
q(36, "Fluids: Crystalloids", "Hartmann's solution (RL) contains sodium (mmol/L) of:",
  ["131", "154", "111", "29"], 0,
  "Crystalloid table: Hartmann's solution (RL): Na 131. (Book p36)")
q(36, "Fluids: Crystalloids", "Hartmann's solution (RL) contains potassium, calcium and lactate (mmol/L) of:",
  ["K 5, Ca 2, Lactate 29", "K 2, Ca 5, Lactate 111", "K 0, Ca 0, Lactate 0", "K 20, Ca 5, Lactate 29"], 0,
  "Crystalloid table: Hartmann's (RL): K 5, Ca 2, Lactate 29. (Book p36)")
q(36, "Fluids: Crystalloids", "The chloride content of Hartmann's solution and normal saline respectively is:",
  ["111 and 154", "154 and 111", "131 and 154", "29 and 154"], 0,
  "Crystalloid table: RL Cl 111; Normal saline Cl 154. (Book p36)")
q(36, "Fluids: Crystalloids", "Normal saline contains sodium and chloride (mmol/L) of:",
  ["154 and 154", "131 and 111", "154 and 111", "131 and 154"], 0,
  "Crystalloid table: Normal saline: Na 154, Cl 154. (Book p36)")
q(36, "Fluids: Colloids", "Colloids include all of the following EXCEPT:",
  ["Gelofusine", "Haemaccel", "Hetastarch", "Hartmann's solution"], 3,
  "Colloids: Gelofusine, Haemaccel, Hetastarch, Blood products. (Book p36)")
q(36, "Fluids: Colloids", "The main action of colloids (Gelofusine, Haemaccel, Hetastarch, blood products) is to:",
  ["Expand blood volume", "Provide calories", "Correct acidosis", "Replace potassium"], 0,
  "Colloids: Expand blood volume. (Book p36)")
q(36, "Calories", "Calories obtained from carbohydrate and amino acids respectively are:",
  ["4 Kcal/g and 4 Kcal/g", "4 Kcal/g and 9 Kcal/g", "9 Kcal/g and 4 Kcal/g", "7 Kcal/g and 4 Kcal/g"], 0,
  "Calories obtained: Carbohydrate: 4 Kcal/g; Aminoacid: 4 Kcal/g. (Book p36)")
q(36, "Calories", "Calories obtained from fat are:",
  ["9 Kcal/g", "4 Kcal/g", "7 Kcal/g", "2 Kcal/g"], 0,
  "Calories obtained: Fat: 9 Kcal/g. (Book p36)")

# ---------------- UNITS ----------------
def uid(n): return {"id": f"SURG-U6-{n}", "ch": 6, "n": n}
def rng(a, b): return [f"SURG-C6-{i:03d}" for i in range(a, b + 1)]
UNITS = [
    {**uid(1), "title": "Nutritional Assessment: Indicators", "sec": "Nutritional Assessment \u00b7 p28",
     "qs": rng(1, 8),
     "guide": "No single biochemical marker identifies malnutrition: low albumin foretells poor outcome while pre albumin tracks better, >10% unintentional weight loss in 6 months and BMI <15 signal poor prognosis, and skin fold thickness reads body fat while mid arm circumference reads muscle mass."},
    {**uid(2), "title": "MUST Tool & Energy Requirement", "sec": "Malnutrition Universal Screening Tool \u00b7 p28",
     "qs": rng(9, 15),
     "guide": "The MUST tool adds BMI score, unintentional weight loss and acute disease affect score into an overall malnutrition risk, while the REE table climbs from 1 (20 Kcal/kg/day sedentary) through 1.4 and 1.8 sepsis to 2 with 40 Kcal/kg/day in severe burns."},
    {**uid(3), "title": "Enteral vs Parenteral & Route Algorithm", "sec": "Enteral and Parenteral Nutrition \u00b7 p28",
     "qs": rng(16, 25),
     "guide": "Enteral beats parenteral because it is physiological, cheap, maintains enterohepatic circulation and blocks bacterial translocation. When oral fails, duration and gastric emptying decide: under 3 weeks a nasogastric or nasojejunal tube, beyond 3 weeks a gastrostomy or jejunostomy."},
    {**uid(4), "title": "Ryles & Nasojejunal Tubes", "sec": "Ryles Tube \u00b7 p29",
     "qs": rng(26, 31),
     "guide": "Insert the Ryles tube sitting with the neck slightly flexed, measure nose-ear-xiphisternum, and confirm by aspirating gastric contents or auscultating pushed air over the epigastrium; the nasojejunal tube goes in under fluoroscopy and bypasses the stomach."},
    {**uid(5), "title": "Invasive Feeding Tubes: Stamm, Witzel, Gastrostomy vs Jejunostomy", "sec": "Invasive Feeding Tubes \u00b7 p30",
     "qs": rng(32, 40),
     "guide": "Gastrostomy (Stamm, Witzel, PEG/RIG) is more physiological than jejunostomy (Stamm, Witzel) but risks aspiration. Stamm uses a Red Robinson tube through a stab incision and purse string with peridrain leakage; Witzel tunnels the distal jejunum and leaks less."},
    {**uid(6), "title": "Technique of PEG & RIG", "sec": "Technique of PEG \u00b7 p31",
     "qs": rng(41, 47),
     "guide": "PEG runs from transoral endoscope insufflation through transillumination and finger indentation, transgastric suture fixation and a Seldinger gastrostomy; RIG steps in when endoscopy is impossible or respiratory or oropharyngeal function is compromised."},
    {**uid(7), "title": "Enteral Principle & Complications", "sec": "Enteral Nutrition: Principle \u00b7 p31",
     "qs": rng(48, 56),
     "guide": "Start feeds at 10-20 mL/hr and climb to 75 mL/hr if tolerated, withholding the next feed when aspirates exceed 75-100 cc. Tube problems (blockage, migration, leakage) are the m/c complication, while osmotic diarrhoea from hyperosmolar feeds leads feeding-regime trouble."},
    {**uid(8), "title": "Parenteral Nutrition: Indications & Routes", "sec": "Parenteral Nutrition \u00b7 p32",
     "qs": rng(57, 66),
     "guide": "TPN serves paralytic ileus beyond 72 hours, non-contracting bowel, short bowel syndrome, >500 cc faecal fistulas, acute IBD needing bowel rest and early severe pancreatitis. The central line is the best route, PICC sits in between, and peripheral lines are least preferred for thrombophlebitis."},
    {**uid(9), "title": "Central Line: Vein Comparison & Assessment", "sec": "Central Line \u00b7 p32",
     "qs": rng(67, 76),
     "guide": "Subclavian lines thrombose and infect least but pneumothorax most and dominate TPN; the internal jugular is easiest to place and the commonest vein overall; femoral lines infect most. The tip must sit in the SVC just above the right atrium, and the X-ray also rules out pneumothorax."},
    {**uid(10), "title": "PICC Line", "sec": "PICC Line \u00b7 p33",
     "qs": rng(77, 81),
     "guide": "Ultrasound-guided into a peripheral vessel with the tip just above the right atrium, a PICC lasts 2-3 months for chemotherapy, TPN or prolonged antibiotics - but demands regular dressing and care."},
    {**uid(11), "title": "TPN Solution & Types", "sec": "TPN Solution \u00b7 p33",
     "qs": rng(82, 91),
     "guide": "1-2 litres over 24 hours in a 20:30:50 protein:fat:carbohydrate mix, as 3-in-1 or 2-in-1 bags with trace elements and vitamins but no fibre. High osmolar bags raise CO2 and thrombosis risk, low osmolar bags suit pulmonary failure, and low volume low protein bags suit renal failure."},
    {**uid(12), "title": "Monitoring on Nutritional Support", "sec": "Monitoring \u00b7 p34",
     "qs": rng(92, 98),
     "guide": "Daily: pulse, BP, temperature, weight and abdominal gain (>1 Kg/day is the earliest sign of overfeeding), input-output charts and food consumed. Plasma: Na, K, urea, creatinine, glucose, magnesium, phosphate and LFTs, weekly once the regime is stable."},
    {**uid(13), "title": "Complications of TPN", "sec": "Complications of TPN \u00b7 p34",
     "qs": rng(99, 113),
     "guide": "Catheter related sepsis is the m/c line complication, confirmed by matching peripheral and central cultures, endoluminal brush or tip culture; lines also bring pneumothorax, arrhythmias, thrombosis, air embolism and migration. The regime brings hyperglycemia, cholestasis (withhold TPN), zinc deficiency, refeeding and electrolyte imbalance, and 25% of long-term users derange liver enzymes - managed with lipid free solutions."},
    {**uid(14), "title": "Refeeding Syndrome", "sec": "Refeeding Syndrome \u00b7 p35",
     "qs": rng(114, 127),
     "guide": "Feeding a chronically starved patient flips catabolism into an insulin-driven anabolic state that drags phosphate, magnesium, potassium and calcium into cells; hypophosphatemia drives the derangement and CHF/arrhythmia kill. Risk: BMI <16, >15% weight loss in 3-6 months, >10 days without intake, low pre-feeding electrolytes - prevent with slow feeds (max 10 Kcal/kg/day to full needs over 4-7 days), electrolyte monitoring and thiamine."},
    {**uid(15), "title": "Post Operative Fluid Requirement", "sec": "Post Operative Fluid Requirement \u00b7 p35",
     "qs": rng(128, 132),
     "guide": "Goal directed replacement: insensible losses 30-40 mL/kg/day, Ryles aspirate with NS + KCl, drains with RL and urine with NS/DNS."},
    {**uid(16), "title": "K+, Daily Electrolytes, Fluids & Calories", "sec": "K+ Replacement \u00b7 p36",
     "qs": rng(133, 147),
     "guide": "Potassium waits until day 2 because surgical cell injury dumps K+ out of cells; daily needs run Na 50-90, K 50, Ca 5, Mg 1 mmol. Hartmann's (Na 131, K 5, Ca 2, Cl 111, lactate 29) contrasts with normal saline (154/154), colloids expand blood volume, and calories come 4-4-9 from carbohydrate, amino acid and fat."},
]

data = {"questions": Q, "units": UNITS}
with open("data/ch6.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
print(f"ch6: {len(Q)} questions, {len(UNITS)} units")
