#!/usr/bin/env python3
"""Build data/ch66.json — Oral Cancers (Marrow Surgery Ed 8, pp509-519)."""
import json

Q = []


def q(page, sec, text, correct, wrongs, note=None):
    opts = [correct] + list(wrongs)
    assert len(opts) == 4
    Q.append({
        "id": f"SURG-C66-{len(Q)+1:03d}",
        "sec": sec,
        "page": page,
        "q": text,
        "opts": opts,
        "ans": 0,
        "exp": (note or correct) + f" (Book p{page})",
    })


# ------------------------------------------------------------------ p509
S1 = "Squamous Cell Carcinoma of the Oral Cavity"
q(509, S1, "M/c oral and oropharyngeal carcinoma:", "Squamous cell carcinoma", ["Adenocarcinoma", "Melanoma", "Lymphoma"])
q(509, S1, "Staining of keratin pearls:", "Eosinophilic", ["Basophilic", "Amphophilic", "Non-staining"])
q(509, S1, "Well differentiated tumors show:", "Increased number of keratin pearls", ["Decreased keratin pearls", "No keratin pearls", "Only mucin"])
q(509, S1, "Poorly differentiated tumors show:", "Decreased number of keratin pearls", ["Increased keratin pearls", "Abundant keratin", "Only keratin"])
q(509, S1, "M/c gene mutation in oral cancers:", "p53", ["KRAS", "BRCA1", "APC"])
q(509, S1, "M/c site of oral cancer in INDIA:", "Buccal mucosa / gingivo buccal sulcus", ["Lateral border of tongue", "Hard palate", "Floor of mouth"])
q(509, S1, "M/c site of oral cancer WORLDWIDE:", "Lateral border of tongue", ["Buccal mucosa", "Gingivo buccal sulcus", "Lip"])

S2 = "Risk Factors for Oral Cancer"
q(509, S2, "Risk factors for oral cancer include all EXCEPT:", "Dental flossing", ["Smoking", "Alcohol", "Betel quid"])
q(509, S2, "Mechanical risk factor for oral cancer:", "Sharp, ill fitting dentures", ["Soft toothbrush", "Dental floss", "Mouthwash"])
q(509, S2, "Immune-related risk factor for oral cancer:", "Immunosuppression", ["Hyperthyroidism", "Diabetes insipidus", "Anaemia"])
q(509, S2, "Chronic fungal infection predisposing to oral cancer:", "Hyperplastic candidiasis", ["Oral thrush only", "Aspergillosis", "Mucormycosis"])
q(509, S2, "EBV is associated with:", "Nasopharyngeal carcinoma", ["Oral SCC", "Lip carcinoma", "Tongue carcinoma"])
q(509, S2, "Percentage of oral SCC associated with HPV:", "5%", ["50%", "70%", "90%"])
q(509, S2, "Percentage of oropharyngeal SCC associated with HPV:", "50-70%", ["5%", "10%", "100%"])
q(509, S2, "Prognosis of HPV-associated oropharyngeal SCC:", "Better prognosis", ["Worse prognosis", "Same prognosis", "Always fatal"])

S3 = "Pre-malignant Conditions and Verrucous Carcinoma"
q(509, S3, "HIGH risk pre-malignant lesions include:", "Erythroplakia, proliferative verrucous leukoplakia and chronic hyperplastic candidiasis", ["Oral submucous fibrosis and syphilitic glossitis", "Oral lichen planus and DLE", "Ranula and mucocele"])
q(509, S3, "MEDIUM risk pre-malignant lesions:", "Oral submucous fibrosis and syphilitic glossitis", ["Erythroplakia and leukoplakia", "Oral lichen planus and DLE", "Candidiasis"])
q(509, S3, "LOW risk pre-malignant lesions:", "Oral lichen planus and DLE", ["Erythroplakia", "Oral submucous fibrosis", "Chronic hyperplastic candidiasis"])
q(509, S3, "Verrucous carcinoma is also called:", "Ackerman tumor", ["Buschke-Lowenstein tumor", "Warthin tumor", "Ameloblastoma"])
q(509, S3, "Verrucous carcinoma is a variant of:", "Squamous cell carcinoma", ["Adenocarcinoma", "Basal cell carcinoma", "Melanoma"])
q(509, S3, "Viral association of verrucous carcinoma:", "HPV positive", ["EBV positive", "CMV positive", "HIV positive"])
q(509, S3, "Growth pattern of verrucous carcinoma:", "Outward growth, slow growing", ["Deeply invasive, rapidly growing", "Ulcerative, rapid", "Metastatic at presentation"])

# ------------------------------------------------------------------ p510
S4 = "Verrucous Carcinoma Prognosis and Leukoplakia"
q(510, S4, "Prognosis of verrucous carcinoma:", "Good", ["Poor", "Uniformly fatal", "Unpredictable"])
q(510, S4, "Verrucous variant of penile carcinoma:", "Buschke-Lowenstein tumor", ["Ackerman tumor", "Marjolin's ulcer", "Bowen's disease"])
q(510, S4, "Behaviour of Buschke-Lowenstein tumor:", "Slow growing with better prognosis", ["Rapidly growing with poor prognosis", "Always metastatic", "Benign without recurrence"])
q(510, S4, "Common feature of leukoplakia and candidiasis:", "White patches", ["Red patches", "Ulceration", "Pigmentation"])
q(510, S4, "Definition of leukoplakia:", "A white patch not characterized as any other condition", ["A red patch that can be rubbed off", "An ulcer with everted edges", "A white patch that rubs off"])
q(510, S4, "Key clinical distinguishing feature of leukoplakia:", "Cannot be rubbed off", ["Can be rubbed off", "Painful", "Bleeds on touch"])
q(510, S4, "Increase in cancer risk with leukoplakia:", "3-5 times", ["6-9 times", "10-20 times", "No increase"])
q(510, S4, "Management of leukoplakia:", "Eliminate risk factors, antioxidants and excision", ["Radiotherapy", "Chemotherapy", "Antifungals"])
q(510, S4, "Modalities used for excision of leukoplakia:", "CO2 laser and cautery", ["Cryotherapy and radiotherapy", "Sclerotherapy", "Embolisation"])
q(510, S4, "Proliferative verrucous leukoplakia is:", "Multifocal with usually no typical risk factors", ["Unifocal with strong smoking history", "Always associated with alcohol", "Never premalignant"])
q(510, S4, "Cancerous conversion rate of proliferative verrucous leukoplakia:", "High", ["Low", "Nil", "Same as normal mucosa"])
q(510, S4, "Management of proliferative verrucous leukoplakia:", "Excision at the earliest", ["Observation", "Antifungals", "Radiotherapy"])
q(510, S4, "Speckled leukoplakia is:", "Leukoplakia surrounded by a reddish border", ["Leukoplakia with a black border", "Multifocal white plaques", "Depigmented patch"])
q(510, S4, "Management of speckled leukoplakia:", "Excision", ["Observation", "Antifungals", "Chemotherapy"])

S5 = "Hyperplastic Candidiasis and Erythroplakia"
q(510, S5, "Key feature distinguishing hyperplastic candidiasis from leukoplakia:", "Can be rubbed off", ["Cannot be rubbed off", "Is painless", "Is always malignant"])
q(510, S5, "Border of hyperplastic candidiasis:", "Reddish border", ["Black border", "Pigmented border", "No border"])
q(510, S5, "Malignant potential of hyperplastic candidiasis:", "Increased risk of malignancy", ["No risk", "Protective", "Only in children"])
q(510, S5, "Definition of erythroplakia:", "A reddish patch not characterized by other conditions", ["A white patch that rubs off", "An ulcer with rolled edges", "A pigmented macule"])
q(510, S5, "Erythroplakia:", "Cannot be rubbed off", ["Can be rubbed off", "Is always painful", "Always bleeds"])
q(510, S5, "Increase in cancer risk with erythroplakia:", "6-9 times", ["3-5 times", "1-2 times", "No increase"])
q(510, S5, "Most aggressive type of erythroplakia:", "Speckled erythroplakia", ["Homogeneous erythroplakia", "Verrucous erythroplakia", "Nodular erythroplakia"])
q(510, S5, "Management of erythroplakia:", "Eliminate risk factors and excision", ["Antifungals", "Radiotherapy alone", "Observation"])

# ------------------------------------------------------------------ p511
S6 = "Risk of Malignant Change and Oral Submucous Fibrosis"
q(511, S6, "Risk of malignant change in a pre-existing dysplastic lesion is higher in:", "Females", ["Males", "Children", "Smokers only"])
q(511, S6, "Size of lesion associated with increased risk of malignant change:", ">200 mm sq", ["<50 mm sq", ">10 mm sq", ">1000 mm sq"])
q(511, S6, "Lesion homogeneity associated with higher malignant risk:", "Non-homogeneous lesions", ["Homogeneous lesions", "Both equal", "Uniformly white lesions"])
q(511, S6, "Counterintuitive risk factor for malignant change in a dysplastic lesion:", "Non-smoker", ["Heavy smoker", "Alcohol user", "Betel quid chewer"])
q(511, S6, "Number of lesions associated with increased malignant risk:", "Presence of multiple lesions", ["A single lesion", "No lesions", "Only two lesions"])
q(511, S6, "Location with the highest risk of malignant change:", "Lateral border of tongue", ["Hard palate", "Upper lip", "Gingiva"])
q(511, S6, "Oral submucous fibrosis is:", "A hypersensitivity reaction to betel nut", ["A bacterial infection", "An autoimmune disease", "A viral infection"])
q(511, S6, "Sequence of events in oral submucous fibrosis:", "Fibrosis → inadequate mouth opening → poor hygiene → ↑ risk of cancer", ["Ulceration → infection → cancer", "Hyperplasia → dysplasia → cancer directly", "Atrophy → bleeding → cancer"])
q(511, S6, "Examination finding in oral submucous fibrosis:", "White bands in mouth", ["Red velvety patch", "Black pigmentation", "Ulcer with everted edges"])
q(511, S6, "First step in managing oral submucous fibrosis:", "Stop betel quid consumption and smoking", ["Immediate excision", "Radiotherapy", "Antifungals"])
q(511, S6, "Intralesional drug used in oral submucous fibrosis:", "Triamcinolone", ["Bleomycin", "Methotrexate", "Cisplatin"])
q(511, S6, "Reason excision is avoided in oral submucous fibrosis:", "Healing occurs by increased fibrosis", ["High bleeding risk", "Risk of metastasis", "Poor anaesthesia"])
q(511, S6, "Other uses of triamcinolone:", "Keloids, costochondritis and ganglion", ["Cancer chemotherapy", "Antibiotic therapy", "Anticoagulation"])

S7 = "Plummer-Vinson Syndrome"
q(511, S7, "Plummer-Vinson syndrome is also known as:", "Patterson-Kelly-Brown syndrome / sideropenic dysphagia", ["Stewart-Treves syndrome", "Ackerman syndrome", "Ortner's syndrome"])
q(511, S7, "Plummer-Vinson syndrome is common in:", "Perimenopausal women", ["Young men", "Children", "Elderly men"])
q(511, S7, "Haematological feature of Plummer-Vinson syndrome:", "Iron deficiency anemia", ["Megaloblastic anemia", "Polycythemia", "Thrombocytosis"])
q(511, S7, "Nail change in Plummer-Vinson syndrome:", "Koilonychia (spoon shaped nails)", ["Clubbing", "Onycholysis", "Beau's lines"])
q(511, S7, "Oral feature of Plummer-Vinson syndrome:", "Angular cheilitis / stomatitis", ["Macroglossia", "Gingival hyperplasia", "Ranula"])
q(511, S7, "Cause of dysphagia in Plummer-Vinson syndrome:", "Post-cricoid webs", ["Achalasia", "Oesophageal cancer", "Stricture from reflux"])
q(511, S7, "Malignancies associated with Plummer-Vinson syndrome:", "Hypopharyngeal carcinoma and squamous cell carcinoma of esophagus", ["Gastric adenocarcinoma", "Colonic carcinoma", "Thyroid carcinoma"])
q(511, S7, "Management of Plummer-Vinson syndrome:", "Correction of iron deficiency and CO2 excision of webs", ["Total oesophagectomy", "Radiotherapy", "Steroids"])

# ------------------------------------------------------------------ p512
S8 = "Field Cancerisation"
q(512, S8, "Field cancerisation is typically seen in all of the following EXCEPT:", "Thyroid gland", ["Oral cavity", "Bladder", "Colorectal region"])
q(512, S8, "Percentage of synchronous cancer in the colorectal region:", "4%", ["10%", "25%", "50%"])
q(512, S8, "Mechanism of field cancerisation:", "Risk factors involve the entire mucosa producing multiple cancers", ["A single clone metastasizes widely", "Immune failure alone", "Genetic mutation without exposure"])
q(512, S8, "Synchronous cancers develop:", "Within 6 months of the primary cancer", ["After 6 months of the primary", "After 5 years", "Before the primary"])
q(512, S8, "Metachronous cancers develop:", "After 6 months of the primary cancer", ["Within 6 months", "Simultaneously", "Before the primary"])
q(512, S8, "Clinical relevance of field cancerisation:", "Close observation, follow up and screening for other cancers", ["No follow up needed", "Immediate total resection of mucosa", "Prophylactic chemotherapy for all"])

S9 = "Work Up of Oral Cancers"
q(512, S9, "Confirmational investigation for oral cancer:", "Incisional (edge/wedge) biopsy", ["FNAC of the lesion", "CT scan", "PET-CT"])
q(512, S9, "Reason biopsy is taken from the EDGE, not the centre:", "Centre of the lesion is necrotic", ["Edge is easier to reach", "Centre bleeds excessively", "Centre is always benign"])
q(512, S9, "If a biopsy shows infection/inflammatory cells:", "Give antibiotics and repeat the biopsy", ["Declare it benign", "Proceed to surgery", "Start chemotherapy"])
q(512, S9, "IOC for staging oral cancer:", "CECT of PNS, neck and thorax", ["MRI brain", "USG neck", "Plain X-ray"])
q(512, S9, "Depth of invasion (DOI) is measured:", "From the level of the adjacent skin/mucosal surface downwards", ["From the top of the exophytic tumour", "Across the widest tumour diameter", "From the deepest node"])
q(512, S9, "Tumor thickness differs from DOI because it:", "Includes the exophytic component above the surface", ["Excludes the deep component", "Is measured on imaging only", "Is always smaller"])

# ------------------------------------------------------------------ p513
S10 = "TNM Staging (8th AJCC)"
q(513, S10, "Tx in oral cancer staging means:", "Tumour cannot be assessed", ["No tumour", "Carcinoma in situ", "Distant metastasis"])
q(513, S10, "T1 oral cancer:", "Size ≤2 cm, DOI ≤5 mm", ["Size ≤2 cm, DOI 5-10 mm", "Size 2-4 cm", "Size >4 cm"])
q(513, S10, "T2 oral cancer criteria:", "Size ≤2 cm with DOI 5-10 mm, OR size 2-4 cm with DOI <10 mm", ["Size ≤2 cm with DOI ≤5 mm", "Size >4 cm", "Involvement of adjacent structures"])
q(513, S10, "T3 oral cancer:", "Size >4 cm or DOI >10 mm", ["Size ≤2 cm, DOI ≤5 mm", "Size 2-4 cm, DOI <10 mm", "Adjacent structure involvement"])
q(513, S10, "T4 oral cancer:", "Involvement of adjacent structures", ["Size >4 cm only", "DOI >10 mm only", "Nodal involvement"])
q(513, S10, "T4a versus T4b:", "T4a resectable, T4b not resectable", ["T4a not resectable, T4b resectable", "Both resectable", "Both unresectable"])
q(513, S10, "N0 nodal status:", "No lymph nodes involved", ["Single ipsilateral LN ≤3 cm", "Cannot be assessed", "Bilateral nodes"])
q(513, S10, "N1 nodal status:", "Single ipsilateral LN ≤3 cm", ["Single ipsilateral LN >3-6 cm", "Multiple ipsilateral LN ≤6 cm", "Bilateral LN ≤6 cm"])
q(513, S10, "N2a nodal status:", "Single ipsilateral LN >3-6 cm", ["Single ipsilateral LN ≤3 cm", "Multiple ipsilateral LN ≤6 cm", "Bilateral LN ≤6 cm"])
q(513, S10, "N2b nodal status:", "Multiple ipsilateral LN ≤6 cm", ["Single ipsilateral LN ≤3 cm", "Bilateral/contralateral LN ≤6 cm", "Single LN >6 cm"])
q(513, S10, "N2c nodal status:", "Bilateral / contralateral LN ≤6 cm", ["Multiple ipsilateral LN ≤6 cm", "Single ipsilateral LN >3-6 cm", "Extranodal extension"])
q(513, S10, "N3a nodal status:", "Single node >6 cm or extranodal extension", ["Bilateral nodes ≤6 cm", "Single node ≤3 cm", "No nodes"])
q(513, S10, "N3b nodal status:", "Clinical or radiographic extranodal extension — matted nodes or nodes attached to skin", ["Single node >6 cm without extension", "Bilateral nodes ≤6 cm", "No nodes involved"])
q(513, S10, "M0 status:", "No metastasis", ["Distant metastasis", "Cannot be assessed", "Nodal metastasis"])
q(513, S10, "M/c site of distant metastasis in oral cancer:", "Lung", ["Liver", "Bone", "Brain"])

S11 = "Surgical Management of Oral Cancer"
q(513, S11, "R0 resection means:", "Microscopic freedom from disease", ["Macroscopic residual disease", "Microscopic residual disease", "No resection"])
q(513, S11, "Margin taken in wide local excision of oral cancer:", "0.5 cm", ["0.1 cm", "2 cm", "5 cm"])
q(513, S11, "Indication for mandibular resection:", "Involvement of the mandible", ["Any oral cancer", "Nodal involvement", "Lip involvement"])
q(513, S11, "Indication for neck dissection:", "Lymph node involvement", ["Mandibular involvement", "Small T1 lesion", "Distant metastasis"])
q(513, S11, "Commando operation consists of:", "Wide local excision + mandibular resection + neck dissection", ["WLE + radiotherapy", "Mandibular resection alone", "Neck dissection + flap only"])
q(513, S11, "Fourth component of surgical management after resection:", "Reconstruction with flaps", ["Chemotherapy", "Tracheostomy", "Gastrostomy"])

# ------------------------------------------------------------------ p514
S12 = "Lip Cancer Management and Surgical Approaches"
q(514, S12, "Management of lip cancer involving <1/3rd of the lip:", "Wide local excision with primary closure", ["Johanson's step ladder resection", "Flap reconstruction", "Radiotherapy alone"])
q(514, S12, "Management of lip cancer involving >1/3rd to 2/3rd of the lip:", "Johanson's step ladder resection", ["WLE with primary closure", "Flap reconstruction", "Observation"])
q(514, S12, "Management of lip cancer involving >2/3rd of the lip:", "Flap reconstruction", ["WLE with primary closure", "Johanson's step ladder resection", "Chemotherapy"])
q(514, S12, "Visor approach is used for:", "Resection of mandible and floor of mouth", ["Maxillectomy", "Parotidectomy", "Tonsillectomy"])
q(514, S12, "Advantage of the visor approach:", "Lifting up the area increases the area of access", ["Avoids all incisions", "Reduces operating time only", "Preserves all nerves"])
q(514, S12, "Indication for the Weber-Ferguson approach:", "Maxillectomy", ["Mandibulectomy", "Neck dissection", "Glossectomy"])
q(514, S12, "M/c surgical approach for oral cancer resection:", "Lip split approach", ["Visor approach", "Weber-Ferguson approach", "Transoral approach"])
q(514, S12, "Lip split approach is used for:", "Resection of mandible and buccal mucosa", ["Maxillectomy", "Thyroidectomy", "Parotidectomy"])

# ------------------------------------------------------------------ p515
S13 = "Lymph Nodes of the Neck"
q(515, S13, "Level IA nodes:", "Submental", ["Submandibular", "Upper deep cervical", "Posterior triangle"])
q(515, S13, "Level IB nodes:", "Submandibular", ["Submental", "Middle deep cervical", "Mediastinal"])
q(515, S13, "Level II nodes:", "Upper deep cervical", ["Middle deep cervical", "Lower deep cervical", "Submental"])
q(515, S13, "Level IIa and IIb refer to:", "Anterior and posterior subdivisions of the upper deep cervical nodes", ["Superior and inferior posterior triangle", "Submental and submandibular", "Pre and paratracheal"])
q(515, S13, "Level III nodes:", "Middle deep cervical", ["Upper deep cervical", "Lower deep cervical", "Posterior triangle"])
q(515, S13, "Level IV nodes:", "Lower deep cervical", ["Middle deep cervical", "Upper deep cervical", "Central compartment"])
q(515, S13, "Boundaries of the anterior triangle of the neck:", "Midline, sternocleidomastoid and angle of mandible", ["Sternocleidomastoid, angle of mandible and trapezius", "Clavicle, trapezius and midline", "Hyoid, thyroid and clavicle"])
q(515, S13, "Level V refers to:", "Posterior triangle nodes (Va superior, Vb inferior)", ["Central compartment nodes", "Mediastinal nodes", "Submental nodes"])
q(515, S13, "Largest group of neck nodes:", "Level V (posterior triangle)", ["Level I", "Level II", "Level VI"])
q(515, S13, "Boundaries of the posterior triangle:", "Sternocleidomastoid, angle of mandible and trapezius", ["Midline, SCM and angle of mandible", "Clavicle, hyoid and midline", "Trapezius, clavicle and mandible"])
q(515, S13, "Level VI nodes are also called:", "Central compartment nodes / Delphian lymph nodes / pre & paratracheal", ["Posterior triangle nodes", "Mediastinal nodes", "Submental nodes"])
q(515, S13, "Level VI nodes are the first draining nodes in:", "Thyroid cancer and laryngeal cancer", ["Tongue cancer", "Lip cancer", "Parotid cancer"])
q(515, S13, "Level VII nodes:", "Mediastinal", ["Posterior triangle", "Central compartment", "Submandibular"])

S14 = "Neck Node Management Principles"
q(515, S14, "Effect of prophylactic lymph node dissection in T1, T2 tumors:", "Increases survival", ["Decreases survival", "No effect", "Only cosmetic benefit"])
q(515, S14, "Sentinel lymph node biopsy can demonstrate:", "Occult metastases and unexpected contralateral drainage", ["Depth of invasion", "Perineural invasion", "Tumour grade"])
q(515, S14, "Prophylactic elective neck dissection means:", "Selective neck dissection — supraomohyoid dissection", ["Radical neck dissection", "Central neck dissection", "Modified radical neck dissection"])
q(515, S14, "Carcinomas with contralateral lymph node drainage include all EXCEPT:", "Carcinoma of the lateral buccal mucosa", ["Angle of mouth", "Lip cancer crossing midline", "Carcinoma tip of tongue"])
q(515, S14, "Palatal carcinoma with contralateral drainage:", "Soft palate carcinoma", ["Hard palate carcinoma", "Retromolar trigone", "Alveolus"])

# ------------------------------------------------------------------ p516
S15 = "Neck Dissection: Incisions and Types"
q(516, S15, "M/c incision used for neck dissection:", "Modified Schobinger's incision", ["Crile's incision", "Martin's incision", "MacFee incision"])
q(516, S15, "Radical neck dissection was described by:", "Crile", ["Schobinger", "Martin", "MacFee"])
q(516, S15, "Lymph node levels removed in radical neck dissection:", "Levels I-V", ["Levels I-III", "Level VI only", "Levels II-IV"])
q(516, S15, "Three extra lymphatic structures removed in radical neck dissection:", "Spinal accessory nerve, internal jugular vein and sternocleidomastoid", ["Vagus, carotid artery and SCM", "Phrenic nerve, IJV and trapezius", "Hypoglossal nerve, IJV and omohyoid"])
q(516, S15, "Glandular structures removed in radical neck dissection:", "Tail of parotid and submandibular gland", ["Thyroid and parathyroid", "Sublingual gland only", "Thymus"])
q(516, S15, "Structures removed in modified radical neck dissection:", "Levels I-V, tail of parotid and submandibular gland", ["Levels I-III only", "Level VI only", "Levels II-IV"])
q(516, S15, "Defining feature of modified radical neck dissection:", "At least 1 extra lymphatic structure is preserved", ["All extra lymphatic structures removed", "No lymph nodes removed", "Only level VI removed"])
q(516, S15, "Functional neck dissection means:", "All 3 extra lymphatic structures are preserved", ["One structure preserved", "Two structures preserved", "None preserved"])
q(516, S15, "MRND type I:", "1 extra lymphatic structure preserved", ["2 structures preserved", "3 structures preserved", "None preserved"])
q(516, S15, "MRND type II:", "2 extra lymphatic structures preserved", ["1 structure preserved", "3 structures preserved", "None preserved"])
q(516, S15, "MRND type III:", "3 extra lymphatic structures preserved", ["1 structure preserved", "2 structures preserved", "None preserved"])
q(516, S15, "Selective neck dissection is also called:", "Supraomohyoid neck dissection (SOHND)", ["Radical neck dissection", "Central neck dissection", "Functional neck dissection"])
q(516, S15, "Levels removed in supraomohyoid neck dissection:", "Levels I-III (above the omohyoid)", ["Levels I-V", "Level VI", "Levels IV-VI"])

# ------------------------------------------------------------------ p517
S16 = "Central Neck Dissection, Complications and Flaps"
q(517, S16, "Level removed in central neck dissection:", "Level VI", ["Level V", "Levels I-III", "Level VII"])
q(517, S16, "Complications of neck dissection include all EXCEPT:", "Hypothyroidism from thyroid removal", ["Bleeding", "Infection", "Injury to nerves"])
q(517, S16, "Marginal mandibular nerve (ramus mandibularis) supplies the:", "Angle of mouth", ["Tongue", "Shoulder", "Diaphragm"])
q(517, S16, "How is marginal mandibular nerve injury prevented:", "Incision at 2 finger breadths from the angle of mandible", ["Incision directly over the angle", "Incision above the mandible", "No prevention possible"])
q(517, S16, "Spinal accessory nerve injury causes:", "Shoulder dysfunction with drooping of shoulder and pain", ["Tongue deviation", "Diaphragmatic palsy", "Loss of taste"])
q(517, S16, "Nerves at risk in neck dissection besides spinal accessory and marginal mandibular:", "Hypoglossal and phrenic nerves", ["Optic and oculomotor", "Sciatic and femoral", "Radial and ulnar"])
q(517, S16, "Carotid artery blowout is:", "Opening in the carotid artery post dissection due to infection, leading to bleeding and death", ["Aneurysm formation without bleeding", "Thrombosis of the carotid", "Carotid body tumour"])
q(517, S16, "M/c used flap in head and neck reconstruction surgery:", "Pectoralis major myocutaneous (PMMC) flap", ["Deltopectoral flap", "Abbe-Estlander flap", "Free fibular flap"])
q(517, S16, "Abbe-Estlander flap is used for:", "Lip and angle of mouth reconstruction", ["Mandibular reconstruction", "Tongue reconstruction", "Scalp reconstruction"])
q(517, S16, "Abbe-Estlander flap is based on:", "Labial vessels", ["Peroneal vessels", "Radial artery", "Thoracoacromial artery"])

# ------------------------------------------------------------------ p518
S17 = "Free Flaps"
q(518, S17, "Definition of a free flap:", "Flap taken from one site and placed in another", ["Flap rotated about its pedicle", "Skin graft without vessels", "Flap left attached at both ends"])
q(518, S17, "Test done prior to creation of a forearm flap:", "Allen's test", ["Adson's test", "Perthes test", "Trendelenburg test"])
q(518, S17, "Most versatile flap for head and neck reconstruction:", "Radial artery forearm flap", ["PMMC flap", "Free fibular flap", "Deltopectoral flap"])
q(518, S17, "Main use of the free fibular flap:", "Mandibular reconstruction", ["Lip reconstruction", "Tongue reconstruction", "Scalp reconstruction"])
q(518, S17, "Free fibular flap is especially used in patients who are:", "Edentulous (absence of teeth)", ["Fully dentate", "Children only", "Diabetic"])
q(518, S17, "Free fibular flap is based on:", "Peroneal vessels", ["Radial artery", "Labial vessels", "Thoracodorsal vessels"])

S18 = "Adjuvant Therapy and Prognosis"
q(518, S18, "High risk features indicating adjuvant chemotherapy/radiotherapy include all EXCEPT:", "Well differentiated histology", ["Extra nodal extension", "Lymphovascular invasion", "Involved margins"])
q(518, S18, "Neural high risk feature for adjuvant therapy:", "Perineural invasion", ["Perivascular oedema", "Muscle atrophy", "Bone sclerosis"])
q(518, S18, "ONE MAJOR indication for radiotherapy:", "Extranodal extension ± involved margins", ["Close margins alone", "Single involved node", "Small T1 tumour"])
q(518, S18, "TWO MINOR indications for radiotherapy include:", "Close margins, multiple involved nodes, lymph node invasion, perineural invasion", ["Extranodal extension only", "Distant metastasis", "Negative margins"])
q(518, S18, "Advantage of concurrent chemo-radiation:", "Better response — the chemoagent acts as a radiosensitizer increasing radiotherapy efficacy", ["Shorter treatment duration only", "No side effects", "Avoids surgery entirely"])
q(518, S18, "Neoadjuvant chemo-radiation means:", "Chemotherapy/radiotherapy prior to surgery", ["Therapy after surgery", "Therapy during surgery", "Therapy instead of surgery"])
q(518, S18, "Indication for neoadjuvant chemo-radiation:", "Advanced tumors — to shrink the tumor", ["Early T1 tumours", "Benign lesions", "Premalignant lesions"])
q(518, S18, "Immunotherapy agents used in oral cancer:", "PDL-1 inhibitors", ["EGFR agonists", "Anti-VEGF only", "Tyrosine kinase activators"])
q(518, S18, "Indication for immunotherapy in oral cancer:", "Recurrent or metastatic SCC", ["Early stage SCC", "Premalignant lesions", "Verrucous carcinoma"])
q(518, S18, "Most important prognostic factor in oral cancer:", "Lymph node status", ["Tumour size", "Patient age", "Tumour site"])

# ------------------------------------------------------------------ p519
S19 = "Metastasis from Unknown Primary"
q(519, S19, "First step in a patient with an enlarged cervical lymph node:", "FNAC", ["Excision biopsy", "PET-CT", "Radiotherapy"])
q(519, S19, "If FNAC shows cancer but the primary source is not located, next step:", "Look for hidden sources", ["Start palliative care", "Perform radical neck dissection immediately", "Repeat FNAC only"])
q(519, S19, "Retromolar trigone is the space:", "Behind the 3rd molar", ["Behind the 1st molar", "Below the tongue", "Behind the tonsil"])
q(519, S19, "Hidden sources of a primary head and neck cancer include all EXCEPT:", "Hard palate", ["Retromolar trigone", "Base of tongue", "Tonsillar fossa"])
q(519, S19, "Fossa of Rosenmuller is located in the:", "Nasopharynx", ["Oropharynx", "Hypopharynx", "Larynx"])
q(519, S19, "Hypopharyngeal hidden site for an occult primary:", "Pyriform sinus", ["Fossa of Rosenmuller", "Retromolar trigone", "Base of tongue"])
q(519, S19, "PET-CT stands for:", "Positron emission tomography - computed tomography", ["Photon emission tissue CT", "Peripheral emission tomography", "Positive emission thermography"])
q(519, S19, "Role of PET-CT in an unknown primary:", "Whole body scan to locate the primary tumour", ["To grade the tumour", "To measure depth of invasion", "To assess nodal size only"])
q(519, S19, "Isotope used in PET-CT:", "18-Fluorodeoxy glucose (18-FDG)", ["Technetium-99m", "Iodine-131", "Gallium-67"])
q(519, S19, "Half life of 18-FDG:", "110 mins", ["10 mins", "6 hours", "8 days"])

S20 = "Dentigerous Cyst, Dental Cyst and Ameloblastoma"
q(519, S20, "Dentigerous cyst is associated with:", "An unerupted tooth", ["A caried tooth", "An extracted tooth", "A healthy erupted tooth"])
q(519, S20, "M/c tooth associated with a dentigerous cyst:", "3rd molar", ["1st molar", "Canine", "Incisor"])
q(519, S20, "Management of a dentigerous cyst:", "Enucleation", ["Removal of the caried tooth", "Wide local excision", "Radiotherapy"])
q(519, S20, "Dental cyst is associated with:", "A caried tooth", ["An unerupted tooth", "A missing tooth", "A supernumerary tooth"])
q(519, S20, "Management of a dental cyst:", "Removal of the caried tooth", ["Enucleation of the cyst alone", "Wide local excision", "Observation"])
q(519, S20, "Ameloblastoma is a tumor of the:", "Mandible", ["Maxilla", "Tongue", "Parotid"])
q(519, S20, "Clinical feature of ameloblastoma:", "Bony hard swelling", ["Soft fluctuant swelling", "Pulsatile swelling", "Transilluminant swelling"])
q(519, S20, "Investigation of choice for ameloblastoma:", "Orthopantomogram (OPG)", ["FNAC", "PET-CT", "USG"])
q(519, S20, "Management of ameloblastoma:", "Wide local excision (WLE)", ["Enucleation", "Radiotherapy", "Observation"])

UNIT_DEFS = [
    (S1, "Squamous cell carcinoma is the m/c oral and oropharyngeal cancer, recognised by eosinophilic keratin pearls — abundant when well differentiated, scarce when poorly differentiated. p53 is the m/c mutation. Site differs by geography: buccal mucosa/gingivo buccal sulcus in India, lateral border of tongue worldwide."),
    (S2, "Smoking, alcohol, betel quid, immunosuppression and sharp ill-fitting dentures head the risk list, joined by chronic infection: hyperplastic candidiasis, EBV (nasopharyngeal carcinoma) and HPV — 5% of oral SCC but 50-70% of oropharyngeal SCC, which carries a better prognosis."),
    (S3, "Rank the premalignant lesions: HIGH risk — erythroplakia, proliferative verrucous leukoplakia, chronic hyperplastic candidiasis; MEDIUM — oral submucous fibrosis, syphilitic glossitis; LOW — oral lichen planus, DLE. Verrucous carcinoma (Ackerman tumor) is an HPV-positive, slow, outward-growing SCC variant."),
    (S4, "Verrucous carcinoma has a good prognosis, and its penile counterpart is the Buschke-Lowenstein tumor. Leukoplakia is a white patch that CANNOT be rubbed off, raising cancer risk 3-5 times — treat by eliminating risk factors, antioxidants and CO2 laser or cautery excision. Proliferative verrucous leukoplakia is multifocal, arises without typical risk factors, converts often and must be excised early; speckled leukoplakia has a reddish border and is excised."),
    (S5, "Hyperplastic candidiasis CAN be rubbed off, has a reddish border and still raises malignancy risk. Erythroplakia is a red patch that cannot be rubbed off, carrying a 6-9 fold cancer risk, worst in its speckled form — eliminate risk factors and excise."),
    (S6, "A dysplastic lesion is more dangerous in a female, non-smoker, with a lesion >200 mm sq, non-homogeneous, multiple, and on the lateral border of the tongue. Oral submucous fibrosis is a betel nut hypersensitivity: fibrosis limits mouth opening, hygiene fails, cancer risk rises, and white bands appear. Stop betel quid and smoking, give antioxidants and intralesional triamcinolone — never excise, because healing brings more fibrosis."),
    (S7, "Plummer-Vinson (Patterson-Kelly-Brown, sideropenic dysphagia) strikes perimenopausal women with iron deficiency anemia, koilonychia, angular cheilitis and intermittent dysphagia from post-cricoid webs, raising the risk of hypopharyngeal and oesophageal SCC. Correct the iron and excise webs with CO2."),
    (S8, "Field cancerisation — oral cavity, bladder and colorectal region (4% synchronous) — means risk factors bathe the entire mucosa so multiple cancers arise: synchronous within 6 months of the primary, metachronous after. Hence close follow up and screening for other cancers."),
    (S9, "Confirm with an incisional edge or wedge biopsy — the centre is necrotic; if inflammation dominates, give antibiotics and repeat. Stage with CECT of PNS, neck and thorax, and distinguish tumour thickness (includes the exophytic part) from depth of invasion measured below the mucosal surface."),
    (S10, "AJCC 8th: T1 ≤2 cm with DOI ≤5 mm; T2 either ≤2 cm with DOI 5-10 mm or 2-4 cm with DOI <10 mm; T3 >4 cm or DOI >10 mm; T4 adjacent structures (a resectable, b not). Nodes: N1 single ipsilateral ≤3 cm; N2a single ipsilateral >3-6 cm; N2b multiple ipsilateral ≤6 cm; N2c bilateral/contralateral ≤6 cm; N3a >6 cm or extranodal extension; N3b clinical/radiographic extranodal extension with matted nodes or skin attachment. Lung is the m/c metastatic site."),
    (S11, "Surgery aims at R0 — microscopic freedom with a 0.5 cm margin. Add mandibular resection when the mandible is involved and neck dissection when nodes are involved; all three together make the Commando operation, followed by flap reconstruction."),
    (S12, "Lip cancer by extent: <1/3rd WLE with primary closure, >1/3rd-2/3rd Johanson's step ladder resection, >2/3rd flap reconstruction. Approaches: visor for mandible and floor of mouth, Weber-Ferguson for maxillectomy, and the lip split — the m/c — for mandible and buccal mucosa."),
    (S13, "Neck levels: IA submental, IB submandibular, II upper deep cervical (IIa anterior, IIb posterior), III middle deep cervical, IV lower deep cervical — all in the anterior triangle bounded by midline, SCM and angle of mandible. Level V is the posterior triangle (Va superior, Vb inferior), the largest group, bounded by SCM, angle of mandible and trapezius. Level VI is the central compartment / Delphian / pre and paratracheal nodes, first to drain thyroid and laryngeal cancer; level VII is mediastinal."),
    (S14, "Prophylactic lymph node dissection improves survival even in T1 and T2 tumours. Sentinel lymph node biopsy reveals occult metastases and unexpected contralateral drainage, and prophylactic elective neck dissection means a selective supraomohyoid dissection. Expect contralateral drainage from the angle of mouth, lip cancer crossing the midline, carcinoma of the tip of tongue and soft palate carcinoma."),
    (S15, "Modified Schobinger's is the m/c incision, alongside Crile's, Martin's, hockey stick and MacFee. Crile's radical neck dissection removes levels I-V plus three extra lymphatic structures — spinal accessory nerve, internal jugular vein, sternocleidomastoid — with the tail of parotid and submandibular gland. MRND preserves at least one of those three (type I one, II two, III three, the last also called functional). Selective supraomohyoid dissection takes levels I-III above the omohyoid."),
    (S16, "Central neck dissection removes level VI. Complications: bleeding, infection and nerve injury — marginal mandibular nerve supplying the angle of mouth (avoided by incising 2 finger breadths from the mandible), spinal accessory (drooping painful shoulder), hypoglossal and phrenic — plus carotid blowout, where infection opens the artery and the patient bleeds to death. The PMMC flap is the m/c head and neck flap; the Abbe-Estlander flap, based on labial vessels, rebuilds lip and angle of mouth."),
    (S17, "Free flaps move tissue from one site to another. The radial artery forearm flap — preceded by Allen's test — is the most versatile for head and neck. The free fibular flap, on peroneal vessels, rebuilds the mandible, especially in edentulous patients."),
    (S18, "Adjuvant chemo/radiotherapy follows high risk features: extranodal extension, lymphovascular invasion, perineural invasion and involved margins. Radiotherapy needs one major (extranodal extension ± involved margins) or two minor indications (close margins, multiple involved nodes, lymph node invasion, perineural invasion). Concurrent chemo-radiation works better because the chemoagent radiosensitizes; neoadjuvant therapy shrinks advanced tumours before surgery; PDL-1 inhibitors serve recurrent or metastatic SCC. Lymph node status is the most important prognostic factor."),
    (S19, "An enlarged cervical node goes to FNAC; if cancer is found but no primary, hunt the hidden sites — retromolar trigone (behind the 3rd molar), base of tongue, tonsillar fossa, fossa of Rosenmuller in the nasopharynx and pyriform sinus. PET-CT whole body scanning with 18-FDG (half life 110 minutes) locates the primary."),
    (S20, "Dentigerous cyst hangs on an UNERUPTED tooth, usually the 3rd molar, and is enucleated; a dental cyst sits on a CARIED tooth and is cured by removing that tooth. Ameloblastoma is a bony hard mandibular tumour diagnosed on orthopantomogram and treated by wide local excision."),
]

first_page = {}
for x in Q:
    first_page.setdefault(x["sec"], x["page"])

UNITS = []
for i, (title, guide) in enumerate(UNIT_DEFS, 1):
    UNITS.append({
        "id": f"SURG-U66-{i}",
        "ch": 66,
        "n": i,
        "title": title,
        "sec": f"{title} · p{first_page[title]}",
        "qs": [x["id"] for x in Q if x["sec"] == title],
        "guide": guide,
    })

covered = [x for u in UNITS for x in u["qs"]]
assert covered == [x["id"] for x in Q]
assert len(set(covered)) == len(covered)
with open("data/ch66.json", "w", encoding="utf-8") as f:
    json.dump({"questions": Q, "units": UNITS}, f, ensure_ascii=False, indent=1)
print(f"ch66: {len(Q)} questions, {len(UNITS)} units")
