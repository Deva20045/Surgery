#!/usr/bin/env python3
"""Build data/ch48.json — Prostate: Part 2 (Marrow Surgery Ed 8, pp365-370)."""
import json

Q = []

def q(page, sec, text, correct, wrongs, note=None):
    opts = [correct] + list(wrongs)
    assert len(opts) == 4
    Q.append({
        "id": f"SURG-C48-{len(Q)+1:03d}",
        "sec": sec,
        "page": page,
        "q": text,
        "opts": opts,
        "ans": 0,
        "exp": (note or correct) + f" (Book p{page})",
    })

# ------------------------------------------------------------------ p365
S1 = "BPH: Medical Management"
q(365, S1, "Alpha blockers for BPH are:", "Alpha1A selective", ["Alpha1 non-selective only", "Beta blockers", "Calcium channel blockers"])
q(365, S1, "Alpha blocker drugs for BPH include:", "Tamsulosin, Alfuzosin", ["Finasteride, Dutasteride", "Flutamide, Abiraterone", "Goserelin, Buserelin"])
q(365, S1, "5α-reductase inhibitor drugs for BPH include:", "Finasteride, Dutasteride", ["Tamsulosin, Alfuzosin", "Degarelix, Goserelin", "Paclitaxel, Cabazitaxel"])
q(365, S1, "Alpha blockers act on the:", "Dynamic component (decreased smooth muscle tone)", ["Static component", "Stromal hyperplasia", "Glandular atrophy"])
q(365, S1, "5α-reductase inhibitors act on the:", "Static component (decreased stromal hyperplasia)", ["Dynamic component", "Smooth muscle tone", "Bladder neck relaxation"])
q(365, S1, "Onset of action of alpha blockers is:", "Quick (Days)", ["Delayed (weeks/months)", "Over 6 months", "After a year"])
q(365, S1, "Onset of action of 5α-reductase inhibitors is:", "Delayed (weeks/months)", ["Quick (Days)", "Within hours", "Immediate"])
q(365, S1, "5α-reductase inhibitors have more sustained action with:", "50% decrease in PSA", ["50% increase in PSA", "No change in PSA", "100% rise in PSA"])
q(365, S1, "Over 6 months, 5α-reductase inhibitors cause:", "20–30% decrease in prostate volume", ["20–30% increase in volume", "No volume change", "Complete disappearance"])
q(365, S1, "The sustained PSA and volume effects occur over:", "6 months", ["6 days", "6 weeks", "6 years"])
q(365, S1, "First-dose side effect of alpha blockers is:", "Postural hypotension", ["Hypertension", "Difficulty with erection", "Decreased sexual drive"])
q(365, S1, "Side effects of 5α-reductase inhibitors include:", "Difficulty with erection", ["Postural hypotension", "Tachycardia", "Diarrhoea"])
q(365, S1, "5α-reductase inhibitors decrease:", "Sexual drive", ["Blood pressure acutely", "Serum creatinine", "Urine output immediately"])
q(365, S1, "Best medical management of BPH is:", "Combination therapy", ["Alpha blocker alone", "5α-reductase inhibitor alone", "No drugs"])

S2 = "BPH: Surgical Indications and Options"
q(365, S2, "A surgical indication in BPH is involvement of upper tracts with:", "Hydronephrosis", ["Hydrocele", "Hydatid cyst", "Hydrocephalus"])
q(365, S2, "BPH needs surgery when there is:", "No response to medical mx", ["Good response to drugs", "Mild IPSS only", "Normal flow rate"])
q(365, S2, "A surgical indication in BPH is:", "Acute/chronic retention of urine", ["Normal voiding", "No residual urine", "Frequency only"])
q(365, S2, "Recurrent infections prompting BPH surgery are:", "Multiple UTIs", ["Multiple pneumonias", "Single UTI", "Skin infections"])
q(365, S2, "A surgical indication in BPH is:", "Gross hematuria", ["Microscopic pyuria only", "No haematuria", "Proteinuria only"])
q(365, S2, "Back pressure changes in the bladder include:", "Diverticulae, trabeculations", ["Normal bladder wall", "Bladder stones only", "Ureterocele"])
q(365, S2, "A flow-rate indication for BPH surgery is urine flow rate:", "<10 mL/s", [">15 mL/s", "10–15 mL/s", ">20 mL/s"])
q(365, S2, "A pressure indication for BPH surgery is bladder pressure:", ">80 cm H2O", ["<60 cm H2O", "60–80 cm H2O", "<10 cm H2O"])
q(365, S2, "A type of prostate surgery is:", "Trans urethral resection of prostate (TURP)", ["Trans urethral resection of bladder", "Open cystectomy", "Nephrectomy"])
q(365, S2, "TURP is the:", "Standard of care", ["Older obsolete method", "Experimental method", "Palliative method only"])
q(365, S2, "A laser enucleation surgery for BPH is:", "Holmium laser enucleation of prostate (HOLEP)", ["TULIP", "TURP", "Millin prostatectomy"])
q(365, S2, "A laser incision surgery for BPH is:", "Trans urethral laser incision of prostate (TULIP)", ["HOLEP", "TURP", "Radical cystectomy"])
q(365, S2, "Open/retropubic/Millin's prostatectomy is an:", "Older method", ["Standard of care", "Laser method", "First-line method"])
q(365, S2, "Open prostatectomy is not preferred due to:", "Increased complications", ["Decreased complications", "Better results", "Lower cost"])
q(365, S2, "Lasers used in prostate surgery are:", "Hemostatic, faster surgery", ["Slow and bloody", "Non-hemostatic", "Only diagnostic"])
q(365, S2, "The most common laser used in prostate surgery is:", "Nd:YAG", ["KTPA", "CO2", "Argon"])
q(365, S2, "The best laser, a green light of 532 nm, is:", "KTPA", ["Nd:YAG", "Holmium only", "Excimer"])

# ------------------------------------------------------------------ p366-367
S3 = "TURP: Irrigating Fluids, Technique and Early Complications"
q(366, S3, "Irrigating fluids provide:", "A clear field of vision during the procedure", ["Haemostasis alone", "Anaesthesia", "Antibiotics"])
q(366, S3, "A hypotonic irrigating fluid is:", "5% dextrose", ["Isotonic glycine 1.5%", "Normal saline", "Ringer lactate"])
q(366, S3, "A hypotonic irrigating fluid is:", "Distilled water", ["Normal saline", "Isotonic glycine", "Blood"])
q(366, S3, "Hypotonic fluids increase the risk of:", "TURP syndrome", ["Retrograde ejaculation", "Meatal stenosis", "Bladder neck stenosis"])
q(366, S3, "The most common and best irrigating fluid is:", "Isotonic glycine (1.5%)", ["5% dextrose", "Distilled water", "Normal saline"])
q(366, S3, "Normal saline is only used in:", "Bipolar TURP", ["Monopolar TURP", "Open prostatectomy", "HOLEP only"])
q(366, S3, "The instrument used for TURP is the:", "Resectoscope", ["Cystoscope only", "Nephroscope", "Ureteroscope"])
q(366, S3, "Haemorrhage in TURP occurs:", "During and after surgery", ["Only before surgery", "Never", "Only after a year"])
q(366, S3, "The most common vessels bleeding in TURP are:", "Badenoch's arteries", ["Floch arteries", "Vesical arteries", "Pudendal arteries"])
q(366, S3, "Other vessels bleeding in TURP are:", "Floch arteries", ["Coronary arteries", "Renal arteries", "Carotid arteries"])
q(366, S3, "To control TURP bleeding, do:", "Prophylactic coagulation", ["No coagulation", "Only transfusion", "Only observation"])
q(366, S3, "Prophylactic coagulation sites for Badenoch's arteries are at:", "5 o'clock and 7 o'clock", ["10 o'clock only", "12 o'clock only", "3 o'clock only"])
q(366, S3, "The prophylactic coagulation site for the Floch artery is at:", "10 o'clock", ["5 o'clock", "7 o'clock", "6 o'clock"])
q(366, S3, "Badenoch's and Floch arteries are branches of the:", "Inferior vesicle artery", ["Superior vesicle artery", "Obturator artery", "Pudendal artery"])
q(366, S3, "Veru montanum is the:", "Distal limit of resection", ["Proximal limit of resection", "Site of biopsy", "Site of anastomosis"])
q(366, S3, "The transurethral approach diagram labels the outlet sphincter as the:", "Internal urethral sphincter", ["External urethral sphincter", "Anal sphincter", "Pyloric sphincter"])
q(366, S3, "Clot retention after TURP is managed with:", "Continuous irrigation with a 3-way Foley's catheter", ["Single irrigation only", "No irrigation", "Immediate re-operation"])
q(366, S3, "The 3-way Foley's catheter channels are for:", "Irrigation, urine and balloon", ["Blood, bile and air", "Artery, vein and nerve", "Oxygen, suction and drugs"])
q(366, S3, "Water intoxication is also called:", "Dilutional hyponatremia/TURP syndrome", ["Hypernatremia", "Hyperkalemia", "Metabolic alkalosis"])
q(366, S3, "TURP syndrome pathogenesis involves:", "Hypotonic irrigation fluids (intra-op) creating an osmotic gradient", ["Hypertonic fluids", "Isotonic fluids only", "Blood transfusion"])
q(366, S3, "The amount of fluid diffused into blood in TURP syndrome is:", "~1 litre", ["~100 ml", "~5 litres", "~10 litres"])
q(366, S3, "TURP syndrome leads to:", "Dilutional hyponatremia", ["Hypernatremia", "Hyperchloremia", "Hypokalemia only"])
q(367, S3, "TURP syndrome features appear:", "4–6 hours post-op", ["Immediately on table", "After a week", "After a month"])
q(367, S3, "A clinical feature of TURP syndrome is:", "Altered sensorium", ["Normal sensorium", "Hypertension only", "Fever only"])
q(367, S3, "TURP syndrome causes:", "Nausea and vomiting", ["Diarrhoea only", "Constipation only", "Polyuria only"])
q(367, S3, "In TURP syndrome, monitor:", "Serum Na+", ["Serum K+ only", "Serum calcium only", "Blood glucose only"])
q(367, S3, "Mild TURP syndrome (>120 mEq/L) is managed with:", "Fluid restriction", ["3% hypertonic saline", "Aggressive IV fluids", "Immediate dialysis"])
q(367, S3, "Severe TURP syndrome (<120 mEq/L) needs:", "Na+ correction with 3% hypertonic saline", ["Fluid restriction only", "No treatment", "Only diuretics"])
q(367, S3, "TURP syndrome is prevented with:", "Isotonic irrigating fluids", ["Hypotonic fluids", "Distilled water", "5% dextrose"])
q(367, S3, "Lasers prevent TURP syndrome by:", "Decreasing duration of surgery", ["Increasing duration", "Increasing fluid absorption", "Causing hyponatremia"])
q(367, S3, "Na+ correction must be ≤8–10 mEq/L per day or it can cause:", "Central pontine demyelinosis/myelinolysis", ["Liver failure", "Renal stones", "Bladder rupture"])

# ------------------------------------------------------------------ p367
S4 = "TURP Late Complications and PIRADS"
q(367, S4, "Glycine toxicity increases the risk of MI if absorbed glycine exceeds:", ">500 cc", [">50 cc", ">5 litres", ">5 cc"])
q(367, S4, "The most common late complication after TURP is:", "Retrograde ejaculation", ["Stricture", "Incontinence", "TURP syndrome"])
q(367, S4, "Retrograde ejaculation is due to:", "Bladder neck injury", ["Veru montanum injury", "Urethral injury", "Rectal injury"])
q(367, S4, "The incidence of retrograde ejaculation post TURP is:", "60–70%", ["6–7%", "100%", "1–2%"])
q(367, S4, "Retrograde ejaculation causes:", "Turbid urine (Sperms in urine)", ["Clear urine always", "Haematuria only", "Pneumaturia"])
q(367, S4, "The most common site of stricture after TURP is the:", "Bladder neck", ["Membranous urethra", "Penile urethra", "External meatus"])
q(367, S4, "Large bore resectoscope causes:", "Meatal stenosis", ["Bladder neck stenosis", "Ureteric stricture", "Rectal stenosis"])
q(367, S4, "Incontinence after TURP is due to:", "Resection past veru montanum", ["Bladder neck injury", "Small resection", "Laser use"])
q(367, S4, "PIRADS stands for:", "Prostate imaging reporting and data systems", ["Prostate infection rating and drug854", "Pelvic injury reporting scale", "Prostate biopsy grading"])
q(367, S4, "The imaging modality for PIRADS is:", "MRI", ["CT", "USG", "X-ray"])
q(367, S4, "PI-RADS score 1 means risk of malignancy:", "Very low", ["Low", "Intermediate", "Very high"])
q(367, S4, "PI-RADS score 2 means risk of malignancy:", "Low", ["Very low", "High", "Very high"])
q(367, S4, "PI-RADS score 3 means risk of malignancy:", "Intermediate", ["Low", "High", "Very high"])
q(367, S4, "PI-RADS score 4 means risk of malignancy:", "High", ["Low", "Intermediate", "Very high"])
q(367, S4, "PI-RADS score 5 means risk of malignancy:", "Very high", ["Very low", "Low", "Intermediate"])

# ------------------------------------------------------------------ p368
S5 = "Prostate Cancer: Risk, Screening, Spread and Gleason"
q(368, S5, "Prostate cancer is an:", "Adenocarcinoma", ["Squamous cell carcinoma", "Transitional cell carcinoma", "Sarcoma"])
q(368, S5, "A risk factor for prostate cancer is:", "Increased age", ["Young age", "Female sex", "Low testosterone"])
q(368, S5, "A risk factor for prostate cancer is:", "Increased testosterone", ["Decreased testosterone", "Increased oestrogen", "Decreased DHT"])
q(368, S5, "Prostate cancer risk is higher in:", "African american", ["Asian only", "Caucasian only", "Hispanic only"])
q(368, S5, "The BRCA association in prostate cancer is:", "BRCA2 > BRCA1", ["BRCA1 > BRCA2", "Only BRCA1", "No BRCA link"])
q(368, S5, "A risk factor for prostate cancer is:", "Obesity", ["Underweight", "Short stature", "Anaemia"])
q(368, S5, "The most common gene mutated in prostate cancer is:", "GSTP-1", ["BRCA1", "p53 only", "APC"])
q(368, S5, "Prostate cancer screening is done annually if age:", ">50 yrs", ["<30 yrs", ">80 yrs only", "At birth"])
q(368, S5, "A screening modality for prostate cancer is:", "Digital rectal exam (DRE)", ["Chest X-ray", "Mammography", "Colonoscopy"])
q(368, S5, "A screening modality for prostate cancer is:", "Prostate specific antigen (PSA)", ["AFP", "CEA", "CA 19-9"])
q(368, S5, "Best screening for prostate cancer is:", "DRE + PSA", ["DRE alone", "PSA alone", "USG alone"])
q(368, S5, "A clinical feature of prostate cancer is:", "Lower urinary tract symptoms (LUTS)", ["Upper GI bleed", "Chest pain", "Headache"])
q(368, S5, "Prostate cancer may present with:", "Metastasis", ["Only LUTS", "Only fever", "Only jaundice"])
q(368, S5, "Local workup of prostate cancer is:", "Core biopsy (minimum 12 cores)", ["FNAC only", "Excision biopsy", "No biopsy"])
q(368, S5, "Local spread workup of prostate cancer is:", "Multiparametric MRI (mp MRI)", ["Plain X-ray", "USG only", "Bone scan"])
q(368, S5, "Distant spread workup of prostate cancer is:", "Prostate specific membrane antigen PET (PSMA-PET)", ["HIDA scan", "Meckel scan", "Thyroid scan"])
q(368, S5, "Local spread of prostate cancer is to:", "Seminal vesicles, rectum", ["Bladder dome only", "Kidneys", "Liver"])
q(368, S5, "Lymph node spread of prostate cancer is:", "Obturator LN to Iliac LN", ["Inguinal to cervical", "Axillary to iliac", "Mesenteric nodes"])
q(368, S5, "The most common distant spread of prostate cancer is to:", "Bones", ["Lungs", "Liver", "Brain"])
q(368, S5, "Bony mets favour the:", "Lumbar vertebrae", ["Skull only", "Ribs only", "Small bones of hand"])
q(368, S5, "Bony spread is via:", "Batson's plexus", ["Portal vein", "Thoracic duct", "Coronary sinus"])
q(368, S5, "Prostate bony mets are:", "Osteoblastic > osteolytic", ["Osteolytic > osteoblastic", "Only lytic", "Only cystic"])
q(368, S5, "On a bone scan, black spots signify:", "Metastatic tissue", ["Normal bone", "Fracture healing", "Infection only"])
q(368, S5, "Bone scan is indicated if PSA is:", ">10 ng/mL", ["<4 ng/mL", "<1 ng/mL", ">100 ng/mL only"])
q(368, S5, "Bone scan is indicated in a:", "Symptomatic patient", ["Asymptomatic patient always", "Young patient only", "Female patient"])
q(368, S5, "Bone scan is indicated if Gleason score is:", ">7", ["<6", "=2", "<4"])
q(368, S5, "Gleason scoring starts by identifying the:", "Type of gland", ["Type of stroma", "Type of vessel", "Type of nerve"])
q(368, S5, "In Gleason scoring, the most common pattern is graded:", "Between 1 to 5", ["Between 6 to 10", "Between 0 to 1", "As 0 or 1 only"])
q(368, S5, "In Gleason scoring, the second most common pattern is graded:", "Between 1 to 5", ["Between 6 to 10", "As 10 always", "As 0 always"])
q(368, S5, "Gleason example 3+4 means 3 is most common and 4 is:", "2nd most common", ["Least common", "Absent", "Normal tissue"])
q(368, S5, "Gleason 3+4 gives a score of:", "7", ["3", "4", "12"])
q(368, S5, "In Gleason grading, 1-2-3-4-5 runs from well differentiated to:", "Poorly differentiated", ["Normal tissue", "Benign hyperplasia", "Metaplasia"])

# ------------------------------------------------------------------ p369-370
S6 = "Prostate Cancer: Staging, Grading and Management"
q(369, S6, "Low risk group has ISUP grade group:", "1", ["2", "4", "5"])
q(369, S6, "Low risk Gleason score is:", "≤6", ["7 (3+4)", "7 (4+3)", "9–10"])
q(369, S6, "Intermediate favourable risk has ISUP grade group:", "2", ["1", "3", "5"])
q(369, S6, "Intermediate favourable Gleason score is:", "7 (3+4)", ["≤6", "7 (4+3)", "8"])
q(369, S6, "Intermediate unfavourable risk has ISUP grade group:", "3", ["1", "2", "4"])
q(369, S6, "Intermediate unfavourable Gleason score is:", "7 (4+3)", ["≤6", "7 (3+4)", "9–10"])
q(369, S6, "High risk ISUP grade group 4 has Gleason score:", "8", ["≤6", "7", "9–10"])
q(369, S6, "High risk ISUP grade group 5 has Gleason score:", "9–10", ["≤6", "7", "8"])
q(369, S6, "Tx prostate cancer means:", "Primary tumor cannot be assessed", ["No evidence of tumor", "Tumor confined to prostate", "Fixed tumor"])
q(369, S6, "T0 prostate cancer means:", "No evidence of primary tumor", ["Cannot be assessed", "Incidental finding", "Extracapsular extension"])
q(369, S6, "T1a prostate tumor is an incidental histologic finding in:", "≤5% of resected tissue", [">5% of resected tissue", "100% of tissue", "Needle biopsy"])
q(369, S6, "T1b prostate tumor is an incidental histologic finding in:", ">5% of resected tissue", ["≤5% of resected tissue", "Needle biopsy only", "No tissue"])
q(369, S6, "T1c prostate tumor is identified with:", "Needle biopsy (Eg: due to elevated PSA level)", ["Incidental TURP chips only", "Cystectomy", "Bone scan"])
q(369, S6, "T2 prostate tumor is:", "Confined to prostate", ["Extracapsular", "Fixed to pelvis", "Metastatic"])
q(369, S6, "T3 prostate tumor shows:", "Extracapsular extension (Unilateral/bilateral)", ["Confinement to prostate", "No tumor", "Only needle biopsy finding"])
q(369, S6, "T4 prostate tumor:", "Is fixed or invades adjacent structures other than seminal vesicles", ["Is confined to prostate", "Is incidental only", "Never invades"])
q(369, S6, "A prognostic score for prostate cancer is:", "Partin tables", ["Gleason tables", "IPSS", "Child-Pugh"])
q(369, S6, "A prognostic score for prostate cancer is:", "D'Amico score", ["MELD score", "Apgar score", "Wells score"])
q(369, S6, "Aggressive management criteria include age:", "<70 years of age", [">70 years of age", ">80 years", "<40 years"])
q(369, S6, "Aggressive management needs expected life span:", ">10 years", ["<10 years", "<5 years", "<1 year"])
q(369, S6, "Aggressive tumors are:", "G3/G4 tumors", ["G1/G2 tumors", "Benign tumors", "No tumors"])
q(369, S6, "Observation criteria include age:", ">70 years of age", ["<70 years of age", "<50 years", ">90 years only"])
q(369, S6, "Observation needs expected life span:", "<10 years", [">10 years", ">20 years", ">30 years"])
q(369, S6, "Observation is for:", "G1/G2 tumors", ["G3/G4 tumors", "Metastatic tumors", "T4 tumors"])
q(369, S6, "T1 and T2a aggressive disease gets:", "Nerve preserving robotic radical prostatectomy", ["Observation", "Only ADT", "Palliative care"])
q(369, S6, "Robotic prostatectomy decreases the risk of:", "Sexual/bladder dysfunction", ["Bleeding only", "Infection only", "Pain only"])
q(369, S6, "Radical prostatectomy removes:", "Prostate with part of urethra", ["Bladder only", "Rectum", "Testis"])
q(369, S6, "Radical prostatectomy removes the:", "Seminal vesicle", ["Vas deferens only", "Epididymis", "Penis"])
q(369, S6, "Radical prostatectomy removes:", "Lymph nodes", ["Bones", "Lungs", "Liver"])
q(369, S6, "T1 and T2a in elderly low-grade disease gets:", "Observation", ["Radical prostatectomy", "Salvage surgery", "Chemotherapy"])
q(369, S6, "T2b, T3 and T4 aggressive disease gets:", "Radiotherapy (Brachytherapy → I125, Palliative)", ["Observation", "No treatment", "Only biopsy"])
q(369, S6, "Good response to radiotherapy shows:", "Decreased PSA", ["Increased PSA", "Normal PSA always", "No PSA change"])
q(369, S6, "After good response, do:", "Monitor PSA", ["Immediate salvage surgery", "Stop follow-up", "Cystectomy"])
q(369, S6, "Good responders may also get:", "Androgen deprivation therapy (ADT)", ["Chemotherapy always", "No hormones", "Only antibiotics"])
q(369, S6, "Poor response to radiotherapy needs:", "Salvage Sx", ["Observation", "No treatment", "Only PSA monitoring"])
q(369, S6, "Elderly T2b, T3 and T4 disease gets:", "Radiotherapy ± ADT", ["Observation only", "Radical prostatectomy", "No treatment"])
q(370, S6, "Metastatic prostate cancer is:", "Hormone dependant", ["Hormone independent always", "Radiation resistant", "Surgery only"])
q(370, S6, "First line for metastatic prostate cancer is:", "Androgen deprivation therapy (ADT)", ["Chemotherapy", "Radiotherapy", "Observation"])
q(370, S6, "Surgical ADT is:", "B/L orchidectomy", ["Vasectomy", "TURP", "Nephrectomy"])
q(370, S6, "Rising PSA on ADT means:", "Hormone resistant tumor", ["Cured tumor", "Benign disease", "No tumor"])
q(370, S6, "Anti androgens for prostate cancer include:", "Flutamide, Abiraterone", ["Goserelin, Buserelin", "Degarelix", "Paclitaxel"])
q(370, S6, "LHRH antagonist for prostate cancer is:", "Degarelix", ["Goserelin", "Buserelin", "Flutamide"])
q(370, S6, "LHRH analogues for prostate cancer include:", "Goserelin, Buserelin", ["Degarelix", "Flutamide", "Cabazitaxel"])
q(370, S6, "LHRH analogues cause:", "Initial PSA flare up", ["Immediate PSA fall", "No PSA change", "Castration immediately"])
q(370, S6, "Hence LHRH analogues are combined with:", "Anti-androgens", ["Antibiotics", "Antifungals", "Diuretics"])
q(370, S6, "Chemotherapy for hormone resistant tumors includes:", "Paclitaxel", ["Flutamide", "Degarelix", "Goserelin"])
q(370, S6, "Chemotherapy for hormone resistant tumors includes:", "Cabazitaxel", ["Abiraterone", "Buserelin", "Finasteride"])
q(370, S6, "SIPULEUCEL-T is a:", "T-cell vaccine", ["B-cell vaccine", "Antibiotic", "Hormone"])
q(370, S6, "SIPULEUCEL-T is a:", "CD54 extract", ["CD4 extract", "PSA extract", "Testosterone extract"])
q(370, S6, "The trade name of SIPULEUCEL-T is:", "Provenge", ["Proscar", "Flomax", "Zoladex"])
q(370, S6, "Bony mets get:", "Radiopharmaceutical therapy", ["Only surgery", "Only antibiotics", "No treatment"])
q(370, S6, "Radiopharmaceuticals for bony mets include:", "Strontium 89", ["Iodine 131", "Technetium 99", "Fluorine 18"])
q(370, S6, "Radiopharmaceuticals for bony mets include:", "Radium 223", ["Strontium 90", "Cobalt 60", "Cesium 137"])
q(370, S6, "Strontium 89 and Radium 223 emit:", "Alpha-rays", ["Beta-rays", "Gamma-rays only", "X-rays only"])
q(370, S6, "The most important prognostic factor in prostate cancer is:", "Stage of the disease", ["Age", "PSA velocity", "Prostate size"])

# ------------------------------------------------------------------ units
def first_page(title):
    return next(x["page"] for x in Q if x["sec"] == title)

UNIT_DEFS = [
    (S1, "Alpha1A blockers tamsulosin and alfuzosin relax the dynamic smooth-muscle component within days but risk first-dose postural hypotension, while finasteride and dutasteride shrink the static stromal component over weeks to months with a halved PSA and 20–30% smaller gland at six months at the cost of erection and libido; combining both is the best medical plan."),
    (S2, "Operate BPH for hydronephrotic upper tracts, drug failure, acute or chronic retention, repeated UTIs, gross haematuria, diverticulae/trabeculations, flow below 10 mL/s or pressure above 80 cm water. TURP remains standard of care beside HOLEP, TULIP and the older complication-prone Millin open route, with haemostatic faster lasers led by common Nd:YAG and best green 532-nm KTPA."),
    (S3, "Clear TURP vision comes from isotonic 1.5% glycine as the commonest best fluid, avoiding hypotonic dextrose and distilled water that invite TURP syndrome while reserving saline for bipolar surgery. The resectoscope coagulates Badenoch vessels at 5 and 7 o'clock and Floch vessels at 10 o'clock from the inferior vesical artery, respects veru montanum as the distal limit, irrigates clot retention through a 3-way catheter, and watches for ~1 litre dilutional hyponatraemia at 4–6 hours with altered sensorium and vomiting, restricting fluids when mild, correcting with 3% saline when severe, and preventing it with isotonic fluids and shorter laser cases while limiting correction to 8–10 mEq/day to avoid pontine myelinolysis."),
    (S4, "Beyond 500 cc of absorbed glycine threatens myocardial infarction, while bladder-neck injury causes retrograde ejaculation with spermy turbid urine in 60–70% as the commonest late event, strictures favour the bladder neck with large scopes stenosing the meatus, and cutting past veru montanum incontinently overshoots. PIRADS then grades MRI malignancy risk from 1 very low through 2 low, 3 intermediate and 4 high to 5 very high."),
    (S5, "Prostatic adenocarcinoma rises with age, testosterone, African ancestry, BRCA2 over BRCA1, obesity and GSTP-1 mutation, screened yearly after 50 with DRE plus PSA together. Local disease needs 12-core biopsy, local spread needs multiparametric MRI and distant spread needs PSMA-PET; tumours reach seminal vesicles and rectum locally, obturator then iliac nodes regionally, and lumbar bones distantly through Batson's plexus as osteoblastic-dominant black spots, prompting bone scans when PSA exceeds 10, symptoms appear or Gleason exceeds 7, with Gleason summing the 1–5 grades of the commonest and next-commonest gland patterns."),
    (S6, "ISUP 1–5 maps low ≤6 through intermediate 7(3+4) favourable and 7(4+3) unfavourable to high 8 and 9–10 disease, while TNM runs Tx/T0 through incidental T1a ≤5%, T1b >5% and T1c needle-detected, confined T2, extracapsular T3 and fixed T4 beyond seminal vesicles, refined by Partin and D'Amico scores. Fit under-70 aggressive T1–T2a disease earns nerve-sparing robotic prostatectomy with urethra, vesicles and nodes, while older low-grade cases watch; bulkier T2b–T4 disease takes I-125 brachytherapy with PSA-monitored ADT or salvage surgery, and hormone-dependent metastases start androgen deprivation by bilateral orchidectomy or flutamide/abiraterone, degarelix or flare-prone goserelin/buserelin with antiandrogen cover, escalating to paclitaxel/cabazitaxel, Provenge Sipuleucel-T CD54 vaccine and alpha-emitting strontium-89/radium-223 for bone, with stage as the supreme prognostic factor."),
]

UNITS = []
for i, (title, guide) in enumerate(UNIT_DEFS, 1):
    UNITS.append({
        "id": f"SURG-U48-{i}",
        "ch": 48,
        "n": i,
        "title": title,
        "sec": f"{title} · p{first_page(title)}",
        "qs": [x["id"] for x in Q if x["sec"] == title],
        "guide": guide,
    })

covered = [x for u in UNITS for x in u["qs"]]
assert covered == [x["id"] for x in Q]
assert len(set(covered)) == len(covered)
with open("data/ch48.json", "w", encoding="utf-8") as f:
    json.dump({"questions": Q, "units": UNITS}, f, ensure_ascii=False, indent=1)
print(f"ch48: {len(Q)} questions, {len(UNITS)} units")
