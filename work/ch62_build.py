#!/usr/bin/env python3
"""Build data/ch62.json — Varicose Veins (Marrow Surgery Ed 8, pp476-485)."""
import json

Q = []


def q(page, sec, text, correct, wrongs, note=None):
    opts = [correct] + list(wrongs)
    assert len(opts) == 4
    Q.append({
        "id": f"SURG-C62-{len(Q)+1:03d}",
        "sec": sec,
        "page": page,
        "q": text,
        "opts": opts,
        "ans": 0,
        "exp": (note or correct) + f" (Book p{page})",
    })


# ------------------------------------------------------------------ p476
S1 = "Surgical Anatomy: Venous System and Deep Veins"
q(476, S1, "Percentage of lower limb blood carried by the superficial venous system:", "20%", ["50%", "80%", "100%"])
q(476, S1, "Percentage of lower limb blood carried by the deep venous system:", "80%", ["20%", "50%", "60%"])
q(476, S1, "Function of venous valves:", "Ensure unidirectional flow", ["Increase venous pressure", "Allow bidirectional flow", "Pump blood actively"])
q(476, S1, "Perforators are veins that:", "Connect the superficial to the deep venous system", ["Connect two arteries", "Connect lymphatics", "Drain the skin only"])
q(476, S1, "Direction of normal venous flow in the limb:", "Unidirectional — superficial to deep, distally to proximally", ["Deep to superficial", "Bidirectional", "Random"])
q(476, S1, "Deep veins labelled from above downwards in the diagram:", "Common femoral, superficial femoral, popliteal, then paired tibial/peroneal veins", ["Popliteal, common femoral, peroneal", "Great saphenous, short saphenous, popliteal", "Iliac, obturator, pudendal"])
q(476, S1, "Anterior tibial, posterior tibial and peroneal veins are:", "Paired", ["Single", "Triple", "Absent"])

S2 = "Great Saphenous Vein (GSV)"
q(476, S2, "Great saphenous vein arises from:", "Medial end of dorsal venous arch", ["Lateral end of dorsal venous arch", "Plantar venous arch only", "Popliteal vein"])
q(476, S2, "GSV passes at the knee along the:", "Medial aspect of knee", ["Lateral aspect of knee", "Posterior aspect of knee", "Anterior midline"])
q(476, S2, "GSV at the ankle lies:", "Just anterior to medial malleolus", ["Posterior to medial malleolus", "Anterior to lateral malleolus", "Over the tendo achilles"])
q(476, S2, "Site just anterior to the medial malleolus is the classic site of:", "Venous cut down", ["Arterial puncture", "Nerve block", "Skin grafting"])
q(476, S2, "GSV finally drains at the:", "Sapheno-femoral junction (SFJ)", ["Sapheno-popliteal junction", "Popliteal vein", "Profunda femoris"])
q(476, S2, "Surface marking of the SFJ:", "4 cm below and lateral to the pubic tubercle", ["4 cm above and medial to pubic tubercle", "2 cm below the inguinal ligament midpoint", "At the femoral head"])
q(476, S2, "Below the knee, GSV is closely associated with the:", "Saphenous nerve", ["Sural nerve", "Common peroneal nerve", "Tibial nerve"])
q(476, S2, "Nerve that may be injured while raising the GSV:", "Saphenous nerve", ["Sural nerve", "Femoral nerve", "Obturator nerve"])
q(476, S2, "GSV can be used as a graft in:", "Coronary artery bypass grafting (CABG)", ["Skin grafting", "Nerve grafting", "Bone grafting"])

# ------------------------------------------------------------------ p477
S3 = "GSV Tributaries, Short Saphenous Vein and Giacomini Vein"
q(477, S3, "Tributaries of the GSV labelled in the diagram include:", "Posteromedial thigh tributary and anterior (accessory) saphenous vein", ["Sural and peroneal veins", "Profunda femoris branches", "Perforating arteries"])
q(477, S3, "Vein labelled in the leg as a GSV tributary:", "Anterior tributary of leg", ["Small saphenous vein", "Giacomini vein", "Popliteal vein"])
q(477, S3, "Short saphenous vein (SSV) arises from:", "Lateral end of dorsal venous arch", ["Medial end of dorsal venous arch", "Plantar arch", "Popliteal vein"])
q(477, S3, "Course of the short saphenous vein:", "Goes posteriorly", ["Goes medially", "Goes anteriorly", "Goes laterally around the knee"])
q(477, S3, "Short saphenous vein drains into the:", "Sapheno-popliteal junction (SPJ)", ["Sapheno-femoral junction", "Femoral vein", "Anterior tibial vein"])
q(477, S3, "Why must the SPJ be radiologically marked before surgery:", "Its location is variable", ["It is very deep", "It is calcified", "It is absent in most patients"])
q(477, S3, "Nerve closely associated with the SSV all along its course:", "Sural nerve", ["Saphenous nerve", "Tibial nerve", "Femoral nerve"])
q(477, S3, "Because of sural nerve proximity, SSV surgery avoids:", "Stripping", ["Ligation", "Marking", "Anaesthesia"])
q(477, S3, "Giacomini vein is the:", "Cranial extension of the small saphenous vein connecting with the GSV", ["Perforator at the ankle", "Tributary of the femoral vein", "Deep calf vein"])
q(477, S3, "Clinical significance of the Giacomini vein:", "Cause of recurrence following surgery", ["Cause of DVT", "Site of ulceration", "Site of venous cut down"])

S4 = "Perforators"
q(477, S4, "Perforators connect:", "The superficial to the deep venous system", ["Artery to vein", "Two deep veins", "Lymphatic to vein"])
q(477, S4, "Total number of perforators in the lower limb:", "100-150", ["10-15", "50-60", "300-400"])
q(477, S4, "Thigh perforator is called:", "Hunterian perforator", ["Dodd's perforator", "Boyd's perforator", "Cockett's perforator"])
q(477, S4, "Perforator above the knee:", "Dodd's perforator", ["Boyd's perforator", "Hunterian perforator", "May/Kuster's perforator"])
q(477, S4, "Perforator below the knee:", "Boyd's perforator", ["Dodd's perforator", "Cockett's perforator", "Hunterian perforator"])
q(477, S4, "Perforators above the medial malleolus:", "Cockett's perforators", ["Boyd's perforator", "Dodd's perforator", "May/Kuster's perforator"])
q(477, S4, "Number and level of Cockett's perforators:", "Three — 5, 10 and 15 cm above the medial malleolus", ["Two — 5 and 10 cm", "Four — 2, 4, 6 and 8 cm", "One — at 10 cm"])
q(477, S4, "Perforator at the heel:", "May/Kuster's perforator", ["Cockett's perforator", "Boyd's perforator", "Hunterian perforator"])

# ------------------------------------------------------------------ p478
S5 = "Varicose Veins: Definition, Types and Risk Factors"
q(478, S5, "Definition of varicose veins:", "Dilated and tortuous veins with defective valves", ["Narrowed veins with normal valves", "Thrombosed deep veins", "Dilated arteries"])
q(478, S5, "Cause of PRIMARY varicose veins:", "Defective valves", ["Deep vein thrombosis", "Tumors", "Trauma"])
q(478, S5, "M/c type of varicose veins:", "Secondary", ["Primary", "Congenital", "Traumatic"])
q(478, S5, "Causes of SECONDARY varicose veins:", "Deep vein thrombosis and tumors", ["Defective valves alone", "Arterial disease", "Lymphatic obstruction"])
q(478, S5, "Occupational risk factor for varicose veins:", "Prolonged standing", ["Prolonged sitting with legs up", "Swimming", "Cycling"])
q(478, S5, "Sex predilection of varicose veins:", "Females > males", ["Males > females", "Equal", "Only males"])
q(478, S5, "Genetic risk factor for varicose veins:", "Family history", ["Blood group O", "HLA-B27", "Male gender"])
q(478, S5, "Physiological state increasing risk of varicose veins:", "Pregnancy", ["Menopause", "Puberty in males", "Lactation only"])

S6 = "Pathophysiology of Varicose Veins"
q(478, S6, "In normal physiology, blood in the limb veins is returned:", "Against gravity", ["With gravity", "By arterial pulsation only", "By lymphatics"])
q(478, S6, "Effect of inspiration on venous return:", "↓ intra thoracic pressure", ["↑ intra thoracic pressure", "No change", "↓ venous return"])
q(478, S6, "Role of surrounding muscle in venous return:", "Compression of surrounding muscle ↑ flow", ["Muscle compression ↓ flow", "Muscles have no role", "Muscles occlude deep veins"])
q(478, S6, "Normal effect of exercise on pressure in superficial veins:", "↓ pressure in superficial veins", ["↑ pressure in superficial veins", "No change", "Pressure becomes zero"])
q(478, S6, "Most acceptable theory of varicose vein pathology:", "Ambulatory venous hypertension — pressure in superficial veins ↑ on exercise", ["Arterial hypertension theory", "Lymphatic overload theory", "Infective theory"])

S7 = "Clinical Features and Vein Calibre"
q(478, S7, "Common presentations of varicose veins:", "Dilated veins, dull aching pain and pigmentation", ["Claudication and rest pain", "Fever and rigors", "Sudden pulseless limb"])
q(478, S7, "Diameter defining a varicose vein:", ">3 mm", ["1-3 mm", "≤1 mm", ">10 mm"])
q(478, S7, "Diameter of a reticular vein:", "1-3 mm", [">3 mm", "≤1 mm", ">5 mm"])
q(478, S7, "Diameter of dermal flares / thread veins:", "≤1 mm", ["1-3 mm", ">3 mm", ">5 mm"])
q(478, S7, "Type of pain in varicose veins:", "Dull, aching pain", ["Sharp lancinating pain", "Colicky pain", "Burning rest pain"])
q(478, S7, "Pigmentation in varicose veins is due to:", "Hemosiderin deposition", ["Melanin excess", "Bilirubin deposition", "Carotene deposition"])

# ------------------------------------------------------------------ p479
S8 = "Other Clinical Findings of Chronic Venous Disease"
q(479, S8, "Corona phlebectasia is also called:", "Malleolar flare", ["Gaiter flare", "Champagne sign", "Mickey mouse sign"])
q(479, S8, "Corona phlebectasia appearance:", "Fan shaped pattern of telangiectasia (<1 mm)", ["Single dilated vein >3 mm", "Depigmented patch", "Ulcer with sloping edge"])
q(479, S8, "Multiple veins in corona phlebectasia indicate:", "Early sign of advanced venous disease", ["Normal finding", "Arterial disease", "Lymphatic disease"])
q(479, S8, "Atrophic blanche is:", "Depigmented area surrounded by dilated veins", ["Pigmented patch with ulcer", "Fan of telangiectasia", "Woody induration of the calf"])
q(479, S8, "Atrophic blanche is a sign of:", "Advanced venous disease", ["Early venous disease", "Arterial insufficiency", "Diabetic neuropathy"])
q(479, S8, "Lipodermatosclerosis consists of:", "Contracture of tendo achilles + obliteration of fat + fibrosis", ["Ulceration + infection + gangrene", "Telangiectasia + pigmentation only", "Oedema + erythema alone"])
q(479, S8, "Appearance produced by lipodermatosclerosis:", "Inverted champagne bottle appearance", ["Bag of worms appearance", "Orange peel appearance", "Cauliflower appearance"])
q(479, S8, "Palpatory feel of lipodermatosclerosis:", "Woody feel", ["Boggy feel", "Fluctuant feel", "Crepitus"])
q(479, S8, "Venous ulceration commonly occurs over the:", "Medial malleolus — Gaiter's area", ["Lateral malleolus in all cases", "Dorsum of foot", "Great toe"])
q(479, S8, "Reticular veins seen clinically are:", "Veins of 1-3 mm diameter", ["Veins >3 mm", "Veins ≤1 mm", "Deep veins"])

# ------------------------------------------------------------------ p480
S9 = "CEAP Classification"
q(480, S9, "CEAP stands for:", "Clinical, etiological, anatomical, pathophysiological classification", ["Chronic edema and phlebitis", "Compression, elevation, ablation, prophylaxis", "Clinical evaluation of arterial pathology"])
q(480, S9, "CEAP class C0:", "No visible/palpable veins", ["Telangiectasias", "Varicose veins", "Edema"])
q(480, S9, "CEAP class C1:", "Telangiectasias / reticular veins", ["No visible veins", "Varicose veins", "Healed ulcer"])
q(480, S9, "CEAP class C2:", "Varicose veins", ["Reticular veins", "Edema", "Active ulcer"])
q(480, S9, "CEAP class C2r:", "Recurrent varicose veins", ["Reticular veins", "Recurrent ulcer", "Edema"])
q(480, S9, "CEAP class C3:", "Edema", ["Varicose veins", "Pigmentation", "Healed ulcer"])
q(480, S9, "CEAP class C4:", "Skin/subcutaneous tissue changes secondary to venous disease", ["Edema", "Healed ulcer", "Active ulcer"])
q(480, S9, "CEAP class C4a:", "Pigmentation / eczema", ["Lipodermatosclerosis", "Corona phlebectasia", "Healed ulcer"])
q(480, S9, "CEAP class C4b:", "Lipodermatosclerosis / atrophic blanche", ["Pigmentation/eczema", "Corona phlebectasia", "Active ulcer"])
q(480, S9, "CEAP class C4c:", "Corona phlebectasia", ["Pigmentation", "Lipodermatosclerosis", "Healed ulcer"])
q(480, S9, "CEAP class C5:", "Healed ulcer", ["Active venous ulcer", "Recurrent active ulcer", "Edema"])
q(480, S9, "CEAP class C6:", "Active venous ulcer", ["Healed ulcer", "Recurrent active venous ulcer", "Pigmentation"])
q(480, S9, "CEAP class C6r:", "Recurrent active venous ulcer", ["Healed ulcer", "Active venous ulcer", "Varicose veins"])
q(480, S9, "In case of multiple findings in CEAP:", "Highest grade is considered", ["Lowest grade is considered", "Average is taken", "Each is reported separately only"])
q(480, S9, "Etiological class Ec:", "Congenital", ["Primary", "Secondary", "No venous etiology identified"])
q(480, S9, "Etiological class Ep:", "Primary", ["Congenital", "Secondary", "None identified"])
q(480, S9, "Etiological class Es:", "Secondary (post-thrombotic)", ["Primary", "Congenital", "None identified"])
q(480, S9, "Etiological class En:", "No venous etiology identified", ["Congenital", "Primary", "Secondary"])
q(480, S9, "Anatomical class As:", "Superficial veins", ["Perforator vein", "Deep vein", "No venous location identified"])
q(480, S9, "Anatomical class Ap:", "Perforator vein", ["Superficial veins", "Deep vein", "None identified"])
q(480, S9, "Anatomical class Ad:", "Deep vein", ["Superficial vein", "Perforator", "None identified"])
q(480, S9, "Anatomical class An:", "No venous location identified", ["Deep vein", "Perforator", "Superficial vein"])
q(480, S9, "Pathophysiological class Pr:", "Reflux", ["Obstruction", "Reflux and obstruction", "No venous pathology"])
q(480, S9, "Pathophysiological class Po:", "Obstruction", ["Reflux", "Reflux and obstruction", "None identified"])
q(480, S9, "Pathophysiological class Pr/o:", "Reflux and obstruction", ["Reflux only", "Obstruction only", "None identified"])
q(480, S9, "Pathophysiological class Pn:", "No venous pathology identified", ["Reflux", "Obstruction", "Both"])

S10 = "Clinical Tests: Overview"
q(480, S10, "Tests used for SFJ incompetence:", "Trendelenburg test, Morrisey's cough impulse, Schwartz test", ["Modified Perthes test only", "Fegan's method only", "Allen's test"])
q(480, S10, "Tests used for perforator incompetence:", "Trendelenburg test, multiple tourniquet test, Fegan's method", ["Modified Perthes test", "Schwartz test", "Morrisey's cough impulse"])
q(480, S10, "Test used to detect DVT before varicose vein surgery:", "Modified Perthes test", ["Schwartz test", "Fegan's method", "Morrisey's cough impulse"])
q(480, S10, "Test appearing in BOTH the SFJ and perforator incompetence lists:", "Trendelenburg test", ["Schwartz test", "Fegan's method", "Modified Perthes test"])

# ------------------------------------------------------------------ p481
S11 = "Individual Clinical Tests"
q(481, S11, "In the Trendelenburg test, gradual filling from below indicates:", "Incompetent perforators", ["Incompetent SFJ", "DVT", "Normal veins"])
q(481, S11, "In the Trendelenburg test, rapid filling from above indicates:", "Incompetent SFJ", ["Incompetent perforators", "DVT", "Arterial insufficiency"])
q(481, S11, "Fegan's method involves:", "Feeling along the vein and marking blowouts", ["Tying multiple tourniquets", "Asking the patient to cough", "Walking with tourniquet"])
q(481, S11, "Blowouts marked in Fegan's method represent:", "Sites of incompetent perforators", ["Sites of DVT", "Sites of arterial stenosis", "Sites of ulceration"])
q(481, S11, "Morrisey's cough impulse test: a cough impulse felt at the SFJ means:", "Incompetence of SFJ", ["Perforator incompetence", "DVT", "Normal SFJ"])
q(481, S11, "Levels at which tourniquets are tied in the multiple tourniquet test:", "Above ankle, below knee, above knee and below SFJ", ["Only above the ankle", "Only below the SFJ", "Mid-thigh and groin only"])
q(481, S11, "Multiple tourniquet test is used to:", "Localize the sites of incompetent perforators", ["Rule out DVT", "Assess arterial supply", "Detect SFJ incompetence only"])
q(481, S11, "Purpose of the modified Perthes test:", "To rule out DVT (surgery is not done if deep veins are blocked)", ["To confirm SFJ incompetence", "To locate perforators", "To measure reflux time"])
q(481, S11, "Modified Perthes test technique:", "Tie tourniquet below SFJ and ask the patient to walk", ["Tie tourniquet at ankle and elevate limb", "Ask patient to cough", "Palpate along the vein"])
q(481, S11, "In the modified Perthes test, increased pain and swelling on walking means:", "DVT positive", ["DVT negative", "SFJ incompetence", "Perforator incompetence"])
q(481, S11, "In the modified Perthes test, decreased pain and swelling means:", "DVT negative", ["DVT positive", "Perforator incompetence", "Inconclusive"])

S12 = "Investigation: Doppler / Duplex Scan"
q(481, S12, "IOC for varicose veins:", "Doppler / duplex scan", ["MRI venography", "CT venography", "Plain X-ray"])
q(481, S12, "Doppler assesses all of the following EXCEPT:", "Bone density", ["Flow +/-", "Direction of flow", "Reflux"])
q(481, S12, "On colour Doppler, red colour indicates flow:", "Away from the heart", ["Towards the heart", "No flow", "Turbulent flow"])
q(481, S12, "On colour Doppler, blue colour indicates flow:", "Towards the heart", ["Away from the heart", "Absent flow", "Arterial flow"])
q(481, S12, "Definition of superficial vein reflux on Doppler:", "Retrograde flow lasting ≥0.5 sec", ["Retrograde flow lasting ≥5 sec", "Any retrograde flow", "Forward flow >1 sec"])
q(481, S12, "Mickey mouse sign on ultrasound is formed by:", "CFA, GSV and femoral vein", ["Popliteal artery, vein and SSV", "Three perforators", "Two saphenous veins and a nerve"])

S13 = "Adjunctive Management"
q(481, S13, "Class of compression garments used in varicose veins:", "Class III compression garments (25-35 mmHg)", ["Class I (10-15 mmHg)", "Class II (15-20 mmHg)", "Class IV (>60 mmHg)"])
q(481, S13, "Pressure delivered by class III compression garments:", "25-35 mmHg", ["10-15 mmHg", "15-20 mmHg", "40-50 mmHg"])
q(481, S13, "Main disadvantage of compression garments:", "Low compliance", ["High cost", "Skin cancer risk", "Causes DVT"])
q(481, S13, "In co-existing arterial disease (↓ABPI), compression garments should be used with:", "Reduced pressure", ["Increased pressure", "Same pressure", "Double layers"])
q(481, S13, "Horse chestnut seed extract is:", "Safe and efficacious in treating chronic venous hypertension", ["Contraindicated in venous disease", "Used only for arterial ulcers", "A sclerosant"])
q(481, S13, "Effect of horse chestnut seed extract:", "Improves symptoms and ↓ leg volume", ["Increases leg volume", "Causes thrombosis", "Dissolves clot"])

# ------------------------------------------------------------------ p482
S14 = "Surgical Management: Traditional Procedures"
q(482, S14, "Traditional procedure for GSV + SFJ incompetence:", "Trendelenburg procedure (flush ligation of SFJ)", ["Dodd and Cockett procedure", "SEPS", "Foam sclerotherapy"])
q(482, S14, "Traditional procedure for SSV + SPJ incompetence:", "Flush ligation of SPJ with SPJ marked before surgery and no stripping", ["Trendelenburg procedure", "SEPS", "Endovenous glue"])
q(482, S14, "Reason stripping is avoided in SSV surgery:", "Sural nerve injury", ["Saphenous nerve injury", "Femoral vein injury", "Poor cosmesis"])
q(482, S14, "Traditional procedures for perforator incompetence:", "Dodd & Cockett procedure and SEPS", ["Trendelenburg procedure and stripping", "EVLT and RFA", "Sclerotherapy"])
q(482, S14, "Dodd & Cockett procedure involves:", "Multiple sub-fascial ligation", ["Flush ligation of SFJ", "Laser ablation", "Glue injection"])
q(482, S14, "Treatment of choice (latest procedures) for varicose veins:", "Endovenous laser ablation therapy (EVLT) and radiofrequency ablation (RFA)", ["Trendelenburg procedure", "Dodd & Cockett procedure", "Compression stockings"])
q(482, S14, "Flush ligation means ligation:", "As close to the SFJ as possible", ["At the knee", "At the ankle", "At mid-thigh"])
q(482, S14, "Flush ligation prevents stump dilatation, which would otherwise cause:", "Saphena varix", ["Femoral hernia", "DVT", "Lymphocele"])
q(482, S14, "Tributaries are ligated during Trendelenburg procedure in order to:", "↓ recurrence", ["↑ venous return", "Prevent bleeding only", "Shorten operating time"])
q(482, S14, "First tributary ligated in the Trendelenburg procedure list:", "Superficial external pudendal", ["Superficial epigastric vein", "Deep external pudendal", "Superficial circumflex iliac vein"])
q(482, S14, "Medial tributaries ligated at the SFJ:", "Superficial and deep external pudendal veins", ["Superficial epigastric and circumflex iliac", "Accessory anterior saphenous and posterior medial thigh vein", "Giacomini vein"])
q(482, S14, "Distal tributaries ligated at the SFJ:", "Accessory anterior saphenous vein and posterior medial thigh vein", ["Superficial external pudendal and deep external pudendal", "Superficial epigastric and circumflex iliac", "Sural veins"])
q(482, S14, "Lateral tributaries ligated at the SFJ:", "Superficial epigastric vein and superficial circumflex iliac vein", ["External pudendal veins", "Accessory anterior saphenous vein", "Giacomini vein"])
q(482, S14, "Total number of tributaries listed for ligation in the Trendelenburg procedure:", "6", ["3", "4", "8"])
q(482, S14, "Venous stripping is:", "An additional procedure", ["The mainstay procedure", "Always contraindicated", "Done only in SSV surgery"])
q(482, S14, "Venous stripping is done only till the knee in order to:", "Prevent saphenous nerve injury", ["Prevent sural nerve injury", "Prevent femoral vein injury", "Save operating time"])

# ------------------------------------------------------------------ p483
S15 = "EVLT, RFA and Perforator Surgery"
q(483, S15, "Wavelength of the laser used in EVLT:", "1470 nm", ["810 nm", "532 nm", "2100 nm"])
q(483, S15, "Heat generated by the EVLT laser:", "60 J/cm", ["6 J/cm", "600 J/cm", "20 J/cm"])
q(483, S15, "Two types of lasers used in EVLT:", "Forward firing and lateral firing", ["Pulsed and continuous only", "Red and blue", "Cold and hot"])
q(483, S15, "Disadvantage of EVLT:", "Continuous pull-back required", ["Requires general anaesthesia always", "Causes DVT always", "High recurrence"])
q(483, S15, "EVLT catheter can be inserted into:", "Any vein — GSV/SSV/perforators", ["Only the GSV", "Only deep veins", "Only arteries"])
q(483, S15, "Steps of the EVLT procedure:", "Catheter insertion into vein → vein heats and collapses → catheter withdrawal closing vein", ["Glue injection → compression → ligation", "Ligation → stripping → suturing", "Sclerosant → foam → aspiration"])
q(483, S15, "Temperature and cycle used in radiofrequency ablation:", "120°C for a 20 second cycle", ["60°C for 60 seconds", "200°C for 5 seconds", "37°C for 20 minutes"])
q(483, S15, "Advantages of RFA over EVLT:", "Shorter learning curve and continuous pullback not required", ["Cheaper equipment only", "No anaesthesia needed", "No recurrence"])
q(483, S15, "Dodd and Cockett procedure involves ligation of the incompetent perforator at the:", "Sub-fascial level", ["Supra-fascial level", "Intradermal level", "Deep vein level"])
q(483, S15, "SEPS stands for:", "Sub-fascial endoscopic perforator surgery", ["Superficial endovenous perforator sclerotherapy", "Saphenous endoscopic partial stripping", "Subcutaneous endovenous plication surgery"])
q(483, S15, "Advantage of SEPS:", "Multiple perforator ligation with a single incision", ["No anaesthesia required", "Done percutaneously without incision", "Treats the SFJ"])

S16 = "Newer Modalities: Glue, Trivex and Foam Sclerotherapy"
q(483, S16, "Agent used in endovenous glue therapy:", "Cyanoacrylate glue", ["Fibrin glue", "Sodium tetradecyl sulphate", "Polidocanol"])
q(483, S16, "Mechanism of endovenous glue therapy:", "Collapses the dilated vein", ["Dissolves the clot", "Strips the vein", "Cools the vein"])
q(483, S16, "Trivex is:", "Transilluminated powered phlebectomy", ["Triple vein excision", "Transvenous endoscopy", "Thermal vein expansion"])
q(483, S16, "In Trivex, light is used sub-cutaneously to:", "Illuminate and identify the varicose vein", ["Ablate the vein by heat", "Sterilise the field", "Measure reflux"])
q(483, S16, "Current status of Trivex:", "Not done anymore", ["Treatment of choice", "First-line for perforators", "Used only in pregnancy"])
q(483, S16, "Foam sclerotherapy is also known as:", "Tessari technique", ["Trivex technique", "Dodd technique", "Fegan technique"])
q(483, S16, "Sclerosant-to-air ratio in foam sclerotherapy:", "1 : 3 (or 4)", ["3 : 1", "1 : 1", "1 : 10"])
q(483, S16, "M/c sclerosant used:", "Sodium tetradecyl sulphate", ["Polidocanol", "Ethanolamine oleate", "Sodium morrhuate"])
q(483, S16, "Sclerosants used in foam sclerotherapy include all EXCEPT:", "Cyanoacrylate", ["Sodium tetradecyl sulphate", "Polidocanol", "Sodium morrhuate"])
q(483, S16, "Vein size limit for foam sclerotherapy injection:", "<3 mm only", [">3 mm only", "Any size", ">5 mm"])
q(483, S16, "Veins treated by foam sclerotherapy:", "Reticular veins and thread veins", ["Deep veins", "Perforators only", "Arteries"])
q(483, S16, "Mechanism of foam sclerotherapy:", "Generates an inflammatory response which collapses the dilated vein", ["Freezes the vein", "Mechanically strips the vein", "Blocks the artery"])

# ------------------------------------------------------------------ p484
S17 = "Complications of Varicose Vein Surgery"
q(484, S17, "Wound infection after varicose vein surgery is:", "No longer the m/c complication — reduced by antibiotics", ["Still the m/c complication", "Never seen", "Treated with amputation"])
q(484, S17, "M/c complication of varicose vein surgery:", "Injury to nerves", ["Wound infection", "Bleeding", "Bruising"])
q(484, S17, "Recurrence after varicose vein surgery is more common with:", "SSV > GSV, as SPJ location is variable", ["GSV > SSV", "Perforator surgery only", "Equal in both"])
q(484, S17, "Nerve injured in GSV surgery and its incidence:", "Saphenous nerve (7%)", ["Sural nerve (7%)", "Common peroneal nerve (7%)", "Femoral nerve (7%)"])
q(484, S17, "Nerve injured in SSV surgery in 20% of cases:", "Sural nerve", ["Saphenous nerve", "Common peroneal nerve", "Tibial nerve"])
q(484, S17, "Incidence of common peroneal nerve injury in SSV surgery:", "4%", ["7%", "20%", "40%"])
q(484, S17, "Vascular complications of varicose vein surgery include:", "Bleeding and injury to vessels", ["Pulmonary fibrosis", "Renal failure", "Liver injury"])

S18 = "Complications of Varicose Veins"
q(484, S18, "Bleeding from varicose veins is reduced by:", "Limb elevation", ["Limb dependency", "Hot fomentation", "Massage"])
q(484, S18, "Calcification of veins presents as:", "Hard nodule", ["Soft fluctuant swelling", "Pulsatile mass", "Depigmented patch"])
q(484, S18, "Complications of varicose veins include all EXCEPT:", "Intermittent claudication", ["Superficial thrombophlebitis", "Pigmentation", "Ulceration"])
q(484, S18, "Malignant complication of long-standing varicose ulcer:", "Marjolin's ulcer", ["Basal cell carcinoma", "Melanoma", "Kaposi sarcoma"])
q(484, S18, "Skin sign of chronic venous disease listed among complications:", "Lipodermatosclerosis", ["Hypertrichosis", "Vitiligo", "Acanthosis nigricans"])

S19 = "Varicose / Venous Ulcer"
q(484, S19, "M/c site of a venous ulcer:", "Gaiter area — above the medial malleolus", ["Above the lateral malleolus", "Dorsum of foot", "Sole of foot"])
q(484, S19, "Venous ulcer above the LATERAL malleolus indicates:", "SSV involvement", ["GSV involvement", "Perforator involvement only", "Deep vein involvement"])
q(484, S19, "Depth of a venous ulcer:", "Shallow", ["Deep and punched out", "Undermined", "Penetrating to bone"])
q(484, S19, "Edges of a venous ulcer:", "Sloping edges", ["Punched out edges", "Everted edges", "Undermined edges"])
q(484, S19, "Granulation tissue in a venous ulcer:", "Pale granulation tissue", ["Healthy red granulation", "Absent floor", "Necrotic slough only"])
q(484, S19, "Margins of a venous ulcer are:", "Pigmented", ["Depigmented", "Everted", "Rolled out"])
q(484, S19, "Natural history of a venous ulcer:", "Non-healing", ["Heals within a week", "Self-limiting", "Heals with pigmentation only"])

# ------------------------------------------------------------------ p485
S20 = "Types of Lower Limb Ulcers"
q(485, S20, "Site of a venous ulcer:", "Gaiter area", ["Dorsum/lateral side", "Sole/base of great toe", "Heel"])
q(485, S20, "Site of an arterial ulcer:", "Dorsum / lateral side", ["Gaiter area", "Sole/base of great toe", "Medial malleolus"])
q(485, S20, "Site of a trophic ulcer:", "Sole / base of great toe", ["Gaiter area", "Dorsum of foot", "Lateral malleolus"])
q(485, S20, "Site of a diabetic ulcer:", "Sole / base of great toe", ["Gaiter area", "Dorsum/lateral side", "Popliteal fossa"])
q(485, S20, "Arterial pulsations in a venous ulcer:", "Normal", ["Absent", "Bounding", "Collapsing"])
q(485, S20, "Arterial pulsations in an arterial ulcer:", "Absent pulsations", ["Normal", "Bounding", "Exaggerated"])
q(485, S20, "Arterial pulsations in a trophic ulcer:", "Normal pulsations", ["Absent", "Bounding", "Variable"])
q(485, S20, "Arterial pulsations in a diabetic ulcer:", "May be absent", ["Always normal", "Always bounding", "Always present"])
q(485, S20, "Dilated veins are present in which ulcer type:", "Venous ulcer", ["Arterial ulcer", "Trophic ulcer", "Diabetic ulcer"])
q(485, S20, "Sensations in a venous ulcer:", "Normal", ["Decreased", "Absent", "Hyperesthetic"])
q(485, S20, "Arterial ulcers are characteristically:", "Painful", ["Painless", "Itchy", "Numb"])
q(485, S20, "Sensations in trophic and diabetic ulcers:", "Decreased sensations", ["Normal sensations", "Increased sensations", "Normal but painful"])
q(485, S20, "Margins of a venous ulcer:", "Sloping", ["Punched out", "Everted", "Undermined"])
q(485, S20, "Margins of arterial, trophic and diabetic ulcers:", "Punched out", ["Sloping", "Everted", "Rolled"])

S21 = "Management of Venous Ulcers and Marjolin's Ulcer"
q(485, S21, "Regime used for management of venous ulcers:", "Bisgaard regime", ["Bier's regime", "Buerger's regime", "Bassini regime"])
q(485, S21, "First component of the Bisgaard regime:", "Education", ["Surgery", "Pentoxyphylline", "Amputation"])
q(485, S21, "Elevation of the limb in the Bisgaard regime:", "↓ symptoms", ["↑ symptoms", "Has no effect", "Causes ulcer enlargement"])
q(485, S21, "Grade of elastic compression stockings used in the Bisgaard regime:", "Grade III", ["Grade I", "Grade II", "Grade IV"])
q(485, S21, "Dressing used in the Bisgaard regime:", "4 layer compression bandage", ["Single layer gauze", "Wet to dry dressing", "Alginate only"])
q(485, S21, "Mainstay of venous ulcer management:", "Surgery", ["Antibiotics", "Compression alone", "Pentoxyphylline"])
q(485, S21, "Only drug approved for venous ulcers:", "Pentoxyphylline", ["Aspirin", "Warfarin", "Heparin"])
q(485, S21, "Mechanism of pentoxyphylline:", "↑ microvascular perfusion", ["Dissolves clot", "Reduces INR", "Antibiotic action"])
q(485, S21, "Marjolin's ulcer arises from:", "Long-standing venous ulcers / burns undergoing malignant transformation", ["Acute wounds", "Arterial ulcers only", "Diabetic neuropathy"])
q(485, S21, "M/c histology of Marjolin's ulcer:", "Squamous cell carcinoma (SCC)", ["Basal cell carcinoma", "Melanoma", "Adenocarcinoma"])
q(485, S21, "Edges of Marjolin's ulcer:", "Raised and everted (cauliflower-like)", ["Sloping", "Punched out", "Undermined"])
q(485, S21, "Management of Marjolin's ulcer:", "Wide local excision, no radiotherapy", ["Radiotherapy alone", "Chemotherapy alone", "Compression bandaging"])
q(485, S21, "Radiotherapy is avoided in Marjolin's ulcer because of:", "Increased recurrence noted", ["Skin toxicity only", "Cost", "Lack of equipment"])

S22 = "Associated Syndromes"
q(485, S22, "Klippel-Trenaunay syndrome is a:", "Mesodermal abnormality, non-familial syndrome", ["Ectodermal familial syndrome", "Endodermal syndrome", "Autosomal dominant disorder"])
q(485, S22, "Pathophysiology of Klippel-Trenaunay syndrome:", "Vestigeal deep veins → blood shunted to superficial system → varicose veins", ["Arterial fistulae → high output failure", "Lymphatic aplasia → lymphedema", "Valve destruction by thrombosis"])
q(485, S22, "Clinical features of Klippel-Trenaunay syndrome:", "Absent deep veins, cutaneous naevus, soft tissue and bone hypertrophy", ["Multiple A-V fistulae with cardiac failure", "Absent superficial veins", "Skin depigmentation"])
q(485, S22, "Management of Klippel-Trenaunay syndrome:", "No surgery", ["Trendelenburg procedure", "EVLT", "Stripping of GSV"])
q(485, S22, "Reason surgery is avoided in Klippel-Trenaunay syndrome:", "Deep veins are absent — superficial veins are the only drainage", ["Bleeding risk is too high", "Patients are too young", "Recurrence is certain"])
q(485, S22, "Feature of Parkes-Weber syndrome:", "Multiple A-V fistulae → high output cardiac failure", ["Absent deep veins", "Vestigeal superficial veins", "Lymphatic hypoplasia"])
q(485, S22, "Parkes-Weber syndrome is a differential for:", "Klippel-Trenaunay syndrome", ["Marjolin's ulcer", "Paget-Schroetter disease", "May-Thurner syndrome"])
q(485, S22, "Shared feature of Klippel-Trenaunay and Parkes-Weber syndromes:", "Limb hypertrophy", ["A-V fistulae", "Absent deep veins", "Cardiac failure"])

UNIT_DEFS = [
    (S1, "The limb drains through two systems joined by perforators: superficial (20%) and deep (80%), with valves enforcing one-way flow. The deep column runs common femoral → superficial femoral → popliteal → paired anterior tibial, posterior tibial and peroneal veins."),
    (S2, "The great saphenous vein starts at the MEDIAL end of the dorsal venous arch, runs just anterior to the medial malleolus (classic venous cut-down site), passes the medial knee and ends at the sapheno-femoral junction 4 cm below and lateral to the pubic tubercle. Below the knee it hugs the saphenous nerve — injured when the vein is harvested for CABG."),
    (S3, "GSV tributaries include the posteromedial thigh tributary, the anterior (accessory) saphenous vein and the anterior tributary of the leg. The short saphenous vein rises from the LATERAL dorsal arch, runs posteriorly and ends at the variable sapheno-popliteal junction — radiologically marked before surgery, never stripped because the sural nerve travels with it. The Giacomini vein, the cranial extension of the SSV connecting to the GSV, is a classic cause of post-operative recurrence."),
    (S4, "100-150 perforators link superficial to deep. Learn them head to toe: Hunterian in the thigh, Dodd's above the knee, Boyd's below the knee, three Cockett's perforators 5, 10 and 15 cm above the medial malleolus, and May/Kuster's at the heel."),
    (S5, "Varicose veins are dilated tortuous veins with defective valves — primary from valve failure, secondary (m/c) from DVT or tumours. Prolonged standing, female sex, family history and pregnancy stack the odds."),
    (S6, "Normally blood climbs against gravity helped by falling intra-thoracic pressure on inspiration, muscle compression and a FALL in superficial vein pressure with exercise. When exercise instead RAISES superficial pressure, ambulatory venous hypertension — the most acceptable theory — produces varicosities."),
    (S7, "Patients present with dilated veins, dull aching pain and hemosiderin pigmentation. Calibre defines the label: varicose vein >3 mm, reticular vein 1-3 mm, dermal flares/thread veins ≤1 mm."),
    (S8, "Advanced venous disease announces itself in the skin: corona phlebectasia (malleolar flare — fan of <1 mm telangiectasia, an early sign), atrophic blanche (depigmented area ringed by dilated veins), lipodermatosclerosis (tendo achilles contracture + fat obliteration + fibrosis giving an inverted champagne bottle leg with a woody feel), and ulceration over the medial malleolus in Gaiter's area."),
    (S9, "CEAP: C0 no veins, C1 telangiectasia/reticular, C2 varicose (C2r recurrent), C3 edema, C4 skin changes (a pigmentation/eczema, b lipodermatosclerosis/atrophic blanche, c corona phlebectasia), C5 healed ulcer, C6 active ulcer (C6r recurrent) — always record the highest grade. E = congenital/primary/secondary(post-thrombotic)/none; A = superficial/perforator/deep/none; P = reflux/obstruction/both/none."),
    (S10, "Sort the bedside tests by what they hunt: SFJ incompetence (Trendelenburg, Morrisey's cough impulse, Schwartz), perforator incompetence (Trendelenburg, multiple tourniquet, Fegan's) and DVT (modified Perthes). Trendelenburg straddles the first two lists."),
    (S11, "Trendelenburg: gradual filling from below = incompetent perforators; rapid filling from above = incompetent SFJ. Fegan's marks blowouts, Morrisey's cough impulse at the SFJ confirms SFJ incompetence, and multiple tourniquets (above ankle, below knee, above knee, below SFJ) localise perforators. Modified Perthes rules out DVT — walk with a tourniquet below the SFJ and see whether pain and swelling rise (DVT +) or fall (DVT −)."),
    (S12, "Doppler/duplex is the IOC: it shows flow, direction (red away from heart, blue towards) and reflux, defined as retrograde superficial flow lasting ≥0.5 sec. The CFA, GSV and femoral vein together make the Mickey mouse sign."),
    (S13, "Adjunctive care means class III compression garments (25-35 mmHg) — limited by poor compliance, and pressure must be reduced if ABPI is low from arterial disease. Horse chestnut seed extract is safe and efficacious in chronic venous hypertension, improving symptoms and reducing leg volume."),
    (S14, "Traditional surgery is tailored: Trendelenburg flush ligation for GSV+SFJ, flush ligation of the pre-marked SPJ without stripping for SSV, and Dodd & Cockett or SEPS for perforators — while EVLT and RFA are now the treatment of choice. Flush ligation as close to the SFJ as possible prevents a stump saphena varix, and six tributaries are ligated to cut recurrence: superficial and deep external pudendal (medial), accessory anterior saphenous and posterior medial thigh (distal), superficial epigastric and superficial circumflex iliac (lateral). Stripping is additional and stops at the knee to spare the saphenous nerve."),
    (S15, "EVLT uses a 1470 nm laser generating 60 J/cm through forward or lateral firing fibres — the catheter heats and collapses the vein, but continuous pull-back is needed. RFA delivers 120°C in 20 second cycles with a shorter learning curve and no continuous pullback. For perforators, Dodd & Cockett does open sub-fascial ligation while SEPS ligates multiple perforators through a single incision."),
    (S16, "Newer options: endovenous cyanoacrylate glue collapses the vein; Trivex (transilluminated powered phlebectomy) is no longer done; and foam sclerotherapy — the Tessari technique, sclerosant-to-air 1:3 or 1:4 — injects reticular and thread veins <3 mm. Sodium tetradecyl sulphate is the m/c sclerosant, with polidocanol, ethanolamine oleate and sodium morrhuate as alternatives, all working by inflammatory collapse of the vein."),
    (S17, "Nerve injury is now the m/c complication of varicose vein surgery — saphenous nerve in 7% of GSV cases, sural nerve in 20% and common peroneal in 4% of SSV cases. Wound infection has fallen with antibiotics; bruising, bleeding, vessel injury and recurrence (SSV > GSV, because the SPJ wanders) complete the list."),
    (S18, "Varicose veins complicate into bleeding (controlled by limb elevation), calcification with a hard nodule, superficial thrombophlebitis, pigmentation, lipodermatosclerosis, ulceration and, eventually, Marjolin's ulcer."),
    (S19, "The venous ulcer sits in the gaiter area above the medial malleolus — or above the lateral malleolus when the SSV is involved. It is shallow with sloping edges, pale granulation tissue, pigmented margins, and it does not heal."),
    (S20, "Learn the four-column ulcer table: venous (gaiter area, normal pulsations, dilated veins, normal sensation, sloping margin); arterial (dorsum/lateral side, absent pulsations, painful, punched out); trophic (sole/base of great toe, normal pulsations, ↓sensation, punched out); diabetic (sole/base of great toe, pulsations may be absent, ↓sensation, punched out)."),
    (S21, "The Bisgaard regime: education, elevation, grade III elastic compression stockings, a 4-layer compression bandage, with surgery as the mainstay and pentoxyphylline the only approved drug (it raises microvascular perfusion). A long-standing ulcer or burn scar that turns cauliflower-like with raised everted edges is Marjolin's ulcer — usually SCC, treated by wide local excision, no radiotherapy because recurrence rises."),
    (S22, "Klippel-Trenaunay: a non-familial mesodermal abnormality with vestigeal deep veins shunting blood into the superficial system — absent deep veins, cutaneous naevus, soft tissue and bone hypertrophy, and absolutely no surgery. Parkes-Weber is its differential, driven by multiple A-V fistulae causing high output cardiac failure, also with limb hypertrophy."),
]

first_page = {}
for x in Q:
    first_page.setdefault(x["sec"], x["page"])

UNITS = []
for i, (title, guide) in enumerate(UNIT_DEFS, 1):
    UNITS.append({
        "id": f"SURG-U62-{i}",
        "ch": 62,
        "n": i,
        "title": title,
        "sec": f"{title} · p{first_page[title]}",
        "qs": [x["id"] for x in Q if x["sec"] == title],
        "guide": guide,
    })

covered = [x for u in UNITS for x in u["qs"]]
assert covered == [x["id"] for x in Q]
assert len(set(covered)) == len(covered)
with open("data/ch62.json", "w", encoding="utf-8") as f:
    json.dump({"questions": Q, "units": UNITS}, f, ensure_ascii=False, indent=1)
print(f"ch62: {len(Q)} questions, {len(UNITS)} units")
