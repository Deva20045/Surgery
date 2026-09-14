#!/usr/bin/env python3
"""Build data/ch47.json — Prostate: Part 1 (Marrow Surgery Ed 8, pp360-364)."""
import json

Q = []

def q(page, sec, text, correct, wrongs, note=None):
    opts = [correct] + list(wrongs)
    assert len(opts) == 4
    Q.append({
        "id": f"SURG-C47-{len(Q)+1:03d}",
        "sec": sec,
        "page": page,
        "q": text,
        "opts": opts,
        "ans": 0,
        "exp": (note or correct) + f" (Book p{page})",
    })

# ------------------------------------------------------------------ p360
S1 = "Surgical Anatomy of the Prostate"
q(360, S1, "The gland sitting above the prostate in the zones diagram is the:", "Seminal vesicle", ["Bulbourethral gland", "Adrenal gland", "Pituitary gland"])
q(360, S1, "The dilated terminal part of the vas shown in the prostate diagram is the:", "Ampulla of vas deferens", ["Ampulla of Vater", "Prostatic utricle", "Ejaculatory duct only"])
q(360, S1, "The central zone of the prostate has:", "Short, unbranched glands", ["Long, branched glands", "No glands", "Only fibromuscular stroma"])
q(360, S1, "The urethra passing through the prostate is the:", "Prostatic urethra", ["Penile urethra", "Membranous urethra only", "Bulbar urethra only"])
q(360, S1, "The peripheral zone of the prostate has:", "Long, branched glands", ["Short, unbranched glands", "Only smooth muscle", "No epithelium"])
q(360, S1, "The most common zone involved in prostate cancer is the:", "Peripheral zone", ["Transitional zone", "Central zone", "Fibromuscular zone"])
q(360, S1, "The most common zone involved in benign prostatic hypertrophy (BPH) is the:", "Transitional zone", ["Peripheral zone", "Central zone", "Fibromuscular zone"])
q(360, S1, "A zone of the prostate listed is the:", "Fibromuscular zone", ["Fibroelastic lung zone", "Muscularis mucosa zone", "Serosal zone"])
q(360, S1, "The urethra distal to the prostate shown in the diagram is the:", "Penile urethra", ["Prostatic urethra", "Preliminary urethra", "Pelvic ureter"])
q(360, S1, "In the TURP anatomy diagram, the structure above the bladder neck is the:", "Bladder", ["Prostate", "Veru montanum", "Internal sphincter"])
q(360, S1, "The junction between bladder and prostate is the:", "Bladder neck", ["Veru montanum", "External meatus", "Trigone of the neck"])
q(360, S1, "The landmark labelled in the prostatic urethra on TURP anatomy is the:", "Veru montanum", ["Bladder dome", "Ureteric orifice", "Cowper gland"])
q(360, S1, "The sphincter at the bladder outlet shown in TURP anatomy is the:", "Internal sphincter", ["External anal sphincter", "Pyloric sphincter", "Lower oesophageal sphincter"])
q(360, S1, "Veru montanum is the distal limit of resection during TURP to prevent:", "Incontinence", ["Retrograde ejaculation", "Impotence", "Haematuria"])
q(360, S1, "Injury to the bladder neck during TURP causes:", "Retrograde ejaculation", ["Stress incontinence", "Impotence", "Meatal stenosis"])
q(360, S1, "The most common complication of TURP is:", "Retrograde ejaculation", ["Incontinence", "Stricture", "TURP syndrome"])
q(360, S1, "The neurovascular bundle lies:", "Posterolateral to prostate", ["Anteromedial to prostate", "Inside the bladder", "Within the rectum"])
q(360, S1, "Injury to the neurovascular bundle causes:", "Impotence", ["Incontinence", "Retrograde ejaculation", "Haematuria"])
q(360, S1, "The fascia labelled near the neurovascular bundle is:", "Denonvilliers fascia", ["Buck fascia", "Colles fascia", "Scarpa fascia"])
q(360, S1, "The plane labelled near the neurovascular bundle is the:", "Holy plane", ["Sacred cavity", "Pelvic brim", "Pouch of Douglas"])

# ------------------------------------------------------------------ p361
S2 = "Prostatic Capsules, Corpora Amylacea and Stones"
q(361, S2, "Bleed during TURP if the capsule is invaded comes from the:", "Prostatic venous plexus", ["Prostatic artery only", "Vesical artery", "Obturator vein"])
q(361, S2, "The prostatic venous plexus carries metastases to the:", "Bones/vertebral column", ["Lungs only", "Liver only", "Brain only"])
q(361, S2, "The outer capsule in the prostate capsule diagram is the:", "False capsule", ["True capsule", "Renal capsule", "Glisson capsule"])
q(361, S2, "The layer between the false and true capsules is the:", "Prostatic venous plexus", ["Neurovascular bundle", "Ejaculatory duct", "Urethral sphincter"])
q(361, S2, "The inner capsule in the prostate capsule diagram is the:", "True capsule", ["False capsule", "Hepatic capsule", "Splenic capsule"])
q(361, S2, "Corpora amylacea is the precursor lesion for:", "Prostatic stones", ["Prostate cancer", "BPH", "Prostatitis"])
q(361, S2, "Corpora amylacea shows:", "Eosinophilic lamellated bodies", ["Basophilic crystals", "Psammoma bodies", "Coffin-lid crystals"])
q(361, S2, "Endogenous prostatic stones form:", "In the prostate", ["In the kidney", "In the bladder only", "In the ureter only"])
q(361, S2, "Endogenous prostatic stones account for:", "20%", ["2%", "80%", "100%"])
q(361, S2, "The most common composition of prostatic stones is:", "CaPO4", ["Calcium oxalate", "Uric acid", "Cystine"])
q(361, S2, "Endogenous prostatic stones are diagnosed:", "Incidentally", ["Always with retention", "Only on biopsy", "Only after TURP"])
q(361, S2, "Management of endogenous prostatic stones is:", "Mx not required", ["Immediate TURP", "Radical prostatectomy", "Long antibiotics"])
q(361, S2, "Exogenous prostatic stones are formed:", "Elsewhere (Eg: Kidney)", ["In the prostate", "In the seminal vesicle only", "In the vas deferens"])
q(361, S2, "Management of exogenous prostatic stones is:", "Mx not required", ["Emergency surgery", "Radiotherapy", "Hormonal therapy"])

S3 = "Acute versus Chronic Prostatitis"
q(361, S3, "The most common organism causing acute prostatitis is:", "E coli", ["Proteus", "Klebsiella", "Pseudomonas"])
q(361, S3, "Acute prostatitis is secondary to:", "UTI", ["Pneumonia", "Meningitis", "Cellulitis"])
q(361, S3, "Chronic prostatitis follows:", "Multiple episodes of acute prostatitis", ["A single UTI only", "BPH surgery", "Vasectomy"])
q(361, S3, "A clinical feature of acute prostatitis is:", "Fever", ["Hypothermia", "Jaundice", "Haemoptysis"])
q(361, S3, "Acute prostatitis presents with:", "Pain", ["Painless lump", "Itching only", "Numbness"])
q(361, S3, "Chronic prostatitis presents with:", "Dull perineal pain (Prostatodynia)", ["High fever with rigors", "Acute retention only", "Gross haematuria in every case"])
q(361, S3, "Digital rectal examination in acute prostatitis shows a:", "Tender, boggy prostate", ["Hard fixed prostate", "Rubbery mobile prostate", "Normal prostate"])
q(361, S3, "Digital rectal examination in chronic prostatitis shows a:", "Tender prostate", ["Boggy prostate", "Hard fixed prostate", "Rubbery mobile prostate"])
q(361, S3, "Urine microscopy in acute prostatitis shows:", "Threads and neutrophils", ["Red cell casts", "Coffin-lid crystals", "Fatty casts"])
q(361, S3, "In acute prostatitis, prostatic massage is:", "Contraindicated", ["Mandatory", "The first test", "Done daily"])
q(361, S3, "The investigation for chronic prostatitis is the:", "3 tube test", ["Single urine culture only", "PSA alone", "Plain X-ray"])
q(361, S3, "Acute prostatitis is treated with antibiotics for:", "2–3 weeks", ["4–6 weeks", "2–3 days", "6 months"])
q(361, S3, "Chronic prostatitis is treated with antibiotics for:", "4–6 weeks", ["2–3 weeks", "2–3 days", "1 year"])

# ------------------------------------------------------------------ p362
S4 = "Three-Tube Test and Lower Urinary Tract Symptoms"
q(362, S4, "VB1 in the 3 tube test is:", "First voided 10 ml", ["Mid-stream culture", "Prostatic secretions", "First voided after massage"])
q(362, S4, "VB1 samples the:", "Urethra", ["Bladder", "Prostate", "Kidney"])
q(362, S4, "VB2 in the 3 tube test is:", "Mid-stream culture", ["First voided 10 ml", "Prostatic secretions", "Void after massage"])
q(362, S4, "VB2 is collected:", "200 ml later", ["Immediately after VB1", "After prostate massage", "After 24 hours"])
q(362, S4, "VB2 samples the:", "Bladder", ["Urethra", "Prostate", "Ureter"])
q(362, S4, "EPS in the 3 tube test stands for:", "Prostatic secretions", ["Early prostate serum", "External pelvic swab", "Empty bladder sample"])
q(362, S4, "EPS is collected after:", "Prostate massage", ["Bladder wash", "Urethral swab", "Blood culture"])
q(362, S4, "EPS samples the:", "Prostate", ["Urethra", "Bladder", "Testis"])
q(362, S4, "VB3 in the 3 tube test is:", "First voided 10 ml after massage", ["First voided before massage", "Mid-stream culture", "24-hour urine"])
q(362, S4, "VB3 is collected after:", "Void following prostate massage", ["Sleep", "Exercise", "Antibiotics"])
q(362, S4, "All 3-tube test samples are:", "Sent for culture", ["Discarded", "Sent for cytology only", "Kept for a week"])
q(362, S4, "Both BPH and prostate cancer present with:", "Lower urinary tract symptoms (LUTS)", ["Upper GI bleeding", "Chest pain", "Headache"])
q(362, S4, "Hesitancy is a:", "Voiding (Obstructive) symptom", ["Storage (Irritative) symptom", "Post-mictural symptom only", "Constitutional symptom"])
q(362, S4, "Hesitancy is worse with:", "A full bladder", ["An empty bladder", "Exercise", "Fasting"])
q(362, S4, "Poor flow in LUTS is:", "Not improved by straining", ["Improved by straining", "Improved by fasting", "Relieved by lying down"])
q(362, S4, "Intermittent stream means urine:", "Stops and starts", ["Flows continuously", "Is bloody always", "Is milky"])
q(362, S4, "Dribbling includes dribbling:", "After micturition", ["Before puberty", "Only at night", "Only during fever"])
q(362, S4, "A voiding symptom is:", "Sensation of poor bladder emptying", ["Frequency", "Urgency", "Nocturia"])
q(362, S4, "Episodes of near retention are:", "Voiding symptoms", ["Storage symptoms", "Systemic symptoms", "Normal findings"])
q(362, S4, "Frequency is a:", "Storage (Irritative) symptom", ["Voiding symptom", "Post-mictural symptom", "Pain symptom"])
q(362, S4, "The most common and earliest LUTS is:", "Frequency", ["Nocturia", "Urgency", "Dribbling"])
q(362, S4, "A storage symptom is:", "Nocturia", ["Hesitancy", "Poor flow", "Intermittent stream"])
q(362, S4, "A storage symptom is:", "Urgency", ["Dribbling", "Poor emptying", "Near retention"])
q(362, S4, "A storage symptom is:", "Urge incontinence", ["Hesitancy", "Poor flow", "Dribbling"])
q(362, S4, "Nocturnal incontinence is also called:", "Enuresis", ["Encopresis", "Epistaxis", "Haemoptysis"])
q(362, S4, "In BPH, post mictural LUTS like dribbling and incomplete emptying:", "Aren't corrected even post TURP", ["Always resolve post TURP", "Never occur", "Occur only after TURP"])
q(362, S4, "The prostate cancer diagram shows a normal prostate with:", "Normal urethra", ["Compressed urethra", "Enlarged prostate", "Diverticulum"])
q(362, S4, "The BPH diagram shows an enlarged prostate with:", "Compressed urethra", ["Normal urethra", "Normal prostate", "Ureterocele"])

# ------------------------------------------------------------------ p362-364
S5 = "Workup: Examination, USG, PSA and Biopsy"
q(362, S5, "On digital rectal examination, BPH feels:", "Rubbery", ["Hard", "Stony", "Boggy"])
q(362, S5, "In BPH the rectal mucosa is:", "Mobile", ["Fixed", "Ulcerated", "Absent"])
q(362, S5, "On digital rectal examination, prostate cancer feels:", "Hard", ["Rubbery", "Boggy", "Soft"])
q(362, S5, "In prostate cancer the rectal mucosa is:", "Fixed", ["Mobile", "Normal in every case", "Transilluminant"])
q(362, S5, "Urine examination includes:", "Urine routine and microscopy", ["Stool routine only", "Sputum cytology", "CSF analysis"])
q(362, S5, "Urine examination includes:", "Urine culture and sensitivity", ["Blood culture only", "Throat swab", "Skin biopsy"])
q(362, S5, "Urine examination includes testing:", "Urine glucose", ["Urine ketones only", "Urine pregnancy", "Urine osmolality only"])
q(363, S5, "USG KUB assesses:", "Prostatic size", ["Liver span", "Spleen size", "Thyroid volume"])
q(363, S5, "USG KUB assesses:", "Prostatic volume", ["Renal artery flow only", "Bladder stone colour", "Urethral length only"])
q(363, S5, "USG KUB measures:", "Residual urine", ["Serum PSA", "Urine glucose", "Bladder pressure"])
q(363, S5, "USG KUB assesses:", "LN status", ["Bone density", "Lung nodules", "Brain mets"])
q(363, S5, "USG KUB looks for:", "Hydronephrosis", ["Hydrocele", "Hydatid cyst", "Hydrocephalus"])
q(363, S5, "Free PSA is:", "Better than protein bound PSA", ["Worse than bound PSA", "Equal to bound PSA", "Never measured"])
q(363, S5, "PSA velocity suspecting malignancy is:", ">0.75 ng/ml/year", ["<0.25 ng/ml/year", ">7.5 ng/ml/day", "<0.075 ng/ml/year"])
q(363, S5, "BPSA (Nicked) and IPSA (Intact) are raised in:", "Benign prostatic conditions", ["Prostate cancer", "Bladder cancer", "Renal cancer"])
q(363, S5, "Pro PSA is raised in:", "Cancer", ["Benign conditions", "UTI only", "Normal prostate"])
q(363, S5, "PSA evaluation is done at:", "50 to 69 years", ["20 to 30 years", "80 to 90 years", "Birth"])
q(363, S5, "PSA 0–3 ng/ml is:", "Normal", ["Highly malignant", "Always prostatitis", "Always BPH"])
q(363, S5, "PSA 0–3 ng/ml differentials include:", "BPH and Prostatitis", ["Cancer in every case", "Bladder stone", "Urethral stricture"])
q(363, S5, "With PSA 0–3 ng/ml, confirm diagnosis by ruling out prostatitis then:", "Start patient on BPH mx (Biopsy not required)", ["Immediate TRUS biopsy", "Radical prostatectomy", "Radiotherapy"])
q(363, S5, "PSA >3–4 ng/ml differentials include:", "BPH, Cancer and Prostatitis", ["Only normal prostate", "Only bladder cancer", "Only renal stones"])
q(363, S5, "With PSA >3–4 ng/ml, if prostatitis is present give:", "Antibiotics 4–6 weeks", ["Antibiotics 2–3 days", "Immediate surgery", "No treatment"])
q(363, S5, "After antibiotics for prostatitis, repeat PSA after:", "6 weeks", ["6 days", "6 months", "1 year"])
q(363, S5, "On repeat after treatment, PSA becomes:", "Normal", ["Higher always", "Undetectable always", "Unchanged"])
q(363, S5, "With PSA >3–4 ng/ml and no prostatitis, do:", "TRUS guided trucut biopsy", ["Only observation", "Empirical TURP", "Cystectomy"])
q(363, S5, "Minimum cores to be taken on prostate biopsy:", "12 cores", ["2 cores", "6 cores", "24 cores"])
q(363, S5, "Transperineal biopsy samples the:", "Anterior lobe", ["Posterior lobe", "Median lobe only", "Lateral lobe only"])
q(363, S5, "Transperineal biopsy is done under:", "GA", ["LA", "No anaesthesia", "Spinal only"])
q(363, S5, "Transperineal biopsy has:", "Decreased risk of infection", ["Increased risk of infection", "No infection risk difference", "100% infection"])
q(363, S5, "Transperineal biopsy is done if:", "Raised PSA but TRUS biopsy negative", ["PSA is normal", "DRE is normal", "Patient refuses consent"])
q(363, S5, "Transrectal biopsy samples the:", "Posterior lobe", ["Anterior lobe", "Whole gland equally", "Seminal vesicle only"])
q(363, S5, "Transrectal biopsy is done under:", "LA", ["GA", "No anaesthesia", "Epidural only"])
q(363, S5, "Transrectal biopsy has:", "Increased risk of infection", ["Decreased risk of infection", "No risk at all", "Only bleeding risk"])
q(363, S5, "Uroflowmetry >15 ml/sec is:", "Normal", ["Equivocal", "Low", "High"])
q(363, S5, "Uroflowmetry 10–15 ml/sec is:", "Equivocal", ["Normal", "Low", "High"])
q(363, S5, "Uroflowmetry <10 ml/sec is:", "Low", ["Normal", "Equivocal", "High"])
q(363, S5, "Bladder pressure <60 cm of H2O is:", "Normal", ["Equivocal", "High", "Low"])
q(363, S5, "Bladder pressure 60–80 cm of H2O is:", "Equivocal", ["Normal", "High", "Low"])
q(363, S5, "Bladder pressure >80 cm of H2O is:", "High", ["Normal", "Equivocal", "Low"])

# ------------------------------------------------------------------ p364
S6 = "Neurogenic Bladder, Marion Disease and BPH Basics"
q(364, S6, "In bladder outlet obstruction, bladder pressure is:", "Increased", ["Decreased markedly", "Normal always", "Absent"])
q(364, S6, "In bladder outlet obstruction, flow rate is:", "Decreased", ["Increased", "Normal always", "Absent"])
q(364, S6, "In neurogenic bladder, bladder pressure is:", "Markedly decreased", ["Increased", "Normal always", "High"])
q(364, S6, "In neurogenic bladder, flow rate is:", "Decreased", ["Increased", "Normal always", "High"])
q(364, S6, "Marion disease occurs due to hypertrophy of the:", "Internal sphincter", ["External sphincter", "Detrusor only", "Prostate"])
q(364, S6, "Marion disease has:", "LUTS positive but no BPH/cancer", ["No LUTS", "BPH in every case", "Cancer in every case"])
q(364, S6, "BPH occurs in the:", "5th decade", ["2nd decade", "8th decade", "Neonatal period"])
q(364, S6, "BPH affects the:", "Transitional zone", ["Peripheral zone", "Central zone", "Fibromuscular zone"])
q(364, S6, "In BPH the prostatic urethral lumen is:", "Decreased, causing LUTS features", ["Increased", "Normal", "Absent"])
q(364, S6, "In BPH the prostatic urethral curve is:", "Increased, causing difficult catheterisation", ["Decreased", "Normal", "Absent"])
q(364, S6, "Obstruction in BPH raises pressure in the bladder causing:", "Diverticulae, trabeculae and increased residual urine", ["Decreased residual urine", "Bladder rupture in every case", "Normal bladder always"])
q(364, S6, "International prostate symptom score 0–7 is:", "Mild", ["Moderate", "Severe", "Normal"])
q(364, S6, "Mild IPSS is managed with:", "Observation", ["Medical or surgery", "Immediate TURP", "Radiotherapy"])
q(364, S6, "International prostate symptom score 8–19 is:", "Moderate", ["Mild", "Severe", "Normal"])
q(364, S6, "Moderate IPSS is managed with:", "Medical or surgery", ["Observation only", "No treatment", "Only radiotherapy"])
q(364, S6, "International prostate symptom score 20–25 is:", "Severe", ["Mild", "Moderate", "Normal"])
q(364, S6, "Severe IPSS is managed with:", "Medical or surgery", ["Observation only", "No treatment", "Only antibiotics"])
q(364, S6, "The static component of BPH is:", "Increase in prostate bulk", ["Increase in smooth muscle tone", "Decrease in stroma", "Bladder neck relaxation"])
q(364, S6, "The static component is stromal hyperplasia due to:", "5DHT", ["Testosterone only", "Oestrogen only", "PSA"])
q(364, S6, "The dynamic component of BPH is:", "Increase in smooth muscle tone", ["Increase in prostate bulk", "Stromal hyperplasia", "Glandular atrophy"])
q(364, S6, "The dynamic component is mediated by:", "Alpha adrenergic receptors", ["Beta receptors only", "Muscarinic receptors", "Dopamine receptors"])

# ------------------------------------------------------------------ units
def first_page(title):
    return next(x["page"] for x in Q if x["sec"] == title)

UNIT_DEFS = [
    (S1, "Central zone glands are short and unbranched while peripheral glands are long and branched, with cancer favouring the periphery and BPH the transition zone around the prostatic urethra. Veru montanum marks the distal TURP limit that protects continence, bladder-neck injury causes retrograde ejaculation as the commonest TURP complication, and the posterolateral neurovascular bundle in the holy plane near Denonvilliers fascia threatens impotence when injured."),
    (S2, "Between true and false capsules lies the prostatic venous plexus, which bleeds if the capsule is breached and carries metastases to bone and vertebrae. Corpora amylacea are eosinophilic lamellated precursors of stones; endogenous CaPO4 stones arise in the prostate in a fifth of cases while exogenous stones arrive from the kidney, both usually incidental and needing no treatment."),
    (S3, "Acute prostatitis is an E. coli UTI complication with fever, pain and a tender boggy prostate showing threads and neutrophils, where massage is forbidden and 2–3 weeks of antibiotics suffice. Chronic disease follows repeated acute attacks with dull prostadynia and a tender gland, diagnosed by the 3-tube test and treated for 4–6 weeks."),
    (S4, "VB1 samples urethral first-void, VB2 bladder midstream 200 ml later, EPS prostatic secretions after massage and VB3 post-massage first-void, all cultured to localize infection. BPH and cancer both cause LUTS: obstructive hesitancy, poor unimproved flow, intermittent stream, post-void dribbling, poor emptying and near-retention, plus irritative frequency as the earliest commonest symptom with nocturia, urgency, urge and nocturnal enuresis; BPH post-micturition dribbling may persist even after TURP."),
    (S5, "BPH feels rubbery with mobile mucosa while cancer feels hard with fixed mucosa, followed by urine routine, culture and glucose, then USG KUB for size, volume, residual urine, nodes and hydronephrosis. Free PSA beats bound PSA, velocity above 0.75 ng/ml/year alarms, BPSA/IPSA mark benign disease and proPSA marks cancer; at 50–69 years low PSA avoids biopsy while high PSA is triaged through prostatitis treatment and repeat testing to TRUS trucut biopsy of at least 12 cores, choosing transperineal anterior under GA for lower infection after negative TRUS versus transrectal posterior under LA, and grading flow above 15 as normal, 10–15 equivocal and below 10 low against bladder pressures below 60 normal, 60–80 equivocal and above 80 high."),
    (S6, "Outlet obstruction raises bladder pressure with low flow while neurogenic bladder drops pressure markedly with low flow, and Marion disease from internal-sphincter hypertrophy mimics LUTS without BPH or cancer. Fifth-decade transitional-zone BPH narrows the lumen to cause LUTS and steepens the curve to hinder catheterisation, backing pressure into diverticulae, trabeculae and residual urine; IPSS grades 0–7 mild for observation and 8–25 moderate-severe for medical or surgical care, splitting disease into a 5DHT static bulk component and an alpha-mediated dynamic tone component."),
]

UNITS = []
for i, (title, guide) in enumerate(UNIT_DEFS, 1):
    UNITS.append({
        "id": f"SURG-U47-{i}",
        "ch": 47,
        "n": i,
        "title": title,
        "sec": f"{title} · p{first_page(title)}",
        "qs": [x["id"] for x in Q if x["sec"] == title],
        "guide": guide,
    })

covered = [x for u in UNITS for x in u["qs"]]
assert covered == [x["id"] for x in Q]
assert len(set(covered)) == len(covered)
with open("data/ch47.json", "w", encoding="utf-8") as f:
    json.dump({"questions": Q, "units": UNITS}, f, ensure_ascii=False, indent=1)
print(f"ch47: {len(Q)} questions, {len(UNITS)} units")
