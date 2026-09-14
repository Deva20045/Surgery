#!/usr/bin/env python3
"""Build data/ch45.json — Kidney: Part 2 (Marrow Surgery Ed 8, pp339-352)."""
import json

Q = []


def q(page, sec, text, correct, wrongs, note=None):
    opts = [correct] + list(wrongs)
    assert len(opts) == 4
    Q.append({
        "id": f"SURG-C45-{len(Q)+1:03d}",
        "sec": sec,
        "page": page,
        "q": text,
        "opts": opts,
        "ans": 0,
        "exp": (note or correct) + f" (Book p{page})",
    })


# ------------------------------------------------------------------ p339
S1 = "Vesicoureteric Reflux"
q(339, S1, "Vesicoureteric reflux is:", "Upward flow of urine during micturition", ["Downward flow of urine into the urethra", "Bile reflux into the stomach", "Blood flow from the kidney to the bladder"])
q(339, S1, "A clinical feature of vesicoureteric reflux is:", "Recurrent urinary tract infection", ["Painless scrotal mass", "Painless jaundice", "Cannonball lung metastases"])
q(339, S1, "Vesicoureteric reflux can cause:", "Pyelonephritis", ["Peyronie's disease", "Hydrocele", "Penile fracture"])
q(339, S1, "A renal consequence of vesicoureteric reflux is:", "Renal scarring", ["Renal collar formation", "Cystic degeneration of the epididymis", "A simple renal cyst only"])
q(339, S1, "Long-standing vesicoureteric reflux may lead to:", "Decreased renal function", ["Increased spermatogenesis", "Biliary obstruction", "A normal renal function in every case"])
q(339, S1, "The investigation of choice for vesicoureteric reflux is:", "Micturating cystourethrogram", ["Retrograde urethrogram only", "HIDA scan", "Plain chest radiography"])
q(339, S1, "Grade I vesicoureteric reflux is reflux into a:", "Non-dilated ureter", ["Severely dilated ureter with loss of papillary impressions", "Bladder diverticulum", "Renal vein"])
q(339, S1, "Grade II vesicoureteric reflux is reflux into the:", "Renal pelvis without distension", ["Urethra only", "Renal vein", "Scrotum"])
q(339, S1, "Grade III vesicoureteric reflux causes:", "Mild distension", ["No reflux at all", "Severe ureteric distension with loss of papillary impressions", "Only a renal cyst"])
q(339, S1, "Grade IV vesicoureteric reflux shows:", "Blunting of calyces and a tortuous ureter", ["A non-dilated ureter", "Only bladder-wall thickening", "A normal collecting system"])
q(339, S1, "Grade V vesicoureteric reflux shows severe ureteric distension with:", "Loss of papillary impressions", ["A normal ureter", "A simple renal cyst", "A normal bladder neck"])
q(339, S1, "The management of grade I–III vesicoureteric reflux is:", "Antibiotic prophylaxis", ["Immediate nephrectomy", "Only radiotherapy", "Total cystectomy"])
q(339, S1, "The management of grade IV–V vesicoureteric reflux is:", "Antibiotic prophylaxis with or without intervention", ["Only reassurance", "Only circumcision", "Only oral analgesics"])
q(339, S1, "The endoscopic treatment of vesicoureteric reflux listed is:", "STING", ["Fowler–Stephens orchidopexy", "Whipple procedure", "Lord's plication"])
q(339, S1, "STING stands for:", "Subureteric Teflon injection", ["Surgical tubular internal nephrostomy graft", "Suprapubic treatment of infected nephritis", "Selective testicular injection"])
q(339, S1, "The alternative endoscopic material/procedure to STING listed is:", "Deflux", ["BEP", "Cabanas", "Barbagli"])
q(339, S1, "HIT in endoscopic reflux treatment stands for:", "Hydrodistension implantation technique", ["High-intensity tomography", "Hilar internal traction", "Hepatic implantation therapy"])
q(339, S1, "The open operation for vesicoureteric reflux is:", "Reimplantation of the ureters", ["Partial nephrectomy in every case", "Dorsal slit surgery", "Hydrocelectomy"])
q(339, S1, "The named open ureteric reimplantation technique is:", "Politano–Leadbetter technique", ["Anderson–Hynes technique", "Nesbit technique", "Grayhack technique"])

# ------------------------------------------------------------------ p340-342
S2 = "Retroperitoneal Trauma and Renal Injury"
q(340, S2, "Zone I of retroperitoneal trauma contains the:", "Major vessels, pancreas and aorta/IVC region", ["Pelvic structures only", "Kidney and ureter only", "External genitalia only"])
q(340, S2, "Zone I retroperitoneal trauma has the:", "Maximum mortality", ["Lowest mortality", "No mortality", "Same mortality as a superficial haematoma"])
q(340, S2, "Zone II of retroperitoneal trauma contains the:", "Kidneys, ureters and renal vessels", ["Portal triad only", "Pelvic structures only", "Scrotum and penis"])
q(340, S2, "Zone III of retroperitoneal trauma contains the:", "Pelvic structures", ["Pancreas only", "Renal hilum only", "Thoracic aorta"])
q(340, S2, "The most common zone of retroperitoneal involvement listed is:", "Zone III", ["Zone I", "Zone II", "The cervical zone"])
q(340, S2, "The investigation of choice for a stable patient with renal trauma is:", "CECT", ["Single-shot IVU only", "FAST", "Plain skull radiography"])
q(340, S2, "The investigation listed for an unstable patient with renal trauma is:", "Single-shot intravenous urography", ["Routine MRI", "Barium enema", "HIDA scan"])
q(340, S2, "FAST in the evaluation of renal trauma is:", "Not useful", ["The investigation of choice", "Mandatory before every IVU", "Diagnostic of ureteric injury in every case"])
q(340, S2, "The dye used for IVU in renal trauma is:", "Urografin", ["Barium", "Deflux", "Methylene blue"])
q(340, S2, "A non-visualized kidney on IVU after trauma suggests an absent kidney or:", "Injury to the renal vessels", ["A hydrocele", "A urethral stricture only", "A normal renal artery"])
q(340, S2, "Retroperitoneal dye accumulation on IVU indicates:", "Extravasation related to retroperitoneal injury", ["A normal renal collecting system", "A bladder stone", "A patent processus vaginalis"])
q(340, S2, "Grade I renal injury is:", "Subcapsular haematoma", ["Kidney avulsion", "Laceration into the collecting system", "A shattered kidney"])
q(340, S2, "Grade I renal injury may present with:", "Microscopic or gross haematuria", ["Only jaundice", "Only anuria", "A normal urine examination in every case"])
q(340, S2, "Grade II renal injury is a laceration:", "Less than 1 cm without urinary extravasation", ["More than 1 cm into the collecting system", "With avulsion of the hilum", "With a completely shattered kidney"])
q(341, S2, "Grade III renal injury is a laceration:", "More than 1 cm", ["Less than 1 mm only", "Into the ureteric orifice", "With total renal avulsion"])
q(341, S2, "Grade IV renal injury includes laceration into the:", "Collecting system", ["Scrotal skin", "Portal vein", "Bladder trigone only"])
q(341, S2, "Laceration into the collecting system produces a urinary leak called:", "Urinoma", ["Hydrocele", "Varicocele", "Bilhemia"])
q(341, S2, "Grade IV renal injury may involve injury to the:", "Renal artery or vein", ["Cystic artery only", "External iliac vein only", "Portal triad only"])
q(341, S2, "An arterial blood clot after renal trauma can result from:", "Endothelial injury", ["A patent processus vaginalis", "A ureterocele", "A simple renal cyst"])
q(341, S2, "Grade V renal injury is represented by a:", "Shattered kidney or avulsion of the hilum", ["Subcapsular haematoma only", "Small cortical laceration", "Simple renal contusion"])
q(341, S2, "Grade I–III renal injuries are managed:", "Conservatively", ["By immediate nephrectomy", "By total penectomy", "By radiotherapy"])
q(341, S2, "A sterile urinoma after grade IV renal injury is treated with a:", "DJ stent", ["Pigtail catheter in every case", "Dorsal slit", "Biliary drain"])
q(341, S2, "An infected urinoma after grade IV renal injury is treated with:", "Pigtail catheter drainage", ["Only observation", "Only oral vitamins", "Immediate bilateral nephrectomy"])
q(341, S2, "Vascular injury in grade IV renal trauma is managed by:", "Exploration of the retroperitoneum and repair", ["Only antibiotic prophylaxis", "Circumcision", "Observation for one year"])
q(341, S2, "An expanding haematoma is a feature suggesting:", "Vascular injury in renal trauma", ["A simple hydrocele", "A sterile urine culture", "A low-grade renal cyst"])
q(341, S2, "A pulsatile leak after renal trauma suggests:", "Vascular injury", ["A ureterocele", "A bladder diverticulum", "A normal renal artery"])
q(341, S2, "Non-visualization on IVU is a feature suggesting:", "Vascular injury in grade IV renal trauma", ["Only grade I injury", "An uncomplicated renal cyst", "A normal kidney"])
q(341, S2, "Grade V renal injury is treated with:", "Partial or total nephrectomy", ["Only antibiotic prophylaxis", "Dorsal slit surgery", "Endoscopic STING"])

# ------------------------------------------------------------------ p342
S3 = "Ureteric Injury"
q(342, S3, "The most common cause of ureteric injury is:", "Surgery", ["Renal stones in every case", "Blunt scrotal trauma", "Peyronie's disease"])
q(342, S3, "A common operation causing ureteric injury is:", "Hysterectomy", ["Circumcision", "Hydrocelectomy", "Appendectomy only"])
q(342, S3, "Another operation causing ureteric injury is:", "Pelvic tumour resection", ["Cataract surgery", "Thyroidectomy only", "Dental extraction"])
q(342, S3, "One point of ureteric injury during pelvic dissection is the:", "Ligation of gonadal vessels", ["Ligation of the cystic duct", "Division of the portal vein", "Excision of the foreskin"])
q(342, S3, "Another point of ureteric injury is:", "Ligation of uterine vessels", ["Ligation of the renal artery in every case", "Division of the pancreatic duct", "Excision of the scrotal skin"])
q(342, S3, "Dissection of the bladder or vagina is a point at which the:", "Ureter may be injured", ["Testis always torses", "Gallbladder ruptures", "Renal cortex regenerates"])
q(342, S3, "A partial ureteric injury recognized during surgery is repaired with:", "An absorbable suture", ["A non-absorbable vascular graft in every case", "Only antibiotics", "Total nephrectomy"])
q(342, S3, "A complete ureteric tear without loss of segment is treated by:", "Anastomosis over a DJ stent", ["Boari flap in every case", "Only observation", "Urethral dilatation"])
q(342, S3, "A complete ureteric transection with loss of a segment is treated with:", "Boari flap repair or psoas hitch", ["Only a Foley catheter", "Hydrocelectomy", "Cystolithotomy"])
q(342, S3, "A delayed presentation of ureteric injury may be:", "Urinoma", ["A clear hydrocele", "A varicocele only", "Painless penile plaque"])
q(342, S3, "An urinoma after delayed ureteric injury is managed with a pigtail catheter followed by:", "DJ stenting", ["Orchidectomy", "Radiotherapy", "Only observation"])
q(342, S3, "Complete ureteric tie-off can cause:", "Renal atrophy", ["Increased renal function", "A penile tumour", "A scrotal cyst"])
q(342, S3, "The most common fistula after ureteric injury is:", "Uretero-vaginal fistula", ["Uretero-gastric fistula", "Uretero-bronchial fistula", "Uretero-cutaneous fistula in every case"])
q(342, S3, "A diagnostic investigation for delayed ureteric injury is:", "CT urography", ["HIDA scan", "Plain chest radiography", "Micturating cystourethrogram only"])
q(342, S3, "Another investigation for delayed ureteric injury is:", "IVU", ["Barium meal", "PET-CT only", "Scrotal ultrasound only"])
q(342, S3, "The definitive treatment for a recognized ureteric injury is:", "Repair", ["Only analgesia", "Only antibiotics", "Routine orchidectomy"])

# ------------------------------------------------------------------ p343-344
S4 = "Renal Tuberculosis"
q(343, S4, "Renal tuberculosis is usually a secondary infection acquired through the:", "Haematogenous route", ["Ascending bile duct route", "Direct scrotal route", "Portal venous route only"])
q(343, S4, "The earliest lesion in renal tuberculosis is a:", "Papillary ulcer", ["Putty kidney", "Thimble bladder", "Golf-hole ureteric orifice"])
q(343, S4, "The renal tuberculosis lesion that follows papillary ulceration is the:", "Ghost calyx", ["Cement kidney", "Ureterocele", "Renal collar"])
q(343, S4, "A ghost calyx is also described radiologically as a:", "Moth-eaten calyx", ["Cobra-head calyx", "Flower-vase calyx", "Coffin-lid calyx"])
q(343, S4, "A later renal tuberculosis complication is a:", "Perinephric abscess", ["Simple cortical cyst", "Hydrocele", "Varicocele"])
q(343, S4, "Caseous necrosis with pus-filled renal tissue produces:", "Putty kidney", ["Horseshoe kidney", "Clear-cell kidney", "Cystine kidney"])
q(343, S4, "Calcification of a putty kidney produces:", "Cement kidney", ["Mulberry kidney", "Drooping-lily kidney", "Keyhole kidney"])
q(343, S4, "Herr's kink is kinking of the:", "Ureteropelvic junction", ["Ureterovesical junction only", "Renal artery", "Bladder neck"])
q(343, S4, "Renal tuberculosis can cause a ureteric:", "Stricture with shortening of the ureter", ["Dilatation with increased length in every case", "Cystic tumour", "Complete absence at birth"])
q(343, S4, "The golf-hole ureteric orifice in renal tuberculosis:", "Remains open", ["Always becomes completely closed", "Is a ureterocele", "Is a normal bladder neck"])
q(343, S4, "A thimble bladder in renal tuberculosis has:", "Decreased capacity", ["Increased capacity", "Normal capacity in every case", "Only a ureteric stone"])
q(343, S4, "Renal tuberculosis may involve the testis and epididymis causing:", "Epididymo-orchitis", ["Hydrocele only", "Penile fracture", "Varicocele only"])
q(343, S4, "A vas finding in genitourinary tuberculosis is:", "Beading of the vas", ["Dilatation of the pampiniform plexus only", "Complete absence of the vas in every case", "A ureterocele"])
q(343, S4, "Genitourinary tuberculosis may cause:", "Sinus formation", ["A keyhole bladder only", "Biliary fistula", "Pancreatic pseudocyst"])
q(343, S4, "The prostate in genitourinary tuberculosis may feel:", "Boggy", ["Rock hard in every case", "Completely absent", "Transilluminant"])
q(343, S4, "A cortical abscess in renal tuberculosis may rupture into the:", "Perinephric space", ["Pleural cavity only", "Gallbladder", "Tunica vaginalis"])
q(343, S4, "The ureter in renal tuberculosis may appear:", "Beaded", ["Coffin-lid shaped", "Cobra-headed", "Completely normal in every case"])
q(343, S4, "Renal tuberculosis may thicken the bladder wall and produce a:", "Thimble bladder", ["Megacystis", "Keyhole bladder only", "Bladder diverticulum in every case"])
q(343, S4, "Renal tuberculosis may also produce a:", "Urethral stricture", ["Ureteric stone in every case", "Hydrocele", "Peyronie's plaque"])
q(344, S4, "Clinical features of renal tuberculosis include:", "Haematuria, a mass and weight loss", ["Only jaundice", "Only scrotal pain", "Only cough"])
q(344, S4, "The investigation of choice for renal tuberculosis is:", "CT urography", ["HIDA scan", "Plain X-ray only", "Micturating cystourethrogram only"])
q(344, S4, "Urine microscopy in renal tuberculosis shows:", "Pus cells", ["Only red-cell casts in every case", "Bile pigments", "Spermatozoa only"])
q(344, S4, "Sterile pus cells in urine are called:", "Sterile pyuria", ["Haematuria", "Chyluria", "Bilhemia"])
q(344, S4, "Urine culture in renal tuberculosis is typically:", "Sterile", ["Always positive for E. coli", "Always positive for Proteus", "Positive for Candida in every case"])
q(344, S4, "For confirmation, the chapter recommends collecting:", "Three morning urine samples", ["One evening sample only", "A single sputum sample", "Only a blood culture"])
q(344, S4, "The urine sediment in suspected renal tuberculosis is examined with:", "Ziehl–Neelsen staining", ["Gram stain only", "India ink only", "Prussian blue only"])
q(344, S4, "Ziehl–Neelsen staining is used to identify:", "Acid-fast bacilli", ["Coffin-lid crystals", "Psammoma bodies", "Spermatozoa"])
q(344, S4, "The gold standard for renal tuberculosis confirmation is:", "Tuberculosis culture", ["Urine dipstick", "Plain X-ray", "Serum amylase"])
q(344, S4, "The main medical treatment of renal tuberculosis is:", "Antitubercular therapy", ["BEP chemotherapy", "Only a DJ stent", "Only ESWL"])
q(344, S4, "Antitubercular therapy is given how long before planned intervention?", "A few weeks", ["Only after a year", "Only after nephrectomy", "Never before intervention"])
q(344, S4, "The exception requiring early drainage before antitubercular therapy is:", "Perinephric abscess", ["A simple ghost calyx", "A beaded vas", "A stable thimble bladder"])
q(344, S4, "A perinephric abscess in renal tuberculosis is drained with a:", "Pigtail catheter", ["Foley catheter only", "Biliary drain", "Chest tube in every case"])
q(344, S4, "A golf-hole ureteric orifice is treated with:", "Reimplantation of the ureter", ["Only antibiotics forever", "Orchidectomy", "Partial penectomy"])
q(344, S4, "A thimble bladder is treated with augmentation cystoplasty using:", "Ileum", ["Colon only in every case", "Stomach only", "Pericardium"])
q(344, S4, "Kinking of the ureter in renal tuberculosis is treated with:", "DJ stenting", ["Only cystolithotomy", "Radiotherapy", "Hydrocelectomy"])

# ------------------------------------------------------------------ p344-345
S5 = "Pyelonephritis and Bosniak Classification"
q(344, S5, "The most common organism causing pyelonephritis is:", "E. coli", ["Proteus", "Chlamydia", "Mycobacterium tuberculosis"])
q(344, S5, "Pyelonephritis may occur by a haematogenous route or by:", "Ascending infection due to vesicoureteric reflux", ["Descending biliary infection", "Direct scrotal spread", "A renal tumour"])
q(344, S5, "Pyelonephritis is more common in:", "Females than males", ["Males than females", "Only neonates", "Only elderly men"])
q(344, S5, "A risk factor for pyelonephritis is:", "Pregnancy", ["A simple spermatocele", "A healed penile fracture", "A normal renal scan"])
q(344, S5, "A clinical feature of pyelonephritis is:", "Fever", ["Painless penile curvature", "Painless jaundice", "A bag-of-worms scrotum"])
q(344, S5, "The pain of pyelonephritis is typically in the:", "Flank close to the renal angle", ["Right shoulder", "Scrotum only", "Epigastrium only"])
q(345, S5, "Urine microscopy in pyelonephritis may show:", "White-cell casts", ["Coffin-lid crystals only", "Spermatozoa only", "Bile casts"])
q(345, S5, "The investigation of choice in pyelonephritis listed is:", "CECT", ["Plain radiography only", "HIDA scan", "Retrograde urethrogram"])
q(345, S5, "Treatment of pyelonephritis includes intravenous antibiotics for:", "7–10 days", ["One dose only", "Six months before diagnosis", "No fixed course"])
q(345, S5, "After initial IV antibiotics for pyelonephritis, treatment is switched to:", "Oral antibiotics", ["Radiotherapy", "Dactinomycin", "Only analgesics"])
q(345, S5, "If pus is present in pyelonephritis, it should be:", "Drained", ["Left untreated", "Treated with ESWL", "Treated with circumcision"])
q(345, S5, "Emphysematous pyelonephritis is most commonly caused by:", "E. coli", ["Proteus only", "Tuberculosis", "Chlamydia"])
q(345, S5, "Emphysematous pyelonephritis is associated with an immunocompromised state and:", "Diabetes mellitus", ["A simple renal cyst", "A hydrocele", "A normal pregnancy only"])
q(345, S5, "Emphysematous pyelonephritis presents with fever and:", "Flank pain near the renal angle", ["Painless jaundice", "A penile ulcer", "A scrotal mass"])
q(345, S5, "The investigation of choice in emphysematous pyelonephritis shows:", "Gas around the kidney on CECT", ["A keyhole bladder on MCU", "A drooping lily on IVU", "A normal kidney on CT"])
q(345, S5, "Initial treatment of emphysematous pyelonephritis is IV antibiotics and:", "Pigtail catheter drainage", ["Immediate circumcision", "Only ESWL", "Only observation"])
q(345, S5, "If emphysematous pyelonephritis fails conservative treatment, the operation is:", "Nephrectomy", ["Hydrocelectomy", "Ureteric reimplantation", "Partial penectomy"])
q(345, S5, "Xanthogranulomatous pyelonephritis is most commonly caused by:", "Proteus more than E. coli", ["Chlamydia more than E. coli", "Tuberculosis only", "Candida only"])
q(345, S5, "Xanthogranulomatous pyelonephritis is seen particularly in:", "Middle-aged females", ["Young boys only", "Elderly men only", "Neonates only"])
q(345, S5, "Xanthogranulomatous pyelonephritis is associated with:", "Diabetes mellitus", ["A simple hydrocele", "Peyronie's disease", "A normal renal scan"])
q(345, S5, "A clinical presentation of xanthogranulomatous pyelonephritis is:", "Flank pain, pyrexia, abdominal mass and calculi", ["Painless jaundice only", "Only penile pain", "Only haemoptysis"])
q(345, S5, "CECT in xanthogranulomatous pyelonephritis shows a:", "Non-functioning kidney with low-density mass and staghorn calculi", ["Normal kidney with a simple cyst", "Keyhole bladder", "Cobra-head ureter only"])
q(345, S5, "The treatment of xanthogranulomatous pyelonephritis is antibiotics plus:", "Subcapsular nephrectomy", ["Only pigtail drainage in every case", "Circumcision", "Radiotherapy"])
q(345, S5, "The investigation of choice for renal cyst classification is:", "CECT", ["MCU", "HIDA scan", "Plain skull X-ray"])
q(345, S5, "The Bosniak classification predicts the risk of:", "Cancer", ["Ureteric reflux", "Testicular torsion", "Penile fracture"])
q(345, S5, "Bosniak class I is a:", "Simple cyst with no workup and 0% malignancy", ["Clearly malignant cyst with 100% risk", "50% malignant cyst", "Cyst requiring immediate total nephrectomy"])
q(345, S5, "Bosniak class II is:", "Minimally complex, with no workup and 0% malignancy", ["Indeterminate with 50% malignancy", "Clearly malignant", "A cyst requiring partial nephrectomy"])
q(345, S5, "Bosniak class IIF requires:", "USG or CT follow-up", ["Immediate total nephrectomy", "No follow-up ever", "Only antibiotics"])
q(345, S5, "Bosniak class IIF has an approximate malignancy risk of:", "5%", ["0%", "50%", "100%"])
q(345, S5, "Bosniak class III is:", "Indeterminate and treated with partial nephrectomy", ["A simple cyst needing no workup", "Clearly malignant requiring total nephrectomy in every case", "A benign hydrocele"])
q(345, S5, "Bosniak class III has an approximate malignancy risk of:", "50%", ["0%", "5%", "100%"])
q(345, S5, "Bosniak class IV is:", "Clearly malignant", ["A simple cyst", "Minimally complex with no risk", "A benign renal tumour"])
q(345, S5, "Bosniak class IV is managed with:", "Partial or total nephrectomy", ["Only follow-up USG", "Only antibiotics", "Only ureteric stenting"])
q(345, S5, "Bosniak class IV has an approximate malignancy risk of:", "100%", ["0%", "5%", "50%"])

# ------------------------------------------------------------------ p346-347
S6 = "Benign Renal Tumours and Birt–Hogg–Dubé Syndrome"
q(346, S6, "An angiomyolipoma is a tumour composed of:", "Blood vessels, muscle and fat", ["Only epithelial cells", "Only lymphoid tissue", "Only cartilage"])
q(346, S6, "Angiomyolipoma arises from:", "Perivascular epithelioid cells", ["Collecting-duct cells only", "Urothelial cells only", "Glomerular podocytes only"])
q(346, S6, "Angiomyolipoma most often occurs in the:", "Fifth to sixth decade", ["First month of life", "Second to third decade only", "Ninth decade only"])
q(346, S6, "The familial syndrome associated with angiomyolipoma is:", "Tuberous sclerosis", ["Birt–Hogg–Dubé syndrome only", "Peutz–Jeghers syndrome", "Denys–Drash syndrome"])
q(346, S6, "Tuberous sclerosis commonly presents in the:", "Second to third decade", ["Fifth to sixth decade only", "Neonatal period only", "Eighth decade"])
q(346, S6, "Tuberous sclerosis may produce:", "Multiple bilateral renal lesions", ["Only a unilateral ureterocele", "Only a simple renal cyst", "Only a bladder stone"])
q(346, S6, "A dermatological lesion of tuberous sclerosis is an:", "Ash-leaf macule", ["Erythroplasia of Queyrat", "Keratin pearl", "Coffin-lid crystal"])
q(346, S6, "Another dermatological lesion of tuberous sclerosis is a:", "Shagreen patch", ["Psammoma body", "Butterfly haematoma", "Golf-hole ulcer"])
q(346, S6, "A further dermatological lesion of tuberous sclerosis is:", "Adenoma sebaceum", ["Bowen disease", "A central stellate scar", "A mulberry stone"])
q(346, S6, "Angiomyolipoma may be:", "Asymptomatic", ["Always painful", "Always malignant", "Always associated with jaundice"])
q(346, S6, "A symptomatic angiomyolipoma may present with:", "Pain or a lump", ["Only painless jaundice", "Only urinary infection", "Only penile curvature"])
q(346, S6, "Wunderlich syndrome is:", "Spontaneous retroperitoneal haemorrhage", ["A ureteric reflux grade", "A type of renal cyst", "A posterior urethral valve"])
q(346, S6, "The Lenk triad in Wunderlich syndrome includes flank mass, hypotension and:", "Absence of haematuria", ["Severe jaundice", "A high-riding prostate", "A keyhole defect"])
q(346, S6, "On CECT, angiomyolipoma appears as a low-density lesion because of:", "Fat", ["Bile", "Urine", "Air only"])
q(346, S6, "Bilateral renal lesions in angiomyolipoma are classified in the chapter as:", "Bosniak class III", ["Bosniak class I", "Bosniak class IIF only", "Bosniak class IV in every case"])
q(346, S6, "An angiomyolipoma smaller than 4 cm is managed by:", "Observation", ["Immediate total nephrectomy", "Radiotherapy", "Only chemotherapy"])
q(346, S6, "An angiomyolipoma larger than 4 cm and symptomatic is treated with:", "Partial nephrectomy or nephron-sparing surgery", ["Only observation", "Only antibiotics", "Only ureteric stenting"])
q(346, S6, "A bleeding angiomyolipoma is first treated with:", "Angioembolisation", ["Immediate circumcision", "Only ESWL", "Only oral analgesia"])
q(346, S6, "After embolisation of a bleeding angiomyolipoma, the listed next treatment is:", "Partial nephrectomy", ["Total penectomy", "No follow-up", "Only a Foley catheter"])
q(346, S6, "The most common benign renal tumour is:", "Oncocytoma", ["Angiomyolipoma", "Collecting-duct carcinoma", "Wilms tumour"])
q(346, S6, "Oncocytoma arises from cells rich in:", "Mitochondria", ["Lipid droplets only", "Glycogen only", "Cilia only"])
q(346, S6, "Oncocytoma has:", "Eosinophilic cytoplasm", ["Clear bile-filled cytoplasm", "Coffin-lid crystals", "Plant-like cells only"])
q(347, S6, "Birt–Hogg–Dubé syndrome is associated with a gene on chromosome:", "17", ["3", "6", "16"])
q(347, S6, "Birt–Hogg–Dubé syndrome is associated with:", "Chromophobe RCC and oncocytoma", ["Only Wilms tumour", "Only renal agenesis", "Only a hydrocele"])
q(347, S6, "The dermatological lesions of Birt–Hogg–Dubé syndrome include:", "Trichodiscomas and fibrofolliculomas", ["Ash-leaf macules only", "Keratin pearls", "Shagreen patches only"])
q(347, S6, "Birt–Hogg–Dubé-associated renal lesions may be:", "Bilateral and multicentric", ["Always unilateral and solitary", "Only cystic in one kidney", "Limited to the bladder"])
q(347, S6, "The investigation of choice for these benign renal tumours is:", "CECT", ["MCU", "HIDA scan", "Plain radiography only"])
q(347, S6, "A central stellate scar may be seen in:", "Focal nodular hyperplasia of the liver, chromophobe RCC and oncocytoma", ["Only a ureterocele", "Only renal tuberculosis", "Only a hydrocele"])
q(347, S6, "The Bosniak class associated with the central-stellate-scar lesion in the chapter is:", "Bosniak III", ["Bosniak I", "Bosniak IIF only", "Bosniak IV in every case"])
q(347, S6, "The management of this Bosniak III renal lesion is:", "Partial nephrectomy, especially if larger than 4 cm", ["Only observation regardless of size", "Only antibiotics", "Total penectomy"])

# ------------------------------------------------------------------ p347-349
S7 = "Renal Cell Carcinoma: Risk Factors and Types"
q(347, S7, "Renal-cell carcinoma is also called:", "Grawitz tumour, hypernephroma or internist's tumour", ["Wilms tumour only", "Cobb's tumour", "Buschke–Lowenstein tumour"])
q(347, S7, "A risk factor for renal-cell carcinoma is:", "Diabetes mellitus", ["Hypospadias", "A simple hydrocele", "A healed urethral injury"])
q(347, S7, "Another risk factor for renal-cell carcinoma is:", "Hypertension", ["Balanitis only", "Ectopic testis", "A normal renal scan"])
q(347, S7, "Tobacco intake is a risk factor for:", "Renal-cell carcinoma", ["Only posterior urethral valves", "Only hydrocele", "Only ectopic ureter"])
q(347, S7, "Thorotrast exposure can cause renal-cell carcinoma as well as:", "Hepatocellular carcinoma and cholangiocarcinoma", ["Only seminoma", "Only penile cancer", "Only pyelonephritis"])
q(347, S7, "Increased protein intake is listed as a risk factor for:", "Renal-cell carcinoma", ["Renal agenesis", "Posterior urethral valves", "A simple renal cyst"])
q(347, S7, "Renal-cell carcinoma may be:", "Sporadic or familial", ["Only congenital", "Only infectious", "Only traumatic"])
q(347, S7, "The most common type of renal-cell carcinoma is:", "Clear-cell RCC", ["Papillary RCC", "Chromophobe RCC", "Collecting-duct carcinoma"])
q(347, S7, "Clear-cell RCC is associated genetically with deletion of:", "3p and 9q", ["1q only", "17p only", "6p and 16q"])
q(348, S7, "Clear-cell RCC is associated with von Hippel–Lindau syndrome and a gene on:", "Chromosome 3p", ["Chromosome 6", "Chromosome 11", "Chromosome 17"])
q(348, S7, "Clear-cell RCC may be:", "Bilateral and multicentric", ["Always unilateral and solitary", "Only confined to the bladder", "Always a simple cyst"])
q(348, S7, "Clear-cell RCC arises from the:", "Proximal convoluted tubule", ["Collecting duct only", "Distal ureter", "Seminiferous tubule"])
q(348, S7, "Papillary RCC may be associated with:", "Hereditary papillary RCC syndrome", ["Denys–Drash syndrome only", "Fournier's gangrene", "Balanitis xerotica obliterans"])
q(348, S7, "Long-term dialysis is associated with the micropapillary variant of:", "Papillary RCC", ["Clear-cell RCC", "Chromophobe RCC", "Medullary RCC"])
q(348, S7, "The genetic mutation associated with papillary RCC is:", "c-MET", ["PKHD1", "PRSS1", "STK11"])
q(348, S7, "Papillary RCC contains:", "Psammoma bodies", ["Coffin-lid crystals", "Keratin pearls", "Ash-leaf macules"])
q(348, S7, "Psammoma bodies represent foci of:", "Dystrophic calcification", ["Caseous necrosis", "Fat deposition", "Venous thrombosis"])
q(348, S7, "Papillary RCC arises from the:", "Proximal convoluted tubule more than distal convoluted tubule", ["Collecting duct only", "Renal pelvis only", "Ureteric orifice"])
q(348, S7, "Chromophobe RCC is associated with loss of multiple chromosomes including:", "1, 2, 6, 10 and 13", ["3, 4 and 5 only", "11 and 17 only", "X and Y only"])
q(348, S7, "Chromophobe RCC is associated with:", "Birt–Hogg–Dubé syndrome", ["Peutz–Jeghers syndrome", "Beckwith–Wiedemann syndrome only", "Cystinuria"])
q(348, S7, "The histology of chromophobe RCC shows:", "Plant-like cells with raisin-like nuclei", ["Clear cells with no nuclei", "Coffin-lid crystals", "Keratin pearls"])
q(348, S7, "Chromophobe RCC is positive for:", "Cytokeratin", ["AFP", "CA 19-9", "PSA"])
q(348, S7, "Among the RCC types listed, chromophobe RCC has the:", "Best prognosis", ["Worst prognosis", "Same prognosis as collecting-duct cancer", "Always fatal prognosis"])
q(348, S7, "Collecting-duct Bellini cancer arises from the:", "Collecting duct", ["Proximal convoluted tubule", "Distal convoluted tubule only", "Renal capsule"])
q(348, S7, "Collecting-duct Bellini cancer has the:", "Worst prognosis among the RCCs listed", ["Best prognosis", "Same prognosis as oncocytoma", "Benign prognosis"])
q(348, S7, "The genetics of collecting-duct Bellini cancer include deletion of:", "1q and monosomy of multiple chromosomes", ["3p only", "17p only", "6q only"])
q(348, S7, "Medullary RCC is associated with:", "Sickle-cell anaemia", ["Cystinuria", "Tuberous sclerosis only", "Vesicoureteric reflux"])
q(348, S7, "Medullary RCC has a:", "Poor prognosis", ["Best prognosis", "Benign course", "Prognosis unrelated to histology"])

# ------------------------------------------------------------------ p349
S8 = "Renal Cell Carcinoma: Presentation, Spread and Paraneoplastic Syndromes"
q(349, S8, "The most common symptom of renal-cell carcinoma is:", "Haematuria", ["Painless jaundice", "Urinary dribbling from birth", "A scrotal swelling"])
q(349, S8, "The classical triad of renal-cell carcinoma consists of haematuria, pain and:", "A mass", ["Jaundice", "Hydrocele", "Cough"])
q(349, S8, "The classical triad of renal-cell carcinoma occurs in approximately:", "15–20% of patients", ["1–2%", "50–60%", "100%"])
q(349, S8, "Renal-cell carcinoma can spread along the renal veins as:", "Tumour thrombi", ["Coffin-lid stones", "Ureteroceles", "Simple cysts"])
q(349, S8, "A left RCC tumour thrombus can block the testicular vein and cause:", "A secondary varicocele", ["A hydrocele only", "A urethral stricture", "A penile fracture"])
q(349, S8, "The most common site of distant metastasis from renal-cell carcinoma is the:", "Lung", ["Brain", "Skin", "Spleen"])
q(349, S8, "Cannonball metastases in the lungs may be due to:", "Renal-cell carcinoma", ["A simple hydrocele", "Ureterocele", "Phimosis"])
q(349, S8, "The most common paraneoplastic laboratory abnormality in renal-cell carcinoma is:", "Raised ESR", ["Low AFP", "Low CA 19-9", "Raised amylase only"])
q(349, S8, "A renal-cell-carcinoma endocrine paraneoplastic syndrome is:", "Hypercalcaemia due to PTH-related peptide", ["Hypocalcaemia due to calcitonin", "Hypoglycaemia due to insulinoma", "Hyperbilirubinaemia due to obstruction only"])
q(349, S8, "Hypertension may be a paraneoplastic manifestation of:", "Renal-cell carcinoma", ["A simple hydrocele", "Ureteric injury only", "Hypospadias"])
q(349, S8, "Polycythaemia in renal-cell carcinoma is due to release of:", "Erythropoietin", ["ACTH", "PTH-related peptide only", "CA 19-9"])
q(349, S8, "Nonmetastatic hepatic dysfunction in renal-cell carcinoma is called:", "Stauffer syndrome", ["Cushing syndrome", "Wunderlich syndrome", "Nutcracker syndrome"])
q(349, S8, "Stauffer syndrome is mediated by:", "Interleukin-6", ["Erythropoietin", "AFP", "Cytokeratin"])
q(349, S8, "Stauffer syndrome includes raised serum bilirubin and:", "Raised liver enzymes", ["Low liver enzymes", "Low creatinine only", "Raised urinary calcium only"])
q(349, S8, "The liver abnormalities of Stauffer syndrome settle after:", "Surgery", ["Circumcision", "ESWL", "Only antibiotics"])
q(349, S8, "Galactorrhoea is listed as a paraneoplastic manifestation of:", "Renal-cell carcinoma", ["A ureterocele", "A simple renal cyst", "Posterior urethral valves"])
q(349, S8, "Cushing syndrome in renal-cell carcinoma is due to release of:", "ACTH", ["Erythropoietin", "PTH-related peptide", "CA 19-9"])
q(349, S8, "Renal-cell carcinoma may cause:", "Alterations in glucose metabolism", ["Only hypothermia", "Only a keyhole bladder", "Only an ectopic ureter"])
q(349, S8, "A non-endocrine paraneoplastic manifestation of RCC is:", "Amyloidosis", ["Hyperthyroidism only", "A hydrocele", "Coffin-lid crystalluria"])
q(349, S8, "Another non-endocrine manifestation of RCC is:", "Anaemia", ["Polycythaemia only", "Bifid clitoris", "Hypospadias"])
q(349, S8, "A neuromyopathy associated with RCC is:", "Lambert–Eaton syndrome", ["Myasthenia due to thymoma only", "Bell-clapper deformity", "Cobb's collar"])
q(349, S8, "The investigation of choice for RCC is:", "CECT", ["HIDA scan", "MCU", "Plain radiography only"])
q(349, S8, "Biopsy of an RCC is indicated when:", "The diagnosis is unclear or metastasis is present", ["Every simple cyst is seen", "A patient has a hydrocele", "Only after nephrectomy"])
q(349, S8, "CT angiography in RCC is performed to see:", "Spread along the renal vein", ["Only urethral reflux", "Only bladder capacity", "Only a scrotal lesion"])

# ------------------------------------------------------------------ p350-351
S9 = "Renal Cell Carcinoma: Staging and Management"
q(350, S9, "T0 renal-cell carcinoma means:", "No evidence of a primary tumour", ["A tumour smaller than 4 cm", "Distant metastasis", "Regional nodal disease"])
q(350, S9, "T1 RCC is a tumour smaller than 7 cm and:", "Confined to the kidney", ["Invading the IVC", "Beyond Gerota fascia", "Involving the ipsilateral adrenal gland"])
q(350, S9, "T1a RCC is smaller than:", "4 cm", ["7 cm", "10 cm", "2 cm only"])
q(350, S9, "T1b RCC is larger than 4 cm but smaller than:", "7 cm", ["2 cm", "4 cm", "10 cm"])
q(350, S9, "T2 RCC is larger than 7 cm and:", "Confined to the kidney", ["Beyond Gerota fascia", "In the supradiaphragmatic IVC", "In the adrenal gland in every case"])
q(350, S9, "T2a RCC measures 7 cm to less than:", "10 cm", ["4 cm", "7 cm", "20 cm"])
q(350, S9, "T2b RCC measures more than:", "10 cm", ["4 cm", "7 cm", "1 cm"])
q(350, S9, "T3 RCC extends into major veins or perinephric tissues but not beyond:", "Gerota fascia or the ipsilateral adrenal gland", ["The urethra", "The scrotum", "The contralateral kidney in every case"])
q(350, S9, "T3a RCC may extend into renal-vein branches or invade:", "Perirenal or renal-sinus fat", ["The bladder mucosa only", "The scrotal skin", "The portal vein"])
q(350, S9, "T3b RCC extends into the:", "Subdiaphragmatic inferior vena cava", ["Portal vein", "Superior mesenteric vein", "External iliac vein only"])
q(350, S9, "T3c RCC extends into the:", "Supradiaphragmatic inferior vena cava", ["Renal pelvis only", "Ureteric orifice", "Scrotum"])
q(350, S9, "T4 RCC invades beyond the:", "Gerota fascia", ["Tunica albuginea", "Urogenital diaphragm", "Renal capsule only"])
q(350, S9, "T4 RCC may also show contiguous extension into the:", "Ipsilateral adrenal gland", ["Contralateral testis", "Gallbladder", "Pancreas in every case"])
q(350, S9, "N0 RCC means:", "No regional lymph-node metastasis", ["Distant lung metastasis", "A tumour smaller than 4 cm", "A positive para-aortic node"])
q(350, S9, "N1 RCC means metastasis in regional:", "Para-aortic lymph nodes", ["Cervical lymph nodes only", "Inguinal nodes only", "Mesenteric nodes only"])
q(350, S9, "M0 RCC means:", "No distant metastasis", ["Distant lung metastasis", "Regional nodal metastasis", "A primary tumour is absent"])
q(350, S9, "The most common distant metastatic site in RCC is the:", "Lung", ["Brain", "Bone", "Skin"])
q(350, S9, "The mainstay of treatment for RCC is:", "Surgery", ["Radiotherapy alone", "Chemotherapy alone", "Observation for every stage"])
q(350, S9, "RCC is described as resistant to:", "Chemotherapy and radiotherapy", ["Surgery", "Immunotherapy only", "Renal transplantation"])
q(350, S9, "Partial nephrectomy or nephron-sparing surgery is indicated for:", "T1 disease up to 7 cm", ["Only T4 disease", "Any metastatic disease only", "Only a simple renal cyst"])
q(350, S9, "A tumour restricted to the poles is an indication for:", "Partial nephrectomy", ["Total penectomy", "Only chemotherapy", "No treatment"])
q(350, S9, "Bilateral RCC is an indication for:", "Partial nephrectomy or nephron-sparing surgery", ["Routine bilateral total nephrectomy", "Only ESWL", "Only radiotherapy"])
q(350, S9, "RCC in a solitary functioning kidney is an indication for:", "Partial nephrectomy", ["Immediate total nephrectomy", "Only observation", "Only ureteric stenting"])
q(350, S9, "A relative indication for nephron-sparing surgery is RCC when the other kidney has:", "Hydronephrosis", ["A normal scan", "A simple hydrocele", "Only a urethral stricture"])
q(350, S9, "Another relative indication for nephron-sparing surgery is disease in the other kidney with:", "Stones", ["Only a spermatocele", "Only a penile plaque", "Only a normal ureter"])
q(350, S9, "The most important prognostic factor in RCC is:", "Pathological stage", ["Scrotal skin colour", "Presence of a hydrocele", "Serum amylase"])
q(350, S9, "The staging system listed for RCC is:", "Robson staging", ["Jackson staging", "Young staging", "Bosniak staging"])
q(350, S9, "The grading system listed for RCC is:", "Fuhrman system", ["Cabanas system", "SIOP system", "Weigert–Meyer system"])
q(351, S9, "Radical nephrectomy is performed when partial nephrectomy is:", "Contraindicated", ["Always preferred for T1a disease", "Required for every cyst", "Used only for hydrocele"])
q(351, S9, "Radical nephrectomy removes the kidney with:", "Gerota's fascia", ["Only the renal pelvis", "Only the urethra", "Only the adrenal vein"])
q(351, S9, "Radical nephrectomy includes removal of:", "Para-aortic lymph nodes", ["Only inguinal nodes", "Only cervical nodes", "Only mesenteric nodes"])
q(351, S9, "The ureter is removed up to the:", "Pelvic brim", ["External urinary meatus", "Diaphragm", "Scrotum"])
q(351, S9, "Cryoablation works by:", "Rapid freezing and gradual thawing", ["Rapid heating only", "Chemical dissolution", "Radiation alone"])
q(351, S9, "The temperature used for cryoablation is approximately:", "−20°C", ["+20°C", "−2°C", "+100°C"])
q(351, S9, "Cryoablation is listed for T1a RCC when surgery cannot be performed, such as in an:", "Elderly patient", ["Infant with a hydrocele", "Young patient with a normal kidney", "Patient with simple cyst only"])
q(351, S9, "Cryoablation may be used as palliative surgery for:", "Advanced or metastatic tumours", ["Only a benign cyst", "Only hypospadias", "Only ureteric reflux"])
q(351, S9, "Debulking surgery in metastatic RCC is performed to:", "Decrease tumour burden", ["Increase tumour burden", "Treat a hydrocele", "Create a renal cyst"])
q(351, S9, "A drug class listed for metastatic RCC is:", "mTOR inhibitors", ["Only antitubercular drugs", "Only alpha blockers", "Only bile-acid sequestrants"])
q(351, S9, "Sorafenib and sunitinib are:", "Tyrosine-kinase inhibitors", ["Antitubercular drugs", "Alpha blockers", "Corticosteroids"])
q(351, S9, "Sorafenib and sunitinib are also used in:", "Hepatocellular carcinoma and GIST", ["Only hydrocele", "Only pyelonephritis", "Only renal agenesis"])
q(351, S9, "Another therapy listed for metastatic RCC is:", "Interleukin-2", ["D-penicillamine", "Cholestyramine", "Urografin"])

# ------------------------------------------------------------------ p351-352
S10 = "Wilms Tumour"
q(351, S10, "Wilms tumour is the most common:", "Paediatric renal tumour", ["Adult renal tumour", "Testicular tumour", "Penile tumour"])
q(351, S10, "Wilms tumour usually occurs at:", "2–5 years of age", ["Birth only", "12–15 years only", "Adult age only"])
q(351, S10, "Wilms tumour is the second most common:", "Abdominal malignancy in children", ["Renal cyst in adults", "Cause of adult hypertension", "Testicular tumour in elderly men"])
q(351, S10, "The most common abdominal malignancy in children listed is:", "Neuroblastoma", ["Wilms tumour", "RCC", "Lymphoma"])
q(351, S10, "A clinical feature of Wilms tumour is an abdominal:", "Mass", ["Ulcer", "Cough only", "Scrotal swelling"])
q(351, S10, "Unlike neuroblastoma, a Wilms tumour mass:", "Rarely crosses the midline", ["Always crosses the midline", "Is always bilateral", "Is always calcified"])
q(351, S10, "A presentation of Wilms tumour is:", "Haematuria", ["Painless jaundice", "Peyronie's curvature", "Only urinary infection"])
q(351, S10, "Wilms tumour can spread along the renal veins as:", "Tumour thrombi", ["Coffin-lid crystals", "Ureteroceles", "Simple cysts"])
q(351, S10, "Wilms tumour is described as being:", "Resected easily", ["Always unresectable", "Radiotherapy resistant in every case", "Only treated by ESWL"])
q(351, S10, "The most common distant metastatic site of Wilms tumour is the:", "Lung", ["Brain", "Skin", "Gallbladder"])
q(351, S10, "The familial locus associated with Wilms tumour is on chromosome:", "11", ["3", "6", "17"])
q(351, S10, "Beckwith–Wiedemann syndrome is associated with Wilms tumour, macroglossia and:", "Hypoglycaemia", ["Hypercalcaemia", "Peyronie's disease", "Coffin-lid stones"])
q(351, S10, "Denys–Drash syndrome is associated with Wilms tumour, genitourinary malformation and:", "Nephropathy", ["A hydrocele", "Pheochromocytoma only", "Gallstone disease"])
q(351, S10, "The WAGR syndrome includes Wilms tumour, aniridia, GU malformation and:", "Mental retardation", ["Hyperthyroidism", "Cystinuria", "Peyronie's disease"])
q(351, S10, "Wilms tumour may be:", "Bilateral", ["Never bilateral", "Only metastatic", "Only a benign cyst"])
q(352, S10, "The investigation of choice for Wilms tumour is:", "CECT", ["HIDA scan", "MCU", "Retrograde urethrogram"])
q(352, S10, "Peripheral calcification on imaging favours:", "Neuroblastoma", ["Wilms tumour", "Clear-cell RCC", "A simple renal cyst"])
q(352, S10, "Intratumoral calcification is characteristic of:", "Neuroblastoma", ["Wilms tumour", "Oncocytoma", "Ureterocele"])
q(352, S10, "Stage V Wilms tumour means:", "Bilateral Wilms tumours", ["Distant lung metastasis only", "A unilateral T1 tumour", "A non-functioning kidney only"])
q(352, S10, "Wilms tumour is:", "Chemotherapy and radiotherapy sensitive", ["Chemotherapy and radiotherapy resistant", "Only treated with ESWL", "Always treated by observation"])
q(352, S10, "The chemotherapy described for Wilms tumour is:", "Dactinomycin-based", ["BEP-based", "FOLFOX-based", "Only cisplatin-based"])
q(352, S10, "The surgical principle for Wilms tumour is the same as for:", "Renal-cell carcinoma", ["Penile cancer", "Posterior urethral valves", "Hydrocele"])
q(352, S10, "The most important prognostic factor in Wilms tumour is:", "Histological findings", ["The side of the tumour", "Presence of a hydrocele", "The patient's blood group"])
q(352, S10, "An epithelial histological pattern in Wilms tumour is contrasted with a blastemal pattern, in which increased blastemal component indicates:", "Poor prognosis", ["A better prognosis", "No prognostic significance", "A benign tumour"])
q(352, S10, "The National Wilms Tumor Study Group approach is:", "Surgery followed by chemotherapy with or without radiotherapy", ["Chemotherapy only", "Radiotherapy before any surgery in every case", "Only observation"])
q(352, S10, "The Society of International Pediatric Oncology approach is:", "Chemotherapy followed by surgery with or without radiotherapy", ["Immediate nephrectomy without chemotherapy", "Only radiotherapy", "Only ESWL"])


# ------------------------------------------------------------------ units

def first_page(title):
    return next(x["page"] for x in Q if x["sec"] == title)

UNIT_DEFS = [
    (S1, "VUR is urine moving upward during micturition, leaving recurrent UTI, pyelonephritis, scars and falling renal function. MCU grades it from I, reflux without dilatation, through V, severe ureteric dilatation with lost papillary impressions; prophylaxis is enough for I–III, while IV–V may need STING/Deflux/HIT or Politano–Leadbetter reimplantation."),
    (S2, "In retroperitoneal trauma, Zone I carries the major vessels and the highest mortality, Zone II the renal structures, and Zone III the pelvic structures. Stable renal trauma gets CECT, unstable trauma single-shot Urografin IVU because FAST is not useful; grade I–III conservatively, drain or stent grade-IV urinoma according to infection, repair vascular injury and reserve partial/total nephrectomy for shattered grade V kidneys."),
    (S3, "Surgery, particularly hysterectomy and pelvic tumour resection, is the commonest ureteric injury mechanism. Repair partial tears with absorbable suture, complete tears without loss over a DJ stent, and segment loss with Boari flap or psoas hitch; delayed urinoma, renal atrophy and ureterovaginal fistula require CT urography/IVU and repair."),
    (S4, "Renal tuberculosis arrives haematogenously and progresses from papillary ulcer and ghost/moth-eaten calyx to perinephric abscess, putty/cement kidney, Herr's kink, ureteric stricture, golf-hole orifice and thimble bladder. Sterile pyuria, three morning samples with Ziehl–Neelsen staining and TB culture establish it; ATT precedes intervention except for early abscess drainage, and each structural complication has its named repair."),
    (S5, "E. coli, ascending reflux and pregnancy frame pyelonephritis; CECT, WBC casts and culture guide IV antibiotics, oral switch and drainage. Recognize emphysematous disease by gas and xanthogranulomatous disease by Proteus, a non-functioning low-density staghorn kidney. Bosniak I/IIF are low risk, III is indeterminate and IV clearly malignant, with the follow-up or nephrectomy plan attached."),
    (S6, "Angiomyolipoma contains vessels, muscle and fat and links to tuberous sclerosis, bilateral lesions and Wunderlich haemorrhage; observe below 4 cm, preserve nephron above 4 cm when symptomatic, and embolise bleeding lesions before partial nephrectomy. Oncocytoma is the commonest benign renal tumour with eosinophilic mitochondrial cytoplasm; Birt–Hogg–Dubé brings chromosome-17 lesions, chromophobe RCC, oncocytoma, trichodiscomas and fibrofolliculomas."),
    (S7, "RCC risk is linked to diabetes, hypertension, tobacco, thorotrast and high protein intake. Clear cell is common and VHL/3p-linked; papillary carries c-MET and psammoma bodies; chromophobe has raisin nuclei and the best prognosis; collecting-duct Bellini is worst; medullary RCC links to sickle-cell anaemia. Keep each origin, association and genetic clue paired."),
    (S8, "RCC most often causes haematuria, while the classical pain–mass–haematuria triad appears in only 15–20%. Venous tumour thrombi, lung cannonballs and left secondary varicocele reveal spread; raised ESR, PTH-related hypercalcaemia, EPO polycythaemia, Stauffer syndrome, Cushing syndrome, galactorrhoea, anaemia, amyloidosis and Lambert–Eaton are the paraneoplastic map. CECT is standard, biopsy is selective and CT angiography maps renal-vein spread."),
    (S9, "Use the RCC TNM table exactly: T1 and T2 are size-confined, T3 reaches veins/perinephric tissues without leaving Gerota, T4 crosses Gerota or enters the ipsilateral adrenal; N1 is para-aortic nodal spread and M1 distant disease, usually lung. Surgery is the mainstay because RCC resists chemo and radiation; choose nephron-sparing surgery when possible, radical nephrectomy when necessary, cryoablation for selected T1a or palliation, and targeted/IL-2 strategies for metastases."),
    (S10, "Wilms tumour is the commonest paediatric renal tumour at 2–5 years, usually a resectable mass that rarely crosses midline, spreads by renal veins and to lung, and links to chromosome 11, Beckwith–Wiedemann, Denys–Drash and WAGR syndromes. CECT stages it, peripheral/intratumoral calcification points toward neuroblastoma, histology determines prognosis, and NWTS starts with surgery whereas SIOP starts with chemotherapy."),
]

UNITS = []
for i, (title, guide) in enumerate(UNIT_DEFS, 1):
    UNITS.append({
        "id": f"SURG-U45-{i}",
        "ch": 45,
        "n": i,
        "title": title,
        "sec": f"{title} · p{first_page(title)}",
        "qs": [x["id"] for x in Q if x["sec"] == title],
        "guide": guide,
    })

covered = [x for u in UNITS for x in u["qs"]]
assert covered == [x["id"] for x in Q]
assert len(set(covered)) == len(covered)
with open("data/ch45.json", "w", encoding="utf-8") as f:
    json.dump({"questions": Q, "units": UNITS}, f, ensure_ascii=False, indent=1)
print(f"ch45: {len(Q)} questions, {len(UNITS)} units")
