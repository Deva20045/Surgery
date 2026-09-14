#!/usr/bin/env python3
"""Build data/ch55.json — Abdominal Trauma (Marrow Surgery Ed 8, pp417-425)."""
import json

Q = []

def q(page, sec, text, correct, wrongs, note=None):
    opts = [correct] + list(wrongs)
    assert len(opts) == 4
    Q.append({
        "id": f"SURG-C55-{len(Q)+1:03d}",
        "sec": sec,
        "page": page,
        "q": text,
        "opts": opts,
        "ans": 0,
        "exp": (note or correct) + f" (Book p{page})",
    })

# ------------------------------------------------------------------ p417
S1 = "Most Commonly Injured Organs and Blunt Trauma: FAST/eFAST"
q(417, S1, "Overall, the m/c injured organ in abdominal trauma is the:", "Spleen", ["Liver", "Small intestine", "Kidney"])
q(417, S1, "In blunt abdominal trauma the order of injury is:", "Spleen > Liver", ["Liver > Spleen", "Small intestine > Liver", "Spleen > Kidney"])
q(417, S1, "In penetrating abdominal trauma the order of injury is:", "Liver > Small intestine", ["Small intestine > Liver", "Spleen > Liver", "Stomach > Liver"])
q(417, S1, "In gunshot wounds (GSW) the order of injury is:", "Small intestine > Liver", ["Liver > Small intestine", "Colon > Liver", "Spleen > Colon"])
q(417, S1, "Seatbelt syndrome characteristically injures the:", "Mesentery", ["Duodenum", "Spleen", "Bladder"])
q(417, S1, "Deceleration injury characteristically injures the:", "Duodeno-jejunal flexure", ["Mesentery", "Spleen", "Rectum"])
q(417, S1, "In children the order of abdominal organ injury is:", "Spleen > Kidney", ["Liver > Spleen", "Kidney > Spleen", "Spleen > Liver"])
q(417, S1, "In a hemodynamically stable blunt abdominal trauma patient, the 1st Ix is:", "FAST", ["CECT", "DPL", "X-ray"])
q(417, S1, "In a hemodynamically stable blunt patient, the IOC is:", "CECT", ["FAST", "DPL", "MRI"])
q(417, S1, "In a hemodynamically unstable blunt patient, the 1st Ix is:", "FAST", ["CECT", "DPL", "Angiogram"])
q(417, S1, "In a hemodynamically unstable blunt patient, the IOC is:", "FAST", ["CECT", "DPL", "MRI"])
q(417, S1, "The definitive management of blunt abdominal trauma needing surgery is:", "Midline laparotomy", ["Kocher's incision", "Pfannenstiel", "Laparoscopy"])
q(417, S1, "FAST stands for:", "Focused assessment sonogram in trauma", ["Fast abdominal sonographic test", "Focused abdominal scanning technique", "Free abdominal sonography triage"])
q(417, S1, "FAST USG is done in the:", "Emergency room (ER)", ["OT", "Radiology suite", "ICU only"])
q(417, S1, "The advantage of FAST is that it:", "Can be done quickly and gives crucial information", ["Detects all hollow viscus injury", "Quantifies blood loss", "Replaces CT"])
q(417, S1, "The first FAST view is the:", "Epigastrium", ["Right upper quadrant", "Left upper quadrant", "Suprapubic"])
q(417, S1, "The second FAST view is the:", "Right upper quadrant", ["Epigastrium", "Left upper quadrant", "Suprapubic"])
q(417, S1, "The third FAST view is the:", "Left upper quadrant", ["Epigastrium", "RUQ", "Suprapubic"])
q(417, S1, "The fourth FAST view is the:", "Suprapubic", ["Epigastrium", "RUQ", "LUQ"])
q(417, S1, "eFAST (extended FAST) adds assessment of the:", "Thoracic cavity (5) & (6)", ["Pelvis only", "Retroperitoneum", "Groin"])
q(417, S1, "The advantage of eFAST is that it detects free fluid in the abdomen or:", "Pericardium", ["Pleura only", "Scrotum", "Joints"])
q(417, S1, "On the probe-site diagram, the RUQ probe looks for collection around the:", "Liver", ["Spleen", "Pelvis", "Pericardium"])
q(417, S1, "On the probe-site diagram, the LUQ probe looks for collection around the:", "Spleen", ["Liver", "Pelvis", "Pericardium"])
q(417, S1, "The epigastric/subxiphoid/PSL probe gives the pericardial window for:", "Cardiac tamponade", ["Pneumothorax", "Pelvic collection", "Liver tear"])
q(417, S1, "The suprapubic probe looks for collection in the:", "Pelvis", ["Pericardium", "LUQ", "RUQ"])
q(417, S1, "The right and left anterior chest probes (5, 6) look for:", "Pneumothorax", ["Hemothorax only", "Tamponade", "Diaphragm tear"])
q(417, S1, "Free fluid on FAST USG appears as a:", "Hypoechoic collection", ["Hyperechoic collection", "Anechoic gas shadow", "Calcific focus"])

# ------------------------------------------------------------------ p418
S2 = "FAST Disadvantages, Blunt Work-up and Penetrating Trauma Work-up"
q(418, S2, "FAST will not reliably detect free blood less than:", "<100 ml", ["<10 ml", "<500 ml", "<1 litre"])
q(418, S2, "FAST does not directly identify injury to:", "Hollow viscous", ["Solid organs", "Pericardium", "Pelvis"])
q(418, S2, "FAST cannot reliably exclude injury in:", "Penetrating trauma", ["Blunt trauma", "Children", "Pedestrians"])
q(418, S2, "FAST may need repeating or supplementing with:", "Other Ix", ["Clinical exam only", "Repeat FAST never", "Observation only"])
q(418, S2, "FAST is unreliable for assessment of the retroperitoneum because of:", "Bowel gas", ["Fat", "Bone", "Fluid"])
q(418, S2, "Another disadvantage of FAST is that it is:", "Operator dependent", ["Time consuming", "Radiation heavy", "Costly"])
q(418, S2, "In the blunt work-up, peritonitis or hemodynamic instability with positive FAST leads to:", "Exploratory laparotomy", ["Abdominal CT scan", "Observation", "DPL"])
q(418, S2, "In the blunt work-up, no peritonitis and no hemodynamic instability leads to:", "Abdominal CT scan", ["Exploratory laparotomy", "FAST repeat only", "DPL"])
q(418, S2, "On CT, hollow organ injury yes or indeterminate leads to:", "Exploratory laparotomy or diagnostic laparoscopy", ["Nonoperative management", "IR evaluation", "Observation"])
q(418, S2, "Solid organ injury with pseudoaneurysm or arterial blush on contrasted CT leads to:", "Interventional radiology evaluation", ["Nonoperative management", "Laparotomy always", "Antibiotics"])
q(418, S2, "Solid organ injury without pseudoaneurysm/blush is managed by:", "Nonoperative management", ["IR evaluation", "Laparotomy", "Laparoscopy"])
q(418, S2, "If CT shows no solid organ injury, the work-up directs to:", "Manage other injuries", ["Laparotomy", "IR", "Repeat CT"])
q(418, S2, "In penetrating trauma, a sharp object in the ER should:", "Never be removed as it can lead to ↑ bleeding", ["Be removed immediately", "Be pushed in further", "Be cut at skin level"])
q(418, S2, "A penetrating injury superficial to the peritoneum is worked up with:", "Local examination & CECT abdomen", ["Midline laparotomy", "DPL", "FAST only"])
q(418, S2, "Peritoneal breach (+) features include peritonitis with rebound tenderness and:", "Rigidity, guarding", ["Borborygmi", "Tympany only", "Visible peristalsis"])
q(418, S2, "Other features of peritoneal breach are omentum hanging out, bile staining and:", "Hemodynamic instability", ["Fever only", "Leukocytosis only", "Bruising"])
q(418, S2, "Peritoneal breach (+) is managed by:", "Midline laparotomy (no Ix done)", ["CECT first", "DPL first", "Observation"])

# ------------------------------------------------------------------ p419
S3 = "Diagnostic Peritoneal Lavage and Splenic Trauma Grading"
q(419, S3, "DPL is indicated when:", "FAST is not available", ["CT is available", "Patient is stable", "FAST is positive"])
q(419, S3, "Before DPL, the stomach is decompressed with a Ryle's tube and the bladder with a:", "Urinary catheter", ["Suprapubic catheter", "Cystoscope", "Nephrostomy"])
q(419, S3, "The DPL needle is inserted:", "Just below the umbilicus", ["Above the umbilicus", "In the left iliac fossa", "Suprapubically"])
q(419, S3, "Aspirating >10 cc of gross blood at DPL means:", "Positive DPL", ["Negative DPL", "Repeat lavage", "Instill saline"])
q(419, S3, "If no blood is aspirated at DPL, the next step is to instill:", "1 L of Ringer lactate", ["1 L of normal saline", "500 mL of saline", "2 L of Ringer lactate"])
q(419, S3, "After instillation, the DPL fluid is positive if RBC count exceeds:", ">1 lakh/cumm", [">10,000/cumm", [">50,000/cumm"] , ">5 lakh/cumm"])
q(419, S3, "DPL fluid is positive if WBC count exceeds:", ">500/cumm", [">100/cumm", [">1000/cumm"] , ">5000/cumm"])
q(419, S3, "DPL fluid is positive if serum amylase exceeds:", ">175 IU/L", [">75 IU/L", [">100 IU/L"] , ">300 IU/L"])
q(419, S3, "DPL fluid is also positive with the presence of:", "Fecal content", ["Bile only", "Air only", "Food fibres only"])
q(419, S3, "Management of a +ve DPL is:", "Midline laparotomy", ["Observation", "CECT", "Repeat DPL"])
q(419, S3, "The m/c organ injured in abdominal trauma is the:", "Spleen", ["Liver", "Kidney", "Pancreas"])
q(419, S3, "Suspect splenic trauma with fracture of which ribs on the left side?", "9-11th ribs", ["7-8th ribs", ["11-12th ribs"] , "5-6th ribs"])
q(419, S3, "Another clue to splenic trauma is bruising of the:", "Left lower chest wall", ["Left flank only", "Epigastrium", "Left shoulder"])
q(419, S3, "The +ve sign seen in splenic rupture is the:", "Kehr sign", ["Ballance sign", ["Grey Turner sign"] , "Cullen sign"])
q(419, S3, "Kehr sign is elicited by raising the left lower limb so that blood accumulates beneath the:", "Left dome of diaphragm", ["Right dome of diaphragm", ["Splenic flexure"] , "Left paracolic gutter"])
q(419, S3, "Kehr sign produces referred pain to the:", "Shoulder tip", ["Left flank", "Epigastrium", "Back"])
q(419, S3, "Grade 1 splenic trauma includes subcapsular haematoma of:", "<10% of surface area", ["10-50% of surface area", [">50% of surface area"] , ">25% of surface area"])
q(419, S3, "Grade 1 splenic trauma parenchymal laceration depth is:", "<1 cm", ["1-3 cm", [">3 cm"] , "<3 cm"])
q(419, S3, "Grade 1 splenic trauma also includes a:", "Capsular tear", ["Hilar tear", ["Shattered spleen"] , "Vascular injury"])
q(419, S3, "Grade 2 splenic trauma subcapsular haematoma covers:", "10-50% of surface area", ["<10%", [">50%"] , "10-30%"])
q(419, S3, "Grade 2 splenic trauma intraparenchymal haematoma is:", "<5 cm", [">5 cm", ["<10 cm"] , ">10 cm"])
q(419, S3, "Grade 2 splenic trauma parenchymal laceration depth is:", "1-3 cm", ["<1 cm", [">3 cm"] , "3-5 cm"])
q(419, S3, "Grade 3 splenic trauma subcapsular haematoma covers:", ">50% surface area", ["<10%", ["10-50%"] , "25-50%"])
q(419, S3, "Grade 3 splenic trauma ruptured subcapsular or intraparenchymal haematoma is:", ">5 cm", ["<5 cm", [">2 cm"] , "<2 cm"])
q(419, S3, "Grade 3 splenic trauma parenchymal laceration depth is:", ">3 cm", ["1-3 cm", ["<1 cm"] , ">5 cm"])
q(419, S3, "Grade 4 splenic trauma is any injury with a splenic vascular injury or active bleeding confined within the splenic capsule, or laceration of segmental/hilar vessels producing:", ">25% devascularisation", [">10% devascularisation", [">50% devascularisation"] , ">75% devascularisation"])
q(419, S3, "Grade 5 splenic trauma is a:", "Shattered spleen + vascular injury", ["Subcapsular haematoma >50%", ["Hilar avulsion only"] , "Capsular tear only"])

# ------------------------------------------------------------------ p420
S4 = "Splenic Trauma: Imaging, Management and Splenectomy Complications"
q(420, S4, "On delayed splenic CT imaging, a pseudoaneurysm or arteriovenous fistula shows a subsequent:", "↓ in arterial blush", ["↑ in arterial blush", ["No change in blush"] , "New blush"])
q(420, S4, "Active bleeding from a splenic vascular injury shows a subsequent:", "↑ in arterial blush in delayed imaging", ["↓ in arterial blush", ["Washout"] , "No blush"])
q(420, S4, "Grade I & II splenic injuries are usually:", "Stable", ["Unstable", ["Transient"] , "Shocky"])
q(420, S4, "The IOC for grade I & II splenic injury is:", "CECT", ["FAST", ["DPL"] , "X-ray"])
q(420, S4, "Conservative splenic management monitors vitals, haematocrit and:", "Serial 24 hr CECT", ["Serial FAST", ["Daily DPL"] , "Weekly MRI"])
q(420, S4, "An ↑ in grade of injury or contrast blush on CECT in a conserved spleen prompts:", "Angioembolization", ["Laparotomy", ["Splenectomy"] , "Observation"])
q(420, S4, "Conservative splenic management that fails, or shows unstable vitals or peritonitis, proceeds to:", "Laparotomy", ["Angioembolization", ["Repeat CECT"] , "Transfusion alone"])
q(420, S4, "At laparotomy for splenic injury, the preferred approach is:", "Splenic preservation/splenorrhaphy", ["Splenectomy always", ["Partial splenectomy only"] , "Packing"])
q(420, S4, "A stable grade III splenic injury is managed:", "Same as grade I & II", ["Same as grade IV & V", ["Splenectomy"] , "Angioembolization always"])
q(420, S4, "An unstable grade III splenic injury is managed:", "Same as grade IV & V", ["Same as grade I & II", ["Conservatively"] , "By angioembolization"])
q(420, S4, "The IOC for unstable grade IV or V splenic injury is:", "FAST", ["CECT", ["DPL"] , "MRI"])
q(420, S4, "A FAST +ve unstable grade IV/V splenic injury needs laparotomy with:", "Splenectomy (difficult to save the spleen)", ["Splenorrhaphy", ["Packing only"] , "Angioembolization"])
q(420, S4, "The first complication of splenectomy listed is:", "Hemorrhage", ["Pancreatic fistula", ["OPSI"] , "Thrombocytosis"])
q(420, S4, "Splenectomy risks injury to the pancreas because the tail of pancreas lies:", "Close to hilum of spleen", ["Behind the stomach", ["In the splenorenal ligament only"] , "Near the splenic flexure"])
q(420, S4, "Pancreatic tail injury during splenectomy causes a pancreatic fistula with:", "Amylase rich secretions", ["Bile rich secretions", ["Chyle"] , "Pus"])
q(420, S4, "Post-splenectomy hematological change shows transient ↑ in all 3 cell lines for:", "2 weeks", ["2 days", ["2 months"] , "6 weeks"])
q(420, S4, "The post-splenectomy ↑ WBC is often:", "Mistaken for infection", ["Mistaken for leukemia", ["Ignored"] , "Treated with G-CSF"])
q(420, S4, "Post-splenectomy platelets >10 lakh/cumm predispose to:", "Thrombosis", ["Bleeding", ["Sepsis"] , "Anemia"])
q(420, S4, "Post-splenectomy thrombocytosis is treated with:", "Prophylactic aspirin", ["Heparin drip", ["Warfarin"] , "Plateletpheresis always"])
q(420, S4, "Permanent peripheral smear changes post-splenectomy include basophilic stippling, reticulocytes, Howell-Jolly bodies and:", "Hypersegmented WBC's", ["Hyposegmented WBC's", ["Target cells only"] , "Spherocytes only"])

# ------------------------------------------------------------------ p421
S5 = "OPSI, Post-splenectomy Vaccination and Liver Trauma Grades"
q(421, S5, "The m/c complication after splenectomy listed is:", "Left lower lobe atelectasis/pneumonia", ["OPSI", ["Hemorrhage"] , "Fistula"])
q(421, S5, "Left lower lobe atelectasis/pneumonia post-splenectomy is due to:", "↓ expansion of chest on (L) side", ["Aspiration", ["Emboli"] , "Effusion"])
q(421, S5, "OPSI stands for:", "Opportunistic/Overwhelming Post Splenectomy Infection", ["Overwhelming Post Surgical Infection", ["Opportunistic Post Septic Injury"] , "Overwhelming Pneumococcal Sepsis Infection"])
q(421, S5, "OPSI is caused by encapsulated bacteria, the m/c being:", "Pneumococcus", ["Meningococcus", ["H. influenzae"] , "Staphylococcus"])
q(421, S5, "Other OPSI organisms are meningococcus and:", "H. influenzae", ["E. coli", ["Klebsiella"] , "Pseudomonas"])
q(421, S5, "OPSI occurs in:", "Children > adults", ["Adults > children", ["Equal"] , "Elderly only"])
q(421, S5, "OPSI is seen commonly within the first:", "2 years of splenectomy", ["2 months", ["5 years"] , "10 years"])
q(421, S5, "OPSI mortality is highest in:", "Hematological conditions > Trauma", ["Trauma > hematological", ["Equal"] , "Iatrogenic only"])
q(421, S5, "Pneumococcal & meningococcal vaccination post-splenectomy is repeated every:", "5 years", ["2 years", ["10 years"] , "Yearly"])
q(421, S5, "H. influenzae vaccination post-splenectomy is repeated every:", "10 years", ["5 years", ["Yearly"] , "2 years"])
q(421, S5, "The vaccine repeated yearly post-splenectomy is:", "Influenzae", ["Pneumococcal", ["Meningococcal"] , "H. influenzae"])
q(421, S5, "For elective splenectomy, vaccines are given:", "2 weeks before", ["2 weeks after", ["On the day"] , "1 month after"])
q(421, S5, "For emergency splenectomy, vaccines are given on:", "Post op day 1/2", ["Post op day 7", ["Post op day 14"] , "Post op day 30"])
q(421, S5, "Antibody titres are less when the vaccine is given:", "After Sx", ["Before Sx", ["During Sx"] , "Never"])
q(421, S5, "Liver grade 1 haematoma is subcapsular and covers:", "<10% surface area", ["10-50%", [">50%"] , "<25%"])
q(421, S5, "Liver grade 1 laceration is a capsular tear with parenchymal depth:", "<1 cm", ["1-3 cm", [">3 cm"] , "<2 cm"])
q(421, S5, "Liver grade 2 subcapsular haematoma covers:", "10-50% surface area", ["<10%", [">50%"] , "25-75%"])
q(421, S5, "Liver grade 2 intraparenchymal haematoma diameter is:", "<10 cm", [">10 cm", ["<5 cm"] , ">5 cm"])
q(421, S5, "Liver grade 2 laceration is a capsular tear 1-3 cm deep and:", "<10 cm length", [">10 cm length", ["<5 cm length"] , ">5 cm length"])
q(421, S5, "Liver grade 3 subcapsular haematoma covers:", ">50% surface area (ruptured subcapsular or intraparenchymal)", ["10-50%", ["<10%"] , "25-50%"])
q(421, S5, "Liver grade 3 intraparenchymal haematoma is:", ">10 cm", ["<10 cm", [">5 cm"] , "<5 cm"])
q(421, S5, "Liver grade 3 laceration depth is:", ">3 cm", ["1-3 cm", ["<1 cm"] , ">5 cm"])
q(421, S5, "Liver grade 3 also includes vascular injury with active bleeding:", "Contained within liver parenchyma", ["Breaching into peritoneum", ["Into bile ducts"] , "Into IVC"])
q(421, S5, "Liver grade 4 laceration disrupts parenchyma involving:", "25-75% hepatic lobe or 1-3 Couinaud segments", ["<25% lobe", [">75% lobe"] , "Whole lobe"])
q(421, S5, "Liver grade 4 vascular injury bleeds actively:", "Breaching the liver parenchyma into the peritoneum", ["Contained within parenchyma", ["Into biliary tree"] , "Into portal vein"])
q(421, S5, "Liver grade 5 laceration disrupts:", ">75% of hepatic lobe", ["25-75% lobe", ["50% lobe"] , "<25% lobe"])
q(421, S5, "Liver grade 5 vascular injury involves:", "Juxtahepatic venous injuries (retrohepatic vena cava/central major hepatic veins)", ["Portal vein only", ["Hepatic artery only"] , "Cystic vein"])
q(421, S5, "For multiple liver injuries, the grade is advanced by one up to grade:", "III", ["II", ["IV"] , "V"])

# ------------------------------------------------------------------ p422
S6 = "Liver Trauma Work-up, Pringle's Manoeuvre and Packing"
q(422, S6, "The first step in the liver trauma work-up is to:", "Resuscitate", ["Operate", ["Scan"] , "Transfuse"])
q(422, S6, "Unstable liver trauma (grade III, IV, V) proceeds to:", "Surgery", ["Conservative mx", ["Angioembolization"] , "Observation"])
q(422, S6, "Stable liver trauma (grade I, II, III) is managed:", "Conservatively", ["Surgically", ["By embolization"] , "By packing"])
q(422, S6, "Conservative liver management consists of monitor, hematocrit and:", "Serial CECT", ["Serial FAST", ["Daily DPL"] , "Weekly MRI"])
q(422, S6, "A conservatively managed liver patient who remains stable is:", "Discharged", ["Operated", ["Embolized"] , "Kept for 2 weeks"])
q(422, S6, "Conservative liver management complications to treat include hemorrhage, biliary, vascular and:", "Sepsis", ["Fistula", ["Stricture"] , "Abscess only"])
q(422, S6, "A conserved liver patient who becomes unstable goes to:", "Surgery", ["Repeat CECT", ["Embolization"] , "ICU only"])
q(422, S6, "Pringle's manoeuvre compresses the:", "Hepatic pedicle", ["Portal vein only", ["Hepatic artery only"] , "IVC"])
q(422, S6, "Pringle's manoeuvre compresses the pedicle for:", "15-20 mins", ["5-10 mins", ["30-45 mins"] , "60 mins"])
q(422, S6, "Pringle's manoeuvre compresses the pedicle at the:", "Foramen of Winslow", ["Foramen magnum", ["Epiploic foramen of Morgagni"] , "Hepatoduodenal ligament root only"])
q(422, S6, "The foramen of Winslow contents compressed in Pringle's manoeuvre are:", "Common bile duct (CBD), portal vein, hepatic artery", ["IVC, aorta, crura", ["CBD, IVC, aorta"] , "Portal vein, splenic vein, IMV"])
q(422, S6, "If bleeding ↓ with Pringle's manoeuvre, the cause is the:", "Portal vein/hepatic artery", ["Hepatic vein", ["IVC"] , "Cystic artery"])
q(422, S6, "If bleeding continues with Pringle's manoeuvre, the cause is the:", "Hepatic vein", ["Portal vein", ["Hepatic artery"] , "CBD"])
q(422, S6, "An advantage of Pringle's manoeuvre is to:", "Achieve temporary control", ["Achieve permanent control", ["Diagnose cirrhosis"] , "Prevent sepsis"])
q(422, S6, "The other advantage of Pringle's manoeuvre is:", "To find the source of bleed", ["To biopsy liver", ["To drain bile"] , "To mobilize colon"])
q(422, S6, "In liver packing, the first step is to cut the:", "Rt & Lt triangular ligaments", ["Falciform ligament", ["Round ligament"] , "Hepatogastric ligament"])
q(422, S6, "Cutting the triangular ligaments lets the liver separate from the:", "Diaphragm", ["Stomach", ["Kidney"] , "Colon"])
q(422, S6, "Liver packing places mops above & below the liver for:", "24-48 hrs", ["6-12 hrs", ["72-96 hrs"] , "1 week"])
q(422, S6, "Packing controls bleeding by the:", "Tamponading effect", ["Coagulation cascade", ["Vasoconstriction"] , "Hypothermia"])

# ------------------------------------------------------------------ p423
S7 = "Liver Complications, Mesenteric Injury and Duodenal/Pancreatic Injury"
q(423, S7, "The first complication of liver trauma is:", "Bleeding", ["Bile leak", ["Abscess"] , "Stricture"])
q(423, S7, "A bile leak from minor biliary radicles is managed by:", "Ligate the radicles", ["Repair over T-tube", ["Whipple's"] , "Stenting"])
q(423, S7, "A bile leak from CBD/major ducts is managed by:", "Repair over T-tube", ["Ligate the duct", ["Choledochojejunostomy always"] , "Observation"])
q(423, S7, "The third complication of liver trauma is:", "Liver abscess", ["Strictures in CBD", ["AV malformations"] , "Portal vein injury"])
q(423, S7, "The fourth complication of liver trauma is:", "Strictures in CBD", ["Liver abscess", ["AV malformations"] , "Biloma"])
q(423, S7, "The fifth complication of liver trauma is:", "AV malformations", ["Strictures", ["Abscess"] , "Hernia"])
q(423, S7, "Vascular injury to the portal vein is managed by:", "Repair with prolene suture", ["Ligation", ["Graft always"] , "Stent"])
q(423, S7, "In a longitudinal mesenteric tear:", "Only 1 branch is cut, no loss of vascularity", ["All vessels are cut", ["Vascularity lost"] , "Bowel is devascularised"])
q(423, S7, "A longitudinal mesenteric tear is managed by:", "Repair the tear", ["Resection & anastomosis", ["Exteriorisation"] , "Stoma"])
q(423, S7, "In a transverse mesenteric tear:", "All vessels are cut, loss of vascularity", ["Only 1 branch is cut", ["No vascular loss"] , "Tear is superficial"])
q(423, S7, "A transverse mesenteric tear is managed by:", "Resection & anastomosis", ["Repair the tear", ["Patch"] , "Stoma only"])
q(423, S7, "The mildest duodenal injury is:", "Duodenal haematoma", ["Duodenal perforation", ["Pancreatic injury"] , "Duodenal transection"])
q(423, S7, "Duodenal haematoma is managed by keeping the patient NPO for:", "Bowel rest", ["Early feeds", ["TPN always"] , "Surgery"])
q(423, S7, "Duodenal perforation presents with:", "Features of peritonitis", ["Obstruction", ["Jaundice"] , "GI bleed"])
q(423, S7, "X-ray in duodenal perforation shows:", "Gas under diaphragm", ["Air-fluid levels", ["Calcification"] , "Retroperitoneal air only"])
q(423, S7, "Duodenal perforation is managed by:", "Omental patch repair", ["Resection", ["Whipple's"] , "Diversion only"])
q(423, S7, "Pancreatic injury is:", "2° to blunt/penetrating trauma", ["1° spontaneous", ["Only iatrogenic"] , "Only penetrating"])
q(423, S7, "The most important prognostic factor in pancreatic injury is:", "Injury to main pancreatic duct", ["Parenchymal contusion", ["Duodenal involvement"] , "Vascular injury"])
q(423, S7, "In the book's pancreatic injury flowchart, the arm labelled YES (injury to main pancreatic duct) leads to:", "Conservative Mx", ["Distal pancreatectomy", ["Begger's procedure"] , "Whipple's"])
q(423, S7, "In the book's flowchart, the NO arm checks for injury in the body & tail of pancreas, treated by:", "Distal pancreatectomy", ["Begger's procedure", ["Conservative Mx"] , "Whipple's"])
q(423, S7, "Injury in the head & neck of pancreas in the book's flowchart is treated by:", "Begger's procedure (duodenal preserving pancreatic head resection)", ["Distal pancreatectomy", ["Conservative Mx"] , "Total pancreatectomy"])

# ------------------------------------------------------------------ p424
S8 = "Colon & Rectal Injury, ETC/DCS and Abdominal Compartment Syndrome Etiology"
q(424, S8, "Colon & rectal injury shows peritonitis if:", "Perforation (+)", ["No perforation", ["Only contusion"] , "Only hematoma"])
q(424, S8, "Emergency laparotomy for colon/rectal injury creates a:", "Diverting stoma/colostomy", ["Primary anastomosis always", ["Hartman always"] , "Tube colostomy only"])
q(424, S8, "The other operation listed for colon/rectal injury is the:", "Hartman procedure", ["Whipple's", ["Miles procedure"] , "Deloyers"])
q(424, S8, "ETC stands for:", "Early Total care", ["Emergency Total care", ["Early Trauma care"] , "Extended Total care"])
q(424, S8, "ETC aims at definitive mx of injuries within:", "36 hours", ["24 hours", ["48 hours"] , "72 hours"])
q(424, S8, "ETC can shift to DCS if:", "Patient deteriorates", ["Patient improves", ["Surgeon prefers"] , "ICU full"])
q(424, S8, "DCS stands for:", "Damage control Sx", ["Definitive control Sx", ["Delayed control Sx"] , "Direct control Sx"])
q(424, S8, "DCS means simultaneous resuscitation with early rapid life & limb saving Sx, with definitive Sx:", "Deferred till patient is stable", ["Done immediately", ["Abandoned"] , "Done in ICU"])
q(424, S8, "The DCS terrible triad includes hypothermia, acidosis and:", "Coagulopathy", ["Hypoxemia", ["Hypercapnia"] , "Anemia"])
q(424, S8, "ETC requires stable haemodynamics, no hypoxaemia/hypercapnia, no acidosis and:", "(N) coagulation", ["Coagulopathy", ["Thrombocytopenia"] , "DIC"])
q(424, S8, "DCS phase 0 is:", "Identification of patient for DCS in emergency room", ["Emergency laparotomy", ["Correction of physiology"] , "Re-laparotomy"])
q(424, S8, "Between phase 0 and phase 1 the patient is:", "Resuscitated", ["Operated", ["Scanned"] , "Warmed only"])
q(424, S8, "DCS phase 1 is:", "Emergency laparotomy", ["Re-laparotomy", ["ICU physiology"] , "Closure"])
q(424, S8, "The aims of DCS phase 1 laparotomy are to stop bleeding and:", "Prevent contamination", ["Correct anatomy", ["Close abdomen"] , "Resect bowel"])
q(424, S8, "After phase 1 the abdomen gets a:", "Temporary abdominal closure", ["Definitive closure", ["Mesh graft"] , "Stoma"])
q(424, S8, "DCS phase 2 corrects physiology (lethal triad of trauma) in the:", "ICU", ["OT", ["ER"] , "Ward"])
q(424, S8, "Phase 3 re-laparotomy follows phase 2 after:", "48-72 hrs", ["24 hrs", ["1 week"] , "12 hrs"])
q(424, S8, "The aims of DCS phase 3 re-laparotomy are to correct anatomy and:", "Close abdomen", ["Resect more bowel", ["Place drains only"] , "Re-pack"])
q(424, S8, "The DCS phases map to stages 1, 2, 3 and:", "Stage 4, 5", ["Stage 4 only", ["Stage 6"] , "Stage 5 only"])
q(424, S8, "An etiology of abdominal compartment syndrome is massive burns of:", ">15-20% of BSA", [">5-10% of BSA", [">30-40% of BSA"] , ">50% of BSA"])
q(424, S8, "Another etiology of abdominal compartment syndrome is:", "Massive ascites", ["Bowel obstruction only", ["Pneumoperitoneum"] , "Ileus only"])
q(424, S8, "The third etiology of abdominal compartment syndrome listed is:", "Bowel obstruction", ["Massive ascites", ["Burns"] , "Pregnancy"])

# ------------------------------------------------------------------ p425
S9 = "ACS: Pressure Measurement, Organ Effects and Retroperitoneal Zones"
q(425, S9, "Intra-abdominal pressure is measured after draining urine via a:", "Foley's catheter", ["Suprapubic catheter", ["Nephrostomy"] , "Ureteric stent"])
q(425, S9, "For pressure measurement, the volume of saline injected into the bladder via Foley's is:", "50cc", ["20cc", ["100cc"] , "500cc"])
q(425, S9, "The pressure measured to indicate abdominal pressure is the:", "Bladder pressure", ["Gastric pressure", ["IVC pressure"] , "Rectal pressure"])
q(425, S9, "Intra abdominal HTN (IAH) is ↑ of IAP above:", ">12 mmHg", [">8 mmHg", [">20 mmHg"] , ">25 mmHg"])
q(425, S9, "Abdominal compartment syndrome (ACS) is IAP of:", "≥20 mmHg with new organ dysfunction", [">12 mmHg", [">15 mmHg alone"] , "≥30 mmHg"])
q(425, S9, "Renal effects of ACS are ↓ GFR and:", "↓ urine output", ["↑ urine output", ["Hematuria"] , "Proteinuria"])
q(425, S9, "CVS effects of ACS begin with ↓ venous return causing:", "↓ SBP, ↓ cardiac output", ["↑ SBP", ["↑ cardiac output"] , "↑ HR only"])
q(425, S9, "Respiratory effects of ACS include ↓ inspiratory volumes & capacities and:", "↑ pressure in thoracic cavity", ["↓ thoracic pressure", ["Bronchospasm"] , "Effusion"])
q(425, S9, "Visceral perfusion in ACS is:", "↓", ["↑", ["Normal"] , "Redistributed"])
q(425, S9, "The intracranial effect of ACS is:", "↑ intracranial tension", ["↓ intracranial tension", ["No effect"] , "Seizures only"])
q(425, S9, "Retroperitoneal zone 1 contains IVC, aorta and:", "Pancreas", ["Kidneys", ["Ureters"] , "Pelvic structures"])
q(425, S9, "The retroperitoneal zone with max mortality is zone:", "1", ["2", ["3"] , "4"])
q(425, S9, "The IOC in an unstable patient with zone 1 retroperitoneal trauma is:", "Angiogram", ["CECT", ["Single shot IV urogram"] , "FAST"])
q(425, S9, "Retroperitoneal zone 2 contains kidney, ureter and:", "Renal vessels", ["Pancreas", ["Aorta"] , "Pelvic vessels"])
q(425, S9, "The IOC for zone 2 retroperitoneal trauma in a stable patient is:", "CECT", ["Angiogram", ["Single shot IV urogram"] , "X-ray"])
q(425, S9, "The IOC for zone 2 retroperitoneal trauma in an unstable patient is:", "Single shot IV urogram", ["CECT", ["Angiogram"] , "MRI"])
q(425, S9, "Retroperitoneal zone 3 contains:", "Pelvic structures", ["Kidneys", ["Pancreas"] , "Aorta"])
q(425, S9, "The m/c injured retroperitoneal zone is zone:", "3", ["1", ["2"] , "Equal"])

# ------------------------------------------------------------------ units
def first_page(title):
    return next(x["page"] for x in Q if x["sec"] == title)

UNIT_DEFS = [
    (S1, "The spleen leads overall and in blunt trauma (spleen > liver) and in children (spleen > kidney), while penetrating trauma favours liver > small intestine and gunshots small intestine > liver; seatbelt syndrome hits the mesentery and deceleration the duodeno-jejunal flexure. Stable blunt patients get FAST first and CECT as IOC, unstable ones FAST as both, and surgery means midline laparotomy. FAST (focused assessment sonogram in trauma) is an ER tool whose four views — epigastrium, RUQ (perihepatic), LUQ (perisplenic) and suprapubic (pelvis) — become eFAST when the two anterior chest windows (5, 6) add pneumothorax and the subxiphoid pericardial window catches tamponade; free fluid reads as a hypoechoic collection."),
    (S2, "FAST misses free blood under 100 ml, cannot see hollow viscus or penetrating injury, cannot assess the retroperitoneum through bowel gas, may need repeating and is operator dependent. The blunt algorithm sends peritonitis or instability with positive FAST straight to exploratory laparotomy, stable patients to CT, hollow-organ yes/indeterminate to laparotomy or diagnostic laparoscopy, and solid-organ injuries with pseudoaneurysm or arterial blush to interventional radiology while the rest are managed nonoperatively. In penetrating trauma an impaled object is never removed in the ER; wounds superficial to peritoneum get local examination plus CECT, while peritoneal breach with peritonitis, hanging omentum, bile staining or instability goes to midline laparotomy without investigations."),
    (S3, "DPL rescues settings without FAST: decompress stomach and bladder, needle just below the umbilicus, >10 cc gross blood = positive, otherwise instil 1 L Ringer lactate and call it positive with >1 lakh RBC/cumm, >500 WBC/cumm, amylase >175 IU/L or fecal content, then laparotomy. Splenic trauma is suspected with left 9-11th rib fractures, left lower chest wall bruising and a positive Kehr sign (left leg raised, blood under the left diaphragm referring pain to the shoulder tip). Grading runs I (subcapsular <10%, laceration <1 cm, capsular tear), II (10-50%, intraparenchymal <5 cm, laceration 1-3 cm), III (>50%, ruptured or >5 cm hematoma, laceration >3 cm), IV (vascular injury or segmental/hilar laceration with >25% devascularisation) to V (shattered spleen with vascular injury)."),
    (S4, "Delayed CT separates splenic pseudoaneurysm/AV fistula (falling arterial blush) from active bleeding (rising blush). Grades I-II, usually stable with CECT as IOC, are conserved with vitals, hematocrit and serial 24-hour CECT, escalating to angioembolization for rising grade or blush and to laparotomy — preferably splenorrhaphy — if conservation fails, vitals turn or peritonitis appears; stable grade III mirrors I-II while unstable III and unstable IV-V (FAST as IOC, positive → splenectomy) follow the surgical route. Splenectomy complications run hemorrhage, pancreatic tail injury with amylase-rich fistula, a two-week three-line cytosis whose WBC rise mimics infection and platelets above 10 lakh/cumm risk thrombosis needing prophylactic aspirin, and permanent smear stigmata — basophilic stippling, reticulocytes, Howell-Jolly bodies and hypersegmented WBCs."),
    (S5, "Left lower lobe atelectasis/pneumonia from poor left chest expansion is the commonest post-splenectomy complication, ahead of OPSI — overwhelming post-splenectomy infection by encapsulated pneumococcus (m/c), meningococcus and H. influenzae, hitting children more than adults within the first two years and killing haematological patients most. Vaccines repeat every 5 years (pneumococcal/meningococcal), 10 years (H. influenzae) and yearly (influenzae), given two weeks before elective or post-op day 1-2 after emergency splenectomy, with poorer titres post-surgery. Liver trauma grades I-V track subcapsular and intraparenchymal haematoma size, laceration depth, contained versus peritoneal-breaching vascular injury and juxtahepatic venous disruption, advancing one grade for multiple injuries up to III."),
    (S6, "Liver trauma is resuscitated first: unstable grade III-V goes to surgery while stable grade I-III is conserved with monitoring, hematocrit and serial CECT, discharging those who stay stable and treating hemorrhage, biliary, vascular and septic complications, with surgery for late instability. Pringle's manoeuvre clamps the hepatic pedicle (CBD, portal vein, hepatic artery) at the foramen of Winslow for 15-20 minutes: bleeding that falls implicates portal vein/hepatic artery, bleeding that continues the hepatic veins, giving temporary control and localising the source. Packing cuts both triangular ligaments, frees the liver from the diaphragm and packs mops above and below for 24-48 hours for a tamponading effect."),
    (S7, "Liver trauma complications proceed bleeding, bile leak (ligate minor radicles, repair CBD/major ducts over a T-tube), liver abscess, CBD strictures, AV malformations and portal vein injury repaired with prolene. Mesenteric longitudinal tears cut one branch without vascular loss and are repaired, while transverse tears cut all vessels with devascularisation needing resection and anastomosis. Duodenal haematoma, the mildest injury, rests the bowel NPO; perforation shows peritonitis and subdiaphragmatic gas and gets an omental patch. Pancreatic injury, secondary to blunt or penetrating trauma, prognosticates on main duct injury; the book's flowchart routes its YES arm to conservative management and its NO arm to site-based surgery — distal pancreatectomy for body/tail and Begger's duodenum-preserving head resection for head/neck."),
    (S8, "Colon and rectal injuries declare themselves by peritonitis when perforated and are handled by emergency laparotomy creating a diverting stoma/colostomy or by the Hartman procedure. Early total care definitively fixes injuries within 36 hours but converts to damage control surgery — simultaneous resuscitation with rapid life- and limb-saving surgery, definitive repair deferred — when the patient deteriorates; DCS battles the terrible triad of hypothermia, acidosis and coagulopathy while ETC demands stable haemodynamics, no hypoxaemia/hypercapnia, no acidosis and normal coagulation. DCS runs phase 0 identification in the ER, resuscitation, phase 1 laparotomy to stop bleeding and prevent contamination with temporary closure, phase 2 ICU correction of physiology and phase 3 re-laparotomy at 48-72 hours to correct anatomy and close (stages 1 to 4, 5). Massive burns >15-20% BSA, massive ascites and bowel obstruction cause abdominal compartment syndrome."),
    (S9, "Intra-abdominal pressure is read off the bladder after Foley drainage and 50 cc saline instillation; intra-abdominal hypertension is IAP >12 mmHg and abdominal compartment syndrome ≥20 mmHg with new organ dysfunction. ACS lowers GFR and urine output, cuts venous return with falling SBP and cardiac output, shrinks inspiratory volumes while raising thoracic pressure, drops visceral perfusion and raises intracranial tension. Retroperitoneal zone 1 (IVC, aorta, pancreas) carries maximal mortality and needs angiography when unstable; zone 2 (kidney, ureter, renal vessels) uses CECT if stable and a single-shot IV urogram if unstable; zone 3 (pelvic structures) is the most commonly injured zone."),
]

UNITS = []
for i, (title, guide) in enumerate(UNIT_DEFS, 1):
    UNITS.append({
        "id": f"SURG-U55-{i}",
        "ch": 55,
        "n": i,
        "title": title,
        "sec": f"{title} · p{first_page(title)}",
        "qs": [x["id"] for x in Q if x["sec"] == title],
        "guide": guide,
    })

covered = [x for u in UNITS for x in u["qs"]]
assert covered == [x["id"] for x in Q]
assert len(set(covered)) == len(covered)
with open("data/ch55.json", "w", encoding="utf-8") as f:
    json.dump({"questions": Q, "units": UNITS}, f, ensure_ascii=False, indent=1)
print(f"ch55: {len(Q)} questions, {len(UNITS)} units")
