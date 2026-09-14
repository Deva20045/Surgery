#!/usr/bin/env python3
"""Build data/ch67.json — Salivary Glands (Marrow Surgery Ed 8, pp520-528)."""
import json

Q = []


def q(page, sec, text, correct, wrongs, note=None):
    opts = [correct] + list(wrongs)
    assert len(opts) == 4
    Q.append({
        "id": f"SURG-C67-{len(Q)+1:03d}",
        "sec": sec,
        "page": page,
        "q": text,
        "opts": opts,
        "ans": 0,
        "exp": (note or correct) + f" (Book p{page})",
    })


# ---------------------------------------------------------------- p520
S1 = "Anatomy of the Salivary Glands"
q(520, S1, "Embryological origin of the parotid gland:", "Ectodermal", ["Endodermal", "Mesodermal", "Neural crest"])
q(520, S1, "Embryological origin of the submandibular and sublingual glands:", "Endodermal", ["Ectodermal", "Mesodermal", "Neural crest"])
q(520, S1, "Duct of the parotid gland:", "Stenson's duct", ["Wharton's duct", "Bartholin's duct", "Rivinus duct"])
q(520, S1, "Stenson's duct opens:", "Opposite the crown of the upper 2nd molar", ["On either side of the frenulum", "Into the floor of mouth posteriorly", "Behind the 3rd molar"])
q(520, S1, "Duct of the submandibular gland:", "Wharton's duct", ["Stenson's duct", "Rivinus duct", "Parotid duct"])
q(520, S1, "Wharton's duct opens:", "On either side of the frenulum", ["Opposite the upper 2nd molar", "Into the tonsillar fossa", "Behind the 3rd molar"])
q(520, S1, "Plane dividing the parotid into superficial and deep lobes:", "Fasciovenous plane", ["Fascio-arterial plane", "Buccopharyngeal fascia", "Stylomandibular ligament"])
q(520, S1, "Structures forming the fasciovenous plane of the parotid:", "Facial nerve, retromandibular vein and external carotid artery", ["Facial nerve, internal jugular vein and internal carotid artery", "Auriculotemporal nerve, facial vein and facial artery", "Hypoglossal nerve, retromandibular vein and ECA"])
q(520, S1, "Proportion of parotid gland formed by the superficial lobe:", "80%", ["20%", "50%", "95%"])
q(520, S1, "Proportion of parotid gland formed by the deep lobe:", "20%", ["80%", "50%", "5%"])
q(520, S1, "Incidence of an accessory parotid gland:", "21-61%", ["1-5%", "5-10%", "80-90%"])
q(520, S1, "Complications if an accessory parotid gland is not removed during parotidectomy:", "Sialocele and fistula formation", ["Frey's syndrome and facial palsy", "Haemorrhage and infection", "Recurrence of cancer only"])

S2 = "Imaging Investigations of Salivary Glands"
q(520, S2, "CECT of the salivary gland is used to:", "Differentiate inflammatory lesions from neoplasms", ["Detect stones", "Differentiate benign from malignant", "Guide FNAC"])
q(520, S2, "Best CT modality for salivary gland stones:", "NCCT", ["CECT", "MRI", "PET-CT"])
q(520, S2, "Imaging used to differentiate benign from malignant salivary tumours:", "MRI", ["NCCT", "CECT", "Plain X-ray"])
q(520, S2, "IOC among imaging modalities for salivary glands, also used to guide FNAC:", "High resolution USG", ["MRI", "NCCT", "PET-CT"])

# ---------------------------------------------------------------- p521
S3 = "Milan System for Salivary Gland Cytopathology"
q(521, S3, "The Milan system is used for:", "FNAC of salivary gland lesions", ["Histopathological grading", "Radiological staging", "Surgical classification"])
q(521, S3, "Risk of malignancy in Milan category I (non-diagnostic):", "25%", ["10%", "20%", "60%"])
q(521, S3, "Management of Milan category I:", "Clinical and radiological correlation / repeat FNAC under imaging guidance", ["Immediate surgery", "Radiotherapy", "No follow up"])
q(521, S3, "Risk of malignancy in Milan category II (non-neoplastic):", "10%", ["25%", "20%", "35%"])
q(521, S3, "Management of Milan category II:", "Clinical follow-up and radiological correlation", ["Surgery", "Repeat FNAC always", "Chemotherapy"])
q(521, S3, "AUS in the Milan system stands for:", "Atypia of undetermined significance", ["Adenoma of uncertain source", "Atypical uncharacterised swelling", "Acinar undifferentiated sarcoma"])
q(521, S3, "Risk of malignancy in Milan category III (AUS):", "20%", ["10%", "25%", "35%"])
q(521, S3, "Management of Milan category III (AUS):", "Repeat FNAC or surgery", ["Clinical follow-up only", "Radiotherapy", "No action"])
q(521, S3, "Risk of malignancy in Milan category IVA (benign neoplasm):", "<5%", ["20%", "35%", "60%"])
q(521, S3, "SUMP in the Milan system stands for:", "Salivary gland neoplasm of uncertain malignant potential", ["Suspicious undetermined malignant pathology", "Salivary undifferentiated malignant process", "Sialadenitis of uncertain metaplastic potential"])
q(521, S3, "Risk of malignancy in Milan category IVB (SUMP):", "35%", ["<5%", "20%", "60%"])
q(521, S3, "Management of Milan category IVB (SUMP):", "Conservative surgery", ["Clinical follow-up alone", "Radical surgery", "Radiotherapy alone"])
q(521, S3, "Risk of malignancy in Milan category V (suspicious for malignancy):", "60%", ["35%", "20%", ">90%"])
q(521, S3, "Risk of malignancy in Milan category VI (malignant):", ">90%", ["60%", "35%", "25%"])
q(521, S3, "Management of Milan category VI:", "Surgery, extent depending on type and grade of malignancy", ["Repeat FNAC", "Clinical follow-up", "Conservative surgery only"])

S4 = "Stafne Bone Cyst and Ranula"
q(521, S4, "Stafne bone cyst is a cyst in the:", "Mandible", ["Maxilla", "Sublingual gland", "Parotid gland"])
q(521, S4, "Stafne bone cyst is the m/c site for:", "Ectopic salivary tissue", ["Ectopic thyroid tissue", "Ectopic pancreas", "Ectopic parathyroid"])
q(521, S4, "Literal translation of 'ranula':", "Frog's belly", ["Little swelling", "Water sac", "Frog's eye"])
q(521, S4, "A ranula is a:", "Mucus extravasation cyst involving the sublingual gland", ["Mucus retention cyst of the parotid", "Lymphatic malformation", "Dermoid cyst"])
q(521, S4, "Clinical features of a ranula:", "Fluctuant swelling in the floor of mouth, brilliantly transilluminant", ["Bony hard swelling in the mandible", "Pulsatile neck swelling", "Non-transilluminant parotid swelling"])
q(521, S4, "Diagnosis of a ranula:", "Based on clinical findings ± FNAC", ["Mandatory CT", "Mandatory biopsy", "Sialography only"])

# ---------------------------------------------------------------- p522
S5 = "Management of Ranula and Plunging Ranula"
q(522, S5, "Management of a ranula:", "Excision of the ranula along with the sublingual gland", ["Incision and drainage", "Marsupialization", "Aspiration alone"])
q(522, S5, "M/c structure injured during ranula excision:", "Submandibular duct", ["Lingual nerve", "Hypoglossal nerve", "Facial artery"])
q(522, S5, "M/c nerve injured during ranula excision:", "Lingual nerve", ["Hypoglossal nerve", "Facial nerve", "Glossopharyngeal nerve"])
q(522, S5, "Why are incision & drainage and marsupialization avoided in ranula:", "High recurrence rate", ["High bleeding risk", "Risk of malignancy", "Poor cosmesis"])
q(522, S5, "Brilliantly transilluminant swellings include all EXCEPT:", "Lipoma", ["Hydrocele", "Cystic hygroma", "Ranula"])
q(522, S5, "Brilliantly transilluminant swelling of the scrotum/epididymis:", "Hydrocele and epididymal cyst", ["Varicocele", "Testicular tumour", "Hernia"])
q(522, S5, "A plunging ranula is a:", "Mucus RETENTION cyst involving the sublingual and submandibular glands", ["Mucus extravasation cyst of the sublingual gland alone", "Lymphatic malformation of the neck", "Branchial cyst"])
q(522, S5, "Clinical features of a plunging ranula:", "Intra oral plus neck swelling", ["Intra oral swelling only", "Neck swelling only", "Parotid swelling"])
q(522, S5, "Investigation for a plunging ranula:", "CT/MRI ± FNAC", ["Sialography only", "Plain X-ray", "PET-CT"])
q(522, S5, "Management of a plunging ranula:", "Excision of the intra oral swelling and sublingual gland plus aspiration of the neck swelling", ["Excision of the neck swelling alone", "Marsupialization", "Observation"])

S6 = "Benign Conditions of Minor Salivary Glands and Parotid Abscess"
q(522, S6, "Natural history of a mucus retention cyst of minor salivary glands:", "M/c resolves spontaneously", ["Always turns malignant", "Always needs excision", "Always recurs"])
q(522, S6, "Management of a mucus retention cyst that does not reduce:", "Simple excision", ["Radiotherapy", "Marsupialization", "Sclerotherapy"])
q(522, S6, "M/c site of acute necrotising sialometaplasia:", "Palate (affecting minor salivary glands)", ["Buccal mucosa", "Floor of mouth", "Parotid gland"])
q(522, S6, "Appearance of acute necrotising sialometaplasia:", "Swelling with a central crater and rolled out margins", ["Flat white patch", "Red velvety patch", "Bony hard swelling"])
q(522, S6, "Purpose of biopsy in acute necrotising sialometaplasia:", "To rule out cancer", ["To confirm infection", "To grade dysplasia", "To plan radiotherapy"])
q(522, S6, "Natural course of acute necrotising sialometaplasia:", "Heals in a few weeks", ["Progresses to cancer", "Needs wide excision", "Persists lifelong"])
q(522, S6, "Risk factor for parotid abscess:", "Immunocompromised state (diabetics)", ["Young age", "Female sex", "Smoking"])
q(522, S6, "Cause of excruciating pain in parotid abscess:", "Stretch of the capsule", ["Nerve infiltration", "Duct obstruction", "Bone erosion"])
q(522, S6, "Fluctuation in parotid abscess is a:", "Late sign", ["Early sign", "Never present", "Diagnostic first sign"])
q(522, S6, "Diagnosis of parotid abscess:", "Clinical diagnosis / USG", ["Mandatory CT", "FNAC", "Sialography"])

# ---------------------------------------------------------------- p523
S7 = "Parotid Abscess Drainage and Recurrent Parotitis of Childhood"
q(523, S7, "Management of a parotid abscess:", "Incision and drainage using Hilton's method", ["Wide local excision", "Total parotidectomy", "Antibiotics alone always"])
q(523, S7, "In Hilton's method the forceps are opened:", "Parallel to the vital structures (facial nerve) while breaking loculi", ["Perpendicular to the facial nerve", "Only after nerve division", "Randomly"])
q(523, S7, "Incision used for draining a parotid abscess:", "Transverse facial incision", ["Vertical midline incision", "Lazy S incision", "Hockey stick incision"])
q(523, S7, "Age group of recurrent parotitis in childhood:", "3-6 years", ["0-1 year", "10-15 years", "16-20 years"])
q(523, S7, "Clinical features of recurrent parotitis in childhood:", "Rapid swelling of one or both glands, aggravated by chewing and eating", ["Painless slow swelling", "Only unilateral fixed swelling", "Swelling unrelated to food"])
q(523, S7, "Typical course of recurrent parotitis in childhood:", "Symptoms for 1 week → quiescent period → recurrence", ["Continuous symptoms lifelong", "Single episode only", "Progression to abscess always"])
q(523, S7, "Investigation of choice in recurrent parotitis of childhood:", "USG", ["MRI", "Sialography", "PET-CT"])
q(523, S7, "Snowstorm appearance on USG refers to:", "Multiple hypo and hyper echoic areas", ["A single anechoic cyst", "Uniform hyperechoic gland", "Calcified duct"])
q(523, S7, "Treatment of recurrent parotitis in childhood:", "Long course of antibiotics plus endoscopic washouts", ["Superficial parotidectomy", "Radiotherapy", "Duct ligation"])

S8 = "Sialolithiasis"
q(523, S8, "Sialolithiasis means:", "Stones in the salivary glands", ["Inflammation of the salivary glands", "Tumour of the salivary glands", "Fistula of the duct"])
q(523, S8, "M/c salivary gland involved by stones:", "Submandibular gland", ["Parotid gland", "Sublingual gland", "Minor salivary glands"])
q(523, S8, "Reasons submandibular stones are commoner:", "Antigravity drainage and more viscous secretions", ["Shorter duct and watery secretions", "Ectodermal origin", "Higher blood supply"])
q(523, S8, "M/c composition of salivary stones:", "Calcium phosphate — Ca3(PO4)2", ["Calcium oxalate", "Uric acid", "Cystine"])
q(523, S8, "Classical presentation of sialolithiasis:", "Post prandial painful neck swelling", ["Painless slow growing swelling", "Fever with rash", "Nocturnal swelling"])
q(523, S8, "IOC for sialolithiasis:", "NCCT", ["CECT", "MRI", "USG"])
q(523, S8, "Percentage of salivary stones that are radio opaque:", "80%", ["20%", "50%", "100%"])
q(523, S8, "First line treatment of sialolithiasis:", "Endoscopic management", ["Duct slitting", "ESWL", "Gland excision"])
q(523, S8, "Stones amenable to endoscopic management:", "<5 mm distal stones and intraparenchymal 5-7 mm stones", [">10 mm distal stones", "All stones regardless of size", "Only non-visualised stones"])
q(523, S8, "Management if endoscopy fails or the distal stone is >5 mm:", "Duct slitting", ["ESWL", "Gland excision", "Observation"])
q(523, S8, "Management of a non-palpable and non-visualized stone:", "ESWL", ["Duct slitting", "Endoscopy", "Gland excision"])
q(523, S8, "Excision of the gland in sialolithiasis is:", "The last resort", ["The first line", "Never done", "Routine"])
q(523, S8, "NCCT is the IOC in all of the following EXCEPT:", "Salivary gland tumour", ["Salivary stone", "Renal stone", "Head injury"])

# ---------------------------------------------------------------- p524
S9 = "Salivary Gland Tumors: Distribution and Parotid Tumors"
q(524, S9, "Rule regarding gland size and tumour behaviour:", "Larger glands m/c benign tumors, smaller glands m/c malignant tumors", ["Larger glands m/c malignant", "All glands equally malignant", "Only minor glands get benign tumours"])
q(524, S9, "Percentage of parotid tumours that are benign:", "90%", ["50%", "20%", "10%"])
q(524, S9, "Percentage of submandibular gland tumours that are malignant:", "50%", ["10%", "80%", "90%"])
q(524, S9, "Percentage of sublingual gland tumours that are malignant:", "80%", ["10%", "50%", "20%"])
q(524, S9, "Percentage of minor salivary gland tumours that are malignant:", "90%", ["10%", "50%", "80%"])
q(524, S9, "Classical clinical sign of a parotid tumour:", "Swelling on the side of the face that lifts the ear lobule", ["Swelling depressing the ear lobule", "Midline neck swelling", "Swelling moving with deglutition"])
q(524, S9, "M/c lobe involved in parotid tumours:", "Superficial lobe", ["Deep lobe", "Accessory lobe", "Both equally"])
q(524, S9, "Cause of pain in parotid tumour:", "Stretching of the capsule/fascia", ["Duct obstruction", "Bone erosion", "Venous congestion"])
q(524, S9, "Sign of deep lobe parotid enlargement:", "Tonsillar fossa pushed medially", ["Ear lobule depressed", "Trismus only", "Tongue deviation"])
q(524, S9, "IOC for a parotid tumour:", "FNAC", ["CT", "MRI", "Biopsy"])
q(524, S9, "M/c parotid tumour overall (benign):", "Pleomorphic adenoma", ["Warthin's tumor", "Hemangioma", "Mucoepidermoid carcinoma"])
q(524, S9, "M/c parotid tumour in children:", "Hemangioma", ["Pleomorphic adenoma", "Warthin's tumor", "Adenoid cystic carcinoma"])
q(524, S9, "M/c malignant parotid tumour:", "Mucoepidermoid carcinoma", ["Adenoid cystic carcinoma", "Acinic cell carcinoma", "Squamous cell carcinoma"])

S10 = "Pleomorphic Adenoma"
q(524, S10, "M/c tumour of the parotid gland:", "Pleomorphic adenoma", ["Warthin's tumor", "Mucoepidermoid carcinoma", "Adenoid cystic carcinoma"])
q(524, S10, "Demographics of pleomorphic adenoma:", "M/c in females, 5th decade (range 3rd-6th decade)", ["M/c in males, 6th decade", "M/c in children", "M/c in males, 2nd decade"])
q(524, S10, "Clinical features of pleomorphic adenoma:", "Slow growing parotid swelling commonly involving the superficial lobe", ["Rapidly growing painful swelling", "Bilateral deep lobe swelling", "Ulcerated swelling with nodes"])
q(524, S10, "IOC for pleomorphic adenoma:", "FNAC", ["CT", "MRI", "Excision biopsy"])
q(524, S10, "HPE of pleomorphic adenoma:", "Epithelial/myoepithelial component in a myxoid background — a triphasic tumour", ["Two layers of oncocytic cells with lymphoid stroma", "Swiss cheese pattern", "Mucous and epidermoid cells"])
q(524, S10, "IHC pattern of pleomorphic adenoma:", "CK7 strong and diffuse", ["cKit positive ductal cells only", "CD34 positive", "Chromogranin positive"])
q(524, S10, "Markers expressed by myoepithelial cells in pleomorphic adenoma:", "p63, S-100, SOX10, SMA", ["cKit, CEA, CA-125", "CD20, CD3", "TTF-1, napsin"])

# ---------------------------------------------------------------- p525
S11 = "Pleomorphic Adenoma Management and Carcinoma Ex-pleomorphic Adenoma"
q(525, S11, "Management of pleomorphic adenoma:", "Superficial parotidectomy", ["Enucleation", "Radiotherapy", "Total radical parotidectomy"])
q(525, S11, "Cause of high recurrence in pleomorphic adenoma:", "Finger like projections left behind if not removed", ["Lymphatic spread", "Multicentric origin in both glands", "Haematogenous spread"])
q(525, S11, "Mixed malignant tumor is also called:", "Carcinoma ex-pleomorphic adenoma", ["Warthin's tumor", "Adenoid cystic carcinoma", "Acinic cell carcinoma"])
q(525, S11, "Carcinoma ex-pleomorphic adenoma arises from:", "Malignant transformation in a long standing pleomorphic adenoma", ["A Warthin's tumour", "De novo in minor glands", "A ranula"])
q(525, S11, "Features suggesting malignancy in a parotid swelling include all EXCEPT:", "Slow painless growth over years", ["Rapid increase in size", "Facial nerve involvement", "Ulceration and lymph node involvement"])
q(525, S11, "IOC for carcinoma ex-pleomorphic adenoma:", "FNAC", ["CT", "MRI", "PET-CT"])
q(525, S11, "Management of carcinoma ex-pleomorphic adenoma:", "Surgery followed by radiotherapy", ["Radiotherapy alone", "Chemotherapy alone", "Observation"])

S12 = "Warthin's Tumor"
q(525, S12, "Warthin's tumor is also known as:", "Adenoma lymphomatosum", ["Ackerman tumor", "Ameloblastoma", "Oncocytoma"])
q(525, S12, "Warthin's tumor is the:", "2nd m/c parotid tumor", ["M/c parotid tumor", "M/c malignant parotid tumor", "M/c childhood tumor"])
q(525, S12, "Strong aetiological associations of Warthin's tumor:", "Smoking and radiation exposure", ["Betel quid and alcohol", "HPV infection", "Diabetes"])
q(525, S12, "Demographics of Warthin's tumor:", "M/c in males, 6th decade", ["M/c in females, 5th decade", "M/c in children", "M/c in females, 2nd decade"])
q(525, S12, "Site of Warthin's tumor:", "Exclusively seen in the parotid", ["Exclusively submandibular", "M/c sublingual", "Minor salivary glands"])
q(525, S12, "Percentage of Warthin's tumors that are bilateral:", "10%", ["50%", "1%", "90%"])
q(525, S12, "Warthin's tumor typically presents as a:", "Painful parotid swelling", ["Painless hard swelling", "Ulcerated swelling", "Pulsatile swelling"])
q(525, S12, "Malignant transformation in Warthin's tumor is:", "Rare", ["Very common", "Universal", "Seen in 50%"])
q(525, S12, "HPE of Warthin's tumor:", "Two layers of eosinophilic cells rich in mitochondria with lymphocytic infiltration", ["Swiss cheese pattern", "Myxoid background with myoepithelial cells", "Mucous, epidermoid and intermediate cells"])
q(525, S12, "Management of Warthin's tumor:", "Superficial parotidectomy", ["Enucleation", "Radiotherapy", "Total radical parotidectomy"])

S13 = "Mucoepidermoid Carcinoma"
q(525, S13, "M/c salivary gland malignancy in children and young adults:", "Mucoepidermoid carcinoma", ["Adenoid cystic carcinoma", "Acinic cell carcinoma", "Pleomorphic adenoma"])
q(525, S13, "Peak incidence of mucoepidermoid carcinoma:", "2nd decade", ["5th decade", "6th decade", "8th decade"])
q(525, S13, "Risk factor for mucoepidermoid carcinoma:", "Radiation/chemotherapy during childhood", ["Smoking", "Betel quid", "HPV infection"])

# ---------------------------------------------------------------- p526
S14 = "Mucoepidermoid Carcinoma: Features and Management"
q(526, S14, "Clinical features of mucoepidermoid carcinoma:", "Fast growing parotid swelling with possible facial nerve involvement", ["Slow painless swelling", "Bilateral swelling", "Swelling in childhood only"])
q(526, S14, "IOC for mucoepidermoid carcinoma:", "FNAC", ["CT", "MRI", "Open biopsy"])
q(526, S14, "Management of LOW grade mucoepidermoid carcinoma:", "Parotidectomy", ["Surgery plus radiotherapy", "Radiotherapy alone", "Chemotherapy"])
q(526, S14, "Management of intermediate/high grade mucoepidermoid carcinoma with infiltrative margins:", "Surgery plus radiotherapy", ["Parotidectomy alone", "Radiotherapy alone", "Observation"])

S15 = "Adenoid Cystic Carcinoma and Treatment Principles"
q(526, S15, "Adenoid cystic carcinoma is the:", "2nd m/c malignant parotid tumor", ["M/c malignant parotid tumor", "M/c benign parotid tumor", "M/c childhood tumor"])
q(526, S15, "Cause of pain in adenoid cystic carcinoma:", "Perineural invasion", ["Capsular stretch", "Duct obstruction", "Bone erosion"])
q(526, S15, "HPE finding in adenoid cystic carcinoma:", "Swiss cheese pattern", ["Triphasic myxoid pattern", "Two layers of oncocytes", "Keratin pearls"])
q(526, S15, "IHC of ductal cells in adenoid cystic carcinoma:", "cKit positive", ["p63 positive", "SMA positive", "S-100 positive"])
q(526, S15, "IHC of myoepithelial cells in adenoid cystic carcinoma:", "p63 and SMA", ["cKit and CEA", "CD34 and CD31", "TTF-1"])
q(526, S15, "Management of adenoid cystic carcinoma:", "Surgery plus radiotherapy", ["Surgery alone", "Radiotherapy alone", "Chemotherapy alone"])
q(526, S15, "Resection margin for malignant salivary gland tumours:", "0.5 cm", ["1 cm", "2 cm", "5 cm"])
q(526, S15, "Indications for elective supraomohyoid neck dissection in salivary malignancy:", "T3/T4 tumors and high grade tumors", ["All T1 tumours", "Benign tumours", "Only node positive disease"])
q(526, S15, "Indications for adjuvant radiotherapy in salivary gland malignancy include all EXCEPT:", "Stage 1 low grade tumour with clear margins", ["Stage 3 & 4 tumors", "High grade tumours", "PNI/LVI and extra nodal spread"])
q(526, S15, "PNI and LVI stand for:", "Perineural invasion and lymphovascular invasion", ["Peripheral nodal involvement and low volume invasion", "Post nodal irradiation and left ventricular index", "Partial nerve injury and lymph vessel inflammation"])

# ---------------------------------------------------------------- p527
S16 = "Surgery for the Parotid Gland"
q(527, S16, "Incision used for parotidectomy:", "Lazy S / modified Blair's incision", ["Transverse facial incision", "Hockey stick incision", "MacFee incision"])
q(527, S16, "Purpose of the lazy S incision placement 2 finger breadths below the angle of mandible:", "Prevent injury to the marginal mandibular nerve", ["Improve cosmesis only", "Reduce bleeding", "Access the deep lobe"])
q(527, S16, "Total CONSERVATIVE parotidectomy involves:", "Superficial plus deep lobe removal with the facial nerve preserved", ["Superficial lobe removal only", "Superficial + deep lobe with facial nerve sacrificed", "Deep lobe removal only"])
q(527, S16, "Total RADICAL parotidectomy involves:", "Superficial lobe, deep lobe and facial nerve sacrificed", ["Facial nerve preserved", "Superficial lobe only", "Nerve grafting without gland removal"])
q(527, S16, "M/c nerve used for cable graft after facial nerve sacrifice:", "Greater auricular nerve", ["Sural nerve", "Hypoglossal nerve", "Lingual nerve"])
q(527, S16, "BEST nerve graft after facial nerve sacrifice:", "Sural nerve graft", ["Greater auricular nerve", "Hypoglossal nerve", "Vagus nerve"])
q(527, S16, "Marginal mandibular nerve (ramus marginalis) injury causes:", "Drooping of the mouth", ["Anaesthesia over the beard region", "Gustatory sweating", "Tongue deviation"])
q(527, S16, "Greater auricular nerve injury causes:", "Anaesthesia over the beard region", ["Drooping of the mouth", "Gustatory sweating", "Shoulder drop"])
q(527, S16, "Most specific pointer for identifying the facial nerve:", "Tragal pointer — nerve lies 1 cm inferior and deep", ["Styloid process", "Posterior belly of digastric", "Retrograde method"])
q(527, S16, "Pointers used to locate the facial nerve include all EXCEPT:", "Hyoid bone", ["Styloid process", "Posterior belly of digastric", "Retrograde method and nerve stimulators"])
q(527, S16, "A LOW output parotid fistula (with gland):", "Closes spontaneously", ["Requires Newman & Seabrook surgery", "Always needs parotidectomy", "Requires radiotherapy"])
q(527, S16, "A HIGH output parotid fistula (with duct) is treated by:", "Newman & Seabrook surgery", ["Observation", "Simple suturing", "Radiotherapy"])

S17 = "Frey's Syndrome"
q(527, S17, "Frey's syndrome is:", "Gustatory sweating", ["Facial drooping", "Anaesthesia over the beard region", "Loss of taste"])
q(527, S17, "Nerve misdirected in Frey's syndrome:", "Auriculotemporal nerve (post ganglionic parasympathetic fibres)", ["Greater auricular nerve", "Marginal mandibular nerve", "Lingual nerve"])
q(527, S17, "Test confirming Frey's syndrome:", "Starch iodine test — true colour confirms diagnosis", ["Allen's test", "Hilton's test", "Schirmer's test"])
q(527, S17, "Non-surgical management options for Frey's syndrome:", "Botox and anti-perspirants", ["Antibiotics", "Steroids", "Radiotherapy"])
q(527, S17, "Definitive management of Frey's syndrome:", "Tympanic neurectomy", ["Botox", "Anti-perspirants", "Total parotidectomy"])
q(527, S17, "Prevention of Frey's syndrome:", "Muscle flap (sternocleidomastoid/digastric) to cover the parotid", ["Wide excision of skin", "Nerve grafting", "Early feeding"])

# ---------------------------------------------------------------- p528
S18 = "Extracapsular Dissection and Submandibular Gland"
q(528, S18, "Extracapsular dissection is done for:", "Benign tumors", ["High grade malignancy", "Adenoid cystic carcinoma", "Recurrent malignancy"])
q(528, S18, "Effect of extracapsular dissection on oncological safety:", "No effect on oncological safety (recurrence)", ["Markedly worsens recurrence", "Eliminates recurrence", "Increases metastasis"])
q(528, S18, "Advantage of extracapsular dissection:", "Less incidence of facial nerve injury and Frey's syndrome", ["Faster wound healing only", "Less bleeding only", "No scar"])
q(528, S18, "Purpose of bimanual palpation in a submandibular swelling:", "To differentiate the gland swelling from lymph nodes", ["To assess the facial nerve", "To detect stones", "To grade malignancy"])
q(528, S18, "On bimanual palpation:", "Submandibular swelling is palpable; lymph nodes are not palpable", ["Both are equally palpable", "Lymph nodes are palpable, gland is not", "Neither is palpable"])
q(528, S18, "M/c BENIGN tumour of the submandibular gland:", "Pleomorphic adenoma", ["Warthin's tumor", "Adenoid cystic carcinoma", "Hemangioma"])
q(528, S18, "M/c MALIGNANT tumour of the submandibular gland:", "Adenoid cystic carcinoma", ["Mucoepidermoid carcinoma", "Pleomorphic adenoma", "Squamous cell carcinoma"])
q(528, S18, "IOC for a submandibular gland swelling:", "FNAC", ["CT", "MRI", "Sialography"])
q(528, S18, "Management of a submandibular gland tumour:", "Submandibular gland excision", ["Enucleation", "Radiotherapy alone", "Observation"])
q(528, S18, "Incision placement in submandibular gland excision:", "2 finger breadths below the angle of mandible to prevent marginal mandibular nerve injury", ["Directly over the angle of mandible", "In the midline of the neck", "Above the mandible"])
q(528, S18, "M/c nerve injured in submandibular gland surgery:", "Marginal mandibular nerve", ["Lingual nerve", "Hypoglossal nerve", "Facial nerve trunk"])
q(528, S18, "Nerves at risk in submandibular gland surgery:", "Lingual, marginal mandibular and hypoglossal nerves", ["Vagus, phrenic and accessory nerves", "Facial trunk and auriculotemporal nerves", "Glossopharyngeal and trigeminal nerves"])
q(528, S18, "Vascular structures injured in submandibular gland surgery:", "Anterior facial vein and facial artery", ["Internal jugular vein and carotid artery", "Retromandibular vein and ECA", "Vertebral artery"])
q(528, S18, "M/c tumour of the sublingual and minor salivary glands:", "Adenoid cystic carcinoma", ["Pleomorphic adenoma", "Warthin's tumor", "Mucoepidermoid carcinoma"])
q(528, S18, "Management of sublingual and minor salivary gland tumours:", "Excision plus radiotherapy", ["Excision alone", "Radiotherapy alone", "Chemotherapy alone"])

UNIT_DEFS = [
    (S1, "The parotid is ectodermal; submandibular and sublingual glands are endodermal. Stenson's duct opens opposite the crown of the upper 2nd molar, Wharton's duct on either side of the frenulum. The fasciovenous plane — facial nerve, retromandibular vein, external carotid artery — splits the parotid into a superficial lobe (80%) and deep lobe (20%). An accessory parotid gland is present in 21-61% and, if left behind at parotidectomy, causes sialocele and fistula."),
    (S2, "Imaging by purpose: CECT separates inflammation from neoplasm, NCCT detects stones, MRI separates benign from malignant, and high resolution USG is the IOC and guides FNAC."),
    (S3, "Milan system for FNAC: I non-diagnostic 25% (correlate/repeat under imaging); II non-neoplastic 10% (follow up); III AUS 20% (repeat FNAC or surgery); IVA benign <5% (conservative surgery or follow up); IVB SUMP 35% (conservative surgery); V suspicious 60% (surgery); VI malignant >90% (surgery by type and grade)."),
    (S4, "Stafne bone cyst is a mandibular cyst, the m/c site of ectopic salivary tissue. Ranula — 'frog's belly' — is a mucus EXTRAVASATION cyst of the sublingual gland presenting as a fluctuant, brilliantly transilluminant floor of mouth swelling diagnosed clinically ± FNAC."),
    (S5, "Excise the ranula with the sublingual gland; the submandibular duct is the m/c structure and the lingual nerve the m/c nerve injured. I&D and marsupialization recur too often. Brilliantly transilluminant swellings: hydrocele, meningocele, cystic hygroma, epididymal cyst, ranula. A plunging ranula is a mucus RETENTION cyst of sublingual plus submandibular glands giving intraoral and neck swelling — image with CT/MRI ± FNAC, excise the intraoral part with the sublingual gland and aspirate the neck component."),
    (S6, "Mucus retention cysts of minor glands usually resolve; excise if they do not. Acute necrotising sialometaplasia sits on the palate as a central crater with rolled out margins, is biopsied only to exclude cancer, and heals in weeks. Parotid abscess strikes diabetics with excruciating pain from capsular stretch, fever and inflammation; fluctuation comes late and diagnosis is clinical or by USG."),
    (S7, "Drain a parotid abscess by I&D using Hilton's method — forceps opened parallel to the facial nerve — through a transverse facial incision. Recurrent parotitis of childhood affects 3-6 year olds with rapid swelling aggravated by chewing, a week of symptoms then quiescence and recurrence; USG shows a snowstorm of hypo and hyper echoic areas and treatment is a long antibiotic course with endoscopic washouts."),
    (S8, "Sialolithiasis favours the submandibular gland because of antigravity drainage and viscous secretions, with calcium phosphate stones causing post prandial painful swelling. NCCT is the IOC (80% radio opaque). Treat endoscopically for distal stones <5 mm and intraparenchymal 5-7 mm stones, duct slitting if that fails or the distal stone is >5 mm, ESWL for non-palpable non-visualised stones, and gland excision only as a last resort."),
    (S9, "Larger glands mostly harbour benign tumours: parotid 90% benign, submandibular 50/50, sublingual 80% malignant, minor glands 90% malignant. A parotid tumour lifts the ear lobule, usually from the superficial lobe, hurts from capsular stretch, and pushes the tonsillar fossa medially when deep. FNAC is the IOC. M/c parotid tumour is pleomorphic adenoma; in children, hemangioma; m/c malignant is mucoepidermoid carcinoma > adenoid cystic carcinoma."),
    (S10, "Pleomorphic adenoma, the m/c parotid tumour, favours females in the 5th decade and grows slowly in the superficial lobe. FNAC is the IOC; HPE shows a triphasic epithelial/myoepithelial tumour in myxoid background, CK7 strong and diffuse, with myoepithelial cells expressing p63, S-100, SOX10 and SMA."),
    (S11, "Treat pleomorphic adenoma by superficial parotidectomy — its finger like projections cause high recurrence if left. Carcinoma ex-pleomorphic adenoma (mixed malignant tumour) arises in long standing lesions, announced by rapid growth, pain, facial nerve involvement, ulceration and nodes; FNAC confirms and treatment is surgery followed by radiotherapy."),
    (S12, "Warthin's tumor (adenoma lymphomatosum) is the 2nd m/c parotid tumour, strongly linked to smoking and radiation, m/c in males in the 6th decade, exclusive to the parotid, bilateral in 10%, painful, and rarely malignant. HPE shows two layers of mitochondria-rich eosinophilic cells with lymphocytic infiltration; treat with superficial parotidectomy."),
    (S13, "Mucoepidermoid carcinoma is the m/c salivary malignancy of children and young adults, peaking in the 2nd decade, and follows childhood radiation or chemotherapy."),
    (S14, "Mucoepidermoid carcinoma grows fast and may involve the facial nerve; FNAC is the IOC. Low grade disease needs parotidectomy alone, while intermediate and high grade tumours with infiltrative margins need surgery plus radiotherapy."),
    (S15, "Adenoid cystic carcinoma is the 2nd m/c malignant parotid tumour and hurts because of perineural invasion; HPE shows a Swiss cheese pattern with cKit positive ductal cells and p63/SMA positive myoepithelial cells, treated by surgery plus radiotherapy. For malignant salivary tumours generally take a 0.5 cm margin, do elective SOHND for T3/T4 and high grade tumours, and add adjuvant RT for stage 3-4, high grade, positive margins, PNI/LVI or extra nodal spread."),
    (S16, "Parotidectomy uses the lazy S / modified Blair's incision placed to spare the marginal mandibular nerve. Total conservative removes both lobes sparing the facial nerve; total radical sacrifices the nerve, repaired by a cable graft — greater auricular m/c, sural best. Complications: haemorrhage, marginal mandibular injury (drooping mouth), greater auricular injury (beard anaesthesia) and facial nerve injury, prevented by pointers — tragal (most specific, nerve 1 cm inferior and deep), styloid process, posterior belly of digastric, retrograde method and nerve stimulators. Low output fistulae close spontaneously; high output duct fistulae need Newman & Seabrook surgery."),
    (S17, "Frey's syndrome is gustatory sweating from misdirected auriculotemporal post ganglionic parasympathetic fibres, confirmed by the starch iodine test. Manage with botox and anti-perspirants, definitively by tympanic neurectomy, and prevent by covering the parotid with a sternocleidomastoid or digastric muscle flap."),
    (S18, "Extracapsular dissection suits benign tumours: recurrence is unchanged but facial nerve injury and Frey's syndrome are fewer. In a submandibular swelling, bimanual palpation makes the gland palpable while nodes are not; pleomorphic adenoma is the m/c benign and adenoid cystic carcinoma the m/c malignant tumour, diagnosed by FNAC and treated by gland excision through an incision 2 finger breadths below the mandible. Complications: haemorrhage, injury to lingual, marginal mandibular (m/c) and hypoglossal nerves, anterior facial vein and facial artery. Sublingual and minor gland tumours are m/c adenoid cystic carcinoma, treated by excision plus radiotherapy."),
]

first_page = {}
for x in Q:
    first_page.setdefault(x["sec"], x["page"])

UNITS = []
for i, (title, guide) in enumerate(UNIT_DEFS, 1):
    UNITS.append({
        "id": f"SURG-U67-{i}",
        "ch": 67,
        "n": i,
        "title": title,
        "sec": f"{title} · p{first_page[title]}",
        "qs": [x["id"] for x in Q if x["sec"] == title],
        "guide": guide,
    })

covered = [x for u in UNITS for x in u["qs"]]
assert covered == [x["id"] for x in Q]
with open("data/ch67.json", "w", encoding="utf-8") as f:
    json.dump({"questions": Q, "units": UNITS}, f, ensure_ascii=False, indent=1)
print(f"ch67: {len(Q)} questions, {len(UNITS)} units")
