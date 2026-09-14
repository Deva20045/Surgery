#!/usr/bin/env python3
"""Build data/ch63.json — Arterial System : Part 1 (Marrow Surgery Ed 8, pp486-493)."""
import json

Q = []


def q(page, sec, text, correct, wrongs, note=None):
    opts = [correct] + list(wrongs)
    assert len(opts) == 4
    Q.append({
        "id": f"SURG-C63-{len(Q)+1:03d}",
        "sec": sec,
        "page": page,
        "q": text,
        "opts": opts,
        "ans": 0,
        "exp": (note or correct) + f" (Book p{page})",
    })


# ------------------------------------------------------------------ p486
S1 = "Acute Arterial Occlusion"
q(486, S1, "M/c cause of acute arterial occlusion:", "Embolus", ["Thrombus", "Trauma", "Vasospasm"])
q(486, S1, "M/c source of the embolus in acute arterial occlusion:", "Heart", ["Aorta", "Lower limb veins", "Carotid artery"])
q(486, S1, "Cardiac risk factors for acute arterial occlusion:", "H/o coronary artery disease and atrial fibrillation", ["H/o valve replacement only", "H/o pericarditis", "H/o myocarditis"])
q(486, S1, "Clinical features of acute arterial occlusion are remembered as:", "6 P's", ["4 P's", "5 P's", "3 P's"])
q(486, S1, "Which are LATE signs among the 6 P's:", "Paresis and pulselessness", ["Pain and pallor", "Paresthesia and poikilothermia", "Pain and pulselessness"])
q(486, S1, "'Poikilothermia' in the 6 P's refers to:", "Cold limbs", ["Fever", "Fluctuating BP", "Sweating"])
q(486, S1, "Earliest of the 6 P's to appear:", "Pain", ["Paresis", "Pulselessness", "Paralysis"])
q(486, S1, "IOC for acute arterial occlusion:", "Duplex scan (colour doppler + B mode USG)", ["CT angiography", "MRI", "Plain X-ray"])
q(486, S1, "Time window defining 'early presentation' in acute arterial occlusion:", "Within 6-8 hours", ["Within 24 hours", "Within 48 hours", "Within 1 hour"])
q(486, S1, "Options for a patient presenting early with acute arterial occlusion:", "Thrombolysis or embolectomy", ["Amputation", "Observation", "Compression bandaging"])
q(486, S1, "Contraindication to thrombolysis:", "Bleeding disorder", ["Atrial fibrillation", "Diabetes", "Hypertension"])
q(486, S1, "Embolectomy is performed using:", "Fogarty's balloon", ["Dormia basket", "Greenfield filter", "Amplatzer device"])
q(486, S1, "Management if the patient presents LATE with gangrene:", "Amputation", ["Thrombolysis", "Embolectomy", "Angioplasty"])
q(486, S1, "Angiographic appearance of an embolic occlusion:", "Sudden cut off with no collaterals", ["Gradual tapering with collaterals", "Corkscrew collaterals", "Aneurysmal dilatation"])
q(486, S1, "In Fogarty's balloon embolectomy, the balloon is:", "Dilated beyond the block and withdrawn", ["Left in situ permanently", "Inflated proximal to the block only", "Used to inject sclerosant"])

S2 = "Reperfusion Injury"
q(486, S2, "Metabolism occurring initially due to the arterial block:", "Anaerobic metabolism", ["Aerobic metabolism", "Ketogenesis", "Gluconeogenesis"])
q(486, S2, "Reperfusion injury follows:", "Thrombolysis / embolectomy restoring blood flow", ["Amputation", "Compression therapy", "Anticoagulation"])
q(486, S2, "Mechanism of reperfusion injury:", "Restoration of blood flow → generation of free radicals → free radical injury", ["Continued ischemia", "Bacterial infection", "Immune complex deposition"])

# ------------------------------------------------------------------ p487
S3 = "Compartment Syndrome"
q(487, S3, "Compartment syndrome after reperfusion is due to:", "Swelling of muscle", ["Bleeding into the joint", "Nerve transection", "Bone fracture"])
q(487, S3, "Compartment pressure defining compartment syndrome:", ">30 mmHg", [">10 mmHg", ">60 mmHg", ">100 mmHg"])
q(487, S3, "Clinical features of compartment syndrome:", "Pain / pain on passive flexion", ["Painless swelling", "Fever with chills", "Absent sensation only"])
q(487, S3, "Management of compartment syndrome:", "Fasciotomy", ["Amputation", "Anticoagulation", "Compression bandage"])

S4 = "Chronic Arterial Occlusion and Claudication"
q(487, S4, "Chronic arterial occlusion is secondary to:", "Thrombus", ["Embolus", "Vasospasm", "Trauma"])
q(487, S4, "Distal run off means:", "Structures distal to the block survive due to collaterals", ["Blood runs off into veins", "Distal tissue dies immediately", "Blood shunts into lymphatics"])
q(487, S4, "Mechanism of chronic arterial occlusion shown in the diagram:", "Gradual extension of thrombus with collateral formation", ["Sudden embolic cut off", "Arterial rupture", "Vasospasm"])
q(487, S4, "Intermittent claudication is:", "Cramping pain felt after walking a certain distance", ["Pain at rest relieved by walking", "Pain on first step", "Pain relieved by bending forwards"])
q(487, S4, "Distance after which claudication pain appears is called:", "Claudication distance", ["Ischemic distance", "Perfusion distance", "Rest distance"])
q(487, S4, "As the disease progresses, claudication distance:", "Decreases", ["Increases", "Remains constant", "Becomes infinite"])
q(487, S4, "Reason pain occurs on walking in chronic arterial occlusion:", "Increased demand for blood is not met due to arterial blockage", ["Venous congestion", "Nerve compression", "Muscle inflammation"])
q(487, S4, "Rest pain in chronic arterial occlusion is relieved by:", "Hanging the leg down from the bed at night", ["Elevating the leg", "Walking", "Applying ice"])
q(487, S4, "End-stage feature of chronic arterial occlusion:", "Gangrene", ["Varicose veins", "Lymphedema", "Cellulitis"])

S5 = "Differential Diagnosis of Claudication"
q(487, S5, "In intermittent claudication, pain is usually in a muscle group:", "One muscle group lower than the block", ["At the level of the block", "One group above the block", "Diffuse in the whole limb"])
q(487, S5, "Natural progression of intermittent claudication:", "Progresses to rest pain", ["Resolves spontaneously", "Progresses to varicose veins", "Progresses to DVT"])
q(487, S5, "Characteristic pain pattern of osteoarthritis:", "Maximum pain on the first step", ["Pain after a fixed walking distance", "Pain relieved by bending forwards", "Pain only at night"])
q(487, S5, "Site of pain in osteoarthritis:", "Pain in the affected joint", ["Pain in the calf muscle", "Pain in the buttock", "Pain in the sole"])
q(487, S5, "Neurogenic claudication is caused by:", "Lumbar canal stenosis", ["Aortoiliac block", "Femoral artery stenosis", "Osteoarthritis of knee"])
q(487, S5, "Pain in neurogenic claudication:", "Varies with posture and is relieved when the patient bends forwards", ["Is fixed regardless of posture", "Is relieved by standing erect", "Occurs only at rest"])

# ------------------------------------------------------------------ p488
S6 = "Boyd's Classification"
q(488, S6, "Boyd's class 1:", "Pain on walking but pain decreases as patient continues to walk", ["Pain on walking, continues to walk despite pain", "Pain forces patient to stop", "Pain at rest"])
q(488, S6, "Reason pain decreases in Boyd's class 1:", "Washout of substance P", ["Formation of collaterals", "Vasospasm relief", "Endorphin release only"])
q(488, S6, "Boyd's class 2:", "Pain on walking, continues to walk despite pain", ["Pain decreases as walking continues", "Pain forces patient to stop", "Pain at rest"])
q(488, S6, "Boyd's class 3:", "Pain forces the patient to stop", ["Pain decreases on walking", "Patient continues despite pain", "Pain at rest"])
q(488, S6, "Boyd's class 4:", "Pain at rest", ["Pain on walking only", "Pain relieved by walking", "No pain"])

S7 = "Symptoms According to Site of Arterial Disease"
q(488, S7, "Earliest claudication site in aortoiliac obstruction:", "Buttocks", ["Calves", "Thighs", "Feet"])
q(488, S7, "Pulses in aortoiliac obstruction:", "Femoral and distal pulses absent in both limbs", ["Unilaterally absent femoral pulse", "Only ankle pulses absent", "All pulses palpable"])
q(488, S7, "Bruit in aortoiliac obstruction is heard over the:", "Aortoiliac region", ["Popliteal fossa", "Femoral triangle only", "Carotid"])
q(488, S7, "Impotence with aortoiliac obstruction is known as:", "Leriche syndrome", ["Buerger's disease", "Subclavian steal syndrome", "May-Thurner syndrome"])
q(488, S7, "Claudication pattern in iliac obstruction:", "Unilateral claudication in the thigh and calf and sometimes the buttock", ["Bilateral buttock claudication", "Claudication in calf and foot only", "No claudication"])
q(488, S7, "Pulse finding in iliac obstruction:", "Unilateral absence of femoral and distal pulses", ["Bilateral absence of femoral pulses", "All pulses present", "Only ankle pulses absent"])
q(488, S7, "Claudication in femoropopliteal obstruction:", "Unilateral claudication in the calf", ["Bilateral buttock claudication", "Claudication in foot only", "Thigh and buttock claudication"])
q(488, S7, "Pulse findings in femoropopliteal obstruction:", "Femoral pulse palpable with absent unilateral distal pulses", ["Femoral pulse absent bilaterally", "All pulses absent", "All pulses present"])
q(488, S7, "Pulse findings in distal obstruction:", "Femoral and popliteal pulses palpable, ankle pulses absent", ["Femoral pulse absent", "Popliteal pulse absent", "All pulses absent"])
q(488, S7, "Claudication in distal obstruction:", "Claudication in calf and foot", ["Claudication in buttocks", "Claudication in thigh only", "No claudication"])
q(488, S7, "Bruit over the iliac region suggests:", "Iliac obstruction", ["Distal obstruction", "Femoropopliteal obstruction", "Carotid stenosis"])

S8 = "Arterial Ulcer and ABPI"
q(488, S8, "Type of ulcer complicating chronic arterial occlusion:", "Punched out ulcer", ["Sloping ulcer", "Everted ulcer", "Undermined ulcer"])
q(488, S8, "Features of an arterial ulcer include all EXCEPT:", "Dilated superficial veins", ["Loss of pulsation", "Loss of muscle mass", "Shiny skin/loss of hair"])
q(488, S8, "Sensations in an arterial ulcer:", "Intact", ["Absent", "Decreased", "Hyperesthetic"])
q(488, S8, "Skin changes over an arterial ulcer:", "Shiny skin with loss of hair", ["Hyperpigmented thick skin", "Excess hair growth", "Woody induration"])
q(488, S8, "IOC for chronic arterial occlusion:", "Duplex scan", ["ABPI", "DSA", "MRI"])
q(488, S8, "ABPI is calculated as:", "Maximum SBP at ankle / maximum SBP at brachial artery", ["Maximum SBP at brachial / maximum SBP at ankle", "Diastolic ankle / systolic brachial", "Mean arterial ankle / brachial"])
q(488, S8, "Normal ABPI:", "0.9 - 1.4", ["0.4 - 0.9", "1.4 - 2.0", "<0.4"])
q(488, S8, "ABPI < 0.9 indicates:", "Intermittent claudication", ["Normal limb", "Calcified vessels", "Venous disease"])
q(488, S8, "ABPI < 0.4 indicates:", "CTLI (chronic limb threatening ischemia)", ["Normal", "Intermittent claudication", "Diabetes"])
q(488, S8, "Features of CTLI:", "Ischemic rest pain +/- ulceration/gangrene", ["Claudication only", "Asymptomatic", "Painless swelling"])
q(488, S8, "CTLI requires:", "Urgent revascularization", ["Observation", "Compression stockings", "Elevation only"])

# ------------------------------------------------------------------ p489
S9 = "ABPI Interpretation, TBI and DSA"
q(489, S9, "A fall in ABPI of more than how much after exercise indicates arterial disease:", ">20%", [">5%", ">50%", ">80%"])
q(489, S9, "Patients with ABPI < 0.5 compared with those >0.5 are:", "Twice more likely to deteriorate", ["Equally likely to deteriorate", "Less likely to deteriorate", "Never deteriorate"])
q(489, S9, "A gradually decreasing ABPI is a sign of:", "Imminent limb loss", ["Recovery", "Venous disease", "Improved collaterals"])
q(489, S9, "Every 0.1 fall in ABPI increases risk of cardiac mortality by:", "10%", ["1%", "25%", "50%"])
q(489, S9, "ABPI > 1.4 is seen in all EXCEPT:", "Buerger's disease", ["Diabetes mellitus", "Calcified vessels", "Chronic renal failure"])
q(489, S9, "Principle behind the toe brachial pressure index (TBI):", "Digital arteries are more resistant to sclerosis", ["Toe arteries are larger", "Toe pressure equals brachial pressure", "Digital arteries calcify first"])
q(489, S9, "TBI + ABPI together are reliable for:", "Large vessel occlusions in diabetic patients", ["Venous reflux", "Lymphatic obstruction", "Carotid disease"])
q(489, S9, "TBI < 0.6 indicates:", "Significant arterial lesion", ["Normal perfusion", "Venous disease", "Calcified vessels"])
q(489, S9, "DSA provides:", "Dynamic arterial flow information", ["Static venous anatomy", "Tissue perfusion maps", "Bone detail"])
q(489, S9, "Potential complications of DSA include all EXCEPT:", "Gangrene of bowel", ["Bleeding", "Thrombosis", "Renal dysfunction"])
q(489, S9, "Vascular complications of DSA:", "Aneurysm and dissection", ["Osteomyelitis", "Cellulitis", "Neuropathy"])
q(489, S9, "Only indication for DSA:", "When intervention is planned", ["Routine screening", "Follow up of claudication", "Diagnosis of varicose veins"])

S10 = "Buerger's Disease versus Atherosclerosis"
q(489, S10, "Two major causes of chronic arterial occlusion:", "Buerger's disease and atherosclerosis", ["Raynaud's and Leriche", "Embolism and trauma", "Vasospasm and compression"])
q(489, S10, "Buerger's disease is also known as:", "Thromboangitis obliterans", ["Takayasu arteritis", "Giant cell arteritis", "Polyarteritis nodosa"])
q(489, S10, "Gender distribution of Buerger's disease:", "M >> F", ["F >> M", "M = F", "Only females"])
q(489, S10, "Gender distribution of atherosclerosis:", "M = F", ["M >> F", "F >> M", "Only males"])
q(489, S10, "Age of presentation of Buerger's disease:", "3rd - 4th decade", ["1st decade", "5th decade", "7th decade"])
q(489, S10, "Age of presentation of atherosclerosis:", "5th decade", ["2nd decade", "3rd decade", "8th decade"])
q(489, S10, "Sole risk factor for Buerger's disease:", "Smoking", ["Dyslipidemia", "Type A personality", "Alcohol"])
q(489, S10, "Risk factors for atherosclerosis:", "Stress, smoking, alcohol, type A personality, dyslipidemia", ["Smoking only", "Cold exposure", "Vibrating tools"])
q(489, S10, "Limb involvement in both Buerger's disease and atherosclerosis:", "LL > UL", ["UL > LL", "UL only", "Equal"])
q(489, S10, "Structures involved in Buerger's disease:", "Arteries (thrombosis), veins (thrombophlebitis) and nerves (neuropathy)", ["Arteries only", "Veins only", "Nerves only"])
q(489, S10, "Investigation that may be used for diagnosis in Buerger's disease:", "Muscle biopsy +/-", ["Bone scan", "Nerve conduction only", "Echocardiography"])
q(489, S10, "Structures involved in atherosclerosis:", "Arteries", ["Arteries, veins and nerves", "Veins only", "Lymphatics"])
q(489, S10, "Direction of spread in Buerger's disease:", "Distal to proximal", ["Proximal to distal", "Random", "Bilateral simultaneous"])
q(489, S10, "Direction of spread in atherosclerosis:", "Proximal to distal", ["Distal to proximal", "Random", "Centrifugal"])
q(489, S10, "Vessels involved in Buerger's disease:", "Small to medium", ["Medium to large", "Large only", "Capillaries only"])
q(489, S10, "Vessels involved in atherosclerosis:", "Medium to large", ["Small to medium", "Capillaries", "Venules"])

# ------------------------------------------------------------------ p490
S11 = "Management of Buerger's Disease"
q(490, S11, "Most important step in the management of Buerger's disease:", "Cessation of smoking", ["Lumbar sympathectomy", "Angioplasty", "Grafting"])
q(490, S11, "Mechanism of pentoxyphylline in Buerger's disease:", "↓ viscosity", ["↑ viscosity", "Vasoconstriction", "Anticoagulation"])
q(490, S11, "Type of amputation preferred in Buerger's disease:", "Conservative amputations", ["Above knee amputation always", "Hip disarticulation", "Hemipelvectomy"])
q(490, S11, "Lumbar sympathectomy in Buerger's disease is done to:", "↓ rest pain", ["↑ claudication distance", "Cure the disease", "Dissolve the thrombus"])
q(490, S11, "In bilateral lumbar sympathectomy, which ganglion is preserved on one side:", "L1 ganglion", ["L2 ganglion", "L3 ganglion", "L5 ganglion"])
q(490, S11, "L1 ganglion is preserved on one side to prevent:", "Impotence", ["Incontinence", "Paralysis", "Gangrene"])
q(490, S11, "Contralateral effect of lumbar sympathectomy:", "Intermittent claudication — cutaneous vasodilation precipitates rest pain", ["Improved claudication distance", "Complete cure", "Hyperhidrosis only"])
q(490, S11, "Reason angioplasty/grafting has no role in Buerger's disease:", "Absent distal target vessels and narrow vessels", ["Patients are too young", "Vessels are too large", "High bleeding risk"])
q(490, S11, "Angiographic hallmark of Buerger's disease:", "Corkscrew collaterals", ["Sudden cut off with no collaterals", "String of beads", "Aneurysmal dilatation"])

S12 = "Management of Atherosclerosis: Angioplasty and Grafting"
q(490, S12, "First step in management of atherosclerotic occlusion:", "Endovascular stenting (angioplasty)", ["Bypass graft", "Amputation", "Sympathectomy"])
q(490, S12, "If angioplasty fails or is contraindicated, next step:", "Bypass graft", ["Amputation", "Observation", "Sympathectomy"])
q(490, S12, "Duration for which the balloon is inflated in angioplasty:", "30 seconds and then deflated", ["3 seconds", "5 minutes", "30 minutes"])
q(490, S12, "Angioplasty is more successful for:", "Above knee > below knee vessels", ["Below knee > above knee vessels", "Digital vessels", "Aorta only"])
q(490, S12, "Complications of angioplasty include all EXCEPT:", "Impotence", ["Failure", "Hematoma", "Thrombosis"])
q(490, S12, "Indication for an aorto-bifemoral graft:", "Leriche syndrome (block at aortic bifurcation)", ["Iliac block alone", "Femoral block alone", "Distal calf block"])
q(490, S12, "Best material for an aorto-bifemoral graft:", "Dacron", ["PTFE", "Reversed saphenous vein", "Silicone"])
q(490, S12, "Graft used for an iliac block:", "Aorto-femoral grafting", ["Ilio-popliteal grafting", "Aorto-bifemoral grafting", "Femoro-tibial grafting"])
q(490, S12, "Graft used for a femoral block:", "Ilio-popliteal grafting", ["Aorto-femoral grafting", "Aorto-bifemoral grafting", "Carotid bypass"])
q(490, S12, "Best NATURAL material for an infra-inguinal graft:", "Reversed saphenous vein graft", ["Dacron", "PTFE", "Bovine pericardium"])
q(490, S12, "Best SYNTHETIC material for an infra-inguinal graft:", "PTFE graft", ["Dacron", "Silicone", "Nylon"])

# ------------------------------------------------------------------ p491
S13 = "Gangrene"
q(491, S13, "Definition of gangrene:", "Macroscopic and microscopic death of tissue", ["Microscopic death only", "Reversible ischemia", "Inflammation of tissue"])
q(491, S13, "Pathophysiology of dry gangrene:", "Tissue desiccation due to gradual slowing of blood", ["Venous blockade with super added infection", "Arterial embolism only", "Direct trauma"])
q(491, S13, "Pathophysiology of wet gangrene:", "Venous blockade / super added infection", ["Tissue desiccation", "Gradual slowing of arterial blood", "Vasospasm"])
q(491, S13, "Line of demarcation in dry gangrene:", "Good", ["Poor", "Absent", "Always proximal"])
q(491, S13, "If bone is involved in dry gangrene, the result is a:", "Conical stump", ["Flat stump", "Bulbous stump", "Skew stump"])
q(491, S13, "Line of demarcation in wet gangrene:", "Poor", ["Good", "Excellent", "Sharp"])
q(491, S13, "Why the line of demarcation is more proximal in wet gangrene:", "Infection spreads to neighbouring tissues", ["Blood supply improves distally", "Tissue desiccates", "Nerve supply intact"])
q(491, S13, "Line of demarcation is the:", "Junction between living and dead tissue", ["Edge of the ulcer", "Site of amputation only", "Site of infection"])
q(491, S13, "Line of demarcation is lined by:", "Granulation tissue", ["Fibrous scar", "Necrotic slough", "Epithelium"])
q(491, S13, "Sensory finding at the line of demarcation:", "Hyperaesthesia present", ["Complete anaesthesia", "Normal sensation", "Paraesthesia only"])

S14 = "Amputation: Indications and Levels"
q(491, S14, "Mnemonic for indications of amputation:", "Dead, deadly, damn nuisance", ["Pain, pallor, paralysis", "Hot, red, swollen", "Stasis, injury, coagulability"])
q(491, S14, "Gangrene falls under which category of amputation indication:", "Dead", ["Deadly", "Damn nuisance", "Elective"])
q(491, S14, "Gas gangrene and soft tissue sarcoma fall under:", "Deadly", ["Dead", "Damn nuisance", "Cosmetic"])
q(491, S14, "Contractures fall under which amputation indication:", "Damn nuisance", ["Dead", "Deadly", "Emergency"])
q(491, S14, "Local digit amputation is typically done in:", "Diabetic patients", ["Trauma patients only", "Sarcoma patients", "Burns patients"])
q(491, S14, "Ray excision is indicated when there is:", "MTP joint involvement", ["Only skin involvement", "Only nail involvement", "Knee involvement"])

# ------------------------------------------------------------------ p492
S15 = "Amputation Levels, Stump and Complications"
q(492, S15, "Transmetatarsal amputation is done when:", "Several toes are affected", ["Only one toe is affected", "The knee is involved", "The thigh is involved"])
q(492, S15, "Amputation giving the best chance of walking:", "Below knee amputation (preserves knee)", ["Above knee amputation", "Hip disarticulation", "Transmetatarsal amputation"])
q(492, S15, "Advantage of above knee amputation:", "Heals well", ["Best chance of walking", "Preserves the knee", "No phantom limb"])
q(492, S15, "Minimum stump length in below knee amputation:", "Not less than 8 cm below knee (10-12 cm)", ["Not less than 2 cm", "Not less than 20 cm", "Not less than 30 cm"])
q(492, S15, "M/c preferred flap in below knee amputation:", "Long posterior flap", ["Skew flap", "Anterior flap", "Medial flap"])
q(492, S15, "Anterior mark for the long posterior flap:", "10 cm below the tibial tuberosity", ["5 cm above the tibial tuberosity", "At the ankle", "At the knee joint line"])
q(492, S15, "Alternative flap to the long posterior flap:", "Skew flap", ["Rotation flap", "Free flap", "V-Y flap"])
q(492, S15, "Minimum stump length in above knee amputation:", "Not less than 20 cm", ["Not less than 8 cm", "Not less than 10 cm", "Not less than 30 cm"])
q(492, S15, "Early complications of amputation:", "Hemorrhage, infection, flap necrosis and DVT", ["Pain and phantom limb", "Contracture and arthritis", "Osteoporosis"])
q(492, S15, "Late complications of amputation:", "Pain and phantom limb", ["Hemorrhage and infection", "Flap necrosis", "DVT"])

S16 = "Raynaud's Phenomenon"
q(492, S16, "Raynaud's phenomenon is:", "Episodic vasospasm of digital vessels", ["Fixed occlusion of large arteries", "Venous thrombosis of digits", "Lymphatic obstruction"])
q(492, S16, "1st phase of Raynaud's phenomenon:", "Arterial + venous spasm — hands white", ["Artery relaxes + venous spasm — hands blue", "Arterial and venous relaxation — hands red", "Only venous spasm"])
q(492, S16, "2nd phase of Raynaud's phenomenon:", "Artery relaxes + venous spasm — hand blue and painful", ["Arterial and venous spasm — white hand", "Complete relaxation — red hand", "No colour change"])
q(492, S16, "3rd phase of Raynaud's phenomenon:", "Arterial + venous relaxation — hands red", ["Arterial and venous spasm — white", "Artery relaxes with venous spasm — blue", "Hands remain white"])
q(492, S16, "Painful phase of Raynaud's phenomenon:", "2nd phase (blue hand)", ["1st phase (white hand)", "3rd phase (red hand)", "All phases equally"])
q(492, S16, "Colour sequence in Raynaud's phenomenon:", "White → blue → red", ["Red → white → blue", "Blue → red → white", "White → red → blue"])

# ------------------------------------------------------------------ p493
S17 = "Primary versus Secondary Raynaud's"
q(493, S17, "Prevalence of primary Raynaud's compared with secondary:", "Primary is common, secondary is rare", ["Primary is rare, secondary is common", "Both equally common", "Both very rare"])
q(493, S17, "Association with autoimmune rheumatic disease (AIRD):", "Absent in primary, present in secondary", ["Present in primary, absent in secondary", "Present in both", "Absent in both"])
q(493, S17, "ANA association in Raynaud's:", "No in primary, generally yes in secondary", ["Yes in primary, no in secondary", "Yes in both", "No in both"])
q(493, S17, "Microangiopathy on periungueal capillaroscopy (PUC):", "Absent in primary, generally present in secondary", ["Present in primary only", "Present in both", "Absent in both"])
q(493, S17, "Family history of Raynaud's phenomenon:", "Present in primary, occasionally absent/no in secondary", ["Absent in primary, present in secondary", "Present in both", "Absent in both"])
q(493, S17, "Pharmacological treatment need:", "Occasionally in primary, frequently in secondary", ["Frequently in primary, occasionally in secondary", "Never in either", "Always in both"])
q(493, S17, "Complications in primary versus secondary Raynaud's:", "Rare in primary, present in secondary", ["Common in primary, rare in secondary", "Equal in both", "Absent in both"])
q(493, S17, "AIRD stands for:", "Autoimmune rheumatic disease", ["Arterial ischemic reperfusion disease", "Acute inflammatory rheumatic disorder", "Autoimmune Raynaud's induced disease"])
q(493, S17, "PUC stands for:", "Periungueal capillaroscopy", ["Peripheral ulcer classification", "Pulmonary ultrasound capillary", "Primary ulcer criteria"])
q(493, S17, "Primary Raynaud's is precipitated by:", "Cold, vibrating tools and heavy machinery", ["Heat and exercise", "Infection", "Drugs only"])
q(493, S17, "DOC for Raynaud's phenomenon:", "Calcium channel blockers (CCBs)", ["Beta blockers", "ACE inhibitors", "Diuretics"])

S18 = "Acrocyanosis and Subclavian Steal Syndrome"
q(493, S18, "Acrocyanosis is seen in:", "Females", ["Males", "Children only", "Elderly males"])
q(493, S18, "Pain in acrocyanosis:", "Painless", ["Severely painful", "Burning pain", "Colicky pain"])
q(493, S18, "Acrocyanosis is distinguished from Raynaud's because it is:", "Not episodic", ["Episodic", "Triphasic", "Always painful"])
q(493, S18, "Sequence in acrocyanosis:", "Mottled cyanosis followed by paraesthesia", ["White then blue then red", "Pallor followed by gangrene", "Redness followed by ulceration"])
q(493, S18, "Subclavian steal syndrome is stenosis in the:", "First part of the subclavian artery", ["Second part of the subclavian artery", "Third part of the subclavian artery", "Brachiocephalic artery"])
q(493, S18, "Etiology of subclavian steal syndrome:", "Thrombus and thoracic outlet obstruction", ["Embolus from the heart only", "Venous thrombosis", "Lymphatic obstruction"])
q(493, S18, "Pathophysiology of subclavian steal syndrome during exercise:", "Retrograde blood flow from basilar/vertebral artery", ["Antegrade increased flow to the brain", "Venous congestion of the arm", "Arterial rupture"])
q(493, S18, "Consequence of retrograde vertebral flow in subclavian steal syndrome:", "↓ perfusion of brain → syncopal attacks", ["↑ perfusion of brain", "Arm gangrene", "Stroke in all patients"])
q(493, S18, "Management of subclavian steal syndrome:", "Angioplasty", ["Amputation", "Sympathectomy", "Anticoagulation alone"])
q(493, S18, "Symptom that classically precipitates subclavian steal syndrome:", "Exercise of the arm", ["Rest", "Sleep", "Eating"])

UNIT_DEFS = [
    (S1, "Acute arterial occlusion is embolic, and the heart — especially in CAD and atrial fibrillation — is the m/c source. Remember the 6 P's: pain, pallor, paresis, pulselessness, paresthesia and poikilothermia, with paresis and pulselessness arriving late. Duplex scan is the IOC; within 6-8 hours choose thrombolysis (contraindicated in bleeding disorders) or Fogarty balloon embolectomy, while late gangrene means amputation. Angiography shows a sudden cut off with no collaterals."),
    (S2, "The blocked limb first runs anaerobic; once thrombolysis or embolectomy restores flow, free radicals are generated and injure the very tissue you saved — reperfusion injury."),
    (S3, "Muscle swells after reperfusion, and pressure above 30 mmHg is compartment syndrome: pain, especially on passive flexion. The answer is fasciotomy."),
    (S4, "Chronic occlusion is thrombotic and slow, so collaterals keep distal structures alive (distal run off). Intermittent claudication is cramping pain after a fixed claudication distance which shortens as disease progresses, because exercise demand outstrips a blocked artery. Rest pain relieved by hanging the leg out of bed, then gangrene, complete the story."),
    (S5, "Distinguish three limps: intermittent claudication (cramping after a set distance, one muscle group below the block, progresses to rest pain), osteoarthritis (maximum pain on the FIRST step, in the affected joint) and neurogenic claudication of lumbar canal stenosis (posture dependent, relieved by bending forwards)."),
    (S6, "Boyd grades claudication by behaviour: class 1 pain eases as the patient walks on (substance P washout), class 2 pain persists but the patient continues, class 3 pain forces a stop, class 4 pain at rest."),
    (S7, "Site dictates symptoms. Aortoiliac: earliest buttock claudication with thigh/calf pain, bilateral loss of femoral and distal pulses, aortoiliac bruit and impotence — Leriche syndrome. Iliac: unilateral thigh/calf (sometimes buttock) claudication, iliac bruit, unilateral pulse loss. Femoropopliteal: unilateral calf claudication with a palpable femoral but absent distal pulses. Distal: femoral and popliteal pulses present, ankle pulses gone, calf and foot claudication."),
    (S8, "The arterial ulcer is punched out with loss of pulsation and muscle mass, shiny hairless skin — but sensations are intact. Duplex is the IOC; ABPI (max ankle SBP ÷ max brachial SBP) reads 0.9-1.4 normal, <0.9 claudication and <0.4 chronic limb threatening ischemia with rest pain ± ulceration demanding urgent revascularization."),
    (S9, "ABPI subtleties: a >20% fall after exercise means arterial disease, <0.5 doubles the chance of deterioration, a steadily falling index warns of imminent limb loss, and every 0.1 drop adds 10% cardiac mortality — while >1.4 means falsely stiff vessels in diabetes, calcification or chronic renal failure. Digital arteries resist sclerosis, so TBI (significant if <0.6) plus ABPI is reliable in diabetics. DSA gives dynamic flow but risks bleeding, thrombosis, aneurysm, dissection and renal dysfunction, so it is done only when intervention is planned."),
    (S10, "Buerger's (thromboangitis obliterans) versus atherosclerosis: M>>F vs M=F; 3rd-4th decade vs 5th; smoking alone vs stress/smoking/alcohol/type A/dyslipidemia; both LL>UL; Buerger's hits arteries (thrombosis), veins (thrombophlebitis) and nerves (neuropathy) while atherosclerosis hits arteries alone; Buerger's spreads distal→proximal through small-to-medium vessels, atherosclerosis proximal→distal through medium-to-large ones."),
    (S11, "Stop the cigarettes — that is the treatment of Buerger's disease. Add pentoxyphylline to cut viscosity, conservative amputations and lumbar sympathectomy for rest pain, preserving the L1 ganglion on one side in bilateral cases to avoid impotence and remembering that contralateral cutaneous vasodilation can precipitate rest pain. Angioplasty and grafting fail because the distal target vessels are absent or too narrow; angiography shows corkscrew collaterals."),
    (S12, "For atherosclerosis, endovascular stenting comes first (balloon inflated 30 seconds, better above the knee than below, risking failure, hematoma, bleeding and thrombosis), with bypass grafting when it fails or is contraindicated. Leriche syndrome needs an aorto-bifemoral Dacron graft; infra-inguinal disease takes aorto-femoral grafting for an iliac block or ilio-popliteal for a femoral block, with a reversed saphenous vein the best natural and PTFE the best synthetic conduit."),
    (S13, "Gangrene is macroscopic and microscopic tissue death. Dry gangrene desiccates as flow slows, giving a good line of demarcation and a conical stump when bone is involved; wet gangrene follows venous blockade or superadded infection, so the line of demarcation is poor and creeps proximally. That line — living meets dead — is lined by granulation tissue and is hyperaesthetic."),
    (S14, "Indications for amputation follow 'dead, deadly, damn nuisance': gangrene (dead), gas gangrene and soft tissue sarcoma (deadly) and contractures (damn nuisance). Diabetic feet get local digit amputation, but MTP joint involvement calls for ray excision."),
    (S15, "Choose the level: transmetatarsal for several affected toes, below knee for the best chance of walking (it preserves the knee), above knee when healing matters most. A below knee stump must be at least 8 cm (ideally 10-12 cm), usually a long posterior flap marked 10 cm below the tibial tuberosity, or a skew flap; an above knee stump at least 20 cm. Early complications are hemorrhage, infection, flap necrosis and DVT; late ones are pain and phantom limb."),
    (S16, "Raynaud's is episodic vasospasm of the digital vessels in three phases: arterial plus venous spasm turns the hand WHITE, then the artery relaxes while the vein stays in spasm making it BLUE and painful, then everything relaxes and the hand goes RED."),
    (S17, "Primary Raynaud's is common, has no AIRD, no ANA, no PUC microangiopathy, a positive family history, rarely needs drugs and rarely complicates. Secondary Raynaud's inverts every one of those. Cold, vibrating tools and heavy machinery precipitate attacks; calcium channel blockers are the DOC."),
    (S18, "Acrocyanosis is the differential — female, painless, NOT episodic, with mottled cyanosis followed by paraesthesia. Subclavian steal syndrome is stenosis of the first part of the subclavian artery (thrombus or thoracic outlet obstruction): on arm exercise, blood flows retrogradely down the vertebral from the basilar, starving the brain and causing syncopal attacks. Treat with angioplasty."),
]

first_page = {}
for x in Q:
    first_page.setdefault(x["sec"], x["page"])

UNITS = []
for i, (title, guide) in enumerate(UNIT_DEFS, 1):
    UNITS.append({
        "id": f"SURG-U63-{i}",
        "ch": 63,
        "n": i,
        "title": title,
        "sec": f"{title} · p{first_page[title]}",
        "qs": [x["id"] for x in Q if x["sec"] == title],
        "guide": guide,
    })

covered = [x for u in UNITS for x in u["qs"]]
assert covered == [x["id"] for x in Q]
assert len(set(covered)) == len(covered)
with open("data/ch63.json", "w", encoding="utf-8") as f:
    json.dump({"questions": Q, "units": UNITS}, f, ensure_ascii=False, indent=1)
print(f"ch63: {len(Q)} questions, {len(UNITS)} units")
