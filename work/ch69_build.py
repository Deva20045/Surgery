#!/usr/bin/env python3
"""Build data/ch69.json — Thorax and Mediastinum (pp535-543)."""
import json

Q = []


def q(page, sec, text, correct, wrongs, note=None):
    opts = [correct] + list(wrongs)
    assert len(opts) == 4
    Q.append({
        "id": f"SURG-C69-{len(Q)+1:03d}",
        "sec": sec,
        "page": page,
        "q": text,
        "opts": opts,
        "ans": 0,
        "exp": (note or correct) + f" (Book p{page})",
    })


# ------------------------------------------------------------ p535
S1 = "Surgical Anatomy of the Lungs and Thoracoscore"
q(535, S1, "Lobes of the RIGHT lung:", "Upper, middle and lower lobe", ["Upper and lower lobe only", "Upper and middle lobe only", "Four lobes"])
q(535, S1, "Lobes of the LEFT lung:", "Upper and lower lobe", ["Upper, middle and lower lobe", "Lower lobe only", "Four lobes"])
q(535, S1, "Why is aspiration and foreign body lodgement commoner on the right:", "The right mainstem bronchus is shorter and straighter", ["The right bronchus is longer and curved", "The left bronchus is wider", "The carina deviates left"])
q(535, S1, "M/c sites of aspiration abscess formation:", "Posterior upper lobe and superior lower lobe", ["Anterior upper lobe and lingula", "Middle lobe only", "Left lower lobe only"])
q(535, S1, "Clinical features of bronchial foreign body:", "Wheezing, stridor and collapse with complete block", ["Haemoptysis and clubbing", "Pleuritic pain with hyper-resonance", "Fever with pus"])
q(535, S1, "Diagnosis and management of a bronchial foreign body:", "X-ray for diagnosis and bronchoscopic removal", ["CT and thoracotomy", "MRI and observation", "USG and antibiotics"])
q(535, S1, "Thoracoscore is:", "A prognostic score of mortality post lung resection using 9 criteria", ["A staging system for lung cancer", "A score for pneumothorax size", "A pain score"])
q(535, S1, "Number of criteria in the Thoracoscore:", "9", ["5", "7", "12"])
q(535, S1, "FEV1 and DLCO (diffusion capacity) are used for:", "Prediction of dyspnoea post lung surgery", ["Predicting mortality only", "Staging lung cancer", "Diagnosing empyema"])

S2 = "Spontaneous Pneumothorax: Types"
q(535, S2, "Pneumothorax means:", "Air in the pleural space", ["Pus in the pleural space", "Blood in the pleural space", "Fluid in the pericardium"])
q(535, S2, "Demographics of primary spontaneous pneumothorax:", "Young, tall people, males > females, usually with a family history", ["Elderly females with lung disease", "Children under 5", "Obese middle aged women"])
q(535, S2, "Source of air leak in primary spontaneous pneumothorax:", "Leak from blebs, usually in the upper lobe", ["Leak from a lower lobe cavity", "Oesophageal perforation", "Tracheal tear"])
q(535, S2, "Lung function and tolerance in primary spontaneous pneumothorax:", "Normal lung function with better pneumothorax tolerance", ["Poor lung function with poor tolerance", "Normal function but poor tolerance", "Always requires ventilation"])
q(535, S2, "Secondary spontaneous pneumothorax occurs due to:", "Underlying lung disease such as TB, tumors and emphysema", ["Blebs in healthy lung", "Tall stature", "Family history alone"])
q(535, S2, "Patients affected by secondary spontaneous pneumothorax:", "Older patients with less pneumothorax tolerance than primary", ["Young tall males with good tolerance", "Children", "Pregnant women only"])

# ------------------------------------------------------------ p536
S3 = "Pneumothorax: Clinical Features and Management Algorithm"
q(536, S3, "Pain of spontaneous pneumothorax:", "Sharp pleuritic pain", ["Dull aching central chest pain", "Burning epigastric pain", "Radiating back pain"])
q(536, S3, "Percussion note in pneumothorax:", "Hyper-resonant", ["Dull", "Stony dull", "Normal"])
q(536, S3, "Auscultation finding in pneumothorax:", "Absent breath sounds", ["Bronchial breathing", "Crepitations", "Pleural rub only"])
q(536, S3, "Diagnostic investigation for pneumothorax:", "Chest X-ray", ["MRI", "PET-CT", "Bronchoscopy"])
q(536, S3, "Immediate step if pneumothorax is bilateral or the patient is haemodynamically unstable:", "Proceed to chest drain", ["Observe for 24 hours", "Aspirate only", "Discharge with review"])
q(536, S3, "Features favouring a SECONDARY pneumothorax in the algorithm:", "Age >50 with significant smoking history, or evidence of underlying lung disease", ["Young tall male with normal X-ray", "Family history alone", "Female sex"])
q(536, S3, "Management of a PRIMARY pneumothorax that is <2 cm and not breathless:", "Consider discharge with OPD review in 2-4 weeks", ["Aspirate", "Chest drain", "Admit for 24 hours oxygen"])
q(536, S3, "Management of a PRIMARY pneumothorax >2 cm and/or breathless:", "Aspirate, and if that fails place a chest drain 8-14 Fr", ["Discharge with review", "Immediate thoracotomy", "Observation alone"])
q(536, S3, "Management of a SECONDARY pneumothorax >2 cm and/or breathless:", "Chest drain 8-14 Fr", ["Discharge review", "Aspirate only", "Observe 24 hours"])
q(536, S3, "Management of a SECONDARY pneumothorax measuring 1-2 cm:", "Aspirate", ["Discharge", "Chest drain always", "Thoracotomy"])
q(536, S3, "Management of a SECONDARY pneumothorax <1 cm:", "Admit, high flow oxygen and observe for 24 hours", ["Discharge with review", "Aspirate", "Chest drain"])
q(536, S3, "Size of chest drain used in pneumothorax:", "8-14 Fr", ["20-24 Fr", "28-32 Fr", "36 Fr"])

S4 = "Indications for Surgery in Pneumothorax"
q(536, S4, "Indications for surgical intervention in pneumothorax include all EXCEPT:", "A first primary ipsilateral pneumothorax that resolves with aspiration", ["Secondary ipsilateral pneumothorax", "First contralateral pneumothorax", "Bilateral spontaneous pneumothorax"])
q(536, S4, "Failure of which treatment mandates surgery in pneumothorax:", "Pneumothorax failing to settle despite chest drainage", ["Failure of oxygen therapy alone", "Failure of antibiotics", "Failure of analgesia"])
q(536, S4, "Professions in which spontaneous pneumothorax warrants surgery:", "Pilots and divers", ["Teachers and clerks", "Drivers", "Farmers"])
q(536, S4, "Pregnancy in a patient with spontaneous pneumothorax is:", "An indication for surgical intervention", ["A contraindication to any treatment", "Irrelevant", "An indication for observation only"])

# ------------------------------------------------------------ p537
S5 = "Interventions for Pneumothorax"
q(537, S5, "Agents used for pleurodesis:", "TALC / tetracycline", ["Bleomycin and cisplatin", "Adrenaline", "Heparin"])
q(537, S5, "VATS stands for:", "Video assisted thoracoscopic surgery", ["Ventilated assisted thoracic support", "Vascular assisted thoracic surgery", "Venous access thoracic system"])
q(537, S5, "How is working space created in VATS:", "By collapsing one lung via a double lumen endotracheal tube", ["By CO2 insufflation only", "By rib resection", "By diaphragm paralysis"])

S6 = "Empyema: Definition and Causes"
q(537, S6, "Empyema is:", "Accumulation of pus in the pleural space", ["Air in the pleural space", "Blood in the pleural space", "Pus in the pericardium"])
q(537, S6, "Pulmonary infective causes of empyema include all EXCEPT:", "Pulmonary embolism", ["Unresolved pneumonia and bronchiectasis", "Tuberculosis and fungal infections", "Lung abscess"])
q(537, S6, "Iatrogenic cause of empyema:", "Aspiration of a pleural effusion of any etiology", ["Bronchoscopy", "Spirometry", "Oxygen therapy"])
q(537, S6, "Traumatic causes of empyema:", "Penetrating injury, surgery and esophageal perforation", ["Blunt abdominal injury", "Rib fracture alone", "Head injury"])
q(537, S6, "Extrapulmonary source of empyema:", "Subphrenic abscess", ["Brain abscess", "Perianal abscess", "Renal abscess"])
q(537, S6, "Bone infection causing empyema:", "Osteomyelitis of ribs or vertebrae", ["Osteomyelitis of the femur", "Skull osteomyelitis", "Mandibular osteomyelitis"])

S7 = "Phases of Empyema"
q(537, S7, "Findings in the EXUDATIVE phase of empyema:", "Fever and pus with a collection on one side on CXR/CT", ["Thickened pus and pleura", "Thickened pleural entrapment of lung", "No collection"])
q(537, S7, "M/c organism causing empyema:", "Staphylococcus aureus", ["Gram negative bacteria", "Mycobacterium tuberculosis", "Candida"])
q(537, S7, "Management of the exudative phase of empyema:", "Aspiration plus antibiotics", ["Chest tube insertion", "Decortication", "Pneumonectomy"])
q(537, S7, "Findings in the FIBRINOPURULENT phase of empyema:", "Thickening of pus and pleura", ["Fever with thin pus", "Thickened pleural entrapment of lung", "Normal pleura"])
q(537, S7, "Management of the fibrinopurulent phase of empyema:", "Chest tube insertion, since aspiration is difficult", ["Aspiration alone", "Decortication", "Antibiotics alone"])
q(537, S7, "Findings in the ORGANIZED phase of empyema:", "Thickened pleural entrapment of the lung", ["Thin free-flowing pus", "Fever with clear fluid", "Air in the pleural space"])
q(537, S7, "Management of the organized phase of empyema:", "Stripping of the pleura / VATS plus decortication", ["Aspiration", "Chest tube alone", "Antibiotics alone"])

# ------------------------------------------------------------ p538
S8 = "Lung Cancer: Risk Factors and Small Cell Lung Cancer"
q(538, S8, "Risk factors for lung cancer:", "Smoking, pollution and asbestos exposure", ["Betel quid and alcohol", "HPV infection", "Chronic lymphedema"])
q(538, S8, "Percentage of lung cancer patients amenable to surgical resection:", "15-20%", ["50%", "70%", "90%"])
q(538, S8, "Modality that has revolutionised treatment of lung cancer:", "Immunotherapy", ["Radiotherapy", "Surgery", "Steroids"])
q(538, S8, "Small cell (oat cell) lung cancer has:", "The strongest association with smoking", ["No association with smoking", "An association with non-smokers", "An association with asbestos only"])
q(538, S8, "Prognosis and chemosensitivity of small cell lung cancer:", "Poor prognosis but highly sensitive to chemotherapy", ["Good prognosis, chemoresistant", "Good prognosis, chemosensitive", "Poor prognosis, chemoresistant"])
q(538, S8, "Which lung cancer has the maximum number of paraneoplastic syndromes:", "Small cell lung cancer", ["Squamous cell carcinoma", "Adenocarcinoma", "Large cell carcinoma"])
q(538, S8, "Hormone causing Cushing's disease in small cell lung cancer:", "Adrenocorticotropic hormone", ["Antidiuretic hormone", "Growth hormone-related peptide", "Anti-VGCC antibody"])
q(538, S8, "Hormone responsible for SIADH in lung cancer:", "Antidiuretic hormone", ["ACTH", "Growth hormone-related peptide", "PTHrP"])
q(538, S8, "Mediator of acromegaly as a paraneoplastic syndrome:", "Growth hormone-related peptide", ["ACTH", "ADH", "Anti-VGCC"])
q(538, S8, "Antibody responsible for Lambert-Eaton syndrome:", "Anti-VGCC (voltage gated calcium channel)", ["Anti-AChR", "Anti-ADH", "Anti-Hu only"])
q(538, S8, "Azzopardi effect refers to:", "Deposition of DNA around blood vessels producing blue/purple staining", ["Keratin pearls around vessels", "Lepidic spread", "Nuclear moulding alone"])
q(538, S8, "IHC markers of small cell lung cancer:", "Chromogranin and NCAM", ["CK7 and p63", "TTF-1 and napsin A only", "S-100 and HMB 45"])

# ------------------------------------------------------------ p539
S9 = "SVC Syndrome and Squamous Cell Carcinoma of the Lung"
q(539, S9, "SVC syndrome is:", "An oncological emergency", ["A chronic benign condition", "A paraneoplastic syndrome", "A post-operative complication only"])
q(539, S9, "Clinical features of SVC syndrome:", "Facial and cerebral edema ± seizures", ["Ptosis and miosis", "Hypotension and bradycardia", "Haemoptysis alone"])
q(539, S9, "Diagnostic investigation for SVC syndrome:", "CECT", ["Chest X-ray", "MRI brain", "Echocardiography"])
q(539, S9, "Management of SVC syndrome:", "Radiotherapy to shrink the tumour plus steroids to lower intracranial pressure", ["Surgery alone", "Chemotherapy alone", "Observation"])
q(539, S9, "Location of squamous cell carcinoma of the lung:", "Centrally placed", ["Peripherally placed", "Apex only", "Diffuse"])
q(539, S9, "M/c lung cancer in SMOKERS:", "Squamous cell carcinoma", ["Adenocarcinoma", "Small cell carcinoma", "Large cell carcinoma"])
q(539, S9, "Pancoast tumor pressing the thoracic inlet presents with:", "Dyspnoea / stridor", ["Ptosis and miosis", "Cushing's syndrome", "SIADH"])
q(539, S9, "Pancoast tumor pressing the sympathetic chain causes:", "Horner's syndrome", ["Lambert-Eaton syndrome", "SVC syndrome", "Acromegaly"])
q(539, S9, "Components of Horner's syndrome:", "Ptosis, miosis, enophthalmos and anhydrosis", ["Ptosis, mydriasis, exophthalmos, hyperhidrosis", "Facial edema and seizures", "Wheeze and stridor"])
q(539, S9, "Management of Pancoast tumor:", "Radiotherapy plus immunotherapy", ["Pneumonectomy alone", "Observation", "Steroids alone"])

S10 = "Adenocarcinoma of the Lung"
q(539, S10, "M/c lung cancer OVERALL:", "Adenocarcinoma", ["Squamous cell carcinoma", "Small cell carcinoma", "Large cell carcinoma"])
q(539, S10, "Sex predilection of lung adenocarcinoma:", "Females > males", ["Males > females", "Equal", "Only males"])
q(539, S10, "Location and growth of lung adenocarcinoma:", "Peripherally placed and slow growing", ["Centrally placed and fast growing", "Peripheral and fast growing", "Central and slow growing"])
q(539, S10, "Adenocarcinoma of lung typically develops in:", "Pre-existing lung cavities due to TB/bronchiectasis", ["Normal upper lobe blebs", "Pleural space", "Mediastinum"])
q(539, S10, "Metastatic behaviour of lung adenocarcinoma:", "Early metastasis", ["Late metastasis", "Never metastasises", "Only local spread"])
q(539, S10, "IHC marker of lung adenocarcinoma:", "NAPSIN A", ["Chromogranin", "p63", "HMB 45"])
q(539, S10, "Mutations associated with lung adenocarcinoma:", "ALK and RAS", ["L-myc", "p53 only", "BRAF only"])

# ------------------------------------------------------------ p540
S11 = "Bronchoalveolar Carcinoma and Clinical Features of Lung Cancer"
q(540, S11, "Bronchoalveolar carcinoma is also called:", "Adenocarcinoma in-situ", ["Large cell carcinoma", "Oat cell carcinoma", "Pancoast tumor"])
q(540, S11, "Features of bronchoalveolar carcinoma:", "In-situ cancer, multifocal, usually resectable with good prognosis", ["Invasive with poor prognosis", "Unifocal and unresectable", "Metastatic at presentation"])
q(540, S11, "Pattern of spread of bronchoalveolar carcinoma:", "Along the broncho-alveolar lining — lepidic pattern", ["Haematogenous only", "Lymphatic only", "Transpleural"])
q(540, S11, "M/c symptom of lung cancer:", "Cough", ["Hemoptysis", "Pain", "Weight loss"])
q(540, S11, "Symptoms of lung cancer include all EXCEPT:", "Polyuria", ["Cough and hemoptysis", "Pain", "Weight loss"])
q(540, S11, "M/c SYMPTOMATIC site of metastasis in lung cancer:", "Brain", ["Adrenal gland", "Bones", "Liver"])
q(540, S11, "Very common but ASYMPTOMATIC site of metastasis in lung cancer:", "Adrenal gland", ["Brain", "Bones", "Skin"])

S12 = "Work-up of Lung Cancer"
q(540, S12, "Initial investigation in suspected lung cancer:", "Chest X-ray", ["HRCT", "PET-CT", "Bronchoscopy"])
q(540, S12, "IOC to assess the extent of a lung tumor:", "HRCT (high resolution CT)", ["Chest X-ray", "PET-CT", "MRI"])
q(540, S12, "Investigation that determines the TYPE of lung tumor:", "Biopsy", ["HRCT", "Chest X-ray", "PET-CT"])
q(540, S12, "Two purposes of mediastinoscopy:", "To check operability and to take a biopsy", ["To drain effusion and ventilate", "To stage distant metastasis", "To perform pleurodesis"])
q(540, S12, "EBUS FNAC stands for:", "Endobronchial ultrasound guided FNAC", ["Extra bronchial ultrasound FNAC", "Endoscopic barium ultrasound", "Endobronchial biopsy under sedation"])
q(540, S12, "IOC for STAGING lung cancer:", "PET-CT", ["HRCT", "Chest X-ray", "Mediastinoscopy"])

# ------------------------------------------------------------ p541
S13 = "Staging of Lung Cancer"
q(541, S13, "T1 lung cancer:", "≤3 cm surrounded by lung/visceral pleura, not involving the main bronchus", ["3-5 cm tumour", "Involvement of the carina", "Any size with nodal spread"])
q(541, S13, "T1a(mi) denotes:", "Minimally invasive carcinoma", ["Tumour ≤1 cm", "Tumour >1 to ≤2 cm", "Tumour >2 to ≤3 cm"])
q(541, S13, "T1a lung cancer:", "≤1 cm", [">1 to ≤2 cm", ">2 to ≤3 cm", ">3 to ≤4 cm"])
q(541, S13, "T1b lung cancer:", ">1 to ≤2 cm", ["≤1 cm", ">2 to ≤3 cm", ">4 to ≤5 cm"])
q(541, S13, "T1c lung cancer:", ">2 to ≤3 cm", [">1 to ≤2 cm", ">3 to ≤4 cm", "≤1 cm"])
q(541, S13, "T2 lung cancer:", ">3 to ≤5 cm, or main bronchus involvement without carina, or visceral pleural invasion, or atelectasis/post obstructive pneumonitis extending to hilum", ["≤3 cm not involving main bronchus", "Carinal involvement", "Any size with distant metastasis"])
q(541, S13, "T2a lung cancer:", ">3 to ≤4 cm", [">4 to ≤5 cm", ">2 to ≤3 cm", "≤1 cm"])
q(541, S13, "T2b lung cancer:", ">4 to ≤5 cm", [">3 to ≤4 cm", ">2 to ≤3 cm", ">5 cm"])

S14 = "Management of Lung Cancer"
q(541, S14, "Stages of lung cancer suitable for surgery:", "T1-T2 and T3 with N0/N1 disease", ["Any T with N3", "Metastatic disease", "Only T1 N0"])
q(541, S14, "Surgical options in lung cancer:", "Lobectomy, pneumonectomy and sleeve resection", ["Decortication and pleurodesis", "VATS biopsy only", "Mediastinoscopy"])
q(541, S14, "Standard approach for lung resection:", "Posterolateral thoracotomy", ["Median sternotomy", "Anterior mini-thoracotomy", "Subcostal incision"])
q(541, S14, "Complications of lung resection include all EXCEPT:", "Frey's syndrome", ["Bleeding and respiratory infection", "Persistent air leak", "Bronchopleural fistula"])
q(541, S14, "Lung cancer subtype that is highly radiosensitive:", "Squamous cell carcinoma", ["Adenocarcinoma", "Large cell carcinoma", "Bronchoalveolar carcinoma"])
q(541, S14, "Role of chemo/immunotherapy in lung cancer:", "Latest modality for all carcinomas, useful in advanced cancer", ["Only for T1 disease", "Replaces surgery in early disease", "Only palliative in SCC"])

S15 = "Summary Comparison of Lung Cancers"
q(541, S15, "Incidence by sex in lung adenocarcinoma versus the others:", "Adenocarcinoma F > M, while SCC, small cell and large cell are M > F", ["All are F > M", "All are M > F", "Adenocarcinoma M > F"])
q(541, S15, "Location of small cell carcinoma:", "Central", ["Peripheral", "Apical", "Pleural"])
q(541, S15, "Location of large cell carcinoma:", "Peripheral", ["Central", "Apical", "Hilar"])
q(541, S15, "Smoking association of adenocarcinoma:", "Non smokers", ["Strongest association with smoking", "Smoking association", "Both smokers and non smokers equally"])
q(541, S15, "Smoking association of large cell carcinoma:", "Both smokers and non smokers", ["Non smokers only", "Strongest association with smoking", "No association"])
q(541, S15, "Paraneoplastic syndrome of squamous cell carcinoma of lung:", "Hypercalcemia", ["SIADH", "Migratory thrombophlebitis", "Gynecomastia"])
q(541, S15, "Paraneoplastic syndrome of lung adenocarcinoma:", "Migratory thrombophlebitis", ["Hypercalcemia", "Cushing's syndrome", "Gynecomastia"])
q(541, S15, "Paraneoplastic syndromes of small cell carcinoma:", "Cushing's syndrome and SIADH", ["Hypercalcemia", "Migratory thrombophlebitis", "Gynecomastia"])
q(541, S15, "Paraneoplastic syndrome of large cell carcinoma:", "Gynecomastia", ["Hypercalcemia", "SIADH", "Migratory thrombophlebitis"])
q(541, S15, "Pathogenesis (gene) of squamous cell carcinoma of lung:", "P53", ["K ras, EGFR, ALK", "L-myc", "BRAF"])
q(541, S15, "Pathogenesis (genes) of lung adenocarcinoma:", "K ras, EGFR, ALK", ["P53", "L-myc", "RB"])
q(541, S15, "Pathogenesis (gene) of small cell carcinoma:", "L-myc", ["P53", "EGFR", "ALK"])
q(541, S15, "Precursor lesion of squamous cell carcinoma of lung:", "Carcinoma in situ (CIS)", ["Atypical adenomatous hyperplasia", "DIPNEH", "Hamartoma"])
q(541, S15, "Precursor lesions of lung adenocarcinoma:", "Adenocarcinoma in situ and atypical adenomatous hyperplasia (AAH)", ["Carcinoma in situ", "DIPNEH", "Blebs"])
q(541, S15, "Precursor lesion of small cell carcinoma:", "DIPNEH — diffuse idiopathic pulmonary neuroendocrine hyperplasia", ["Carcinoma in situ", "AAH", "Hamartoma"])

# ------------------------------------------------------------ p542
S16 = "Histology, IHC and Benign Lung Tumors"
q(542, S16, "H&E findings in squamous cell carcinoma of the lung:", "Keratin pearls and desmosomes", ["Glands lined by pleomorphic cells", "Salt and pepper chromatin with nuclear moulding", "Large pleomorphic cells"])
q(542, S16, "H&E findings in lung adenocarcinoma:", "Glands lined by pleomorphic cells", ["Keratin pearls and desmosomes", "Nuclear moulding and Azzopardi effect", "Large pleomorphic cells"])
q(542, S16, "H&E findings in small cell carcinoma:", "Small cells with salt & pepper chromatin, nuclear moulding and Azzopardi effect", ["Keratin pearls", "Glandular pattern", "Large pleomorphic cells"])
q(542, S16, "H&E findings in large cell carcinoma:", "Large pleomorphic cells", ["Keratin pearls", "Salt and pepper chromatin", "Glandular structures"])
q(542, S16, "IHC of squamous cell carcinoma of the lung:", "CK, P63, P40", ["TTF-1, NAPSIN A", "NSE, chromogranin, synaptophysin", "S-100, HMB45"])
q(542, S16, "IHC of lung adenocarcinoma:", "TTF-1 and NAPSIN A", ["CK, P63, P40", "NSE, chromogranin, synaptophysin", "cKit"])
q(542, S16, "IHC of small cell carcinoma:", "NSE, chromogranin and synaptophysin", ["CK, P63, P40", "TTF-1 and NAPSIN A", "SMA and p63"])
q(542, S16, "M/c benign lung tumor:", "Hamartoma", ["Chondroma", "Lipoma", "Fibroma"])
q(542, S16, "Clinical features of a hamartoma:", "Usually asymptomatic, may cause cough and hemoptysis", ["Always symptomatic with weight loss", "Presents with SVC syndrome", "Causes Horner's syndrome"])
q(542, S16, "Chest X-ray appearance of a hamartoma:", "Coin shaped lesion", ["Cavitating mass", "Pleural effusion", "Reticular shadowing"])
q(542, S16, "Confirmatory investigation and management of a hamartoma:", "CT is confirmatory; VATS guided excision", ["X-ray alone; radiotherapy", "MRI; chemotherapy", "PET-CT; observation"])

S17 = "Mediastinal Tumors by Compartment"
q(542, S17, "Tumors of the SUPERIOR mediastinum:", "Lymphoma, thyroid and parathyroid", ["Thymoma, teratoma and lymphoma", "Neurogenic tumors", "Pericardial cyst"])
q(542, S17, "The 3 T's of the anterior mediastinum:", "Thymoma, teratoma and terrible lymphoma", ["Thyroid, teratoma, thymoma", "Thymoma, thyroid, tuberculosis", "Teratoma, thymoma, tumour of nerve"])
q(542, S17, "M/c mediastinal tumor:", "Thymoma", ["Teratoma", "Lymphoma", "Neurogenic tumor"])
q(542, S17, "Contents of the MIDDLE mediastinum in terms of tumors:", "Cystic lesions (m/c pericardial cyst), lymphoma and mesenchymal tumors", ["Thymoma and teratoma", "Neurogenic tumors", "Thyroid and parathyroid"])
q(542, S17, "M/c cystic lesion of the middle mediastinum:", "Pericardial cyst", ["Bronchogenic cyst", "Thymic cyst", "Enteric cyst"])
q(542, S17, "M/c tumor of the POSTERIOR mediastinum:", "Neurogenic tumor", ["Thymoma", "Teratoma", "Lymphoma"])
q(542, S17, "M/c mediastinal tumor in CHILDREN:", "Neurogenic tumor", ["Thymoma", "Teratoma", "Lymphoma"])

# ------------------------------------------------------------ p543
S18 = "Thymoma and Masaoka Staging"
q(543, S18, "Site of thymoma:", "Anterior mediastinum", ["Posterior mediastinum", "Middle mediastinum", "Superior mediastinum"])
q(543, S18, "Behaviour of thymoma:", "Usually benign", ["Usually malignant", "Always metastatic", "Always in-situ"])
q(543, S18, "Condition associated with thymoma:", "Myasthenia gravis", ["Lambert-Eaton syndrome", "Cushing's syndrome", "SIADH"])
q(543, S18, "Management of a SMALL thymoma:", "Transcervical excision", ["VATS/thoracotomy", "Radiotherapy", "Observation"])
q(543, S18, "Management of a LARGE thymoma:", "VATS / thoracotomy", ["Transcervical excision", "Chemotherapy alone", "Observation"])
q(543, S18, "Masaoka stage I thymoma:", "Macroscopically completely encapsulated with no microscopic capsular invasion", ["Microscopic invasion into the capsule", "Invasion into neighbouring organs", "Pleural dissemination"])
q(543, S18, "Masaoka stage II thymoma:", "Macroscopic invasion into surrounding fatty tissue or mediastinal pleura with microscopic capsular invasion", ["Completely encapsulated", "Invasion into great vessels", "Haematogenous metastasis"])
q(543, S18, "Masaoka stage III thymoma:", "Macroscopic invasion into neighboring organs — pericardium, great vessels, lungs", ["Invasion into mediastinal fat only", "Pleural dissemination", "Lymphogenous metastasis"])
q(543, S18, "Masaoka stage IVA thymoma:", "Pleural or pericardial dissemination", ["Lymphogenous or haematogenous metastasis", "Invasion into fatty tissue", "Complete encapsulation"])
q(543, S18, "Masaoka stage IVB thymoma:", "Lymphogenous or hematogenous metastasis", ["Pleural dissemination", "Pericardial dissemination", "Capsular invasion only"])

S19 = "Mediastinal Germ Cell Tumors"
q(543, S19, "M/c EXTRA GONADAL site of germ cell tumors:", "Anterior mediastinum", ["Posterior mediastinum", "Retroperitoneum", "Pineal gland"])
q(543, S19, "Sex predilection of mediastinal germ cell tumors:", "Males > females", ["Females > males", "Equal", "Only females"])
q(543, S19, "A BENIGN mediastinal germ cell tumor is usually a:", "Teratoma", ["Seminoma", "Yolk sac tumour", "Choriocarcinoma"])
q(543, S19, "Tumor markers raised in malignant mediastinal germ cell tumors:", "αFP, LDH and β-hCG", ["CEA and CA 19-9", "Chromogranin and NSE", "CA-125"])
q(543, S19, "Management of a mediastinal germ cell tumor:", "Excision, followed by chemotherapy if malignant", ["Radiotherapy alone", "Observation", "Chemotherapy without excision"])

UNIT_DEFS = [
    (S1, "The right lung has three lobes, the left two. The right mainstem bronchus is shorter and straighter, so aspiration and foreign bodies land right — abscesses form m/c in the posterior upper lobe and superior lower lobe, while foreign bodies wheeze, cause stridor or collapse and are removed bronchoscopically after X-ray. Thoracoscore uses 9 criteria to predict mortality after lung resection, while FEV1 and DLCO predict post-operative dyspnoea."),
    (S2, "Primary spontaneous pneumothorax hits young, tall males, often with a family history, leaking from upper lobe blebs with normal lung function and good tolerance. Secondary pneumothorax follows TB, tumors or emphysema in older patients, who tolerate it far worse."),
    (S3, "Sharp pleuritic pain with a hyper-resonant note and absent breath sounds, diagnosed on chest X-ray. Bilateral or unstable → chest drain immediately. Age >50 with heavy smoking or evidence of lung disease means secondary. Primary: <2 cm and not breathless → discharge with OPD review in 2-4 weeks; >2 cm or breathless → aspirate, then an 8-14 Fr chest drain. Secondary: >2 cm or breathless → chest drain; 1-2 cm → aspirate; <1 cm → admit, high flow oxygen, observe 24 hours."),
    (S4, "Operate for a secondary ipsilateral pneumothorax, a first contralateral pneumothorax, bilateral spontaneous pneumothorax, failure to settle despite chest drainage, spontaneous haemothorax or at-risk professions such as pilots and divers, and in pregnancy."),
    (S5, "Interventions: pleurodesis with TALC or tetracycline, stripping the pleura by VATS — space made by collapsing one lung through a double lumen endotracheal tube — and ICD."),
    (S6, "Empyema is pus in the pleural space, arising from pulmonary infection (unresolved pneumonia, bronchiectasis, TB, fungi, lung abscess), aspiration of an effusion of any cause, trauma (penetrating injury, surgery, oesophageal perforation), extrapulmonary subphrenic abscess, or osteomyelitis of ribs and vertebrae."),
    (S7, "Three phases: exudative — fever and pus, a one-sided collection on CXR/CT, m/c Staph. aureus, treated by aspiration and antibiotics; fibrinopurulent — thickened pus and pleura needing a chest tube because aspiration fails; organized — thickened pleura entrapping the lung, needing pleural stripping/VATS with decortication."),
    (S8, "Lung cancer follows smoking, pollution and asbestos; only 15-20% are resectable and immunotherapy has revolutionised treatment. Small cell (oat cell) carcinoma has the strongest smoking link, affects males more, carries a poor prognosis but is highly chemosensitive and produces the most paraneoplastic syndromes — Cushing's (ACTH), SIADH (ADH), acromegaly (GH-related peptide) and Lambert-Eaton (anti-VGCC). Pathology shows the Azzopardi effect with salt and pepper appearance; IHC is chromogranin and NCAM."),
    (S9, "SVC syndrome is an oncological emergency with facial and cerebral edema ± seizures, diagnosed on CECT and treated with radiotherapy to shrink the tumour plus steroids. Squamous cell carcinoma sits centrally, is the m/c lung cancer in smokers, and can form a Pancoast tumor pressing the thoracic inlet (dyspnoea, stridor) or the sympathetic chain (Horner's: ptosis, miosis, enophthalmos, anhydrosis) — treated with radiotherapy plus immunotherapy."),
    (S10, "Adenocarcinoma is the m/c lung cancer overall, commoner in females, peripheral and slow growing, developing in pre-existing cavities from TB or bronchiectasis, metastasising early, marked by NAPSIN A and ALK/RAS mutations."),
    (S11, "Bronchoalveolar carcinoma (adenocarcinoma in-situ) is multifocal, usually resectable with good prognosis, spreading along the broncho-alveolar lining in a lepidic pattern. Cough is the m/c symptom, with hemoptysis, pain and weight loss; brain is the m/c symptomatic metastasis while adrenal involvement is very common but asymptomatic."),
    (S12, "Work-up: CXR first, HRCT as IOC for extent, biopsy for type (CT guided, mediastinoscopy — which also checks operability — or EBUS FNAC), and PET-CT as the staging IOC."),
    (S13, "T1 is ≤3 cm surrounded by lung/visceral pleura without main bronchus involvement: T1a(mi) minimally invasive, T1a ≤1 cm, T1b >1-2 cm, T1c >2-3 cm. T2 is >3 to ≤5 cm, or main bronchus involvement sparing the carina, or visceral pleural invasion, or atelectasis/post obstructive pneumonitis reaching the hilum — T2a >3-4 cm, T2b >4-5 cm."),
    (S14, "Surgery suits T1-T2 and T3 with N0/N1: lobectomy, pneumonectomy or sleeve resection through a posterolateral thoracotomy, risking bleeding, respiratory infection, persistent air leak and bronchopleural fistula. Squamous cell carcinoma is highly radiosensitive, and chemo/immunotherapy is the latest modality for all carcinomas, especially advanced disease."),
    (S15, "Summary: SCC — M>F, central, smoking, hypercalcemia, P53, CIS precursor. Adenocarcinoma — F>M, peripheral, non smokers, migratory thrombophlebitis, K ras/EGFR/ALK, AIS and AAH precursors. Small cell — M>F, central, strongest smoking link, Cushing's and SIADH, L-myc, DIPNEH precursor. Large cell — M>F, peripheral, both smokers and non smokers, gynecomastia."),
    (S16, "Histology: SCC keratin pearls and desmosomes (CK, P63, P40); adenocarcinoma glands lined by pleomorphic cells (TTF-1, NAPSIN A); small cell salt & pepper chromatin, nuclear moulding, Azzopardi effect (NSE, chromogranin, synaptophysin); large cell large pleomorphic cells. Hamartoma is the m/c benign lung tumour — usually asymptomatic, sometimes cough or hemoptysis, a coin shaped lesion on CXR confirmed by CT and excised under VATS."),
    (S17, "Mediastinal tumors by compartment: superior — lymphoma, thyroid, parathyroid; anterior — the 3 T's, thymoma (m/c mediastinal tumour), teratoma and terrible lymphoma; middle — cystic lesions, m/c pericardial cyst, plus lymphoma and mesenchymal tumors; posterior — neurogenic tumors, the m/c mediastinal tumour in children, and cystic lesions."),
    (S18, "Thymoma is the m/c mediastinal tumour overall, sits anteriorly, is usually benign and associates with myasthenia gravis; small lesions go transcervically, large ones by VATS or thoracotomy. Masaoka staging: I encapsulated without microscopic capsular invasion; II macroscopic invasion into mediastinal fat or pleura with microscopic capsular invasion; III invasion into pericardium, great vessels or lungs; IVA pleural or pericardial dissemination; IVB lymphogenous or haematogenous metastasis."),
    (S19, "The anterior mediastinum is the m/c extragonadal site for germ cell tumors, commoner in males; benign ones are teratomas while malignant ones raise αFP, LDH and β-hCG. Excise, and add chemotherapy if malignant."),
]

first_page = {}
for x in Q:
    first_page.setdefault(x["sec"], x["page"])

UNITS = []
for i, (title, guide) in enumerate(UNIT_DEFS, 1):
    UNITS.append({
        "id": f"SURG-U69-{i}",
        "ch": 69,
        "n": i,
        "title": title,
        "sec": f"{title} · p{first_page[title]}",
        "qs": [x["id"] for x in Q if x["sec"] == title],
        "guide": guide,
    })

covered = [x for u in UNITS for x in u["qs"]]
assert covered == [x["id"] for x in Q]
with open("data/ch69.json", "w", encoding="utf-8") as f:
    json.dump({"questions": Q, "units": UNITS}, f, ensure_ascii=False, indent=1)
print(f"ch69: {len(Q)} questions, {len(UNITS)} units")
