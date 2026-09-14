#!/usr/bin/env python3
"""Build data/ch64.json — Arterial System : Part 2 (Marrow Surgery Ed 8, pp494-502)."""
import json

Q = []


def q(page, sec, text, correct, wrongs, note=None):
    opts = [correct] + list(wrongs)
    assert len(opts) == 4
    Q.append({
        "id": f"SURG-C64-{len(Q)+1:03d}",
        "sec": sec,
        "page": page,
        "q": text,
        "opts": opts,
        "ans": 0,
        "exp": (note or correct) + f" (Book p{page})",
    })


# ------------------------------------------------------------------ p494
S1 = "Aneurysm: Definition and M/C Sites"
q(494, S1, "Definition of an aneurysm:", "Dilatation of a vessel", ["Narrowing of a vessel", "Occlusion of a vessel", "Inflammation of a vessel"])
q(494, S1, "M/c type of aneurysm:", "Fusiform", ["Saccular", "Dissecting", "False"])
q(494, S1, "M/c vessel involved by aneurysm:", "Circle of Willis", ["Abdominal aorta", "Popliteal artery", "Splenic artery"])
q(494, S1, "M/c EXTRACRANIAL vessel involved by aneurysm:", "Infra renal abdominal aorta", ["Circle of Willis", "Popliteal artery", "Splenic artery"])
q(494, S1, "M/c PERIPHERAL vessel aneurysm:", "Popliteal artery", ["Femoral artery", "Carotid artery", "Radial artery"])
q(494, S1, "M/c VISCERAL vessel aneurysm:", "Splenic", ["Hepatic", "Renal", "Superior mesenteric"])
q(494, S1, "M/c site of a mycotic aneurysm:", "Aorta", ["Popliteal artery", "Splenic artery", "Circle of Willis"])
q(494, S1, "M/c cause of a mycotic aneurysm:", "S. aureus", ["E. coli", "Salmonella typhi", "Streptococcus viridans"])

S2 = "Abdominal Aortic Aneurysm: Site, Screening and Critical Diameter"
q(494, S2, "M/c site of abdominal aortic aneurysm:", "Infra renal abdominal aorta", ["Supra renal aorta", "Aortic arch", "Descending thoracic aorta"])
q(494, S2, "Major risk factor for abdominal aortic aneurysm:", "Atherosclerosis", ["Trauma", "Infection", "Vasculitis"])
q(494, S2, "Screening protocol for AAA in the UK:", "USG from 65 years", ["CT from 50 years", "MRI from 40 years", "X-ray from 70 years"])
q(494, S2, "Critical diameter of an abdominal aortic aneurysm:", "5.5 cm", ["4 cm", "6 cm", "7 cm"])
q(494, S2, "Critical diameters in females are:", "Less by 0.5 cm", ["Greater by 0.5 cm", "The same", "Less by 2 cm"])
q(494, S2, "Critical diameter for an ASCENDING thoracic aortic aneurysm:", "5.5 cm or 0.5 cm increase in size per year", ["6 cm", "4.5 cm", "7 cm"])
q(494, S2, "Critical diameter for a DESCENDING thoracic aortic aneurysm:", "6 cm", ["5.5 cm", "4.5 cm", "7 cm"])
q(494, S2, "Critical diameter for thoracic aortic aneurysm in Marfan patients:", "4.5-5 cm", ["5.5 cm", "6 cm", "7 cm"])
q(494, S2, "Significance of exceeding the critical diameter:", "Increased chance of rupture", ["Spontaneous resolution", "Reduced mortality", "No clinical consequence"])

S3 = "AAA: Clinical Features, Rupture and Investigations"
q(494, S3, "Most abdominal aortic aneurysms are:", "Asymptomatic", ["Always painful", "Always ruptured at presentation", "Always pulsatile and tender"])
q(494, S3, "Classic examination finding in AAA:", "Pulsatile mass", ["Non-pulsatile mass", "Fluctuant swelling", "Hard fixed mass"])
q(494, S3, "Blue toe syndrome is:", "Gangrene due to emboli blocking toe vessels", ["Cyanosis due to venous congestion", "Frostbite of toes", "Raynaud's phenomenon"])
q(494, S3, "M/c site of rupture of an abdominal aortic aneurysm:", "Left retroperitoneum", ["Right retroperitoneum", "Peritoneal cavity", "Duodenum"])
q(494, S3, "Presentation of a ruptured abdominal aortic aneurysm:", "Shock", ["Chronic anaemia", "Painless swelling", "Fever"])
q(494, S3, "Mortality of a ruptured abdominal aortic aneurysm:", "50%", ["2-3%", "10%", "90%"])
q(494, S3, "Screening investigation for AAA:", "USG", ["CT angiography", "MRI", "DSA"])
q(494, S3, "IOC for abdominal aortic aneurysm:", "CT angiography", ["USG", "MRI", "Plain X-ray"])

# ------------------------------------------------------------------ p495
S4 = "AAA Management, Guidelines and EVAR"
q(495, S4, "Conservative management of AAA is indicated when:", "<5.5 cm and asymptomatic", ["≥5.5 cm", "Symptomatic", "Ruptured"])
q(495, S4, "Intervention for AAA is indicated when:", "≥5.5 cm or symptomatic", ["<5.5 cm and asymptomatic", "<4 cm", "Always"])
q(495, S4, "Two interventional options for AAA:", "Open graft surgery and EVAR", ["Thrombolysis and embolectomy", "Sympathectomy and stenting", "Amputation and grafting"])
q(495, S4, "1st line per NICE guidelines for AAA:", "Open surgical repair", ["EVAR", "Conservative management", "Thrombolysis"])
q(495, S4, "Per NICE guidelines, EVAR is used for:", "High risk / hostile abdomen", ["All patients", "Young patients only", "Ruptured aneurysms only"])
q(495, S4, "Per the European Society for Vascular Surgery, 1st line in young patients:", "EVAR", ["Open surgical repair", "Conservative management", "Sympathectomy"])
q(495, S4, "EVAR stands for:", "Endovascular aneurysm repair", ["Endoluminal vascular arterial reconstruction", "External vascular aneurysm repair", "Endoscopic vein ablation repair"])
q(495, S4, "In EVAR, the stent graft is:", "Placed in the aorta", ["Placed in the femoral vein", "Placed in the IVC", "Placed extraluminally"])
q(495, S4, "Follow-up requirement after EVAR:", "Life long follow-up", ["6 weeks follow-up", "No follow-up", "1 year follow-up"])
q(495, S4, "Contraindications to EVAR:", "Difficult access and increased angulation of iliac vessels", ["Young age", "Small aneurysm", "Hostile abdomen"])
q(495, S4, "The EVAR graft's body is fixed in the:", "Aorta", ["Iliac vessels", "Femoral arteries", "Renal arteries"])
q(495, S4, "The EVAR graft's limbs are fixed in the:", "Iliac vessels", ["Aorta", "Renal arteries", "Femoral veins"])

S5 = "Endoleaks"
q(495, S5, "Main complication of EVAR:", "Endoleaks", ["Aortic dissection", "Renal calculi", "Colonic perforation"])
q(495, S5, "Type I endoleak is due to:", "Improper seal", ["Retrograde leak from lumbar vessels", "Direct leak from graft", "Porous graft"])
q(495, S5, "Type I endoleak is m/c after:", "Thoracic aortic aneurysm repair", ["Abdominal aortic aneurysm repair", "Popliteal aneurysm repair", "Carotid repair"])
q(495, S5, "Type II endoleak is due to:", "Retrograde leak from lumbar vessels", ["Improper seal", "Porous graft", "Endotension"])
q(495, S5, "Type II endoleak is m/c in:", "Abdominal aortic aneurysm", ["Thoracic aortic aneurysm", "Popliteal aneurysm", "Femoral aneurysm"])
q(495, S5, "Type III endoleak is due to:", "Direct leak from the graft", ["Improper seal", "Lumbar retrograde flow", "Endotension"])
q(495, S5, "Type IV endoleak is due to:", "Porous graft", ["Improper seal", "Direct graft leak", "Endotension"])
q(495, S5, "Type V endoleak is due to:", "Endotension", ["Porous graft", "Improper seal", "Lumbar collaterals"])

# ------------------------------------------------------------------ p496
S6 = "Open Graft Surgery and Abdominal Maneuvers"
q(496, S6, "Graft material used in open aneurysm surgery:", "Dacron / PTFE", ["Autologous skin", "Silicone", "Bovine bone"])
q(496, S6, "Mattox maneuver is:", "Left medial visceral rotation — left colon mobilized medially", ["Right medial visceral rotation", "Duodenal mobilization", "Splenic flexure resection"])
q(496, S6, "Structure exposed by the Mattox maneuver:", "Aorta", ["IVC", "Duodenum", "Pancreas"])
q(496, S6, "Cattell-Braasch maneuver is:", "Right medial visceral rotation — ascending colon mobilized medially", ["Left medial visceral rotation", "Kocherisation", "Pringle maneuver"])
q(496, S6, "Structure exposed by the Cattell-Braasch maneuver:", "IVC", ["Aorta", "Spleen", "Left kidney"])
q(496, S6, "Indication for the Cattell-Braasch maneuver:", "RCC with metastasis to IVC", ["AAA repair", "Splenectomy", "Left nephrectomy"])
q(496, S6, "Kocherisation refers to:", "Mobilization of the duodenum", ["Mobilization of the left colon", "Mobilization of the spleen", "Mobilization of the aorta"])

S7 = "Complications of Aneurysm Surgery"
q(496, S7, "M/c cause of death after aneurysm surgery:", "Cardiovascular complications", ["Renal failure", "Colonic ischaemia", "Paraparesis"])
q(496, S7, "Aorto-duodenal fistula is a rare cause of:", "Upper GI bleed", ["Lower GI bleed", "Haematuria", "Haemoptysis"])
q(496, S7, "IOC for aorto-duodenal fistula:", "CT angiography", ["Upper GI endoscopy", "USG", "MRI"])
q(496, S7, "Colonic ischaemia after aneurysm surgery is m/c on the:", "Left side of colon", ["Right side of colon", "Transverse colon only", "Caecum"])
q(496, S7, "Reason for left-sided colonic ischaemia after aneurysm surgery:", "Splenic flexure is a watershed area", ["Right colic artery is ligated", "Caecum has poor supply", "Rectum is devascularized"])
q(496, S7, "Presentation of colonic ischaemia after aneurysm surgery:", "Bloody diarrhoea", ["Constipation", "Haematemesis", "Jaundice"])
q(496, S7, "Paraparesis after aneurysm surgery is due to injury to the:", "Artery of Adamkiewicz", ["Artery of Drummond", "Marginal artery of Riolan", "Inferior mesenteric artery"])
q(496, S7, "Artery of Adamkiewicz supplies the:", "Anterior spinal artery", ["Posterior spinal artery", "Vertebral artery", "Renal artery"])
q(496, S7, "Mortality of ELECTIVE aneurysm surgery:", "2-3%", ["10%", "25%", "50%"])
q(496, S7, "Mortality of surgery for a RUPTURED aneurysm:", "50%", ["2-3%", "10%", "90%"])
q(496, S7, "Renal complication after aneurysm surgery:", "Renal failure", ["Renal calculi", "Renal cyst", "Hydronephrosis"])

# ------------------------------------------------------------------ p497
S8 = "Thoraco-abdominal Aortic Aneurysms (Crawford Classification)"
q(497, S8, "Classification used for thoraco-abdominal aortic aneurysms:", "Crawford classification", ["DeBakey classification", "Stanford classification", "CEAP classification"])
q(497, S8, "Crawford type I extends:", "Left subclavian to renal artery", ["Left subclavian to aortic bifurcation", "Mid descending aorta to aortic bifurcation", "Upper abdominal aorta to infra-renal aorta"])
q(497, S8, "Most extensive Crawford type:", "Type 2 — left subclavian to aortic bifurcation", ["Type 1", "Type 3", "Type 4"])
q(497, S8, "Crawford type 3 extends:", "Mid descending aorta to aortic bifurcation", ["Left subclavian to renal artery", "Left subclavian to aortic bifurcation", "Upper abdominal to infra-renal aorta"])
q(497, S8, "Crawford type 4 extends:", "Upper abdominal aorta to infra-renal aorta", ["Left subclavian to renal artery", "Mid descending aorta to bifurcation", "Left subclavian to bifurcation"])
q(497, S8, "Causes of thoraco-abdominal aortic aneurysm:", "Secondary to atherosclerosis and Marfan's syndrome", ["Trauma and infection only", "Vasculitis only", "Congenital only"])
q(497, S8, "Ortner's syndrome in thoraco-abdominal aneurysm is:", "Hoarseness due to pressure over the left recurrent laryngeal nerve", ["Dysphagia due to oesophageal pressure", "Dyspnea due to tracheal pressure", "Stridor from tracheal collapse"])
q(497, S8, "Pressure symptoms of a thoraco-abdominal aneurysm:", "Hoarseness, dysphagia and dyspnea", ["Haematuria and flank pain", "Jaundice and pruritus", "Claudication and rest pain"])
q(497, S8, "Screening investigation for thoraco-abdominal aortic aneurysm:", "USG", ["CT angiography", "MRI", "DSA"])
q(497, S8, "IOC for thoraco-abdominal aortic aneurysm:", "CT angiography", ["USG", "CXR", "MRI"])
q(497, S8, "Management of a symptomatic thoraco-abdominal aneurysm ≥5.5 cm:", "Graft repair", ["Conservative management", "Sympathectomy", "Thrombolysis"])

S9 = "Aortic Dissection: Pathology and Risk Factors"
q(497, S9, "Pathogenesis of aortic dissection:", "Tear in the tunica intima creating a false lumen with blood flowing between intima and media", ["Rupture of the adventitia", "Thrombosis of the vasa vasorum", "Aneurysmal dilatation of the whole wall"])
q(497, S9, "Blood in an aortic dissection flows between:", "Tunica intima and media", ["Media and adventitia", "Adventitia and pleura", "Intima and lumen"])
q(497, S9, "M/c site of aortic dissection:", "Lateral wall of ascending thoracic aorta", ["Descending thoracic aorta", "Abdominal aorta", "Aortic arch"])
q(497, S9, "Aortic dissection is a complication of aneurysm triggered by:", "Hypertension", ["Hypotension", "Anaemia", "Hypothermia"])

# ------------------------------------------------------------------ p498
S10 = "Aortic Dissection: Clinical Features and Investigations"
q(498, S10, "M/c symptom of aortic dissection:", "Chest pain with radiation to back", ["Abdominal pain", "Headache", "Haematuria"])
q(498, S10, "Gender predilection of aortic dissection:", "Male > female", ["Female > male", "Equal", "Only females"])
q(498, S10, "Age of presentation of aortic dissection:", "5th decade", ["2nd decade", "3rd decade", "8th decade"])
q(498, S10, "Characteristic BP finding in aortic dissection:", "Difference in BP between the 2 upper limbs and between upper and lower limb", ["Equal BP in all limbs", "Absent BP in all limbs", "Hypertension in the lower limb only"])
q(498, S10, "Complications of aortic dissection:", "Hypotension and coronary insufficiency", ["Hypertension and polycythemia", "Renal calculi", "Pulmonary fibrosis"])
q(498, S10, "1st investigation in suspected aortic dissection:", "CXR", ["CT angiography", "TEE", "MRI"])
q(498, S10, "CXR findings in aortic dissection:", "Widening of mediastinum and depression of the left main bronchus", ["Elevation of the left main bronchus", "Pleural calcification", "Cavitating lesion"])
q(498, S10, "IOC for a STABLE patient with aortic dissection:", "CT angiography", ["Transesophageal echocardiogram", "CXR", "MRI"])
q(498, S10, "IOC for an UNSTABLE patient with aortic dissection:", "Transesophageal echocardiogram", ["CT angiography", "CXR", "DSA"])

S11 = "Aortic Dissection: Classification and Management"
q(498, S11, "DeBakey type I dissection involves:", "Ascending + descending aorta", ["Only ascending aorta", "Only descending aorta", "Only the arch"])
q(498, S11, "M/c DeBakey type of aortic dissection:", "Type I", ["Type II", "Type III", "All equal"])
q(498, S11, "DeBakey type II dissection involves:", "Only ascending aorta", ["Only descending aorta", "Ascending and descending aorta", "Abdominal aorta"])
q(498, S11, "DeBakey type III dissection involves:", "Only descending aorta", ["Only ascending aorta", "Ascending and descending", "Aortic arch only"])
q(498, S11, "Stanford type A corresponds to:", "DeBakey types I and II", ["DeBakey type III only", "DeBakey type II only", "All DeBakey types"])
q(498, S11, "Stanford type B corresponds to:", "DeBakey type III", ["DeBakey type I", "DeBakey type II", "DeBakey types I and II"])
q(498, S11, "1st step in the management of aortic dissection:", "Short acting beta blocker (esmolol) / nicardipine", ["Immediate thoracotomy", "Thrombolysis", "Anticoagulation"])
q(498, S11, "Purpose of beta blockers in aortic dissection:", "To facilitate permissive hypotension (SBP at lower limit of normal)", ["To raise the blood pressure", "To increase heart rate", "To dissolve the clot"])
q(498, S11, "Management of DeBakey type I and II dissection:", "Thoracotomy + graft repair or EVAR", ["Conservative management only", "Observation", "Anticoagulation only"])
q(498, S11, "Management of DeBakey type III dissection:", "Conservative management + follow up, surgery if it progresses", ["Immediate thoracotomy in all", "EVAR in all", "Amputation"])

# ------------------------------------------------------------------ p499
S12 = "Popliteal and Femoral Artery Aneurysms"
q(499, S12, "Popliteal aneurysm is the:", "M/c peripheral vessel aneurysm", ["M/c visceral aneurysm", "M/c mycotic aneurysm", "Rarest aneurysm"])
q(499, S12, "Proportion of popliteal aneurysms that are bilateral:", "50%", ["10%", "25%", "90%"])
q(499, S12, "Clinical features of popliteal aneurysm:", "Swelling behind the knee, loss of contour, pain and emboli", ["Claudication in the buttock", "Hoarseness of voice", "Haematuria"])
q(499, S12, "IOC for popliteal aneurysm:", "Duplex / CT angiography", ["CXR", "MRI", "Plain X-ray knee"])
q(499, S12, "Management threshold for an ASYMPTOMATIC popliteal aneurysm:", ">2 cm — graft repair/EVAR", [">5.5 cm", ">10 cm", "Never operated"])
q(499, S12, "Management of a symptomatic popliteal aneurysm:", "Graft repair / EVAR", ["Observation", "Compression", "Amputation"])
q(499, S12, "Cause of femoral artery aneurysm:", "Puncture during blood draws / stenting procedures", ["Atherosclerosis only", "Infection only", "Congenital"])
q(499, S12, "Management of a femoral artery aneurysm <3 cm:", "Thrombin injection under USG guidance", ["Surgical repair", "Observation", "EVAR"])
q(499, S12, "Management of a femoral artery aneurysm >3 cm:", "Surgical repair", ["Thrombin injection", "Observation", "Compression"])

S13 = "Carotid Artery Aneurysm and Endarterectomy"
q(499, S13, "M/c site of carotid artery aneurysm:", "Aortic bifurcation", ["Carotid siphon", "Internal carotid at the skull base", "External carotid"], "The book records aortic bifurcation as the m/c site in this section")
q(499, S13, "M/c cause of carotid artery aneurysm:", "Atherosclerosis", ["Trauma", "Infection", "Marfan's syndrome"])
q(499, S13, "M/c presentation of carotid artery disease:", "Transient ischemic attack (TIA)", ["Hoarseness", "Dysphagia", "Headache"])
q(499, S13, "IOC for carotid artery aneurysm:", "Duplex scan", ["CT angiography", "MRI", "DSA"])
q(499, S13, "Degree of stenosis required for carotid endarterectomy:", "≥70%", ["≥30%", "≥50%", "100%"])
q(499, S13, "Ocular indication for carotid endarterectomy:", "Ipsilateral amaurosis fugax / monocular blindness", ["Contralateral amaurosis fugax", "Bilateral cataract", "Glaucoma"])
q(499, S13, "Facial indication for carotid endarterectomy:", "Contralateral facial paralysis", ["Ipsilateral facial paralysis", "Bilateral facial numbness", "Trigeminal neuralgia"])
q(499, S13, "Other neurological indications for carotid endarterectomy:", "Arm/leg paralysis, hemianopia and dysphasia", ["Vertigo alone", "Tinnitus", "Anosmia"])

# ------------------------------------------------------------------ p500
S14 = "Thoracic Outlet Syndrome"
q(500, S14, "Thoracic outlet syndrome is compression of:", "Subclavian vessels and brachial plexus in the thoracic outlet", ["Axillary nerve only", "Carotid artery and vagus", "Vertebral artery"])
q(500, S14, "Risk factors for thoracic outlet syndrome:", "Cervical rib, weak musculature and trauma", ["Diabetes and obesity", "Smoking alone", "Hypertension"])
q(500, S14, "Subclavian artery thrombus in thoracic outlet syndrome causes:", "Emboli and unilateral claudication", ["Bilateral swelling", "Hoarseness", "Dysphagia"])
q(500, S14, "Subclavian/axillary vein thrombosis in thoracic outlet syndrome causes:", "Swelling of the upper limb", ["Pallor of the limb", "Claudication", "Gangrene of fingers"])
q(500, S14, "Subclavian/axillary vein thrombosis is also known as:", "Paget-Schroetter syndrome", ["Leriche syndrome", "Ortner's syndrome", "May-Thurner syndrome"])
q(500, S14, "M/c nerve involved in brachial plexus compression in thoracic outlet syndrome:", "Ulnar nerve", ["Median nerve", "Radial nerve", "Musculocutaneous nerve"])
q(500, S14, "ADSON test maneuver:", "Arm abducted 30° and maximally extended, neck extended, head turned towards the ipsilateral shoulder, deep inhalation", ["Arms in surrender position with hands opening and closing", "Wrists dorsiflexed with arms at 90°", "Head tilted ear to shoulder"])
q(500, S14, "Positive result of the ADSON test:", "Decrease or absence of ipsilateral radial pulse", ["Increase in radial pulse", "Contralateral pain", "Loss of vision"])
q(500, S14, "EAST (elevated arm stress test) is also called:", "ROOS test", ["ELVEY test", "ADSON test", "Allen's test"])
q(500, S14, "EAST/ROOS maneuver:", "Arms in surrender position, shoulders abducted 90° in external rotation, elbows flexed 90°, hand opened and closed for 3 min", ["Deep inhalation with head turned", "Ear to shoulder tilt", "Wrist dorsiflexion only"])
q(500, S14, "Positive result of the EAST/ROOS test:", "Precipitates pain, paresthesias, heaviness or weakness", ["Loss of radial pulse only", "Contralateral symptoms only", "Loss of vision"])
q(500, S14, "ULTT is also called:", "ELVEY test", ["ROOS test", "ADSON test", "Branham test"])
q(500, S14, "ULTT position 1:", "Arms abducted to 90° with elbows flexed", ["Active dorsiflexion of both wrists", "Head tilted ear to shoulder", "Arms in surrender position"])
q(500, S14, "ULTT position 2:", "Active dorsiflexion of both wrists", ["Arms abducted with elbows flexed", "Head tilted ear to shoulder", "Deep inhalation"])
q(500, S14, "ULTT position 3:", "Head is tilted ear to shoulder, in both directions", ["Arms abducted to 90°", "Wrist dorsiflexion", "Deep inspiration"])
q(500, S14, "Interpretation of the ULTT:", "Positions 1 and 2 elicit ipsilateral symptoms, position 3 elicits contralateral symptoms", ["All positions elicit ipsilateral symptoms", "All positions elicit contralateral symptoms", "Only position 1 is diagnostic"])

# ------------------------------------------------------------------ p501
S15 = "Thoracic Outlet Syndrome: Investigations and Management"
q(501, S15, "IOC for thoracic outlet syndrome:", "CT angiography", ["Duplex scan", "MRI", "CXR"])
q(501, S15, "CXR in thoracic outlet syndrome is done to look for:", "Cervical rib", ["Pleural effusion", "Mediastinal widening", "Pneumothorax"])
q(501, S15, "Management of a cervical rib in thoracic outlet syndrome:", "Excision", ["Observation", "Radiotherapy", "Stenting"])
q(501, S15, "Excision of the cervical rib and physiotherapy are done to:", "Relieve neurological symptoms", ["Relieve venous congestion only", "Improve arterial flow only", "Prevent recurrence of embolism"])
q(501, S15, "Management of an arterial block in thoracic outlet syndrome:", "Stenting", ["Anticoagulation", "Physiotherapy", "Excision of rib alone"])
q(501, S15, "Management of a venous block in thoracic outlet syndrome:", "Anticoagulation", ["Stenting", "Physiotherapy", "Excision"])

S16 = "Cirsoid Aneurysm and A-V Fistulae"
q(501, S16, "Cirsoid aneurysm occurs in the region of the:", "Superficial temporal vessels", ["Popliteal vessels", "Femoral vessels", "Splenic vessels"])
q(501, S16, "Clinical feature of cirsoid aneurysm:", "Pulsatile swelling", ["Non-pulsatile hard mass", "Ulcer", "Cold pale limb"])
q(501, S16, "Management of a symptomatic cirsoid aneurysm:", "Surgery", ["Observation", "Compression", "Antibiotics"])
q(501, S16, "A-V fistula is:", "Abnormal communication between arteries and veins", ["Communication between two veins", "Communication between two arteries", "Blocked lymphatic channel"])
q(501, S16, "M/c cause of A-V fistulae:", "Iatrogenic (Cimino fistula)", ["Traumatic", "Congenital", "Infective"])
q(501, S16, "Cimino fistula is a:", "Radiocephalic fistula", ["Brachiobasilic fistula", "Femoral-saphenous fistula", "Carotid-jugular fistula"])
q(501, S16, "Cimino fistula is used for:", "Renal dialysis", ["Chemotherapy", "Blood transfusion", "Parenteral nutrition"])
q(501, S16, "Test done prior to creation of a Cimino fistula:", "Modified Allen's test", ["ADSON test", "Perthes test", "Trendelenburg test"])
q(501, S16, "Modified Allen's test assesses:", "Radio-ulnar patency", ["Venous reflux", "Arterial pressure", "Nerve conduction"])
q(501, S16, "Modified Allen's POSITIVE result:", "Ulnar artery released and patent — palm reperfuses", ["Hand remains pale", "Radial artery released and patent", "No colour change on release"])
q(501, S16, "Modified Allen's NEGATIVE result:", "Ulnar artery released and not patent — hand remains pale", ["Palm reperfuses quickly", "Radial artery occluded only", "Pulse increases"])
q(501, S16, "Congenital causes of A-V fistulae:", "Parkes-Weber syndrome and Sturge-Weber syndrome", ["Klippel-Trenaunay and Marfan syndrome", "Turner and Down syndrome", "Behcet's and Takayasu"])

# ------------------------------------------------------------------ p502
S17 = "A-V Fistulae: Features, Signs and Management"
q(502, S17, "Clinical feature of an A-V fistula:", "Pulsatile swelling", ["Non-pulsatile cold mass", "Ulcerated plaque", "Depigmented patch"])
q(502, S17, "Congenital A-V fistulae lead to:", "High output cardiac failure (hyperdynamic state) and hypertrophy of limb", ["Low output cardiac failure", "Limb atrophy", "Pulmonary fibrosis"])
q(502, S17, "Sign elicited by pressing the feeding vessel of an A-V fistula:", "Nicoladoni / Branham sign", ["Homan's sign", "Moses sign", "Tillaux sign"])
q(502, S17, "On pressing the feeding vessel, the size of the fistula:", "Decreases", ["Increases", "Stays the same", "Becomes pulsatile"])
q(502, S17, "On pressing the feeding vessel, the pulse rate:", "Decreases", ["Increases", "Stays the same", "Becomes irregular"])
q(502, S17, "On pressing the feeding vessel, the systolic BP:", "Increases markedly", ["Decreases", "Stays the same", "Becomes unrecordable"])
q(502, S17, "On pressing the feeding vessel, the bruit:", "Decreases", ["Increases", "Stays the same", "Becomes continuous"])
q(502, S17, "IOC for imaging an A-V fistula:", "MR angiography / DSA", ["USG", "CXR", "Plain X-ray"])
q(502, S17, "First-line management of an A-V fistula:", "Embolisation", ["Surgical excision", "Observation", "Compression"])
q(502, S17, "Embolisation is contraindicated in A-V fistula patients who are:", "Infected / IV drug abusers", ["Elderly", "Diabetic", "Hypertensive"])
q(502, S17, "Management when embolisation is contraindicated:", "Surgical excision", ["Observation", "Radiotherapy", "Anticoagulation"])

S18 = "Coronary Artery Bypass Grafting (CABG)"
q(502, S18, "Left main disease indication for CABG:", "Greater than 50%", ["Greater than 20%", "Greater than 70%", "Greater than 90%"])
q(502, S18, "Three-vessel coronary artery disease indication for CABG:", "Greater than 70% with or without proximal LAD involvement", ["Greater than 30%", "Greater than 50%", "Only with LAD involvement"])
q(502, S18, "Two-vessel disease indication for CABG:", "LAD plus one other major artery", ["Any two arteries except LAD", "Right coronary plus circumflex only", "Any single artery"])
q(502, S18, "CABG is indicated for one or more stenoses >70% in a patient with:", "Significant anginal symptoms despite maximal medical therapy", ["No symptoms", "Normal stress test", "Well-controlled angina"])
q(502, S18, "One vessel disease >70% is an indication for CABG in:", "A survivor of sudden cardiac death with ischemia-related ventricular tachycardia", ["Any asymptomatic patient", "A patient with atrial fibrillation", "A patient with heart failure alone"])
q(502, S18, "M/c graft used in CABG:", "Reversed great saphenous vein", ["LIMA", "RIMA", "Radial artery"])
q(502, S18, "M/c complication of reversed great saphenous vein harvesting:", "Saphenous nerve injury", ["Sural nerve injury", "Femoral vein injury", "Deep vein thrombosis"])
q(502, S18, "LIMA-LAD refers to:", "Left internal mammary artery used for the left anterior descending artery", ["Left iliac mammary artery to LAD", "Left internal mammary to left circumflex", "Radial artery to LAD"])
q(502, S18, "RIMA stands for:", "Right internal mammary artery", ["Right iliac mammary artery", "Right intercostal mammary artery", "Right internal maxillary artery"])
q(502, S18, "Arterial graft option in CABG besides the mammary arteries:", "Radial artery", ["Ulnar artery", "Brachial artery", "Popliteal artery"])

UNIT_DEFS = [
    (S1, "An aneurysm is a dilated vessel — usually fusiform. Memorise the m/c list: circle of Willis overall, infra-renal abdominal aorta extracranially, popliteal for peripheral, splenic for visceral, and the aorta for mycotic aneurysms (S. aureus)."),
    (S2, "AAA is atherosclerotic and sits in the infra-renal aorta; the UK screens with USG from age 65. Critical diameters — 5.5 cm abdominal, 5.5 cm (or growth 0.5 cm/year) ascending thoracic, 6 cm descending thoracic, 4.5-5 cm in Marfan patients — are 0.5 cm less in women, and crossing them means rupture risk."),
    (S3, "Most AAAs are silent until they announce themselves with abdominal pain, a pulsatile mass, or blue toe syndrome from toe-vessel emboli. Rupture usually goes into the LEFT retroperitoneum, presents in shock and carries 50% mortality. Screen with USG, confirm with CT angiography."),
    (S4, "Treat conservatively below 5.5 cm when asymptomatic; intervene at 5.5 cm or with symptoms. NICE puts open surgical repair first, keeping EVAR for high-risk patients or a hostile abdomen, while the European Society favours EVAR in the young. The EVAR stent graft anchors its body in the aorta and limbs in the iliacs, needs lifelong follow-up, and is contraindicated by difficult access or steeply angulated iliac vessels."),
    (S5, "Endoleaks are EVAR's signature complication: type I improper seal (m/c after thoracic repair), type II retrograde lumbar flow (m/c in AAA), type III direct graft leak, type IV porous graft, type V endotension."),
    (S6, "Open repair uses a Dacron or PTFE graft. To reach the aorta, do a Mattox left medial visceral rotation; to reach the IVC — as in RCC with IVC metastasis — do a Cattell-Braasch right medial visceral rotation; Kocherisation mobilises the duodenum."),
    (S7, "Cardiovascular complications are the m/c cause of death after aneurysm surgery. Watch for renal failure, aorto-duodenal fistula causing upper GI bleed (CT angiography is IOC), left-sided colonic ischaemia from the splenic flexure watershed presenting as bloody diarrhoea, and paraparesis from injury to the artery of Adamkiewicz feeding the anterior spinal artery. Mortality: 2-3% elective, 50% ruptured."),
    (S8, "Crawford types the thoraco-abdominal aneurysm: I left subclavian to renal artery, II (most extensive) left subclavian to aortic bifurcation, III mid descending aorta to bifurcation, IV upper abdominal to infra-renal aorta. Causes are atherosclerosis and Marfan's; pressure gives Ortner's syndrome (hoarseness from left recurrent laryngeal nerve), dysphagia and dyspnea. Screen with USG, IOC CT angiography, and graft repair when symptomatic or ≥5.5 cm."),
    (S9, "Dissection begins as an intimal tear creating a false lumen between intima and media, classically on the lateral wall of the ascending thoracic aorta — an aneurysm complication triggered by hypertension."),
    (S10, "Chest pain radiating to the back in a fifth-decade male, with unequal BP between the two arms or between arm and leg, is dissection until proved otherwise; hypotension and coronary insufficiency follow. CXR comes first (widened mediastinum, depressed left main bronchus), then CT angiography if stable or transesophageal echo if unstable."),
    (S11, "DeBakey I (m/c) takes ascending plus descending, II only ascending, III only descending; Stanford A covers DeBakey I and II, Stanford B is III. Start with a short-acting beta blocker (esmolol) or nicardipine for permissive hypotension, then thoracotomy with graft repair or EVAR for types I and II, and conservative follow-up for type III with surgery only if it progresses."),
    (S12, "Popliteal aneurysm is the m/c peripheral aneurysm and is bilateral in half of patients — swelling behind the knee, loss of contour, pain and emboli, imaged by duplex or CT angiography, repaired by graft or EVAR when symptomatic or >2 cm. Femoral aneurysms follow arterial puncture: thrombin injection under USG guidance below 3 cm, surgery above."),
    (S13, "Carotid aneurysm is atherosclerotic and usually presents as a TIA; duplex is the IOC. Carotid endarterectomy needs ≥70% stenosis plus ipsilateral amaurosis fugax or monocular blindness, contralateral facial paralysis, arm/leg paralysis, hemianopia or dysphasia."),
    (S14, "Thoracic outlet syndrome compresses subclavian vessels and brachial plexus — cervical rib, weak musculature or trauma. Arterial thrombus throws emboli and causes unilateral claudication; subclavian/axillary vein thrombosis (Paget-Schroetter) swells the arm; plexus compression hits the ulnar nerve most. Three tests: ADSON (arm abducted 30°, neck extended, head turned, deep breath → loss of ipsilateral radial pulse), EAST/ROOS (surrender position, open-close hand 3 min → pain, paresthesia, heaviness) and ULTT/ELVEY (positions 1 and 2 ipsilateral, position 3 contralateral)."),
    (S15, "CT angiography is the IOC and CXR hunts the cervical rib. Excise the rib and add physiotherapy for neurological symptoms, stent an arterial block, anticoagulate a venous one."),
    (S16, "Cirsoid aneurysm is a pulsatile swelling over the superficial temporal vessels, excised if symptomatic. A-V fistulae are abnormal artery-vein communications — most often iatrogenic Cimino radiocephalic fistulae for dialysis, preceded by a modified Allen's test for radio-ulnar patency (positive = palm reperfuses on ulnar release, negative = hand stays pale) — with traumatic and congenital (Parkes-Weber, Sturge-Weber) causes too."),
    (S17, "An A-V fistula is a pulsatile swelling; congenital ones cause high output cardiac failure and limb hypertrophy. Press the feeding vessel for the Nicoladoni/Branham sign: fistula size down, pulse rate down, systolic BP sharply up, bruit down. Image with MR angiography or DSA, and embolise — unless the patient is infected or an IV drug abuser, in which case excise surgically."),
    (S18, "CABG indications: left main >50%; three-vessel disease >70% with or without proximal LAD; two-vessel disease involving LAD plus another major artery; stenosis >70% with angina despite maximal medical therapy; and one-vessel disease >70% in a sudden cardiac death survivor with ischemia-related VT. Grafts: reversed great saphenous vein (m/c, complicated by saphenous nerve injury), LIMA to LAD, RIMA and the radial artery."),
]

first_page = {}
for x in Q:
    first_page.setdefault(x["sec"], x["page"])

UNITS = []
for i, (title, guide) in enumerate(UNIT_DEFS, 1):
    UNITS.append({
        "id": f"SURG-U64-{i}",
        "ch": 64,
        "n": i,
        "title": title,
        "sec": f"{title} · p{first_page[title]}",
        "qs": [x["id"] for x in Q if x["sec"] == title],
        "guide": guide,
    })

covered = [x for u in UNITS for x in u["qs"]]
assert covered == [x["id"] for x in Q]
assert len(set(covered)) == len(covered)
with open("data/ch64.json", "w", encoding="utf-8") as f:
    json.dump({"questions": Q, "units": UNITS}, f, ensure_ascii=False, indent=1)
print(f"ch64: {len(Q)} questions, {len(UNITS)} units")
