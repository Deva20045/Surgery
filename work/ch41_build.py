#!/usr/bin/env python3
"""Build data/ch41.json — Testicular Disorders: Part 1 (Marrow Surgery Ed 8, pp307-312)."""
import json

Q = []


def q(page, sec, text, correct, wrongs, pos=0, note=None):
    """Add a four-option question; `pos` is the correct answer's final index."""
    opts = list(wrongs)
    opts.insert(pos, correct)
    Q.append({
        "id": f"SURG-C41-{len(Q)+1:03d}",
        "sec": sec,
        "page": page,
        "q": text,
        "opts": opts,
        "ans": pos,
        "exp": (note or correct) + f" (Book p{page})",
    })


# ------------------------------------------------------------------ p307
S1 = "Surgical Anatomy, Blood Supply and Descent"
q(307, S1, "The epididymis primarily:", "Transports sperm to the vas deferens", ["Produces testosterone", "Drains lymph to the inguinal nodes", "Forms the tunica vaginalis"], 0, "The epididymis transports sperm to the vas deferens.")
q(307, S1, "The seminiferous tubules are the site of:", "Spermatogenesis", ["Testosterone storage", "Lymphatic drainage", "Hydrocele formation"], 0, "Seminiferous tubules are the site of spermatogenesis.")
q(307, S1, "The rete testis transports sperm to the:", "Epididymis", ["Prostate", "Seminal vesicle", "Urethral meatus"], 0, "The rete testis transports sperm to the epididymis.")
q(307, S1, "Accumulation of fluid in the tunica vaginalis produces:", "Hydrocele", ["Varicocele", "Spermatocele", "Epididymo-orchitis"], 0, "Fluid accumulation in the tunica vaginalis causes a hydrocele.")
q(307, S1, "The left testicular vein drains:", "At a right angle into the left renal vein", ["Directly into the inferior vena cava", "Into the right renal vein", "Into the portal vein"], 0, "The left testicular vein drains at a right angle into the left renal vein.")
q(307, S1, "The longer course of the left testicular vein contributes to the fact that:", "Left-sided varicocele is more common", ["Right-sided varicocele is more common", "Varicocele is never left-sided", "Only bilateral hydrocele occurs"], 0, "The left testicular vein has a longer course and left varicocele is more common.")
q(307, S1, "The first lymphatic basin for the left testis is the:", "Para-aortic group", ["Superficial inguinal group", "External iliac group", "Mesenteric group"], 0, "Left testicular lymphatics drain first to the para-aortic group.")
q(307, S1, "The first lymphatic basin for the right testis is the:", "Interaortocaval group", ["Para-aortic group only", "Superficial inguinal group", "Internal iliac group"], 0, "Right testicular lymphatics drain first to the interaortocaval group.")
q(307, S1, "The testis develops in the:", "Genital ridge in the retroperitoneum", ["Scrotal skin", "Anterior abdominal wall", "Pelvic peritoneum"], 0, "The testis develops in the genital ridge, which is retroperitoneal.")
q(307, S1, "Which is a trigger for descent of the testis?", "Pull of the gubernaculum", ["Contraction of the cremaster alone", "Closure of the processus vaginalis", "Obstruction of the vas deferens"], 0, "Triggers for descent include the pull of the contractile gubernaculum.")
q(307, S1, "The gubernaculum is described in the chapter as:", "Contractile tissue", ["A lymphatic channel", "A venous plexus", "A part of the tunica albuginea"], 0, "The gubernaculum is contractile tissue involved in testicular descent.")
q(307, S1, "Besides the gubernaculum, testicular descent is aided by:", "Hormonal factors and differential growth of the abdominal wall", ["Only increased intra-abdominal pressure", "Only closure of the inguinal canal", "Only contraction of the dartos muscle"], 0, "Hormonal factors and differential growth of the abdominal wall are also descent triggers.")

# ------------------------------------------------------------------ p308-309
S2 = "Undescended Testis: Pathophysiology, Workup and Management"
q(308, S2, "An undescended testis is one that:", "Is arrested along the normal path of descent", ["Has deviated from the normal path", "Has undergone torsion in the scrotum", "Is always absent"], 0, "An undescended testis is arrested along its normal path of descent.")
q(308, S2, "The most common site of arrest of an undescended testis is the:", "Inguinal canal", ["Abdominal cavity", "Superficial perineum", "Scrotal neck"], 0, "The inguinal canal is the most common site of arrest.")
q(308, S2, "Undescended testis is more common on the:", "Right side", ["Left side", "Two sides equally in every case", "Side of the dominant hand"], 0, "Right-sided undescended testis is more common because the right testis descends later.")
q(308, S2, "Bilateral undescended testes are termed:", "Cryptorchidism", ["Anorchia", "Monorchia", "Ectopic testis"], 0, "Bilateral undescended testes are called cryptorchidism.")
q(308, S2, "The testis begins its descent at approximately:", "3 months of intrauterine life", ["At birth", "6 months of intrauterine life", "9 months of intrauterine life"], 0, "The timeline shows that testicular descent begins at 3 months of intrauterine life.")
q(308, S2, "At approximately 6 months of intrauterine life, the descending testis lies in the:", "Iliac fossa", ["Scrotum", "Superficial inguinal ring", "Perineum"], 0, "At 6 months the testis lies in the iliac fossa.")
q(308, S2, "At approximately 7 months of intrauterine life, the testis lies in the:", "Inguinal canal", ["Iliac fossa", "Scrotum", "Renal fossa"], 0, "At 7 months the testis lies in the inguinal canal.")
q(308, S2, "At approximately 8 months of intrauterine life, the testis lies at the:", "Superficial ring", ["Deep ring only", "Scrotal base", "Pelvic brim"], 0, "At 8 months the testis lies at the superficial ring.")
q(308, S2, "The testis reaches the scrotum at approximately:", "9 months of intrauterine life", ["3 months", "5 months", "7 months"], 0, "The timeline shows scrotal arrival at 9 months of intrauterine life.")
q(308, S2, "A characteristic change in an undescended testis is:", "Decreased volume", ["Increased volume in every case", "Calcification of the tunica", "Immediate hydrocele"], 0, "An undescended testis has decreased volume.")
q(308, S2, "Undescended testis is associated with an increased risk of:", "Intratubular germ cell neoplasia and seminoma", ["Only Leydig-cell adenoma", "Only prostate cancer", "Only renal-cell carcinoma"], 0, "Undescended testis increases intratubular germ cell neoplasia and seminoma risk.")
q(308, S2, "In an undescended testis, which cells are affected more?", "Sertoli cells", ["Leydig cells", "Peritubular myoid cells only", "Red blood cells"], 0, "Sertoli cells are affected more in an undescended testis.")
q(308, S2, "The effect of undescended testis on Sertoli cells is:", "Reduced spermatogenesis", ["Increased spermatogenesis", "Increased testosterone secretion", "No effect on fertility"], 0, "Sertoli-cell injury causes reduced spermatogenesis.")
q(308, S2, "Leydig cells in an undescended testis are affected less, so there are usually:", "Normal secondary sexual characteristics", ["Absent secondary sexual characteristics", "Female secondary sexual characteristics", "Only adrenal sexual characteristics"], 0, "Leydig cells are affected less and secondary sexual characteristics remain normal.")
q(308, S2, "The higher the undescended testis, the:", "Greater the histological changes", ["Less the risk of histological change", "More normal the seminiferous tubules", "Lower the risk of malignancy"], 0, "Higher position is associated with more histological changes.")
q(308, S2, "Which is a listed complication of an undescended testis?", "Trauma", ["Varicose veins of the leg", "Pancreatitis", "Gallstone ileus"], 0, "Trauma is one of the listed complications of an undescended testis.")
q(308, S2, "Sterility associated with an undescended testis is particularly described in:", "Cryptorchidism", ["Retractile testis", "Hydrocele", "A simple epididymal cyst"], 0, "Sterility is described in cryptorchidism; early surgery is recommended.")
q(308, S2, "If surgery for cryptorchidism is delayed until adulthood, the patient may:", "Remain infertile", ["Always regain normal fertility", "Develop only a hydrocele", "Have guaranteed normal spermatogenesis"], 0, "When surgery is done in adulthood, infertility may persist.")
q(308, S2, "The most common associated hernia in undescended testis is:", "Indirect inguinal hernia", ["Direct inguinal hernia", "Femoral hernia", "Incisional hernia"], 0, "Indirect inguinal hernia is the commonest associated hernia, listed as about 95%.")
q(308, S2, "The most common malignancy associated with undescended testis is:", "Seminoma", ["Choriocarcinoma", "Yolk sac tumour", "Leydig-cell tumour"], 0, "Seminoma is the most common malignancy associated with an undescended testis.")
q(308, S2, "Surgery for an undescended testis is recommended before puberty mainly to:", "Reduce the risk of cancer", ["Create a hydrocele", "Prevent all epididymo-orchitis", "Increase the length of the vas deferens"], 0, "Surgery before puberty reduces the risk of cancer.")
q(308, S2, "An undescended testis is commonly reported by the:", "Mother", ["Anaesthetist", "Radiologist", "Laboratory technician"], 0, "Clinical presentation is commonly reported by the mother.")
q(308, S2, "Absent scrotal rugosities suggest:", "An undescended testis", ["A scrotal sebaceous cyst", "A spermatocele", "A normal descended testis"], 0, "Scrotal rugosities are absent in the clinical presentation of an undescended testis.")
q(308, S2, "An inguinal undescended testis is usually:", "Palpable", ["Never palpable", "Visible only on CT", "Always found in the scrotum"], 0, "An inguinal testis is palpable.")
q(308, S2, "The investigation of choice for an inguinal undescended testis is:", "Ultrasonography", ["Plain radiography", "Barium meal", "HIDA scan"], 0, "Ultrasonography is used for an inguinal testis.")
q(308, S2, "The investigation of choice for an intra-abdominal undescended testis is:", "Diagnostic laparoscopy", ["Scrotal transillumination", "Barium enema", "Cystoscopy"], 0, "Diagnostic laparoscopy is the investigation of choice for an intra-abdominal testis.")
q(308, S2, "Spontaneous descent of the testis can occur until approximately:", "5 months of age", ["2 weeks of age", "2 years of age", "Puberty"], 0, "Spontaneous descent can occur until 5 months; conservative management is used until then.")
q(308, S2, "The ideal timing of surgery for an undescended testis is:", "6–12 months of age", ["At birth in every case", "After puberty", "Only after infertility develops"], 0, "The ideal timing of surgery is 6–12 months of age.")
q(309, S2, "In bilateral undescended testis, the initial protocol uses:", "A single dose of beta-hCG", ["Long-term testosterone alone", "A single dose of FSH", "Radiotherapy"], 0, "The bilateral cryptorchidism protocol begins with a single dose of beta-hCG.")
q(309, S2, "In bilateral undescended testes, no response to beta-hCG suggests:", "Anorchia", ["A viable intra-abdominal testis", "Ectopic testis", "Retractile testis"], 0, "No response to beta-hCG in the bilateral protocol suggests anorchia.")
q(309, S2, "In bilateral cryptorchidism, a rise in testosterone with raised FSH and LH is followed by:", "Laparoscopy and exploration", ["Immediate hydrocelectomy", "Observation only", "Radiotherapy"], 0, "Raised testosterone with FSH and LH leads to laparoscopy and exploration in the protocol.")
q(309, S2, "For a unilateral undescended testis, the initial operative evaluation is:", "Laparoscopy", ["Transillumination", "Barium urethrography", "Open scrotal biopsy"], 0, "Laparoscopy is used in the unilateral undescended testis protocol.")
q(309, S2, "At laparoscopy, an intra-abdominal testis that is necrotic or rudimentary is managed by:", "Orchidectomy", ["Orchidopexy", "Observation for spontaneous descent", "Hydrocele repair"], 0, "A necrotic or rudimentary intra-abdominal testis is treated by orchidectomy.")
q(309, S2, "At laparoscopy, a viable intra-abdominal testis is managed by:", "Orchidopexy", ["Orchidectomy in every case", "Excision of the remnant", "No treatment"], 0, "A viable intra-abdominal testis is treated with orchidopexy.")
q(309, S2, "If the testicular vessels are seen exiting the deep ring, the next step is:", "Inguinal exploration", ["Immediate nephrectomy", "Scrotal aspiration", "No further evaluation"], 0, "Vessels exiting the deep ring lead to inguinal exploration.")
q(309, S2, "Blind-ending testicular vessels in the unilateral protocol suggest monorchia or:", "Intrauterine torsion", ["Hydrocele", "Epididymitis", "Varicocele"], 0, "Blind-ending vessels suggest monorchia or intrauterine torsion.")
q(309, S2, "Blind-ending testicular vessels are managed by:", "Excision of the remnant", ["Orchidopexy of the remnant", "Beta-hCG therapy", "Radiotherapy"], 0, "The remnant is excised when the vessels are blind-ending.")
q(309, S2, "Fowler–Stephens orchidopexy is a:", "Two-stage procedure", ["Single-stage hydrocele repair", "Three-stage procedure", "Non-operative protocol"], 0, "Fowler–Stephens orchidopexy is a two-stage procedure.")
q(309, S2, "The first stage of Fowler–Stephens orchidopexy involves:", "High ligation of testicular vessels and mobilisation into the inguinal canal", ["Excision of the testis", "Only fixation in the scrotum", "Ligation of the vas deferens"], 0, "Stage 1 is high ligation of testicular vessels plus mobilisation into the inguinal canal.")
q(309, S2, "The rationale for high ligation in Fowler–Stephens orchidopexy is to create a:", "Longer pedicle that is easier to mobilise", ["Shorter pedicle with no blood supply", "Wider inguinal ring", "New vas deferens"], 0, "High ligation creates a longer pedicle that is easier to mobilise.")
q(309, S2, "The second stage of Fowler–Stephens orchidopexy is performed after a few weeks and involves:", "Mobilisation of the testis into the scrotum", ["Removal of the testis", "Closure of the processus vaginalis only", "Ligation of the renal vein"], 0, "Stage 2 mobilises the testis into the scrotum after a few weeks.")
q(309, S2, "The best method of orchidopexy listed in the chapter is:", "Silbaar technique", ["Keetley–Torek technique", "Jaboulay procedure", "Lord's plication"], 0, "Silbaar is listed as the best orchidopexy method.")
q(309, S2, "In the Silbaar method, the testicular vessels are cut and followed by:", "Microvascular anastomosis with branches of the internal iliac", ["Anastomosis with the portal vein", "Ligation of the vas deferens", "Anastomosis with the femoral artery"], 0, "Silbaar uses microvascular anastomosis with branches of the internal iliac after cutting the testicular vessels.")
q(309, S2, "An ectopic testis is one that:", "Deviates from the normal path of descent", ["Is arrested along the normal path", "Is always intra-abdominal", "Has no blood supply"], 0, "An ectopic testis deviates from the normal path of descent.")
q(309, S2, "The most common site of an ectopic testis is the:", "Superficial inguinal pouch near the superficial ring", ["Perineum", "Renal fossa", "Contralateral scrotum"], 0, "The superficial inguinal pouch close to the superficial ring is the commonest ectopic site.")
q(309, S2, "The treatment of an ectopic testis is:", "Orchidopexy", ["Reassurance only", "Orchidectomy in all cases", "Hydrocelectomy"], 0, "Ectopic testis is managed by orchidopexy.")
q(309, S2, "A retractile testis is considered a:", "Normal variant", ["Malignancy", "Form of anorchia", "Type of hydrocele"], 0, "Retractile testis is a normal variant.")
q(309, S2, "A retractile testis may:", "Occasionally jump into the inguinal canal and return to the scrotum", ["Never enter the inguinal canal", "Always remain intra-abdominal", "Become an ectopic testis"], 0, "A retractile testis can occasionally jump into the inguinal canal and return to the scrotum by itself or manual repositioning.")
q(309, S2, "The management of a retractile testis is:", "Reassurance", ["Immediate orchidectomy", "Fowler–Stephens orchidopexy", "Chemotherapy"], 0, "A retractile testis is managed with reassurance.")

# ------------------------------------------------------------------ p310
S3 = "Testicular Torsion"
q(310, S3, "The bell-clapper deformity predisposes to torsion because of:", "High attachment of the tunica vaginalis", ["Low attachment of the tunica vaginalis", "Absence of the epididymis", "A patent processus vaginalis only"], 0, "Bell-clapper testis has high attachment of the tunica vaginalis.")
q(310, S3, "Which is a risk factor for testicular torsion?", "Testicular inversion", ["A descended testis with normal attachment only", "Hydrocele alone", "Epididymal cyst"], 0, "Testicular inversion is a listed risk factor for torsion.")
q(310, S3, "An undescended testis is a risk factor for:", "Testicular torsion", ["Only hydrocele", "Only penile fracture", "Only balanitis"], 0, "Undescended testis is a risk factor for testicular torsion.")
q(310, S3, "Separation of the testis from the epididymis is a:", "Rare risk factor for torsion", ["Common cause of hydrocele", "Diagnostic sign of epididymitis", "Normal attachment"], 0, "A testis separating from the epididymis is a rare torsion risk factor.")
q(310, S3, "The typical patient with testicular torsion is a:", "Young male", ["Postmenopausal woman", "Neonate with a renal cyst", "Elderly woman"], 0, "Testicular torsion typically affects a young male.")
q(310, S3, "The pain of testicular torsion is typically:", "Acute, severe scrotal pain", ["Mild chronic loin pain", "Painless swelling", "Pain only on micturition"], 0, "Torsion causes acute-onset severe scrotal pain.")
q(310, S3, "Acute swelling in a young male with severe scrotal pain should raise suspicion of:", "Testicular torsion", ["Simple spermatocele", "Scrotal sebaceous cyst", "Chronic hydrocele"], 0, "Acute swelling accompanies the acute pain of torsion.")
q(310, S3, "In testicular torsion, lifting the testis on Prehn's sign causes:", "Increased pain", ["Relief of pain", "No change in pain in every case", "Immediate reduction of swelling"], 0, "The book contrasts torsion, in which lifting the testis increases pain, with epididymo-orchitis, in which pain decreases.")
q(310, S3, "In torsion, the affected testis lies:", "Higher than the opposite testis", ["Lower than the opposite testis", "At the level of the knee", "Only in the perineum"], 0, "The Deming sign is a higher-riding testis on the side of torsion.")
q(310, S3, "A transversely placed testis is suggestive of:", "Testicular torsion", ["Hydrocele", "Varicocele", "Epididymal cyst"], 0, "A transverse lie is a listed sign of torsion.")
q(310, S3, "A 720-degree twist causes more rapid ischaemia than a twist of:", "Less than 360 degrees", ["Exactly 720 degrees", "More than 1080 degrees only", "No twist"], 0, "A 720-degree twist causes more rapid ischaemia than a twist of less than 360 degrees.")
q(310, S3, "If testicular torsion is untwisted within 6 hours, the chance of salvage is approximately:", "100%", ["20%", "50%", "0%"], 0, "Untwisting within 6 hours gives a 100% chance of salvage in the chapter.")
q(310, S3, "If testicular torsion is treated after 24 hours, the chance of salvage is approximately:", "20%", ["100%", "80%", "60%"], 0, "After more than 24 hours the listed chance of salvage is 20%.")
q(310, S3, "The diagnosis of testicular torsion is primarily:", "Clinical, supported by Doppler", ["Made only by biopsy", "Made only by urine culture", "Made by plain abdominal X-ray"], 0, "Torsion is diagnosed clinically and supported by Doppler.")
q(310, S3, "Doppler in testicular torsion shows:", "Absent blood flow in the testis", ["Increased renal blood flow", "A normal testicular flow in every case", "Portal venous flow"], 0, "Doppler shows absent blood flow in the affected testis.")
q(310, S3, "The operative management of suspected testicular torsion is:", "Scrotal exploration", ["Observation for 24 hours", "Aspiration of the hydrocele", "Perineal urethrostomy"], 0, "Scrotal exploration is the operative management of torsion.")
q(310, S3, "At exploration, a viable torsed testis is managed by:", "De-rotation and orchidopexy", ["Orchidectomy without detorsion", "Only antibiotics", "Hydrocelectomy"], 0, "A viable testis is de-rotated and fixed by orchidopexy.")
q(310, S3, "At exploration, a necrotic torsed testis is managed by:", "Orchidectomy", ["Orchidopexy alone", "Observation", "Epididymal aspiration"], 0, "A necrotic testis requires orchidectomy.")
q(310, S3, "Orchidopexy for torsion uses:", "Three-point fixation with non-absorbable sutures", ["A single absorbable suture", "No fixation", "Only a skin suture"], 0, "The testis is fixed at three points with non-absorbable sutures.")
q(310, S3, "After unilateral testicular torsion, the contralateral testis should undergo:", "Prophylactic orchidopexy", ["Routine orchidectomy", "No procedure ever", "Only hydrocele repair"], 0, "Prophylactic contralateral orchidopexy is performed because the predisposing anatomy may be bilateral.")

# ------------------------------------------------------------------ p311
S4 = "Epididymo-orchitis and Hydrocele"
q(311, S4, "Epididymo-orchitis is an infection of the:", "Epididymis and testis", ["Prostate and seminal vesicle only", "Tunica albuginea only", "Kidney and ureter"], 0, "Epididymo-orchitis is infection of the epididymis plus testis.")
q(311, S4, "The most common organism in epididymo-orchitis in a patient younger than 40 years is:", "Chlamydia", ["Escherichia coli", "Proteus", "Candida"], 0, "In patients under 40 years, Chlamydia is the commonest organism.")
q(311, S4, "The most common organism in epididymo-orchitis in a patient older than 40 years is:", "Escherichia coli", ["Chlamydia", "Mycobacterium tuberculosis", "Staphylococcus aureus"], 0, "In patients over 40 years, E. coli is the commonest organism, secondary to UTI.")
q(311, S4, "A typical clinical feature of epididymo-orchitis is:", "Acute scrotal pain and swelling", ["Painless scrotal mass", "Chronic loin pain only", "A dry cough"], 0, "Epididymo-orchitis presents with acute scrotal pain and swelling.")
q(311, S4, "The important differential diagnosis of acute epididymo-orchitis is:", "Testicular torsion", ["Renal-cell carcinoma", "Hydrocele of the cord", "Phimosis"], 0, "Testicular torsion is the important differential diagnosis.")
q(311, S4, "Initial management of epididymo-orchitis includes:", "Antibiotics, scrotal support and pain killers", ["Orchidectomy in every case", "Only radiotherapy", "Only aspiration"], 0, "Management is antibiotics plus scrotal support and pain killers.")
q(311, S4, "A hydrocele is an accumulation of fluid in the:", "Tunica vaginalis", ["Seminiferous tubules", "Vas deferens", "Epididymal head only"], 0, "Hydrocele is fluid accumulation in the tunica vaginalis.")
q(311, S4, "The most common type of hydrocele is:", "Vaginal hydrocele", ["Hydrocele of the cord", "Congenital hydrocele", "Infantile hydrocele"], 0, "Vaginal hydrocele is the commonest type.")
q(311, S4, "A vaginal hydrocele consists of fluid accumulation:", "Only around the testis", ["Only inside the epididymis", "Within the renal pelvis", "Around the prostate"], 0, "Vaginal hydrocele is fluid only around the testis.")
q(311, S4, "The commonest type of vaginal hydrocele is:", "Primary hydrocele", ["Secondary hydrocele", "Congenital hydrocele", "Infantile hydrocele"], 0, "Primary vaginal hydrocele is the commonest type.")
q(311, S4, "Primary vaginal hydrocele is caused by:", "Decreased absorption", ["Increased secretion only", "A renal tumour", "A patent urethra"], 0, "Primary hydrocele is due to decreased absorption.")
q(311, S4, "Secondary vaginal hydrocele is caused by:", "Increased secretion", ["Decreased lymphatic drainage only", "Absent tunica vaginalis", "A short vas deferens"], 0, "Secondary vaginal hydrocele is due to increased secretion.")
q(311, S4, "The most common cause of secondary vaginal hydrocele listed is:", "Epididymo-orchitis", ["Renal agenesis", "Testicular descent", "Phimosis"], 0, "Secondary hydrocele is most commonly secondary to epididymo-orchitis; trauma and tumours are also listed.")
q(311, S4, "A primary hydrocele is usually:", "A tense swelling with the testis not separately palpable", ["A lax swelling with the testis clearly palpable", "A solid non-scrotal mass", "A painful inguinal mass"], 0, "Primary hydrocele is tense and the testis is not separately palpable.")
q(311, S4, "A secondary hydrocele is usually:", "A lax swelling with the testis separately palpable", ["A tense swelling with no testis palpable", "A solid mass in the renal angle", "A completely empty scrotum"], 0, "Secondary hydrocele is lax and the testis is separately palpable.")
q(311, S4, "A primary hydrocele usually contains:", "Clear fluid and brilliantly transilluminates", ["Turbid fluid with no transillumination", "Blood that never transilluminates", "Air that gives a double bubble sign"], 0, "Primary hydrocele contains clear fluid and is brilliantly transilluminant.")
q(311, S4, "A secondary hydrocele usually:", "Does not transilluminate because the fluid is turbid", ["Brilliantly transilluminates", "Contains only air", "Always contains sperm"], 0, "Secondary hydrocele has turbid fluid and no transillumination.")
q(311, S4, "The operation listed for a small hydrocele is:", "Lord's plication", ["Jaboulay's procedure only", "Fowler–Stephens procedure", "Barbagli urethroplasty"], 0, "Lord's plication is used for small hydroceles.")
q(311, S4, "Jaboulay's procedure consists of:", "Eversion and suturing of the sac", ["High ligation of testicular vessels", "End-to-end urethral anastomosis", "Excision of the testis"], 0, "Jaboulay's procedure is eversion plus suturing of the hydrocele sac.")
q(311, S4, "An inguinoscrotal swelling in infantile hydrocele has which getting-above sign?", "Getting above the swelling is negative", ["Getting above the swelling is positive", "It is positive only after exercise", "The sign is never assessed"], 0, "In infantile hydrocele, an inguinoscrotal swelling cannot be got above.")
q(311, S4, "The treatment of infantile hydrocele is:", "Excision of excess sac with eversion of the sac", ["Orchidectomy", "Only reassurance in all cases", "Percutaneous nephrostomy"], 0, "Infantile hydrocele is treated by excision of excess sac and eversion of the sac.")

# ------------------------------------------------------------------ p312
S5 = "Congenital Hydrocele and Miscellaneous Scrotal Conditions"
q(312, S5, "Congenital hydrocele is associated with a:", "Patent processus vaginalis", ["Closed processus vaginalis", "Absent tunica vaginalis", "Patent urethra only"], 0, "Congenital hydrocele has a patent processus vaginalis.")
q(312, S5, "A patent processus vaginalis in congenital hydrocele communicates with the:", "Peritoneal cavity", ["Renal pelvis", "Seminal vesicle", "Subarachnoid space"], 0, "The patent processus vaginalis communicates with the peritoneal cavity.")
q(312, S5, "Congenital hydrocele is associated with a:", "Hernial sac", ["Pancreatic pseudocyst", "Urethral diverticulum", "Renal abscess"], 0, "The chapter depicts a hernial sac with congenital hydrocele.")
q(312, S5, "The treatment of congenital hydrocele is:", "Herniotomy, done by 2–3 years of age", ["Lord's plication at birth in every case", "Orchidectomy", "Radiotherapy"], 0, "Congenital hydrocele is treated by herniotomy, done by 2–3 years of age.")
q(312, S5, "Hydrocele of the cord presents as:", "Swelling along the spermatic cord", ["Only a renal-angle mass", "A swelling inside the prostate", "A lesion of the glans"], 0, "Hydrocele of the cord presents as swelling along the cord.")
q(312, S5, "Symptomatic hydrocele of the cord is treated by:", "Excision", ["Antibiotics only", "Fowler–Stephens orchidopexy", "Perineal urethrostomy"], 0, "Symptomatic hydrocele of the cord is treated by excision.")
q(312, S5, "A spermatocele is usually:", "Unilocular", ["Multiloculated like a bunch of grapes", "A solid tumour", "A communicating hydrocele"], 0, "Spermatocele is unilocular; an epididymal cyst is multiloculated.")
q(312, S5, "An epididymal cyst is characteristically:", "Multiloculated, like a bunch of grapes", ["Unilocular and solid", "Always connected to the kidney", "Filled with blood only"], 0, "An epididymal cyst is multiloculated and has a bunch-of-grapes appearance.")
q(312, S5, "A spermatocele involves the:", "Head of the epididymis", ["Tunica vaginalis only", "Renal pelvis", "Prostatic urethra"], 0, "The spermatocele involves the epididymal head.")
q(312, S5, "An epididymal cyst represents:", "Cystic degeneration of the epididymis", ["Cystic degeneration of the kidney", "A dilated seminal vesicle", "A testicular germ-cell tumour"], 0, "An epididymal cyst is due to cystic degeneration of the epididymis.")
q(312, S5, "The fluid in a spermatocele is described as:", "Barley coloured", ["Crystal clear", "Milky white in every case", "Frankly purulent"], 0, "Spermatocele contains barley-coloured fluid.")
q(312, S5, "The fluid in an epididymal cyst is:", "Crystal clear and gives a Chinese-lantern transillumination pattern", ["Barley coloured and opaque", "Always blood stained", "Non-transilluminant air"], 0, "Epididymal cyst contains crystal-clear fluid and transilluminates in a Chinese-lantern pattern.")
q(312, S5, "Spermatocele contains:", "Sperm", ["Only bile", "No fluid at all", "Urine"], 0, "Sperm are present in a spermatocele.")
q(312, S5, "The treatment of a symptomatic spermatocele is:", "Excision", ["Observation only regardless of symptoms", "Orchidectomy in every case", "Antitubercular therapy"], 0, "A symptomatic spermatocele is treated by excision, which may cause infertility.")
q(312, S5, "Excision of a symptomatic spermatocele may cause:", "Infertility", ["Hydronephrosis", "Penile fracture", "Aortic aneurysm"], 0, "Excision of a spermatocele may cause infertility.")
q(312, S5, "The treatment of a symptomatic epididymal cyst is:", "Excision", ["Radiotherapy", "Only scrotal support", "High inguinal orchidectomy"], 0, "A symptomatic epididymal cyst is treated by excision.")
q(312, S5, "Scrotal sebaceous cysts are due to:", "Blocked hair-follicle ducts", ["Patent processus vaginalis", "Torsion of the testis", "A ureteric stone"], 0, "Scrotal sebaceous cysts are due to blocked hair follicle ducts.")
q(312, S5, "Scrotal sebaceous cysts are associated with:", "No increased risk of cancer", ["A very high risk of seminoma", "A guaranteed risk of SCC", "An increased risk of renal-cell carcinoma"], 0, "The chapter states that scrotal sebaceous cysts do not increase cancer risk.")
q(312, S5, "The treatment of a symptomatic scrotal sebaceous cyst is:", "Excision", ["Chemotherapy", "Orchidopexy", "Endoscopic urethrotomy"], 0, "Symptomatic scrotal sebaceous cysts are treated by excision.")

# ------------------------------------------------------------------ units

def first_page(title):
    for x in Q:
        if x["sec"] == title:
            return x["page"]
    return 0

UNIT_DEFS = [
    (S1, "The testis develops in the retroperitoneal genital ridge and descends under the pull of the contractile gubernaculum, hormonal factors and differential abdominal-wall growth. Remember the transport map: epididymis to vas, rete testis to epididymis; the left testicular vein takes a long right-angled route to the left renal vein, while left and right testicular lymph drain first to para-aortic and interaortocaval groups respectively."),
    (S2, "An undescended testis is arrested on its normal route, usually in the inguinal canal, with the right side more often involved. It shrinks, injures Sertoli cells and spermatogenesis, raises intratubular germ-cell neoplasia and seminoma risk, and brings trauma, torsion, infertility and indirect hernia; use ultrasound for an inguinal testis and diagnostic laparoscopy for an intra-abdominal one. Wait for spontaneous descent only to five months, operate at 6–12 months, and follow the beta-hCG/laparoscopy and orchidopexy algorithms; distinguish ectopic from retractile testis."),
    (S3, "Torsion is an acute surgical emergency in a young male: the bell-clapper anatomy, severe pain, high-riding transverse testis and painful Prehn sign point to absent Doppler flow. Salvage is best within six hours, so explore rather than delay; de-rotate and fix a viable testis, remove a necrotic one, use three-point non-absorbable fixation and fix the other side prophylactically."),
    (S4, "Epididymo-orchitis infects both epididymis and testis: Chlamydia is common below 40 years and E. coli above 40 years, but torsion must be excluded. Hydrocele is fluid in the tunica vaginalis: primary is common, decreased absorption, tense, clear and brilliantly transilluminant; secondary is increased secretion, commonly from epididymo-orchitis, lax, separately palpable and turbid. Match the hydrocele operation to the lesion — Lord for small sacs, Jaboulay for eversion and suture, and excision plus eversion for infantile hydrocele."),
    (S5, "Congenital hydrocele communicates through a patent processus vaginalis and is treated with age-appropriate herniotomy; cord hydrocele runs along the cord and is excised when symptomatic. A spermatocele is a unilocular barley-coloured, sperm-containing epididymal-head lesion, whereas an epididymal cyst is a multiloculated crystal-clear Chinese-lantern lesion. Both symptomatic lesions are excised, while scrotal sebaceous cysts arise from blocked hair-follicle ducts without increased cancer risk."),
]

UNITS = []
for i, (title, guide) in enumerate(UNIT_DEFS, 1):
    UNITS.append({
        "id": f"SURG-U41-{i}",
        "ch": 41,
        "n": i,
        "title": title,
        "sec": f"{title} · p{first_page(title)}",
        "qs": [x["id"] for x in Q if x["sec"] == title],
        "guide": guide,
    })

covered = [x for u in UNITS for x in u["qs"]]
assert covered == [x["id"] for x in Q]
assert len(set(covered)) == len(covered)
with open("data/ch41.json", "w", encoding="utf-8") as f:
    json.dump({"questions": Q, "units": UNITS}, f, ensure_ascii=False, indent=1)
print(f"ch41: {len(Q)} questions, {len(UNITS)} units")
