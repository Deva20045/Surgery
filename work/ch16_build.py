#!/usr/bin/env python3
"""Build data/ch16.json for PULSE Surgery ch16 (Thyroid : Part 3, book p102-110)."""
import json

Q = []
def q(page, sec, text, opts, ans, exp):
    Q.append({"id": f"SURG-C16-{len(Q)+1:03d}", "sec": sec, "page": page,
              "q": text, "opts": opts, "ans": ans, "exp": exp})

# ---------------- p102 · EMBRYOLOGY & LINGUAL THYROID ----------------
q(102, "Thyroid Embryology & Lingual Thyroid", "The thyroid gland descends from the tongue starting at:",
  ["Foramen caecum", "Tip of tongue", "Vallate papillae", "Root of tongue lateral margin"], 0,
  "Embryology: foramen caecum (posterior 1/3rd tongue) → thyroglossal tract → thyroid gland; tract obliterates. (Book p102)")
q(102, "Thyroid Embryology & Lingual Thyroid", "The foramen caecum lies at the junction of:",
  ["Anterior 2/3rd and posterior 1/3rd of tongue", "Anterior 1/3rd and posterior 2/3rd", "Two halves of tongue", "Tongue and floor of mouth"], 0,
  "Foramen caecum between anterior 2/3rd and posterior 1/3rd of tongue. (Book p102)")
q(102, "Thyroid Embryology & Lingual Thyroid", "Lingual thyroid is:",
  ["Undescended thyroid tissue just below the tongue", "A persistent thyroglossal tract", "Ectopic ovarian thyroid", "A lateral neck swelling"], 0,
  "Lingual thyroid: undescended thyroid tissue; site just below the tongue. (Book p102)")
q(102, "Thyroid Embryology & Lingual Thyroid", "On clinical examination of lingual thyroid, the swelling causes:",
  ["Tongue lifted up", "Tongue deviated laterally", "Tracheal deviation", "Dysphagia lusoria"], 0,
  "C/F: swelling → tongue lifted up. (Book p102)")
q(102, "Thyroid Embryology & Lingual Thyroid", "Before excising a lingual thyroid, USG neck is done to:",
  ["Check for normal thyroid tissue in the neck", "Stage a cancer", "Measure the swelling", "Guide FNAC"], 0,
  "Ix: FNAC shows thyroid tissue; USG neck before Sx to check for normal thyroid tissue. (Book p102)")
q(102, "Thyroid Embryology & Lingual Thyroid", "After excision of a lingual thyroid that was the only thyroid tissue, the patient needs:",
  ["Thyroxine supplementation", "Radioiodine", "Steroids", "Nothing"], 0,
  "Mx: excision + thyroxine supplementation if it is the only thyroid tissue. (Book p102)")

# ---------------- p102-103 · THYROGLOSSAL CYST: DX, MX & COMPLICATIONS ----------------
q(102, "Thyroglossal Cyst: Dx, Mx & Complications", "A thyroglossal cyst is due to:",
  ["Persistent thyroglossal tract", "Undescended thyroid tissue", "A branchial arch remnant", "Blocked lymphatic"], 0,
  "Etiology: persistent thyroglossal tract. (Book p102)")
q(102, "Thyroglossal Cyst: Dx, Mx & Complications", "The most common site of a thyroglossal cyst is:",
  ["Subhyoid", "Suprahyoid", "At the tongue base", "Intrathoracic"], 0,
  "Site: subhyoid (m/c). (Book p102)")
q(102, "Thyroglossal Cyst: Dx, Mx & Complications", "A thyroglossal cyst presents as a midline neck swelling that moves with:",
  ["Deglutition AND protrusion of tongue", "Deglutition only", "Protrusion of tongue only", "Respiration only"], 0,
  "Midline neck swelling: moves with deglutition & protrusion of tongue. (Book p102)")
q(102, "Thyroglossal Cyst: Dx, Mx & Complications", "The Sistrunk procedure removes:",
  ["Cyst + part of hyoid bone + tract till base of tongue", "Cyst only", "Cyst + whole hyoid + sternum", "Cyst + thyroid isthmus"], 0,
  "Sistrunk: removal of cyst + part of hyoid bone + tract till base of tongue. (Book p102)")
q(102, "Thyroglossal Cyst: Dx, Mx & Complications", "Incision & drainage of a thyroglossal cyst is never done because it leads to:",
  ["Thyroglossal fistula", "Malignant change", "Hypothyroidism", "Airway obstruction"], 0,
  "Incision & drainage → thyroglossal fistula: NEVER done. (Book p102)")
q(102, "Thyroglossal Cyst: Dx, Mx & Complications", "Complications of a thyroglossal cyst include thyroglossal fistula and:",
  ["Papillary thyroid carcinoma (long standing cases)", "Follicular carcinoma", "Medullary carcinoma", "Anaplastic carcinoma"], 0,
  "Complications: 1. Thyroglossal fistula (mx: Sistrunk); 2. Papillary thyroid carcinoma in long standing cases. (Book p102)")
q(103, "Thyroglossal Cyst: Dx, Mx & Complications", "An inflamed thyroglossal cyst can lead to:",
  ["Fistula", "Carcinoma", "Hypothyroidism", "Lingual thyroid"], 0,
  "Inflamed thyroglossal cyst can lead to fistula. (Book p103)")
q(103, "Thyroglossal Cyst: Dx, Mx & Complications", "Thyroglossal vs branchial fistula: thyroglossal is midline and always acquired; branchial fistula lies:",
  ["Lower 1/3rd along sternocleidomastoid; congenital/acquired", "Upper 1/3rd along trapezius; always acquired", "Midline; congenital", "Behind the ear; acquired"], 0,
  "Branchial fistula: lower 1/3rd along sternocleidomastoid; congenital/acquired (thyroglossal: midline, always acquired). (Book p103)")

# ---------------- p103 · HYPERTHYROIDISM: FEATURES & CAUSES ----------------
q(103, "Hyperthyroidism: Features & Causes", "Clinical features of hyperthyroidism include all EXCEPT:",
  ["Weight gain", "Weight loss despite good appetite", "Tachycardia", "Heat intolerance"], 0,
  "Features: thin irritable patient, weight loss DESPITE good appetite, tachycardia, diarrhoea, tremors, heat intolerance, oligomenorrhea. (Book p103)")
q(103, "Hyperthyroidism: Features & Causes", "The most common cause of hyperthyroidism with diffuse ↑ uptake on thyroid scan is:",
  ["Graves' disease", "Plummer's disease", "Toxic nodular goitre", "Struma ovarii"], 0,
  "Graves' disease: m/c; diffuse ↑ uptake. (Book p103)")
q(103, "Hyperthyroidism: Features & Causes", "Solitary toxic nodule/Plummer's disease shows on thyroid scan:",
  ["↑ single hot nodule", "Diffuse ↑", "Multiple hot nodules", "↓ uptake"], 0,
  "Solitary toxic nodule/Plummer's: ↑ single hot nodule. (Book p103)")
q(103, "Hyperthyroidism: Features & Causes", "Toxic nodular goitre shows on scan:",
  ["↑ multiple hot nodules", "Single hot nodule", "Diffuse uptake", "Cold nodules only"], 0,
  "Toxic nodular goitre: ↑ multiple hot nodules. (Book p103)")
q(103, "Hyperthyroidism: Features & Causes", "Factitious hyperthyroidism (↑ exogenous intake) shows on thyroid scan:",
  ["↓ uptake", "↑ diffuse", "Single hot nodule", "Multiple hot nodules"], 0,
  "Factitious hyperthyroidism: ↓ uptake (so does struma ovarii - ectopic thyroid in ovary). (Book p103)")
q(103, "Hyperthyroidism: Features & Causes", "Jod-Basedow phenomenon is:",
  ["Iodine induced hyperthyroidism", "Iodine induced hypothyroidism", "Amiodarone hypothyroidism", "Post-partum thyrotoxicosis"], 0,
  "Jod-Basedow phenomenon: I2 induced hyperthyroidism (↑ uptake). (Book p103)")
q(103, "Hyperthyroidism: Features & Causes", "A TSH secreting pituitary adenoma causes hyperthyroidism with:",
  ["↑ TSH and ↑ uptake", "↓ TSH", "↓ uptake", "Normal TSH"], 0,
  "TSH secreting pituitary adenoma: ↑ TSH, ↑ uptake. (Book p103)")
q(103, "Hyperthyroidism: Features & Causes", "Struma ovarii is:",
  ["Ectopic thyroid tissue in ovary (↓ neck uptake)", "Ovarian metastasis of thyroid cancer", "A thyroid teratoma", "Hyperthyroidism of pregnancy"], 0,
  "Struma ovarii: ectopic thyroid tissue in ovary; neck scan ↓. (Book p103)")

# ---------------- p103-104 · ANTITHYROID DRUGS & PRE-OP PREPARATION ----------------
q(103, "Antithyroid Drugs & Pre-op Preparation", "The antithyroid drugs are:",
  ["Propylthiouracil (PTU) and carbimazole", "Thyroxine and liothyronine", "Propranolol and nadolol", "Steroids"], 0,
  "Drugs only: 1. PTU; 2. carbimazole. (Book p103)")
q(103, "Antithyroid Drugs & Pre-op Preparation", "Mechanism of PTU/carbimazole includes:",
  ["(-) thyroid peroxidase enzyme and blocking T4 → T3", "Blocking TSH receptors", "Destroying follicles", "Inhibiting iodine uptake only"], 0,
  "Mechanism: (-) thyroid peroxidase enzyme; T4 →(-) T3 (PTU also blocks peripheral conversion). (Book p103)")
q(103, "Antithyroid Drugs & Pre-op Preparation", "The antithyroid drug safe in 1st trimester of pregnancy & lactation is:",
  ["PTU", "Carbimazole", "Radioiodine", "Aspirin"], 0,
  "PTU safe in 1st trimester of pregnancy & lactation. (Book p103)")
q(103, "Antithyroid Drugs & Pre-op Preparation", "The important side effect of antithyroid drugs and its 1st sign are:",
  ["Agranulocytosis; sore throat", "Hepatitis; jaundice", "Rash; itching", "Anemia; pallor"], 0,
  "S/E: agranulocytosis; 1st sign: sore throat. (Book p103)")
q(104, "Antithyroid Drugs & Pre-op Preparation", "Radioiodine ablation for hyperthyroidism uses I-131 which:",
  ["Acts via β rays; t½ 7-8 days", "Acts via α rays; t½ 7 days", "Acts via γ rays; t½ 8 days", "Acts via β rays; t½ 70 days"], 0,
  "RIA: I131 acts via β rays; t½ 7-8 days. (Book p104)")
q(104, "Antithyroid Drugs & Pre-op Preparation", "Antithyroid drugs are started how many weeks before surgery?",
  ["6-8 weeks", "1-2 weeks", "3-4 days", "6 months"], 0,
  "Start antithyroid drugs 6-8 wks before Sx. (Book p104)")
q(104, "Antithyroid Drugs & Pre-op Preparation", "The long acting β blocker given prior to thyroid surgery is:",
  ["Nadolol", "Propranolol", "Atenolol", "Metoprolol"], 0,
  "Nadolol OD (long acting β blocker) prior to Sx. (Book p104)")
q(104, "Antithyroid Drugs & Pre-op Preparation", "Nadolol is continued for 7 days post Sx because:",
  ["Half life of T3 is 7 days", "Half life of T4 is 7 days", "It prevents wound infection", "It prevents hypocalcemia"], 0,
  "Continue 7 days post Sx (half life of T3: 7 days); advantage ↑ sympathetic outflow control; last dose evening before Sx. (Book p104)")
q(104, "Antithyroid Drugs & Pre-op Preparation", "The last dose of β blocker before thyroid surgery is given:",
  ["Evening before Sx", "Morning of Sx", "3 days before", "Not stopped at all"], 0,
  "Last dose: evening before Sx. (Book p104)")
q(104, "Antithyroid Drugs & Pre-op Preparation", "Drugs before thyroid surgery aim to:",
  ["Achieve euthyroid state (prevent thyroid storm)", "Shrink the gland only", "Reduce vascularity only", "Prevent hypocalcemia"], 0,
  "Drugs: to achieve euthyroid state (prevent thyroid storm). (Book p104)")

# ---------------- p104 · THYROID STORM ----------------
q(104, "Thyroid Storm", "Thyroid storm is:",
  ["Uncontrolled thyrotoxicosis", "Controlled hypothyroidism", "A variant of Hashimoto's", "Post-op hypocalcemia"], 0,
  "Thyroid storm: uncontrolled thyrotoxicosis. (Book p104)")
q(104, "Thyroid Storm", "The most common etiology of thyroid storm is:",
  ["Inadequately prepared patient", "Upper respiratory tract infection", "FNAC", "Anaesthetic agents"], 0,
  "Etiology: inadequately prepared patient (m/c); URTI; interventions (FNAC); Sx trauma; anaesthetic agents. (Book p104)")
q(104, "Thyroid Storm", "The leading cause of death in thyroid storm is:",
  ["Arrhythmia (from palpitations)", "Dehydration", "Hyperthermia", "Hypertension"], 0,
  "Features: dehydration, hyperthermia, HTN crisis, palpitations → arrhythmia (leading cause of death). (Book p104)")
q(104, "Thyroid Storm", "Aggressive IV fluid therapy in thyroid storm prevents dehydration and:",
  ["Acute tubular necrosis", "Heart block", "Hypocalcemia", "Pulmonary fibrosis"], 0,
  "Aggressive IV fluids: prevent dehydration & acute tubular necrosis. (Book p104)")
q(104, "Thyroid Storm", "Hyperthermia in thyroid storm is managed with:",
  ["Cold fluids/packs", "Antipyretics only", "Warm blankets", "Dantrolene"], 0,
  "Hyperthermia: cold fluids/packs. (Book p104)")
q(104, "Thyroid Storm", "The large-dose β blocker used in thyroid storm is:",
  ["Propranolol", "Nadolol", "Atenolol", "Carvedilol"], 0,
  "Mx: IV steroid & antibiotics; large dose β blockers (propranolol); PTU/carbimazole. (Book p104)")
q(104, "Thyroid Storm", "Which drug must be AVOIDED in thyroid storm as it worsens the condition?",
  ["Aspirin", "PTU", "Propranolol", "Steroids"], 0,
  "Avoid aspirin (worsens the condition). (Book p104)")

# ---------------- p104-105 · GRAVES: BASICS & EYE SIGNS ----------------
q(104, "Graves: Basics & Eye Signs", "Graves' disease is:",
  ["Autoimmune condition (female > male), m/c cause of hyperthyroidism", "A viral thyroiditis", "Iodine deficiency disease", "A pituitary adenoma"], 0,
  "Autoimmune (female > male); m/c cause of hyperthyroidism. (Book p104)")
q(104, "Graves: Basics & Eye Signs", "The etiology of Graves' disease is:",
  ["Thyroid receptor antibodies (TRAb) - stimulating antibodies", "Blocking TSH antibodies", "Anti-TPO antibodies", "Anti-thyroglobulin"], 0,
  "TRAb: stimulating antibodies (earlier called LATS: long acting thyroid stimulating antibodies). (Book p104)")
q(104, "Graves: Basics & Eye Signs", "The dermopathy of Graves' disease is:",
  ["Pretibial myxedema", "Erythema nodosum", "Acanthosis nigricans", "Vitiligo"], 0,
  "Dermopathy: pretibial myxedema. (Book p104)")
q(105, "Graves: Basics & Eye Signs", "Graves' disease is associated with:",
  ["Pernicious anemia & myasthenia gravis", "Addison's only", "Diabetes insipidus", "Celiac disease"], 0,
  "Associations: pernicious anemia; myasthenia gravis. (Book p105)")
q(105, "Graves: Basics & Eye Signs", "Thyroid acropachy refers to:",
  ["Subperiosteal bone formation", "Joint effusions", "Osteoporosis", "Pathological fractures"], 0,
  "Thyroid acropachy: subperiosteal bone formation. (Book p105)")
q(105, "Graves: Basics & Eye Signs", "Exophthalmos in Graves' shows:",
  ["Upper sclera is visible", "Lower sclera hidden", "Conjunctival pallor", "Miosis"], 0,
  "Exophthalmos: upper sclera is visible. (Book p105)")
q(105, "Graves: Basics & Eye Signs", "Von Graefe's sign and Dalrymple's sign (lid lag & lid retraction) are due to:",
  ["Spasm of Muller's muscle", "Weakness of orbicularis oculi", "Edema of lids", "Fibrosis of levator"], 0,
  "Von Graefe (lid lag) & Dalrymple (lid retraction): d/t spasm of Muller muscle. (Book p105)")
q(105, "Graves: Basics & Eye Signs", "Muller's muscle is the:",
  ["Autonomic component of LPS", "Skeletal component of LPS", "Muscle of the lower lid", "Extraocular muscle"], 0,
  "Muller's muscle → autonomic component of LPS. (Book p105)")
q(105, "Graves: Basics & Eye Signs", "Joffroy's sign is:",
  ["Absence of forehead wrinkling when patient looks up", "Lid lag on looking down", "Infrequent blinking", "Loss of accommodation"], 0,
  "Joffroy's sign: absence of forehead wrinkling when patient looks up. (Book p105)")
q(105, "Graves: Basics & Eye Signs", "Moebius sign (sign of severe toxicity) is:",
  ["Loss of accommodation reflex", "Infrequent blinking", "Lid retraction", "Absent corneal reflex"], 0,
  "Moebius sign (severe toxicity): loss of accommodation reflex. (Book p105)")
q(105, "Graves: Basics & Eye Signs", "Stellwag sign (sign of mild toxicity) is:",
  ["Infrequent blinking/staring look", "Loss of convergence", "Lid lag", "Proptosis"], 0,
  "Stellwag sign (mild toxicity): infrequent blinking/staring look. (Book p105)")

# ---------------- p105 · GRAVES: DX & MX ----------------
q(105, "Graves: Dx & Mx", "Dx of Graves' is based on:",
  ["Clinical features + autoantibody levels", "FNAC alone", "TSH alone", "USG alone"], 0,
  "Dx based on C/F + autoantibody levels; diffuse enlargement + hyperthyroid features + eye signs. (Book p105)")
q(105, "Graves: Dx & Mx", "HPE of Graves' disease shows:",
  ["Scalloping of colloid with tall columnar cells", "Lymphocyte infiltration", "Amyloid", "Hurthle cells"], 0,
  "HPE: scalloping of colloid; tall columnar cells. (Book p105)")
q(105, "Graves: Dx & Mx", "A child with Graves' disease is treated with:",
  ["Drugs only", "Surgery", "RIA", "Steroids"], 0,
  "Child: drugs only. (Book p105)")
q(105, "Graves: Dx & Mx", "A pregnant patient with Graves' is treated with:",
  ["Drugs only: PTU", "RIA", "Surgery", "Carbimazole only"], 0,
  "Pregnant: drugs only - PTU. (Book p105)")
q(105, "Graves: Dx & Mx", "An adult Graves' patient WITHOUT goitre is managed with:",
  ["Drugs → RIA", "Drugs → Sx", "Drugs only forever", "Sx first"], 0,
  "Adult without goitre: drugs → RIA; with goitre: drugs → Sx. (Book p105)")
q(105, "Graves: Dx & Mx", "An elderly Graves' patient with comorbidities is managed with:",
  ["Drugs → RIA", "Drugs → Sx", "Observation", "Steroids"], 0,
  "Elderly with comorbidities: drugs → RIA. (Book p105)")
q(105, "Graves: Dx & Mx", "Graves' with extensive eye signs is treated with drugs → Sx because:",
  ["RIA worsens eye signs (C/I)", "Surgery cures eye signs", "Drugs worsen eye signs", "RIA causes cataract"], 0,
  "With extensive eye signs: drugs → Sx; RIA is C/I (worsens eye signs). (Book p105)")
q(105, "Graves: Dx & Mx", "The preferred surgical option in Graves' is:",
  ["Total thyroidectomy > subtotal/near total", "Hemithyroidectomy", "Isthmusectomy", "Enucleation"], 0,
  "Sx: total thyroidectomy > subtotal/near total thyroidectomy. (Book p105)")

# ---------------- p106 · PLUMMER'S & SOLITARY TOXIC NODULE ----------------
q(106, "Plummer's & Solitary Toxic Nodule", "Plummer's disease/toxic nodular goitre has female:male ratio and rank among hyperthyroidism causes of:",
  ["5:1; 2nd m/c cause", "3:1; m/c cause", "5:1; 3rd cause", "1:5; 2nd cause"], 0,
  "Plummer's: female:male 5:1; 2nd m/c cause of hyperthyroidism. (Book p106)")
q(106, "Plummer's & Solitary Toxic Nodule", "Thyroid scan in Plummer's disease/toxic nodular goitre shows:",
  ["Multiple hot & cold nodules", "Single hot nodule", "Diffuse uptake", "No uptake"], 0,
  "Scan: multiple hot & cold nodules. (Book p106)")
q(106, "Plummer's & Solitary Toxic Nodule", "Mx of Plummer's disease/toxic nodular goitre is:",
  ["Drugs → total thyroidectomy", "Drugs → RIA", "Drugs only", "Hemithyroidectomy"], 0,
  "Mx: drugs → total thyroidectomy. (Book p106)")
q(106, "Plummer's & Solitary Toxic Nodule", "A solitary toxic nodule (5th decade, female > male) shows on scan and is treated with:",
  ["Single hot nodule; drugs → RIA", "Cold nodule; Sx", "Diffuse uptake; drugs", "Multiple nodules; total thyroidectomy"], 0,
  "Solitary toxic nodule: single hot nodule; mx drugs → RIA. (Book p106)")

# ---------------- p106 · HYPOTHYROIDISM: CAUSES & FEATURES ----------------
q(106, "Hypothyroidism: Causes & Features", "The most common cause of hypothyroidism overall is:",
  ["Iodine deficiency", "Hashimoto thyroiditis", "Sheehan syndrome", "Drugs"], 0,
  "Iodine deficiency: m/c overall; Hashimoto: m/c in west. (Book p106)")
q(106, "Hypothyroidism: Causes & Features", "The most common cause of hypothyroidism in the west is:",
  ["Hashimoto thyroiditis", "Iodine deficiency", "Pituitary adenoma", "Refetoff syndrome"], 0,
  "Hashimoto thyroiditis: m/c in west. (Book p106)")
q(106, "Hypothyroidism: Causes & Features", "Wolff-Chaikoff phenomenon is:",
  ["Iodine induced hypothyroidism", "Iodine induced hyperthyroidism", "Amiodarone thyrotoxicosis", "Post-partum hypothyroidism"], 0,
  "Wolff-Chaikoff: iodine induced hypothyroidism (Jod-Basedow is the hyper counterpart). (Book p106)")
q(106, "Hypothyroidism: Causes & Features", "Sheehan syndrome is:",
  ["Post partum pituitary apoplexy", "Autoimmune thyroiditis", "End organ T4 resistance", "TPO deficiency"], 0,
  "Sheehan syndrome: post partum pituitary apoplexy. (Book p106)")
q(106, "Hypothyroidism: Causes & Features", "Dyshormonogenesis refers to:",
  ["TPO enzyme deficiency", "Iodine deficiency", "TSH receptor mutation", "Thyroglobulin excess"], 0,
  "Dyshormonogenesis: TPO enzyme deficiency. (Book p106)")
q(106, "Hypothyroidism: Causes & Features", "Refetoff syndrome is:",
  ["Elderly patients with end organ resistance to T4", "Post partum apoplexy", "Iodine induced hypothyroidism", "Pituitary apoplexy"], 0,
  "Refetoff syndrome: elderly patients with end organ resistance to T4. (Book p106)")
q(106, "Hypothyroidism: Causes & Features", "A non-functioning pituitary adenoma causes hypothyroidism with ↓ TSH; this is:",
  ["The exception (secondary hypothyroidism)", "The rule", "T3 resistance", "Autoimmune"], 0,
  "Non functioning pituitary adenoma: ↓ TSH (exception). (Book p106)")
q(106, "Hypothyroidism: Causes & Features", "Clinical features of hypothyroidism include all EXCEPT:",
  ["Weight loss", "Dull, lethargic", "Bradycardia", "Menorrhagia"], 0,
  "Features: dull lethargic, alopecia, bradycardia, constipation, weight GAIN, cold intolerance, menorrhagia. (Book p106)")

# ---------------- p106-107 · HASHIMOTO'S THYROIDITIS ----------------
q(106, "Hashimoto's Thyroiditis", "Hashimoto's (lymphocytic) thyroiditis incidence is:",
  ["Autoimmune, female > male, strong hereditary component", "Male > female, viral", "Equal sexes, iodine related", "Childhood only"], 0,
  "Autoimmune: female > male; strong hereditary component. (Book p106)")
q(106, "Hashimoto's Thyroiditis", "Hashimoto's is associated with HLA:",
  ["DR3/B8", "B27", "B35", "DR4"], 0,
  "A/w: HLA DR3/B8; Down's & Turner's syndromes. (Book p106)")
q(106, "Hashimoto's Thyroiditis", "Hashimoto's is associated with which chromosomal syndromes?",
  ["Down's & Turner's", "Klinefelter's & Marfan", "Down's & Klinefelter's", "Turner's & Noonan"], 0,
  "Down's & Turner's syndromes. (Book p106)")
q(107, "Hashimoto's Thyroiditis", "Autoantibodies in Hashimoto's are against:",
  ["Thyroid receptors (blocking), TPO enzyme & thyroglobulin", "Stimulating TSH receptors", "Calcitonin", "Thyroxine"], 0,
  "Autoantibodies against thyroid receptors (blocking receptors), TPO enzyme, thyroglobulin. (Book p107)")
q(107, "Hashimoto's Thyroiditis", "The brief early hyperthyroid phase of Hashimoto's is called:",
  ["Hashitoxicosis (↑ T3, T4 briefly)", "Thyroid storm", "Jod-Basedow", "Apathetic thyrotoxicosis"], 0,
  "Stored hormones released → hashitoxicosis (↑ T3, T4 briefly) then prolonged hypothyroidism. (Book p107)")
q(107, "Hashimoto's Thyroiditis", "Long standing Hashimoto's cases can develop which cancers (m/c first)?",
  ["Lymphoma (m/c), FTC, PTC", "PTC only", "Anaplastic only", "MTC"], 0,
  "Long standing cases: lymphoma (m/c cancer), FTC, PTC. (Book p107)")
q(107, "Hashimoto's Thyroiditis", "FNAC in Hashimoto's shows:",
  ["Lymphocyte infiltration & Hurthle cells", "Orphan Annie nuclei", "Amyloid", "Giant cells"], 0,
  "Ix: autoantibody levels; FNAC lymphocyte infiltration + Hurthle cells. (Book p107)")
q(107, "Hashimoto's Thyroiditis", "Mx of Hashimoto's is:",
  ["Low dose thyroxine gradually titrated till TSH becomes normal; total thyroidectomy if goitre (+)", "Antithyroid drugs", "RIA", "Steroids"], 0,
  "Low dose thyroxine gradually titrated till TSH normal; if goitre (+) → total thyroidectomy. (Book p107)")

# ---------------- p108 · SUBACUTE & POST-PARTUM THYROIDITIS ----------------
q(108, "Subacute & Post-partum Thyroiditis", "Subacute thyroiditis is also called:",
  ["De Quervain/viral/granulomatous thyroiditis", "Riedel's thyroiditis", "Hashimoto's", "Suppurative thyroiditis"], 0,
  "De Quervain/viral/granulomatous thyroiditis; associated with HLA B35. (Book p108)")
q(108, "Subacute & Post-partum Thyroiditis", "The sentinel event for subacute thyroiditis is:",
  ["URTI (viral), 4-6 weeks before", "Surgery", "Trauma", "Iodine load"], 0,
  "Sentinel event: URTI (viral); after 4-6 weeks lymphocytic infiltration. (Book p108)")
q(108, "Subacute & Post-partum Thyroiditis", "The clinical course of subacute thyroiditis is:",
  ["Hyperthyroidism → hypothyroidism → euthyroid (self limiting)", "Hypothyroidism only", "Hyperthyroidism only", "Permanent hypothyroidism"], 0,
  "Spike of hyperthyroidism → hypothyroidism → euthyroid (self limiting); follicles regenerate in 2-3 months. (Book p108)")
q(108, "Subacute & Post-partum Thyroiditis", "Subacute thyroiditis classically presents with painful neck enlargement and:",
  ["↑ ESR", "↓ ESR", "Painless goitre", "Exophthalmos"], 0,
  "Painful neck enlargement; ↑ ESR. (Book p108)")
q(108, "Subacute & Post-partum Thyroiditis", "Mx of subacute thyroiditis is:",
  ["Symptomatic + steroids", "Antithyroid drugs", "Surgery", "RIA"], 0,
  "Mx: symptomatic; steroids. (Book p108)")
q(108, "Subacute & Post-partum Thyroiditis", "Post-partum thyroiditis is seen in what timeframe and frequency?",
  ["2-12 months post partum (in 10%)", "Immediately post partum (50%)", "After 2 years (5%)", "During pregnancy"], 0,
  "Seen in 2-12 months post partum (in 10%). (Book p108)")
q(108, "Subacute & Post-partum Thyroiditis", "The etiology of post-partum thyroiditis is:",
  ["Autoimmune thyroiditis (2nd m/c cause)", "Viral infection", "Iodine deficiency", "Bacterial"], 0,
  "Etiology: autoimmune thyroiditis (2nd m/c cause); anti TPO antibodies (+); 10 fold risk of Hashimoto's. (Book p108)")
q(108, "Subacute & Post-partum Thyroiditis", "Mx of post-partum thyroiditis is:",
  ["Correction of hypothyroidism", "Steroids", "Surgery", "Antithyroid drugs"], 0,
  "Mx: correction of hypothyroidism; features same as Hashimoto. (Book p108)")

# ---------------- p108-109 · RIEDEL'S THYROIDITIS & SUMMARY ----------------
q(108, "Riedel's Thyroiditis & Summary", "Riedel's/fibrosing thyroiditis associations include:",
  ["IgG4, Peyronie's disease, Dupuytren's contracture", "HLA B35", "Down's syndrome", "Pernicious anemia"], 0,
  "Associations: IgG4; Peyronie's disease; Dupuytren's contracture. (Book p108)")
q(108, "Riedel's Thyroiditis & Summary", "Fibrosis within the gland in Riedel's causes:",
  ["Painless enlargement - woody hard gland", "Painful swelling", "Toxic symptoms", "Ophthalmopathy"], 0,
  "Within gland → painless enlargement → woody hard. (Book p108)")
q(108, "Riedel's Thyroiditis & Summary", "Fibrosis in the vicinity of the gland causes pressure symptoms:",
  ["RLN hoarseness & tracheal stridor", "Dysphagia only", "Horner's syndrome", "Venous congestion"], 0,
  "In vicinity → pressure symptoms: RLN hoarseness; trachea stridor. (Book p108)")
q(109, "Riedel's Thyroiditis & Summary", "The important D/D of Riedel's thyroiditis is:",
  ["Anaplastic cancer", "Graves' disease", "Adenoma", "Lingual thyroid"], 0,
  "D/D: anaplastic cancer. (Book p109)")
q(109, "Riedel's Thyroiditis & Summary", "Ix and Mx of Riedel's thyroiditis are:",
  ["USG guided core biopsy; steroids + tamoxifen", "FNAC; PTU", "Scan; RIA", "CXR; surgery"], 0,
  "Ix: USG guided core biopsy; mx: steroids, tamoxifen. (Book p109)")
q(109, "Riedel's Thyroiditis & Summary", "Summary: painful neck swelling with URTI history and spontaneous recovery is:",
  ["Subacute De Quervain thyroiditis", "Hashimoto's", "Riedel's", "Graves'"], 0,
  "Subacute: H/o URTI, painful, hyper→hypo→spontaneous recovery; Hashimoto painless prolonged hypo; Riedel painless hard gland. (Book p109)")

# ---------------- p109 · GOITRE: TYPES & MALIGNANCY RISK ----------------
q(109, "Goitre: Types & Malignancy Risk", "Etiology of diffuse goitre includes all EXCEPT:",
  ["Carcinoma", "Iodine deficiency", "Pregnancy/puberty (↑ demand states)", "Hashimoto's/Graves'"], 0,
  "Diffuse goitre: iodine deficiency, pregnancy & puberty (demand states), Hashimoto's, Graves'. (Book p109)")
q(109, "Goitre: Types & Malignancy Risk", "Untreated diffuse goitre progresses to MNG due to:",
  ["Variable TSH stimulation", "Iodine excess", "Autoimmunity", "Viral infection"], 0,
  "Untreated diffuse goitre → MNG (d/t variable TSH stimulation). (Book p109)")
q(109, "Goitre: Types & Malignancy Risk", "Multinodular goitre etiology is:",
  ["Long standing iodine deficiency", "Acute iodine load", "Viral", "Autoimmune"], 0,
  "MNG: long standing iodine deficiency. (Book p109)")
q(109, "Goitre: Types & Malignancy Risk", "A 'dominant nodule' means:",
  ["Single palpable nodule + rest of gland palpable", "Single palpable nodule + rest not palpable", "Multiple nodules", "A cyst"], 0,
  "Dominant nodule: single palpable nodule + rest of gland palpable (isolated nodule: rest not palpable). (Book p109)")
q(109, "Goitre: Types & Malignancy Risk", "Risk of malignancy in thyroid swellings: solid swellings have:",
  ["Twice the risk of cystic ones", "Half the risk", "Equal risk", "No risk"], 0,
  "Solid swellings have twice the risk as cystic ones. (Book p109)")
q(109, "Goitre: Types & Malignancy Risk", "Regarding malignancy risk in thyroid swellings, males have:",
  ["4 times greater risk than females", "Equal risk", "Half the risk", "2 times lesser risk"], 0,
  "Males have 4 times greater risk than females. (Book p109)")

# ---------------- p110 · RETROSTERNAL GOITRE ----------------
q(110, "Retrosternal Goitre", "A retrosternal goitre is:",
  ["Thyroid swelling behind the sternum", "A lateral neck goitre", "Ectopic lingual thyroid", "A mediastinal teratoma"], 0,
  "Retrosternal goitre: thyroid swelling behind the sternum. (Book p110)")
q(110, "Retrosternal Goitre", "The most common type of retrosternal goitre (90%) is:",
  ["2° retrosternal/plunging goitre", "1° mediastinal", "Ectopic", "Malignant"], 0,
  "2° retrosternal/plunging goitre (m/c, 90%): starts in neck & plunges into mediastinum. (Book p110)")
q(110, "Retrosternal Goitre", "1° mediastinal retrosternal goitre (10%) arises from and is supplied by:",
  ["Ectopic thyroid tissue in mediastinum; mediastinal vessels", "Neck thyroid; neck vessels", "Lingual thyroid; carotid", "Thymus; internal thoracic"], 0,
  "1° mediastinal: ectopic thyroid tissue in mediastinum; blood supply mediastinal vessels (2°: neck vessels). (Book p110)")
q(110, "Retrosternal Goitre", "The blood supply of a 2° (plunging) retrosternal goitre is from:",
  ["Neck vessels", "Mediastinal vessels", "Bronchial arteries", "Pericardial branches"], 0,
  "2° retrosternal: neck vessels. (Book p110)")
q(110, "Retrosternal Goitre", "On examination of a retrosternal goitre:",
  ["Lower limit is not palpable", "Upper limit not palpable", "It moves with swallowing always", "It is transilluminant"], 0,
  "Goitre: lower limit not palpable; pressure symptoms dyspnoea/stridor. (Book p110)")
q(110, "Retrosternal Goitre", "Pemberton sign: when the patient raises his hands:",
  ["Swelling presses on thoracic inlet, blocking venous drainage → facial congestion", "The goitre becomes palpable", "Stridor is relieved", "Voice changes"], 0,
  "Pemberton sign: raise hands → swelling presses on thoracic inlet → blocks venous drainage → facial congestion. (Book p110)")
q(110, "Retrosternal Goitre", "The IOC investigation for retrosternal goitre is:",
  ["CECT neck & thorax", "Chest x-ray alone", "FNAC", "USG abdomen"], 0,
  "Ix: CECT neck & thorax (IOC); chest x-ray (trachea pushed to opposite side). (Book p110)")
q(110, "Retrosternal Goitre", "Most retrosternal goitres are removed via:",
  ["Neck/cervical incision (m/c)", "Median sternotomy always", "VATS", "Thoracotomy"], 0,
  "Neck/cervical incision & remove goitre: m/c. (Book p110)")
q(110, "Retrosternal Goitre", "Median sternotomy is indicated in all EXCEPT:",
  ["A primary uncomplicated small plunging goitre", "Recurrent mediastinal goitre", "1° mediastinal goitre", "Goitre larger than thoracic inlet"], 0,
  "Median sternotomy in: recurrent mediastinal, 1° mediastinal, goitre larger than thoracic inlet, malignant retrosternal goitre. (Book p110)")

# ---------------- units ----------------
def sec_ids(*labels):
    return [x["id"] for x in Q if x["sec"] in labels]

def first_page(label):
    for x in Q:
        if x["sec"] == label:
            return x["page"]
    return 0

UNIT_DEFS = [
    ("Thyroid Embryology & Lingual Thyroid", ("Thyroid Embryology & Lingual Thyroid",),
     "Thyroid descends from foramen caecum (junction anterior 2/3-posterior 1/3 tongue) via thyroglossal tract which obliterates. Lingual thyroid = undescended tissue below tongue (tongue lifted up); FNAC + USG neck to confirm normal gland before excision; thyroxine if it was the only tissue."),
    ("Thyroglossal Cyst: Dx, Mx & Complications", ("Thyroglossal Cyst: Dx, Mx & Complications",),
     "Persistent tract → subhyoid (m/c) midline swelling moving with deglutition AND tongue protrusion. Sistrunk = cyst + part of hyoid + tract to tongue base; I&D never (fistula). Complications: fistula & PTC in long-standing cases. Vs branchial fistula: lower 1/3 along SCM, congenital/acquired."),
    ("Hyperthyroidism: Features & Causes", ("Hyperthyroidism: Features & Causes",),
     "Thin irritable, weight loss despite appetite, tachycardia, diarrhoea, tremors, heat intolerance, oligomenorrhea. Scan patterns: Graves diffuse ↑ (m/c); Plummer's single hot; toxic nodular goitre multiple hot; factitious & struma ovarii ↓; Jod-Basedow (iodine-induced) ↑; TSH adenoma ↑TSH ↑."),
    ("Antithyroid Drugs & Pre-op Preparation", ("Antithyroid Drugs & Pre-op Preparation",),
     "PTU/carbimazole block peroxidase & T4→T3; PTU safe in 1st trimester/lactation; agranulocytosis - sore throat 1st sign. RIA I131 β-rays t½ 7-8 d. Pre-Sx: drugs 6-8 wks to euthyroid, nadolol (long acting) till 7 days post-op (T3 t½), last dose evening before."),
    ("Thyroid Storm", ("Thyroid Storm",),
     "Uncontrolled thyrotoxicosis from inadequately prepared patient (m/c), URTI, FNAC, Sx trauma, anaesthetics. Dehydration, hyperthermia, HTN crisis; arrhythmia kills. Mx: aggressive IV fluids (prevent ATN), cold packs, IV steroids + antibiotics, high-dose propranolol, PTU; avoid aspirin."),
    ("Graves: Basics & Eye Signs", ("Graves: Basics & Eye Signs",),
     "Autoimmune F>M, m/c hyperthyroid cause; stimulating TRAb (LATS); pretibial myxedema; a/w pernicious anemia & myasthenia. Acropachy = subperiosteal bone. Eye: exophthalmos; von Graefe lid lag + Dalrymple retraction (Muller spasm), Joffroy no forehead wrinkle, Moebius loss of accommodation (severe), Stellwag infrequent blink (mild)."),
    ("Graves: Dx & Mx", ("Graves: Dx & Mx",),
     "Dx: C/F + autoantibodies; HPE scalloped colloid + tall columnar cells. Mx by status: child drugs; pregnant PTU; adult no goitre drugs→RIA; with goitre drugs→Sx; elderly comorbid drugs→RIA; extensive eye signs drugs→Sx (RIA worsens eyes). Sx: total > subtotal."),
    ("Plummer's & Solitary Toxic Nodule", ("Plummer's & Solitary Toxic Nodule",),
     "Plummer's/toxic nodular goitre: F:M 5:1, 2nd m/c cause, multiple hot & cold nodules, drugs → total thyroidectomy. Solitary toxic nodule: 5th decade F>M, single hot nodule, drugs → RIA."),
    ("Hypothyroidism: Causes & Features", ("Hypothyroidism: Causes & Features",),
     "Causes: iodine deficiency (overall m/c), Hashimoto (west m/c), Wolff-Chaikoff (iodine-induced), non-functioning pituitary adenoma ↓TSH (exception), Sheehan (post-partum apoplexy), dyshormonogenesis (TPO deficiency), euthyroid sick syndrome, Refetoff (end-organ T4 resistance). Dull, alopecia, bradycardia, constipation, weight gain, cold intolerance, menorrhagia."),
    ("Hashimoto's Thyroiditis", ("Hashimoto's Thyroiditis",),
     "Autoimmune F>M, hereditary, HLA DR3/B8, Down's/Turner's. Blocking receptor + anti-TPO + anti-thyroglobulin antibodies; lymphocytes destroy follicles → hashitoxicosis spike → prolonged hypothyroidism. Long-standing: lymphoma (m/c), FTC, PTC. FNAC lymphocytes + Hurthle; titrate low-dose thyroxine to TSH; total thyroidectomy if goitre."),
    ("Subacute & Post-partum Thyroiditis", ("Subacute & Post-partum Thyroiditis",),
     "De Quervain (viral/granulomatous, HLA B35): post-URTI 4-6 wks; painful neck + ↑ESR; hyper→hypo→euthyroid self-limiting (follicles regenerate 2-3 mo); symptomatic + steroids. Post-partum: 2-12 mo (10%), autoimmune 2nd m/c, anti-TPO +, 10-fold Hashimoto risk; correct hypothyroidism."),
    ("Riedel's Thyroiditis & Summary", ("Riedel's Thyroiditis & Summary",),
     "IgG4 fibrosing disease (Peyronie's, Dupuytren's): woody hard painless gland, pressure symptoms; D/D anaplastic; core biopsy; steroids + tamoxifen. Summary table: Hashimoto painless prolonged hypo; De Quervain painful post-URTI spontaneous recovery; Riedel hard gland."),
    ("Goitre: Types & Malignancy Risk", ("Goitre: Types & Malignancy Risk",),
     "Diffuse: iodine deficiency, demand states (pregnancy/puberty), Hashimoto/Graves; untreated → MNG (variable TSH). MNG: long-standing iodine deficiency. Dominant nodule = single palpable + rest palpable. Malignancy risk: solid 2× cystic; males 4× females."),
    ("Retrosternal Goitre", ("Retrosternal Goitre",),
     "Behind sternum; 2° plunging m/c (90%, neck vessels) vs 1° mediastinal (10%, ectopic, mediastinal vessels). Lower limit not palpable; Pemberton sign (arms up → inlet obstruction → facial congestion). CECT neck + thorax IOC; neck incision m/c; sternotomy for recurrent, 1°, larger than inlet, malignant."),
]

UNITS = []
for i, (title, labels, guide) in enumerate(UNIT_DEFS, 1):
    UNITS.append({"id": f"SURG-U16-{i}", "ch": 16, "n": i, "title": title,
                  "sec": f"{labels[0]} · p{first_page(labels[0])}",
                  "qs": sec_ids(*labels), "guide": guide})

covered = [i for u in UNITS for i in u["qs"]]
assert covered == [x["id"] for x in Q], "units must cover questions in order"

data = {"questions": Q, "units": UNITS}
with open("data/ch16.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
print(f"ch16: {len(Q)} questions, {len(UNITS)} units")
