#!/usr/bin/env python3
"""Build data/ch61.json — Venous Thrombosis (Marrow Surgery Ed 8, pp470-475)."""
import json

Q = []


def q(page, sec, text, correct, wrongs, note=None):
    opts = [correct] + list(wrongs)
    assert len(opts) == 4
    Q.append({
        "id": f"SURG-C61-{len(Q)+1:03d}",
        "sec": sec,
        "page": page,
        "q": text,
        "opts": opts,
        "ans": 0,
        "exp": (note or correct) + f" (Book p{page})",
    })


# ------------------------------------------------------------------ p470
S1 = "Anatomy of Lower Limb Deep Veins"
q(470, S1, "Chapter that opens the Vascular Surgery section at p470:", "Venous thrombosis", ["Varicose veins", "Arterial system", "Lymphatic system"])
q(470, S1, "Number of pairs of deep/superficial veins of the calf described:", "3 pairs", ["1 pair", "2 pairs", "4 pairs"], "3 pairs of veins carry 80% of blood")
q(470, S1, "Percentage of blood carried by the 3 paired calf veins:", "80%", ["20%", "50%", "95%"])
q(470, S1, "The 3 paired calf veins are:", "Peroneal, anterior tibial and posterior tibial veins", ["Popliteal, femoral and saphenous veins", "Great and small saphenous veins", "Profunda femoris and obturator veins"])
q(470, S1, "The paired calf veins join to form:", "Femoral vein", ["Popliteal artery", "Great saphenous vein", "External iliac artery"])
q(470, S1, "Vein labelled at the top of the deep venous diagram:", "Common femoral vein", ["Peroneal vein", "Popliteal vein", "Anterior tibial vein"])
q(470, S1, "Junction where the great saphenous vein drains, shown in the diagram:", "Saphenofemoral junction", ["Sapheno-popliteal junction", "Ilio-caval junction", "Perforator junction"])
q(470, S1, "Deep branch labelled beside the superficial femoral vein:", "Profunda femoral vein", ["Peroneal vein", "Obturator vein", "Inferior gluteal vein"])
q(470, S1, "Vein lying between the femoral and calf veins in the diagram:", "Popliteal vein", ["Common iliac vein", "Profunda femoral vein", "Saphenofemoral junction"])
q(470, S1, "Peroneal, anterior tibial and posterior tibial veins are described as:", "Usually paired", ["Always single", "Always triple", "Absent in most people"])

S2 = "Lower Limb DVT: Definition and Complications"
q(470, S2, "Definition of deep vein thrombosis:", "Semi solid coagulum in the deep veins", ["Liquid blood in superficial veins", "Air embolus in deep veins", "Fatty plaque in deep veins"])
q(470, S2, "DVT is the m/c cause of death following which surgery:", "Bariatric surgery", ["Thyroid surgery", "Hernia surgery", "Cataract surgery"])
q(470, S2, "Complications of DVT:", "Pulmonary embolism and post thrombotic limb", ["Stroke and MI", "Aneurysm and dissection", "Gangrene of bowel and stoma"])
q(470, S2, "Life-threatening complication of DVT:", "Pulmonary embolism", ["Post thrombotic limb", "Varicose veins", "Lipodermatosclerosis"])
q(470, S2, "Chronic complication of DVT affecting the limb:", "Post thrombotic limb", ["Pulmonary embolism", "Cor pulmonale", "Renal failure"])

S3 = "Virchow's Triad and Patient Risk Factors"
q(470, S3, "Triad describing the risk factors of DVT:", "Virchow's triad", ["Beck's triad", "Charcot's triad", "Saint's triad"])
q(470, S3, "First component of Virchow's triad:", "Stasis", ["Hypercoagulability", "Endothelial injury", "Hypoxia"])
q(470, S3, "Second component of Virchow's triad:", "Hypercoagulability", ["Stasis", "Endothelial injury", "Inflammation"])
q(470, S3, "Third component of Virchow's triad:", "Endothelial injury", ["Stasis", "Hypercoagulability", "Hyperviscosity"])
q(470, S3, "Patient factors for DVT include all of the following EXCEPT:", "Young age with active lifestyle", ["Age", "Obesity", "Immobility"])
q(470, S3, "Obesity and immobility increase DVT risk mainly by:", "Stasis", ["Endothelial injury", "Hypocoagulability", "Fibrinolysis"])
q(470, S3, "Venous condition listed as a patient risk factor for DVT:", "Varicose veins", ["Arterial aneurysm", "Lymphedema", "AV fistula"])
q(470, S3, "Pregnancy, puerperium and high dose estrogen therapy together constitute a:", "Prothrombotic state", ["Hypocoagulable state", "Fibrinolytic state", "Immunodeficient state"])
q(470, S3, "Hormonal therapy listed as a DVT risk factor:", "High dose estrogen therapy", ["Low dose thyroxine", "Insulin therapy", "Testosterone gel"])
q(470, S3, "Previous history of which conditions raises DVT risk:", "Previous DVT / pulmonary embolism", ["Previous appendicectomy", "Previous hernia repair", "Previous cataract surgery"])
q(470, S3, "Inherited/acquired clotting tendency listed as a patient factor:", "Thrombophilia", ["Haemophilia", "Von Willebrand disease", "ITP"])
q(470, S3, "Malignancy contributes to DVT as a:", "Patient risk factor (tumors/cancers)", ["Protective factor", "Cause of hypocoagulability", "Cause of arterial embolism only"])

# ------------------------------------------------------------------ p471
S4 = "Disease and Surgical Procedure Risk Factors"
q(471, S4, "Disease/surgical procedure risk factors act through:", "Tissue factor", ["Protein C", "Plasminogen", "Antithrombin III"])
q(471, S4, "Trauma/surgery at which sites carries highest DVT risk:", "Hip, pelvis and lower limb", ["Hand and wrist", "Face and scalp", "Thyroid and neck"])
q(471, S4, "Malignancies most associated with DVT:", "Pelvic malignancies and abdominal metastases", ["Skin basal cell carcinoma", "Lip carcinoma", "Thyroid microcarcinoma"])
q(471, S4, "Cardiac conditions predisposing to DVT:", "Heart failure and recent myocardial infarction", ["Mitral valve prolapse only", "Innocent murmur", "Sinus arrhythmia"])
q(471, S4, "Neurological risk factor for DVT:", "Paralysis of lower limbs", ["Facial palsy", "Trigeminal neuralgia", "Carpal tunnel syndrome"])
q(471, S4, "Metabolic risk factor listed for DVT:", "Homocystinemia", ["Hypercalcemia", "Hypokalemia", "Hyponatremia"])
q(471, S4, "May-Thurner syndrome is:", "Right iliac artery compresses left iliac vein", ["Left iliac artery compresses right iliac vein", "Aorta compresses IVC", "SMA compresses duodenum"])
q(471, S4, "Vein compressed in May-Thurner syndrome:", "Left iliac vein", ["Right iliac vein", "Left renal vein", "IVC"])
q(471, S4, "Bowel disease listed as a DVT risk factor:", "Inflammatory bowel disease", ["Irritable bowel syndrome", "Celiac disease", "Lactose intolerance"])
q(471, S4, "Renal condition predisposing to DVT:", "Nephrotic syndrome", ["Nephritic syndrome", "Renal calculi", "Hydronephrosis"])
q(471, S4, "Haematological condition listed as a DVT risk factor:", "Polycythemia", ["Anaemia", "Leukopenia", "Thrombocytopenia"])
q(471, S4, "Plasma protein disorder predisposing to DVT:", "Paraproteinemia", ["Hypoalbuminemia", "Hypogammaglobulinemia", "Alpha-1 antitrypsin excess"])
q(471, S4, "Antibody states predisposing to thrombosis:", "PNH antibody or lupus anticoagulant", ["Anti-TPO antibody", "Anti-GBM antibody", "Rheumatoid factor"])
q(471, S4, "Vasculitis listed as a risk factor for venous thrombosis:", "Behcet's disease", ["Kawasaki disease", "Henoch-Schonlein purpura", "Takayasu arteritis"])
q(471, S4, "M/c inherited thrombophilia mutation listed:", "Factor V Leiden mutation", ["Factor VIII deficiency", "Factor IX mutation", "Prothrombin deficiency"])
q(471, S4, "Deficiency of which natural anticoagulants predisposes to DVT:", "Protein C and S deficiency", ["Protein A deficiency", "Factor VII deficiency", "Fibrinogen deficiency"])

S5 = "Clinical Features and Signs of DVT"
q(471, S5, "Most DVTs are:", "Mostly asymptomatic", ["Always painful", "Always bilateral", "Always with fever"])
q(471, S5, "Laterality of DVT:", "Usually unilateral; bilateral in 20-30% cases", ["Always bilateral", "Always unilateral", "Bilateral in 80%"])
q(471, S5, "Percentage of DVT that is bilateral:", "20-30%", ["5-10%", "50-60%", "80-90%"])
q(471, S5, "M/c vein involved in lower limb DVT:", "Calf / soleal veins", ["Ilio-femoral veins", "Great saphenous vein", "Popliteal artery"])
q(471, S5, "M/c vein responsible for pulmonary embolism:", "Ilio-femoral veins", ["Calf veins", "Soleal veins", "Small saphenous vein"])
q(471, S5, "Risk of pulmonary embolism with proximal veins:", "Increased risk", ["Decreased risk", "No risk", "Same as calf veins"])
q(471, S5, "Clinical features of pulmonary embolism include:", "Chest pain, dyspnoea, ↑JVP and ↓SBP", ["Chest pain with ↓JVP and ↑SBP", "Fever with bradycardia only", "Haematuria and flank pain"])
q(471, S5, "Effect of pulmonary embolism on JVP:", "↑ JVP", ["↓ JVP", "No change in JVP", "Absent JVP"])
q(471, S5, "Effect of pulmonary embolism on systolic BP:", "↓ SBP", ["↑ SBP", "No change", "Wide pulse pressure"])
q(471, S5, "Constant sign of DVT:", "Limb edema", ["Moses sign", "Homan's sign", "Cough impulse"])
q(471, S5, "Moses sign is:", "Pain on squeezing the calf muscles", ["Pain on dorsiflexion of foot", "Pain on hip flexion", "Pain on percussion of the vein"])
q(471, S5, "Homan's sign is:", "Resistance in calf on dorsiflexion of the foot", ["Pain on squeezing calf", "Pain on plantar flexion", "Loss of adductor reflex"])

S6 = "Phlegmasia Cerulea and Alba Dolens"
q(471, S6, "Phlegmasia cerulea dolens presents with:", "Painful blue limbs", ["Painful white limb", "Painless swollen limb", "Cold pulseless white limb only"])
q(471, S6, "Pathology of phlegmasia cerulea dolens:", "Thrombosis of major axial veins + collaterals", ["Thrombosis of axial veins with collaterals spared", "Arterial thrombosis", "Lymphatic obstruction"])
q(471, S6, "Phlegmasia cerulea dolens can lead to:", "Venous gangrene", ["Arterial aneurysm", "Lymphedema praecox", "Compartment sparing"])
q(471, S6, "Phlegmasia alba dolens is also known as:", "Milk leg", ["Blue leg", "Champagne leg", "Elephant leg"])
q(471, S6, "Phlegmasia alba dolens presents with:", "Painful white limb", ["Painful blue limb", "Painless red limb", "Black gangrenous limb"])
q(471, S6, "Pathology of phlegmasia alba dolens:", "Thrombosis of major axial veins with collaterals spared", ["Thrombosis of axial veins plus collaterals", "Arterial embolism", "Superficial vein thrombosis"])
q(471, S6, "Phlegmasia alba dolens is common during:", "Pregnancy", ["Childhood", "Old age only", "Post-menopause"])
q(471, S6, "Difference between cerulea and alba dolens lies in involvement of:", "Collaterals (involved in cerulea, spared in alba)", ["Arteries", "Lymphatics", "Perforators only"])

# ------------------------------------------------------------------ p472
S7 = "Wells' Criteria for Predicting DVT"
q(472, S7, "Wells' criteria are used for:", "Predicting DVT", ["Staging cancer", "Grading burns", "Predicting shock"])
q(472, S7, "Score for lower limb trauma or surgery or immobilisation in a plaster cast:", "1", ["2", "3", "-2"])
q(472, S7, "Score for being bedridden >3 days or surgery in last 4 weeks:", "1", ["2", "3", "0"])
q(472, S7, "Score for tenderness along the line of femoral or popliteal veins:", "1", ["2", "3", "-2"])
q(472, S7, "Score for entire limb swollen:", "1", ["2", "3", "-2"])
q(472, S7, "Calf circumference criterion in Wells' score:", "Calf >3 cm larger circumference than the other side", ["Calf >1 cm larger", "Calf >5 cm larger", "Calf >10 cm larger"])
q(472, S7, "Level at which calf circumference is measured in Wells' criteria:", "10 cm below the tibial tuberosity", ["5 cm above the tibial tuberosity", "At the malleolus", "At mid-thigh"])
q(472, S7, "Score for pitting oedema in Wells' criteria:", "1", ["2", "3", "-2"])
q(472, S7, "Dilated collateral superficial veins score 1 point provided they are:", "Not varicose veins", ["Varicose veins", "Thrombosed veins", "Perforators"])
q(472, S7, "Score for previous DVT:", "1", ["2", "3", "-2"])
q(472, S7, "Malignancy scores 1 point if treated up to:", "6 months ago", ["1 month ago", "3 months ago", "2 years ago"])
q(472, S7, "Variable scoring 3 points in Wells' criteria:", "Intravenous drug abuse", ["Previous DVT", "Pitting oedema", "Entire limb swollen"])
q(472, S7, "Score given for 'alternative diagnosis more likely than DVT':", "-2", ["-1", "0", "+2"])
q(472, S7, "Wells' score of -2 to 0 indicates:", "Low probability (5%)", ["Moderate probability (17%)", "High probability (17-53%)", "Definite DVT"])
q(472, S7, "Wells' score of 1-2 indicates:", "Moderate probability (17%)", ["Low probability (5%)", "High probability (17-53%)", "No risk"])
q(472, S7, "Wells' score >2 indicates:", "High probability (17-53%)", ["Low probability (5%)", "Moderate probability (17%)", "Zero probability"])
q(472, S7, "Probability of DVT with a low Wells' score:", "5%", ["17%", "33%", "53%"])

S8 = "Investigations of DVT and Pulmonary Embolism"
q(472, S8, "IOC for DVT:", "Doppler / duplex scan", ["MRI", "CT angiography", "Venography"])
q(472, S8, "Duplex scan combines:", "Color doppler + B mode USG", ["CT + MRI", "X-ray + fluoroscopy", "PET + CT"])
q(472, S8, "If Doppler is inconclusive for proximal (iliac) veins, next investigation:", "MRI", ["Repeat Doppler", "CXR", "Plain X-ray pelvis"])
q(472, S8, "Gold standard investigation for pulmonary embolism:", "Pulmonary angiography (invasive)", ["CT angiography", "D-dimer", "Duplex scan"])
q(472, S8, "IOC for pulmonary embolism:", "CT angiography", ["Pulmonary angiography", "MRI", "V/Q scan"])
q(472, S8, "Pulmonary angiography is limited by the fact that it is:", "Invasive", ["Non-specific", "Unavailable", "Radiation free"])
q(472, S8, "D-dimer has a:", "High negative predictive value", ["High positive predictive value", "High specificity", "No clinical use"])
q(472, S8, "Increased D-dimer levels are seen in:", "DVT and post surgery", ["Only DVT", "Only malignancy", "Only pregnancy"])
q(472, S8, "A normal D-dimer is most useful to:", "Rule out DVT", ["Confirm DVT", "Stage DVT", "Predict PE severity"])

S9 = "Management: Anticoagulants and Monitoring"
q(472, S9, "Mainstay of DVT treatment:", "Anticoagulants", ["Thrombolysis", "IVC filter", "Surgery"])
q(472, S9, "Anticoagulants act by:", "Preventing propagation of clot", ["Dissolving the clot", "Trapping the clot", "Removing the clot"])
q(472, S9, "Anticoagulation regime for the first 5 days:", "LMWH + warfarin", ["Warfarin alone", "LMWH alone", "Aspirin alone"])
q(472, S9, "Reason warfarin is overlapped with LMWH initially:", "Warfarin initially induces a prothrombotic state", ["Warfarin is too weak", "LMWH is teratogenic", "LMWH causes bleeding"])
q(472, S9, "Treatment after 5 days:", "Only warfarin", ["Only LMWH", "Only aspirin", "Stop all anticoagulation"])
q(472, S9, "Duration of anticoagulation after a first episode of DVT:", "3 months", ["1 month", "6 weeks", "Lifelong"])
q(472, S9, "Duration of anticoagulation in recurrent DVT:", "Lifelong", ["3 months", "6 months", "1 year"])
q(472, S9, "Warfarin is monitored by:", "INR (International normalized ratio)", ["aPTT", "Platelet count", "Bleeding time"])
q(472, S9, "Target INR during warfarin therapy for DVT:", "2-3", ["1-1.5", "3-4", "4-5"])
q(472, S9, "Rationale for target INR of 2-3:", "Delayed clotting of blood is desired", ["Rapid clotting is desired", "Platelet inhibition", "Fibrinolysis"])
q(472, S9, "Target INR before surgery:", "1.4-1.5", ["2-3", "3-4", "<1"])
q(472, S9, "Agents used to reduce INR:", "FFP and prothrombin factor concentrates", ["Heparin and LMWH", "Aspirin and clopidogrel", "Streptokinase and urokinase"])
q(472, S9, "Preferred agent to reduce INR:", "Prothrombin factor concentrates", ["Fresh frozen plasma", "Platelet concentrate", "Cryoprecipitate"])
q(472, S9, "Anticoagulant continued in pregnant patients:", "LMWH", ["Warfarin", "Rivaroxaban", "Apixaban"])
q(472, S9, "Oral anticoagulant agents are avoided in pregnancy because they are:", "Teratogenic", ["Ineffective", "Too expensive", "Poorly absorbed"])

# ------------------------------------------------------------------ p473
S10 = "Heparin-sensitive Agents and NOACs"
q(473, S10, "Fondaparinux is a:", "Factor Xa inhibitor", ["Direct thrombin inhibitor", "Vitamin K antagonist", "Fibrinolytic"])
q(473, S10, "Bivalirudin is a:", "Direct thrombin inhibitor", ["Factor Xa inhibitor", "Vitamin K antagonist", "Antiplatelet"])
q(473, S10, "Fondaparinux and bivalirudin are used in patients who are:", "Sensitive to heparin", ["Pregnant", "Allergic to warfarin", "Children only"])
q(473, S10, "NOAC stands for:", "Novel anticoagulants", ["New oral antiplatelet class", "Nitrate oral anti-clot", "Non-operative anticoagulation care"])
q(473, S10, "Advantage of NOACs:", "No monitoring required", ["Cheaper than warfarin", "Safe in pregnancy", "Reversible with vitamin K"])
q(473, S10, "Rivaroxaban and apixaban are:", "Factor Xa inhibitors", ["Direct thrombin inhibitors", "Vitamin K antagonists", "Heparinoids"])

S11 = "Direct Thrombolysis"
q(473, S11, "Aim of direct thrombolysis:", "To dissolve the clot", ["To prevent clot propagation", "To trap the clot", "To bypass the clot"])
q(473, S11, "Agents used for direct thrombolysis:", "Streptokinase and urokinase", ["Heparin and warfarin", "Aspirin and clopidogrel", "Rivaroxaban and apixaban"])
q(473, S11, "Route of delivery of thrombolysis in DVT:", "Catheter induced", ["Intramuscular", "Oral", "Subcutaneous"])
q(473, S11, "Direct thrombolysis reduces the risk of:", "Post thrombotic limb", ["Pulmonary embolism only", "Bleeding", "Recurrent varicose veins"])
q(473, S11, "Thrombolysis is beneficial in patients:", "Presenting early", ["Presenting late", "With bleeding tendency", "With recent stroke"])
q(473, S11, "Type of DVT most likely to benefit from thrombolysis:", "Proximal DVT", ["Isolated calf DVT", "Superficial thrombophlebitis", "Asymptomatic DVT"])
q(473, S11, "Symptom severity favouring thrombolysis:", "Moderate/severe symptoms", ["Asymptomatic", "Mild symptoms only", "Any symptom level"])

S12 = "IVC Filter (Greenfield Filter)"
q(473, S12, "IVC filter is also called:", "Greenfield filter", ["Palmaz filter", "Amplatzer device", "Dormia basket"])
q(473, S12, "IVC filter is inserted:", "Under image guidance", ["Blindly at bedside", "Via open laparotomy always", "Through the femoral artery"])
q(473, S12, "Mechanism of action of an IVC filter:", "Entrapment of clot", ["Dissolution of clot", "Prevention of clot formation", "Bypass of the IVC"])
q(473, S12, "Indication for IVC filter — recurrent thromboembolism despite:", "Adequate anticoagulation", ["Compression stockings", "Early ambulation", "Thrombolysis"])
q(473, S12, "IVC filter is indicated in DVT patients with:", "Contraindications to anticoagulation (e.g. intracranial hemorrhage)", ["Mild calf pain", "Normal D-dimer", "First episode DVT on warfarin"])
q(473, S12, "Pulmonary condition that is an indication for IVC filter:", "Chronic pulmonary embolism with resultant pulmonary hypertension", ["Asthma", "COPD", "Pneumonia"])
q(473, S12, "IVC filter is indicated when the patient develops:", "Complications of anticoagulation", ["Therapeutic INR", "Resolution of clot", "Normal Doppler"])
q(473, S12, "Thrombus type that is an indication for IVC filter:", "Propagating iliofemoral venous thrombus in anticoagulation", ["Superficial thrombophlebitis", "Isolated peroneal vein thrombus", "Resolved calf thrombus"])
q(473, S12, "Indication for a RETRIEVABLE IVC filter in trauma:", "Prophylactic placement in a high-risk trauma patient (orthopedic, spinal cord)", ["All trauma patients", "Minor soft tissue injury", "Facial laceration"])
q(473, S12, "Retrievable IVC filter is used when contraindication to anticoagulation is:", "Short-term in duration", ["Permanent", "Absent", "Unknown"])
q(473, S12, "Retrievable IVC filter may be used for protection during:", "Venous thrombolytic therapy", ["Chemotherapy", "Dialysis", "Radiotherapy"])
q(473, S12, "Extensive thrombosis that is an indication for retrievable IVC filter:", "Extensive iliocaval thrombosis", ["Isolated soleal thrombosis", "Superficial varicosity", "Axillary vein thrombosis"])
q(473, S12, "Complications of IVC filter:", "Migration, bleeding and IVC blockage by clot", ["Pulmonary fibrosis", "Renal calculi", "Hepatic abscess"])
q(473, S12, "IVC blockage by clot leads to:", "↓ venous return → ↓ JVP → ↓ CO, ↓ SBP", ["↑ venous return → ↑ CO", "↑ JVP with ↑ SBP", "No haemodynamic change"])
q(473, S12, "Management of IVC blockage by clot after filter placement:", "IV fluids", ["Diuretics", "Vasodilators", "Beta blockers"])
q(473, S12, "JVP in pulmonary embolism versus IVC filter blockage:", "↑ JVP in PE; ↓ JVP in IVC blockage", ["↓ JVP in PE; ↑ JVP in IVC blockage", "↑ in both", "↓ in both"])

# ------------------------------------------------------------------ p474
S13 = "Post Thrombotic Limb"
q(474, S13, "Post thrombotic limb is seen in what proportion of DVT patients:", "2/3rd", ["1/10th", "1/3rd", "All patients"])
q(474, S13, "Mechanism of post thrombotic limb:", "Deep vein clot diverts flow into superficial veins causing varicosities", ["Arterial insufficiency", "Lymphatic blockage", "Neuropathy"])
q(474, S13, "Features of post thrombotic limb:", "Varicose veins, pigmentation and lipodermatosclerosis", ["Pallor, pulselessness, paralysis", "Fever, chills, rigors", "Clubbing and cyanosis"])
q(474, S13, "Lipodermatosclerosis gives which appearance:", "Inverted champagne bottle appearance", ["Bottle neck appearance", "Bag of worms appearance", "Orange peel appearance"])
q(474, S13, "Skin change seen in post thrombotic limb:", "Pigmentation", ["Depigmentation", "Hypertrichosis", "Vitiligo"])
q(474, S13, "Risk factors for post thrombotic limb:", "Proximal DVT, subtherapeutic anticoagulation and recurrent DVT", ["Distal calf DVT only", "Adequate anticoagulation", "Single episode treated early"])
q(474, S13, "Treatment indicated in patients at risk of post thrombotic limb:", "Direct thrombolysis", ["IVC filter", "Amputation", "Antibiotics"])
q(474, S13, "Subtherapeutic anticoagulation increases risk of:", "Post thrombotic limb", ["Bleeding", "Heparin allergy", "Osteoporosis"])

S14 = "DVT Risk Groups and Prophylaxis"
q(474, S14, "High-risk group for DVT includes major orthopaedic surgery or fracture of:", "Pelvis, hip, lower limb", ["Wrist, hand", "Clavicle, scapula", "Nasal bones"])
q(474, S14, "Abdominal/pelvic surgery is high risk for DVT when performed for:", "Cancer", ["Hernia", "Appendicitis", "Gall stones"])
q(474, S14, "Major surgery/trauma/medical illness in a patient with DVT, PE or 3 thrombophilia is:", "High risk", ["Low risk", "Moderate risk", "No risk"])
q(474, S14, "Neurological condition placing patients in the high DVT risk group:", "Lower limb paralysis (stroke, paraplegia)", ["Migraine", "Bell's palsy", "Epilepsy"])
q(474, S14, "Amputation level placing the patient in a high DVT risk group:", "Major lower limb amputation", ["Finger amputation", "Toe nail avulsion", "Ear lobe excision"])
q(474, S14, "Prophylaxis in the high risk group:", "Mechanical + pharmacological prophylaxis", ["Mechanical only", "Pharmacological only", "No prophylaxis"])
q(474, S14, "Two types of DVT prophylaxis:", "Pharmacological and mechanical", ["Surgical and radiological", "Medical and dietary", "Active and passive"])
q(474, S14, "Superior type of DVT prophylaxis:", "Pharmacological", ["Mechanical", "Both equal", "Neither"])
q(474, S14, "Drug of choice for pharmacological DVT prophylaxis:", "LMWH", ["Warfarin", "Aspirin", "Streptokinase"])
q(474, S14, "In surgical patients, last dose of LMWH is given:", "6 hours prior to surgery", ["1 hour prior to surgery", "12 hours after surgery", "At induction"])
q(474, S14, "Mechanical prophylaxis includes:", "Early ambulation and pneumatic compression stockings", ["Bed rest and traction", "Plaster cast", "Limb elevation only"])
q(474, S14, "Simplest mechanical prophylaxis measure:", "Early ambulation", ["Pneumatic compression stockings", "IVC filter", "LMWH"])
q(474, S14, "Device shown for mechanical prophylaxis in the images:", "Pneumatic compression stockings", ["Plaster cast", "Traction frame", "Tourniquet"])

# ------------------------------------------------------------------ p475
S15 = "Upper Limb DVT"
q(475, S15, "Causes of PRIMARY upper limb DVT:", "Paget-Schroetter disease and prothrombotic states", ["Cannula insertion and thoracic outlet obstruction", "Trauma and malignancy only", "Pregnancy and puerperium"])
q(475, S15, "Paget-Schroetter disease is thrombosis of:", "Axillary vein", ["Subclavian artery", "Cephalic vein", "Internal jugular vein"])
q(475, S15, "Risk factor for Paget-Schroetter disease:", "Repetitive arm movements", ["Prolonged bed rest", "Smoking", "Obesity"])
q(475, S15, "Diagnosis of Paget-Schroetter disease:", "Doppler", ["CT angiography", "MRI", "Venography"])
q(475, S15, "Management of Paget-Schroetter disease:", "Anticoagulation", ["Amputation", "Thrombectomy always", "Observation"])
q(475, S15, "Causes of SECONDARY upper limb DVT:", "Thoracic outlet obstruction and cannula insertion", ["Paget-Schroetter disease", "Factor V Leiden", "Protein C deficiency"])
q(475, S15, "Paget-Schroetter disease is classified as:", "Primary upper limb DVT", ["Secondary upper limb DVT", "Superficial thrombophlebitis", "Lymphangitis"])

S16 = "Superficial Thrombophlebitis"
q(475, S16, "Superficial thrombophlebitis is:", "Inflammation and thrombosis of superficial veins", ["Inflammation of deep veins", "Arterial thrombosis", "Lymphatic inflammation"])
q(475, S16, "M/c cause of superficial thrombophlebitis:", "IV line insertion", ["Malignancy", "Pregnancy", "Trauma"])
q(475, S16, "Features of superficial thrombophlebitis:", "Tenderness and cord like swelling", ["Painless swelling", "Pulsatile mass", "Cold pale limb"])
q(475, S16, "Management of superficial thrombophlebitis:", "Thrombophob gel", ["Warfarin lifelong", "IVC filter", "Amputation"])
q(475, S16, "Swelling described in superficial thrombophlebitis:", "Cord like swelling", ["Bag of worms", "Fluctuant abscess", "Pulsatile swelling"])
q(475, S16, "Superficial thrombophlebitis differs from DVT in that it involves:", "Superficial veins", ["Deep veins", "Arteries", "Lymphatics"])

# ------------------------------------------------------------------ units
UNIT_DEFS = [
    (S1, "Three paired calf veins — peroneal, anterior tibial and posterior tibial — carry 80% of the leg's blood and merge upward into the popliteal and then femoral vein, with the profunda femoris and saphenofemoral junction joining near the groin. Fix this map first: everything about DVT location, risk and embolism follows the anatomy."),
    (S2, "DVT is simply a semi-solid coagulum sitting in a deep vein — but it is the m/c cause of death after bariatric surgery. Two complications matter: pulmonary embolism (acute killer) and post thrombotic limb (chronic misery)."),
    (S3, "Virchow's triad — stasis, hypercoagulability, endothelial injury — organises every DVT risk factor. Patient factors: age, obesity and immobility (stasis), varicose veins, pregnancy/puerperium/high dose estrogen (prothrombotic state), previous DVT or PE, thrombophilia and tumours."),
    (S4, "Disease and procedure factors work through tissue factor: hip/pelvis/lower-limb trauma or surgery, pelvic malignancy with abdominal metastases, heart failure, recent MI, lower limb paralysis, infection, homocystinemia and May-Thurner (right iliac artery squashing the left iliac vein). Add IBD, nephrotic syndrome, polycythemia, paraproteinemia, PNH/lupus anticoagulant, Behcet's, factor V Leiden and protein C & S deficiency."),
    (S5, "Most DVT is silent — usually unilateral, bilateral in 20-30%, most often in calf/soleal veins. Emboli come from the ilio-femoral veins (proximal = higher risk), producing chest pain, dyspnoea, ↑JVP and ↓SBP. Limb edema is the constant sign; Moses = pain on squeezing calf, Homan's = resistance on dorsiflexion."),
    (S6, "Phlegmasia cerulea dolens — painful BLUE limb from thrombosis of axial veins PLUS collaterals — can progress to venous gangrene. Phlegmasia alba dolens — 'milk leg', painful WHITE limb with collaterals spared — is common in pregnancy. The collaterals decide the colour."),
    (S7, "Wells' criteria: almost every variable scores 1 (limb trauma/cast, bedridden >3 days or surgery within 4 weeks, tenderness over femoral/popliteal line, entire limb swollen, calf >3 cm larger measured 10 cm below the tibial tuberosity, pitting oedema, dilated non-varicose collaterals, previous DVT, malignancy treated within 6 months), IV drug abuse scores 3, and an alternative diagnosis subtracts 2. Score -2 to 0 = low (5%), 1-2 = moderate (17%), >2 = high (17-53%)."),
    (S8, "IOC for DVT is the Doppler/duplex scan (colour doppler + B mode USG); if proximal iliac veins remain unclear, go to MRI. For pulmonary embolism, CT angiography is the IOC while invasive pulmonary angiography is the gold standard. D-dimer's value is its high negative predictive value — it rises in DVT and after surgery alike."),
    (S9, "Anticoagulation is the mainstay: it prevents clot propagation. LMWH + warfarin for 5 days (warfarin first induces a prothrombotic state), then warfarin alone — 3 months for a first episode, lifelong for recurrence. Monitor INR: target 2-3, but 1.4-1.5 before surgery; reverse with FFP or, preferably, prothrombin factor concentrates. In pregnancy stay on LMWH, since oral agents are teratogenic."),
    (S10, "Heparin-sensitive patients get fondaparinux (factor Xa inhibitor) or bivalirudin (direct thrombin inhibitor). NOACs — rivaroxaban and apixaban, both factor Xa inhibitors — need no monitoring."),
    (S11, "Direct thrombolysis dissolves rather than contains the clot: catheter-delivered streptokinase or urokinase, cutting the risk of post thrombotic limb. Reserve it for early presenters with proximal DVT and moderate/severe symptoms."),
    (S12, "The Greenfield IVC filter is placed under image guidance to entrap clot. Permanent indications: recurrent thromboembolism despite adequate anticoagulation, DVT with contraindication to anticoagulation (e.g. intracranial haemorrhage), chronic PE with pulmonary hypertension, complications of anticoagulation and propagating iliofemoral thrombus. Retrievable ones cover high-risk trauma prophylaxis, short-term contraindications, protection during thrombolysis and extensive iliocaval thrombosis. Beware migration, bleeding and IVC blockage — which drops venous return, JVP, CO and SBP (treat with IV fluids), the mirror image of PE's raised JVP."),
    (S13, "Two-thirds of DVT patients end with a post thrombotic limb: clot in the deep veins pushes flow into superficial veins, producing varicose veins, pigmentation and lipodermatosclerosis with its inverted champagne bottle leg. Proximal DVT, subtherapeutic anticoagulation and recurrent DVT are the risks — and the trigger for direct thrombolysis."),
    (S14, "High-risk DVT groups: major orthopaedic surgery or pelvic/hip/lower limb fracture, abdominal or pelvic cancer surgery, major surgery or trauma in a patient with DVT/PE/thrombophilia, lower limb paralysis and major lower limb amputation — all need mechanical PLUS pharmacological prophylaxis. Pharmacological (LMWH, last dose 6 hours before surgery) is superior; mechanical means early ambulation and pneumatic compression stockings."),
    (S15, "Primary upper limb DVT is Paget-Schroetter disease — axillary vein thrombosis from repetitive arm movements, diagnosed on Doppler and treated with anticoagulation — or a prothrombotic state. Secondary causes are thoracic outlet obstruction and cannula insertion."),
    (S16, "Superficial thrombophlebitis is inflammation plus thrombosis of superficial veins, most often after IV line insertion, giving tenderness and a cord-like swelling. Management is simple: Thrombophob gel."),
]

first_page = {}
for x in Q:
    first_page.setdefault(x["sec"], x["page"])

UNITS = []
for i, (title, guide) in enumerate(UNIT_DEFS, 1):
    UNITS.append({
        "id": f"SURG-U61-{i}",
        "ch": 61,
        "n": i,
        "title": title,
        "sec": f"{title} · p{first_page[title]}",
        "qs": [x["id"] for x in Q if x["sec"] == title],
        "guide": guide,
    })

covered = [x for u in UNITS for x in u["qs"]]
assert covered == [x["id"] for x in Q]
assert len(set(covered)) == len(covered)
with open("data/ch61.json", "w", encoding="utf-8") as f:
    json.dump({"questions": Q, "units": UNITS}, f, ensure_ascii=False, indent=1)
print(f"ch61: {len(Q)} questions, {len(UNITS)} units")
