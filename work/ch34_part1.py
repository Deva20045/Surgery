#!/usr/bin/env python3
"""Build data/ch34.json — ch34 Liver: Part 1 (Marrow Surgery Ed 8, book p245-252)."""
import json

Q = []


def q(page, sec, text, opts, ans, exp):
    Q.append({
        "id": f"SURG-C34-{len(Q)+1:03d}",
        "sec": sec,
        "page": page,
        "q": text,
        "opts": opts,
        "ans": ans,
        "exp": exp,
    })


# ------------------------------------------------------------------ p245
S1 = "Functional Anatomy of the Liver"
q(245, S1, "The functional anatomy of the liver was described by:",
  ["Couinaud", "Brisbane", "Calot", "Ganz"], 0,
  "Functional anatomy of the liver is described by Couinaud. (Book p245)")
q(245, S1, "The liver is divided into how many functional segments?",
  ["8", "4", "5", "6"], 0,
  "The liver is divided into 8 functional segments. (Book p245)")
q(245, S1, "The bare area of the liver is most commonly involved in:",
  ["Amoebic liver abscess", "Pyogenic liver abscess", "Hydatid cyst", "Hepatocellular carcinoma"], 0,
  "The bare area of the liver is the m/c site involved in amoebic liver abscess. (Book p245)")
q(245, S1, "The gallbladder fossa is formed by segments:",
  ["4B and 5", "2 and 3", "6 and 7", "1 and 8"], 0,
  "GB fossa: segments 4B and 5. (Book p245)")
q(245, S1, "Because the gallbladder fossa is formed by segments 4B and 5, gallbladder cancer is resected by:",
  ["Radical cholecystectomy including those segments",
   "Simple cholecystectomy alone",
   "Left hepatectomy",
   "Right trisectorectomy"], 0,
  "The page notes the GB fossa segments can be involved in GB cancer and are therefore resected in a radical cholecystectomy. (Book p245)")
q(245, S1, "Functional classification of the liver is based on:",
  ["The portal vein more than the hepatic vein",
   "The hepatic vein more than the portal vein",
   "The bile ducts alone",
   "The hepatic artery alone"], 0,
  "Functional classification is based on the portal vein rather than the hepatic vein. (Book p245)")
q(245, S1, "How many sectors does the liver have?",
  ["4", "2", "3", "8"], 0,
  "There are 4 sectors: right posterior, right anterior, left medial and left lateral. (Book p245)")
q(245, S1, "Which of the following is NOT one of the four sectors of the liver?",
  ["Right medial", "Right posterior", "Right anterior", "Left lateral"], 0,
  "The four sectors are right posterior, right anterior, left medial and left lateral. (Book p245)")
q(245, S1, "The three major fissures of the liver are related to the:",
  ["Hepatic veins — right, left and middle", "Portal veins — right, left and main",
   "Bile ducts", "Sectoral branches of the hepatic artery"], 0,
  "Major fissures: 3 fissures related to the right hepatic vein, left hepatic vein and middle hepatic vein. (Book p245)")
q(245, S1, "The three minor fissures of the liver are related to all of the following EXCEPT the:",
  ["Middle hepatic vein", "Right portal vein", "Left portal vein", "Fissure of Ganz"], 0,
  "Minor fissures: 3 fissures — right portal vein, left portal vein and the fissure of Ganz. (Book p245)")

S2 = "Segment I: The Caudate Lobe"
q(245, S2, "Segment I of the liver is the:",
  ["Caudate lobe", "Quadrate lobe", "Left lateral section", "Right posterior section"], 0,
  "Segment I is the caudate lobe. (Book p245)")
q(245, S2, "The caudate lobe lies:",
  ["Posteriorly, to the left of the IVC", "Anteriorly, to the right of the IVC",
   "Inferior to the gallbladder fossa", "Within the left lobe above the falciform ligament"], 0,
  "The caudate lobe lies posteriorly, to the left of the IVC. (Book p245)")
q(245, S2, "The caudate lobe is called an independent segment because it drains bile into:",
  ["Both the left and the right lobes", "Only the left duct system",
   "Only the right duct system", "The cystic duct"], 0,
  "Segment I drains bile into both left and right lobe ducts — one reason it is called an independent segment. (Book p245)")
q(245, S2, "The blood supply of the caudate lobe comes from:",
  ["Both the left and the right lobes", "Only the right portal vein",
   "Only the left portal vein", "The hepatic artery alone"], 0,
  "Segment I receives blood from both the left and the right lobes. (Book p245)")
q(245, S2, "The caudate lobe drains directly into the:",
  ["IVC", "Portal vein", "Hepatic vein confluence via the middle hepatic vein", "Azygos vein"], 0,
  "It has direct venous drainage into the IVC. (Book p245)")
q(245, S2, "Segment I undergoes compensatory hypertrophy in:",
  ["Budd-Chiari syndrome", "Portal vein thrombosis", "Cirrhosis", "Cardiac failure"], 0,
  "Because it drains directly into the IVC, segment I hypertrophies in Budd-Chiari syndrome. (Book p245)")

# ------------------------------------------------------------------ p246
S3 = "Brisbane Classification of Liver Resection"
q(246, S3, "According to the Brisbane classification, a left hepatectomy removes segments:",
  ["4A, 4B, 2 and 3", "5, 6, 7 and 8", "2 and 3 only", "4A and 4B only"], 0,
  "Left hepatectomy: segments 4A, 4B, 2 and 3. (Book p246)")
q(246, S3, "A right hepatectomy removes segments:",
  ["5, 6, 7 and 8", "4A, 4B, 2 and 3", "1 and 4A", "2, 3 and 4B"], 0,
  "Right hepatectomy: segments 5, 6, 7 and 8. (Book p246)")
q(246, S3, "A left trisectorectomy removes:",
  ["Segments 4A, 4B, 2 and 3 plus 5 and 8",
   "Segments 5, 6, 7 and 8 plus 4A and 4B",
   "Segments 2 and 3 only",
   "Segments 6 and 7 only"], 0,
  "Left trisectorectomy: 4A, 4B, 2, 3 + 5, 8. (Book p246)")
q(246, S3, "A right trisectorectomy removes:",
  ["Segments 5, 6, 7 and 8 plus 4A and 4B",
   "Segments 4A, 4B, 2 and 3 plus 5 and 8",
   "Segments 5 and 8 only",
   "Segments 1, 6 and 7"], 0,
  "Right trisectorectomy: 5, 6, 7, 8 + 4A, 4B. (Book p246)")
q(246, S3, "The old name for a left trisectorectomy is:",
  ["Extended left hepatectomy", "Extended right hepatectomy",
   "Left lateral sectionectomy", "Central hepatectomy"], 0,
  "Left trisectorectomy was formerly called an extended left hepatectomy. (Book p246)")
q(246, S3, "The old name for a right trisectorectomy is:",
  ["Extended right hepatectomy", "Extended left hepatectomy",
   "Right posterior sectionectomy", "Hemihepatectomy"], 0,
  "Right trisectorectomy was formerly called an extended right hepatectomy. (Book p246)")

S4 = "Blood Supply and the Liver Pedicle"
q(246, S4, "The liver has a dual blood supply: portal vein contributes about:",
  ["80%", "20%", "50%", "60%"], 0,
  "Dual blood supply: portal vein 80% and hepatic artery 20%. (Book p246)")
q(246, S4, "The hepatic artery contributes approximately what fraction of hepatic blood flow?",
  ["20%", "80%", "50%", "35%"], 0,
  "Portal vein 80% + hepatic artery 20%. (Book p246)")
q(246, S4, "Which hepatic artery is described as larger and supplying the majority of the liver?",
  ["Right hepatic artery", "Left hepatic artery", "Middle hepatic artery", "Common hepatic artery"], 0,
  "Right hepatic artery: larger, supplies the majority of the liver. (Book p246)")
q(246, S4, "In the 'Mickey mouse sign' of the liver pedicle, the portal vein lies:",
  ["Posteriorly", "Anteriorly", "To the left", "To the right"], 0,
  "Mickey mouse sign: portal vein posteriorly, CBD to the right (dextra) and hepatic artery to the left. (Book p246)")
q(246, S4, "In the Mickey mouse sign, the CBD lies to the __________ and the hepatic artery to the __________.",
  ["Right; left", "Left; right", "Right; middle", "Left; middle"], 0,
  "CBD (dextra = right), hepatic artery (left), portal vein (posteriorly). (Book p246)")

S5 = "Functions of the Liver and Their Assessment"
q(246, S5, "All of the following are listed as normal liver functions EXCEPT:",
  ["Production of erythropoietin", "Maintaining core body temperature",
   "pH balance and correction of acidosis", "Synthesis of clotting factors"], 0,
  "The listed functions are: maintaining core body temperature, pH balance and correction of acidosis, synthesis of clotting factors, glucose metabolism, bilirubin formation from Hb degradation, drug and hormone metabolism/excretion and removal of endotoxins and foreign antigens. (Book p246)")
q(246, S5, "Which liver function is listed as number 3 and, when it fails, produces a bleeding tendency?",
  ["Synthesis of clotting factors", "Glucose metabolism",
   "Bilirubin formation from Hb degradation", "Removal of endotoxins"], 0,
  "Function 3 is synthesis of clotting factors — its failure in liver dysfunction causes bleeding. (Book p246)")
q(246, S5, "Bilirubin is formed from:",
  ["Haemoglobin degradation", "Bile acid breakdown", "Cholesterol metabolism", "Amino acid catabolism"], 0,
  "Bilirubin formation from Hb degradation is listed as a normal liver function. (Book p246)")
q(246, S5, "Failure of the liver to remove endotoxins and foreign antigens is one of the mechanisms behind:",
  ["Encephalopathy in liver dysfunction", "Jaundice", "Ascites", "Portal hypertension"], 0,
  "The page links liver dysfunction with encephalopathy. (Book p246)")
q(246, S5, "Liver function tests listed in this chapter include:",
  ["Liver enzymes and clotting factor tests", "Only serum bilirubin",
   "Only serum albumin", "Only prothrombin time"], 0,
  "Liver function tests (LFT): liver enzymes and clotting factor tests. (Book p246)")
q(246, S5, "The investigation of choice that differentiates HCC from metastasis is:",
  ["Triple phase CT", "USG abdomen", "Plain CT abdomen", "MRCP"], 0,
  "Triple phase CT is the IOC and is specifically said to differentiate between HCC and metastases. (Book p246)")

# ------------------------------------------------------------------ p247
S6 = "Child-Turcotte-Pugh Score"
q(247, S6, "Each clinical/laboratory criterion in the Child-Turcotte-Pugh score is allotted points from:",
  ["1 to 3", "1 to 4", "0 to 2", "1 to 5"], 0,
  "The scoring columns are 1, 2 and 3 points for each criterion. (Book p247)")
q(247, S6, "In the Child-Turcotte-Pugh score, severe encephalopathy (grades 3 or 4) scores:",
  ["3 points", "1 point", "2 points", "4 points"], 0,
  "Encephalopathy: none = 1, mild to moderate (grades I or II) = 2, severe (grades 3 or 4) = 3. (Book p247)")
q(247, S6, "Diuretic refractory ascites in the Child-Turcotte-Pugh score is graded as:",
  ["Severe (3 points)", "Mild to moderate (2 points)", "None (1 point)", "Not scored"], 0,
  "Ascites: none = 1, mild to moderate/diuretic responsive = 2, severe/diuretic refractory = 3. (Book p247)")
q(247, S6, "In the Child-Turcotte-Pugh score, a bilirubin of 2-3 mg/dL scores:",
  ["2 points", "1 point", "3 points", "0 points"], 0,
  "Bilirubin (mg/dL): <2 = 1, 2-3 = 2, >3 = 3. (Book p247)")
q(247, S6, "An albumin of 2.8-3.5 g/dL scores how many points in the Child-Turcotte-Pugh score?",
  ["2", "1", "3", "0"], 0,
  "Albumin (g/dL): >3.5 = 1, 2.8-3.5 = 2, <2.8 = 3. (Book p247)")
q(247, S6, "In the Child-Turcotte-Pugh score the prothrombin time columns are:",
  ["<4 s, 4-6 s and >6 s", "<2 s, 2-4 s and >4 s", "<10 s, 10-14 s and >14 s", "<6 s, 6-10 s and >10 s"], 0,
  "Prothrombin time (s): <4 = 1, 4-6 = 2, >6 = 3 (or the INR equivalent: <1.7, 1.7-2.3, >2.3). (Book p247)")
q(247, S6, "The INR values used in the Child-Turcotte-Pugh score are:",
  ["<1.7, 1.7-2.3 and >2.3", "<1.0, 1.0-1.5 and >1.5", "<2.0, 2.0-3.0 and >3.0", "<1.5, 1.5-2.5 and >2.5"], 0,
  "International normalised ratio (INR): <1.7 = 1, 1.7-2.3 = 2, >2.3 = 3. (Book p247)")
q(247, S6, "Child-Turcotte-Pugh class A corresponds to a total score of:",
  ["5-6", "7-9", "10-15", "1-3"], 0,
  "Class A: 5-6 (least severe). (Book p247)")
q(247, S6, "Child-Turcotte-Pugh class B corresponds to a total score of:",
  ["7-9", "5-6", "10-15", "3-5"], 0,
  "Class B: 7-9 (moderately severe). (Book p247)")
q(247, S6, "Child-Turcotte-Pugh class C corresponds to a total score of:",
  ["10-15", "5-6", "7-9", "16-20"], 0,
  "Class C: 10-15 (most severe). (Book p247)")
q(247, S6, "The surgical mortality quoted for Child-Pugh class A is:",
  ["10%", "30%", "70%", "5%"], 0,
  "Correlates with surgical mortality: class A 10%. (Book p247)")
q(247, S6, "The surgical mortality quoted for Child-Pugh class C is:",
  ["70%", "10%", "30%", "50%"], 0,
  "Class C carries about 70% surgical mortality. (Book p247)")
q(247, S6, "A cirrhotic patient with bilirubin 4 mg/dL, albumin 2.5 g/dL, INR 2.6, moderate ascites and grade II encephalopathy falls into Child class:",
  ["C", "A", "B", "Cannot be scored without a biopsy"], 0,
  "Bilirubin >3 (3), albumin <2.8 (3), INR >2.3 (3), moderate ascites (2) and grade I-II encephalopathy (2) = 13 points, i.e. class C (10-15). (Book p247)")

S7 = "MELD and PELD Scores"
q(247, S7, "The MELD score uses which three parameters?",
  ["Serum bilirubin, INR and creatinine", "Albumin, bilirubin and INR",
   "Bilirubin, albumin and sodium", "Creatinine, sodium and INR"], 0,
  "Parameters involved in MELD: S. bilirubin, INR and creatinine. (Book p247)")
q(247, S7, "With a MELD score of 20 or less, mortality rises by:",
  ["1% per score", "2% per score", "5% per score", "10% per score"], 0,
  "Score ≤20: mortality ↑ 1% per score. (Book p247)")
q(247, S7, "With a MELD score above 20, mortality rises by:",
  ["2% per score after 20", "1% per score", "5% per score", "10% per score"], 0,
  "Score >20: mortality ↑ 2% per score after 20. (Book p247)")
q(247, S7, "Which of the following is NOT a parameter of the PELD score?",
  ["Creatinine", "Albumin", "Total bilirubin", "Growth failure"], 0,
  "PELD parameters: albumin, total bilirubin, INR, growth failure and age (<1 year). (Book p247)")
q(247, S7, "The age criterion used in the PELD score is:",
  ["Less than 1 year", "Less than 5 years", "Less than 12 years", "More than 60 years"], 0,
  "Age (<1 yr) is one of the five PELD parameters — PELD is the paediatric score. (Book p247)")

# ------------------------------------------------------------------ p248
S8 = "Liver Abscess: Types and Clinical Features"
q(248, S8, "The organism causing an amoebic liver abscess is:",
  ["Entamoeba histolytica", "Echinococcus granulosus",
   "Staphylococcus aureus", "Klebsiella pneumoniae"], 0,
  "Amoebic liver abscess is caused by Entamoeba histolytica. (Book p248)")
q(248, S8, "Amoebic liver abscess reaches the liver by which route?",
  ["Portal vein", "Ascending cholangitis", "Hepatic artery", "Direct extension from the colon"], 0,
  "Route of spread for amoebic abscess: the portal vein (which has laminar flow to the right side). (Book p248)")
q(248, S8, "The laminar portal flow to the right side explains why amoebic abscesses are most common in the:",
  ["Right lobe", "Left lobe", "Caudate lobe", "Quadrate lobe"], 0,
  "Because portal flow preferentially streams to the right side, the right lobe (bare area, segment 7) is most often involved. (Book p248)")
q(248, S8, "The most common route of spread for a pyogenic liver abscess is:",
  ["Ascending cholangitis", "Portal vein", "Hepatic artery", "Direct spread from a perforated ulcer"], 0,
  "Pyogenic abscess: ascending cholangitis. (Book p248)")
q(248, S8, "The commonest organism overall in a pyogenic liver abscess is:",
  ["E. coli", "Staphylococcus aureus", "Klebsiella", "Bacteroides"], 0,
  "Pyogenic abscess: polymicrobial (40%), m/c overall E. coli. (Book p248)")
q(248, S8, "The commonest organism causing pyogenic liver abscess in Asia is:",
  ["Klebsiella", "E. coli", "Staphylococcus aureus", "Enterococcus"], 0,
  "m/c in Asia: Klebsiella. (Book p248)")
q(248, S8, "A child with chronic granulomatous disease and a liver abscess is most likely to grow:",
  ["Staphylococcus aureus", "E. coli", "Klebsiella", "Streptococcus viridans"], 0,
  "m/c in children with CGD: S. aureus. (Book p248)")
q(248, S8, "Pyogenic liver abscess pus is typically:",
  ["Polymicrobial in about 40% of cases", "Always sterile", "Always fungal", "Always a single organism"], 0,
  "Polymicrobial (40%) is quoted for pyogenic liver abscess. (Book p248)")
q(248, S8, "CGD in the liver abscess table expands to:",
  ["Chronic granulomatous disease", "Common bile duct disease",
   "Cystic gallbladder disease", "Chronic gastric distension"], 0,
  "CGD: Chronic granulomatous disease. (Book p248)")
q(248, S8, "Amoebic liver abscesses are usually:",
  ["Solitary", "Multiple", "Bilobar and diffuse", "Confined to the left lobe"], 0,
  "Number: usually solitary in amoebic disease; solitary or multiple in pyogenic disease. (Book p248)")
q(248, S8, "The most common laboratory abnormality in amoebic liver abscess is:",
  ["Raised PT/INR", "Raised ALP", "Raised serum amylase", "Raised serum calcium"], 0,
  "Labs in amoebic abscess: ↑ PT/INR (m/c) and serology positive for Entamoeba. (Book p248)")
q(248, S8, "A raised ALP in a pyogenic liver abscess is attributed to:",
  ["Ascending cholangitis", "Bone metastasis", "Hepatocellular necrosis", "Haemolysis"], 0,
  "Pyogenic abscess labs: ↑ ALP (due to cholangitis), ↑ PT/INR and ↑ S. bilirubin. (Book p248)")
q(248, S8, "The diagnosis of an amoebic liver abscess is supported by:",
  ["Positive serology for Entamoeba", "Stool culture", "Blood culture", "Sputum microscopy"], 0,
  "Serology positive for Entamoeba is listed under the labs for amoebic abscess. (Book p248)")
q(248, S8, "Flask-shaped ulcers in the gut are associated with:",
  ["Amoebic liver abscess", "Pyogenic liver abscess", "Hydatid disease", "Amoebic colitis only, never with liver abscess"], 0,
  "Ulcers in the gut (flask-shaped) appear in the amoebic column. (Book p248)")
q(248, S8, "Compared with an amoebic abscess, a patient with a pyogenic liver abscess is:",
  ["More sick with more jaundice", "Less sick with less jaundice",
   "Asymptomatic", "Only febrile at night"], 0,
  "Clinical features: amoebic — pain and fever; pyogenic — more sick, ↑ jaundice. (Book p248)")
q(248, S8, "The pus of an amoebic liver abscess is classically described as:",
  ["Anchovy sauce pus", "Thick cream-coloured pus", "Green bile-stained pus", "Caseous material"], 0,
  "Amoebic pus is anchovy-sauce pus, in contrast to the neutrophil-rich pus of a pyogenic abscess. (Book p248)")
q(248, S8, "Epidemiologically both amoebic and pyogenic liver abscess are:",
  ["More common in males", "More common in females",
   "Equal in both sexes", "Seen only in children"], 0,
  "Epidemiology: males > females for both; pyogenic abscess is also associated with immunocompromise. (Book p248)")
q(248, S8, "Immunocompromised state is listed as a predisposition for:",
  ["Pyogenic liver abscess", "Amoebic liver abscess", "Hydatid cyst", "Hepatic adenoma"], 0,
  "Immunocompromised is listed in the pyogenic column. (Book p248)")

S9 = "Diagnosis and Treatment of Amoebic Liver Abscess"
q(248, S9, "The investigation of choice for a liver abscess is:",
  ["CECT abdomen", "Plain X-ray abdomen", "MRCP", "Liver scan"], 0,
  "IOC: CECT abdomen. (Book p248)")
q(248, S9, "On imaging, a liver abscess appears as:",
  ["An abscess cavity with hypoechoic liquefied pus", "A solid hyperechoic mass",
   "A calcified cyst", "A multiloculated cystic lesion with daughter cysts"], 0,
  "Abscess cavity with hypoechoic liquefied pus. (Book p248)")
q(248, S9, "Radiological resolution of the abscess cavity after treatment takes:",
  ["Months", "48 hours", "1 week", "Never — it persists for life"], 0,
  "Radiological resolution of the cavity takes months (post-Rx), so imaging is not used to judge early response. (Book p248)")
q(249, S9, "The drug used for an amoebic liver abscess in this chapter is:",
  ["Metronidazole (double strength 800 mg TID)", "Chloroquine alone",
   "Albendazole", "Ciprofloxacin"], 0,
  "A. Amoebic liver abscess: metronidazole (double strength: 800 mg TID). (Book p249)")
q(249, S9, "Response to metronidazole is judged after:",
  ["4-5 days", "24 hours", "2 weeks", "6 weeks"], 0,
  "After 4-5 days the fever and pain should settle. (Book p249)")
q(249, S9, "The total duration of metronidazole therapy recommended here is:",
  ["2-3 weeks", "4-5 days", "10 days", "6 months"], 0,
  "After the initial 4-5 days and a fall in fever and pain, treatment is continued for 2-3 weeks. (Book p249)")
q(249, S9, "After completion of the course of metronidazole, the patient should receive:",
  ["A luminal amoebicide — diloxanide furoate for 10 days",
   "No further treatment",
   "Albendazole for 10 days",
   "A repeat course of metronidazole"], 0,
  "After completion of the course, a luminal amoebicide (diloxanide furoate × 10 days) is given. (Book p249)")
q(249, S9, "If an amoebic abscess does not respond to metronidazole, the next step is:",
  ["Aspiration of pus under USG/CT guidance", "Immediate laparotomy",
   "Change to albendazole", "Add steroids"], 0,
  "Not responding → aspiration of pus (USG/CT guided). (Book p249)")
q(249, S9, "Which of the following is NOT listed as an indication for aspirating an amoebic liver abscess?",
  ["A cavity smaller than 2 cm", "Cavity larger than 5 cm",
   "Pregnancy", "Impending rupture"], 0,
  "Other indications listed: abscess cavity >5 cm, pregnant patient, impending rupture and a left lobe abscess (which can rupture into the pericardium). (Book p249)")
q(249, S9, "A left lobe amoebic liver abscess is aspirated early because it can rupture into the:",
  ["Pericardium", "Splenic vein", "Stomach", "Pleural cavity only on the right"], 0,
  "Left lobe liver abscess can rupture into the pericardium. (Book p249)")
q(249, S9, "A pigtail catheter is used for:",
  ["Aspiration of pus anywhere in the abdominal cavity under USG/CT guidance",
   "Draining bile from the gallbladder",
   "Feeding jejunostomy",
   "Measuring portal pressure"], 0,
  "Pigtail catheter: aspiration of pus anywhere in the abdominal cavity under USG/CT guidance. (Book p249)")

S10 = "Pyogenic Liver Abscess and Complications of Amoebic Abscess"
q(249, S10, "First-line treatment of a pyogenic liver abscess is:",
  ["Broad spectrum IV antibiotics", "Immediate surgery",
   "Metronidazole alone", "Albendazole"], 0,
  "B. Pyogenic liver abscess: IV antibiotics, broad spectrum. (Book p249)")
q(249, S10, "The threshold for aspiration in a pyogenic liver abscess should be:",
  ["Low — aspirate quickly with a pigtail catheter if the patient is not responding",
   "Very high — never aspirate",
   "Same as for an amoebic abscess (wait 2-3 weeks)",
   "Aspiration is contraindicated"], 0,
  "Low threshold for aspiration: if the patient is not responding, aspirate quickly with a pigtail catheter. (Book p249)")
q(249, S10, "The most common site of rupture of an amoebic liver abscess is the:",
  ["Sub-diaphragmatic space", "Pleural cavity", "Peritoneal cavity", "Pericardial cavity"], 0,
  "Rupture: sub-diaphragmatic space (m/c), then pleural, peritoneal and pericardial cavities. (Book p249)")
q(249, S10, "Which of the following is NOT listed as a rupture site of an amoebic liver abscess?",
  ["Splenic parenchyma", "Sub-diaphragmatic space", "Pleural cavity", "Pericardial cavity"], 0,
  "The listed sites are sub-diaphragmatic (m/c), pleural, peritoneal and pericardial. (Book p249)")
q(249, S10, "Secondary infection is listed as a complication of:",
  ["Amoebic liver abscess", "Hydatid cyst only", "Pyogenic liver abscess only", "Hepatic adenoma"], 0,
  "Complications of amoebic liver abscess: rupture (into four sites) and secondary infection. (Book p249)")
