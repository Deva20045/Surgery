#!/usr/bin/env python3
"""Build data/ch52.json — Plastic Surgery : Part 2 (Marrow Surgery Ed 8, pp393-398)."""
import json

Q = []

def q(page, sec, text, correct, wrongs, note=None):
    opts = [correct] + list(wrongs)
    assert len(opts) == 4
    Q.append({
        "id": f"SURG-C52-{len(Q)+1:03d}",
        "sec": sec,
        "page": page,
        "q": text,
        "opts": opts,
        "ans": 0,
        "exp": (note or correct) + f" (Book p{page})",
    })

# ------------------------------------------------------------------ p393
S1 = "Bed Sores/Pressure Sores: Grading and Management"
q(393, S1, "Pressure sores are formed when constant pressure exceeds:", ">30 mmHg", [">15 mmHg", ">60 mmHg", ">90 mmHg"])
q(393, S1, "The same pressure threshold (>30 mmHg) is quoted for:", "Compartment syndrome", ["Crush syndrome", "Tourniquet palsy", "Raynaud phenomenon"])
q(393, S1, "The m/c site of bed sores is:", "Ischium", ["Greater trochanter", "Sacrum", "Heel"])
q(393, S1, "The second commonest site of bed sores is:", "Greater trochanter", ["Ischium", "Sacrum", "Heel"])
q(393, S1, "In the bed-sore site order Ischium > Greater trochanter > Sacrum > Heel, the least common listed site is:", "Heel", ["Sacrum", "Greater trochanter", "Ischium"])
q(393, S1, "Stage 1 pressure sore is:", "Non-blanchable erythema of intact skin", ["Partial thickness skin loss with exposed dermis", "Full thickness skin loss", "Full thickness skin and tissue loss"])
q(393, S1, "Stage 1 pressure sore treatment includes:", "Keep area dry", ["Debridement and VAC", "Flap closure", "Immediate suturing"])
q(393, S1, "Offloading in stage 1 bed sores is achieved with:", "Air/water mattress", ["Ripple bed of steel", "Hard board", "Sand bag"])
q(393, S1, "Opsite spray in stage 1 bed sores:", "Prevents ↑ staging", ["Treats infection", "Debrides slough", "Closes the ulcer"])
q(393, S1, "Stage 2 pressure sore is:", "Partial thickness skin loss with exposed dermis", ["Non-blanchable erythema of intact skin", "Full thickness skin loss", "Full thickness skin and tissue loss"])
q(393, S1, "Stage 3 pressure sore is:", "Full thickness skin loss", ["Partial thickness skin loss with exposed dermis", "Full thickness skin and tissue loss", "Non-blanchable erythema"])
q(393, S1, "Stage 4 pressure sore is:", "Full thickness skin and tissue loss", ["Full thickness skin loss", "Partial thickness skin loss", "Intact skin with erythema"])
q(393, S1, "Stages 2-3 pressure sores are treated by:", "Debridement → VAC dressing (−ve pressure)", ["Debridement → flap closure", ["Opsite spray only"] , "Primary suturing"])
q(393, S1, "Stage 4 pressure sores are treated by:", "Debridement → flap closure (Eg: Tensor fascia lata flap)", ["Debridement → VAC dressing", ["Opsite spray"] , "Offloading alone"])
q(393, S1, "An example flap for stage 4 bed sore closure is:", "Tensor fascia lata flap", ["Deltopectoral flap", ["Radial forearm flap"] , "Free fibular flap"])
q(393, S1, "'Unstageable full-thickness pressure injury' means:", "Obscured full-thickness skin and tissue loss", ["Persistent non-blanchable deep red discoloration", ["Partial thickness loss"] , "Intact skin with blanchable erythema"])
q(393, S1, "'Deep tissue pressure injury' shows:", "Persistent, non-blanchable, deep red/maroon/purple discoloration (skin intact)", ["Obscured full-thickness loss", ["Blanchable erythema"] , "Exposed dermis"])

# ------------------------------------------------------------------ p394
S2 = "Bed Sore Prevention and VAC Dressing"
q(394, S2, "A predisposing factor for bed sores is:", "Wheelchair bound patient", ["Ambulant patient", ["Young age"] , "High serum albumin"])
q(394, S2, "Poor nutritional status predisposing to bed sores is marked by:", "↓ S. albumin", ["↑ S. albumin", ["↑ S. globulin"] , "↓ S. calcium"])
q(394, S2, "Another predisposing local factor for bed sores is:", "Wet/macerated area", ["Dry skin", ["Well-padded bony prominences"] , "Clean skin"])
q(394, S2, "Adequate nutrition for bed-sore prevention means:", "Monitor and correct S. albumin", ["High fat diet", ["Fluid restriction"] , "Vitamin A megadose"])
q(394, S2, "The bedsheet for a bedridden patient should be:", "Dry + no wrinkles", ["Wet and smooth", ["Dry with wrinkles"] , "Synthetic and damp"])
q(394, S2, "A bed-bound patient should be repositioned:", "Every 2 hours", ["Every 30 minutes", ["Every 6 hours"] , "Once daily"])
q(394, S2, "A wheelchair-bound patient should lift for 10 sec:", "Every 10 minutes", ["Every 2 hours", ["Every 30 minutes"] , "Every 5 minutes"])
q(394, S2, "An air/water mattress is used when:", "The patient is unable to change position (offloading)", ["The patient is ambulant", ["Infection is present"] , "The sore is stage 4"])
q(394, S2, "VAC dressing stands for:", "Vacuum assisted closure", ["Vascular access catheter", ["Vacuum applied compression"] , "Vapour assisted closure"])
q(394, S2, "VAC dressing applies a negative pressure occlusive dressing of:", "−125 mmHg", ["−75 mmHg", ["−250 mmHg"] , "−20 mmHg"])
q(394, S2, "VAC hastens wound healing by:", "Sucking out dead tissue", ["Adding growth factors", ["Keeping the wound dry"] , "Immobilising the limb"])
q(394, S2, "VAC ↑ vascularity; its m/c complication is:", "Bleeding", ["Infection", ["Flap necrosis"] , "Pain only"])
q(394, S2, "Increased vascularity with VAC leads to:", "↑ cytokines/cells for healing", ["↓ cytokines", ["Fibrosis"] , "Ischemia"])
q(394, S2, "An indication for VAC dressing is:", "Chronic non-healing wounds", ["Untreated osteomyelitis", ["Malignant wound"] , "Dry eschar"])
q(394, S2, "VAC can be used on a venous ulcer only when it is:", "Without slough", ["With slough", ["Infected"] , "Ischemic"])
q(394, S2, "VAC can be used on burn wounds only when they are:", "Without eschar", ["With eschar", ["Full thickness only"] , "Circumferential"])
q(394, S2, "For bed sores, VAC is applied:", "After debridement", ["Before debridement", ["Instead of debridement"] , "Only in stage 1"])
q(394, S2, "VAC is indicated in diabetic ulcer only when there is no:", "Osteomyelitis", ["Neuropathy", ["Ischemia"] , "Callus"])

# ------------------------------------------------------------------ p394-395
S3 = "Wound Healing: Phases, Cells and Wound Strength"
q(394, S3, "The correct order of wound healing phases is:", "Hemostasis → Inflammatory → Proliferative → Remodelling", ["Inflammatory → Hemostasis → Proliferative → Remodelling", ["Hemostasis → Proliferative → Inflammatory → Remodelling"] , "Remodelling → Proliferative → Inflammatory → Hemostasis"])
q(394, S3, "The inflammatory phase of wound healing lasts:", "Upto 4 days", ["Upto 24 hours", ["Upto 14 days"] , "Upto 3 months"])
q(394, S3, "In the inflammatory phase, neutrophils (acute phase) are later replaced by:", "Macrophages", ["Fibroblasts", ["Lymphocytes"] , "Mast cells"])
q(395, S3, "The proliferative phase begins:", "After 4 days", ["After 24 hours", ["After 14 days"] , "After 3 months"])
q(395, S3, "In the proliferative phase the predominant cells are:", "Macrophages and fibroblasts", ["Neutrophils and lymphocytes", ["Platelets and mast cells"] , "Keratinocytes only"])
q(395, S3, "Fibroblasts in the proliferative phase lay down:", "Type 3 collagen (disorganised)", ["Type 1 collagen (organised)", ["Type 4 collagen"] , "Elastin only"])
q(395, S3, "In the remodelling phase:", "Type 1 collagen replaces type 3 in a ratio 4:1", ["Type 3 collagen replaces type 1 in a ratio 4:1", ["Type 1 replaces type 3 in a ratio 1:4"] , "Collagen is completely removed"])
q(395, S3, "Wound strength at 1 week is about:", "~10% of normal", ["~50% of normal", ["~70-80% of normal"] , "~100% of normal"])
q(395, S3, "Wound strength at 3 months is about:", "70-80% of normal (maximum)", ["10% of normal", ["40-50% of normal"] , "100% of normal"])
q(395, S3, "With time a healed wound:", "Never regains original strength", ["Regains original strength by 6 months", ["Exceeds original strength"] , "Regains strength only if sutured"])
q(395, S3, "The matrix-changes graph of wound healing plots collagen I, collagen III, fibronectin and:", "Wound strength", ["Epithelial thickness", ["Vascularity"] , "Tensile elasticity"])
q(394, S3, "The cellular-changes graph of wound healing plots neutrophils, macrophages, fibroblasts and:", "Lymphocytes", ["Platelets", ["Keratinocytes"] , "Mast cells"])
q(394, S3, "On the wound healing timeline the maturation phase extends upto:", "36 months", ["14 days", ["6 months"] , "12 months"])

# ------------------------------------------------------------------ p395-396
S4 = "Factors Affecting Wound Healing and Types of Healing"
q(395, S4, "A local factor affecting wound healing is:", "Foreign body", ["Anemia", ["Steroids"] , "Malnutrition"])
q(395, S4, "Another local factor affecting wound healing is:", "Radiation", ["Vitamin C deficiency", ["Immunocompromise"] , "Diabetes"])
q(395, S4, "A systemic factor affecting wound healing is:", "Anemia", ["Foreign body", ["Trauma"] , "Infection"])
q(395, S4, "Malnutrition impairs wound healing when S. albumin is:", "<3 gm/dL", ["<5 gm/dL", ["<1 gm/dL"] , ">4 gm/dL"])
q(395, S4, "Vitamin C deficiency causes:", "Abnormal collagen/matrix deposition", ["Inhibition of inflammatory phase", ["Excess granulation"] , "Early epithelialisation"])
q(395, S4, "Steroids impair healing by:", "Inhibiting the inflammatory phase", ["Causing abnormal collagen deposition", ["Lysing fibroblasts"] , "Blocking angiogenesis only"])
q(395, S4, "If steroids must be continued around injury, they should only be restarted:", "3-4 days post injury", ["Immediately", ["After 3 weeks"] , "After 3 months"])
q(395, S4, "Primary intention healing is seen in:", "Sutured wound", ["Gaping irregular wound", ["Left-open wound"] , "Infected wound"])
q(395, S4, "Primary intention healing shows:", "Minimal granulation", ["↑ granulation", ["↑ contracture"] , "Bad scar"])
q(395, S4, "The scar of primary intention healing is:", "Good scar with minimal wound contracture", ["Keloid", ["Hypertrophic"] , "Wide and contracted"])
q(395, S4, "Secondary intention healing means:", "Wound left open", ["Wound sutured immediately", ["Wound resutured late"] , "Wound grafted"])
q(395, S4, "Secondary intention healing shows:", "↑ granulation and contracture", ["Minimal granulation", ["Minimal contracture"] , "Hairline scar"])
q(395, S4, "Time to heal in secondary intention is:", "↑ (increased)", ["↓ (decreased)", ["Same as primary"] , "Nil"])
q(395, S4, "Secondary intention healing ends in:", "Bad scar (keloid/hypertrophic)", ["Hairline scar", ["Good scar"] , "No scar"])
q(396, S4, "Tertiary intention healing means:", "Wound initially left open, then resutured once healthy granulation tissue (+)", ["Wound sutured immediately", ["Wound never sutured"] , "Wound grafted primarily"])
q(396, S4, "Tertiary intention healing ends with:", "Late suturing with wide scar", ["Hairline scar", ["No scar"] , "Minimal scar"])

# ------------------------------------------------------------------ p396
S5 = "Keloids vs Hypertrophic Scars"
q(396, S5, "Keloids are characterised by:", "↑ type III collagen", ["↓ type III collagen", ["↑ type I collagen only"] , "No collagen change"])
q(396, S5, "The m/c site of keloids is:", "Sternum", ["Ear lobe", ["Shoulders"] , "Extensor surfaces"])
q(396, S5, "Other classic keloid sites include:", "Ear lobe and shoulders", ["Palms and soles", ["Scalp only"] , "Flexures"])
q(396, S5, "Hypertrophic scars classically occur on:", "Extensor surfaces", ["Sternum", ["Ear lobe"] , "Flexor surfaces"])
q(396, S5, "Keloids are predisposed in:", "Dark skin", ["Children", ["Fair skin"] , "Elderly"])
q(396, S5, "Hypertrophic scars are predisposed in:", "Children", ["Dark skin adults", ["Elderly"] , "Pregnancy"])
q(396, S5, "Keloid growth characteristically:", "Grows beyond the boundary of scar", ["Grows within the boundary of scar", ["Stops at epithelialisation"] , "Never grows"])
q(396, S5, "Hypertrophic scar growth:", "Grows within the boundary of scar", ["Grows beyond the boundary", ["Invades deeper fascia"] , "Metastasises"])
q(396, S5, "With time/pressure a keloid:", "Does not subside", ["Subsides", ["Disappears"] , "Blanches"])
q(396, S5, "With time/pressure a hypertrophic scar:", "Subsides", ["Does not subside", ["Enlarges"] , "Ulcerates"])
q(396, S5, "The clinical feature of a keloid is:", "Raised, red, itchy lesion", ["Flat pale lesion", ["Depressed atrophic lesion"] , "Pigmented macule"])
q(396, S5, "First-line treatment of keloids is:", "Intralesional triamcinolone", ["Silicon gel pads", ["Excision always"] , "Radiotherapy alone"])
q(396, S5, "Recurrent keloids are treated with:", "Sx excision, laser/radiotherapy", ["Intralesional triamcinolone only", ["Silicon gel pads"] , "Pressure garments alone"])
q(396, S5, "Hypertrophic scars are treated with:", "Silicon gel pads", ["Intralesional triamcinolone", ["Sx excision"] , "Radiotherapy"])

# ------------------------------------------------------------------ p396-397
S6 = "Cleft Lip and Palate: Epidemiology, Risk Factors and Documentation"
q(396, S6, "The incidence of cleft lip/palate is:", "1 in 600 live births", ["1 in 60 live births", ["1 in 6000 live births"] , "1 in 60,000 live births"])
q(396, S6, "Cleft lip/palate occurs:", "Males > females", ["Females > males", ["Equally"] , "Only in males"])
q(396, S6, "The m/c cleft defect is:", "Combined lip + palate", ["Isolated cleft lip", ["Isolated cleft palate"] , "Alveolar cleft"])
q(396, S6, "A maternal intake risk factor for clefting is:", "Phenytoin", ["Folic acid", ["Penicillin"] , "Iron"])
q(396, S6, "Other maternal intake risk factors for clefting include:", "Anti-epileptics and steroids", ["Antibiotics", ["Antacids"] , "Antihistamines"])
q(396, S6, "The genetic risk factor for clefting listed is:", "Pierre Robin syndrome", ["Down syndrome", ["Turner syndrome"] , "Marfan syndrome"])
q(396, S6, "Pierre Robin syndrome shows:", "Retrognathia with posteriorly displaced tongue", ["Prognathia with anterior tongue", ["Macroglossia only"] , "Ankyloglossia"])
q(396, S6, "Pierre Robin syndrome is associated with:", "Isolated cleft palate", ["Combined lip and palate", ["Isolated cleft lip"] , "No cleft"])
q(397, S6, "In cleft documentation, the first 'L' stands for:", "Lip (one side)", ["Lip (other side)", ["Alveolus"] , "Labium majus"])
q(397, S6, "In cleft documentation, 'H' stands for:", "Hard palate", ["Soft palate", ["Hemilip"] , "Hard palate other side"])
q(397, S6, "In cleft documentation, 'S' stands for:", "Soft palate", ["Hard palate", ["Septum"] , "Sinus"])
q(397, S6, "In cleft documentation, a capital letter denotes:", "Complete defect", ["Partial defect", ["Unilateral defect"] , "Bilateral defect"])
q(397, S6, "In cleft documentation, a small letter denotes:", "Partial defect", ["Complete defect", ["Midline defect"] , "Repaired defect"])
q(397, S6, "A child with complete cleft lip with partial alveolar and soft palate defect of 1 side is documented as:", "Las", ["LAS", ["LasH"] , "lAS"])
q(397, S6, "A clinical feature of cleft lip/palate is:", "Cosmetic issues", ["Hearing normality", ["No speech problem"] , "Feeding ease"])
q(397, S6, "Repair of cleft lip/palate must be done before:", "Speech development", ["Dentition", ["Puberty"] , "School admission only for cosmetics"])
q(397, S6, "Feeding problems and middle ear infections are features of:", "Cleft palate", ["Cleft lip only", ["Alveolar cleft only"] , "Both are absent"])

# ------------------------------------------------------------------ p397
S7 = "Cleft Lip and Palate: Management and Complications"
q(397, S7, "Cleft lip surgery is done after:", "3-6 months", ["3-6 weeks", ["12-15 months"] , "1 year"])
q(397, S7, "The (old) Rule of 10 for cleft lip repair includes age:", "10 weeks", ["10 days", ["10 months"] , "10 years"])
q(397, S7, "The Rule of 10 includes weight:", "10 pounds", ["10 kg", ["10 ounces"] , "10 grams"])
q(397, S7, "The Rule of 10 includes haemoglobin:", "10 gm%", ["8 gm%", ["12 gm%"] , "14 gm%"])
q(397, S7, "The m/c repair for cleft lip is:", "Millard repair", ["Wardill-Kilner", ["Von Langenbeck"] , "V-Y plasty"])
q(397, S7, "Soft palate repair is done after:", "3-6 months", ["12-15 months", ["3-6 weeks"] , "2 years"])
q(397, S7, "Hard palate repair is done after:", "12-15 months", ["3-6 months", ["6-9 months"] , "5 years"])
q(397, S7, "Hard palate repair is deliberately delayed to:", "Allow for complete bony growth", ["Allow speech to develop first", ["Reduce anaesthesia risk"] , "Let teeth erupt"])
q(397, S7, "A unipedicled palate surgery type is:", "Wardill-Kilner/V-Y plasty", ["Von Langenbeck repair", ["Millard repair"] , "Furlow repair"])
q(397, S7, "A bipedicled palate surgery type is:", "Von Langenbeck repair", ["Wardill-Kilner", ["V-Y plasty"] , "Millard repair"])
q(397, S7, "A complication of cleft surgery is:", "Bleeding", ["Hypertrophy of scar only", ["Dental caries"] , "Nasal polyps"])
q(397, S7, "Another complication of cleft surgery is:", "Mal-aligned cupid's bow", ["Vermillion excess", ["Nasal septal perforation"] , "Trismus"])
q(397, S7, "Velopharyngeal insufficiency after cleft palate repair means:", "Palate moves with speech", ["Palate fails to elevate ever", ["Nasal regurgitation of solids"] , "Snoring"])
q(397, S7, "The landmark aligned during cleft lip repair is the:", "Vermillion border", ["Alar base only", ["Philtral column only"] , "Nasal sill only"])

# ------------------------------------------------------------------ p398
S8 = "Tissue Expanders"
q(398, S8, "The principle of tissue expanders is:", "Mechanical stimulus → induce tissue growth (generate soft tissue)", ["Chemical stimulus → induce bone growth", ["Thermal stimulus → induce fat growth"] , "Electrical stimulus → induce nerve growth"])
q(398, S8, "Tissue expanders ↑ surface area initially by:", "Stretching", ["Tissue growth", ["Cell migration"] , "Edema"])
q(398, S8, "Later, expander-driven ↑ surface area is by:", "Tissue growth", ["Stretching", ["Elastic recoil"] , "Fluid injection"])
q(398, S8, "A histological change under a tissue expander is:", "Dermal thinning", ["Dermal thickening", ["Epidermal thinning"] , "Fat hypertrophy"])
q(398, S8, "Another histological change under a tissue expander is:", "Epidermal thickening", ["Epidermal thinning", ["Dermal fibrosis"] , "Appendage loss"])
q(398, S8, "Subcutaneous fat under a tissue expander shows:", "Atrophy", ["Hypertrophy", ["Necrosis"] , "No change"])
q(398, S8, "Tissue expansion has:", "No effect on skin appendages", ["Destroyed appendages", ["Increased appendages"] , "Appendage migration"])

# ------------------------------------------------------------------ units
def first_page(title):
    return next(x["page"] for x in Q if x["sec"] == title)

UNIT_DEFS = [
    (S1, "Constant pressure above 30 mmHg — the same figure as compartment syndrome — kills skin over ischium first, then greater trochanter, sacrum and heel. Stage 1 is non-blanchable erythema of intact skin managed by keeping the area dry, offloading on air/water mattresses and Opsite spray to stop upstaging; stage 2 (partial thickness loss with exposed dermis) and stage 3 (full thickness skin loss) need debridement then −ve-pressure VAC, while stage 4 (full thickness skin and tissue loss) needs debridement then flap closure such as the tensor fascia lata flap. Recent updates add unstageable full-thickness pressure injury (obscured loss) and deep tissue pressure injury (persistent non-blanchable deep red/maroon/purple with intact skin)."),
    (S2, "Wheelchair binding, low serum albumin and wet macerated skin set the stage for pressure sores, countered by correcting albumin, keeping bedsheets dry and wrinkle-free, turning bed-bound patients every 2 hours, lifting wheelchair patients 10 seconds every 10 minutes and offloading on air/water mattresses. VAC (vacuum assisted closure) seals the wound at −125 mmHg, sucks out dead tissue and raises vascularity — bleeding being the commonest complication — which floods the wound with cytokines and healing cells; it suits chronic non-healing wounds, slough-free venous ulcers, eschar-free burns, debrided bed sores and diabetic ulcers without osteomyelitis."),
    (S3, "Healing runs hemostasis → inflammatory (upto 4 days, neutrophils handing over to macrophages) → proliferative (after 4 days, macrophages and fibroblasts laying disorganised type 3 collagen) → remodelling, where type 1 collagen replaces type 3 at 4:1. Strength climbs from ~10% of normal at one week to a ceiling of 70-80% at three months and never regains the original; the matrix curve tracks collagen I, collagen III, fibronectin and wound strength while the cellular curve tracks neutrophils, macrophages, fibroblasts and lymphocytes out to a maturation phase of 36 months."),
    (S4, "Local enemies of healing are foreign body, radiation, infection and trauma; systemic ones are anemia, malnutrition with albumin below 3 gm/dL, immunocompromise, vitamin C deficiency causing abnormal collagen/matrix deposition, and steroids that inhibit the inflammatory phase and should only restart 3-4 days post injury. Sutured clean wounds heal by primary intention with minimal granulation, minimal contracture and a good hairline scar; open gaping wounds heal by secondary intention with exuberant granulation, contracture, delayed healing and keloid/hypertrophic scarring; wounds left open then resutured once healthy granulation appears heal by tertiary intention with a wide scar."),
    (S5, "Keloids are type-III-collagen-rich tumours of scar that favour sternum, ear lobe and shoulders in dark-skinned patients, grow beyond the scar boundary, never subside with time or pressure and present as raised, red, itchy lesions treated by intralesional triamcinolone, with recurrences needing excision plus laser/radiotherapy. Hypertrophic scars prefer extensor surfaces in children, stay within the scar boundary, subside with time/pressure and respond to silicon gel pads."),
    (S6, "Cleft lip and palate strike 1 in 600 live births, boys more than girls, most often as combined lip plus palate; maternal phenytoin, anti-epileptics and steroids plus the genetic Pierre Robin syndrome (retrognathia with posteriorly displaced tongue and isolated cleft palate) drive risk. Documentation reads L-A-H-S-A-L across the two sides with capital letters for complete and small letters for partial defects, so a complete lip with partial alveolar and soft palate on one side writes 'Las'. Cosmetics, speech (repair must precede speech development) and, in cleft palate, feeding problems and middle ear infections dominate the clinical picture."),
    (S7, "Cleft lip is closed at 3-6 months once the old Rule of 10 (10 weeks, 10 pounds, 10 gm% Hb) is met, usually by Millard repair; soft palate follows at 3-6 months while hard palate waits till 12-15 months to allow complete bony growth. Palate surgery is unipedicled (Wardill-Kilner/V-Y plasty) or bipedicled (Von Langenbeck), and complications run bleeding, infection, mal-aligned cupid's bow at the vermillion border and velopharyngeal insufficiency with the palate moving during speech."),
    (S8, "Tissue expanders convert mechanical stretch into biological gain: initial surface-area increase comes from stretching and later from true tissue growth, generating extra soft tissue for reconstruction. Under the expander the dermis thins, the epidermis thickens and subcutaneous fat atrophies, while skin appendages remain untouched."),
]

UNITS = []
for i, (title, guide) in enumerate(UNIT_DEFS, 1):
    UNITS.append({
        "id": f"SURG-U52-{i}",
        "ch": 52,
        "n": i,
        "title": title,
        "sec": f"{title} · p{first_page(title)}",
        "qs": [x["id"] for x in Q if x["sec"] == title],
        "guide": guide,
    })

covered = [x for u in UNITS for x in u["qs"]]
assert covered == [x["id"] for x in Q]
assert len(set(covered)) == len(covered)
with open("data/ch52.json", "w", encoding="utf-8") as f:
    json.dump({"questions": Q, "units": UNITS}, f, ensure_ascii=False, indent=1)
print(f"ch52: {len(Q)} questions, {len(UNITS)} units")
