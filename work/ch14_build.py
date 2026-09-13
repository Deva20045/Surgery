#!/usr/bin/env python3
"""Build data/ch14.json for PULSE Surgery ch14 (Thyroid : Part 1, book p82-89)."""
import json

Q = []
def q(page, sec, text, opts, ans, exp):
    Q.append({"id": f"SURG-C14-{len(Q)+1:03d}", "sec": sec, "page": page,
              "q": text, "opts": opts, "ans": ans, "exp": exp})

# ---------------- p82 · ARTERIES & VEINS ----------------
q(82, "Surgical Anatomy: Arteries & Veins", "The thyroid gland is described as:",
  ["Butterfly shaped", "Horseshoe shaped", "Pear shaped", "Dumbbell shaped"], 0,
  "Butterfly shaped gland. (Book p82)")
q(82, "Surgical Anatomy: Arteries & Veins", "The superior thyroid artery arises from the external carotid and is ligated:",
  ["Close to the gland", "At its origin", "Away from the gland", "With the carotid"], 0,
  "Superior Thyroid artery: Liged close to the gland. (Book p82)")
q(82, "Surgical Anatomy: Arteries & Veins", "The inferior thyroid artery arises from:",
  ["Thyrocervical trunk (subclavian artery)", "External carotid", "Arch of aorta directly", "Brachiocephalic trunk"], 0,
  "Inferior thyroid artery from Thyrocervical trunk ← Subclavian artery. (Book p82)")
q(82, "Surgical Anatomy: Arteries & Veins", "Why are only the capsular branches of the inferior thyroid artery ligated?",
  ["To prevent devascularisation of parathyroid & hence prevent hypocalcemia", "To prevent RLN injury", "To reduce bleeding only", "To preserve the thymus"], 0,
  "Inferior thyroid artery also supplies parathyroid; only capsular branches ligated to prevent devascularisation of parathyroid & hence prevent hypocalcemia. (Book p82)")
q(82, "Surgical Anatomy: Arteries & Veins", "Arteria thyroidea ima is:",
  ["A direct branch of arch of aorta", "A branch of external carotid", "A branch of thyrocervical trunk", "A branch of internal carotid"], 0,
  "Arteria thyroidea ima: Direct branch of arch of aorta. (Book p82)")
q(82, "Surgical Anatomy: Arteries & Veins", "The superior thyroid vein drains into:",
  ["Internal jugular vein", "Left brachiocephalic vein", "External jugular vein", "SVC"], 0,
  "Superior thyroid vein → Internal jugular vein. (Book p82)")
q(82, "Surgical Anatomy: Arteries & Veins", "The FIRST vessel ligated during thyroid surgery is:",
  ["Middle thyroid vein (seen in 30%)", "Superior thyroid artery", "Inferior thyroid vein", "Inferior thyroid artery"], 0,
  "Middle thyroid vein (seen in 30%): First vessel ligated during thyroid Sx. (Book p82)")
q(82, "Surgical Anatomy: Arteries & Veins", "The inferior thyroid vein drains into:",
  ["Left brachiocephalic vein", "Internal jugular vein", "Right brachiocephalic vein", "Azygos"], 0,
  "Inferior thyroid vein → Left brachiocephalic vein. (Book p82)")

# ---------------- p82 · NERVES & BERRY'S LIGAMENT ----------------
q(82, "Nerves & Berry's Ligament", "The right recurrent laryngeal nerve winds around:",
  ["Subclavian vessels", "Arch of aorta", "Innominate artery", "Carotid bifurcation"], 0,
  "Rt recurrent laryngeal nerve: winds around subclavian vessels. (Book p82)")
q(82, "Nerves & Berry's Ligament", "The left recurrent laryngeal nerve winds around the arch of aorta and has:",
  ["A longer course", "A shorter course", "No relation to vessels", "The same course as right"], 0,
  "Lt recurrent laryngeal nerve: winds around arch of aorta; Longer course. (Book p82)")
q(82, "Nerves & Berry's Ligament", "Both recurrent laryngeal nerves pass:",
  ["Between branches of the inferior thyroid artery", "Anterior to the trachea", "Within Berry's ligament", "With the middle thyroid vein"], 0,
  "RLN passes b/w branches of inferior thyroid artery. (Book p82)")
q(82, "Nerves & Berry's Ligament", "Non recurrent laryngeal nerves are seen in what percentage of individuals?",
  ["2%", "10%", "20%", "0.2%"], 0,
  "In 2% individuals: Non recurrent laryngeal nerves. (Book p82)")
q(82, "Nerves & Berry's Ligament", "The external laryngeal nerve lies near:",
  ["The superior pole of gland", "The inferior pole", "The isthmus", "The trachea"], 0,
  "External Laryngeal Nerve Site: Near superior pole of gland. (Book p82)")
q(82, "Nerves & Berry's Ligament", "Berry's ligament is a:",
  ["Condensation of pre-tracheal fascia", "Part of carotid sheath", "Condensation of buccopharyngeal fascia", "Remnant of thyroglossal duct"], 0,
  "Berry's ligament: Condensation of pre-tracheal fascia. (Book p82)")
q(82, "Nerves & Berry's Ligament", "Berry's ligament attaches the thyroid gland to:",
  ["Trachea", "Cricoid cartilage", "Hyoid bone", "Sternohyoid"], 0,
  "Attaches thyroid gland to trachea. (Book p82)")
q(82, "Nerves & Berry's Ligament", "Thyroid swelling moves on deglutition because of:",
  ["Berry's ligament", "Strap muscles", "Carotid sheath", "Prevertebral fascia"], 0,
  "Helps in movement of thyroid swelling on deglutition. (Book p82)")
q(82, "Nerves & Berry's Ligament", "The most common site of injury of the RLN is:",
  ["Berry's ligament", "Thoracic inlet", "Carotid sheath", "Superior pole"], 0,
  "Berry's Ligament: m/c site of injury of RLN. (Book p82)")
q(82, "Nerves & Berry's Ligament", "Beahr's (recurrent laryngeal nerve) triangle helps to:",
  ["Locate RLN during Sx", "Locate superior parathyroid", "Avoid middle thyroid vein", "Find arteria thyroidea ima"], 0,
  "Recurrent laryngeal nerve triangle (Beahr's triangle): Helps to locate RLN during Sx. (Book p82)")

# ---------------- p82-83 · EXAMINATION METHODS ----------------
q(83, "Thyroid Examination & TFT", "A normal thyroid gland is:",
  ["Neither visible nor palpable", "Palpable but not visible", "Visible but not palpable", "Always palpable"], 0,
  "Normal thyroid gland: neither visible nor palpable. (Book p83)")
q(83, "Thyroid Examination & TFT", "Which is NOT a clinical method of thyroid examination?",
  ["Kocher's method", "Pizillo's method", "Lahey's method", "Crile's method"], 0,
  "Clinical methods: 1. Pizillo's; 2. Lahey's; 3. Crile's method. (Book p83)")
q(83, "Thyroid Examination & TFT", "The ideal method to look for nodularity is:",
  ["Crile's method", "Pizillo's method", "Lahey's method", "Inspection only"], 0,
  "Crile's method: Ideal method to look for nodularity. (Book p83)")
q(83, "Thyroid Examination & TFT", "The FIRST investigation done in thyroid disorders is:",
  ["Thyroid Function Tests (TFT)", "USG neck", "FNAC", "CT"], 0,
  "TFT: First investigation done. (Book p83)")
q(83, "Thyroid Examination & TFT", "The active form of thyroid hormone measured in TFT is:",
  ["T3", "T4", "TSH", "Thyroglobulin"], 0,
  "Components: T3 (active form), T4, TSH, Anti thyroid antibodies. (Book p83)")
q(83, "Thyroid Examination & TFT", "A DECREASED TSH indicates:",
  ["Hyperthyroidism", "Hypothyroidism", "Euthyroid state", "Medullary cancer"], 0,
  "TSH ↓: Hyperthyroidism; ↑: Hypothyroidism. (Book p83)")
q(83, "Thyroid Examination & TFT", "An INCREASED TSH indicates:",
  ["Hypothyroidism", "Hyperthyroidism", "Thyroiditis always", "Cancer"], 0,
  "TSH ↑: Hypothyroidism. (Book p83)")

# ---------------- p83 · USG NECK & TIRADS ----------------
q(83, "USG Neck & TIRADS", "Which USG feature suggests a BENIGN thyroid nodule?",
  ["Wider > taller", "Taller > wider", "Microcalcifications", "Infiltrative margins"], 0,
  "Benign: Iso- or hyperechoic, macrocalcifications, regular border, wider > taller, no infiltrative margins, kidney-shaped nodes, peripheral vascularity. (Book p83)")
q(83, "USG Neck & TIRADS", "Which USG feature suggests a MALIGNANT thyroid nodule?",
  ["Hypoechoic with microcalcifications", "Hyperechoic", "Regular border", "Wider > taller"], 0,
  "Malignant: Hypoechoic, microcalcifications, border irregularity, taller > wider, infiltrative margins. (Book p83)")
q(83, "USG Neck & TIRADS", "Abnormal cervical lymph nodes in malignancy are:",
  ["Round shaped with loss of fatty hilum", "Kidney shaped with fatty hilum", "Elongated", "Always calcified"], 0,
  "Abnormal cervical lymph nodes (Round shaped) Loss of fatty hilum. (Book p83)")
q(83, "USG Neck & TIRADS", "Malignant nodules show which vascularity pattern?",
  ["Increased intranodular vascularity", "Peripheral vascularity", "No vascularity", "Avascular core"], 0,
  "Malignant: Increased intranodular vascularity (benign: peripheral). (Book p83)")
q(83, "USG Neck & TIRADS", "TIRADS criteria include composition, margin, shape, echogenicity and:",
  ["Echogenic foci", "Vascularity", "Size", "Site"], 0,
  "TIRADS criteria: Composition, Margin, Shape, Echogenicity, Echogenic foci. (Book p83)")
q(84, "USG Neck & TIRADS", "TIRADS TR1 and TR2 are managed with:",
  ["No FNAC required", "FNAC required", "Surgery", "CT neck"], 0,
  "TR1 Benign, TR2 Not Suspicious → No FNAC required. (Book p84)")
q(84, "USG Neck & TIRADS", "FNAC is required for which TIRADS scores?",
  ["TR 3-5", "TR 1-2", "Only TR5", "TR 2-4"], 0,
  "TR3 mildly, TR4 moderately, TR5 highly suspicious → FNAC required. (Book p84)")

# ---------------- p84 · FNAC ----------------
q(84, "FNAC & Royal College Classification", "FNAC in thyroid disorders is IOC but CANNOT differentiate:",
  ["Follicular adenoma vs carcinoma", "Papillary vs medullary cancer", "Benign vs malignant nodes", "Cyst vs solid"], 0,
  "IOC in Thyroid disorders, but can't differentiate b/w follicular adenoma & carcinoma. (Book p84)")
q(84, "FNAC & Royal College Classification", "The needle used for thyroid FNAC is:",
  ["23-30 gauge", "16-18 gauge", "10-12 gauge", "30-32 gauge"], 0,
  "Needle used: 23 - 30 gauge. (Book p84)")
q(84, "FNAC & Royal College Classification", "Criteria for FNAC adequacy: at least how many groups of follicular cells?",
  ["6 groups with ≥10 cells each on a single slide", "3 groups with ≥5 cells", "10 groups with ≥6 cells", "1 group of 100 cells"], 0,
  "At least 6 groups of follicular cells, each group having at least 10 cells on a single slide. (Book p84)")
q(84, "FNAC & Royal College Classification", "Thy 1 and Thy 1c (non-diagnostic / non-diagnostic cystic) are managed by:",
  ["USG guided FNAC repeated", "Surgery", "Follow up", "Hemithyroidectomy"], 0,
  "Thy 1 / Thy 1c → USG guided FNAC repeated. (Book p84)")
q(84, "FNAC & Royal College Classification", "Thy 2 (non-neoplastic) is managed with:",
  ["Follow up", "Surgery", "Repeat FNAC", "RT"], 0,
  "Thy 2 → Follow up. (Book p84)")
q(84, "FNAC & Royal College Classification", "Thy 3 (follicular) is managed with:",
  ["Hemithyroidectomy", "Total thyroidectomy", "Follow up", "Repeat FNAC"], 0,
  "Thy 3 → Hemithyroidectomy. (Book p84)")
q(84, "FNAC & Royal College Classification", "Thy 4 (suspicious) and Thy 5 (malignant) are managed with:",
  ["Sx", "Follow up", "Repeat FNAC", "Antibiotics"], 0,
  "Thy 4 / Thy 5 → Sx. (Book p84)")
q(84, "FNAC & Royal College Classification", "FNNAC (Fine Needle Non Aspiration Cytology) is used in:",
  ["Superficial swellings", "Deep retrosternal goitre", "Cysts only", "Bone lesions"], 0,
  "FNNAC: Fine Needle Non Aspiration Cytology - Used in superficial swellings. (Book p84)")
q(84, "FNAC & Royal College Classification", "Thyroid FNAC is also reported using:",
  ["Bethesda Criteria", "TIRADS", "TNM", "RECIST"], 0,
  "Thyroid FNAC is also reported using Bethesda Criteria. (Book p84)")

# ---------------- p84-85 · THYROID SCAN & OTHER IMAGING ----------------
q(84, "Thyroid Scan & Imaging", "Indications for thyroid scan are ↓TSH with features of hyperthyroidism and:",
  ["Ectopic/aberrant thyroid tissue", "Hypothyroidism", "Cancer staging", "Retrosternal goitre"], 0,
  "Indications: 1. ↓ TSH with features of hyperthyroidism; 2. Ectopic/aberrant thyroid tissue. (Book p84)")
q(84, "Thyroid Scan & Imaging", "On thyroid scan, Tc99 assesses:",
  ["Uptake", "Uptake & organification", "Organification only", "Excretion"], 0,
  "Tc99 uptake assessed. (Book p84)")
q(84, "Thyroid Scan & Imaging", "I123 assesses:",
  ["Uptake & organification", "Uptake only", "Perfusion", "Size"], 0,
  "I123: uptake & organification assessed. (Book p84)")
q(85, "Thyroid Scan & Imaging", "A non functioning/COLD nodule carries what malignancy risk?",
  ["30%", "4%", "1%", "70%"], 0,
  "Non functioning/cold nodule (30% malignant). (Book p85)")
q(85, "Thyroid Scan & Imaging", "A hyperfunctioning/HOT nodule carries what malignancy risk?",
  ["4%", "30%", "50%", "10%"], 0,
  "Hyperfunctioning/hot nodule (4% malignant). (Book p85)")
q(85, "Thyroid Scan & Imaging", "Graves' disease shows on thyroid scan:",
  ["Diffuse increased uptake", "Diffuse decreased uptake", "Cold nodule", "Hot nodule"], 0,
  "Graves' disease: Diffuse ↑ uptake. (Book p85)")
q(85, "Thyroid Scan & Imaging", "Thyroiditis shows on thyroid scan:",
  ["Diffuse decreased uptake", "Diffuse increased uptake", "Solitary hot nodule", "Multiple cold nodules"], 0,
  "Thyroiditis: Diffuse ↓ uptake. (Book p85)")
q(85, "Thyroid Scan & Imaging", "Toxic nodular goitre is also called:",
  ["Plummer's disease", "Graves' disease", "Hashimoto's", "Riedel's"], 0,
  "Toxic nodular goitre (Plummer's disease). (Book p85)")
q(85, "Thyroid Scan & Imaging", "CECT neck & thorax is indicated for:",
  ["Retrosternal goitre and large malignant goitre", "All goitres", "Only thyrotoxicosis", "Thyroiditis"], 0,
  "CECT indications: 1. Retrosternal goitre; 2. Large malignant goitre. (Book p85)")
q(85, "Thyroid Scan & Imaging", "Whole body iodine scan is used in differentiated thyroid cancer:",
  ["After total thyroidectomy to look for residual recurrent disease", "Before FNAC", "For initial diagnosis", "For retrosternal goitre"], 0,
  "DTC: After total thyroidectomy to look for residual recurrent disease. (Book p85)")

# ---------------- p85 · THYROIDECTOMY INDICATIONS ----------------
q(85, "Thyroidectomy Indications", "Which is NOT an indication for thyroidectomy?",
  ["Thy 2 on FNAC", "Neoplasia", "FNAC +ve Thy 3-5", "Toxic adenoma"], 0,
  "Indications: 1. Neoplasia; 2. FNAC +ve Thy 3-5; 3. Clinical suspicion; 4. Toxic adenoma; 5. Pressure symptoms; 6. Cosmetic purpose. (Book p85)")
q(85, "Thyroidectomy Indications", "Clinical suspicion warranting thyroidectomy includes all EXCEPT:",
  ["Soft mobile nodule in a young female", "↑ Age", "Male sex", "Hard, fixed nodule"], 0,
  "Clinical suspicion: ↑ Age; male sex; Hard, fixed nodule; RLN palsy; Lymphadenopathy; Recurrent cyst. (Book p85)")
q(85, "Thyroidectomy Indications", "Which features raise clinical suspicion for thyroid cancer?",
  ["RLN palsy, lymphadenopathy, recurrent cyst", "Diffuse soft goitre", "Thyroiditis", "Family history only"], 0,
  "RLN palsy; Lymphadenopathy; Recurrent cyst (plus ↑ age, male sex, hard fixed nodule). (Book p85)")

# ---------------- p86 · TYPES OF THYROIDECTOMY ----------------
q(86, "Types of Thyroidectomy", "Hemithyroidectomy removes:",
  ["1 lobe + isthmus", "Both lobes + isthmus", "Majority of both glands", "One lobe only"], 0,
  "Hemithyroidectomy: Removal of 1 lobe + isthmus. (Book p86)")
q(86, "Types of Thyroidectomy", "Total thyroidectomy removes:",
  ["Both lobes + isthmus", "1 lobe + isthmus", "4-8 g remnant on both sides", "One lobe + subtotal other"], 0,
  "Total thyroidectomy: Removal of both lobes + isthmus. (Book p86)")
q(86, "Types of Thyroidectomy", "Subtotal thyroidectomy leaves:",
  ["4-8 g of gland on both sides", "1 lobe intact", "The isthmus only", "Nothing"], 0,
  "Subtotal: Removal of majority of both glands + isthmus; 4-8g of gland left on both sides. (Book p86)")
q(86, "Types of Thyroidectomy", "Near total thyroidectomy is also called:",
  ["Hartley Dunhill procedure", "Halstead procedure", "Joll's procedure", "Sistrunk procedure"], 0,
  "Near total thyroidectomy (Hartley Dunhill procedure). (Book p86)")
q(86, "Types of Thyroidectomy", "In the Hartley Dunhill procedure:",
  ["One side lobectomy + isthmus removal; other side subtotal lobectomy", "Both sides total", "Both sides subtotal", "Isthmus only"], 0,
  "One side: Lobectomy + isthmus removal; Other side: Subtotal lobectomy. (Book p86)")
q(86, "Types of Thyroidectomy", "Which thyroidectomy types are NOT done anymore?",
  ["Subtotal and near total", "Total and hemi", "Only total", "Hemi only"], 0,
  "Subtotal & near total: ↓ risk of recurrence but (Not done anymore). (Book p86)")
q(86, "Types of Thyroidectomy", "Incidence of hypothyroidism, RLN injury & hypoparathyroidism is:",
  ["Equal in all types of thyroidectomy", "Highest in total", "Lowest in hemi", "Only in subtotal"], 0,
  "Incidence of hypothyroidism, RLN injury & hypoparathyroidism is equal in all types of thyroidectomy. (Book p86)")

# ---------------- p86-87 · PROCEDURE & POSITION ----------------
q(86, "Procedure & Position", "The position for thyroidectomy is:",
  ["Rose/Barking Dog Position", "Lithotomy", "Prone", "Lateral"], 0,
  "Rose/Barking Dog Position. (Book p86)")
q(86, "Procedure & Position", "The 30° elevation in thyroid position gives a bloodless field by ↓ venous congestion but ↑ risk of:",
  ["Air embolism", "DVT", "Hypotension", "Bradyarrhythmia"], 0,
  "30° elevation ↓ venous congestion (bloodless field), ↑ risk of air embolism. (Book p86)")
q(86, "Procedure & Position", "Neck extension during thyroidectomy is achieved by:",
  ["Towel roll below shoulder", "Head ring", "Shoulder strap", "Prone pillow"], 0,
  "Neck extension by towel roll below shoulder. (Book p86)")
q(86, "Procedure & Position", "Joll's thyroid retractor is:",
  ["Placed on each side of thyroid gland during open Sx; not used now", "Used in MIVAT", "A self-retaining abdominal retractor", "Used for sternotomy"], 0,
  "Joll's thyroid retractor: Placed on each side of thyroid gland during open Sx; Not used now. (Book p86)")
q(87, "Procedure & Position", "The collar incision is made how far above the suprasternal notch?",
  ["2 finger breadth", "1 finger breadth", "5 cm", "At the notch"], 0,
  "Collar incision: 2 finger breadth suprasternal notch. (Book p87)")
q(87, "Procedure & Position", "After the collar incision, the next step is raising the:",
  ["Sub platysmal tunnel", "Strap muscles", "Carotid sheath", "Prevertebral fascia"], 0,
  "2. Sub platysmal tunnel. (Book p87)")
q(87, "Procedure & Position", "If strap muscles must be cut, it is done HIGH up to avoid injury to:",
  ["Ansa cervicalis", "RLN", "External laryngeal nerve", "Vagus"], 0,
  "If strap muscles are cut: Done high up (to avoid ansa cervicalis injury). (Book p87)")
q(87, "Procedure & Position", "Order of vessel ligation in thyroidectomy: middle thyroid vein, superior pole vessels, then:",
  ["Capsular branches of inferior thyroid artery", "Origin of inferior thyroid artery", "Inferior thyroid vein first", "Arteria thyroidea ima"], 0,
  "Ligate middle thyroid vein, superior pole vessels → Capsular branches of inferior thyroid artery. (Book p87)")
q(87, "Procedure & Position", "Parathyroid glands are identified intraoperatively as yellowish structures due to:",
  ["Sentinel pad of fat", "Their capsule", "Calcium content", "Adjacent thymus"], 0,
  "Parathyroid gland (yellowish, d/t sentinel pad of fat). (Book p87)")
q(87, "Procedure & Position", "After removing the thyroid, the incision is closed with insertion of:",
  ["Romovac suction drain", "Corrugated rubber", "Penrose drain", "No drain ever"], 0,
  "Close the incision & insert Romovac suction drain. (Book p87)")

# ---------------- p87-88 · MIVAT ----------------
q(87, "MIVAT", "MIVAT stands for:",
  ["Minimally Invasive Video Assisted Thyroid Sx", "Minimal Incision Video Ablation Therapy", "Minimally Invasive Vascular Access Technique", "Micro Invasive Video Assisted Tracheostomy"], 0,
  "MIVAT: Minimally Invasive Video Assisted Thyroid Sx. (Book p87)")
q(87, "MIVAT", "The most common approach in remote-access thyroid surgery is:",
  ["Trans axillary", "Trans oral robotic Sx (TORS)", "Retroauricular", "Nipple"], 0,
  "Approaches: Trans axillary: m/c; TORS; Retroauricular; Nipple. (Book p87)")
q(87, "MIVAT", "Which is NOT a remote access approach listed for thyroid surgery?",
  ["Transumbilical", "Trans axillary", "Retroauricular", "Nipple"], 0,
  "Approaches: Trans axillary (m/c), Trans oral robotic Sx (TORS), Retroauricular, Nipple. (Book p87)")
q(88, "MIVAT", "Indications of MIVAT include:",
  ["<3cm nodule, T1 papillary thyroid cancer, parathyroid adenomas", "Large tumors", "Thyroiditis", "Retrosternal goitre"], 0,
  "Indications: <3cm nodule; T1 Papillary thyroid cancer; Parathyroid adenomas. (Book p88)")
q(88, "MIVAT", "Contraindications of MIVAT are:",
  ["Large tumor and thyroiditis", "Small nodule", "T1 papillary cancer", "Parathyroid adenoma"], 0,
  "C/I: Large tumor; Thyroiditis. (Book p88)")

# ---------------- p88 · COMPLICATIONS: HEMORRHAGE & NERVES ----------------
q(88, "Complications: Hemorrhage & Nerves", "Reactionary hemorrhage after thyroid surgery occurs:",
  ["Few hours after Sx", "During Sx", "After 7 days", "After 1 month"], 0,
  "Types: 1° during Sx; Reactionary: Few hours after Sx. (Book p88)")
q(88, "Complications: Hemorrhage & Nerves", "Incidence of nerve injury in thyroid surgery is:",
  ["2-10%", "20-30%", "0-1%", "50%"], 0,
  "Injury to nerves: Incidence: 2-10%. (Book p88)")
q(88, "Complications: Hemorrhage & Nerves", "Nerve injury during thyroid surgery is prevented by:",
  ["Nerve monitoring", "Big incisions", "Routine strap muscle cut", "Drains"], 0,
  "Prevention: Nerve monitoring. (Book p88)")
q(88, "Complications: Hemorrhage & Nerves", "The MOST common nerve injury (often unnoticed) is to the:",
  ["External laryngeal nerve", "Recurrent laryngeal nerve", "Vagus", "Ansa cervicalis"], 0,
  "External laryngeal nerve: m/c, but goes unnoticed. (Book p88)")
q(88, "Complications: Hemorrhage & Nerves", "The external laryngeal nerve supplies:",
  ["Cricothyroid", "All larynx muscles", "Sensory supply of larynx", "Strap muscles"], 0,
  "External laryngeal nerve muscles supplied: Cricothyroid. (Book p88)")
q(88, "Complications: Hemorrhage & Nerves", "Unilateral external laryngeal nerve injury causes:",
  ["Hoarseness", "Aspiration", "Stridor", "Aphonia"], 0,
  "ELN U/L: Hoarseness; B/L: Aspiration; Not life threatening (NLT). (Book p88)")
q(88, "Complications: Hemorrhage & Nerves", "Bilateral external laryngeal nerve injury causes:",
  ["Aspiration", "Hoarseness only", "Stridor", "Aphonia"], 0,
  "ELN B/L: Aspiration (NLT). (Book p88)")
q(88, "Complications: Hemorrhage & Nerves", "The RLN supplies:",
  ["All muscles of larynx except cricothyroid + sensory supply of larynx", "Only cricothyroid", "Only sensory", "Strap muscles"], 0,
  "RLN: All muscles of larynx except cricothyroid; Sensory supply of larynx. (Book p88)")
q(88, "Complications: Hemorrhage & Nerves", "Unilateral RLN injury causes hoarseness; the patient:",
  ["Can speak (not life threatening)", "Cannot speak at all", "Develops stridor", "Aspirates always"], 0,
  "RLN U/L: Hoarseness: Patient can speak (NLT). (Book p88)")
q(88, "Complications: Hemorrhage & Nerves", "Bilateral RLN injury causes:",
  ["Aphonia, stridor, aspiration (life threatening)", "Hoarseness only", "No symptoms", "Cough only"], 0,
  "RLN B/L: Aphonia, Stridor, Aspiration (↓ sensation) - LT. (Book p88)")

# ---------------- p88-89 · RESPIRATORY DISTRESS & HYPOPARATHYROIDISM ----------------
q(88, "Respiratory Distress & Hypoparathyroidism", "The most common cause of post operative respiratory distress after thyroidectomy is:",
  ["Laryngeal edema", "Tension haematoma", "Laryngomalacia", "B/L RLN injury"], 0,
  "Causes: a. Laryngeal edema: m/c. (Book p88)")
q(88, "Respiratory Distress & Hypoparathyroidism", "Tension haematoma causing respiratory distress is due to:",
  ["Reactionary hemorrhage → tense swelling pressing on trachea", "Laryngeal edema", "Tracheal collapse", "Pneumothorax"], 0,
  "Reactionary hemorrhage → Tense swelling pressing on trachea. (Book p88)")
q(88, "Respiratory Distress & Hypoparathyroidism", "Immediate management of tension haematoma is:",
  ["Open the sutures, evacuate the hematoma, ligate bleeding vessels in the OT", "Intubate and observe", "Needle aspiration only", "IV antibiotics"], 0,
  "Mx: Open the sutures; Evacuate the hematoma; Ligate bleeding vessels in the OT. (Book p88)")
q(88, "Respiratory Distress & Hypoparathyroidism", "Laryngomalacia after thyroidectomy is due to:",
  ["Removal of long standing thyroid swelling → tracheal rings collapse", "RLN injury", "Edema", "Hematoma"], 0,
  "Removal of long standing thyroid swelling → tracheal rings collapse. (Book p88)")
q(88, "Respiratory Distress & Hypoparathyroidism", "Laryngomalacia is prevented by:",
  ["Adequate examination of larynx & vocal cords before Sx", "Routine intubation", "Steroids", "Smaller incision"], 0,
  "Prevention: Adequate examination of larynx & vocal cords before sx. (Book p88)")
q(89, "Respiratory Distress & Hypoparathyroidism", "Hypoparathyroidism as a complication appears as a LATE cause at:",
  ["48-72 hrs after Sx", "6 hrs", "1 week", "1 month"], 0,
  "Hypoparathyroidism: Late cause: 48-72 hrs after sx. (Book p89)")
q(89, "Respiratory Distress & Hypoparathyroidism", "The other late complications listed are:",
  ["Keloid and recurrence", "Hemorrhage", "Air embolism", "Ansa cervicalis injury"], 0,
  "4. Keloid; 5. Recurrence. (Book p89)")

# ---------------- p89 · HYPOPARATHYROIDISM ----------------
q(89, "Hypoparathyroidism", "The most common cause of hypoparathyroidism after thyroid surgery is vascular insult via:",
  ["Inferior thyroid artery", "Superior thyroid artery", "Middle thyroid vein", "Arteria thyroidea ima"], 0,
  "Cause: Vascular insult to parathyroid glands: inferior thyroid artery: m/c. (Book p89)")
q(89, "Hypoparathyroidism", "Symptoms of hypoparathyroidism start at:",
  ["48-72 hrs after Sx", "Immediately in OT", "1 week", "6 hours"], 0,
  "Start 48-72 hrs after Sx. (Book p89)")
q(89, "Hypoparathyroidism", "The EARLIEST symptom of hypoparathyroidism is:",
  ["Perioral numbness", "Tetany", "Respiratory distress", "Carpopedal spasm"], 0,
  "Earliest: Perioral numbness → tingling/paresthesia → Tetany → Respiratory distress (Cause of death). (Book p89)")
q(89, "Hypoparathyroidism", "The cause of death in untreated hypoparathyroidism is:",
  ["Respiratory distress", "Cardiac arrest from hypercalcemia", "Hemorrhage", "Sepsis"], 0,
  "Tetany → Respiratory distress (Cause of death). (Book p89)")
q(89, "Hypoparathyroidism", "Chvostek sign is:",
  ["Twitching of facial muscles on tapping over facial nerve", "Carpopedal spasm", "Hand spasm with BP cuff", "Numbness of lips"], 0,
  "Chvostek sign: Twitching of facial muscles on tapping over facial nerve. (Book p89)")
q(89, "Hypoparathyroidism", "Trousseau sign is:",
  ["Carpopedal spasm/obstetrician's hand; hand spasm when BP cuff inflated above systolic BP", "Facial twitching on tapping", "Knee jerk loss", "Papilledema"], 0,
  "Trousseau sign (Carpopedal spasm)/Obstetrician's hand: Spasm of hand when BP cuff inflated above systolic BP. (Book p89)")
q(89, "Hypoparathyroidism", "Trousseau sign indicates:",
  ["Neuromuscular hyperexcitability (hypocalcemia & hypoparathyroidism)", "Hypokalemia", "Hypercalcemia", "Neuropathy"], 0,
  "D/t neuromuscular hyperexcitability; Seen in hypocalcemia & hypoparathyroidism. (Book p89)")
q(89, "Hypoparathyroidism", "Monitoring in hypoparathyroidism uses S. calcium (ionized > total) and S. PTH whose half life is:",
  ["7 minutes", "7 hours", "7 days", "70 minutes"], 0,
  "S. PTH (1/2 life: 7 minutes). (Book p89)")
q(89, "Hypoparathyroidism", "Major symptoms or S.Ca2+ <8 mg/dl is treated with:",
  ["I/V Calcium gluconate + oral Ca2+ + oral Vit D3", "Oral Ca only", "Observation", "IV magnesium"], 0,
  "Major symptoms or S.Ca2+ <8mg/dl → I/V Calcium gluconate + oral Ca2+ + oral Vit D3. (Book p89)")
q(89, "Hypoparathyroidism", "Minor symptoms with S.Ca2+ >8 mg/dl are treated with:",
  ["Oral Ca2+ + oral Vit D3", "IV calcium gluconate", "IV PTH", "Dialysis"], 0,
  "Minor symptoms & S.Ca2+ >8mg/dl → Oral Ca2+ + oral Vit D3. (Book p89)")
q(89, "Hypoparathyroidism", "Permanent hypoparathyroidism (due to removal of parathyroid glands) occurs in about:",
  ["1% cases, symptoms last >1 year", "10% cases", "50% cases", "0.01%"], 0,
  "Permanent hypoparathyroidism: D/t removal of parathyroid glands; 1% cases; Symptoms last >1 year. (Book p89)")

# ---------------- units ----------------
def sec_ids(*labels):
    return [x["id"] for x in Q if x["sec"] in labels]

def first_page(label):
    for x in Q:
        if x["sec"] == label:
            return x["page"]
    return 0

UNIT_DEFS = [
    ("Surgical Anatomy: Arteries & Veins", ("Surgical Anatomy: Arteries & Veins",),
     "Butterfly gland: superior thyroid artery (external carotid) ligated close to the gland; inferior thyroid artery (thyrocervical trunk) feeds parathyroids too, so only capsular branches are tied to dodge hypocalcemia; arteria thyroidea ima sprouts from the aortic arch. Veins: superior → IJV, middle (30%, first ligated) → IJV, inferior → left brachiocephalic."),
    ("Nerves & Berry's Ligament", ("Nerves & Berry's Ligament",),
     "Right RLN loops the subclavian vessels, left the aortic arch (longer course); both run between inferior thyroid artery branches, and 2% of people have non-recurrent nerves. The external laryngeal nerve hugs the superior pole. Berry's ligament - pre-tracheal fascia condensing onto trachea - makes the gland move on swallowing and is the m/c site of RLN injury; Beahr's triangle locates the RLN."),
    ("Thyroid Examination & TFT", ("Thyroid Examination & TFT",),
     "Normal thyroid is neither visible nor palpable; examine by Pizillo's, Lahey's or Crile's (best for nodularity). TFT is the first test - T3 the active hormone - with TSH down in hyper- and up in hypothyroidism."),
    ("USG Neck & TIRADS", ("USG Neck & TIRADS",),
     "Benign nodules are iso/hyperechoic, macrocalcified, regular, wider-than-taller with peripheral flow and kidney-shaped nodes; malignancy flips every feature (hypoechoic, microcalcifications, taller-than-wide, infiltrative, round nodes losing fatty hilum, intranodular flow). TIRADS scores composition, margin, shape, echogenicity, echogenic foci: TR1-2 need no FNAC, TR3-5 do."),
    ("FNAC & Royal College Classification", ("FNAC & Royal College Classification",),
     "FNAC is IOC with a 23-30G needle and needs 6 groups of ≥10 follicular cells, yet cannot split follicular adenoma from carcinoma. Royal College: Thy1/1c repeat USG-FNAC, Thy2 follow up, Thy3 hemithyroidectomy, Thy4/5 surgery; FNNAC serves superficial swellings and Bethesda also reports thyroid FNAC."),
    ("Thyroid Scan & Imaging", ("Thyroid Scan & Imaging",),
     "Scan when TSH is low with thyrotoxic features or for ectopic tissue: Tc99 reads uptake, I123 uptake plus organification. Cold nodules are 30% malignant vs 4% hot; Graves' lights up diffusely, thyroiditis stays dark, Plummer's shows toxic nodular goitre. CECT for retrosternal/large malignant goitre; whole-body iodine scan hunts residual DTC after total thyroidectomy."),
    ("Thyroidectomy Indications", ("Thyroidectomy Indications",),
     "Operate for neoplasia, FNAC Thy3-5, clinical suspicion (age, male, hard fixed nodule, RLN palsy, lymphadenopathy, recurrent cyst), toxic adenoma, pressure symptoms or cosmetics."),
    ("Types of Thyroidectomy", ("Types of Thyroidectomy",),
     "Hemi = lobe + isthmus; total = both lobes + isthmus; subtotal leaves 4-8 g each side and near-total (Hartley Dunhill) does lobectomy + isthmus one side with subtotal lobectomy opposite - the last two are retired. Hypothyroidism, RLN injury and hypoparathyroidism rates are equal across all types."),
    ("Procedure & Position", ("Procedure & Position",),
     "Rose/barking-dog position: 30° head-up for a bloodless field at the price of air embolism risk, neck extended on a towel roll. Collar incision two finger-breadths above the sternal notch, subplatysmal tunnel, strap muscles cut high to spare ansa cervicalis; ligate middle vein, superior pole vessels then capsular inferior artery branches; parathyroids glow yellowish via sentinel fat; finish with a Romovac drain. Joll's retractor is history."),
    ("MIVAT", ("MIVAT",),
     "Minimally Invasive Video Assisted Thyroid Sx suits <3 cm nodules, T1 papillary cancers and parathyroid adenomas but not large tumors or thyroiditis; remote access routes: trans-axillary (m/c), TORS, retroauricular, nipple."),
    ("Complications: Hemorrhage & Nerves", ("Complications: Hemorrhage & Nerves",),
     "Primary bleeding is intra-op, reactionary hours later. Nerve injury 2-10%, prevented by monitoring: external laryngeal (cricothyroid) is m/c but silent - U/L hoarseness, B/L aspiration, never fatal; RLN U/L hoarseness with preserved speech, B/L aphonia-stridor-aspiration and life threatening."),
    ("Respiratory Distress & Hypoparathyroidism", ("Respiratory Distress & Hypoparathyroidism",),
     "Post-op distress: laryngeal edema m/c, tension haematoma (open sutures, evacuate, ligate in OT), laryngomalacia from collapsed tracheal rings after long goitres (pre-op laryngoscopy prevents), B/L RLN injury; hypoparathyroidism is the late 48-72 h cause, plus keloid and recurrence."),
    ("Hypoparathyroidism", ("Hypoparathyroidism",),
     "Vascular insult via the inferior thyroid artery starves parathyroids; perioral numbness at 48-72 h escalates to tingling, tetany and fatal respiratory distress. Chvostek = facial tap twitching; Trousseau = carpopedal/obstetric hand with cuff above systolic. Watch ionized Ca and PTH (t½ 7 min): <8 mg/dl or major symptoms → IV calcium gluconate plus oral Ca/D3, otherwise oral; permanent form (glands removed) hits 1% and lasts >1 year."),
]

UNITS = []
for i, (title, labels, guide) in enumerate(UNIT_DEFS, 1):
    UNITS.append({"id": f"SURG-U14-{i}", "ch": 14, "n": i, "title": title,
                  "sec": f"{labels[0]} · p{first_page(labels[0])}",
                  "qs": sec_ids(*labels), "guide": guide})

covered = [i for u in UNITS for i in u["qs"]]
assert covered == [x["id"] for x in Q], "units must cover questions in order"

data = {"questions": Q, "units": UNITS}
with open("data/ch14.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
print(f"ch14: {len(Q)} questions, {len(UNITS)} units")
