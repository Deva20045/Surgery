#!/usr/bin/env python3
"""Build data/ch57.json — Head Trauma (Marrow Surgery Ed 8, pp435-443)."""
import json

Q = []

def q(page, sec, text, correct, wrongs, note=None):
    opts = [correct] + list(wrongs)
    assert len(opts) == 4
    Q.append({
        "id": f"SURG-C57-{len(Q)+1:03d}",
        "sec": sec,
        "page": page,
        "q": text,
        "opts": opts,
        "ans": 0,
        "exp": (note or correct) + f" (Book p{page})",
    })

# ------------------------------------------------------------------ p435
S1 = "Anatomy of Scalp (SCALP) and Scalp Laceration"
q(435, S1, "The mnemonic for layers of the scalp is:", "SCALP", ["SCALD", "SCARF", "PLACS"])
q(435, S1, "In the SCALP mnemonic, 'A' stands for:", "Aponeurosis", ["Arachnoid", "Arteries", "Areolar tissue"])
q(435, S1, "The 4th layer of the scalp is:", "Loose areolar tissue", ["Aponeurosis", "Periosteum", "Connective tissue"])
q(435, S1, "The 5th layer of the scalp is:", "Periosteum", ["Loose areolar tissue", "Skin", "Dura"])
q(435, S1, "In scalp laceration, blood vessels cannot vasoconstrict because they are:", "Adherent to fibrous septa", ["In spasm", "Inside the aponeurosis", "Surrounded by bone"])
q(435, S1, "The result of vessel-septa adherence in scalp laceration is:", "↑Bleeding", ["No bleeding", "Delayed bleeding", "Thrombosis"])
q(435, S1, "EMERGENCY mx of scalp laceration is:", "Apply pressure", ["Ligature the vessel", "Apply ice", "Head elevation"])
q(435, S1, "DEFINITIVE mx of scalp laceration is:", "Suturing the laceration", ["Pressure dressing", "Staples only", "Flap coverage"])
q(435, S1, "Needle rule for scalp suturing:", "No 1/1-0/2-0 suture", ["Only 1-0 suture", "Only round body needle", "Only 4-0 suture"])
q(435, S1, "Needle TYPE preferred for scalp suturing:", "Cutting / reverse cutting", ["Round body", "Blunt", "Taper cut only"])
q(435, S1, "Bleeding below the aponeurotic layer of scalp leads to:", "Black eye", ["Cavernous sinus thrombosis", "Meningitis", "Battle sign"])
q(435, S1, "Infection from the dangerous area of face spreads via loose areolar tissue through:", "Emissary veins", ["Lymphatics", "Nerve sheaths", "Arterial supply"])
q(435, S1, "Retrograde spread of facial infection via emissary veins causes:", "Cavernous sinus thrombosis", ["Sagittal sinus thrombosis", "Brain abscess only", "Meningitis only"])
q(435, S1, "The 'dangerous area of face' shown corresponds to the triangle covering:", "Upper lip and nose (medial canthus to upper lip)", ["Forehead", "Chin", "Temple"])

# ------------------------------------------------------------------ p435-436
S2 = "Skull Fractures: Depressed vs Non-Depressed"
q(435, S2, "Non-depressed skull fracture is managed:", "Conservatively", ["Surgically always", "With steroids", "With antibiotics"])
q(435, S2, "Ix of depressed skull fracture is:", "NCCT (IOC)", ["MRI", "X-ray skull", "Contrast CT"])
q(436, S2, "Mx of depressed skull fracture is surgical elevation & fixation only if:", "Focal neurological signs (+) OR depression > adjacent skull thickness", ["Any fracture seen", "Patient demands", "Cosmesis alone"])
q(436, S2, "IOC for head injuries overall:", "NCCT", ["MRI", "X-ray skull AP/Lat", "PET"])
q(436, S2, "Depression exceeding which structure mandates surgery (without focal signs)?", "Adjacent skull thickness", ["2 cm depth", "Dural thickness", "Scalp thickness"])

# ------------------------------------------------------------------ p436-437
S3 = "Base of Skull Fractures: Anterior / Middle / Posterior Fossa"
q(436, S3, "ANTERIOR cranial fossa fracture involves the:", "Cribriform plate", ["Petrous temporal", "Occipital bone", "Sphenoid wing"])
q(436, S3, "MIDDLE cranial fossa fracture involves the:", "Petrous part of temporal bone", ["Cribriform plate", "Occipital bone", "Frontal sinus"])
q(436, S3, "POSTERIOR cranial fossa fracture involves the:", "Occipital bone", ["Cribriform plate", "Petrous temporal", "Zygoma"])
q(436, S3, "Raccoon eyes (B/L black eye) suggest:", "Anterior fossa fracture", ["Middle fossa fracture", "Posterior fossa fracture", "Nasal fracture only"])
q(436, S3, "In raccoon eyes the posterior/superior border of subconjunctival hemorrhage:", "Cannot be seen", ["Is sharply seen", "Is absent", "Is calcified"])
q(436, S3, "A visible posterior/superior border of subconjunctival hemorrhage indicates:", "Direct trauma to the eye", ["Basal skull fracture", "Cavernous sinus thrombosis", "Orbital cellulitis"])
q(436, S3, "CSF rhinorrhoea is confirmed by:", "Target/Halo sign (+) & β2 transferrin", ["β2 microglobulin", "Glucose only", "Target sign (–)"])
q(436, S3, "Target/Halo sign & β2 transferrin differentiate CSF leak from:", "Epistaxis", ["Lacrimation", "Saliva", "Serous otitis"])
q(436, S3, "Along with CSF rhinorrhoea, anterior fossa fracture features include:", "Epistaxis, anosmia & frontal lobe contusion", ["Hemotympanum & otorrhea", "Battle sign & VI nerve palsy", "Vernet syndrome"])
q(436, S3, "Anosmia in anterior fossa fracture is due to:", "Cribriform plate fracture (olfactory fibers)", ["Occipital injury", "Facial nerve injury", "Petrous fracture"])
q(436, S3, "Battle sign — discoloration over the mastoid process — appears:", "24-48 hrs after fracture", ["Immediately", "After 1 week", "After 1 month"])
q(436, S3, "Battle sign indicates:", "Middle cranial fossa (petrous temporal) fracture", ["Anterior fossa fracture", "Frontal contusion", "Nasal fracture"])
q(436, S3, "Middle fossa fracture features (ear):", "Hemotympanum & CSF otorrhea", ["Rhinorrhoea & anosmia", "Raccoon eyes", "Visual problems"])
q(436, S3, "Middle fossa (petrous) fracture commonly injures which nerve?", "Facial nerve", ["VI nerve", "IX-XI nerves", "II nerve"])
q(436, S3, "PARADOXICAL rhinorrhoea (rare) pathway in petrous fracture:", "Middle ear → CSF into Eustachian tube → nose", ["Nose → Eustachian tube → ear", "Mouth → ear", "Sinus → orbit"])
q(436, S3, "Temporal lobe contusions accompany:", "Middle fossa fracture", ["Anterior fossa fracture", "Posterior fossa fracture", "Depressed vault fracture"])
q(436, S3, "POSTERIOR fossa fracture features include:", "Visual problems, occipital contusion & VIth nerve injury", ["Raccoon eyes", "Battle sign", "CSF otorrhea"])
q(436, S3, "Vernet syndrome / Jugular foramen syndrome (rare) is:", "IX-XIth cranial nerve injury", ["VI nerve palsy", "II nerve injury", "VII-VIII injury"])
q(437, S3, "The clinical photo of discoloration over the mastoid region is labelled:", "Battle sign", ["Raccoon eyes", "Target/halo sign", "Halo vest"])
q(436, S3, "Ix of base of skull fractures:", "NCCT (IOC)", ["MRI", "Skull X-ray", "Angiography"])
q(436, S3, "Base of skull fractures are treated as:", "Open fractures", ["Closed fractures", "No treatment", "Only observation"])
q(436, S3, "Prophylactic antibiotic of choice in base of skull fracture:", "3rd generation cephalosporin (to prevent meningitis)", ["Penicillin G", "Metronidazole only", "Vancomycin"])
q(436, S3, "Nose/ear is NOT packed in CSF leak because packing:", "Aids growth of bacteria via anaerobic conditions", ["Stops CSF flow", "Causes bleeding", "Blocks the sinus"])

# ------------------------------------------------------------------ p437
S4 = "NICE Guidelines for Head Injury"
q(437, S4, "NICE head injury guidelines require ruling out which injury in ALL patients?", "Cervical spine injury", ["Thoracic injury", "Pelvic injury", "Facial fracture"])
q(437, S4, "GCS monitoring in the FIRST 2 hours is done every:", "1/2 hour", ["1 hour", "2 hours", "4 hours"])
q(437, S4, "GCS monitoring in the NEXT 4 hours is done every:", "1 hour", ["1/2 hour", "2 hours", "6 hours"])
q(437, S4, "After 6 hours, GCS monitoring is done every:", "2 hours", ["1/2 hour", "1 hour", "6 hours"])
q(437, S4, "Adult CT within 1 HOUR indication (GCS):", "GCS <13 at any point", ["GCS <15 at any time", "GCS ≤8 only", "GCS 13 at 8 hours"])
q(437, S4, "Adult CT within 1 hour: GCS <15 at:", "2 hours", ["30 mins", "4 hours", "8 hours"])
q(437, S4, "More than ONE episode of vomiting after head injury in adults warrants CT:", "Within 1 hour", ["Within 8 hours", "Within 24 hours", "Never"])
q(437, S4, "Which seizure type mandates CT within 1 hour in adults?", "Post-traumatic seizure", ["Febrile seizure", "Alcohol withdrawal seizure", "Epileptic absence"])
q(437, S4, "Adult CT within 8 HOURS indications:", "Age >65 yrs & retrograde amnesia >30 mins", ["Age >40 yrs & amnesia >10 min", "Age >65 yrs only", "Any age with vomiting"])
q(437, S4, "In adults, suspected open/depressed/basal skull fracture needs CT:", "Within 1 hour", ["Within 8 hours", "Within 24 hours", "Only if GCS falls"])
q(437, S4, "In CHILDREN, head injury with suspicion of NAI (non-accidental injury) needs:", "CT", ["Observation only", "MRI always first", "X-ray skull"])
q(437, S4, "In children, GCS <14 or <15 applies to:", "Under-ones", ["Under-fives", "Under-tens", "Adolescents"])
q(437, S4, "In children, bruise/swelling/laceration of what size warrants CT?", ">5 cm in under-ones", [">3 cm in under-fives", ">10 cm any age", ">2 cm in newborns"])
q(437, S4, "Unexplained confusion >4 hours after head injury requires:", "Neurosurgeon involvement", ["CT after 24 h", "Discharge advice", "Steroids"])
q(437, S4, "Neurosurgeon is involved when GCS is:", "≤8", ["≤13", "≤15", "<5 only"])

# ------------------------------------------------------------------ p438
S5 = "Brain Injury: Types, Severity, Concussion vs DAI"
q(438, S5, "PRIMARY brain injury is due to:", "Impact", ["Rise in ICT", "Hypoxia", "Hypotension"])
q(438, S5, "SECONDARY brain injury is due to:", "Rise in ICT", ["Impact", "Direct contusion", "Scalp laceration"])
q(438, S5, "MINOR head injury severity is:", "GCS 15/15, no LOC", ["GCS 14/15, LOC(+)", "GCS 9-13", "GCS ≤8"])
q(438, S5, "MILD head injury severity is:", "GCS 14/15, LOC(+)", ["GCS 15/15 no LOC", "GCS 9-13", "GCS ≤8"])
q(438, S5, "MODERATE head injury GCS is:", "9-13", ["14-15", "≤8", "3-5"])
q(438, S5, "SEVERE head injury GCS is:", "≤8", ["9-13", "14-15", "13-14"])
q(438, S5, "The mildest type of primary brain injury is:", "Concussion", ["DAI", "Contusion", "EDH"])
q(438, S5, "The most severe type of primary brain injury is:", "Diffuse axonal injury (DAI)", ["Concussion", "Contusion", "SAH"])
q(438, S5, "Mechanism of concussion:", "Contact sports", ["High velocity shearing", "Penetrating injury", "Blast"])
q(438, S5, "Mechanism of DAI:", "High velocity injury → shearing force b/w grey & white matter", ["Contact sports", "Low velocity fall", "Venous tear"])
q(438, S5, "Colorado classification grades (concussion):", "Grade I confusion, Grade II amnesia, Grade III LOC", ["Grade I LOC, Grade II confusion, Grade III amnesia", "I coma, II amnesia, III confusion", "I death, II vegetative, III recovery"])
q(438, S5, "Multiple concussions lead to:", "Chronic traumatic encephalopathy", ["DAI", "EDH", "Normal pressure hydrocephalus"])
q(438, S5, "Ix of concussion:", "NCCT (IOC) — Normal", ["MRI — hemorrhages", "EEG", "LP"])
q(438, S5, "Mx/advice after concussion:", "Avoid contact sports", ["Immediate surgery", "Lumbar puncture", "Steroids"])
q(438, S5, "C/F of DAI:", "Coma with no improvement of GCS", ["Lucid interval", "Raccoon eyes", "Battle sign"])
q(438, S5, "DAI: NCCT shows:", "Normal scan", ["Biconvex bleed", "Crescenteric bleed", "Punctate hemorrhages"])
q(438, S5, "IOC for DAI:", "MRI — punctate hemorrhages at grey & white matter junction", ["NCCT", "EEG", "Angiography"])
q(438, S5, "Autopsy findings in DAI:", "Retraction balls, clubbed axons", ["Plaques & tangles", "Lewy bodies", "Ring hemorrhages"])
q(438, S5, "Prognosis of DAI:", "Worst", ["Best", "Intermediate", "Depends only on age"])
q(438, S5, "Isolated brain/head injury rarely causes:", "Hypotension", ["Hypertension", "Bradycardia", "Seizure"])
q(438, S5, "In a head injury patient with hypotension, suspect:", "Bleeding elsewhere (thorax, pelvis, abdomen, long bones)", ["Brain bleed as cause", "Scalp hemorrhage only", "Neurogenic shock always"])
q(438, S5, "Concealed bleeding sites searched in a hypotensive head injury patient:", "Thorax, pelvis, abdomen & long bones", ["Scalp & face", "Neck & hands", "Feet only"])
q(438, S5, "Hypotension with associated spinal injury in head trauma is due to:", "Neurogenic bladder", ["Neurogenic heart", "Adrenal failure", "Vagal stimulation"])
q(438, S5, "Late stage head injury state that can cause hypotension:", "Brain herniation", ["Concussion", "DAI", "Scalp tear"])

# ------------------------------------------------------------------ p439
S6 = "Intracranial Haemorrhages: Contusion and Extradural (EDH)"
q(439, S6, "The m/c type of bleed following head trauma is:", "Contusion (intraparenchymal bleed)", ["EDH", "SDH", "SAH"])
q(439, S6, "M/c site of traumatic cerebral contusion:", "Temporal > frontal lobe", ["Frontal > temporal", "Occipital", "Parietal"])
q(439, S6, "Frontal lobe contusion can cause:", "Personality changes", ["Hemotympanum", "Battle sign", "CSF leak"])
q(439, S6, "Ix of contusion:", "NCCT (IOC)", ["MRI", "X-ray", "Angio"])
q(439, S6, "In the majority, contusion mx is:", "Conservative — control the ICT", ["Surgical evacuation", "Steroids", "Decompressive craniectomy"])
q(439, S6, "Contusions that coalesce & increase in size need:", "Sx evacuation", ["Observation", "Mannitol only", "LP"])
q(439, S6, "EDH incidence is m/c in:", "Young age", ["Elderly", "Infants", "Middle age"])
q(439, S6, "Mechanism of EDH:", "High velocity impact", ["Trivial injury", "Whiplash", "Blast wave"])
q(439, S6, "M/c source of bleeding in EDH:", "Middle meningeal artery", ["Bridging veins", "Sagittal sinus", "Cortical artery"])
q(439, S6, "The lucid interval in EDH is:", "Not pathognomonic", ["Always present", "Pathognomonic", "Seen only in children"])
q(439, S6, "Classic NCCT appearance of EDH:", "Biconvex/lens-shaped hemorrhage", ["Crescenteric", "Star-shaped", "Diffuse white-out"])
q(439, S6, "EDH bleed is restricted between:", "Skull & dura (limited by cranial sutures)", ["Dura & arachnoid", "Arachnoid & pia", "Within brain"])
q(439, S6, "Definitive mx of EDH:", "Craniotomy > Burr hole", ["Burr hole > craniotomy", "Observation", "Mannitol"])
q(439, S6, "EDH accumulates near the:", "Pterion", ["Lambda", "Bregma", "Asterion"])
q(439, S6, "Indication for craniotomy in EDH (clot volume):", ">30 cc", [">10 cc", ">50 cc", ">100 cc"])
q(439, S6, "Indication for craniotomy in EDH (midline shift):", ">5 mm", [">2 mm", ">10 mm", ">15 mm"])
q(439, S6, "Indication for craniotomy in EDH (clot thickness):", ">1.5 cm", [">0.5 cm", ">2.5 cm", ">3 cm"])
q(439, S6, "If NCCT is not available, the side of craniotomy/burr hole is decided by:", "Same side as the dilated pupil", ["Opposite to dilated pupil", "Side of hemiparesis", "Side of Battle sign"])
q(439, S6, "Normal phenomenon: a LEFT EDH produces:", "Right sided hemiparesis", ["Left sided hemiparesis", "Bilateral paresis", "No weakness"])
q(439, S6, "Site of burr hole is marked on NCCT as:", "Same side as the bleeding", ["Contralateral side", "Midline", "Depends on pupil only"])

# ------------------------------------------------------------------ p440
S7 = "Kernohan Notch Phenomenon"
q(440, S7, "Kernohan notch phenomenon occurs in:", "Lt. temporal lobe EDH (left side bleed)", ["Rt frontal SDH", "Bilateral SAH", "Posterior fossa EDH"])
q(440, S7, "Sequence after ↑ICT in Kernohan phenomenon:", "Temporal lobe/uncal herniation → compress Kernohan notch on Rt. side", ["Uncal herniation → Lt notch → Rt corticospinal", "Tonsillar herniation → medulla", "Subfalcial herniation → ACA"])
q(440, S7, "Kernohan notch compresses the:", "Right corticospinal tract", ["Left corticospinal tract", "Optic tract", "Medial lemniscus"])
q(440, S7, "The paradoxical result of right corticospinal tract compression (left EDH):", "Lt sided hemiparesis (falsely localised as Rt sided bleed)", ["Rt sided hemiparesis", "Bilateral weakness", "Only ataxia"])
q(440, S7, "Kernohan phenomenon can falsely localise the bleed as:", "Right sided", ["Left sided", "Bilateral", "Midline"])

# ------------------------------------------------------------------ p440
S8 = "Subdural Haemorrhage and Traumatic SAH"
q(440, S8, "ACUTE subdural hemorrhage is defined as:", "<3 days", ["<7 days", "3-21 days", ">21 days"])
q(440, S8, "SUBACUTE subdural hemorrhage duration:", "3-21 days", ["<3 days", "21-60 days", ">21 days"])
q(440, S8, "CHRONIC subdural hemorrhage duration:", ">21 days", ["<3 days", "3-21 days", ">7 days only"])
q(440, S8, "Mechanism of CHRONIC SDH:", "Trivial injury → bleed in bridging veins", ["High velocity → MMA tear", "Penetrating injury", "Cortical artery rupture"])
q(440, S8, "Classic chronic SDH patient:", "Elderly patient post trivial injury", ["Young adult post RTA", "Infant", "Athlete"])
q(440, S8, "Typical chronic SDH course:", "Normal for few days/weeks → altered sensorium", ["Immediate coma", "Lucid interval", "Progressive blindness"])
q(440, S8, "IOC for SDH:", "CT scan", ["MRI", "NCCT only for chronic", "LP"])
q(440, S8, "CT appearance of SDH:", "Concavo convex/crescenteric hemorrhage", ["Biconvex/lens", "Ring enhancing", "Diffuse axonal spots"])
q(440, S8, "SDH blood is located:", "B/w dura & arachnoid", ["B/w skull & dura", "Intraparenchymal", "Subarachnoid"])
q(440, S8, "SDH is NOT restricted by suture lines, hence:", "↑Extent of brain injury", ["Smaller bleed", "Self-limiting", "Never crosses midline"])
q(440, S8, "Craniotomy/burr hole for SDH — ANY 1 criterion (thickness):", ">1 cm", [">1.5 cm", ">0.5 cm", ">3 cm"])
q(440, S8, "Craniotomy/burr hole for SDH — ANY 1 criterion (midline shift):", ">5 mm", [">10 mm", ">2 mm", ">1 cm"])
q(440, S8, "Craniotomy/burr hole for SDH — ANY 2 criteria include:", ">2 points drop in GCS, ICP >20 mmHg, fixed dilated pupil", [">30 cc clot, >5 mm shift", "Lucid interval, raccoon eyes", "Age >65, amnesia"])
q(440, S8, "The m/c cause of SAH is:", "Trauma", ["Aneurysm", "AVM", "Hypertension"])
q(440, S8, "Mx of traumatic SAH:", "Conservative", ["Surgery", "Coiling", "Nimodipine infusion"])

# ------------------------------------------------------------------ p441
S9 = "Bleeds Summary, Secondary Brain Injury, Monro-Kellie, CPP & Cushing's"
q(441, S9, "Summary: EDH history is:", "Usually young patient, high velocity impact", ["Usually elderly, trivial injury", "Any age, spontaneous", "Infant, birth trauma"])
q(441, S9, "Summary: Chronic SDH history is:", "Usually elderly patient, trivial injury", ["Young, high velocity", "Always iatrogenic", "Child, NAI"])
q(441, S9, "Summary: EDH feature & CT:", "Lucid interval; biconvex hemorrhage", ["Coma; concavo convex", "Altered sensorium; crescenteric", "None; normal"])
q(441, S9, "Summary: Chronic SDH feature & CT:", "Normal for a few weeks then altered sensorium; concavo convex", ["Lucid interval; biconvex", "Coma; MRI IOC", "None; normal"])
q(441, S9, "Summary: DAI features & Ix:", "Coma with no signs of recovery; IOC is MRI", ["Lucid interval; CT", "Altered sensorium; CT", "Hemiparesis; X-ray"])
q(441, S9, "Normal state (Monro-Kellie) intracranial components:", "Venous volume, arterial volume, brain & CSF", ["Brain, blood, bone", "CSF, blood, mass", "Brain, CSF, lymph"])
q(441, S9, "The doctrine explaining compensated vs decompensated states with a mass:", "Monro-Kellie doctrine", ["Cushing doctrine", "Starling law", "Monroe-Guthrie test"])
q(441, S9, "Cerebral Perfusion Pressure (CPP) is:", "The pressure required to perfuse brain parenchyma", ["Pressure inside ventricles", "Systemic BP only", "Venous sinus pressure"])
q(441, S9, "CPP formula:", "CPP = mean arterial pressure − intracranial pressure", ["CPP = ICP − MAP", "CPP = SBP − ICP", "CPP = MAP × ICP"])
q(441, S9, "Normal CPP:", "≥60 mmHg", ["≥100 mmHg", "≥40 mmHg", "≥80 mmHg"])
q(441, S9, "Cushing's reflex triad (response to maintain CPP despite ↑ICP):", "↑SBP, ↓HR & altered respiration", ["↓SBP, ↑HR, tachypnea", "↑SBP, ↑HR, apnea", "↓SBP, ↓HR, bradypnea"])
q(441, S9, "The MAP rises in raised ICT to:", "Maintain CPP despite ↑ICP", ["Reduce brain volume", "Treat hypertension", "Shrink CSF spaces"])
q(441, S9, "Cushing's ulcers — site:", "Acid producing areas of stomach", ["Duodenal cap only", "Esophagus", "Colon"])
q(441, S9, "Cushing's ulcers — type:", "Stress ulcers", ["Peptic ulcers", "Dieulafoy lesions", "Mallory-Weiss tears"])

# ------------------------------------------------------------------ p442
S10 = "Management of Raised ICT and Key Parameters"
q(442, S10, "Raised ICT in trauma — mx step 1:", "Adequate oxygen", ["Mannitol first", "Hyperventilation first", "Steroids"])
q(442, S10, "Adequate perfusion in raised ICT means SBP:", ">100 mmHg", [">80 mmHg", ">120 mmHg", ">90 mmHg"])
q(442, S10, "Dextrose solutions are AVOIDED in head injury because they cause:", "Hyperglycemia → worsens cerebral edema", ["Hyponatremia", "Hypoglycemia", "Metabolic acidosis"])
q(442, S10, "Osmotic agent used in raised ICT:", "I/V mannitol", ["Dextrose", "Furosemide only", "Hypertonic saline only"])
q(442, S10, "Hyperventilation in raised ICT is used:", "Only in moderate amounts", ["Maximally", "Never", "Continuously for 48 h"])
q(442, S10, "Head position in raised ICT:", "Slight elevation", ["Flat", "Trendelenburg", "Head down"])
q(442, S10, "Role of steroids in traumatic raised ICT:", "No role", ["First line", "Given with mannitol", "Always prophylactic"])
q(442, S10, "Steroids ARE used in ↑ICT when there is:", "Vasogenic edema d/t tumors", ["Cytotoxic edema", "Any trauma", "SAH"])
q(442, S10, "Target PaCO2 in head injury:", "4.5-5.0 kPa", ["6-7 kPa", "3.0-3.5 kPa", "8-9 kPa"])
q(442, S10, "Target PaO2 in head injury:", ">11 kPa", [">5 kPa", ">8 kPa", ">15 kPa"])
q(442, S10, "Target MAP in head injury:", "80-90 mmHg", ["60-70 mmHg", "100-120 mmHg", "50-60 mmHg"])
q(442, S10, "Target ICP in head injury:", "<20 mmHg", ["<30 mmHg", "<40 mmHg", "<60 mmHg"])
q(442, S10, "Target CPP in head injury:", ">60 mmHg", [">100 mmHg", ">40 mmHg", ">80 mmHg"])
q(442, S10, "Target [Na+] in head injury:", ">140 mmol/L", [">130 mmol/L", ">120 mmol/L", ">150 mmol/L"])
q(442, S10, "Target [K+] in head injury:", ">4 mmol/L", [">3 mmol/L", ">2.5 mmol/L", ">5 mmol/L"])
q(442, S10, "Prophylactic phenytoin/valproate is NOT recommended for:", "Preventing LATE posttraumatic seizures (PTS)", ["Early PTS", "Status epilepticus", "Alcohol withdrawal"])
q(442, S10, "Phenytoin/valproate prophylaxis IS used in:", "Early PTS", ["Late PTS", "All PTS", "Never"])

# ------------------------------------------------------------------ p442
S11 = "NICE Discharge Criteria in Mild Head Injury"
q(442, S11, "GCS criterion for discharge in mild head injury:", "GCS 15/15 with no focal deficits", ["GCS ≥13", "GCS 14/15", "GCS ≥12"])
q(442, S11, "CT requirement before discharge:", "Normal CT brain if indicated", ["CT mandatory in all", "No CT ever", "CT only for elderly"])
q(442, S11, "Patient must NOT be under the influence of:", "Alcohol or drugs", ["Caffeine", "Smoking", "Antibiotics"])
q(442, S11, "Discharge requires the patient to be accompanied by:", "A responsible adult", ["A doctor", "A nurse", "A physiotherapist"])
q(442, S11, "Advice format at discharge:", "Verbal AND written head injury advice", ["Verbal only", "Written only", "No advice needed"])
q(442, S11, "Seek medical attention if — headache:", "Persistent/worsening despite analgesia", ["Any mild headache", "Headache at night only", "Never"])
q(442, S11, "Seek medical attention if — vomiting:", "Persistent", ["One episode", "Never", "Only morning"])
q(442, S11, "Seek medical attention symptoms also include:", "Drowsiness, visual disturbance, limb weakness or numbness", ["Mild nausea", "Neck stiffness only", "Tinnitus only"])

# ------------------------------------------------------------------ p443
S12 = "Glasgow Outcome Score and Brain Death"
q(443, S12, "Glasgow Outcome Score is a:", "Prognostic score", ["Severity score", "Anatomical score", "Disability pension score"])
q(443, S12, "Glasgow Outcome Score 1:", "Death", ["Good recovery", "PVS", "Severe disability"])
q(443, S12, "Glasgow Outcome Score 2:", "Persistent vegetative state", ["Death", "Moderate disability", "Severe disability"])
q(443, S12, "Glasgow Outcome Score 3:", "Severe disability", ["Moderate disability", "Good recovery", "PVS"])
q(443, S12, "Glasgow Outcome Score 4:", "Moderate disability", ["Severe disability", "Good recovery", "Death"])
q(443, S12, "Glasgow Outcome Score 5:", "Good recovery", ["Moderate disability", "PVS", "Death"])
q(443, S12, "Brain death is certified by:", "2 experts", ["1 expert", "3 experts", "A panel of 5"])
q(443, S12, "Brain death can be declared only if:", "There is no possibility of recovery of brain function", ["EEG is flat once", "Pupils are sluggish", "GCS is 5"])
q(443, S12, "Brain death criteria — GCS:", "3", ["≤5", "≤8", "0"])
q(443, S12, "Brain death criteria — pupils:", "Nonreactive", ["Sluggish", "Constricted", "Dilated but reactive"])
q(443, S12, "Brain death criteria — brainstem reflexes:", "Absent", ["Present", "Hyperactive", "Variable"])
q(443, S12, "Brain death criteria — ventilation:", "No spontaneous ventilatory effort", ["Needs O2 only", "Rapid shallow breathing", "Normal"])
q(443, S12, "Confounding factors excluded before brain death declaration:", "Alcohol/drug intoxication & hypothermia", ["Diabetes", "Anemia", "Hypertension"])
q(443, S12, "Ancillary studies used in brain death:", "EEG & cerebral angiography", ["MRI only", "PET only", "LP"])

# ------------------------------------------------------------------ units
UNIT_DEFS = [
    (S1, "Scalp layers ride the SCALP mnemonic — Skin, Connective tissue, Aponeurosis, Loose areolar tissue, Periosteum. The dense connective layer anchors vessels to fibrous septa so they cannot constrict: pressure first, then suture (no 1/1-0/2-0; cutting or reverse-cutting needle). Blood under the aponeurosis tracks to a black eye, and loose areolar tissue carries infection from the dangerous area of the face retrograde via emissary veins into cavernous sinus thrombosis."),
    (S2, "Non-depressed skull fractures heal with conservative mx; depressed ones get an NCCT (the IOC for head injury) and are elevated and fixed only for focal neurological signs or depression deeper than the adjacent skull."),
    (S3, "Fossa-wise: anterior fractures hit the cribriform plate (bilateral raccoon eyes whose posterior border vanishes, CSF rhinorrhoea with halo sign and β2 transferrin, epistaxis, anosmia, frontal contusion); middle hit the petrous temporal (Battle sign at 24-48 h, hemotympanum, otorrhea, facial palsy, paradoxical rhinorrhoea); posterior hit the occipital bone (visual problems, VI nerve, Vernet syndrome IX-XI). Treat as open fractures with a 3rd-gen cephalosporin and never pack the nose/ear."),
    (S4, "NICE: rule out cervical spine injury in everyone and log GCS half-hourly for 2 h, hourly to 6 h, then 2-hourly. Adults get CT within 1 h for GCS <13 anytime, <15 at 2 h, focal deficit, suspected open/depressed/basal fracture, >1 vomit, post-traumatic seizure or LOC — and within 8 h for age >65 or retrograde amnesia >30 min. Children add NAI suspicion, first seizure, GCS <14/<15 in under-ones and >5 cm swellings; GCS ≤8, a falling GCS or confusion >4 h calls the neurosurgeon."),
    (S5, "Primary injury comes with the impact, secondary with rising ICT; severity runs minor (15, no LOC), mild (14, LOC), moderate (9-13), severe (≤8). Concussion — the mildest — grades Colorado I-II-III (confusion, amnesia, LOC) and heals off contact sports; DAI — the worst — shears grey-white junction with coma, a normal NCCT, punctate MRI hemorrhages and retraction balls at autopsy. Isolated head injury rarely drops the BP: suspect thorax/pelvis/abdomen/long-bone bleeding, neurogenic bladder or late herniation."),
    (S6, "Contusion is the commonest traumatic bleed (temporal > frontal, personality changes when frontal) — NCCT, control ICT, evacuate only when it coalesces. EDH is a young person's high-velocity bleed from the middle meningeal artery near the pterion: lucid interval (±, not pathognomonic), biconvex clot splinted by sutures, and craniotomy for >30 cc, >5 mm shift or >1.5 cm thickness — pick the side off the CT or the dilated pupil (left EDH → right hemiparesis normally)."),
    (S7, "Kernohan notch: a left temporal EDH pushes ↑ICT, uncal herniation, and the notch on the RIGHT crushes the right corticospinal tract — so the LEFT side becomes weak and the bleed is falsely localised as right-sided."),
    (S8, "SDH is timed acute <3 d, subacute 3-21 d, chronic >21 d; the chronic one is an elderly post-trivial-illness bridging-vein bleed that wakes up altered weeks later. CT shows a concavo-convex crescent between dura and arachnoid that ignores suture lines. Surgery needs any one of >1 cm thickness or >5 mm shift, or any two of >2-point GCS drop, ICP >20 mmHg, fixed dilated pupil. Traumatic SAH — trauma is the commonest SAH cause — stays conservative."),
    (S9, "The summary table contrasts EDH (young, high velocity, lucid, biconvex) with chronic SDH (elderly, trivial, delayed sensorium, concavo-convex) and DAI (high velocity coma, MRI IOC). Monro-Kellie balances venous, arterial, brain and CSF volumes until decompensation. CPP = MAP − ICP and must stay ≥60; the Cushing reflex buys perfusion with ↑SBP, ↓HR and altered respiration, while Cushing's stress ulcers blossom in acid-producing stomach areas."),
    (S10, "Raised ICT in trauma: oxygenate, perfuse (SBP >100), skip dextrose (hyperglycemia worsens edema), give IV mannitol, hyperventilate only moderately, elevate the head, and no steroids — except vasogenic tumour edema. Hold PaCO2 4.5-5.0 kPa, PaO2 >11, MAP 80-90, ICP <20, CPP >60, Na >140, K >4; phenytoin/valproate covers early PTS but not late seizures."),
    (S11, "Mild head injury discharges home only with GCS 15/15 without deficits, a normal CT if CT was indicated, no alcohol/drugs on board, a responsible adult and verbal-plus-written advice; return for persistent headache, vomiting, drowsiness, visual disturbance or limb weakness."),
    (S12, "Glasgow Outcome Score walks 1-5: death, vegetative state, severe disability, moderate disability, good recovery. Brain death is certified by two experts when nothing can recover — GCS 3, nonreactive pupils, absent brainstem reflexes, no spontaneous ventilatory effort, no confounders (alcohol, drugs, hypothermia) — with EEG and cerebral angiography as ancillary support."),
]

first_page = {}
for x in Q:
    first_page.setdefault(x["sec"], x["page"])

UNITS = []
for i, (title, guide) in enumerate(UNIT_DEFS, 1):
    UNITS.append({
        "id": f"SURG-U57-{i}",
        "ch": 57,
        "n": i,
        "title": title,
        "sec": f"{title} · p{first_page[title]}",
        "qs": [x["id"] for x in Q if x["sec"] == title],
        "guide": guide,
    })

covered = [x for u in UNITS for x in u["qs"]]
assert covered == [x["id"] for x in Q]
assert len(set(covered)) == len(covered)
with open("data/ch57.json", "w", encoding="utf-8") as f:
    json.dump({"questions": Q, "units": UNITS}, f, ensure_ascii=False, indent=1)
print(f"ch57: {len(Q)} questions, {len(UNITS)} units")
