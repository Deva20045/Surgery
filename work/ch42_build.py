#!/usr/bin/env python3
"""Build data/ch42.json — Testicular Disorders: Part 2 (Marrow Surgery Ed 8, pp313-317)."""
import json

Q = []


def q(page, sec, text, correct, wrongs, pos=0, note=None):
    opts = list(wrongs)
    opts.insert(pos, correct)
    Q.append({
        "id": f"SURG-C42-{len(Q)+1:03d}", "sec": sec, "page": page,
        "q": text, "opts": opts, "ans": pos,
        "exp": (note or correct) + f" (Book p{page})",
    })


# ------------------------------------------------------------------ p313
S1 = "Varicocele"
q(313, S1, "A varicocele is a:", "Dilated, tortuous pampiniform venous plexus", ["Dilated lymphatic plexus", "Torsed spermatic cord", "Cyst of the epididymal head"], 0, "Varicocele is dilatation and tortuosity of the pampiniform plexus of veins.")
q(313, S1, "Varicocele is one of the most common causes of:", "Male infertility", ["Female infertility", "Hydronephrosis", "Penile fracture"], 0, "Varicocele is one of the common causes of male infertility.")
q(313, S1, "The countercurrent mechanism is lost in varicocele, causing:", "Increased temperature and decreased spermatogenesis", ["Decreased temperature and increased spermatogenesis", "Increased testosterone only", "No effect on sperm production"], 0, "Loss of countercurrent cooling raises temperature and reduces spermatogenesis.")
q(313, S1, "Varicocele is more common on the:", "Left side", ["Right side", "Right in every child", "Side with the shorter vein"], 0, "Varicocele is left-sided more often than right-sided.")
q(313, S1, "The left testicular vein is a risk factor for left varicocele because it is:", "Longer", ["Shorter", "Absent", "Connected directly to the portal vein"], 0, "The left testicular vein has a longer course.")
q(313, S1, "The left testicular vein opens into the left renal vein at approximately:", "90 degrees", ["10 degrees", "45 degrees", "180 degrees"], 0, "The left testicular vein opens at 90 degrees into the left renal vein.")
q(313, S1, "A loaded sigmoid colon can contribute to left varicocele by:", "Pressing on the left testicular vein", ["Compressing the right renal artery", "Occluding the portal vein", "Torsing the epididymis"], 0, "A loaded sigmoid can press on the left testicular vein.")
q(313, S1, "The left adrenal vein opens opposite the left testicular vein and may cause:", "Vasoconstriction from increased adrenaline and noradrenaline", ["Bile reflux", "Lymphatic obstruction", "Decreased catecholamine release"], 0, "The opposite adrenal-vein opening is associated with catecholamine-mediated vasoconstriction.")
q(313, S1, "A left renal vein blocked by spread of renal-cell carcinoma causes:", "Secondary varicocele", ["Primary hydrocele", "Epididymo-orchitis", "Testicular torsion"], 0, "Left renal-vein obstruction from RCC causes secondary varicocele.")
q(313, S1, "A common symptom of varicocele is:", "A dull, dragging pain", ["Severe acute pain", "Pain only during ejaculation", "Painless jaundice"], 0, "Varicocele may cause dull, dragging pain.")
q(313, S1, "Varicocele may be:", "Asymptomatic", ["Always painful", "Always associated with fever", "Always associated with haematuria"], 0, "Varicocele can be asymptomatic.")
q(313, S1, "A typical clinical sign of varicocele is a:", "Bag of worms", ["Pyriform gallbladder", "Cannonball chest", "Transverse testis"], 0, "The scrotal swelling of varicocele has a bag-of-worms feel.")
q(313, S1, "On examination of varicocele, getting above the swelling is:", "Possible", ["Impossible in every case", "Possible only in a hydrocele", "Not relevant"], 0, "Getting above a varicocele swelling is positive.")
q(313, S1, "The investigation of choice for varicocele is:", "Doppler", ["Barium meal", "HIDA scan", "Plain skull radiography"], 0, "Doppler is the investigation of choice.")
q(313, S1, "Grade I varicocele is:", "Impalpable but detected on Doppler", ["Palpable and visible", "Visible but not detected on Doppler", "Always associated with infertility"], 0, "Grade I is impalpable and detected on Doppler.")
q(313, S1, "Grade II varicocele is:", "Palpable and detected on Doppler", ["Impalpable and Doppler negative", "Visible without palpation", "Only seen during surgery"], 0, "Grade II is palpable and detected on Doppler.")
q(313, S1, "Grade III varicocele is:", "Visible", ["Detected only on Doppler", "Never palpable", "Only visible on CT"], 0, "Grade III varicocele is visible.")
q(313, S1, "Varicocele treatment is indicated:", "Only if symptomatic", ["In every asymptomatic patient", "Only after testicular torsion", "Only if the patient has hydrocele"], 0, "The chapter recommends treatment only if symptomatic.")
q(313, S1, "After varicocele treatment, sperm counts improve in approximately:", "30–40%", ["5–10%", "70–80%", "100%"], 0, "Sperm counts improve in only 30–40% after treatment.")
q(313, S1, "The first-line treatment listed for varicocele is:", "Percutaneous embolisation of gonadal veins", ["Orchidectomy", "Hydrocelectomy", "Antibiotics alone"], 0, "First-line treatment is percutaneous embolisation of the gonadal veins.")
q(313, S1, "The most effective method for treating varicocele is:", "Microsurgical varicocelectomy", ["Simple scrotal aspiration", "Dorsal slit", "Radiotherapy"], 0, "Microsurgical varicocelectomy is listed as the most effective method.")
q(313, S1, "Recurrence after varicocele treatment is related to:", "Dual blood supply", ["A single arterial supply", "A patent processus vaginalis", "The absence of lymphatics"], 0, "Recurrence is due to dual blood supply and is managed by surgical ligation.")

# ------------------------------------------------------------------ p314
S2 = "Fournier's Gangrene"
q(314, S2, "Fournier's gangrene is:", "Necrotising fasciitis of the perineal region", ["A superficial scrotal sebaceous cyst", "A testicular tumour", "A non-infective hydrocele"], 0, "Fournier's gangrene is necrotising fasciitis involving the perineum.")
q(314, S2, "The infection in Fournier's gangrene is typically:", "Synergistic aerobic and anaerobic infection", ["A purely viral infection", "A sterile inflammatory reaction", "Only a fungal infection"], 0, "Fournier's is described as synergistic gangrene due to aerobic plus anaerobic infection.")
q(314, S2, "Fournier's gangrene is common in:", "Immunocompromised patients", ["Only healthy athletes", "Only neonates", "Only patients with hydrocele"], 0, "Immunocompromised patients are commonly affected.")
q(314, S2, "A specifically listed risk group for Fournier's gangrene is:", "Patients with diabetes", ["Patients with isolated myopia", "Patients with varicocele only", "Patients with a spermatocele"], 0, "Diabetes is listed among the epidemiological associations.")
q(314, S2, "Fournier's gangrene may follow:", "Trivial trauma", ["Only major abdominal surgery", "A normal ultrasound", "A healed hydrocele"], 0, "The chapter notes that Fournier's may follow trivial trauma.")
q(314, S2, "Fournier's gangrene has:", "High mortality", ["No mortality", "Only cosmetic consequences", "A uniformly benign course"], 0, "Fournier's gangrene has high mortality.")
q(314, S2, "Clinical symptoms of Fournier's gangrene include:", "Fever, pain and swelling", ["Painless jaundice only", "Haematemesis and melena", "Only urinary frequency"], 0, "Fever, pain and swelling are listed symptoms.")
q(314, S2, "A characteristic sign of Fournier's gangrene is:", "Foul-smelling discharge", ["Clear transilluminant fluid", "A bag of worms", "A painless firm testis"], 0, "Foul-smelling discharge is a listed sign.")
q(314, S2, "Sepsis in Fournier's gangrene is suggested by:", "Fever, tachycardia and hypotension", ["Bradycardia and hypertension", "Only microscopic haematuria", "Normal vital signs"], 0, "Sepsis is described by fever, tachycardia and hypotension.")
q(314, S2, "Crepitus in Fournier's gangrene:", "May be present", ["Is always absent", "Confirms a hydrocele", "Occurs only in varicocele"], 0, "Crepitus may be present in Fournier's gangrene.")
q(314, S2, "The most important component of Fournier's management is:", "Aggressive debridement", ["Observation", "Scrotal aspiration", "Delayed radiotherapy"], 0, "Aggressive debridement is the most important treatment.")
q(314, S2, "Supportive management of Fournier's gangrene includes:", "Intravenous fluids and intravenous antibiotics", ["Only oral vitamins", "Only chemotherapy", "No antimicrobial therapy"], 0, "Management includes IV fluids and IV antibiotics.")
q(314, S2, "During debridement for Fournier's gangrene, the testis and urethra are:", "Spared irrespective of severity", ["Always excised", "Removed if there is any fever", "Replaced by prostheses"], 0, "Testis and urethra are spared because of their dual blood supply.")
q(314, S2, "A recent update listed for Fournier's gangrene is:", "Hyperbaric oxygen therapy", ["Brachytherapy", "Percutaneous nephrolithotomy", "Radioiodine"], 0, "Hyperbaric oxygen therapy is noted as a recent update.")

# ------------------------------------------------------------------ p314-315
S3 = "Testicular Tumours: Classification, Presentation and Workup"
q(314, S3, "Approximately what proportion of testicular tumours are germ-cell tumours?", "95%", ["5%", "25%", "50%"], 0, "Germ-cell tumours comprise about 95% of testicular tumours.")
q(314, S3, "Sex-cord/stromal tumours comprise approximately:", "5% of testicular tumours", ["95%", "50%", "75%"], 0, "Sex-cord/stromal tumours comprise about 5%.")
q(314, S3, "The most common overall germ-cell tumour is:", "Seminoma", ["Choriocarcinoma", "Embryonal carcinoma", "Yolk-sac tumour"], 0, "Seminoma is the most common overall germ-cell tumour.")
q(314, S3, "Which is a non-seminomatous germ-cell tumour?", "Choriocarcinoma", ["Leydig-cell tumour", "Sertoli-cell tumour", "Seminoma"], 0, "Non-seminomatous tumours include choriocarcinoma, embryonal carcinoma, teratoma and yolk-sac tumour.")
q(314, S3, "The most common testicular tumour in children is:", "Yolk-sac tumour", ["Seminoma", "Sertoli-cell tumour", "Lymphoma"], 0, "Yolk-sac tumour is the commonest testicular tumour in children.")
q(314, S3, "The sex-cord/stromal tumour types listed are:", "Leydig-cell and Sertoli-cell tumours", ["Seminoma and teratoma", "Choriocarcinoma and yolk-sac tumour", "Lymphoma and embryonal carcinoma"], 0, "Sex-cord/stromal tumours listed are Leydig-cell and Sertoli-cell tumours.")
q(314, S3, "Lymphoma is the most common testicular tumour in:", "The elderly", ["Young children", "The second decade only", "Patients with hydrocele"], 0, "Lymphoma is the commonest testicular tumour in the elderly.")
q(314, S3, "Lymphoma is the most common bilateral testicular tumour in approximately:", "10–15% of cases", ["1–2%", "50–60%", "90%"], 0, "Lymphoma is the commonest bilateral testicular tumour in 10–15% of cases.")
q(315, S3, "The most common presentation of a testicular tumour is a:", "Painless testicular mass", ["Painful scrotal ulcer", "Fever with crepitus", "Hydrocele that always transilluminates"], 0, "The common presentation is a painless testicular mass with loss of testicular sensation.")
q(315, S3, "A testicular tumour may cause an abdominal lump because of involvement of:", "Para-aortic lymph nodes", ["Superficial inguinal nodes only", "Mesenteric nodes only", "Cervical nodes only"], 0, "Abdominal lumps result from para-aortic lymph-node involvement.")
q(315, S3, "The most common site of distant metastasis from a testicular tumour is the:", "Lung", ["Brain", "Bone", "Skin"], 0, "The lung is the most common site of distant metastasis.")
q(315, S3, "Cannonball lung metastases are an atypical presentation of:", "Testicular tumour", ["Hydrocele", "Varicocele", "Phimosis"], 0, "Cannonball lung metastases are listed as an atypical presentation.")
q(315, S3, "Leydig-cell tumours may cause:", "Masculinisation, precocious puberty and gynaecomastia", ["Feminisation only", "Only infertility without endocrine effects", "Hypoglycaemia and jaundice"], 0, "Leydig-cell tumours cause masculinisation, precocious puberty and gynaecomastia.")
q(315, S3, "Sertoli-cell tumours may cause:", "Feminisation and gynaecomastia", ["Masculinisation only", "Cannonball lung metastases only", "Renal colic"], 0, "Sertoli-cell tumours cause feminisation and gynaecomastia.")
q(315, S3, "The term hurricane tumour refers to aggressive:", "Choriocarcinoma", ["Seminoma", "Sertoli-cell tumour", "Yolk-sac tumour"], 0, "Hurricane tumour is aggressive choriocarcinoma.")
q(315, S3, "The average survival in the hurricane tumour described is:", "About 6 months", ["About 6 days", "About 6 years", "Normal life expectancy"], 0, "The listed average survival for hurricane tumour is about six months.")
q(315, S3, "After a scrotal mass is found on ultrasound, the next workup step is:", "Tumour markers AFP, beta-hCG and LDH", ["Immediate trans-scrotal biopsy", "Only urine culture", "Only serum amylase"], 0, "The workup proceeds from scrotal USG to AFP, beta-hCG and LDH tumour markers.")
q(315, S3, "Confirmation of a testicular tumour is by:", "Histopathology using Chevassu's manoeuvre", ["Scrotal aspiration alone", "Plain X-ray", "A HIDA scan"], 0, "Confirmation is by histopathology after Chevassu's manoeuvre.")
q(315, S3, "Staging of a testicular tumour is completed with:", "PET-CT", ["Barium meal", "Doppler of the renal artery only", "Scrotal transillumination"], 0, "PET-CT is used for staging in the depicted workup.")
q(315, S3, "Trans-scrotal biopsy or FNAC should never be done because it may cause:", "Scrotal seeding and increased tumour stage", ["Immediate renal failure", "Hydrocele resolution", "Improved prognosis"], 0, "Trans-scrotal biopsy/FNAC can seed the scrotum and increase staging.")
q(315, S3, "Chevassu's manoeuvre begins with a:", "High inguinal incision", ["Midline laparotomy", "Scrotal incision", "Perineal incision"], 0, "Chevassu's manoeuvre begins with a high inguinal incision.")
q(315, S3, "During Chevassu's manoeuvre, the testis is:", "Delivered and the cord is clamped before splitting the testis", ["Biopsied through the scrotum", "Removed before the cord is clamped", "Left in place for observation"], 0, "The testis is delivered, the cord is clamped, the testis is split and a frozen section is taken.")
q(315, S3, "If the frozen section in Chevassu's manoeuvre is positive, the operation is:", "High inguinal orchidectomy", ["Repositioning the testis", "Hydrocelectomy", "No treatment"], 0, "A positive frozen section leads to high inguinal orchidectomy.")
q(315, S3, "If the frozen section in Chevassu's manoeuvre is negative, the testis is:", "Repositioned", ["Excised in every case", "Treated with radiotherapy immediately", "Placed in the contralateral scrotum"], 0, "A negative frozen section leads to repositioning of the testis.")

# ------------------------------------------------------------------ p315-316
S4 = "Testicular Tumour Staging"
q(315, S4, "In pathological T staging, pTX means:", "The primary tumour cannot be assessed", ["No evidence of primary tumour", "Intratubular germ-cell neoplasia", "Tumour invades the scrotum"], 0, "pTX means the primary tumour cannot be assessed.")
q(315, S4, "In pathological T staging, pT0 means:", "No evidence of a primary tumour", ["Tumour limited to the testis without invasion", "Intratubular germ-cell neoplasia", "Tumour invades the spermatic cord"], 0, "pT0 means there is no evidence of a primary tumour.")
q(315, S4, "pTIS denotes:", "Intratubular germ-cell neoplasia", ["No regional nodes", "Tumour invading scrotum", "Distant metastasis"], 0, "pTIS denotes intratubular germ-cell neoplasia.")
q(315, S4, "pT1 testicular tumour is limited to the testis and epididymis without:", "Vascular or lymphatic invasion", ["Any testicular sensation", "A tunica vaginalis", "An epididymis"], 0, "pT1 is limited to testis and epididymis without vascular or lymphatic invasion.")
q(315, S4, "pT2 includes tumour limited to testis and epididymis with vascular/lymphatic invasion OR involvement of the:", "Tunica vaginalis", ["Scrotum only", "Renal pelvis", "Adrenal gland"], 0, "pT2 includes vascular/lymphatic invasion or involvement of the tunica vaginalis.")
q(315, S4, "pT3 testicular tumour invades the:", "Spermatic cord", ["Scrotal skin only", "Kidney", "Para-aortic nodes only"], 0, "pT3 invades the spermatic cord, with or without vascular/lymphatic invasion.")
q(315, S4, "pT4 testicular tumour invades the:", "Scrotum", ["Tunica vaginalis only", "Epididymal head only", "Spermatic cord only"], 0, "pT4 invades the scrotum, with or without vascular/lymphatic invasion.")
q(316, S4, "In nodal staging, NX means:", "Regional lymph nodes cannot be assessed", ["No regional lymph-node metastasis", "A nodal mass over 5 cm", "Distant lung metastasis"], 0, "NX means regional lymph nodes cannot be assessed.")
q(316, S4, "N0 means:", "No regional lymph-node metastasis", ["Regional nodes cannot be assessed", "A mass 2–5 cm", "Distant metastasis"], 0, "N0 means there is no regional lymph-node metastasis.")
q(316, S4, "N1 is a lymph-node mass of:", "2 cm or less or up to 5 positive lymph nodes", ["More than 5 cm", "2–5 cm with no positive nodes", "Any mass in the lung"], 0, "N1 is a nodal mass ≤2 cm or up to 5 positive lymph nodes.")
q(316, S4, "N2 is a lymph-node mass of:", "2–5 cm or more than 5 positive lymph nodes", ["Less than 2 cm with no nodes", "More than 5 cm only", "A mass confined to the testis"], 0, "N2 is a nodal mass 2–5 cm or more than 5 positive lymph nodes.")
q(316, S4, "N3 is a lymph-node mass:", "Greater than 5 cm", ["Less than 2 cm", "Exactly 2 cm", "Only detectable by Doppler"], 0, "N3 is a nodal mass greater than 5 cm.")
q(316, S4, "M0 means:", "No metastasis", ["Lung or non-regional-node metastasis", "Metastasis to other sites", "No primary tumour"], 0, "M0 means no metastasis.")
q(316, S4, "M1a includes metastases to the:", "Lungs or non-regional lymph nodes", ["Scrotum only", "Kidney only", "Skin only"], 0, "M1a includes lung or non-regional lymph-node metastasis.")
q(316, S4, "M1b includes metastases to:", "Other sites", ["Only the para-aortic nodes", "Only the lung", "Only the epididymis"], 0, "M1b denotes metastasis to other sites.")
q(316, S4, "S staging is based on levels of:", "LDH, hCG and AFP", ["PSA, CEA and CA-125", "Amylase, lipase and bilirubin", "Creatinine, urea and sodium"], 0, "S staging is based on LDH, hCG and AFP levels.")
q(316, S4, "Tumour markers for S staging are measured:", "7–10 days after orchidectomy", ["Immediately before any examination only", "One year after surgery", "Only before puberty"], 0, "S-stage markers are measured 7–10 days after orchidectomy.")
q(316, S4, "The reason AFP is allowed time after orchidectomy before S staging is its half-life of:", "5–6 days", ["5–6 hours", "20–30 days", "One year"], 0, "AFP has a half-life of 5–6 days, so markers are measured 7–10 days after orchidectomy.")

# ------------------------------------------------------------------ p316-317
S5 = "Seminomatous and Non-seminomatous Tumours: Management"
q(316, S5, "Seminomatous tumours are the:", "Most common testicular tumours", ["Rarest testicular tumours", "Most common sex-cord tumours only", "Most common renal tumours"], 0, "Seminomatous tumours are listed as the commonest.")
q(316, S5, "Seminomatous tumours are most often seen in the:", "Second and third decades", ["First decade only", "Sixth and seventh decades", "After 80 years only"], 0, "Seminomatous tumours commonly occur in the second and third decades.")
q(316, S5, "Compared with non-seminomatous tumours, seminomatous tumours have a:", "Better prognosis", ["Worse prognosis", "Uniformly fatal prognosis", "Prognosis unrelated to stage"], 0, "Seminomatous tumours have a better prognosis.")
q(316, S5, "Seminomatous tumours are described as:", "Large and homogeneous", ["Small and always cystic", "Multiloculated and purulent", "Diffuse renal lesions"], 0, "Seminomatous tumours are described as large and homogeneous.")
q(316, S5, "Which is a type of seminoma listed in the chapter?", "Classical seminoma", ["Yolk-sac tumour", "Leydig-cell tumour", "Choriocarcinoma"], 0, "The listed seminoma types are classical, anaplastic and spermatocytic.")
q(316, S5, "Lymphocytic infiltration in a seminomatous tumour indicates:", "Good prognosis", ["Poor prognosis", "Mandatory orchidectomy of both testes", "Non-seminomatous histology"], 0, "Lymphocytic infiltration is associated with good prognosis.")
q(316, S5, "Stage I seminoma is:", "Restricted to the testis", ["Testis plus para-aortic nodes", "Testis plus distant metastases", "Only a lung tumour"], 0, "Stage I seminoma is restricted to the testis.")
q(316, S5, "The listed treatment for stage I seminoma is:", "Single-cycle carboplatin plus radiotherapy", ["BEP plus RPLND in every patient", "Only observation without treatment", "Dactinomycin alone"], 0, "Stage I seminoma is treated with single-cycle carboplatin plus radiotherapy.")
q(316, S5, "The radiotherapy field for stage I seminoma is the:", "Inverted-Y field including para-aortic nodes", ["Whole brain field", "Pelvic-only field", "Scrotal skin field"], 0, "The inverted-Y field covers para-aortic lymph nodes.")
q(316, S5, "Stage II seminoma means:", "Testis plus para-aortic lymph nodes", ["Testis only", "Testis plus liver metastasis", "Only a para-aortic mass without testicular disease"], 0, "Stage II involves the testis and para-aortic nodes.")
q(316, S5, "The chemotherapy regimen listed for stage II seminoma is:", "BEP: bleomycin, etoposide and cisplatin", ["FOLFOX", "CHOP", "Dactinomycin only"], 0, "Stage II seminoma is treated with bleomycin, etoposide and cisplatin (BEP).")
q(316, S5, "After BEP for stage II seminoma, complete response is managed by:", "Observation", ["Immediate orchidectomy of the opposite testis", "Mandatory nephrectomy", "Only antibiotics"], 0, "A complete response is observed.")
q(316, S5, "After BEP for stage II seminoma, residual disease is managed by:", "Retroperitoneal lymph-node dissection or radiotherapy", ["Observation in every case", "Hydrocelectomy", "Dorsal slit"], 0, "Residual disease is treated with RPLND or radiotherapy.")
q(317, S5, "Stage III seminoma is:", "Testis with bulky nodes or distant metastases", ["Restricted to the testis", "Only a microscopic intratubular lesion", "A benign scrotal cyst"], 0, "Stage III is testis plus bulky lymph nodes or distant metastases.")
q(317, S5, "In stage III seminoma, aggressive treatment despite metastases:", "Increases survival", ["Has no benefit", "Always worsens survival", "Is contraindicated"], 0, "Aggressive treatment despite metastases increases survival.")
q(317, S5, "The listed stage III seminoma strategy is:", "BEP chemotherapy followed by RPLND and radiotherapy, with or without metastasectomy", ["Observation only", "Radiotherapy alone to the scrotum", "Orchidectomy without systemic treatment"], 0, "Stage III is treated with BEP followed by RPLND and RT ± metastasectomy.")
q(317, S5, "Non-seminomatous tumours are most often seen in the:", "First and second decades", ["Seventh and eighth decades", "Only after 60 years", "Only at birth"], 0, "Non-seminomatous tumours are described in the first and second decades.")
q(317, S5, "Compared with seminomatous tumours, non-seminomatous tumours have a:", "Worse prognosis", ["Better prognosis", "Identical prognosis regardless of stage", "Benign course"], 0, "Non-seminomatous tumours have a worse prognosis.")
q(317, S5, "Approximately what proportion of stage I non-seminomatous tumours have subclinical metastasis?", "50%", ["5%", "10%", "90%"], 0, "Stage I non-seminomatous tumours have subclinical metastases in about 50%.")
q(317, S5, "The listed treatment for stage I non-seminomatous tumour is:", "BEP chemotherapy", ["Carboplatin plus inverted-Y radiotherapy", "Observation only", "Dactinomycin alone"], 0, "Stage I non-seminomatous disease is treated with BEP chemotherapy.")
q(317, S5, "The listed treatment for stage II non-seminomatous tumour is:", "BEP chemotherapy, with RPLND for residual disease", ["Radiotherapy alone", "Only orchidectomy", "Lord's plication"], 0, "Stage II uses BEP; residual disease is treated with RPLND.")
q(317, S5, "The listed treatment for stage III non-seminomatous tumour is:", "BEP chemotherapy plus RPLND with or without metastasectomy", ["Observation", "Only local radiotherapy", "Hydrocelectomy"], 0, "Stage III uses BEP plus RPLND ± metastasectomy.")
q(317, S5, "The most important prognostic factor in both seminomatous and non-seminomatous tumours is:", "Tumour stage", ["Side of the tumour", "Presence of a hydrocele", "Scrotal skin colour"], 0, "Stage of tumour is the most important prognostic factor in both types.")

# ------------------------------------------------------------------ units

def first_page(title):
    return next(x["page"] for x in Q if x["sec"] == title)

UNIT_DEFS = [
    (S1, "Varicocele is a dilated pampiniform plexus and a common male-infertility problem: lost countercurrent cooling raises scrotal temperature and lowers spermatogenesis. Left-sided disease dominates because of the long right-angled left testicular vein, sigmoid pressure, the opposite adrenal-vein opening and possible renal-vein obstruction by RCC. Diagnose with Doppler, grade I–III by palpability/visibility, treat only symptomatic patients, and remember embolisation, microsurgical varicocelectomy, limited sperm-count improvement and recurrence from dual supply."),
    (S2, "Fournier's gangrene is high-mortality synergistic aerobic–anaerobic necrotising fasciitis of the perineum, especially in immunocompromised and diabetic patients. Fever, pain, swelling, foul discharge, sepsis and possible crepitus demand IV fluids, IV antibiotics and immediate aggressive debridement; spare the testis and urethra because their dual blood supply remains intact, and consider hyperbaric oxygen."),
    (S3, "Most testicular tumours are germ-cell tumours, with seminoma common overall and yolk-sac tumour common in children; the small sex-cord group includes Leydig and Sertoli tumours, while lymphoma dominates elderly and bilateral disease. Think painless mass, para-aortic abdominal lump or cannonball lung metastases, and connect Leydig to masculinisation and Sertoli to feminisation. Work from scrotal ultrasound to AFP, beta-hCG and LDH, histology by high inguinal Chevassu's manoeuvre and PET-CT; never biopsy through the scrotum."),
    (S4, "Use the pTNM table precisely: pT1 stays within testis/epididymis without vascular invasion, pT2 adds vascular invasion or tunica vaginalis, pT3 reaches spermatic cord and pT4 scrotum; N1, N2 and N3 rise by nodal size/number, while M1a is lung/non-regional nodes and M1b other sites. S staging uses LDH, hCG and AFP seven to ten days after orchidectomy, allowing for AFP's five-to-six-day half-life."),
    (S5, "Seminoma is common, younger, homogeneous and better-prognosis: stage I receives single-cycle carboplatin plus inverted-Y para-aortic radiotherapy, stage II BEP with observation after complete response or RPLND/RT for residual disease, and stage III aggressive BEP followed by RPLND/RT ± metastasectomy. Non-seminoma is younger, worse-prognosis, half of stage I has occult spread, and its stage-wise backbone is BEP with RPLND for residual or advanced disease; tumour stage remains the key prognostic factor."),
]
UNITS = []
for i, (title, guide) in enumerate(UNIT_DEFS, 1):
    UNITS.append({"id": f"SURG-U42-{i}", "ch": 42, "n": i, "title": title,
                  "sec": f"{title} · p{first_page(title)}",
                  "qs": [x["id"] for x in Q if x["sec"] == title], "guide": guide})
covered = [x for u in UNITS for x in u["qs"]]
assert covered == [x["id"] for x in Q]
assert len(set(covered)) == len(covered)
with open("data/ch42.json", "w", encoding="utf-8") as f:
    json.dump({"questions": Q, "units": UNITS}, f, ensure_ascii=False, indent=1)
print(f"ch42: {len(Q)} questions, {len(UNITS)} units")
