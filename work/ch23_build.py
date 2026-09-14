#!/usr/bin/env python3
"""Build data/ch23.json for PULSE Surgery ch23 (Stomach : Part 2, book p157-160)."""
import json

Q = []
def q(page, sec, text, opts, ans, exp):
    Q.append({"id": f"SURG-C23-{len(Q)+1:03d}", "sec": sec, "page": page,
              "q": text, "opts": opts, "ans": ans, "exp": exp})

# ---------------- p157 · BILLROTH I & II ----------------
S1 = "Gastrectomy Reconstructions: Billroth I & II"
q(157, S1, "Billroth I gastrectomy is a:",
  ["Distal gastrectomy with an end to end gastroduodenal anastomosis",
   "Subtotal gastrectomy with an end to side gastrojejunal anastomosis",
   "Total gastrectomy with a Roux loop",
   "Proximal gastrectomy with esophagogastrostomy"], 0,
  "Billroth I gastrectomy: distal gastrectomy with end to end gastro-duodenal anastomosis. (Book p157)")
q(157, S1, "Billroth II (Polya) reconstruction is performed after:",
  ["Subtotal or partial gastrectomy", "Total gastrectomy", "Proximal gastrectomy",
   "Sleeve gastrectomy"], 0,
  "Billroth II gastrectomy / Polya reconstruction: subtotal/partial gastrectomy. (Book p157)")
q(157, S1, "In a Billroth II (Polya) reconstruction the duodenum is:",
  ["Closed as a duodenal stump", "Anastomosed end to end to the stomach",
   "Anastomosed to the jejunum", "Left open as a fistula"], 0,
  "Billroth II: close the duodenal stump and perform an end to side gastro-jejunal anastomosis. (Book p157)")
q(157, S1, "The anastomosis created in a Billroth II (Polya) reconstruction is:",
  ["End to side gastrojejunostomy", "End to end gastroduodenostomy",
   "Side to side jejunojejunostomy", "End to side duodenojejunostomy"], 0,
  "Billroth II: end to side gastro-jejunal anastomosis. (Book p157)")
q(157, S1, "In a Billroth II reconstruction, bile and pancreatic juice pass through the:",
  ["Afferent loop", "Efferent loop", "Roux limb", "Duodenal stump"], 0,
  "Billroth II: afferent loop carries bile and pancreatic juice; efferent loop carries food. (Book p157)")
q(157, S1, "The limb that carries food in a Billroth II reconstruction is the:",
  ["Efferent loop", "Afferent loop", "Bilio-pancreatic limb", "Roux limb"], 0,
  "Food passes through the efferent loop. (Book p157)")

# ---------------- p157-158 · ROUX-EN-Y ----------------
S2 = "Roux-en-Y Reconstruction"
q(157, S2, "In a Roux-en-Y gastrojejunostomy the duodenal stump is:",
  ["Closed", "Anastomosed to the stomach", "Used as a feeding tube", "Left open"], 0,
  "Roux en Y gastrojejunostomy / gastric bypass: closed duodenal stump, Roux limb and BP limb. (Book p157)")
q(158, S2, "The length of the Roux limb used in a Roux-en-Y reconstruction is:",
  ["50 cm", "10 cm", "100 cm", "5 cm"], 0,
  "Roux limb: 50 cm of jejunum. (Book p158)")
q(158, S2, "The limb carrying bile and pancreatic secretions in a Roux-en-Y reconstruction is the:",
  ["Bilio-pancreatic (BP) limb", "Roux limb", "Afferent loop", "Efferent loop"], 0,
  "Roux-en-Y: Roux limb (50 cm) with a bilio-pancreatic (BP) limb. (Book p158)")
q(158, S2, "A retrocolic Roux limb is placed:",
  ["Behind the colon, through the transverse mesocolon", "In front of the colon",
   "Through the gastrocolic omentum", "Behind the stomach only"], 0,
  "Retrocolic: behind the colon, through the transverse mesocolon. (Book p158)")
q(158, S2, "An antecolic Roux limb is placed:",
  ["In front of the colon", "Behind the colon", "Through the transverse mesocolon",
   "Behind the stomach"], 0,
  "Antecolic: in front of the colon. (Book p158)")

# ---------------- p158 · INTERNAL HERNIAS ----------------
S3 = "Internal Hernias after Reconstruction"
q(158, S3, "Petersen's hernia after a Roux-en-Y reconstruction is bowel herniating:",
  ["Behind the Roux limb", "Through the transverse mesocolon window",
   "Through the omental foramen", "Through the diaphragm"], 0,
  "Petersen hernia: bowel herniation behind the Roux limb. (Book p158)")
q(158, S3, "Stemmer's hernia after gastric reconstruction is bowel herniating:",
  ["Through the transverse mesocolon window", "Behind the Roux limb",
   "Through the omental foramen", "Through the ileocaecal mesentery"], 0,
  "Stemmer's hernia: bowel herniation through the transverse mesocolon window. (Book p158)")
q(160, S3, "Internal hernias after gastric reconstruction include:",
  ["Petersen's and Stemmer's hernias", "Only inguinal hernias",
   "Only incisional hernias", "Spigelian and femoral hernias"], 0,
  "Internal hernias: Stemmer's hernia (through transverse mesocolon) and Petersen's hernia (behind Roux limb). (Book p160)")

# ---------------- p158 · VAGOTOMY: ANATOMY & INDICATIONS ----------------
S4 = "Vagotomy: Branches & Indications"
q(158, S4, "Vagotomy is:",
  ["Not routinely done, having been replaced by proton pump inhibitors",
   "The first line treatment for all peptic ulcers",
   "Done for every gastric cancer", "Done only in children"], 0,
  "Cutting the vagus is not routinely done - it has been replaced by PPIs. (Book p158)")
q(158, S4, "Indications for vagotomy include:",
  ["Duodenal ulcers and type 2 and 3 gastric ulcers", "Type 1 gastric ulcers only",
   "Barrett's esophagus", "Gastric carcinoma"], 0,
  "Indications: duodenal ulcers; type 2 and 3 gastric ulcers. (Book p158)")
q(158, S4, "The anterior nerve of Latarjet terminates as the:",
  ["Crow's foot supplying the antrum", "Criminal nerve of Grassi",
   "Coeliac branch", "Hepatic branch"], 0,
  "Anterior nerve of Latarjet continues as the crow's foot, which supplies the antrum. (Book p158)")
q(158, S4, "Cutting the motor branch to the gallbladder during vagotomy leads to:",
  ["Gallbladder stasis and stone formation", "Immediate gastric emptying",
   "Biliary peritonitis", "Pancreatitis"], 0,
  "Posterior trunk gives a motor branch to the gallbladder; if cut it can lead to GB stasis and stone formation. (Book p158)")
q(158, S4, "Cutting the motor branch to the pylorus results in:",
  ["Impaired gastric emptying requiring a drainage procedure",
   "Immediate dumping syndrome", "Gastric necrosis", "Bile reflux gastritis"], 0,
  "Motor branch to pylorus: if cut, impaired gastric emptying - a drainage procedure is required. (Book p158)")
q(158, S4, "The nerve responsible for ulcer recurrence after vagotomy is the:",
  ["Criminal nerve of Grassi", "Anterior nerve of Latarjet", "Crow's foot",
   "Coeliac branch"], 0,
  "Criminal nerve of Grassi: responsible for ulcer recurrence after vagotomy. (Book p158)")
q(158, S4, "Drainage procedures performed along with vagotomy are:",
  ["Gastrojejunostomy and pyloroplasty", "Gastrostomy and jejunostomy",
   "Antrectomy and Billroth I", "Fundectomy"], 0,
  "Drainage procedures: gastrojejunostomy and pyloroplasty (pyloroplasty renders the pylorus incompetent). (Book p158)")

# ---------------- p159 · TYPES OF VAGOTOMY ----------------
S5 = "Types of Vagotomy"
q(159, S5, "In truncal vagotomy, the distal esophagus is skeletonised for:",
  ["6-8 cm", "1-2 cm", "15-20 cm", "The whole thoracic esophagus"], 0,
  "Truncal vagotomy: distal 6-8 cm of the esophagus is skeletonised. (Book p159)")
q(159, S5, "Highly selective vagotomy denervates:",
  ["Branches to the body and fundus while sparing the antrum and pylorus",
   "The whole stomach including the pylorus",
   "Only the pylorus", "Only the coeliac branch"], 0,
  "HSV: branches to the body and fundus are cut; denervation is stopped 7 cm proximal to the pylorus, sparing the pylorus and antrum. (Book p159)")
q(159, S5, "In highly selective vagotomy, denervation is stopped how far proximal to the pylorus?",
  ["7 cm", "1 cm", "15 cm", "20 cm"], 0,
  "Denervation is stopped 7 cm proximal to the pylorus. (Book p159)")
q(159, S5, "The nerve spared in a highly selective vagotomy is the:",
  ["Anterior nerve of Latarjet", "Criminal nerve of Grassi",
   "Posterior trunk of the vagus", "Coeliac branch"], 0,
  "HSV: anterior nerve of Latarjet is spared. (Book p159)")
q(159, S5, "Compared with other vagotomies, highly selective vagotomy has:",
  ["The fewest complications but a higher ulcer recurrence rate",
   "The most complications and the lowest recurrence",
   "The greatest acid reduction", "No effect on acid"], 0,
  "HSV: fewer complications, but ulcer recurrence is higher; acid reduction is less. (Book p159)")
q(159, S5, "The lowest ulcer recurrence rate is achieved with:",
  ["Truncal vagotomy with antrectomy", "Highly selective vagotomy",
   "Truncal vagotomy with gastrojejunostomy", "Pyloroplasty alone"], 0,
  "Truncal vagotomy with antrectomy gives the greatest acid reduction and the least recurrence. (Book p159)")
q(159, S5, "Truncal vagotomy with antrectomy is indicated for:",
  ["Recurrent ulcers", "Asymptomatic gastritis", "Barrett's esophagus",
   "Gastric outlet obstruction due to cancer"], 0,
  "Indications: truncal vagotomy with antrectomy is used for recurrent ulcers. (Book p159)")

# ---------------- p159 · NUTRITIONAL COMPLICATIONS ----------------
S6 = "Nutritional Complications after Gastric Surgery"
q(159, S6, "The m/c nutritional complication after gastric reconstruction is:",
  ["Iron deficiency anaemia", "Vitamin B12 deficiency", "Calcium deficiency",
   "Vitamin K deficiency"], 0,
  "Nutritional complications: iron deficiency anaemia is the m/c (microcytic hypochromic anaemia). (Book p159)")
q(159, S6, "The peripheral smear in post-gastrectomy iron deficiency anaemia shows:",
  ["Microcytic hypochromic anaemia", "Macrocytic anaemia", "Sickle cells",
   "Spherocytes"], 0,
  "Iron deficiency anaemia: peripheral smear shows microcytic hypochromic anaemia. (Book p159)")
q(159, S6, "Vitamin B12 deficiency after gastric surgery presents with:",
  ["Easy fatigability, neuropathy and megaloblastic anaemia",
   "Bleeding gums and scurvy", "Night blindness", "Osteomalacia alone"], 0,
  "Vitamin B12 deficiency: easy fatigability, neuropathy, megaloblastic anaemia. (Book p159)")
q(159, S6, "Nutritional complications after gastric reconstruction include all of the following EXCEPT:",
  ["Vitamin K deficiency", "Iron deficiency anaemia", "Vitamin B12 deficiency",
   "Calcium deficiency"], 0,
  "Nutritional complications: iron deficiency anaemia, vitamin B12 deficiency, calcium deficiency. (Book p159)")

# ---------------- p159 · SURGICAL COMPLICATIONS ----------------
S7 = "Surgical Complications of Reconstruction"
q(159, S7, "Duodenal stump blowout is seen in:",
  ["Polya and Roux-en-Y reconstructions", "Billroth I reconstruction",
   "Highly selective vagotomy", "Fundoplication"], 0,
  "Duodenal stump blowout: seen in Polya and Roux en Y reconstruction. (Book p159)")
q(159, S7, "Duodenal stump blowout typically presents on post-operative day:",
  ["4", "1", "10", "30"], 0,
  "Duodenal stump blowout presents on post-operative day 4. (Book p159)")
q(159, S7, "The features of duodenal stump blowout are:",
  ["Abdominal pain, fever and peritonitis", "Painless jaundice",
   "Upper GI bleed only", "Asymptomatic drainage"], 0,
  "Duodenal stump blowout: abdominal pain, fever, peritonitis. (Book p159)")
q(159, S7, "Haemorrhage after gastric reconstruction occurs from:",
  ["The anastomotic site", "The spleen", "The liver", "The transverse colon"], 0,
  "Hemorrhage: from the anastomotic site. (Book p159)")
q(159, S7, "Marginal (anastomotic) peptic ulcers after gastric surgery occur because:",
  ["Acid from the stomach passes directly into the jejunum",
   "Bile refluxes into the stomach", "The vagus is intact",
   "Gastrin levels fall"], 0,
  "Peptic ulcers: acid from the stomach goes directly into the jejunum causing ulcers. (Book p159)")
q(159, S7, "Afferent loop syndrome is a complication of:",
  ["Polya (Billroth II) reconstruction", "Billroth I reconstruction",
   "Highly selective vagotomy", "Nissen's fundoplication"], 0,
  "Afferent loop syndrome: seen in Polya reconstruction. (Book p159)")
q(159, S7, "Afferent loop syndrome is caused by:",
  ["Twisting of the afferent loop causing obstruction and perforation",
   "Stricture of the efferent loop", "Internal herniation behind the Roux limb",
   "Bile reflux gastritis"], 0,
  "Afferent loop syndrome: twisting of the afferent loop leads to obstruction and perforation. (Book p159)")

# ---------------- p160 · DUMPING SYNDROME ----------------
S8 = "Dumping Syndrome"
q(160, S8, "Dumping syndrome is m/c after:",
  ["Polya (Billroth II) reconstruction, more than Roux-en-Y", "Billroth I reconstruction",
   "Highly selective vagotomy", "Fundoplication"], 0,
  "Dumping syndrome: m/c with Polya > Roux-en-Y. (Book p160)")
q(160, S8, "Early dumping is caused by:",
  ["Rapid influx of fluid into the bowel due to hyperosmolar contents",
   "Excess insulin release after delayed sugar absorption",
   "Bile reflux into the stomach", "Stricture of the anastomosis"], 0,
  "Early dumping: rapid influx of fluid due to hyperosmolar contents in the bowel. (Book p160)")
q(160, S8, "Features of early dumping include all of the following EXCEPT:",
  ["Rebound hypoglycaemia", "Nausea, vomiting and bloating", "Headache and sweating",
   "Tachycardia"], 0,
  "Early dumping: nausea, vomiting, bloating, headache, sweating, tachycardia; starts 10-15 mins after food and worsens with food. (Book p160)")
q(160, S8, "Late dumping is due to:",
  ["Excess insulin release causing rebound hypoglycaemia",
   "Rapid fluid shifts into the bowel", "Bile reflux gastritis",
   "Afferent loop obstruction"], 0,
  "Late dumping: reduced absorption of sugar but complete insulin release - excess insulin causes rebound hypoglycemia. (Book p160)")
q(160, S8, "Late dumping occurs how long after a meal?",
  ["30-40 minutes", "10-15 minutes", "Immediately", "6-8 hours"], 0,
  "Late dumping: onset 30-40 mins after food, relieved by rest and improves with food. (Book p160)")
q(160, S8, "Early dumping begins how long after a meal?",
  ["10-15 minutes", "30-40 minutes", "2 hours", "6 hours"], 0,
  "Early dumping: onset 10-15 mins after food. (Book p160)")
q(160, S8, "Dietary management of dumping syndrome includes all of the following EXCEPT:",
  ["Large meals with plenty of liquid", "Avoiding sugar rich liquids",
   "Small frequent meals", "A high fat and high protein diet"], 0,
  "Dietary recommendations: avoid large meals, avoid liquids with meals, avoid sugar rich liquids, small frequent meals, high fat and protein diet. (Book p160)")
q(160, S8, "Persistent dumping despite an anti-dumping diet is treated with:",
  ["Octreotide", "Insulin", "Proton pump inhibitors", "Total parenteral nutrition"], 0,
  "Persistent dumping in spite of an anti-dumping diet: octreotide. (Book p160)")
q(160, S8, "If dumping syndrome persists despite dietary measures and octreotide, the next step is:",
  ["Conversion to a Roux-en-Y reconstruction", "Total gastrectomy",
   "Completion antrectomy", "Vagotomy"], 0,
  "If medical measures fail: convert to Roux-en-Y. (Book p160)")

# ---------------- units ----------------
def sec_ids(*labels):
    return [x["id"] for x in Q if x["sec"] in labels]
def first_page(label):
    for x in Q:
        if x["sec"] == label:
            return x["page"]
    return 0

UNIT_DEFS = [
    (S1, "Billroth I is the physiological option - distal gastrectomy with an end-to-end gastroduodenal join. Billroth II (Polya) closes the duodenal stump and joins the stomach end-to-side to jejunum, creating an afferent limb that carries bile and pancreatic juice and an efferent limb that carries food."),
    (S2, "Roux-en-Y also closes the duodenal stump but separates the streams: a 50 cm Roux limb carries food, a bilio-pancreatic limb carries bile and pancreatic juice. The Roux limb can be routed retrocolic (behind the colon, through the transverse mesocolon) or antecolic (in front of the colon)."),
    (S3, "Two internal hernias to name after reconstruction: Petersen's, where bowel slips behind the Roux limb, and Stemmer's, where it slips through the window in the transverse mesocolon."),
    (S4, "Vagotomy is rarely needed now that PPIs exist, but when it is done it is for duodenal ulcers or type 2 and 3 gastric ulcers. Know the wiring: the anterior trunk continues as the anterior nerve of Latarjet and its crow's foot to the antrum with a motor branch to the pylorus (cut it and the stomach will not empty, so add a drainage procedure); the posterior trunk gives a coeliac branch, a gallbladder branch (cut it and stones form) and the posterior nerve of Latarjet; the criminal nerve of Grassi is the one left behind that brings the ulcer back."),
    (S5, "Truncal vagotomy skeletonises the distal 6-8 cm of esophagus and needs drainage (gastrojejunostomy or pyloroplasty). Highly selective vagotomy cuts only the branches to the body and fundus, stops 7 cm short of the pylorus and spares the nerve of Latarjet - so no drainage, fewer complications, but more recurrences; truncal vagotomy with antrectomy reduces acid most and recurs least."),
    (S6, "Expect iron deficiency (microcytic hypochromic, and the commonest), then B12 deficiency with neuropathy and megaloblastic anaemia, then calcium deficiency."),
    (S7, "Duodenal stump blowout belongs to Polya and Roux-en-Y and strikes around day 4 with pain, fever and peritonitis; bleeding comes from the anastomosis; acid hitting jejunum directly causes marginal ulcers; and in a Polya the afferent loop can twist, obstruct and perforate."),
    (S8, "Dumping is commonest after Polya. Early dumping (10-15 minutes) is the osmotic fluid shift - nausea, bloating, sweating, tachycardia, worse with food. Late dumping (30-40 minutes) is excess insulin after rapid sugar absorption - rebound hypoglycaemia that food actually relieves. Treat with small frequent low-sugar, high-fat and high-protein meals, then octreotide, then conversion to Roux-en-Y."),
]

UNITS = []
for i, (title, guide) in enumerate(UNIT_DEFS, 1):
    UNITS.append({"id": f"SURG-U23-{i}", "ch": 23, "n": i, "title": title,
                  "sec": f"{title} · p{first_page(title)}",
                  "qs": sec_ids(title), "guide": guide})

covered = [i for u in UNITS for i in u["qs"]]
assert covered == [x["id"] for x in Q], "units must cover questions in order"

data = {"questions": Q, "units": UNITS}
with open("data/ch23.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
print(f"ch23: {len(Q)} questions, {len(UNITS)} units")
