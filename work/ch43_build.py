#!/usr/bin/env python3
"""Build data/ch43.json — Urethral and Penile Disorders (Marrow Surgery Ed 8, pp318-326)."""
import json

Q = []


def q(page, sec, text, correct, wrongs, note=None):
    opts = [correct] + list(wrongs)
    assert len(opts) == 4
    Q.append({
        "id": f"SURG-C43-{len(Q)+1:03d}",
        "sec": sec,
        "page": page,
        "q": text,
        "opts": opts,
        "ans": 0,
        "exp": (note or correct) + f" (Book p{page})",
    })


# ------------------------------------------------------------------ p318
S1 = "Urethral Anatomy, Investigations and Penile Coverings"
q(318, S1, "The female urethra is approximately:", "3–4 cm long", ["1 cm long", "10–12 cm long", "18–20 cm long"])
q(318, S1, "The short female urethra predisposes females to:", "Urinary tract infection", ["Renal-cell carcinoma", "Testicular torsion", "Penile fracture"])
q(318, S1, "The male urethra is approximately:", "18–20 cm long", ["3–4 cm long", "6–8 cm long", "30–35 cm long"])
q(318, S1, "Which part of the urethra is the most distensible?", "Prostatic urethra", ["Membranous urethra", "Bulbar urethra", "External urinary meatus"])
q(318, S1, "Which part of the urethra is the shortest and least distensible?", "Membranous urethra", ["Prostatic urethra", "Bulbar urethra", "Penile urethra"])
q(318, S1, "The membranous urethra pierces the:", "Urogenital diaphragm", ["Pelvic diaphragm only", "Tunica vaginalis", "Superficial perineal fascia"])
q(318, S1, "The bulbar urethra is characterized by a:", "Bend", ["Valve at the bladder neck", "Complete absence of erectile tissue", "Connection to the renal pelvis"])
q(318, S1, "The longest portion of the male urethra is the:", "Penile urethra", ["Membranous urethra", "Prostatic urethra", "Bulbar urethra"])
q(318, S1, "The narrowest portion of the urethra is the:", "External urinary meatus", ["Prostatic urethra", "Bulbar urethra", "Membranous urethra"])
q(318, S1, "In a retrograde urethrogram, contrast is inserted through the:", "Penis", ["Bladder by suprapubic puncture", "Renal artery", "Rectum"])
q(318, S1, "A retrograde urethrogram primarily delineates the:", "Distal urethra", ["Renal pelvis", "Proximal ureter", "Bladder dome"])
q(318, S1, "The investigation performed in urethral trauma to delineate the urethral lumen is:", "Retrograde urethrogram", ["HIDA scan", "Barium enema", "Plain skull radiograph"])
q(318, S1, "In a micturating cystourethrogram, dye is placed in the:", "Bladder", ["Scrotum", "Renal vein", "Corpus cavernosum"])
q(318, S1, "A micturating cystourethrogram delineates the:", "Proximal urethra", ["Distal urethra only", "Renal calyces", "Epididymis"])
q(318, S1, "A micturating cystourethrogram is used to diagnose:", "Vesicoureteric reflux", ["Varicocele", "Peyronie's disease", "Penile carcinoma"])
q(318, S1, "The most superficial covering of the penis is the:", "Skin", ["Buck's fascia", "Tunica albuginea", "Corpus spongiosum"])
q(318, S1, "The superficial fascia of the penis is also called:", "Dartos fascia", ["Buck's fascia", "Colles' ligament", "Scarpa's fascia"])
q(318, S1, "The deep fascia of the penis is called:", "Buck's fascia", ["Dartos fascia", "Tunica vaginalis", "Denonvilliers' fascia"])
q(318, S1, "The erectile tissue that surrounds the urethra is the:", "Corpus spongiosum", ["Corpus cavernosum", "Tunica albuginea", "Dartos fascia"])
q(318, S1, "Rupture of the tunica albuginea of the corpora cavernosa produces:", "Fracture shaft of the penis", ["Hydrocele", "Posterior urethral valve", "Varicocele"])

# ------------------------------------------------------------------ p319-320
S2 = "Hypospadias"
q(319, S2, "Hypospadias is the most common:", "Congenital urogenital anomaly", ["Acquired penile malignancy", "Congenital renal tumour", "Cause of adult hydrocele"])
q(319, S2, "In hypospadias, the urethral opening is placed:", "Ventrally", ["Dorsally", "Laterally on the scrotum in every case", "At the umbilicus"])
q(319, S2, "The incidence of hypospadias listed in the chapter is approximately:", "1 in 450 live births", ["1 in 45 live births", "1 in 4,500 live births", "1 in 45,000 live births"])
q(319, S2, "Hypospadias may be associated with:", "Micropenis and an undescended testis", ["Macropenis and bilateral hydrocele only", "Renal agenesis in every case", "Female internal genitalia in every case"])
q(319, S2, "A downward-directed urinary stream in a child suggests:", "Hypospadias", ["Varicocele", "Hydrocele", "Renal colic"])
q(319, S2, "Chordee is defined as:", "Downward bending of the penis", ["Dorsal displacement of the urethra", "Torsion of the testis", "Dilatation of the pampiniform plexus"])
q(319, S2, "Chordee is most prominent when the penis is:", "Erect", ["Flaccid only", "Inside the bladder", "During renal ultrasonography"])
q(319, S2, "A severe chordee can cause:", "Difficulty with intercourse", ["Painless jaundice", "Urinary stone formation only", "Bilateral renal agenesis"])
q(319, S2, "The severity of hypospadias is proportional to the:", "Proximity of the meatus to the proximal penis", ["Length of the renal artery", "Size of the testis only", "Degree of gallbladder distension"])
q(319, S2, "A possible consequence of severe hypospadias is:", "Infertility", ["Cannonball lung metastases", "Biliary obstruction", "Hydatid disease"])
q(319, S2, "The mildest and most common form of hypospadias is:", "Glanular hypospadias", ["Perineal hypospadias", "Scrotal hypospadias", "Penoscrotal hypospadias"])
q(319, S2, "The distal/anterior group of hypospadias includes:", "Glanular, coronal and distal penile varieties", ["Only scrotal and perineal varieties", "Only prostatic and membranous varieties", "Only midshaft disease"])
q(319, S2, "The middle group of hypospadias is represented by the:", "Midshaft variety", ["Glanular variety", "Perineal variety", "Scrotal variety only"])
q(319, S2, "Which is a posterior/proximal form of hypospadias?", "Perineal hypospadias", ["Glanular hypospadias", "Coronal hypospadias", "Distal penile hypospadias"])
q(319, S2, "The most severe form of hypospadias listed is:", "Perineal hypospadias", ["Glanular hypospadias", "Coronal hypospadias", "Distal penile hypospadias"])
q(319, S2, "The treatment of clinically significant hypospadias is:", "Surgery", ["Radiotherapy", "Observation in every case", "Antitubercular therapy"])
q(319, S2, "The usual timing of hypospadias repair is:", "6–12 months of age", ["At 1 week of age", "After 18 years of age", "Only after infertility develops"])
q(319, S2, "Circumcision is avoided before hypospadias repair because the:", "Foreskin may be needed for reconstruction", ["Foreskin causes renal failure", "Foreskin prevents all chordee", "Circumcision causes posterior urethral valves"])
q(319, S2, "The first principle of hypospadias repair is orthoplasty, which corrects:", "Chordee", ["Hydronephrosis", "A ureteric stone", "A renal tumour"])
q(319, S2, "Urethroplasty in hypospadias repair involves:", "Resection and tubularization of the urethra", ["Excision of the kidney", "Eversion of a hydrocele sac", "Ligation of the renal vein"])
q(319, S2, "Glanuloplasty means:", "Reconstruction of the glans", ["Reconstruction of the bladder", "Repair of the renal pelvis", "Removal of the foreskin only"])
q(319, S2, "The fourth principle of hypospadias repair is:", "Skin cover", ["Lymph-node clearance", "Ureteric reimplantation", "Suprapubic cystolithotomy"])
q(320, S2, "A listed repair for distal hypospadias is the:", "Mathieu procedure", ["Fowler–Stephens procedure", "Whipple procedure", "Boari flap"])
q(320, S2, "A listed repair for mid hypospadias is:", "Snodgrass/TIP repair", ["Jaboulay procedure", "Politano–Leadbetter procedure", "Radical nephrectomy"])
q(320, S2, "TIP in hypospadias surgery stands for:", "Tubularized incised plate", ["Total internal penile excision", "Transitional iliac procedure", "Tunica implantation protocol"])
q(320, S2, "A listed repair for proximal hypospadias is:", "Thiersch–Duplay repair", ["Mathieu repair only", "Lord's plication", "Nesbit's procedure"])
q(320, S2, "The proximal hypospadias repair listed is a:", "Two-stage repair", ["Single-stage renal transplant", "Three-stage bladder diversion", "Non-operative treatment"])
q(320, S2, "A postoperative complication of hypospadias repair is:", "Meatal stenosis", ["Courvoisier's law", "Biliary fistula", "Renal collar formation"])
q(320, S2, "A urethral cutaneous fistula is a complication of:", "Hypospadias repair", ["Horseshoe kidney", "Varicocele embolisation", "Hydrocele transillumination"])
q(320, S2, "Recurrence of chordee after hypospadias repair is attributed to:", "Fibrosis", ["Gallstone impaction", "A patent processus vaginalis", "Pyloric stenosis"])

# ------------------------------------------------------------------ p320
S3 = "Ectopia Vesicae"
q(320, S3, "Ectopia vesicae involves deficiency of the anterior abdominal wall and the:", "Anterior wall of the bladder below the umbilicus", ["Posterior wall of the stomach", "Renal cortex above the diaphragm", "Tunica vaginalis"])
q(320, S3, "The prognosis of ectopia vesicae is described as:", "Poor", ["Uniformly excellent", "Unrelated to the defect", "Better than an isolated hydrocele"])
q(320, S3, "A typical presentation of ectopia vesicae is:", "Urine dribbling from the bladder", ["Painless haematuria only", "A bag-of-worms scrotum", "Obstructive jaundice"])
q(320, S3, "Pelvic diastasis in ectopia vesicae is treated with:", "Iliac osteotomy", ["Radical nephrectomy", "Orchidectomy", "Hepaticojejunostomy"])
q(320, S3, "Ectopia vesicae may be associated with:", "Bilateral congenital inguinal hernias", ["Bilateral renal tumours in every case", "A single acquired femoral hernia only", "Gallstone ileus"])
q(320, S3, "In a male with ectopia vesicae, an associated genital finding may be:", "Undescended testis", ["Hypospadias is impossible", "Bilateral varicocele in every case", "A testicular tumour at birth"])
q(320, S3, "In a female with ectopia vesicae, an associated finding may be:", "Bifid clitoris", ["Absent urethra in every case", "A prostate gland", "A hydrocele"])
q(320, S3, "Complications of ectopia vesicae include:", "Recurrent infections and strictures", ["Only biliary colic", "Only pulmonary embolism", "Only pancreatic fistula"])

# ------------------------------------------------------------------ p320-321
S4 = "Urethral Trauma and Stricture Management"
q(320, S4, "The usual site of an anterior urethral injury is the:", "Bulbar or penile urethra", ["Prostatic urethra only", "Ureteropelvic junction", "Renal pelvis"])
q(320, S4, "The usual mechanism of anterior urethral injury is:", "Direct trauma or a straddle injury", ["Pelvic fracture only", "A viral infection", "A renal biopsy"])
q(320, S4, "A superficial perineal haematoma after anterior urethral injury is classically:", "Butterfly-shaped and involves the penis and scrotum", ["Cannonball-shaped in the chest", "Confined to the renal angle", "Limited to the upper abdomen"])
q(320, S4, "A clinical feature of anterior urethral injury is:", "Blood at the tip of the meatus", ["A high-riding prostate", "Painless jaundice", "A palpable gallbladder"])
q(320, S4, "Another clinical feature of urethral injury is:", "Inability to pass urine", ["Increased bile flow", "Spontaneous hydrocele resolution", "A normal bladder in every case"])
q(320, S4, "The usual site of a posterior urethral injury is the:", "Prostatic or membranous urethra", ["Distal penile urethra only", "Bulbar urethra only", "External urinary meatus only"])
q(320, S4, "A posterior urethral injury is classically secondary to:", "Pelvic fracture", ["A straddle injury only", "Circumcision", "A ureteric stone"])
q(320, S4, "The haematoma of a posterior urethral injury is typically:", "Deep perineal and may involve the anterior abdominal wall and upper third of the thigh", ["Superficial and limited to the scrotum", "Confined to the glans", "Located in the renal capsule"])
q(320, S4, "Vermooten sign is a:", "High-riding or floating prostate on digital rectal examination", ["Transverse testis on scrotal examination", "Pyriform gallbladder on ultrasound", "Cobra-head ureter on IVU"])
q(320, S4, "Bladder distension is a feature particularly associated with:", "Posterior urethral injury", ["A simple hydrocele", "A varicocele", "A superficial penile cyst"])
q(321, S4, "A Foley catheter should be inserted routinely in a patient with suspected urethral trauma:", "Never", ["Before any assessment in every case", "Only through the scrotum", "Only after forceful manipulation"])
q(321, S4, "A full bladder with symptoms after urethral trauma is managed initially with:", "Suprapubic catheterization", ["Blind Foley catheterization", "Orchidectomy", "Urethral dilatation without imaging"])
q(321, S4, "If the bladder is not full and there is no discomfort after urethral trauma, management is to:", "Wait for bladder filling and allow one trial of micturition", ["Perform immediate nephrectomy", "Give radiotherapy", "Insert a catheter forcefully"])
q(321, S4, "The investigation of choice for urethral injury is:", "Retrograde urethrogram", ["Micturating cystourethrogram only", "HIDA scan", "Plain abdominal radiograph"])
q(321, S4, "On retrograde urethrogram, contrast spilling at the injured site suggests:", "Urethral injury", ["A normal urethra", "A renal cyst", "A testicular tumour"])
q(321, S4, "The most common site of a post-traumatic stricture listed is the:", "Bulbomembranous junction", ["External urinary meatus only", "Prostatic apex", "Ureteric orifice"])
q(321, S4, "A short incomplete urethral stricture is managed by passing a guidewire followed by:", "Optical internal urethrotomy or visual internal urethrotomy", ["Radical cystectomy", "Total penectomy", "Hepaticojejunostomy"])
q(321, S4, "The treatment of a short complete urethral stricture is:", "Resection with end-to-end anastomosis", ["Observation for life", "Only oral antibiotics", "Suprapubic nephrostomy"])
q(321, S4, "A long complete urethral stricture is treated by resection followed by:", "A graft to bridge the gap", ["A hydrocele repair", "A renal transplant", "Only balloon dilatation"])
q(321, S4, "The most commonly used graft for a long complete urethral stricture is:", "Buccal mucosal graft", ["Saphenous vein graft", "Pericardial patch only", "Gastric mucosa in every case"])
q(321, S4, "Buccal mucosal graft urethroplasty is also called:", "Barbagli's technique", ["Nesbit's technique", "Grayhack's technique", "Politano's technique"])
q(321, S4, "After excision of a bulbar urethral stricture, the illustrated gap is approximately:", "2 cm", ["0.2 cm", "8 cm", "20 cm"])
q(321, S4, "In the illustrated end-to-end repair, bulbar urethral mobilization provides approximately:", "4–5 cm of lengthening", ["0.5 cm", "1 mm", "10–12 cm"])
q(321, S4, "The ends of the urethra are spatulated by approximately:", "1 cm on each side", ["10 cm on each side", "Only 1 mm on one side", "5 cm on each side"])
q(321, S4, "The illustrated anastomosis uses an overlap of approximately:", "1 cm", ["5 cm", "10 cm", "No overlap is possible"])

# ------------------------------------------------------------------ p322
S5 = "Fracture Shaft of the Penis"
q(322, S5, "Fracture shaft of the penis most commonly occurs when the penis is:", "Erect during sexual intercourse", ["Flaccid during sleep", "Inside the bladder", "During renal ultrasonography"])
q(322, S5, "The pathological lesion in penile fracture is a tear in the corpora cavernosa and/or:", "Tunica albuginea", ["Tunica vaginalis", "Dartos fascia only", "Corpus spongiosum in every case"])
q(322, S5, "A classic clinical feature of penile fracture is a:", "Popping sound", ["Cough impulse", "Bruit over the renal artery", "Painless urinary stream"])
q(322, S5, "The typical external appearance in penile fracture is:", "Eggplant deformity", ["Bag-of-worms deformity", "Cannonball deformity", "Pyriform deformity"])
q(322, S5, "Penile fracture commonly causes:", "Pain and swelling", ["Painless jaundice", "Only microscopic haematuria", "A high-riding prostate"])
q(322, S5, "The operative management of penile fracture includes:", "Drainage of the haematoma and repair of the tear", ["Observation without repair", "Orchidectomy", "Perineal urethrostomy in every case"])
q(322, S5, "Oral contraceptive pills are given for one month after penile-fracture repair to:", "Prevent erection", ["Prevent renal stones", "Treat infection", "Increase spermatogenesis"])

# ------------------------------------------------------------------ p322
S6 = "Posterior Urethral Valves"
q(322, S6, "Posterior urethral valves are seen in:", "Males", ["Females only", "Both sexes equally in the chapter", "Only elderly women"])
q(322, S6, "Posterior urethral valves are:", "One-way valves", ["Two-way ureteric valves", "A type of penile tumour", "A form of hydrocele"])
q(322, S6, "Posterior urethral valves can cause:", "Hydronephrosis", ["Varicocele only", "Gallstone ileus", "Peyronie's disease"])
q(322, S6, "The most common type in Young's classification of posterior urethral valves is:", "Type I", ["Type II", "Type III", "Type IV"])
q(322, S6, "Type I posterior urethral valves are:", "Mucosal folds arising from the verumontanum", ["A constriction at the external meatus", "A bladder diverticulum", "A ureteric stone"])
q(322, S6, "The rare type in Young's classification listed in the chapter is:", "Type II", ["Type I", "Type III", "Type V"])
q(322, S6, "Cobb's collar is classified as:", "Type III posterior urethral valve", ["Type I", "Type II", "Type IV"])
q(322, S6, "A clinical feature of posterior urethral valves is:", "Recurrent urinary tract infection in a male child", ["Painless scrotal swelling only", "Haematemesis", "Adult obstructive jaundice"])
q(322, S6, "The key micturating cystourethrogram finding in posterior urethral valves is a:", "Keyhole defect", ["Double-duct sign", "Cobra-head sign", "Frostberg reverse 3 sign"])
q(322, S6, "The treatment of posterior urethral valves is:", "Fulguration of the valves", ["Hydrocelectomy", "Total nephrectomy in every case", "Radiotherapy"])

# ------------------------------------------------------------------ p323
S7 = "Peyronie's Disease"
q(323, S7, "Peyronie's disease is caused by:", "Calcific deposition in the corpora", ["A dilated pampiniform plexus", "A patent processus vaginalis", "A ureteric obstruction"])
q(323, S7, "In Peyronie's disease, the penis bends:", "Towards the plaque", ["Away from the plaque in every case", "Only towards the scrotum", "Only during micturition"])
q(323, S7, "The curvature of Peyronie's disease is most pronounced during:", "Erection", ["Sleep", "Renal dialysis", "Defecation"])
q(323, S7, "A clinical problem caused by Peyronie's disease is:", "Difficulty during intercourse", ["Painless jaundice", "Loss of renal function in every case", "Haematemesis"])
q(323, S7, "Peyronie's disease is associated with:", "Retroperitoneal fibrosis and Dupuytren's contracture", ["Peutz–Jeghers syndrome", "Courvoisier's law", "Fournier's gangrene only"])
q(323, S7, "In the active phase of Peyronie's disease, the bend:", "Increases", ["Disappears immediately", "Remains constant", "Rotates to the opposite side"])
q(323, S7, "In the stabilization phase of Peyronie's disease, the bend:", "Remains constant", ["Always increases", "Always resolves", "Causes renal failure"])
q(323, S7, "The investigation of choice listed for Peyronie's disease is:", "MRI", ["HIDA scan", "Barium meal", "Plain chest radiography"])
q(323, S7, "On examination in Peyronie's disease, the plaque is usually:", "Palpable", ["Invisible and never palpable", "Located in the kidney", "Confined to the scrotal skin"])
q(323, S7, "The new first-line modality listed for Peyronie's disease is intralesional injection of:", "Collagenase Clostridium histolyticum", ["Bleomycin", "Dactinomycin", "Urokinase"])
q(323, S7, "The intralesional collagenase preparation used for Peyronie's disease is:", "Xiaflex", ["Deflux", "Urografin", "BEP"])
q(323, S7, "If collagenase treatment fails, Nesbit's or the 16-dot technique counterbalances the bend with:", "Contralateral non-absorbable sutures", ["Absorbable renal sutures", "A ureteric stent", "A skin graft alone"])
q(323, S7, "An alternative operation for Peyronie's plaque is excision followed by placement of a:", "Bovine pericardial patch", ["Buccal mucosal graft in every case", "Synthetic ureteric tube", "Gastric patch"])

# ------------------------------------------------------------------ p323-324
S8 = "Priapism"
q(323, S8, "Priapism is defined in the chapter as a prolonged erection lasting more than:", "4 hours", ["30 minutes", "1 hour", "24 hours"])
q(323, S8, "An erection lasting more than six hours can lead to:", "Ischaemia and necrosis", ["Spontaneous cure in every case", "Hydrocele formation", "Renal agenesis"])
q(323, S8, "High-flow priapism results from:", "Increased inflow of blood", ["Venous blockade", "Absent arterial flow", "Urethral stricture only"])
q(323, S8, "A cause of high-flow priapism is:", "Trauma", ["Sickle-cell anaemia only", "Leukaemia only", "A hydrocele"])
q(323, S8, "Another cause of high-flow priapism is:", "Papaverine injection", ["A low-calcium diet", "A patent ureter", "Balanitis xerotica obliterans"])
q(323, S8, "Spinal injury can cause:", "High-flow priapism", ["Only low-flow priapism", "Hydrocele", "Testicular tumour"])
q(323, S8, "High-flow priapism is usually:", "Painless", ["Severely painful in every case", "Associated with jaundice", "Associated with haematemesis"])
q(323, S8, "Penile blood gas in high-flow priapism shows:", "Oxygenated blood", ["Deoxygenated blood", "Bile-stained blood", "No blood"])
q(323, S8, "Low-flow or ischaemic priapism is caused by:", "Venous blockade", ["Increased arterial inflow only", "A ureteric stone", "A scrotal sebaceous cyst"])
q(323, S8, "Compared with high-flow priapism, low-flow priapism is:", "More common", ["Less common in every population", "Never painful", "Always caused by trauma"])
q(323, S8, "A cause of low-flow priapism in children is:", "Sickle-cell anaemia", ["Papaverine injection only", "A straddle injury", "A renal cyst"])
q(323, S8, "Leukaemia is listed as a cause of:", "Low-flow priapism", ["High-flow priapism only", "Peyronie's disease", "Hydrocele"])
q(323, S8, "Low-flow priapism is typically:", "Painful", ["Painless", "Associated with a clear hydrocele", "Associated with a soft prostate"])
q(323, S8, "Penile blood gas in low-flow priapism shows:", "Deoxygenated blood", ["Oxygenated blood", "Only lymph", "Urine"])
q(323, S8, "Penile angiography in low-flow priapism demonstrates the:", "Site of vascular blockage", ["Renal artery aneurysm in every case", "Biliary tree", "Testicular lymphatic basin"])
q(324, S8, "The first step listed in the management sequence for priapism is:", "Sedation followed by adrenaline injection into the corpora", ["Immediate orchidectomy", "Radiotherapy", "Observation for one week"])
q(324, S8, "Adrenaline injection into the corpora relieves priapism by causing:", "Vasoconstriction", ["Vasodilatation", "Diuresis", "Bile secretion"])
q(324, S8, "Persistent priapism after medical treatment is managed with:", "Shunt surgery", ["Hydrocelectomy", "Renal transplantation", "Circumcision alone"])
q(324, S8, "The Greyhack shunt is a:", "Corporo-saphenous shunt", ["Portosystemic shunt", "Ureteric reimplantation", "Bladder neck incision"])
q(324, S8, "Persistent high-flow priapism is treated with:", "Embolisation", ["Only antibiotics", "Fulguration of posterior valves", "Partial nephrectomy"])
q(324, S8, "Embolisation in persistent high-flow priapism works by:", "Blocking blood flow", ["Increasing arterial inflow", "Opening the urethra", "Removing the tunica vaginalis"])

# ------------------------------------------------------------------ p324-325
S9 = "Penile Cancers"
q(324, S9, "The commonest penile cancer is:", "Squamous-cell carcinoma", ["Seminoma", "Basal-cell carcinoma of the kidney", "Small-cell lung carcinoma"])
q(324, S9, "The most common gene mutation listed in penile cancer is in:", "p53", ["BRCA1", "PRSS1", "PKD1"])
q(324, S9, "Buschke–Lowenstein tumour is caused by:", "Human papillomavirus", ["Epstein–Barr virus", "Mycobacterium tuberculosis", "Cytomegalovirus"])
q(324, S9, "Buschke–Lowenstein tumour is characteristically:", "Slow growing", ["Rapidly metastatic in every case", "A renal tumour", "A vascular malformation"])
q(324, S9, "Buschke–Lowenstein tumour grows:", "Outwards and has a good prognosis", ["Only into the renal pelvis", "Inwards with uniformly poor prognosis", "Only along the ureter"])
q(324, S9, "Buschke–Lowenstein tumour resembles:", "Verrucous oral cancer", ["Clear-cell RCC", "A hydrocele", "A pancreatic pseudocyst"])
q(324, S9, "Bowen's disease is a premalignant lesion of the penile:", "Shaft", ["Renal cortex", "Glans only", "Scrotal lymph nodes"])
q(324, S9, "Erythroplasia of Queyrat is a premalignant lesion of the:", "Glans", ["Penile shaft only", "Kidney", "Ureter"])
q(324, S9, "Genital warts are caused by:", "Human papillomavirus", ["Hepatitis B virus", "Proteus", "E. coli"])
q(324, S9, "Balanitis xerotica obliterans may lead to:", "Phimosis", ["Varicocele", "Hydronephrosis from a renal stone in every case", "Testicular torsion"])
q(324, S9, "A further premalignant penile condition listed is:", "Leukoplakia", ["Pyloric stenosis", "Cystinuria", "Horseshoe kidney"])
q(324, S9, "The typical penile-cancer growth is:", "Ulceroproliferative and foul smelling", ["A clear transilluminant swelling", "A painless renal-angle mass", "A purely intratesticular lesion"])
q(324, S9, "In penile cancer, inguinal lymph nodes are positive in approximately:", "50% of cases", ["1% of cases", "5% of cases", "100% of cases"])
q(324, S9, "Inguinal lymph-node enlargement in penile cancer may be due to:", "Infection or cancer", ["Only a hydrocele", "Only renal agenesis", "Only a benign varicocele"])
q(324, S9, "The biopsy finding supporting penile squamous-cell carcinoma is:", "Keratin pearls", ["Psammoma bodies", "Coffin-lid crystals", "Reed–Sternberg cells"])
q(324, S9, "Local staging of penile cancer is performed with:", "MRI", ["HIDA scan", "Micturating cystourethrogram", "Plain abdominal X-ray"])
q(324, S9, "Distant metastasis staging in penile cancer uses:", "PET-CT", ["Retrograde urethrogram", "Barium meal", "Scrotal transillumination"])
q(324, S9, "The staging systems listed for penile cancer include TNM and:", "Jackson's staging", ["Bosniak staging", "Robson staging only", "Young's renal staging"])
q(325, S9, "Bowen disease/in-situ penile cancer can be treated with:", "Topical 5-fluorouracil and laser", ["BEP chemotherapy only", "Immediate radical nephrectomy", "Only antibiotics"])
q(325, S9, "For a primary penile tumour away from the root, the surgical margin listed is:", "0.5 cm", ["0.05 cm", "5 cm", "10 cm"])
q(325, S9, "If the penile stump after resection is more than 2 cm, the operation is:", "Partial penectomy", ["Total nephrectomy", "Hydrocelectomy", "Ureteric reimplantation"])
q(325, S9, "For a deep-seated tumour close to the root, a stump shorter than 2 cm requires:", "Total amputation with perineal urethrostomy", ["Observation only", "Partial nephrectomy", "Endoscopic stone extraction"])
q(325, S9, "Chemotherapy listed for primary penile carcinoma includes:", "5-fluorouracil and cisplatin", ["BEP and carboplatin only", "FOLFOX only", "Dactinomycin and vincristine only"])
q(325, S9, "An enlarged inguinal lymph node in penile cancer should first undergo:", "FNAC", ["Blind excision of the penis", "HIDA scanning", "Renal isotope scanning"])
q(325, S9, "If an enlarged inguinal node is reactive or due to infection, management includes:", "Antibiotics and sentinel lymph-node biopsy", ["Immediate total amputation", "Only radiotherapy", "No assessment"])
q(325, S9, "If an inguinal lymph node contains cancer, listed treatment includes radiotherapy and:", "Ilioinguinal lymph-node clearance", ["Only circumcision", "Perinephric drainage", "A Whipple procedure"])
q(325, S9, "The sentinel lymph-node biopsy described for penile cancer is the:", "Cabanas procedure", ["Mathieu procedure", "Fowler–Stephens procedure", "Anderson–Hynes procedure"])
q(325, S9, "The most important prognostic factor in penile cancer is:", "Lymph-node status", ["Penile length", "Presence of a hydrocele", "Serum amylase"])
q(325, S9, "The commonest cause of death in penile cancer is:", "Erosion of femoral or iliac vessels by lymph nodes", ["Simple phimosis", "A benign scrotal cyst", "A transilluminant hydrocele"])

# ------------------------------------------------------------------ p325-326
S10 = "Phimosis, Circumcision and Paraphimosis"
q(325, S10, "Phimosis is defined as:", "Inability to retract the foreskin", ["Torsion of the testis", "Inability to pass urine from a ureter", "Dilatation of the pampiniform plexus"])
q(325, S10, "Physiological phimosis may persist up to approximately:", "2–6 years of age", ["2–6 weeks of age", "12–15 years in every child", "Adulthood in every child"])
q(325, S10, "Inability to retract the foreskin beyond six years is listed as:", "Symptomatic phimosis", ["A normal adult variant", "Varicocele", "Ectopic testis"])
q(325, S10, "A symptom associated with phimosis is:", "Recurrent urinary tract infection or balanoposthitis", ["Cannonball lung metastases", "Renal artery aneurysm", "Gallstone ileus"])
q(325, S10, "Severe phimosis can cause:", "Hydronephrosis", ["Peyronie's plaque", "A pancreatic tumour", "A renal collar"])
q(325, S10, "Ballooning of the foreskin is a feature of:", "Phimosis", ["Varicocele", "Testicular torsion", "Renal agenesis"])
q(325, S10, "The treatment of symptomatic phimosis is:", "Circumcision", ["Orchidectomy", "Radiotherapy", "Ureteric stenting"])
q(326, S10, "The most common vessel causing haemorrhage after circumcision is the:", "Frenular vessel", ["Renal artery", "Testicular artery", "Dorsal aorta"])
q(326, S10, "Other listed postoperative complications of circumcision include:", "Infection and chordee formation", ["Pancreatitis and jaundice", "Cannonball metastases", "Hydronephrosis in every patient"])
q(326, S10, "Paraphimosis occurs when the foreskin forms a:", "Constriction ring around the penis", ["Ring around the kidney", "Valve in the posterior urethra", "Band around the testis"])
q(326, S10, "The typical presentation of paraphimosis is:", "A swollen painful penis", ["Painless jaundice", "A painless renal mass", "A bag-of-worms scrotum"])
q(326, S10, "Initial conservative management of paraphimosis includes:", "Xylocaine jelly and reduction", ["Immediate nephrectomy", "Radiotherapy", "Only oral chemotherapy"])
q(326, S10, "Multiple punctures in conservative paraphimosis management are followed by:", "Reduction", ["Renal transplantation", "Partial penectomy", "Ureteric reimplantation"])
q(326, S10, "If conservative reduction of paraphimosis fails, the next step is:", "Dorsal slit surgery", ["Bilateral orchidectomy", "Whipple surgery", "Only observation"])


# ------------------------------------------------------------------ units

def first_page(title):
    return next(x["page"] for x in Q if x["sec"] == title)

UNIT_DEFS = [
    (S1, "Map the urethra from the distensible prostatic segment to the narrow external meatus, and keep the investigation direction straight: RGU fills through the penis and shows distal urethra, whereas MCU fills the bladder and demonstrates proximal urethra and reflux. Around the penis, remember the order skin, Dartos, areolar tissue, Buck's fascia and tunica albuginea, with the corpora cavernosa and ventral corpus spongiosum forming the erectile framework."),
    (S2, "Hypospadias is a ventral meatus with severity increasing as the opening moves proximally; glanular disease is mildest and most common, while perineal disease is most severe. Repair at 6–12 months preserves the foreskin for reconstruction and combines chordee correction, urethral tubularization, glanuloplasty and skin cover; know the named distal, mid and proximal procedures and their fistula, stenosis, stricture and recurrent-chordee complications."),
    (S3, "Ectopia vesicae is a poor-prognosis deficiency of the anterior abdominal wall and bladder wall below the umbilicus. Dribbling urine, pelvic diastasis needing iliac osteotomy, bilateral congenital hernias, undescended testis in males, bifid clitoris in females, recurrent infection and strictures are the associated pattern."),
    (S4, "Separate anterior bulbar/penile trauma from posterior prostatic/membranous trauma: straddle injury produces a butterfly superficial haematoma, while pelvic fracture produces deep haematoma, Vermooten's floating prostate and bladder distension. Never pass a Foley blindly; use suprapubic drainage when a full symptomatic bladder demands it and RGU for diagnosis. Match stricture length and completeness to OIU/VIU, end-to-end anastomosis or buccal-mucosal Barbagli graft, including the illustrated spatulation and mobilization measurements."),
    (S5, "Penile fracture is a tear of the corpora cavernosa or tunica albuginea in an erect penis, classically announced by a pop, pain, swelling and eggplant deformity. Drain the haematoma and repair the tear, then use a one-month course of oral contraceptive pills to prevent erection."),
    (S6, "Posterior urethral valves are male one-way valves that produce recurrent UTI and hydronephrosis; Young type I is most common, type II is rare and type III is Cobb's collar. A keyhole defect on MCU points to the diagnosis, and the treatment is valve fulguration."),
    (S7, "Peyronie's disease is a palpable calcific corporal plaque that bends the erect penis towards itself and interferes with intercourse; it travels with retroperitoneal fibrosis and Dupuytren's contracture. Distinguish the active phase, when the angle increases, from stabilization; MRI and examination support diagnosis, collagenase Xiaflex is first line, and failed disease is counterbalanced by Nesbit/16-dot sutures or plaque excision with bovine pericardium."),
    (S8, "Priapism beyond four hours is dangerous, with ischaemia and necrosis after six hours. High-flow disease is painless, oxygenated and inflow-driven after trauma, papaverine or spinal injury; low-flow disease is more common, painful, deoxygenated and venous-blocked in sickle cell disease, children and leukaemia. Follow sedation and intracavernosal adrenaline with Greyhack shunt surgery if persistent, or embolisation for persistent high flow."),
    (S9, "Penile cancer is usually squamous-cell carcinoma with p53 mutation; Buschke–Lowenstein is a slow HPV-related outward-growing verrucous tumour. Know the premalignant site map, keratin pearls, MRI local staging, PET-CT for distant spread, TNM/Jackson systems, margin-based partial versus total amputation, FNAC-led nodal management, Cabanas sentinel biopsy and the prognostic importance of lymph nodes."),
    (S10, "Phimosis is failure to retract the foreskin: physiological to 2–6 years, but symptomatic with persistence, recurrent UTI/balanoposthitis, ballooning or severe hydronephrosis and treated by circumcision. Circumcision most often bleeds from the frenular vessel; paraphimosis is a painful constriction ring, reduced with Xylocaine jelly and punctures or treated by dorsal slit when reduction fails."),
]

UNITS = []
for i, (title, guide) in enumerate(UNIT_DEFS, 1):
    UNITS.append({
        "id": f"SURG-U43-{i}",
        "ch": 43,
        "n": i,
        "title": title,
        "sec": f"{title} · p{first_page(title)}",
        "qs": [x["id"] for x in Q if x["sec"] == title],
        "guide": guide,
    })

covered = [x for u in UNITS for x in u["qs"]]
assert covered == [x["id"] for x in Q]
assert len(set(covered)) == len(covered)
with open("data/ch43.json", "w", encoding="utf-8") as f:
    json.dump({"questions": Q, "units": UNITS}, f, ensure_ascii=False, indent=1)
print(f"ch43: {len(Q)} questions, {len(UNITS)} units")
