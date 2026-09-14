#!/usr/bin/env python3
"""Build data/ch58.json — Thermal Injuries (Marrow Surgery Ed 8, pp444-450)."""
import json

Q = []

def q(page, sec, text, correct, wrongs, note=None):
    opts = [correct] + list(wrongs)
    assert len(opts) == 4
    Q.append({
        "id": f"SURG-C58-{len(Q)+1:03d}",
        "sec": sec,
        "page": page,
        "q": text,
        "opts": opts,
        "ans": 0,
        "exp": (note or correct) + f" (Book p{page})",
    })

# ------------------------------------------------------------------ p444
S1 = "Burns Unit: Referral Criteria and ACLS (ABCDE)"
q(444, S1, "Burns referral criteria include burns of face, hands and:", "Genitalia", ["Feet only", "Trunk only", "Forearms"])
q(444, S1, "Which burn types mandate referral to a burns unit?", "Chemical, electrical & inhalation injury", ["Only thermal", "Only sunburn", "Only first degree"])
q(444, S1, "Partial thickness burns over what TBSA need referral?", ">10% TBSA", [">5% TBSA", ">20% TBSA", ">50% TBSA"])
q(444, S1, "All FULL thickness (3rd degree) burns are:", "Referred to burns unit", ["Managed at home", "Treated with creams only", "Not referred"])
q(444, S1, "Burns management follows which guidelines?", "ACLS (ABCDE)", ["ATLS only", "NICE", "GCS"])
q(444, S1, "In the ACLS 'E' of burns management, exposure assesses:", "Cause of burns & extent of burns", ["Only limbs", "Rectal tone", "Spine only"])
q(444, S1, "ABCDE of burns stands for:", "Airway, Breathing, Circulation, Disability, Exposure", ["Airway, Burns, Circulation, Drainage, Exposure", "Assess, Breathing, Cool, Dress, Evaluate", "Airway, Blood, Circulation, Dressing, Extent"])

# ------------------------------------------------------------------ p444
S2 = "Airway Burns: Signs and Stages"
q(444, S2, "Signs of airway burns (1):", "Singed nasal hair", ["Bilateral clear lungs", "Bradypnea", "Stridor only"])
q(444, S2, "Signs of airway burns (2):", "Hoarseness of voice", ["Rhinorrhoea", "Dysphagia only", "Cough with sputum only"])
q(444, S2, "Signs of airway burns (3):", "Carbonaceous deposits in sputum", ["Hemoptysis", "Purulent sputum", "Pink froth"])
q(444, S2, "History suggesting airway burns:", "Burns in a closed room", ["Open field burn", "Scald only", "Sunburn"])
q(444, S2, "Burns involving which regions suggest airway burns?", "Head, face & neck", ["Only feet", "Only perineum", "Only back"])
q(444, S2, "Altered sensorium after burns suggests:", "Airway burns (with closed room/head/face burns)", ["Only pain", "Fluid overload always", "Nothing"])
q(444, S2, "Airway burns require:", "Prophylactic intubation (d/t rapid airway collapse)", ["Observation only", "Tracheostomy always", "Nebulisation only"])
q(444, S2, "Reason for prophylactic intubation in airway burns:", "Rapid airway collapse", ["Facial swelling only", "Voice change", "Sputum retention"])

# ------------------------------------------------------------------ p444
S3 = "Stages of Airway Burns and Breathing (Hypoxia Causes)"
q(444, S3, "Stage 1 of airway burns:", "Acute pulmonary insufficiency — hypoxia", ["ARDS at 24-48 h", "Bronchopneumonia", "Fibrosis"])
q(444, S3, "Stage 2 of airway burns (24-48 hrs):", "ARDS-like picture — B/L lung infiltrates, hypoxia", ["Immediate asphyxia", "Bronchopneumonia", "Pleural effusion"])
q(444, S3, "ARDS-like stage of airway burns requires:", "Intubation & bronchodilators", ["Only O2 mask", "Chest physiotherapy only", "Steroids only"])
q(444, S3, "Stage 3 of airway burns:", "Bronchopneumonia", ["ARDS", "Acute insufficiency", "Atelectasis only"])
q(444, S3, "Pathogenesis of burn bronchopneumonia:", "Burns → epithelial injury → ↓immune response", ["Burns → sepsis → DIC", "Burns → aspiration", "Fluid overload"])
q(444, S3, "EARLY phase (1-3 days) bronchopneumonia organism:", "S. aureus", ["Gram negative bacteria", "Pseudomonas only", "Candida"])
q(444, S3, "LATE phase (>3 days) bronchopneumonia organism:", "Gram negative bacteria", ["S. aureus", "S. pyogenes", "Anaerobes only"])
q(444, S3, "Causes of hypoxia in burns (1-3):", "Inhalation of smoke, airway collapse & CO poisoning", ["Only anemia", "Neurogenic shock", "Pulmonary embolism"])
q(444, S3, "CO causes hypoxia by:", "↑affinity to hemoglobin → ↓O2 transportation", ["Blocking cytochrome oxidase only", "Causing bronchospasm", "Alveolar flooding"])
q(444, S3, "Eschar around the chest causes hypoxia by:", "Restricting chest expansion", ["Aspiration", "Pneumothorax", "Pulmonary embolism"])
q(444, S3, "Mx of chest-restricting eschar:", "Escharotomy", ["Steroids", "IPPV only", "Analgesia"])

# ------------------------------------------------------------------ p445
S4 = "Circulation: Burns Pathophysiology"
q(445, S4, "Burns release inflammatory mediators that cause:", "Vasodilation", ["Vasoconstriction", "Thrombosis", "No change"])
q(445, S4, "Burns <10% TBSA produce:", "Localized immune response", ["Generalized immune response", "Septic shock", "No response"])
q(445, S4, "Burns >10% TBSA produce:", "Generalized immune response", ["Localized immune response", "Immune paralysis only", "No response"])
q(445, S4, "Vasodilation after burns causes dehydration via:", "↑evaporation", ["↓sweating", "Polyuria", "Vomiting"])
q(445, S4, "Leaky vessels after burns (12-24 hrs) cause:", "Albumin lost into extravascular space → tissue edema (3rd space loss)", ["Albumin gain in vessels", "RBC gain", "Hemoconcentration of lymph only"])

# ------------------------------------------------------------------ p445
S5 = "Fluid Resuscitation: Parkland, Brooke, Galveston & Target Urine Output"
q(445, S5, "Colloid formulas used AFTER 12 hrs:", "Muir & Barclay formula", ["Parkland", "Brooke", "Galveston"])
q(445, S5, "The m/c crystalloid formula for burns:", "Parkland formula (Ringer lactate)", ["Muir & Barclay", "Brooke colloid", "Hartmann colloid"])
q(445, S5, "Parkland formula:", "4 × body weight (kg) × % TBSA of burns (excluding 1° burns)", ["2 × weight × %TBSA", "3 × weight × %TBSA", "4 × weight × %TBSA (including 1°)"])
q(445, S5, "In Parkland, the 24-hr volume is given as:", "½ amount over 8 hrs + ½ over 16 hrs", ["¼ over 12 h + ¾ over 12 h", "All over 4 h", "⅓ over 8 h each split"])
q(445, S5, "Modified Parkland/Brooke formula:", "2 × body weight (kg) × %TBSA", ["4 × weight × %TBSA", "3 × weight × %TBSA", "6 × weight × %TBSA"])
q(445, S5, "Flame/scald fluid rate in adults & older children (≥14 yr):", "2 mL LR × kg × %TBSA (urine 0.5 mL/kg/hr)", ["4 mL LR", "3 mL LR", "1 mL LR"])
q(445, S5, "Fluid rate for children (<14 yr) with flame/scald burns:", "3 mL LR × kg × %TBSA (urine 30-50 mL/hr)", ["2 mL LR (0.5 mL/kg/hr)", "4 mL LR (1-1.5 mL/kg/hr)", "1 mL LR"])
q(445, S5, "Infants/young children (≤30 kg) with flame/scald burns get:", "3 mL LR × kg × %TBSA PLUS sugar solution at maintenance (urine 1 mL/kg/hr)", ["Only 2 mL LR", "4 mL LR only", "Colloids only"])
q(445, S5, "Electrical injury fluid resuscitation (all ages):", "4 mL LR × kg × %TBSA until urine clears (urine 1-1.5 mL/kg/hr)", ["2 mL LR until urine clears", "3 mL LR fixed 24 h", "Colloid 12-hourly"])
q(445, S5, "Maintenance fluid in children — first 10 kg:", "100 mL/kg", ["50 mL/kg", "20 mL/kg", "150 mL/kg"])
q(445, S5, "Maintenance fluid in children — next 10 kg:", "50 mL/kg", ["100 mL/kg", "20 mL/kg", "75 mL/kg"])
q(445, S5, "Maintenance fluid in children — every kg AFTER 20 kg:", "20 mL/kg (all over 24 hrs)", ["50 mL/kg", "100 mL/kg", "10 mL/kg"])
q(445, S5, "Galveston formula is:", "For crystalloid solutions, also used in children", ["Colloid formula for adults", "Only for electrical burns", "For escharotomy timing"])

# ------------------------------------------------------------------ p446
S6 = "Burns % Calculation: Palm, Rule of 9s, Lund & Browder"
q(446, S6, "Palm of the patient equals what TBSA (for small burns)?", "1%", ["2%", "5%", "9%"])
q(446, S6, "Wallace's rule is also called:", "Rule of 9s", ["Rule of palms", "Lund rule", "Browder rule"])
q(446, S6, "The BEST method for burns % calculation:", "Lund & Browder chart", ["Rule of 9s", "Palm method", "Serial weighing"])
q(446, S6, "In adults (rule of 9s), each arm is:", "9% (4.5% front + 4.5% back)", ["18%", "4.5%", "1%"])
q(446, S6, "In adults, head & neck together are:", "9% (4.5% front + 4.5% back)", ["18%", "1%", "13.5%"])
q(446, S6, "In adults, front trunk is:", "18%", ["9%", "36%", "13.5%"])
q(446, S6, "In adults, each leg is:", "18% (9% front + 9% back)", ["9%", "13.5%", "27%"])
q(446, S6, "In adults, perineum is:", "1%", ["9%", "18%", "0.5%"])
q(446, S6, "In CHILDREN (rule of 9s), head is:", "18%", ["9%", "13.5%", "1%"])
q(446, S6, "In CHILDREN, each arm is:", "9%", ["4.5%", "18%", "13.5%"])
q(446, S6, "In CHILDREN, each leg is:", "13.5%", ["18%", "9%", "27%"])
q(446, S6, "Child photo: burns over one arm (9%) + anterior chest/abdomen (9%) equal:", "18%", ["9%", "27%", "36%"])

# ------------------------------------------------------------------ p446
S7 = "Zones of Burns"
q(446, S7, "The zone of burns with IRREVERSIBLE damage:", "Zone of coagulation/necrosis", ["Zone of stasis", "Zone of hyperemia", "All zones"])
q(446, S7, "Zone of stasis if POORLY managed becomes:", "Zone of necrosis", ["Zone of hyperemia", "Normal skin", "Zone of coagulation shrinkage"])
q(446, S7, "Zone of stasis if MANAGED WELL becomes:", "Zone of hyperemia (reversible → healing)", ["Necrosis", "Coagulation", "Scar only"])
q(446, S7, "Zone of hyperemia develops d/t:", "Vasodilation", ["Thrombosis", "Necrosis", "Infection"])
q(446, S7, "The zone of stasis is characterised by:", "Capillary damage & tissue edema", ["Instant charring", "Only pain", "Full thickness death"])
q(446, S7, "Immune change in the burn zone:", "G-CSF receptor downregulation; reduced immune cell capacity", ["G-CSF upregulation", "Complement gain", "No immune change"])

# ------------------------------------------------------------------ p446-447
S8 = "Degrees of Burns"
q(446, S8, "1st degree burns involve:", "Epidermis only", ["Epidermis + dermis", "Subcutaneous tissue", "Muscle"])
q(446, S8, "1st degree burns character:", "Red, tender, blanching (+)", ["Black, charred, painless", "Leathery white", "Non-blanching"])
q(446, S8, "1st degree burns heal:", "Without scarring in 3-5 days", ["With scarring in 3 weeks", "By grafting", "In 3 months"])
q(446, S8, "Classic example of 1st degree burn:", "Sunburn", ["Flame burn of hand", "Electrical entry wound", "Scald over thigh"])
q(446, S8, "2nd degree SUPERFICIAL burns involve:", "Epidermis + papillary dermis", ["Whole dermis", "Muscle", "Epidermis only"])
q(446, S8, "Superficial 2nd degree burns look:", "Similar to 1st degree burns (blister seen)", ["Black & charred", "Painless & white", "Mummified"])
q(446, S8, "Superficial 2nd degree burns heal on proper dressing:", "Without scarring in 2-3 weeks", ["In 3-5 days", "With keloids always", "Only by grafting"])
q(446, S8, "2nd degree DEEP burns involve:", "Epidermis + (whole) dermis", ["Papillary dermis only", "Subcutaneous fat", "Bone"])
q(446, S8, "Deep 2nd degree burns are:", "Red, ↓tender, ±blanching (d/t vessel thrombosis)", ["Always painless & black", "Blanching ++", "Painless from day 1"])
q(446, S8, "Deep 2nd degree burns result in:", "Hypertrophic scars & keloids; requires dressing of wound", ["Heal in 3 days", "Never scar", "Need amputation"])
q(447, S8, "3rd degree burns involve:", "Subcutaneous tissue", ["Dermis only", "Epidermis only", "Papillary dermis"])
q(447, S8, "4th degree burns involve:", "Muscle", ["Subcutaneous tissue", "Whole dermis", "Epidermis"])
q(447, S8, "Character of 3rd/4th degree burns:", "Black, charred, no blanching & PAINLESS", ["Red, tender, blanching", "Blistering & painful", "Weepy & pink"])
q(447, S8, "Mx of 3rd/4th degree burns:", "Early excision + split thickness skin grafting", ["Dressing only", "Conservative healing", "Mesh only"])
q(446, S8, "Blister photo over reddened skin (painful, heals 2-3 weeks) depicts:", "Superficial 2nd degree burn", ["1st degree", "4th degree", "Chemical burn"])

# ------------------------------------------------------------------ p447
S9 = "General Measures and Compartment Syndrome / Escharotomy"
q(447, S9, "Initial wash for a burn wound:", "Room temperature water", ["Ice cold water", "Hot water", "Alcohol"])
q(447, S9, "Ryle's tube insertion is indicated in burns >:", "15-20% (to avoid vomiting caused by ileus)", ["5%", "50%", "80%"])
q(447, S9, "Avoid in burns first aid:", "Bursting blisters, IM & SC injections", ["IV fluids", "Tetanus toxoid", "Analgesia"])
q(447, S9, "Compartment syndrome in burns — compartment pressure:", ">30 mm Hg", [">10 mm Hg", ">60 mm Hg", ">100 mm Hg"])
q(447, S9, "Compartment syndrome in burns occurs d/t:", "Circumferential eschar", ["Fluid overload", "Sepsis", "Positioning"])
q(447, S9, "Clinical features of burn compartment syndrome:", "Severe pain not relieved by medication & pain on passive flexion", ["Painless swelling", "Coldness only", "Itching"])
q(447, S9, "Treatment of burn compartment syndrome:", "Escharotomy (a type of fasciotomy)", ["Analgesia", "Elevation", "Delay till day 7"])
q(447, S9, "Layers cut in escharotomy:", "Skin → S/c tissue → superficial fascia → deep fascia (till muscle is exposed)", ["Only epidermis", "Skin + muscle", "Fascia alone"])

# ------------------------------------------------------------------ p447
S10 = "Nutrition in Burns"
q(447, S10, "BEE/REE multiplier — Normal:", "1", ["1.4", "1.8", "2"])
q(447, S10, "BEE/REE multiplier — mild/moderate sepsis:", "1.4", ["1", "1.8", "2"])
q(447, S10, "BEE/REE multiplier — severe sepsis:", "1.8", ["1.4", "2", "2.5"])
q(447, S10, "BEE/REE multiplier — severe burns:", "2 (= 40 kcal/kg/day)", ["1.8", "1.4", "1"])
q(447, S10, "Caloric requirement formula in burns:", "Curreri/Sutherland formula", ["Davies formula", "Harris only", "Muir-Barclay"])
q(447, S10, "Day 5-10 of burns: nitrogen balance is:", "Negative → 20% of nutrition must be protein", ["Positive", "Neutral", "Zero"])
q(447, S10, "Protein requirement formula in burns:", "Davies formula", ["Curreri", "Sutherland", "Parkland"])

# ------------------------------------------------------------------ p447-448
S11 = "Dressing Materials and Special Agents in 2° Burns"
q(447, S11, "Aims of burn dressing:", "Protect damaged epithelium, minimise infection & promote healing", ["Dry the wound", "Tighten eschar", "Colour the skin"])
q(447, S11, "Dressing for 1st degree burns:", "Expose the wound", ["Vaseline gauze", "Hydrocolloid", "Silver cream"])
q(447, S11, "Dressing for superficial 2nd degree burns:", "Vaseline/paraffin gauze; collagen dressing (if not infected)", ["Hydrocolloid (Duoderm)", "Exposure", "Debridement"])
q(447, S11, "Dressing for deep 2nd degree burns:", "Hydrocolloid dressing (e.g. Duoderm)", ["Exposure", "Vaseline gauze only", "Collagen only"])
q(448, S11, "The m/c special agent in 2° burns:", "1% Silver sulphadiazine", ["Silver nitrate", "Mafenide", "Cesium nitrate"])
q(448, S11, "1% Silver sulphadiazine is effective against:", "Pseudomonas & Gram negative bacteria", ["Only fungi", "Only anaerobes", "Viruses"])
q(448, S11, "Disadvantages of silver sulphadiazine:", "Requires frequent dressing change & doesn't penetrate eschar (superficial wounds only)", ["Black stain", "Metabolic acidosis", "Hypoglycemia"])
q(448, S11, "Silver nitrate — spectrum & drawback:", "Pseudomonas > Gram negative; black stain", ["Penetrates eschar; pain", "Immunomodulator; expensive", "Only gram positive; acidosis"])
q(448, S11, "The special agent that PENETRATES eschar:", "5% Mafenide acetate", ["Silver sulphadiazine", "Silver nitrate", "Cesium nitrate"])
q(448, S11, "Disadvantages of mafenide acetate:", "Painful application & metabolic acidosis", ["Black stain", "Expensive", "Poor eschar entry"])
q(448, S11, "The BEST special agent for 2° burns:", "Cesium nitrate (immunomodulator)", ["Silver sulphadiazine", "Mafenide", "Silver nitrate"])
q(448, S11, "Drawback of cesium nitrate:", "Expensive", ["Painful", "Black stain", "Acidosis"])

# ------------------------------------------------------------------ p448
S12 = "Management of Complications and Causes of Death in Burns"
q(448, S12, "Mx of hypertrophic scar after burns:", "Spontaneous resolution with time", ["Intralesional triamcinolone", "V-Y plasty", "Wide excision"])
q(448, S12, "Mx of keloids after burns:", "Intralesional triamcinolone", ["Observation only", "V-Y plasty", "Radiation only"])
q(448, S12, "Mx of post-burn contracture:", "V-Y plasty, Z plasty", ["Triamcinolone", "Wide local excision", "Graft alone"])
q(448, S12, "Mx of Marjolin's ulcer:", "Wide local excision", ["Z plasty", "Triamcinolone", "Dressing"])
q(448, S12, "IMMEDIATE cause of death in burns:", "Asphyxia > neurogenic shock", ["Hypovolemic shock", "Septicemia", "Renal failure"])
q(448, S12, "EARLY (1-3 days) cause of death in burns:", "Hypovolemic shock", ["Septic shock", "Asphyxia", "CO poisoning"])
q(448, S12, "LATE (>3 days) & m/c OVERALL cause of death in burns:", "Septic shock", ["Hypovolemia", "Asphyxia", "Arrhythmia"])
q(448, S12, "M/c causative organism of lethal burn septicemia:", "Pseudomonas", ["S. aureus", "E. coli", "Klebsiella"])

# ------------------------------------------------------------------ p448
S13 = "Chemical Burns and Hydrofluoric Acid"
q(448, S13, "Which chemical burn penetrates DEEPER?", "Alkali burns > acid burns", ["Acid > alkali", "Equal", "Neither penetrates"])
q(448, S13, "First mx step of chemical burns:", "Wash with water (do NOT try neutralization)", ["Neutralise with weak acid/base", "Apply oil", "Occlusive dressing"])
q(448, S13, "Chemical POWDER on skin is managed by:", "Brush off (before washing)", ["Immediate water only", "Neutralization", "Solvent wipe"])
q(448, S13, "Hydrofluoric acid burns — electrolyte effects:", "↓Ca²⁺ (chelation), ↑K⁺ (tissue damage) & acidosis", ["↑Ca²⁺, ↓K⁺", "↑Na⁺ only", "No change"])
q(448, S13, "Mx of hydrofluoric acid burns:", "Calcium gluconate (topical gel/oral/i.v./i.a.)", ["Sodium bicarbonate", "Magnesium sulfate", "Insulin-dextrose"])

# ------------------------------------------------------------------ p449
S14 = "Electrical Burns and Lightning Injury"
q(449, S14, "Electrical burns are typically what degree?", "3°/4°", ["1°", "2° superficial", "Sunburn-like"])
q(449, S14, "DC current causes:", "Heart blocks", ["Tetany", "Myoglobinuria", "Only skin burns"])
q(449, S14, "AC current causes:", "Tetany → muscle damage → myoglobinuria", ["Heart blocks only", "Only surface burn", "Deafness"])
q(449, S14, "Myoglobinuria after AC injury is prevented by:", "↑IV fluids (to prevent ATN)", ["Diuretics only", "Alkalinisation alone", "Fluid restriction"])
q(449, S14, "M/c cause of death in electrical burns:", "Arrhythmia", ["Renal failure", "Sepsis", "Hypovolemia"])
q(449, S14, "Examination of electrical burns must include:", "Both entry AND exit wounds", ["Entry only", "Exit only", "Mouth"])
q(449, S14, "Definitive care of electrical burn wound:", "Early excision + split thickness skin grafting", ["Dressing for weeks", "Amputation always", "Conservative healing"])
q(449, S14, "DIRECT lightning injury features:", "High grade electrical injury & arrhythmias", ["Filigree burns", "Only superficial burns", "No cardiac effect"])
q(449, S14, "INDIRECT lightning injury:", "Filigree burns pattern; superficial burns d/t sparks from adjacent object", ["High grade deep burns", "Always fatal", "Entry-exit wounds"])

# ------------------------------------------------------------------ p449-450
S15 = "Hypothermia: Stages, Rewarming, Frostbite and Trench Foot"
q(449, S15, "Hypothermia is usually caused by:", "30 mins of cold exposure", ["3 hours", "24 hours", "1 week"])
q(449, S15, "Stage I hypothermia:", "Conscious, shivering (35-32°C / 95-89.6°F)", ["Unconscious, shivering", "No vital signs", "J/Osborne waves"])
q(449, S15, "Stage II hypothermia:", "Impaired consciousness, NOT shivering (32-28°C); ECG J/Osborne waves", ["Conscious, shivering", "No vital signs", "Hyperthermia"])
q(449, S15, "Stage III hypothermia:", "Unconscious, not shivering; vital signs present (28-24°C)", ["No vital signs", "Conscious", "Shivering violently"])
q(449, S15, "Stage IV hypothermia:", "No vital signs (<24°C / <75.2°F)", ["Vital signs present", "Shivering", "J waves only"])
q(449, S15, "Treatment of Stage I hypothermia:", "Warm environment & clothing, warm sweet drinks, active movement", ["ECMO", "CPR", "Immobility"])
q(449, S15, "Treatment of Stage II hypothermia:", "Cardiac monitoring, minimal movements to avoid arrhythmias, immobilization, full-body insulation, active external rewarming", ["Sweet drinks & movement", "ECMO only", "Nothing"])
q(449, S15, "Stage III hypothermia treatment adds:", "ECMO or CPB in cases with cardiac instability", ["Active movement", "Cold lavage", "Observation"])
q(449, S15, "Stage IV hypothermia treatment:", "Stage 2 and 3 management plus CPR + ECMO or CPB", ["Warm drinks", "External warmth only", "Declare death"])
q(450, S15, "PASSIVE rewarming (prevent heat loss) includes:", "Dry patient, warm environment, shivering, blankets/clothing, cover head", ["Heating pads", "Heated IV fluids", "CPB"])
q(450, S15, "Passive rewarming level of hypothermia:", "Mild: 35°C to 32°C", ["Moderate 32-28", "Severe <28", "Any stage"])
q(450, S15, "ACTIVE EXTERNAL rewarming methods:", "Heating pad, warm water/blankets/water bottles, warm water immersion, convection heaters (lamps & radiant warmers)", ["Gastric lavage", "CPB", "Heated IV fluids"])
q(450, S15, "Active external rewarming level:", "Mild (35-32°C) and moderate (<32-28°C)", ["Severe only", "Any", "None"])
q(450, S15, "ACTIVE INTERNAL rewarming methods:", "Heated intravenous fluids & gastric or colonic lavage", ["Blankets", "Lamps", "Warm drinks"])
q(450, S15, "Internal rewarming level:", "Moderate (<32-28°C) and severe (<28-24°C)", ["Mild only", "None", "Only stage IV"])
q(450, S15, "BEST method of rewarming (severe):", "Cardiopulmonary bypass", ["Warm water immersion", "Heated blankets", "Gastric lavage"])
q(450, S15, "Best site to measure core temperature:", "Rectal > esophageal", ["Axillary", "Oral", "Tympanic"])
q(450, S15, "Before declaring death in hypothermia:", "Body temperature should have returned to normal", ["2 hours of arrest suffices", "No rule", "Pupils only"])

# ------------------------------------------------------------------ p450
S16 = "Frostbite and Trench Foot"
q(450, S16, "Frostbite pathophysiology:", "Dry cold exposure → formation of ice crystals → tissue damage", ["Wet cold → stasis", "Heat → edema", "Chemical chelation"])
q(450, S16, "After frostbite rewarming:", "Vasodilation → free O₂ radicals → reperfusion injury", ["Vasoconstriction", "Immediate healing", "Necrosis without radicals"])
q(450, S16, "Trench foot pathophysiology:", "Wet cold exposure → microvascular damage + stasis and occlusion", ["Dry cold → ice crystals", "Burn injury", "Arterial emboli"])
q(450, S16, "Mx of frostbite/trench foot — rewarming water temperature:", "40°C (rapid rewarming)", ["60°C", "25°C", "10°C"])
q(450, S16, "What must be AVOIDED in frostbite?", "Rubbing the tissue", ["Rewarming", "Elevation", "Analgesia"])
q(450, S16, "Correct along with rewarming:", "Hyperkalemia & acidosis", ["Hypokalemia & alkalosis", "Hypernatremia", "Hypocalcemia only"])
q(450, S16, "Gangrenous frostbite amputation timing:", "Once demarcation line appears", ["Immediately", "Never", "After 1 year"])

# ------------------------------------------------------------------ units
UNIT_DEFS = [
    (S1, "Face, hands, genitalia, chemical/electrical/inhalation burns, partial thickness >10% TBSA and any full thickness burn go to the burns unit; the resuscitation skeleton is ACLS-style ABCDE, where exposure means finding the cause and extent."),
    (S2, "Singed nasal hair, hoarseness, carbonaceous sputum, closed-room or face/neck burns and altered sensorium all point to airway burns — intubate prophylactically because the airway collapses fast."),
    (S3, "Airway burns run hypoxia → ARDS-like bilateral infiltrates at 24-48 h → bronchopneumonia (S. aureus early, gram negatives late). Add smoke, CO's hemoglobin grip and a chest eschar strangling expansion to the hypoxia list."),
    (S4, "Burn mediators vasodilate: <10% TBSA stays a local immune event, >10% goes systemic, and leaky 12-24 h vessels spill albumin into the third space."),
    (S5, "Crystalloids follow Parkland (4 × kg × %TBSA, half in 8 h, half in 16 h, Ringer lactate, 1° burns excluded) or modified Brooke (2 ×); colloids come after 12 h by Muir & Barclay. Children <14 get 3 mL/kg/%, infants add sugar maintenance; electrical injuries get 4 mL until urine clears; Galveston covers pediatric crystalloid."),
    (S6, "Palm = 1% for small burns, Wallace's rule of 9s for adults (arm 9, head 9, trunk 18 each half, leg 18, perineum 1), children shift volume to the head (18%) and legs (13.5%), and the Lund & Browder chart is the best method overall."),
    (S7, "The wound is three zones: central coagulation (irreversible), surrounding stasis (capillary damage + edema — salvageable into hyperemia if well managed, necrosis if not), and outer hyperemia from vasodilation; G-CSF receptor downregulation blunts local immunity."),
    (S8, "1st degree = epidermis (sunburn, blanching red, heals 3-5 d); superficial 2nd = papillary dermis (blisters, 2-3 weeks, no scar); deep 2nd = whole dermis (thrombosed vessels, keloids); 3rd = subcutaneous fat and 4th = muscle — charred, painless, needing early excision and STSG."),
    (S9, "Wash with room-temperature water, decompress the ileus-prone stomach (Ryle's in >15-20%), never burst blisters or give IM/SC injections. Circumferential eschar drives pressures >30 mm Hg — severe pain and pain on passive flexion demand escharotomy down to deep fascia until muscle is exposed."),
    (S10, "Energy multipliers stack 1 / 1.4 / 1.8 / 2 (severe burns = 40 kcal/kg/day) via Curreri/Sutherland; days 5-10 run negative nitrogen balance so 20% of nutrition must be protein (Davies formula)."),
    (S11, "Dressings aim to protect, decontaminate and heal: expose 1st degree, vaseline/collagen for superficial 2nd, hydrocolloid (Duoderm) for deep 2nd. Silver sulphadiazine 1% remains the m/c agent (frequent changes, no eschar penetration), silver nitrate stains black, mafenide 5% penetrates eschar but burns and acidifies, and cesium nitrate — the best — is an immunomodulator with a price tag."),
    (S12, "Hypertrophic scars settle alone, keloids get triamcinolone, contractures get V-Y/Z-plasty, Marjolin's ulcer a wide excision. Death runs asphyxia → hypovolemic shock (1-3 d) → septic shock, the overall top killer, with Pseudomonas the usual organism."),
    (S13, "Alkali bites deeper than acid; flood with water and never neutralize — brush powders off first. Hydrofluoric acid chelates calcium (↓Ca²⁺, ↑K⁺, acidosis) and is treated with calcium gluconate by gel, mouth, IV or IA."),
    (S14, "Electrical burns are 3°/4°: DC blocks the heart, AC tetanises muscle into myoglobinuria (flood with fluids to dodge ATN), and arrhythmia kills most. Trace entry and exit wounds, excise early and graft; lightning splits into direct (high-grade, arrhythmias) and indirect filigree spark burns."),
    (S15, "Thirty minutes of cold drops the core: stage I shivering 35-32°C, stage II 32-28°C with J/Osborne waves, stage III 28-24°C unconscious with vitals, stage IV <24°C flat. Rewarm passively (mild), actively externally (mild-moderate), internally (moderate-severe) and with CPB/ECMO (best, severe); core temp reads best rectally and must normalise before death is declared."),
    (S16, "Frostbite = dry cold freezing ice crystals into tissue; rewarming then vasodilates and free radicals cause reperfusion injury. Trench foot = wet cold with microvascular stasis. Rewarm fast at 40°C, never rub, fix hyperkalemia and acidosis, and amputate gangrene only at the demarcation line."),
]

first_page = {}
for x in Q:
    first_page.setdefault(x["sec"], x["page"])

UNITS = []
for i, (title, guide) in enumerate(UNIT_DEFS, 1):
    UNITS.append({
        "id": f"SURG-U58-{i}",
        "ch": 58,
        "n": i,
        "title": title,
        "sec": f"{title} · p{first_page[title]}",
        "qs": [x["id"] for x in Q if x["sec"] == title],
        "guide": guide,
    })

covered = [x for u in UNITS for x in u["qs"]]
assert covered == [x["id"] for x in Q]
assert len(set(covered)) == len(covered)
with open("data/ch58.json", "w", encoding="utf-8") as f:
    json.dump({"questions": Q, "units": UNITS}, f, ensure_ascii=False, indent=1)
print(f"ch58: {len(Q)} questions, {len(UNITS)} units")
