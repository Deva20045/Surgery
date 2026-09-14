#!/usr/bin/env python3
"""Build data/ch53.json — Neurosurgery (Marrow Surgery Ed 8, pp399-409)."""
import json

Q = []

def q(page, sec, text, correct, wrongs, note=None):
    opts = [correct] + list(wrongs)
    assert len(opts) == 4
    Q.append({
        "id": f"SURG-C53-{len(Q)+1:03d}",
        "sec": sec,
        "page": page,
        "q": text,
        "opts": opts,
        "ans": 0,
        "exp": (note or correct) + f" (Book p{page})",
    })

# ------------------------------------------------------------------ p399
S1 = "Cerebrovascular Accidents and Berry Aneurysms"
q(399, S1, "The ischemic type of cerebrovascular accident includes:", "Thrombotic and embolic", ["Intracerebral and SAH", "EDH and SDH", "SAH and EDH"])
q(399, S1, "The hemorrhagic types of CVA include intracerebral, SAH, EDH and:", "SDH", ["Ischemic stroke", "TIA", "Venous sinus thrombosis"])
q(399, S1, "SAH stands for:", "Subarachnoid hemorrhage", ["Subacute hematoma", "Subaponeurotic hemorrhage", "Supratentorial hemorrhage"])
q(399, S1, "EDH stands for:", "Extra dural hemorrhage", ["Extra dural hematoma of spine only", "Epidural venous bleed", "Ex vacuo hemorrhage"])
q(399, S1, "SDH stands for:", "Subdural hemorrhage", ["Subdural hygroma", "Subarachnoid hemorrhage", "Sinus dural hemorrhage"])
q(399, S1, "The m/c cause of intracerebral hemorrhage is:", "↑ HTN", ["Berry aneurysm", "AV malformation", "Trauma"])
q(399, S1, "The m/c site of intracerebral hemorrhage is:", "Basal ganglia (putamen)", ["Pons", "Cerebellum", "Lobar white matter"])
q(399, S1, "Traumatic SAH is mostly managed:", "Conservatively", ["By coiling", "By clipping", "By exteriorisation"])
q(399, S1, "The more important cause of SAH is:", "Rupture of berry aneurysms", ["Trauma", "Venous rupture", "Capillary bleed"])
q(399, S1, "The m/c aneurysm overall is the:", "Berry aneurysm", ["Fusiform aneurysm", "Mycotic aneurysm", "Dissecting aneurysm"])
q(399, S1, "The m/c extracranial site of berry aneurysm is:", "Infrarenal abdominal aorta", ["Thoracic aorta", "Femoral artery", "Renal artery"])
q(399, S1, "Berry aneurysms are morphologically:", "Saccular, junctional aneurysms", ["Fusiform, mid-arterial", "Dissecting", "Atherosclerotic"])
q(399, S1, "A risk factor for berry aneurysm is:", "Polycystic kidney disease", ["Simple renal cyst", "Medullary sponge kidney", "Horseshoe kidney"])
q(399, S1, "Another risk factor for berry aneurysm is:", "Ehlers-Danlos syndrome", ["Marfan-like obesity", "Osteogenesis imperfecta type I", "Alport syndrome"])
q(399, S1, "Yet another risk factor for berry aneurysm is:", "Fibromuscular dysplasia", ["Atherosclerosis obliterans", "Takayasu arteritis", "Polyarteritis nodosa"])
q(399, S1, "Other risk factors for berry aneurysms include HTN, smoking and:", "Marfan syndrome", ["Turner syndrome", "Noonan syndrome", "Klinefelter syndrome"])
q(399, S1, "The m/c site of rupture of a berry aneurysm is the:", "Apex", ["Neck", "Base", "Lateral wall"])
q(399, S1, "On the circle of Willis, the m/c site of berry aneurysm is the:", "Anterior communicating artery", ["Middle cerebral artery", "Internal carotid artery", "Basilar artery"])
q(399, S1, "The anterior communicating artery site accounts for what percentage of berry aneurysms?", "40%", ["34%", "20%", "4%"])
q(399, S1, "The middle cerebral artery site accounts for what percentage of berry aneurysms?", "34%", ["40%", "20%", "4%"])
q(399, S1, "The internal carotid/posterior communicating site accounts for what percentage of berry aneurysms?", "20%", ["40%", "34%", "4%"])
q(399, S1, "The posterior circulation (basilar) site accounts for what percentage of berry aneurysms?", "4%", ["20%", "34%", "40%"])

# ------------------------------------------------------------------ p400
S2 = "SAH: Clinical Features, Investigations, Grading and Management"
q(400, S2, "The classic headache of SAH is:", "Thunderclap headache / worst headache of life", ["Gradual holocranial headache", "Early morning headache", "Positional headache"])
q(400, S2, "In SAH, focal neurological signs are:", "Absent", ["Always present", ["Present in half"] , "Present late only"])
q(400, S2, "A clinical feature of SAH is:", "Neck stiffness", ["Kernig-negative rigidity", ["Limb hypertonia"] , "Papilloedema always"])
q(400, S2, "SAH may be preceded by:", "Prodromal symptoms", ["No warning ever", ["Seizure only"] , "Visual aura only"])
q(400, S2, "Terson's syndrome is:", "SAH + vitreous hemorrhage", ["SAH + retinal detachment", ["SAH + papilloedema"] , "SAH + third nerve palsy"])
q(400, S2, "MCA aneurysm characteristically causes:", "Retroorbital pain", ["Occipital pain", ["Neck pain"] , "Vertex pain"])
q(400, S2, "The IOC for SAH is:", "NCCT", ["MRI", ["Lumbar puncture first"] , "Catheter angiography first"])
q(400, S2, "The grading done on CT for SAH is:", "Fischer grading", ["Hunt and Hess", ["WFNS"] , "GCS"])
q(400, S2, "CSF tap in SAH shows:", "Xanthochromia", ["Frank pus", ["Clear CSF"] , "Chylous CSF"])
q(400, S2, "Xanthochromia in SAH CSF is due to:", "RBC lysis", ["High protein", ["Low glucose"] , "Bilirubin from liver"])
q(400, S2, "Hunt and Hess grading is based on:", "Neurological symptoms", ["GCS", ["CT blood load"] , "Angiographic findings"])
q(400, S2, "WFNS grading is based on:", "GCS", ["Neurological symptoms", ["Fischer grade"] , "Motor score alone"])
q(400, S2, "WFNS stands for:", "World Federation of Neurological Surgeons", ["World Forum of Neurological Science", ["Western Federation of Neurosurgery"] , "World Federation of Neurosciences"])
q(400, S2, "The first step in managing SAH is:", "Cerebral angiography", ["Craniotomy", ["Coiling blind"] , "NCCT repeat"])
q(400, S2, "Cerebral angiography in SAH is followed by:", "Intervention", ["Observation", ["Repeat tap"] , "Anticoagulation"])
q(400, S2, "The interventional radiology option for aneurysm is:", "Coiling", ["Clipping", ["Wrapping"] , "Trapping"])
q(400, S2, "The surgical option for aneurysm is:", "Clipping", ["Coiling", ["Embolisation"] , "Stenting"])
q(400, S2, "In coiling, the coil is released into the aneurysm through a:", "Catheter", ["Guidewire alone", ["Needle"] , "Endoscope"])
q(400, S2, "After the coil fills the aneurysm:", "The catheter is removed", ["The catheter is left in situ", ["The coil is retrieved"] , "Balloon is inflated permanently"])

# ------------------------------------------------------------------ p401
S3 = "SAH Complications and Brain Herniation Syndromes"
q(401, S3, "A complication of SAH is:", "Re-bleeding", ["Hypotension", ["Hypothermia"] , "Seizure-free course"])
q(401, S3, "Hydrocephalus after SAH is due to blood:", "Blocking CSF flow", ["Blocking arterial flow", ["Blocking venous sinuses"] , "Irritating choroid plexus"])
q(401, S3, "Delayed ischemic neurological deficits after SAH appear:", "2-10 days later", ["Within 24 hours", ["After 1 month"] , "After 6 months"])
q(401, S3, "Delayed ischemic neurological deficits are due to:", "Vasospasm", ["Re-bleed", ["Embolism"] , "Hydrocephalus"])
q(401, S3, "Vasospasm after SAH is prevented with:", "Nimodipine", ["Nifedipine", ["Amlodipine"] , "Verapamil"])
q(401, S3, "In aortic dissection, esmolol is used to control:", "Permissive HTN", ["Hypotension", ["Bradycardia"] , "Vasospasm"])
q(401, S3, "Brain herniation begins with breakdown of the:", "Munroe-Kellie doctrine", ["Cushing doctrine", ["Starling doctrine"] , "Bernoulli doctrine"])
q(401, S3, "Raised ICT lowers CPP because CPP equals:", "MAP − ICP", ["MAP + ICP", ["ICP − MAP"] , "MAP × ICP"])
q(401, S3, "The compensatory response to falling CPP is the:", "Cushing's reflex", ["Baroreceptor reflex", ["Bezold-Jarisch reflex"] , "Oculocardiac reflex"])
q(401, S3, "Cushing's reflex produces ↑ SBP which causes:", "↑ HTN", ["↓ HTN", ["↑ ICP"] , "↓ SV"])
q(401, S3, "Cushing's reflex bradycardia increases EDV and thereby:", "↑ SV", ["↓ SV", ["↓ MAP"] , "↑ heart rate"])
q(401, S3, "The third component of Cushing's reflex is:", "Altered breathing", ["Altered vision", ["Altered pupil"] , "Altered tone"])
q(401, S3, "The net effect of Cushing's reflex is ↑ MAP so that CPP is maintained at:", "≥ 60 mmHg", ["≥ 30 mmHg", ["≥ 90 mmHg"] , "≥ 120 mmHg"])
q(401, S3, "The herniation diagram labels cingulate herniation as:", "Subfalcine", ["Transtentorial", ["Transcalvarial"] , "Tonsillar"])
q(401, S3, "The herniation diagram labels downward cerebellar herniation as:", "Tonsillar", ["Transcalvarial", ["Subfalcine"] , "Uncal"])
q(401, S3, "The herniation through the skull defect in the diagram is:", "Transcalvarial", ["Tonsillar", ["Uncal"] , "Central"])
q(401, S3, "Uncal herniation is also called:", "Lateral transtentorial", ["Central transtentorial", ["Subfalcine"] , "Tonsillar"])
q(401, S3, "Uncal herniation produces:", "Ipsilateral CN III palsy ('blown pupil') + contralateral hemiplegia/posturing", ["Contralateral CN III palsy only", ["Bilateral CN III palsy"] , "Ipsilateral hemiplegia only"])
q(401, S3, "The Kernohan notch phenomenon is invoked in:", "Uncal (lateral transtentorial) herniation", ["Subfalcine herniation", ["Tonsillar herniation"] , "Transcalvarial herniation"])
q(401, S3, "In uncal herniation the mass is usually in the:", "Temporal lobe → medial temporal lobe under tentorium cerebelli", ["Frontal lobe under falx", ["Occipital lobe under tentorium"] , "Cerebellum upwards"])
q(401, S3, "Central transtentorial herniation progresses as:", "Coma + B/L small pupils → decorticate → decerebrate posturing → respiratory paralysis → death", ["Coma + dilated pupils → seizure → death", ["Headache → vomiting → recovery"] , "Coma + B/L small pupils → immediate death"])
q(401, S3, "Central transtentorial herniation finally passes through the:", "Foramen magnum", ["Tentorial notch only", ["Falx"] , "Optic canal"])
q(401, S3, "Subfalcine herniation presents with coma + contralateral weakness and posturing especially of the:", "Leg", ["Arm", ["Face"] , "Trunk"])
q(401, S3, "Subfalcine herniation can cause an:", "ACA stroke", ["MCA stroke", ["PCA stroke"] , "Basilar stroke"])
q(401, S3, "In subfalcine herniation a frontal/parietal mass pushes the:", "Cingulate gyrus under falx cerebri", ["Uncus under tentorium", ["Tonsils through foramen magnum"] , "Vermis upwards"])
q(401, S3, "Cerebellar herniation (up or down) produces cerebellar signs + medullary dysfunction ending in:", "Coma + B/L posturing", ["Unilateral posturing", ["Seizures"] , "Locked-in state"])

# ------------------------------------------------------------------ p402-403
S4 = "Kernohan Notch, Management of ↑ ICT and Brain Abscess"
q(402, S4, "Kernohan notch phenomenon is also known as a:", "False localizing sign", ["True localizing sign", ["Meninigitis sign"] , "Herniation sign"])
q(402, S4, "In the Kernohan notch diagram, the bleed causes uncal herniation that presses on the:", "Contralateral (C/L) Kernohan's notch", ["Ipsilateral notch", ["Falx"] , "Tonsil"])
q(402, S4, "The tract compressed at Kernohan's notch is the:", "Descending pyramidal (motor) tract", ["Ascending spinothalamic tract", ["Optic tract"] , "Corticopontine tract"])
q(402, S4, "Pressure on the motor tract at Kernohan's notch yields limb weakness that is:", "Ipsilateral (false localising sign)", ["Contralateral only", ["Bilateral"] , "Absent"])
q(402, S4, "In managing ↑ ICT, adequate IV fluids aim to keep CPP at:", "≥60 mmHg", ["≥30 mmHg", ["≥90 mmHg"] , "≥110 mmHg"])
q(402, S4, "In managing ↑ ICT, SBP should be maintained:", ">100 mmHg", [">80 mmHg", [">140 mmHg"] , ">60 mmHg"])
q(402, S4, "Dextrose fluids are avoided in ↑ ICT because they:", "Worsen cerebral edema", ["Raise sugar", ["Cause diuresis"] , "Lower SBP"])
q(402, S4, "IV mannitol lowers ICT because it is an:", "Osmotic diuretic", ["Loop diuretic", ["Thiazide"] , "K-sparing diuretic"])
q(402, S4, "In ↑ ICT, adequate O2 is given with the patient:", "Propped up", ["Flat", ["Head down"] , "Prone"])
q(402, S4, "Steroids help in ↑ ICT when the edema is:", "Vasogenic (d/t tumors)", ["Cytotoxic", ["Interstitial"] , "Osmotic"])
q(402, S4, "Hematogenous brain abscess most commonly involves the:", "Parietal region", ["Frontal region", ["Temporal region"] , "Occipital region"])
q(402, S4, "A risk factor for hematogenous brain abscess is:", "Immunocompromised state", ["Hypertension", ["Diabetes insipidus"] , "Obesity"])
q(402, S4, "Another risk factor for hematogenous brain abscess is:", "Cyanotic heart disease", ["ASD only", ["Rheumatic heart disease"] , "Endocarditis of aortic valve"])
q(403, S4, "Direct spread from frontal sinusitis causes a:", "Frontal lobe abscess", ["Temporal lobe abscess", ["Parietal lobe abscess"] , "Cerebellar abscess"])
q(403, S4, "Direct spread from otitis media causes a:", "Temporal lobe abscess", ["Frontal lobe abscess", ["Occipital abscess"] , "Pontine abscess"])
q(403, S4, "A clinical feature of brain abscess is:", "Headache", ["Neck pain only", ["Diplopia only"] , "Tinnitus only"])
q(403, S4, "Another clinical feature of brain abscess is:", "Seizure", ["Hemianopia only", ["Ptosis"] , "Dysarthria only"])
q(403, S4, "Brain abscess also presents with nausea/vomiting, vomiting and:", "Neurological deficits", ["Psychiatric features", ["Visual failure"] , "Hearing loss"])
q(403, S4, "On imaging a brain abscess classically appears as a:", "Ring enhanced lesion", ["Homogeneous mass", ["Calcified nodule"] , "Cystic non-enhancing lesion"])
q(403, S4, "The IOC for brain abscess is:", "CT", ["X-ray", ["Ultrasound"] , "PET"])
q(403, S4, "The other key investigation for brain abscess is:", "MRI", ["CT myelogram", ["Skull X-ray"] , "Angiography"])
q(403, S4, "First-line management of brain abscess is:", "IV antibiotics", ["Immediate excision always", ["Aspiration always"] , "Steroids alone"])
q(403, S4, "A solitary brain abscess is best:", "Drained", ["Excised with margins", ["Left alone"] , "Treated with steroids"])
q(403, S4, "Multiple brain abscesses are managed by:", "Continue antibiotics + monitor", ["Drainage of all", ["Excision of all"] , "Radiotherapy"])
q(403, S4, "Brain abscess management also includes treating the 1° cause, anti-epileptics and:", "Managing ↑ ICT", ["Long-term steroids", ["Prophylactic RT"] , "Lifelong anticoagulation"])

# ------------------------------------------------------------------ p403-404
S5 = "Neural Tube Defects: Spina Bifida Occulta and Aperta"
q(403, S5, "Spina bifida occulta is a:", "Closed spina bifida (neural tube defect)", ["Open spina bifida", ["Meningocele"] , "Myelomeningocele"])
q(403, S5, "In spina bifida occulta there is a defect in ≥1 vertebrae but:", "No herniation of meninges/cord", ["Herniation of meninges only", ["Herniation of cord only"] , "Herniation of both"])
q(403, S5, "Spina bifida occulta is usually:", "Asymptomatic", ["Paralytic", ["Painful"] , "Progressive"])
q(403, S5, "At the site of spina bifida occulta one may see a:", "Dimple/tuft of hair", ["Sinus tract with discharge", ["Lipoma always"] , "Cystic swelling"])
q(403, S5, "Spina bifida occulta is diagnosed on:", "X-ray", ["MRI", ["CT"] , "Ultrasound"])
q(403, S5, "Management of spina bifida occulta is:", "No intervention needed", ["Early surgery", ["Folate only"] , "Shunt"])
q(403, S5, "The spina bifida occulta diagram labels, superficial to deep, skin, hair, dura, arachnoid and:", "Transverse process", ["Spinous process", ["Pedicle"] , "Lamina"])
q(404, S5, "In spina bifida aperta:", "Only membranes/membranes + cord herniate out of posterior vertebral arch defect", ["Nothing herniates", ["Only bone herniates"] , "Cord never herniates"])
q(404, S5, "Meningocele is herniation of:", "Meninges only, not cord", ["Meninges + cord", ["Cord only"] , "Nerve roots only"])
q(404, S5, "A presentation of meningocele is:", "Swelling", ["Pain only", ["Fever"] , "Tenderness"])
q(404, S5, "Meningocele may present with lower limb:", "Weakness/spasticity", ["Flaccidity only", ["Tremors"] , "Atrophy only"])
q(404, S5, "Meningocele may present with:", "Bladder bowel dysfunction", ["Constipation only", ["Diarrhoea only"] , "No sphincteric issue"])
q(404, S5, "On examination a meningocele is a:", "Cystic swelling (CSF)", ["Solid swelling", ["Pulsatile swelling"] , "Reducible swelling"])
q(404, S5, "Fluctuation in a meningocele is:", "(+)", ["(−)", ["Absent always"] , "Only transillumination"])
q(404, S5, "The investigation to determine extent of herniation in meningocele is:", "MRI", ["CT", ["X-ray"] , "Myelogram"])
q(404, S5, "Meningocele is managed by:", "Surgery", ["Observation always", ["Aspiration"] , "Sclerotherapy"])
q(404, S5, "Early surgery for meningocele is indicated if there is:", "Infection/leakage", ["Asymptomatic course", ["Normal neurology"] , "Small size"])
q(404, S5, "The other indication for early meningocele surgery is:", "Tethering of cord", ["Hydrocephalus alone", ["Cosmesis"] , "Large size"])
q(404, S5, "Late surgery for meningocele is acceptable if the child is:", "Asymptomatic with normal neurological functions", ["Leaking CSF", ["Infected"] , "Tethered"])
q(404, S5, "The most severe type of neural tube defect is:", "Myelomeningocele", ["Meningocele", ["Spina bifida occulta"] , "Lipomeningocele"])
q(404, S5, "Myelomeningocele is herniation of:", "Membranes + cord", ["Meninges only", ["Cord only"] , "Bone + cord"])
q(404, S5, "Neural tube defects are prevented by:", "Folate administration during pregnancy", ["Vitamin B12", ["Iron"] , "Vitamin D"])
q(404, S5, "Maternal use of which drugs ↑ NTD risk?", "Anti-epileptics (phenytoin, valproate)", ["Antibiotics", ["Antihistamines"] , "Antacids"])
q(404, S5, "Clinical features of myelomeningocele are:", "Same as meningocele", ["Milder than meningocele", ["Only cutaneous"] , "Absent at birth"])
q(404, S5, "Surgery for myelomeningocele is:", "Difficult with poorer prognosis compared to meningocele", ["Easier with better prognosis", ["Same as meningocele"] , "Never indicated"])

# ------------------------------------------------------------------ p405-406
S6 = "Chiari Malformation and Dandy Walker Syndrome"
q(405, S6, "Chiari I malformation shows downward displacement of the:", "Cerebellar tonsils", ["Cerebellar vermis", ["Medulla"] , "Fourth ventricle"])
q(405, S6, "Chiari I malformation is associated with:", "Syringomyelia", ["Hydrocephalus always", ["Spina bifida always"] , "Dandy Walker"])
q(405, S6, "Chiari II malformation shows:", "Hydrocephalus", ["No hydrocephalus", ["Syringomyelia only"] , "Tonsillar ascent"])
q(405, S6, "Chiari II malformation shows breaking of the:", "Tectal plate", ["Cribriform plate", ["Quadrigeminal cistern"] , "Petrous apex"])
q(405, S6, "In Chiari II there is downward displacement of cerebellum, brainstem and:", "Fourth ventricle", ["Third ventricle", ["Lateral ventricles"] , "Aqueduct"])
q(405, S6, "Chiari I typically presents in:", "Young adults", ["Infancy", ["Neonates"] , "Elderly"])
q(405, S6, "Chiari II typically presents in:", "Infancy", ["Young adults", ["Adolescence"] , "Middle age"])
q(405, S6, "The usual presentation of Chiari I is:", "Neck/cervical pain", ["Progressive hydrocephalus", ["Respiratory distress"] , "Seizures"])
q(405, S6, "The usual presentation of Chiari II is:", "Progressive hydrocephalus and respiratory distress", ["Neck pain", ["Headache only"] , "Ataxia only"])
q(405, S6, "Caudal dislocation of the medulla in Chiari I is:", "Unusual", ["Yes", ["Constant"] , "Early"])
q(405, S6, "Caudal dislocation of the medulla in Chiari II is:", "Yes", ["Unusual", ["Never"] , "Rare"])
q(405, S6, "In Chiari I the structure dislocated into the cervical canal is the:", "Tonsil", ["Inferior vermis", ["Medulla"] , "4th ventricle"])
q(405, S6, "In Chiari II the structures dislocated into the cervical canal are:", "Inferior vermis, medulla, 4th ventricle", ["Tonsil only", ["Tonsil + medulla"] , "Vermis only"])
q(405, S6, "Hydrocephalus in Chiari I:", "May be absent", ["Rarely absent", ["Always present"] , "Present at birth"])
q(405, S6, "Hydrocephalus in Chiari II:", "Rarely absent", ["May be absent", ["Never present"] , "Transient"])
q(405, S6, "Spina bifida in Chiari I:", "May be present", ["Rarely absent", ["Always present"] , "Never"])
q(405, S6, "Spina bifida in Chiari II:", "Rarely absent", ["May be present", ["Never"] , "In 10%"])
q(405, S6, "Management of Chiari I is usually:", "Conservative", ["Surgical decompression always", ["Shunt always"] , "Radiotherapy"])
q(405, S6, "Management of Chiari II centres on:", "Mx of hydrocephalus, with poor prognosis", ["Conservative follow-up", ["Tonsillar decompression"] , "Folate"])
q(405, S6, "In Dandy Walker syndrome the 4th ventricle shows:", "Marked cystic dilatation", ["Stenosis", ["Normal size"] , "Collapse"])
q(405, S6, "In Dandy Walker syndrome the cerebellar vermis shows:", "Hypogenesis/agenesis", ["Hypertrophy", ["Normal development"] , "Calcification"])
q(405, S6, "In Dandy Walker syndrome the tentorium and lateral sinus are:", "Displaced superiorly", ["Displaced inferiorly", ["Normal"] , "Absent"])
q(405, S6, "A clinical feature of Dandy Walker syndrome is:", "Prominent occipital region", ["Prominent frontal region", ["Microcephaly"] , "Scaphocephaly"])
q(405, S6, "Another clinical feature of Dandy Walker syndrome is:", "Macrocephaly", ["Microcephaly", ["Normocephaly"] , "Plagiocephaly"])
q(405, S6, "The third clinical feature of Dandy Walker syndrome is:", "Hydrocephalus", ["Seizures", ["Blindness"] , "Deafness"])
q(406, S6, "Dandy Walker syndrome is investigated with:", "MRI/CT", ["X-ray", ["Ultrasound only"] , "PET"])
q(406, S6, "Management of Dandy Walker syndrome is:", "Rx hydrocephalus", ["Vermis repair", ["Folate"] , "Observation"])
q(406, S6, "The prognosis of Dandy Walker syndrome is:", "Poor", ["Excellent", ["Good"] , "Fair"])

# ------------------------------------------------------------------ p406
S7 = "CNS Tumors: Salient Features, Management and Brain Metastases"
q(406, S7, "The m/c 1° brain tumor is:", "Glioma", ["Meningioma", ["Medulloblastoma"] , "Schwannoma"])
q(406, S7, "After glioma, the next common 1° brain tumor is:", "Meningioma", ["Medulloblastoma", ["Ependymoma"] , "Lymphoma"])
q(406, S7, "The m/c 1° brain malignancy in children is:", "Medulloblastoma", ["Pilocytic astrocytoma", ["Ependymoma"] , "GBM"])
q(406, S7, "The m/c brain tumor overall is:", "Metastasis/2° tumors", ["Glioma", ["Meningioma"] , "Pituitary adenoma"])
q(406, S7, "A clinical feature of CNS tumors is:", "Focal neurological deficits", ["Diffuse pain only", ["Fever"] , "Rash"])
q(406, S7, "CNS tumors classically cause seizures and headache that is:", "Worse in morning", ["Worse at night", ["Positional"] , "Constant"])
q(406, S7, "Vomiting in CNS tumors is due to:", "↑ ICT", ["Gastric irritation", ["Vagal tone"] , "Chemo"])
q(406, S7, "Frontal lobe tumors cause Witzelsucht syndrome, i.e.:", "Pathological joking", ["Pathological crying", ["Pathological laughter only"] , "Apathy"])
q(406, S7, "The other frontal lobe tumor feature is:", "Personality changes", ["Memory loss only", ["Aphasia"] , "Hemianopia"])
q(406, S7, "The IOC for CNS tumors is:", "MRI", ["CT", ["PET/CT"] , "X-ray"])
q(406, S7, "PET/CT in brain tumors:", "Can miss lesions in brain", ["Is the IOC", ["Detects all lesions"] , "Replaces MRI"])
q(406, S7, "Treatment options for CNS tumors are surgery, radiotherapy and:", "Chemotherapy", ["Immunotherapy only", ["Hormonal therapy"] , "Observation"])
q(406, S7, "Surgery is preferred for CNS tumors when there are:", "Solitary/1-2 lesions", ["Multiple lesions", ["Leptomeningeal disease"] , "Diffuse infiltration"])
q(406, S7, "Chemotherapy for CNS tumors uses agents that:", "Cross the blood brain barrier", ["Are large molecules", ["Bind plasma proteins"] , "Stay intravascular"])
q(406, S7, "Another chemotherapy route for CNS tumors is:", "Intrathecal chemotherapy", ["Intra-arterial only", ["Intravesical"] , "Intraperitoneal"])
q(406, S7, "Radiotherapy for CNS tumors includes whole brain RT and:", "Stereotactic radiosurgery", ["Brachytherapy only", ["Proton only"] , "Palliative RT only"])
q(406, S7, "Stereotactic radiosurgery for CNS tumors is delivered by the:", "Gamma knife", ["LINAC only", ["Cyberknife only"] , "Proton beam"])
q(406, S7, "The gamma knife uses radioactive cobalt sources with shielding, a helmet and converging:", "Gamma rays on the target", ["X-rays on the cord", ["Protons on the skull"] , "Electrons on the dura"])
q(406, S7, "Raised ICT from CNS tumors is also managed as part of:", "Mx: ↑ ICT", ["Mx: seizure only", ["Mx: anemia"] , "Mx: pain only"])
q(406, S7, "The m/c cancer metastasizing to cerebrum is:", "Lung cancer", ["Breast cancer", ["Colon cancer"] , "Melanoma"])
q(406, S7, "The m/c cancer metastasizing to leptomeninges is:", "Breast cancer", ["Lung cancer", ["Gastric cancer"] , "Renal cancer"])
q(406, S7, "The IOC for brain metastases is:", "MRI", ["CT", ["PET"] , "X-ray"])
q(406, S7, "Solitary brain metastases are managed by:", "Sx", ["RT alone", ["Chemo alone"] , "Observation"])
q(406, S7, "The mainstay of treatment for brain metastases is:", "Radiotherapy", ["Surgery", ["Chemotherapy"] , "Steroids"])
q(406, S7, "Leptomeningeal metastatic disease is treated with:", "Chemotherapy", ["Radiotherapy", ["Surgery"] , "Shunt"])
q(406, S7, "Vasogenic edema around brain mets is treated with:", "Steroids (DOC)", ["Mannitol (DOC)", ["Hypertonic saline (DOC)"] , "Diuretics (DOC)"])
q(406, S7, "Brain metastases management also includes:", "Antiepileptics", ["Anticoagulants", ["Antibiotics"] , "Antivirals"])

# ------------------------------------------------------------------ p407
S8 = "Astrocytomas and Oligodendroglioma"
q(407, S8, "Astrocytoma grade I is:", "Pilocytic astrocytoma", ["Low grade (fibrillary) astrocytoma", ["Anaplastic astrocytoma"] , "Glioblastoma multiforme"])
q(407, S8, "Astrocytoma grade II is:", "Low grade (fibrillary astrocytoma)", ["Pilocytic astrocytoma", ["Anaplastic astrocytoma"] , "GBM"])
q(407, S8, "Astrocytoma grade III is:", "Anaplastic astrocytoma", ["Pilocytic astrocytoma", ["Low grade fibrillary"] , "GBM"])
q(407, S8, "Astrocytoma grade IV is:", "Glioblastoma multiforme (GBM)", ["Anaplastic astrocytoma", ["Pilocytic astrocytoma"] , "Fibrillary astrocytoma"])
q(407, S8, "The astrocytoma grades progress from:", "I → IV", ["IV → I", ["II → III only"] , "No progression"])
q(407, S8, "Pilocytic astrocytoma is commonly seen in:", "Children", ["Adults", ["Elderly"] , "Infants only"])
q(407, S8, "Pilocytic astrocytoma presents as a:", "Mural nodule with no infiltration", ["Diffuse infiltrating mass", ["Cyst with enhancing wall only"] , "Calcified plaque"])
q(407, S8, "Pilocytic astrocytoma is a:", "Low grade tumor", ["High grade tumor", ["Grade III"] , "Grade IV"])
q(407, S8, "The m/c site of pilocytic astrocytoma is the:", "Posterior fossa", ["Frontal lobe", ["Temporal lobe"] , "Spinal cord"])
q(407, S8, "The IOC for pilocytic astrocytoma is:", "MRI", ["CT", ["PET"] , "X-ray"])
q(407, S8, "Pilocytic astrocytoma is managed by:", "Excision of lesion", ["RT alone", ["Chemo alone"] , "Observation"])
q(407, S8, "GBM shows:", "Rapid progression", ["Slow progression", ["Static course"] , "Spontaneous regression"])
q(407, S8, "GBM carries the:", "Worst prognosis", ["Best prognosis", ["Intermediate prognosis"] , "No prognostic impact"])
q(407, S8, "GBM is managed with:", "Sx → RT", ["RT alone", ["Chemo alone"] , "Sx alone"])
q(407, S8, "The drug added for GBM is:", "Oral temozolomide", ["IV cisplatin", ["Oral procarbazine only"] , "IV methotrexate"])
q(407, S8, "GBM crossing the midline is called a:", "Butterfly tumor", ["Moth tumor", ["Batswing tumor"] , "Dumbbell tumor"])
q(407, S8, "Butterfly (GBM) tumor shows:", "Hemorrhage & necrosis", ["Calcification", ["Cystic change only"] , "Fat"])
q(407, S8, "The other feature of butterfly tumor is:", "Infiltration", ["Encapsulation", ["Cleavage plane"] , "Softness"])
q(407, S8, "Oligodendroglioma most commonly occurs at age:", "40-60 years", ["10-20 years", ["20-30 years"] , ">70 years"])
q(407, S8, "MRI in oligodendroglioma characteristically shows:", "Calcifications", ["Hemorrhage", ["Fat"] , "Diffusion restriction only"])
q(407, S8, "Oligodendroglioma is confirmed by:", "HPE", ["MRI alone", ["CT alone"] , "CSF"])
q(407, S8, "Oligodendroglioma is managed with Sx → RT plus:", "Oral temozolomide", ["IV carmustine only", ["Oral lomustine only"] , "No drug"])
q(407, S8, "HPE of oligodendroglioma shows a:", "Fried egg appearance", ["Starry sky", ["Honeycomb"] , "Salt and pepper"])
q(407, S8, "The vasculature of oligodendroglioma is described as:", "Chicken wire vascularity", ["Staghorn vessels", ["Sinusoidal vessels"] , "Telangiectatic vessels"])
q(407, S8, "CT in oligodendroglioma shows:", "Intra-tumoral calcifications", ["Intra-tumoral fat", ["Intra-tumoral air"] , "No calcification"])
q(407, S8, "CNS tumors showing calcifications include medulloblastoma, oligodendroglioma and:", "Meningioma", ["GBM", ["Pilocytic astrocytoma"] , "CNS lymphoma"])

# ------------------------------------------------------------------ p408
S9 = "Ependymoma, Meningioma and Medulloblastoma"
q(408, S9, "Ependymoma occurs in:", "Children > adults", ["Adults > children", ["Equal ages"] , "Elderly only"])
q(408, S9, "Ependymoma blocks the:", "4th ventricle", ["3rd ventricle", ["Lateral ventricle"] , "Aqueduct only"])
q(408, S9, "Blocking CSF drainage by ependymoma causes:", "Hydrocephalus", ["Hydrocephalus ex vacuo", ["Pseudotumor"] , "Idiopathic ICT"])
q(408, S9, "Ependymoma spreads through CSF as:", "Drop metastasis", ["Seed metastasis", ["Lymphatic spread"] , "Hematogenous spread"])
q(408, S9, "The IOC for ependymoma is:", "MRI", ["CT", ["X-ray"] , "PET"])
q(408, S9, "HPE of ependymoma shows:", "Pseudorosettes", ["True rosettes", ["Homer-Wright rosettes"] , "Flexner-Wintersteiner rosettes"])
q(408, S9, "The rosettes of ependymoma are:", "Perivascular pseudorosettes", ["Perineuronal rosettes", ["Glandular rosettes"] , "Nuclear rosettes"])
q(408, S9, "Ependymoma is managed with surgery followed by:", "Craniospinal RT", ["Whole brain RT only", ["Focal RT only"] , "Chemo only"])
q(408, S9, "Meningiomas are:", "Extra-axial, dural based tumors", ["Intra-axial tumors", ["Ventricular tumors"] , "Skull based tumors"])
q(408, S9, "Meningioma occurs in:", "Females > males", ["Males > females", ["Equal"] , "Children only"])
q(408, S9, "Meningioma may present as:", "Asymptomatic", ["Always symptomatic", ["Apoplexy"] , "Fever"])
q(408, S9, "When symptomatic, meningioma may cause a:", "Motor deficit", ["Sensory loss only", ["Seizure only"] , "Visual loss only"])
q(408, S9, "On MRI meningioma shows the:", "Dural tail sign", ["Cortical ribbon sign", ["Empty delta sign"] , "Tram track sign"])
q(408, S9, "On imaging meningioma appears as a well encapsulated tumor:", "With dural extension", ["With brain infiltration", ["With cystic core"] , "With fat density"])
q(408, S9, "HPE of meningioma shows:", "Psammoma bodies", ["Rosenthal fibres", ["Verrocay bodies"] , "Pseudorosettes"])
q(408, S9, "Meningioma is managed by:", "Surgery", ["RT alone", ["Chemo alone"] , "Observation always"])
q(408, S9, "Medulloblastoma is the m/c 1° malignant tumor in:", "Children", ["Adults", ["Elderly"] , "Infants only"])
q(408, S9, "Peak incidence of medulloblastoma is:", "3-4 years", ["1-2 years", ["6-8 years"] , "10-12 years"])
q(408, S9, "Medulloblastoma is associated with:", "Turcot syndrome", ["Gardner syndrome", ["Lynch syndrome"] , "Peutz-Jeghers"])
q(408, S9, "Turcot syndrome is a variation of FAP with APC mutation on chromosome:", "5", ["3", ["7"] , "18"])
q(408, S9, "Medulloblastoma spreads through CSF as:", "Drop metastasis", ["Lymphatic spread", ["Direct invasion only"] , "Hematogenous spread"])
q(408, S9, "The IOC for medulloblastoma is:", "MRI", ["CT", ["X-ray"] , "Ultrasound"])
q(408, S9, "HPE of medulloblastoma shows small round blue cells plus:", "Homer-Wright rosettes", ["Pseudorosettes", ["Psammoma bodies"] , "Verrocay bodies"])
q(408, S9, "Medulloblastoma is managed with surgery followed by:", "Craniospinal RT", ["Focal RT", ["Chemo only"] , "Observation"])

# ------------------------------------------------------------------ p409
S10 = "CNS Lymphoma and Histopathological Features"
q(409, S10, "CNS lymphoma incidence is ↑ in:", "Immunocompromised patients (HIV, post-transplant)", ["Diabetics", ["Hypertensives"] , "Smokers"])
q(409, S10, "The pathology of CNS lymphoma is:", "Diffuse large B cell lymphoma (DLBCL)", ["T cell lymphoma", ["Hodgkin lymphoma"] , "Burkitt lymphoma"])
q(409, S10, "CNS lymphoma is called a ghost cell tumor because of:", "Partial regression with steroids", ["Complete regression with RT", ["Necrosis"] , "Calcification"])
q(409, S10, "CNS lymphoma is diagnosed by:", "Biopsy", ["CSF cytology only", ["MRI alone"] , "PET alone"])
q(409, S10, "CNS lymphoma is managed with:", "Chemotherapy ± surgery → RT", ["Surgery alone", ["RT alone"] , "Steroids alone"])
q(409, S10, "HPE of pilocytic astrocytoma shows Rosenthal fibres and:", "Microcysts", ["Macrocysts", ["Psammoma bodies"] , "Necrosis"])
q(409, S10, "HPE of GBM (Type 4) shows serpentine necrosis and:", "Glomeruloid bodies", ["Psammoma bodies", ["Verrocay bodies"] , "Microcysts"])
q(409, S10, "HPE of oligodendroglioma shows fried egg cells, chicken wire blood vessels and:", "Calcification", ["Necrosis", ["Rosettes"] , "Fat"])
q(409, S10, "HPE of ependymoma shows:", "Perivascular pseudorosettes", ["Homer-Wright rosettes", ["Psammoma bodies"] , "Antoni areas"])
q(409, S10, "HPE of medulloblastoma shows small round blue cells and:", "Homer Wright rosettes", ["Perivascular pseudorosettes", ["Rosenthal fibres"] , "Serpentine necrosis"])
q(409, S10, "HPE of meningioma shows:", "Psammoma bodies", ["Verrocay bodies", ["Fried egg cells"] , "Microcysts"])
q(409, S10, "HPE of schwannoma shows Antoni A, Antoni B and:", "Verrocay bodies", ["Psammoma bodies", ["Homer-Wright rosettes"] , "Glomeruloid bodies"])

# ------------------------------------------------------------------ units
def first_page(title):
    return next(x["page"] for x in Q if x["sec"] == title)

UNIT_DEFS = [
    (S1, "CVAs split into ischemic (thrombotic, embolic) and hemorrhagic (intracerebral, SAH, EDH, SDH); hypertensive intracerebral bleeds favour the basal ganglia putamen. SAH is mostly aneurysmal, and berry aneurysms — the commonest aneurysm overall, saccular and junctional, infrarenal aorta outside the cranium — arise in polycystic kidney, Ehlers-Danlos, HTN, smoking, Marfan and fibromuscular dysplasia, rupturing at the apex. On the circle of Willis the anterior communicating artery leads at 40%, then MCA 34%, ICA/posterior communicating 20% and the basilar tip 4%."),
    (S2, "SAH announces itself as a thunderclap, the worst headache of life, with neck stiffness, prodromes and no focal signs; Terson's syndrome adds vitreous hemorrhage and MCA aneurysms give retroorbital pain. NCCT is the IOC with Fischer grading, CSF tap shows xanthochromia from RBC lysis, Hunt-Hess grades neurological symptoms while WFNS grades GCS. Cerebral angiography comes first and is followed by intervention — endovascular coiling through a catheter that is withdrawn once the coil fills the sac, or surgical clipping."),
    (S3, "SAH complications are re-bleeding, hydrocephalus from blood blocking CSF flow and delayed ischemic deficits at 2-10 days from vasospasm, prevented by nimodipine; in aortic dissection esmolol controls permissive hypertension. Herniation starts when the Munroe-Kellie doctrine breaks: ↑ICT drops CPP (MAP−ICP) and triggers Cushing's reflex — ↑SBP/HTN, bradycardia with ↑EDV and ↑SV, altered breathing — raising MAP to hold CPP ≥60 mmHg. Uncal (lateral transtentorial) herniation blows the ipsilateral third nerve with contralateral posturing (Kernohan notch), central transtentorial runs coma with small pupils through decorticate-decerebrate posturing to respiratory death via the foramen magnum, subfalcine cingulate herniation under the falx causes leg posturing and ACA stroke, and cerebellar herniation adds medullary failure with coma and bilateral posturing."),
    (S4, "The Kernohan notch phenomenon is the false localizing sign: the bleeding side's uncus presses the midbrain against the contralateral notch, compressing the descending pyramidal tract there and weakening limbs ipsilateral to the bleed. ↑ICT is managed with fluids keeping CPP ≥60 and SBP >100 mmHg, avoiding dextrose, giving mannitol as an osmotic diuretic, oxygen propped up and steroids for vasogenic tumour edema. Brain abscesses reach hematogenously (parietal region, immunocompromise, cyanotic heart disease) or directly — frontal sinusitis to frontal lobe, otitis media to temporal lobe — presenting with headache, vomiting, seizures and deficits as ring-enhancing lesions on CT/MRI, treated with IV antibiotics, drainage of solitary abscesses, antibiotics plus monitoring for multiple, plus primary-cause treatment, anti-epileptics and ICT control."),
    (S5, "Spina bifida occulta is the closed defect of ≥1 vertebrae without herniation, asymptomatic apart from a dimple or tuft of hair, diagnosed on X-ray and needing nothing. Spina bifida aperta lets membranes (meningocele) or membranes plus cord (myelomeningocele, the severest NTD) herniate through the posterior arch defect; meningoceles are fluctuant CSF cysts with limb weakness and sphincter dysfunction, mapped by MRI and repaired early if leaking, infected or tethered, late if asymptomatic with normal neurology. Myelomeningoceles are prevented by periconceptional folate, risked by maternal phenytoin/valproate, share meningocele features and carry a difficult repair with poorer prognosis."),
    (S6, "Chiari I drops the cerebellar tonsils (with syringomyelia) and presents in young adults with neck pain, conservative management and only possible hydrocephalus or spina bifida; Chiari II presents in infancy with progressive hydrocephalus and respiratory distress, breaking the tectal plate and dragging inferior vermis, medulla and fourth ventricle caudally, with hydrocephalus and spina bifida rarely absent, needing hydrocephalus treatment with poor prognosis. Dandy Walker shows a hugely cystic fourth ventricle, vermian hypogenesis/agenesis and superiorly displaced tentorium and lateral sinus, giving a prominent occiput, macrocephaly and hydrocephalus on MRI/CT, treated by shunting with poor prognosis."),
    (S7, "Gliomas lead primary brain tumours ahead of meningiomas, medulloblastoma leads primary childhood malignancy, yet metastases are the commonest brain tumours overall; patients show focal deficits, seizures, morning headache and ICT vomiting, with frontal lesions causing Witzelsucht pathological joking and personality change. MRI is the IOC (PET/CT misses brain lesions); treatment mixes surgery for solitary/1-2 lesions, BBB-crossing or intrathecal chemotherapy, and whole-brain RT or gamma-knife stereotactic radiosurgery, plus ICT care. Lung cancer seeds cerebrum and breast cancer the leptomeninges; solitary mets get surgery, radiotherapy is the mainstay, leptomeningeal disease gets chemotherapy, vasogenic edema gets steroids (DOC) and seizures get antiepileptics."),
    (S8, "Astrocytomas grade I-IV as pilocytic, low-grade fibrillary, anaplastic and GBM along a progressing ladder. Pilocytic tumours of children sit as non-infiltrating mural nodules, usually posterior fossa, low grade, MRI-diagnosed and cured by excision; GBM progresses rapidly with the worst prognosis, crosses as a hemorrhagic, necrotic, infiltrating butterfly tumour and is treated by surgery, RT and oral temozolomide. Oligodendroglioma peaks at 40-60 years with calcified lesions, fried-egg cells and chicken-wire vessels, treated by surgery, RT and temozolomide; calcifying CNS tumours are medulloblastoma, oligodendroglioma and meningioma."),
    (S9, "Ependymoma, a childhood tumour, blocks the fourth ventricle causing hydrocephalus and drops CSF metastases, shows perivascular pseudorosettes and needs surgery plus craniospinal RT. Meningioma is an extra-axial dural-based tumour of women, often asymptomatic or causing motor deficit, well encapsulated with dural extension and a dural tail on MRI, psammoma bodies on HPE, cured by surgery. Medulloblastoma, the commonest primary malignant childhood tumour peaking at 3-4 years, links to Turcot syndrome (FAP variant, APC on chromosome 5), drops CSF metastases, shows small round blue cells with Homer-Wright rosettes and is treated by surgery plus craniospinal RT."),
    (S10, "CNS lymphoma strikes immunocompromised HIV and post-transplant patients as diffuse large B-cell lymphoma, regresses partly with steroids earning the ghost-cell tag, is diagnosed by biopsy and treated with chemotherapy ± surgery then RT. The histology cheat-sheet pairs pilocytic astrocytoma with Rosenthal fibres and microcysts, GBM type 4 with serpentine necrosis and glomeruloid bodies, oligodendroglioma with fried-egg cells, chicken-wire vessels and calcification, ependymoma with perivascular pseudorosettes, medulloblastoma with small round blue cells and Homer-Wright rosettes, meningioma with psammoma bodies and schwannoma with Antoni A/B and Verrocay bodies."),
]

UNITS = []
for i, (title, guide) in enumerate(UNIT_DEFS, 1):
    UNITS.append({
        "id": f"SURG-U53-{i}",
        "ch": 53,
        "n": i,
        "title": title,
        "sec": f"{title} · p{first_page(title)}",
        "qs": [x["id"] for x in Q if x["sec"] == title],
        "guide": guide,
    })

covered = [x for u in UNITS for x in u["qs"]]
assert covered == [x["id"] for x in Q]
assert len(set(covered)) == len(covered)
with open("data/ch53.json", "w", encoding="utf-8") as f:
    json.dump({"questions": Q, "units": UNITS}, f, ensure_ascii=False, indent=1)
print(f"ch53: {len(Q)} questions, {len(UNITS)} units")
