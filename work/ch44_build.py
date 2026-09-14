#!/usr/bin/env python3
"""Build data/ch44.json — Kidney: Part 1 (Marrow Surgery Ed 8, pp327-338)."""
import json

Q = []


def q(page, sec, text, correct, wrongs, note=None):
    opts = [correct] + list(wrongs)
    assert len(opts) == 4
    Q.append({
        "id": f"SURG-C44-{len(Q)+1:03d}",
        "sec": sec,
        "page": page,
        "q": text,
        "opts": opts,
        "ans": 0,
        "exp": (note or correct) + f" (Book p{page})",
    })


# ------------------------------------------------------------------ p327
S1 = "Surgical Anatomy and Applied Renal Relationships"
q(327, S1, "The kidney develops from the:", "Metanephric buds", ["Mesonephric ducts only", "Urogenital diaphragm", "Mullerian ducts"])
q(327, S1, "The kidney is initially located in the:", "Iliac fossa", ["Thoracic cavity", "Scrotum", "Perineum"])
q(327, S1, "During development, the kidney ascends to the:", "Lumbar region", ["Cervical region", "Pelvic outlet", "Mediastinum"])
q(327, S1, "The left renal vein is preferred for renal donation because it is:", "Longer and permits easier anastomosis", ["Shorter and has no tributaries", "Absent on the left", "Connected to the portal vein"])
q(327, S1, "The longer left testicular vein and pampiniform plexus make the patient prone to:", "Varicocele", ["Hydrocele only", "Renal agenesis", "Penile fracture"])
q(327, S1, "Renal-cell carcinoma can cause a secondary varicocele by obstructing the:", "Testicular vein", ["Ureteric orifice", "Portal vein", "Cystic duct"])
q(327, S1, "Nutcracker syndrome is caused by compression of the left renal vein between the:", "Superior mesenteric artery and aorta", ["Inferior mesenteric artery and IVC", "Renal artery and portal vein", "Common iliac arteries"])
q(327, S1, "A renal collar is formed when the left renal vein:", "Splits to encase the aorta", ["Enters the portal vein", "Encases the IVC alone", "Crosses the diaphragm twice"])
q(327, S1, "At the renal hilum, the posterior structure is the:", "Renal pelvis", ["Renal vein", "Renal artery", "Ureteric orifice"])
q(327, S1, "At the renal hilum, the middle structure is the:", "Renal artery", ["Renal pelvis", "Renal vein", "Adrenal vein"])
q(327, S1, "At the renal hilum, the anterior structure is the:", "Renal vein", ["Renal pelvis", "Renal artery", "Ureter"])

# ------------------------------------------------------------------ p328-329
S2 = "Renal Agenesis and Duplication of the Ureteric System"
q(328, S2, "Renal agenesis is usually:", "Unilateral", ["Always bilateral", "Always acquired", "Limited to the adrenal gland"])
q(328, S2, "Renal agenesis is associated with agenesis of the:", "Ureter and hem trigone", ["Gallbladder and CBD", "Pancreatic duct", "Tunica vaginalis"])
q(328, S2, "A male with renal agenesis may also have an:", "Undescended testis", ["Ectopic ovary", "Enlarged prostate at birth", "Acquired varicocele in every case"])
q(328, S2, "A female with renal agenesis may have absent:", "Fallopian tubes", ["Seminal vesicles", "Prostate", "Vasa deferentia"])
q(328, S2, "Renal agenesis may also be associated with an absent:", "Adrenal gland", ["Pancreas", "Spleen in every case", "Thyroid gland"])
q(328, S2, "According to the Weigert–Meyer rule, the ureter draining the upper pole inserts:", "Distally and medially in an ectopic location", ["Proximally and laterally in the bladder", "Only into the renal pelvis", "Into the contralateral ureter"])
q(328, S2, "In a duplicated system, the lower-pole ureter usually inserts:", "More proximally and laterally than the upper-pole ureter", ["Distally and medially in the vagina in every case", "Into the renal artery", "Into the scrotum"])
q(328, S2, "An ectopic ureter in a male may open into the:", "Urethra", ["Gallbladder", "Renal vein", "Stomach"])
q(328, S2, "An ectopic ureter in a female may open into the:", "Vagina", ["Spleen", "Cervix in every case", "Portal vein"])
q(328, S2, "A male with a duplicated ureteric system may present with:", "Recurrent urinary tract infection", ["Obstructive jaundice", "Painless penile plaque", "Haemoptysis only"])
q(328, S2, "A female child who is always wet but can pass urine normally may have:", "An ectopic upper-pole ureter", ["Bilateral renal agenesis", "A ureteric stone only", "A bladder tumour"])
q(328, S2, "The child with an ectopic upper-pole ureter can still pass urine normally because the:", "Lower-pole ureter opens into the bladder", ["Upper pole is non-functioning in every case", "Kidney drains into the bowel", "Urethra is absent"])
q(329, S2, "The investigation used for a duplicated ureteric system in the chapter is:", "Intravenous urography", ["HIDA scan", "Micturating cystourethrogram only", "Plain skull radiography"])
q(329, S2, "The contrast dye used for intravenous urography is:", "Urografin", ["Methylene blue only", "Barium sulphate", "Indigo carmine only"])
q(329, S2, "The drooping lily sign suggests:", "Duplication with malrotation of the pelvis", ["Renal-cell carcinoma", "Horseshoe kidney", "A ureteric stone"])
q(329, S2, "The treatment of a symptomatic ectopic ureter is:", "Reimplantation of the ectopic ureter", ["Orchidectomy", "Partial penectomy", "Only scrotal support"])

# ------------------------------------------------------------------ p329-330
S3 = "Polycystic Kidney Disease"
q(329, S3, "Infantile polycystic kidney disease is:", "Autosomal recessive", ["Autosomal dominant", "X-linked recessive", "Mitochondrial"])
q(329, S3, "The gene associated with infantile polycystic kidney disease is PKHD1 on chromosome:", "6", ["4", "16", "17"])
q(329, S3, "Infantile polycystic kidney disease is:", "Usually not compatible with life", ["Always compatible with life", "A benign adult condition", "Limited to the urinary bladder"])
q(329, S3, "Death in infantile polycystic kidney disease is related to:", "Hepatic fibrosis", ["Aortic dissection in every case", "Penile cancer", "Gallstone ileus"])
q(329, S3, "Adult polycystic kidney disease is:", "Autosomal dominant", ["Autosomal recessive", "X-linked dominant", "Mitochondrial"])
q(329, S3, "Adult polycystic kidney disease may be caused by PKD1 on chromosome:", "16", ["6", "11", "17"])
q(329, S3, "Another gene associated with adult polycystic kidney disease is PKD2 on chromosome:", "4", ["3", "9", "13"])
q(329, S3, "Adult polycystic kidney disease is generally:", "Compatible with life", ["Incompatible with life at birth", "Limited to one kidney and never progressive", "A disease of the urethra"])
q(329, S3, "In polycystic kidney disease, multiple cysts enlarge and:", "Compress normal renal parenchyma", ["Replace the bladder wall only", "Obstruct the bile duct only", "Always disappear spontaneously"])
q(329, S3, "Adult polycystic kidney disease typically presents in the:", "Late twenties to early thirties", ["Neonatal period only", "First week after birth", "Seventh decade only"])
q(329, S3, "The most common presentation of adult polycystic kidney disease in a young patient is:", "Hypertension", ["Painless penile swelling", "Obstructive jaundice", "A scrotal ulcer"])
q(329, S3, "Other renal presentations of adult polycystic kidney disease include:", "Pain, haematuria and renal failure", ["Only urinary incontinence", "Only nephrotic syndrome in every case", "Only renal colic without cysts"])
q(329, S3, "The most common extrarenal manifestation of polycystic kidney disease is:", "Cysts in the liver", ["Cysts in the thyroid only", "Pancreatic cancer", "A hydrocele"])
q(329, S3, "Other organs that may contain cysts in polycystic kidney disease are the:", "Spleen, pancreas and lungs", ["Heart valves only", "Testis and prostate only", "Gallbladder and appendix only"])
q(329, S3, "An intestinal association of polycystic kidney disease is:", "Colonic diverticulosis", ["Ulcerative colitis in every case", "Appendicitis", "Bowel obstruction from gallstones"])
q(329, S3, "A cardiac association of polycystic kidney disease is:", "Mitral-valve prolapse", ["Aortic coarctation in every case", "Tricuspid atresia", "Patent ductus arteriosus"])
q(329, S3, "A cerebrovascular association of polycystic kidney disease is a:", "Berry aneurysm in the circle of Willis", ["Cavernous haemangioma of the liver", "Cerebellar tumour", "Carotid dissection in every case"])
q(329, S3, "The differential diagnosis of hypertension in a young patient includes:", "Polycystic kidney disease, renal-artery stenosis, pheochromocytoma and hyperthyroidism", ["Only appendicitis", "Only hydrocele and varicocele", "Only chronic cholecystitis"])
q(330, S3, "Ultrasonography in polycystic kidney disease shows:", "Multiple cysts in the kidneys", ["Only a single ureteric stone", "A keyhole bladder", "A collapsed gallbladder"])
q(330, S3, "On prenatal scanning, the renal cystic threshold listed for unilateral or bilateral disease is:", "At least three cysts", ["Exactly one cyst", "At least ten cysts in one kidney", "Only a solid mass"])
q(330, S3, "On prenatal scanning, the bilateral-kidney threshold listed is:", "At least two cysts in both kidneys", ["A single cyst in one kidney", "At least twenty cysts in one kidney", "No cysts"])
q(330, S3, "Medical treatment listed for polycystic kidney disease includes:", "Vasopressin-receptor antagonists and mTOR inhibitors", ["Only antitubercular drugs", "Only chemotherapy", "Only oral iron"])
q(330, S3, "Renal-replacement options in advanced polycystic kidney disease include:", "Dialysis and transplantation", ["Only urethroplasty", "Only hydrocelectomy", "Only radiotherapy"])

# ------------------------------------------------------------------ p330-331
S4 = "Multicystic Dysplastic Kidney and Horseshoe Kidney"
q(330, S4, "A multicystic dysplastic kidney contains:", "Multiple unilateral or bilateral cysts", ["A single normal renal cyst only", "Only a solid renal tumour", "A duplicated bladder"])
q(330, S4, "Bilateral multicystic dysplastic kidneys are:", "Not compatible with life", ["Always asymptomatic and benign", "Compatible with normal adult life", "Treated by urethrotomy alone"])
q(330, S4, "A presentation of multicystic dysplastic kidney is:", "An abdominal lump at birth", ["Painless jaundice in adulthood", "A penile ulcer", "Only a hydrocele"])
q(330, S4, "Multicystic dysplastic kidney in adults may show rapid progression to:", "Renal failure", ["Liver failure only", "Biliary obstruction", "Testicular torsion"])
q(330, S4, "A horseshoe kidney consists of:", "Fused lower ends of the kidneys", ["Fused upper poles only", "Two separate ectopic ureters", "A single renal cyst"])
q(330, S4, "Ascent of a horseshoe kidney is restricted by the:", "Inferior mesenteric artery", ["Superior mesenteric vein", "Celiac trunk only", "Portal vein"])
q(330, S4, "The fused portion of a horseshoe kidney lies approximately at:", "L3–L4", ["T1–T2", "S1–S2", "C7–T1"])
q(330, S4, "The adrenal glands in horseshoe kidney are:", "Normally placed", ["Always fused with the kidney", "Absent in every case", "Located in the pelvis"])
q(330, S4, "A horseshoe kidney may be:", "Asymptomatic", ["Always painful", "Always malignant", "Always associated with jaundice"])
q(330, S4, "A clinical finding in horseshoe kidney can be an abdominal:", "Lump", ["Ulcer", "Fistula", "Scrotal mass only"])
q(330, S4, "Horseshoe kidney may be associated with:", "Hydronephrosis", ["Only pancreatic pseudocyst", "Only phimosis", "Only a hydrocele"])
q(330, S4, "Other complications of horseshoe kidney include:", "Renal calculi and infections", ["Only biliary colic", "Only pulmonary embolism", "Only testicular tumours"])
q(330, S4, "The investigation of choice for horseshoe kidney is:", "Intravenous urography", ["Barium meal", "Micturating cystourethrogram only", "Plain skull radiography"])
q(330, S4, "The IVU appearance of a horseshoe kidney is called the:", "Flower-vase or handshake sign", ["Cobra-head sign", "Keyhole sign", "Drooping-lily sign"])
q(331, S4, "For hydronephrosis or a malrotated pelvis in a horseshoe kidney, the operation is:", "Pyeloplasty to relieve obstruction", ["Routine nephrectomy", "Circumcision", "Orchidectomy"])
q(331, S4, "The fused portion of a horseshoe kidney should generally not be cut because of the risk of:", "Devascularising both kidneys", ["Causing penile fracture", "Producing a ureterocele", "Creating a hydrocele"])
q(331, S4, "The exception to not cutting the fused portion is a horseshoe kidney with:", "A symptomatic abdominal aortic aneurysm", ["An asymptomatic hydrocele", "A small renal cyst", "A simple varicocele"])

# ------------------------------------------------------------------ p331-332
S5 = "Hydronephrosis and PUJ Obstruction"
q(331, S5, "Hydronephrosis is an aseptic dilation of the:", "Pelvicalyceal system", ["Tunica vaginalis", "Biliary tree", "Seminal vesicle"])
q(331, S5, "Hydronephrosis results from intermittent or complete:", "Low urinary tract blockade", ["Portal hypertension", "Bile reflux", "Lymphatic obstruction only"])
q(331, S5, "Normal renal calyces are:", "Cup shaped", ["Coffin-lid shaped", "Blunt and clubbed", "Cobra headed"])
q(331, S5, "Blunt or clubbed calyces suggest:", "Hydronephrosis", ["A normal renal pelvis", "A hydrocele", "A penile tumour"])
q(331, S5, "The most common acquired intraluminal cause of hydronephrosis is:", "Renal calculi", ["Renal agenesis", "A horseshoe kidney", "A simple cyst"])
q(331, S5, "The most common congenital intramural cause of hydronephrosis is:", "Pelviureteric-junction obstruction", ["A renal tumour", "Bladder diverticulum", "Urethral cancer"])
q(331, S5, "Sloughed renal papillae may be caused by:", "Diabetes mellitus and analgesic abuse", ["Only hypertension", "Only varicocele", "Only appendicitis"])
q(331, S5, "An adynamic obstruction is classified as an:", "Intramural cause of hydronephrosis", ["Extrinsic vascular cause only", "Intraluminal stone", "Infective bladder tumour"])
q(331, S5, "A transitional-cell carcinoma of the renal pelvis produces which IVU sign?", "Goblet sign", ["Fish-hook sign", "Flower-vase sign", "Keyhole sign"])
q(331, S5, "A clinical consequence of hydronephrosis is:", "Decreased renal function", ["Increased spermatogenesis", "Painless penile curvature", "A clear hydrocele"])
q(331, S5, "The investigation of choice for assessing renal function in hydronephrosis is:", "MAG-3 renal isotope scan", ["Plain X-ray alone", "HIDA scan", "Barium enema"])
q(331, S5, "A symptomatic pelviureteric-junction obstruction is treated with:", "Anderson–Hynes pyeloplasty", ["Jaboulay procedure", "Nesbit procedure", "Partial penectomy"])
q(332, S5, "A ureterocele is:", "Dilatation of the terminal ureter", ["Dilatation of the renal artery", "A cyst of the testis", "A bladder tumour"])
q(332, S5, "Ureterocele may produce recurrent:", "Urinary tract infection", ["Painless jaundice", "Haematemesis", "Scrotal pain only"])
q(332, S5, "A functional consequence of ureterocele is:", "Decreased renal function", ["Increased GFR in every case", "Increased bile flow", "Normal renal function in every case"])
q(332, S5, "The IVU appearance of a ureterocele is the:", "Cobra-head or adder-head sign", ["Goblet sign", "Drooping-lily sign", "Reverse-J sign"])
q(332, S5, "Ultrasonography in ureterocele shows:", "Dilated terminal ends of the ureters", ["Only a solid renal mass", "A normal bladder in every case", "A gallbladder stone"])
q(332, S5, "Endoscopic treatment of ureterocele is performed to:", "Ensure drainage", ["Create a renal collar", "Remove the adrenal gland", "Treat a penile plaque"])
q(332, S5, "Definitive surgery for a symptomatic ureterocele may include excision and:", "Reimplantation of the ureter", ["Orchidectomy", "Perineal urethrostomy", "Pancreatectomy"])
q(332, S5, "An aberrant renal vessel causing hydronephrosis is usually:", "Unilateral", ["Always bilateral", "Only intraluminal", "A type of ureterocele"])
q(332, S5, "The treatment of obstruction from an aberrant renal vessel is:", "Pyeloplasty", ["Cutting the vessel in every case", "Radiotherapy", "Circumcision"])
q(332, S5, "An aberrant renal vessel should not be cut because it can:", "Devascularise the kidney", ["Cause a hydrocele", "Produce a penile fracture", "Create a keyhole bladder"])
q(332, S5, "Advanced cancers that can cause extraluminal ureteric obstruction include:", "Soft-tissue sarcoma, cervical, prostatic and colonic cancers", ["Only thyroid cancer", "Only skin cancer", "Only gallbladder stones"])
q(332, S5, "When advanced cancer causes ureteric obstruction, treatment is directed at the:", "Cancer", ["Scrotum", "Foreskin", "Seminiferous tubules"])
q(332, S5, "Retroperitoneal fibrosis is also called:", "Ormond's disease", ["Courvoisier's disease", "Young's disease", "Cabanas disease"])
q(332, S5, "An idiopathic cause of retroperitoneal fibrosis is:", "Idiopathic disease itself", ["A ureterocele", "A hydrocele", "A renal stone only"])
q(332, S5, "A drug associated with retroperitoneal fibrosis is:", "Methysergide", ["Tamsulosin", "Urografin", "Dactinomycin"])
q(332, S5, "Another drug associated with retroperitoneal fibrosis is:", "Bromocriptine", ["Cisplatin", "Xylocaine", "Bleomycin"])
q(332, S5, "IgG-mediated retroperitoneal fibrosis is associated with:", "Dupuytren's contracture and Peyronie's disease", ["Peutz–Jeghers syndrome", "Horseshoe kidney only", "Balanitis only"])
q(332, S5, "Radiotherapy can cause:", "Retroperitoneal fibrosis", ["A simple spermatocele", "Primary hydrocele", "A congenital renal agenesis"])
q(332, S5, "The IVU appearance of retroperitoneal fibrosis is:", "Maiden-waist deformity", ["Cobra-head sign", "Keyhole defect", "Flower-vase sign"])
q(332, S5, "The treatment listed for retroperitoneal fibrosis is:", "DJ stenting", ["Orchidectomy", "Partial penectomy", "Only observation"])

# ------------------------------------------------------------------ p333
S6 = "Retrocaval Ureter and Renal Isotope Scans"
q(333, S6, "In a retrocaval ureter, the ureter lies behind the:", "Inferior vena cava", ["Aorta", "Portal vein", "Superior mesenteric artery"])
q(333, S6, "The IVU sign of a retrocaval ureter is the:", "Fish-hook or reverse-J sign", ["Cobra-head sign", "Goblet sign", "Drooping-lily sign"])
q(333, S6, "The treatment of retrocaval ureter includes:", "Lateralization of the ureter with a DJ stent to maintain patency", ["Total nephrectomy in every case", "Dorsal slit surgery", "Only antibiotics"])
q(333, S6, "A bilateral cause of hydronephrosis listed is:", "Benign prostatic hyperplasia", ["A unilateral hydrocele", "A renal cyst in one pole", "A penile plaque"])
q(333, S6, "Another bilateral cause of hydronephrosis is:", "Bladder-outlet obstruction", ["A spermatocele", "A straddle injury only", "An ectopic testis"])
q(333, S6, "Posterior urethral valve can cause:", "Bilateral hydronephrosis", ["Only unilateral varicocele", "Only a renal cyst", "Only a penile tumour"])
q(333, S6, "Severe phimosis can cause:", "Bilateral hydronephrosis", ["A horseshoe kidney", "A ureterocele in every case", "A pancreatic cyst"])
q(333, S6, "Meatal stenosis is listed as a cause of:", "Bilateral hydronephrosis", ["A renal collar", "Polycystic kidney disease", "A hydrocele"])
q(333, S6, "The best isotope for assessing renal function is:", "MAG-3", ["DMSA", "HIDA", "PET-CT"])
q(333, S6, "Technetium-99m DMSA is used to assess:", "Structural anomalies and scarring", ["Only renal blood flow", "Only ureteric obstruction", "Only bladder capacity"])
q(333, S6, "DTPA and MAG-3 isotope studies assess:", "Functioning of the kidney", ["Penile blood flow", "Biliary drainage", "Testicular lymphatic drainage"])
q(333, S6, "DMSA can provide:", "Total GFR and differential GFR of the two kidneys", ["Only serum bilirubin", "Only the prostate volume", "Only bladder pressure"])
q(333, S6, "A renal contribution of less than 10% on the isotope study indicates a:", "Non-functioning kidney", ["Normal kidney that needs no follow-up", "Hyperfunctioning kidney", "Simple renal cyst"])
q(333, S6, "The listed treatment for a kidney contributing less than 10% is:", "Nephrectomy", ["Only dietary advice", "Ureteric reimplantation in every case", "Circumcision"])
q(333, S6, "A renal contribution greater than 10% means the kidney should generally be:", "Saved", ["Removed immediately", "Ignored permanently", "Treated by penectomy"])

# ------------------------------------------------------------------ p334-335
S7 = "Renal Stone Types and Composition"
q(334, S7, "The most common stone-inhibiting factor is:", "Citrate", ["Oxalate", "Uric acid", "Cystine"])
q(334, S7, "The most common type of renal stone is:", "Calcium oxalate", ["Cystine", "Uric acid", "Xanthine"])
q(334, S7, "Calcium oxalate stones are formed in:", "Acidic urine", ["Strongly alkaline urine only", "Sterile urine only", "Bile"])
q(334, S7, "Calcium oxalate stones are:", "Radiopaque", ["Always radiolucent", "Visible only on MRI", "Never visible on imaging"])
q(334, S7, "Calcium oxalate monohydrate stones are:", "Dumbbell shaped and very hard", ["Envelope shaped and soft", "Coffin-lid shaped", "Brick-red and radiolucent"])
q(334, S7, "Calcium oxalate monohydrate stones are difficult to break by:", "ESWL", ["MCU", "IVU", "Cystoscopy only"])
q(334, S7, "Calcium oxalate dihydrate stones are:", "Envelope shaped", ["Dumbbell shaped", "Hexagonal", "Coffin-lid shaped"])
q(334, S7, "Calcium oxalate stones with spiculated margins are called:", "Mulberry stones", ["Jack stones", "Staghorn stones", "Cement stones"])
q(334, S7, "Mulberry calcium oxalate stones present early with:", "Pain and haematuria", ["Jaundice and melena", "Painless ascites", "Only fever"])
q(334, S7, "Dietary advice for recurrent calcium oxalate stones includes:", "Reducing fat content", ["Avoiding all calcium", "Increasing oxalate intake", "Avoiding all fluids"])
q(334, S7, "Another dietary measure for recurrent calcium oxalate stones is:", "Increasing calcium intake", ["Eliminating dietary calcium", "Increasing purine intake", "Avoiding pyridoxine"])
q(334, S7, "A medication/nutritional measure listed for recurrent calcium oxalate stones is:", "A large dose of pyridoxine", ["High-dose vitamin D only", "D-penicillamine", "Dactinomycin"])
q(334, S7, "Cholestyramine is listed in the dietary advice for recurrent:", "Calcium oxalate stones", ["Cystine stones only", "Uric acid stones only", "Struvite stones only"])
q(334, S7, "Triple-phosphate or struvite stones are also called:", "Staghorn stones", ["Mulberry stones", "Jack stones", "Coffin stones"])
q(334, S7, "The composition of a struvite stone is:", "Calcium magnesium ammonium phosphate", ["Calcium oxalate monohydrate", "Uric acid only", "Cystine only"])
q(334, S7, "Struvite stones form in:", "Alkaline urine", ["Acidic urine only", "Urine with no infection", "Bile"])
q(334, S7, "The organism associated with struvite stones is:", "Proteus", ["Chlamydia", "Candida only", "Mycobacterium tuberculosis only"])
q(334, S7, "The crystals of struvite stones are:", "Coffin-lid shaped", ["Envelope shaped", "Hexagonal", "Glass-shard shaped"])
q(334, S7, "The smooth surface of a struvite stone allows it to:", "Grow and take the shape of the calyx", ["Dissolve in alkaline urine", "Become radiolucent", "Remain microscopic"])
q(334, S7, "Struvite stones are:", "Radiopaque", ["Radiolucent", "Visible only on PET", "Never detectable"])
q(334, S7, "Cystine stones are:", "Radiopaque", ["Always radiolucent", "Seen only on MRI", "Never visible on X-ray"])
q(334, S7, "Cystine stones are characteristically:", "Very hard with a hexagonal crystalline lattice", ["Soft and envelope shaped", "Coffin-lid shaped", "Brick red and amorphous"])
q(334, S7, "Cystine stones are difficult to break by:", "ESWL", ["IVU", "MCU", "Urine culture"])
q(334, S7, "Cystine stones are seen in:", "Cystinuria", ["Hyperthyroidism", "Horseshoe kidney only", "Balanitis"])
q(334, S7, "Recurrent cystine stones are treated with:", "D-penicillamine", ["Allopurinol", "Cholestyramine", "Pyridoxine only"])
q(335, S7, "Uric-acid stones are the most common:", "Radiolucent renal stones", ["Radiopaque renal stones", "Staghorn stones", "Cystine stones"])
q(335, S7, "Uric-acid crystals are described as:", "Glass shards", ["Coffin lids", "Envelopes", "Hexagonal lattices"])
q(335, S7, "Uric-acid stones may be seen in:", "Tumour lysis syndrome", ["Hypospadias", "Hydrocele", "Posterior urethral valves only"])
q(335, S7, "Recurrent uric-acid stones are treated with:", "Allopurinol", ["D-penicillamine", "Pyridoxine", "Cholestyramine only"])
q(335, S7, "Which is a rare radiolucent stone listed in the chapter?", "Xanthine stone", ["Calcium oxalate", "Struvite", "Cystine"])
q(335, S7, "Xanthine stones are described as:", "Brick red", ["Coffin-lid shaped", "Envelope shaped", "Dumbbell shaped"])
q(335, S7, "Which is another rare stone listed in the chapter?", "Indinavir stone", ["Struvite stone", "Mulberry stone", "Calcium oxalate dihydrate"])

# ------------------------------------------------------------------ p335
S8 = "Renal Stone Presentation and Investigation"
q(335, S8, "The most common presentation of a renal stone is:", "Pain", ["Jaundice", "Painless penile mass", "Haemoptysis"])
q(335, S8, "Fixed renal pain is localized to the renal angle because of distension of the:", "Renal capsule", ["Tunica vaginalis", "Bladder wall only", "Peritoneum alone"])
q(335, S8, "Pain from a stone in the renal pelvis radiates from the:", "Loin to the groin", ["Shoulder to the arm", "Chest to the back", "Perineum to the neck"])
q(335, S8, "Pain from an upper or middle ureteric stone follows the:", "Iliohypogastric or obturator nerve", ["Facial nerve", "Vagus nerve", "Phrenic nerve"])
q(335, S8, "Pain from a lower ureteric stone follows the:", "Ilioinguinal nerve", ["Optic nerve", "Radial nerve", "Greater occipital nerve"])
q(335, S8, "A stone impacted in the intramural ureter produces:", "Strangury", ["Courvoisier's law", "Peyronie's disease", "A hydrocele"])
q(335, S8, "Strangury is characterized by an intense urge to micturate and pain at the:", "Tip of the penis or vagina", ["Renal angle only", "Umbilicus", "Right shoulder"])
q(335, S8, "In strangury, the patient may pass:", "Only a few drops of bloody urine", ["A large volume of clear urine immediately", "Only bile", "No urine ever"])
q(335, S8, "Other presentations of renal stones include:", "Haematuria and hydronephrosis", ["Painless jaundice and ascites", "Cannonball metastases", "Only fever"])
q(335, S8, "Dietl's crisis consists of pain and a palpable mass followed by:", "A large quantity of diluted urine", ["Complete anuria forever", "Haematemesis", "Purulent biliary drainage"])
q(335, S8, "The investigation of choice for renal stones is:", "Non-contrast CT KUB", ["Contrast CT only", "HIDA scan", "Micturating cystourethrogram"])
q(335, S8, "NCCT in renal stones stands for:", "Non-contrast computed tomography", ["Nuclear contrast cystoscopy test", "Nephrocalyceal contrast therapy", "Non-cardiac chest tomography"])

# ------------------------------------------------------------------ p336-337
S9 = "Management of Renal Stones"
q(336, S9, "A renal stone smaller than 5 mm requires:", "No active management", ["Immediate PCNL", "Radical nephrectomy", "Mandatory ureteric reimplantation"])
q(336, S9, "For a symptomatic stone larger than 5–6 mm, the first-line treatment is:", "Medical expulsive therapy", ["Immediate nephrectomy", "Only antibiotics", "Radiotherapy"])
q(336, S9, "The alpha blocker used for medical expulsive therapy is:", "Tamsulosin", ["Allopurinol", "D-penicillamine", "Dactinomycin"])
q(336, S9, "If medical management fails for a symptomatic 5–6 mm stone, the first-line intervention is:", "Extracorporeal shock-wave lithotripsy", ["Open cystolithotomy", "Total penectomy", "Observation forever"])
q(336, S9, "ESWL works by:", "Blast-wave dynamics using ultrasonic waves", ["Chemical dissolution only", "Direct surgical extraction through the urethra", "Radioiodine ablation"])
q(336, S9, "The most common complication of ESWL is:", "Pain", ["Renal agenesis", "Penile fracture", "Biliary fistula"])
q(336, S9, "Another complication of ESWL is:", "Urinary tract infection", ["Peyronie's disease", "Hydrocele", "Aortic coarctation"])
q(336, S9, "Another complication of ESWL is:", "Haematuria", ["Painless jaundice", "Scrotal transillumination", "Bifid clitoris"])
q(336, S9, "Stone street or steinstrasse after ESWL is prevented with a:", "DJ stent", ["Foley catheter only", "Biliary stent", "Peritoneal drain"])
q(336, S9, "ESWL is contraindicated in:", "Pregnancy", ["A normal kidney", "A small ureteric stone", "A patient without infection"])
q(336, S9, "Another contraindication to ESWL is an:", "Uncontrolled bleeding disorder", ["Old healed fracture", "Asymptomatic renal cyst", "Ectopic ureter"])
q(336, S9, "ESWL is avoided in a patient who is:", "Obese", ["Normotensive", "Aged 20 years", "Mildly anaemic only"])
q(336, S9, "A cardiac pacemaker is listed as a:", "Contraindication to ESWL", ["Mandatory indication for ESWL", "Treatment for stricture", "Type of renal stone"])
q(336, S9, "ESWL is contraindicated for a stone larger than:", "1.5 cm", ["0.15 cm", "5 cm", "15 cm"])
q(336, S9, "ESWL is contraindicated for a:", "Very hard cystine or calcium oxalate monohydrate stone", ["Soft uric-acid stone only", "Simple renal cyst", "Small struvite fragment"])
q(336, S9, "A lower-calyx stone is listed as:", "A contraindication to ESWL", ["An absolute indication for ESWL", "A type of bladder stone", "A cause of phimosis"])
q(336, S9, "An obstructed urinary system is listed as:", "A contraindication to ESWL", ["A routine indication for ESWL", "A type of hydrocele", "A form of renal agenesis"])
q(336, S9, "RIRS stands for:", "Retrograde intrarenal surgery", ["Renal isotope reflux study", "Rapid internal renal stenting", "Retroperitoneal incision and renal suturing"])
q(336, S9, "RIRS is indicated for stones:", "Smaller than 2 cm", ["Larger than 5 cm", "Only larger than 10 cm", "Only in the bladder"])
q(336, S9, "RIRS is particularly useful for a stone in the:", "Lower pole", ["Gallbladder", "Prostate", "Scrotum"])
q(336, S9, "RIRS is an alternative to ESWL in:", "Obesity", ["A normal-weight patient with no stone", "Painless jaundice", "Hydrocele"])
q(336, S9, "A musculoskeletal deformity is an indication for:", "RIRS", ["Only open nephrectomy", "Only circumcision", "Only radiotherapy"])
q(337, S9, "URS stands for:", "Ureteroscopic removal of stones", ["Ultrasound renal surgery", "Ureteric reflux scoring", "Urethral repair syndrome"])
q(337, S9, "In URS, the stone is visualized and removed via the:", "Ureter", ["Portal vein", "Scrotal skin", "Bile duct"])
q(337, S9, "The laser used in URS is:", "Holmium:YAG", ["CO2 laser only", "Argon laser only", "Excimer laser only"])
q(337, S9, "The basket used to retrieve a ureteric stone during URS is the:", "Dormia basket", ["Fogarty basket", "Cabanas basket", "Jaboulay basket"])
q(337, S9, "PCNL stands for:", "Percutaneous nephrolithotomy", ["Posterior cystic nephrolithiasis lesion", "Pelvic-caliceal nephron lavage", "Prostatic catheter nephrostomy loop"])
q(337, S9, "PCNL is indicated for stones larger than:", "2 cm", ["2 mm", "5 mm only", "10 cm"])
q(337, S9, "PCNL is indicated when ESWL or RIRS has:", "Failed", ["Never been considered", "Already cured the stone", "Produced a hydrocele"])
q(337, S9, "A lower-pole stone unfavourable for ESWL is an indication for:", "PCNL", ["Only observation", "Only medical expulsive therapy", "Only cystoscopy"])
q(337, S9, "Staghorn calculi are an indication for:", "PCNL", ["Circumcision", "Nesbit's procedure", "HIDA scanning"])
q(337, S9, "A hydronephrotic kidney with a large stone is listed as an indication for:", "PCNL", ["Only oral antibiotics", "Only RIRS in every case", "Only urethral dilatation"])
q(337, S9, "Mini-PCNL uses a tract smaller than:", "28 French", ["2 French", "5 French", "100 French"])
q(337, S9, "Mini-PCNL is useful in children and patients with:", "A smaller disease burden", ["Only a bladder tumour", "Only a renal agenesis", "Only a hydrocele"])
q(337, S9, "The most common complication of PCNL is:", "Bruising", ["Painless jaundice", "Penile fracture", "Cannonball metastasis"])
q(337, S9, "A complication of PCNL is:", "Haematuria", ["A keyhole bladder", "A scrotal cyst", "Bifid clitoris"])
q(337, S9, "Another complication of PCNL is:", "Colonic injury", ["Only renal agenesis", "Only biliary colic", "Only varicocele"])
q(337, S9, "Another complication of PCNL is:", "Pneumothorax", ["Hydrocele", "Peyronie's disease", "Ureterocele"])
q(337, S9, "In the stone-management algorithm, a stone smaller than 5 mm is managed by:", "Observation", ["Immediate PCNL", "Radical nephrectomy", "Open bladder surgery"])
q(337, S9, "In the algorithm, a larger symptomatic stone is first treated with:", "Tamsulosin", ["Dactinomycin", "D-penicillamine", "A dorsal slit"])
q(337, S9, "After failed or contraindicated ESWL, the algorithm proceeds to:", "RIRS or PCNL", ["Only circumcision", "Only radiotherapy", "Only observation"])

# ------------------------------------------------------------------ p338
S10 = "Ureteric and Bladder Stones"
q(338, S10, "The investigation of choice for a ureteric stone is:", "NCCT", ["HIDA scan", "Micturating cystourethrogram", "Barium enema"])
q(338, S10, "A gallbladder stone can mimic a ureteric stone; on a lateral X-ray the gallbladder stone is:", "Anterior", ["Posterior", "Inside the urethra", "Always intrarenal"])
q(338, S10, "A calcified 11th rib is listed as a differential diagnosis of a:", "Ureteric stone", ["Bladder tumour", "Hydrocele", "Penile cancer"])
q(338, S10, "The treatment of a ureteric stone larger than 5 mm listed on this page is:", "Ureteroscopic removal with a Dormia basket", ["Immediate total nephrectomy", "Only oral analgesia forever", "Perineal urethrostomy"])
q(338, S10, "Primary bladder stones are formed in:", "Sterile urine", ["Infected urine only", "Bile", "The renal vein"])
q(338, S10, "Primary bladder stones usually occur in:", "Children", ["Elderly women only", "Patients after nephrectomy only", "Newborn girls only"])
q(338, S10, "The most common primary bladder stone is a:", "Mixed urate stone", ["Cystine stone", "Pure calcium carbonate stone", "Struvite stone only"])
q(338, S10, "Secondary bladder stones are caused by:", "Infection or obstruction", ["Only sterile urine", "Only a renal cyst", "Only a hydrocele"])
q(338, S10, "Secondary bladder stones are usually seen in:", "Adults", ["Only neonates", "Only children", "Only pregnant women"])
q(338, S10, "The common secondary bladder stone listed is:", "Calcium oxalate, or a Jack stone", ["Coffin-lid struvite only", "A cystine lattice", "A uric-acid glass shard only"])
q(338, S10, "Bladder stones may present with:", "Haematuria and pain", ["Painless jaundice", "Only a scrotal mass", "Only a cough"])
q(338, S10, "The investigation of choice for bladder stones is:", "NCCT", ["HIDA scan", "PET-CT only", "Retrograde urethrogram only"])
q(338, S10, "The first-line operation for bladder stone is:", "Perurethral cystolithotomy", ["Radical nephrectomy", "Partial penectomy", "Open splenectomy"])
q(338, S10, "A urethral stricture is a contraindication to perurethral cystolithotomy and is managed with:", "Suprapubic cystolithotomy", ["Only ESWL", "Only circumcision", "Only observation"])
q(338, S10, "A bladder diverticulum is a contraindication to perurethral cystolithotomy and is managed with:", "Suprapubic cystolithotomy", ["RIRS only", "Fulguration of posterior valves", "Hydrocelectomy"])


# ------------------------------------------------------------------ units

def first_page(title):
    return next(x["page"] for x in Q if x["sec"] == title)

UNIT_DEFS = [
    (S1, "The kidney begins from metanephric buds in the iliac fossa and ascends to the lumbar region. Surgical relationships are high yield: the long left renal vein is the preferred donor side, its compression between SMA and aorta causes nutcracker syndrome, and the renal hilum reads posterior pelvis, middle artery, anterior vein."),
    (S2, "Renal agenesis is usually unilateral and travels with ipsilateral ureter/hemitrigone absence plus sex-specific genital anomalies. In a duplicated system, apply Weigert–Meyer: the upper-pole ureter ends distally and medially, producing ectopic drainage and the wet child, while IVU shows the drooping lily sign and symptomatic ectopic ureter is reimplanted."),
    (S3, "Contrast infantile AR PKHD1-on-6 disease, often lethal from hepatic fibrosis, with adult AD PKD1-on-16/PKD2-on-4 disease. Enlarging cysts compress renal tissue and cause young hypertension, pain, haematuria and renal failure; liver cysts, berry aneurysm, diverticulosis and mitral prolapse are the extra-renal map, while advanced disease may need vasopressin antagonists, mTOR inhibition, dialysis or transplant."),
    (S4, "Multicystic dysplastic kidney can be unilateral or lethal when bilateral. Horseshoe kidney is a fused lower-pole kidney held below the inferior mesenteric artery: it may be asymptomatic but brings stones, infection and hydronephrosis; IVU gives a flower-vase/handshake sign, pyeloplasty relieves obstruction, and the isthmus is not divided except for a symptomatic abdominal aortic aneurysm."),
    (S5, "Hydronephrosis is aseptic pelvicalyceal dilation from intraluminal, intramural or extraluminal obstruction. Renal stones are the common acquired intraluminal cause, PUJ obstruction the common congenital intramural cause, and Anderson–Hynes treats symptomatic PUJ obstruction. Remember every named clue: goblet, cobra/adder head, maiden waist and the obstruction-specific repairs."),
    (S6, "A right retrocaval ureter lies behind the IVC and creates a fish-hook/reverse-J outline; lateralization and a DJ stent restore patency. MAG-3 best assesses function, DMSA shows scars and structure, and differential contribution below 10% marks a non-functioning kidney for nephrectomy while a contribution above 10% is saved."),
    (S7, "Citrate inhibits stones; calcium oxalate is common, acidic and radiopaque, struvite is alkaline Proteus-driven staghorn, cystine is hard and hexagonal in cystinuria, and uric acid is the common radiolucent stone linked to tumour lysis. Keep the crystal shapes, dietary measures and recurrent-stone drugs tied to their stone type."),
    (S8, "Stone pain follows anatomy: renal pelvis loin-to-groin, upper/mid ureter along iliohypogastric/obturator pathways, lower ureter along ilioinguinal pathway, and intramural impaction causes strangury. Dietl's crisis ends in a gush of dilute urine; NCCT KUB is the investigation of choice."),
    (S9, "Use the size algorithm without shortcuts: under 5 mm observe; symptomatic 5–6 mm gets tamsulosin and then ESWL if medical therapy fails. ESWL uses blast-wave ultrasound but is avoided in pregnancy, bleeding disorders, obesity, pacemakers, children, large/hard/lower-calyx stones and obstruction; RIRS handles smaller lower-pole stones and PCNL handles large, staghorn, hydronephrotic or previously failed cases."),
    (S10, "NCCT confirms ureteric and bladder stones. Remove ureteric stones over 5 mm ureteroscopically with a Dormia basket; primary bladder stones are sterile, paediatric mixed urate stones, while secondary adult stones follow infection/obstruction and are often calcium oxalate Jack stones. Perurethral cystolithotomy is first line unless urethral stricture or diverticulum calls for suprapubic cystolithotomy."),
]

UNITS = []
for i, (title, guide) in enumerate(UNIT_DEFS, 1):
    UNITS.append({
        "id": f"SURG-U44-{i}",
        "ch": 44,
        "n": i,
        "title": title,
        "sec": f"{title} · p{first_page(title)}",
        "qs": [x["id"] for x in Q if x["sec"] == title],
        "guide": guide,
    })

covered = [x for u in UNITS for x in u["qs"]]
assert covered == [x["id"] for x in Q]
assert len(set(covered)) == len(covered)
with open("data/ch44.json", "w", encoding="utf-8") as f:
    json.dump({"questions": Q, "units": UNITS}, f, ensure_ascii=False, indent=1)
print(f"ch44: {len(Q)} questions, {len(UNITS)} units")
