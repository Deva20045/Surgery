#!/usr/bin/env python3
"""Build data/ch51.json — Plastic Surgery : Part 1 (Marrow Surgery Ed 8, pp386-392)."""
import json

Q = []

def q(page, sec, text, correct, wrongs, note=None):
    opts = [correct] + list(wrongs)
    assert len(opts) == 4
    Q.append({
        "id": f"SURG-C51-{len(Q)+1:03d}",
        "sec": sec,
        "page": page,
        "q": text,
        "opts": opts,
        "ans": 0,
        "exp": (note or correct) + f" (Book p{page})",
    })

# ------------------------------------------------------------------ p386
S1 = "Types of Grafts and Skin Grafting: STSG vs FTSG"
q(386, S1, "The chapter 'Plastic Surgery : Part 1' is placed under which book section?", "Speciality Surgery", ["Trauma Surgery", "Vascular Surgery", "Hernia"])
q(386, S1, "An autograft is a graft taken from:", "Same person", ["Identical twin", "Same species", "Different species"])
q(386, S1, "An isograft is a graft taken from:", "Identical twin", ["Same person", "Same species", "Different species"])
q(386, S1, "An allograft is a graft taken from:", "Same species", ["Same person", "Identical twin", "Different species"])
q(386, S1, "A xenograft is a graft taken from:", "Different species", ["Same person", "Identical twin", "Same species"])
q(386, S1, "Grafts differ from flaps in that grafts:", "Don't have their own blood supply", ["Have their own blood supply", "Are always full thickness", "Never take on the recipient"])
q(386, S1, "Grafts survive by relying on:", "Recipient tissue", ["Donor tissue", "Their own pedicle", "Dermal plexus of the graft"])
q(386, S1, "Flaps, unlike grafts:", "Have their own blood supply", ["Rely on recipient tissue", "Are always meshed", "Never survive primarily"])
q(386, S1, "Split thickness skin graft (STSG) is also known as:", "Thiersch graft", ["Wolfe graft", "Pinch graft", "Tube graft"])
q(386, S1, "STSG is described as a:", "Thin graft", ["Whole skin graft", "Thick graft", "Composite graft"])
q(386, S1, "Full thickness skin graft (FTSG) is also known as:", "Wolfe graft", ["Thiersch graft", "Mesh graft", "Flap graft"])
q(386, S1, "FTSG consists of:", "Whole skin", ["Epidermis only", "Parts of dermis only", "Skin with muscle"])
q(386, S1, "The m/c donor site for STSG is:", "Anterolateral thigh", ["Buttocks", "Axilla", "Post-auricular region"])
q(386, S1, "Another donor site listed for STSG is:", "Buttocks", ["Anterolateral thigh only", "Axilla", "Infraclavicular fossa"])
q(386, S1, "A donor site for FTSG is:", "Infra/supraclavicular fossa", ["Anterolateral thigh", "Buttocks", "Scalp"])
q(386, S1, "Another donor site for FTSG is:", "Post-auricular region", ["Axilla", "Buttocks", "Anterolateral thigh"])
q(386, S1, "FTSG is never harvested from:", "Axilla", ["Post-auricular region", "Infraclavicular fossa", "Supraclavicular fossa"])
q(386, S1, "Donor site mortality with STSG is:", "Minimal (only dressing required)", ["Higher (sutures required)", "Absent always", "Needs grafting of donor site"])
q(386, S1, "After STSG harvest the donor site:", "Can be re-used", ["Cannot be re-used", "Needs suturing", "Needs a flap"])
q(386, S1, "Donor site mortality with FTSG is:", "Higher (sutures required)", ["Minimal (only dressing required)", "Nil", "Same as STSG"])
q(386, S1, "After FTSG harvest the donor site:", "Cannot be re-used", ["Can be re-used", "Epithelialises from dermal remnants", "Needs no closure"])
q(386, S1, "STSG is composed of:", "Epidermis + parts of dermis", ["Epidermis + entire dermis", "Epidermis only", "Entire dermis only"])
q(386, S1, "FTSG is composed of:", "Epidermis + entire dermis", ["Epidermis + parts of dermis", "Epidermis only", "Dermis + fat"])
q(386, S1, "Primary contracture in STSG is:", "Less", ["More", "Absent", "Same as FTSG"])
q(386, S1, "Primary contracture in FTSG is:", "More", ["Less", "Absent", "Same as STSG"])
q(386, S1, "Secondary contracture in STSG is:", "More", ["Less", "Absent", "Same as FTSG"])
q(386, S1, "Secondary contracture in FTSG is:", "Less", ["More", "Absent", "Same as STSG"])
q(386, S1, "Survival/take-up of STSG is:", "Better", ["Worse", "Equal to FTSG", "Unpredictable"])
q(386, S1, "Survival/take-up of FTSG is:", "Worse", ["Better", "Equal to STSG", "Always complete"])
q(386, S1, "To trauma, STSG is:", "Less resistant", ["More resistant", "Fully resistant", "Equal to FTSG"])
q(386, S1, "To trauma, FTSG is:", "More resistant", ["Less resistant", "Fragile always", "Equal to STSG"])
q(386, S1, "Cosmetic result of STSG is:", "Worse (darkens with time)", ["Better colour matching", "Identical to FTSG", "Always excellent"])
q(386, S1, "Cosmetic result of FTSG is:", "Better colour matching", ["Worse (darkens with time)", "Same as STSG", "Poor always"])

# ------------------------------------------------------------------ p387
S2 = "Contracture, Meshing and Graft Survival"
q(387, S2, "1° contracture is:", "Graft shrinkage upon lifting from donor site", ["Graft shrinkage upon placing at recipient site", "Graft shrinkage after 4 days", "Graft shrinkage due to infection"])
q(387, S2, "1° contracture is proportional to:", "Dermis", ["1/dermis", "Epidermis", "Fat"])
q(387, S2, "2° contracture is:", "Graft shrinkage upon placing at recipient site", ["Graft shrinkage upon lifting from donor site", "Shrinkage during storage", "Shrinkage during meshing"])
q(387, S2, "2° contracture is proportional to:", "1/dermis", ["Dermis", "Epidermis", "Mesh ratio"])
q(387, S2, "Meshing means:", "Cuts made to STSG", ["Cuts made to FTSG", "Suturing the graft edges", "Debriding the recipient bed"])
q(387, S2, "Meshing increases the surface area of STSG by:", "1.5 times", ["2.5 times", "3 times", "0.5 times"])
q(387, S2, "Meshing of STSG prevents:", "Seroma formation", ["Infection", "Shearing", "Contracture"])
q(387, S2, "The first phase of graft survival is:", "Imbibition", ["Inosculation", "Neovascularisation", "Epithelialisation"])
q(387, S2, "Imbibition lasts:", "24-48 hours", ["2-4 days", "After 4 days", "6-12 hours"])
q(387, S2, "In imbibition the graft is nourished by:", "Plasmatic transfer of nutrients", ["Buds from donor", "New vessels from both ends", "Direct arterial inflow"])
q(387, S2, "The second phase of graft survival is:", "Inosculation", ["Imbibition", "Neovascularisation", "Organisation"])
q(387, S2, "Inosculation occurs at:", "2-4 days", ["24-48 hours", "After 4 days", "Day 7-10"])
q(387, S2, "In inosculation:", "Buds from donor extract nutrition", ["Plasma imbibes into the graft", "Both ends form new vessels", "Lymphatics reconnect first"])
q(387, S2, "Neovascularisation begins:", "After 4 days", ["At 24-48 hours", "At 2-4 days", "Within 12 hours"])
q(387, S2, "In neovascularisation:", "Both ends form new vessels", ["Plasmatic transfer feeds the graft", "Only donor buds feed the graft", "No vessels form"])
q(387, S2, "The m/c cause of graft failure is:", "Seroma/hematoma beneath the graft", ["Infection", "Movement", "Poor recipient bed"])
q(387, S2, "Seroma/hematoma causes graft failure by:", "Lifting the graft up and hampering imbibition", ["Shearing the graft", "Infecting the graft", "Devascularising the donor site"])
q(387, S2, "Infection causing graft failure is classically due to:", "β-hemolytic streptococci and staphylococcus", ["Pseudomonas only", "E. coli only", "Anaerobes only"])
q(387, S2, "Movement causes graft failure through:", "Shearing force", ["Compression", "Tension", "Torsion"])
q(387, S2, "A poor recipient bed causes graft failure due to:", "↑ fibrotic/granulation tissue", ["↑ vascularity", "↓ bacterial load", "Excess periosteum"])
q(387, S2, "Excess fibrotic/granulation tissue on a recipient bed must be:", "Debrided", ["Grafted over directly", "Left to mature", "Injected with steroids"])
q(387, S2, "Grafts take poorly on beds lacking:", "Periosteum/perichondrium/perineurium", ["Muscle", "Fat", "Fascia"])

# ------------------------------------------------------------------ p388
S3 = "Flaps and Random Flaps: Z-plasty, V-Y and Rhomboid"
q(388, S3, "A flap is defined as:", "A piece of tissue having its own blood supply", ["A piece of tissue without blood supply", "A free graft of whole skin", "A meshed split graft"])
q(388, S3, "Random flaps are rotated on:", "Dermal plexus", ["A named artery", "Muscle perforators", "Fascial plexus only"])
q(388, S3, "Random flaps are based on:", "Dermal blood supply", ["Named blood vessel", "Axial vessels", "Perforator vessels"])
q(388, S3, "The ideal length : breadth ratio of a random flap is:", "3:1", ["1:1", "2:1", "4:1"])
q(388, S3, "Long flaps with a narrower base:", "Do not survive", ["Survive best", "Need delay always", "Become axial"])
q(388, S3, "A use of random flaps is:", "Post burn contractures", ["Mandibular reconstruction", "Breast reconstruction", "Tip of nose reconstruction"])
q(388, S3, "Another use of random flaps is:", "Cleft palate repair", ["Floor of mouth cancer", "Pilonidal sinus", "Eyelid reconstruction"])
q(388, S3, "Angles that can be made in Z-plasty include:", "30°, 45° and 60°", ["15°, 30° and 45°", "45°, 60° and 90°", "Only 60°"])
q(388, S3, "Z-plasty is used to:", "↑ length of wound", ["↓ length of wound", "Close circular defects", "Cover bare bone"])
q(388, S3, "A 60° angle Z-plasty gives a length gain of:", "75%", ["50%", "100%", "25%"])
q(388, S3, "Maximum elongation in Z-plasty is obtained with the angle:", "60°", ["30°", "45°", "90°"])
q(388, S3, "V-Y plasty is used for:", "Elongation of wound", ["Shortening of wound", "Nose tip reconstruction", "Breast reconstruction"])
q(388, S3, "Rhomboid flap is used for:", "Reconstruction of tissue", ["Elongation of wound", "Debridement", "Meshing of grafts"])
q(388, S3, "Rhomboid flap is classically illustrated for:", "Basal cell carcinoma", ["Pilonidal sinus only", "Melanoma", "Squamous cell carcinoma"])
q(388, S3, "Rhomboid flap is also classically used for:", "Pilonidal sinus", ["Basal cell carcinoma only", "Bed sore of heel", "Dupuytren contracture"])

# ------------------------------------------------------------------ p389
S4 = "Bilobed/Bipedicled Flaps and Axial Flaps for Head and Neck"
q(389, S4, "Bilobed flap is used for:", "Tip of nose reconstruction", ["Eyelid reconstruction", "Lip reconstruction", "Cheek reconstruction"])
q(389, S4, "Bipedicled flap is used for:", "Eyelid reconstruction", ["Tip of nose reconstruction", "Scalp reconstruction", "Neck reconstruction"])
q(389, S4, "Bilobed and bipedicled flaps are classically employed in:", "Basal cell carcinoma", ["Pilonidal sinus", "Burn contracture", "Oral cancer"])
q(389, S4, "Axial flaps are rotated on:", "A named blood vessel", ["Dermal plexus", "Random subdermal plexus", "Any vein"])
q(389, S4, "Unlike free flaps, an axial (pedicled) flap remains:", "Attached to donor site", ["Disconnected completely", "Frozen for later use", "Attached to recipient only"])
q(389, S4, "Mathes and Nahai classification classifies:", "Axial flaps based on pedicles", ["Random flaps based on dermis", "Free flaps based on veins", "Grafts based on thickness"])
q(389, S4, "Mathes-Nahai Type V flaps have:", "Dominant pedicle (1) + minor pedicles (multiple)", ["Only one pedicle", "Two dominant pedicles", "No dominant pedicle"])
q(389, S4, "Examples of Mathes-Nahai Type V flaps are:", "Pectoralis major flap and latissimus dorsi flap", ["Deltopectoral and radial forearm flaps", "TRAM and DIEP flaps", "Fibular and scapular flaps"])
q(389, S4, "The deltopectoral flap (DP) is based on:", "Perforators of internal mammary artery", ["Pectoral branch of thoracoacromial artery", "Labial vessels", "Superficial temporal artery"])
q(389, S4, "The m/c used flap by head and neck surgeons is:", "Pectoralis major myocutaneous flap (PMMC)", ["Deltopectoral flap", "Latissimus dorsi flap", "Radial forearm flap"])
q(389, S4, "PMMC is based on:", "Pectoral branch of thoracoacromial artery", ["Perforators of internal mammary artery", "Labial vessels", "Facial artery"])
q(389, S4, "PMMC flap is classically shown covering:", "Floor of mouth cancer", ["Tip of nose defect", "Pilonidal sinus", "Breast defect"])
q(389, S4, "Abbe-Estlander flap is based on:", "Labial vessels", ["Facial artery", "Internal mammary perforators", "Pectoral branch of thoracoacromial artery"])
q(389, S4, "Abbe-Estlander flap serves the:", "Oral cavity, floor and angle of mouth", ["Tip of nose", "Eyelid", "Scalp"])
q(389, S4, "Karapandzic flap is a:", "Lip switch flap", ["Nose switch flap", "Cheek advancement flap", "Neck rotation flap"])
q(389, S4, "Karapandzic flap is used for:", "Oral cancer reconstruction", ["Nasal reconstruction", "Eyelid reconstruction", "Breast reconstruction"])

# ------------------------------------------------------------------ p390
S5 = "Flaps for Breast Reconstruction: LD, TRAM vs DIEP and SIA"
q(390, S5, "A flap listed for breast reconstruction is:", "Latissimus dorsi flap", ["Deltopectoral flap", "Radial forearm flap", "Fibular flap"])
q(390, S5, "TRAM stands for:", "Transverse rectus abdominis myocutaneous flap", ["Transverse rectus abdominis mesh flap", "Total rectus abdominis myocutaneous flap", "Transverse radial artery myocutaneous flap"])
q(390, S5, "DIEP stands for:", "Deep inferior epigastric artery perforator flap", ["Deep internal epigastric artery pedicle flap", "Distal inferior epigastric artery perforator flap", "Deep iliac epigastric perforator flap"])
q(390, S5, "Tissue included in a TRAM flap is:", "Skin + s/c + fat + muscle", ["Skin + s/c + fat", "Skin + fat only", "Skin + muscle only"])
q(390, S5, "Tissue included in a DIEP flap is:", "Skin + s/c + fat", ["Skin + s/c + fat + muscle", "Muscle + fascia", "Skin only"])
q(390, S5, "In TRAM, superior epigastric vessels give a:", "Axial flap", ["Free flap", "Perforator flap", "Random flap"])
q(390, S5, "In TRAM, inferior epigastric vessels give a:", "Free flap", ["Axial flap", "Pedicled random flap", "Conjoined flap"])
q(390, S5, "Using both epigastric systems in TRAM produces a:", "'Supercharged TRAM'", ["'Supercharged DIEP'", "Double TRAM", "Turbo LD flap"])
q(390, S5, "A DIEP flap is a:", "Free flap", ["Axial pedicled flap", "Random flap", "Conjoined flap"])
q(390, S5, "DIEP flap is based on:", "Deep inferior epigastric artery perforator", ["Superior epigastric artery", "Superficial inferior epigastric artery", "Internal mammary perforator"])
q(390, S5, "Abdominal wall morbidity in TRAM is ↑↑ because:", "Muscle is removed", ["Muscle is preserved", "Skin is thin", "Fat is excess"])
q(390, S5, "TRAM flap increases the risk of:", "Incisional hernia", ["Inguinal hernia", "Femoral hernia", "Umbilical hernia"])
q(390, S5, "Abdominal wall morbidity in DIEP is ↓ because:", "Muscle is not removed", ["Muscle is removed", "Incision is vertical", "Mesh is always used"])
q(390, S5, "The abdominal incision for TRAM/DIEP is:", "Elliptical (same for both)", ["Vertical midline", "Transverse straight", "Curvilinear oblique"])
q(390, S5, "The best flap for breast reconstruction is:", "DIEP flap", ["TRAM flap", "Latissimus dorsi flap", "SIA flap"])
q(390, S5, "SIA flap stands for:", "Superficial inferior epigastric artery flap", ["Superior iliac artery flap", "Superficial iliac circumflex artery flap", "Septal inferior epigastric artery flap"])

# ------------------------------------------------------------------ p391
S6 = "Free Flaps: Radial Forearm and Free Fibular"
q(391, S6, "A free flap is:", "Disconnected from donor site with microvascular anastomosis at recipient site", ["Left attached to its donor pedicle", "A graft with random supply", "A flap rotated on dermal plexus"])
q(391, S6, "The radial artery forearm flap is disconnected from:", "Arm", ["Leg", "Chest", "Back"])
q(391, S6, "Before excising a radial forearm flap, which test is mandatory?", "Allen's test", ["Trendelenburg test", "Adson's test", "Finkelstein test"])
q(391, S6, "Allen's test checks:", "Radio-ulnar patency", ["Brachial patency", "Cephalic vein patency", "Ulnar nerve function"])
q(391, S6, "In the modified Allen's test the palm is:", "Clenched and blanched with radial and ulnar arteries occluded", ["Open and warm", "Elevated only", "Dependent and congested"])
q(391, S6, "Allen's positive means:", "Ulnar artery released and patent (radial occluded)", ["Ulnar artery released and not patent", "Both arteries patent", "Radial artery released and patent"])
q(391, S6, "Allen's negative means:", "Ulnar artery released and not patent", ["Ulnar artery released and patent", "Radial artery patent", "Both arteries occluded"])
q(391, S6, "The vein harvested with the radial artery forearm flap is:", "Cephalic vein", ["Basilic vein", "Median cubital vein", "Radial venae comitantes only"])
q(391, S6, "Muscles labelled around the radial forearm flap harvest are:", "Brachioradialis and flexor carpi ulnaris", ["Biceps and triceps", "Flexor digitorum profundus only", "Pronator quadratus and supinator"])
q(391, S6, "The free fibular flap is based on:", "Peroneal vessels", ["Anterior tibial vessels", "Posterior tibial vessels", "Popliteal vessels"])
q(391, S6, "The best flap for mandibular reconstruction is:", "Free fibular flap", ["Radial forearm flap", "PMMC flap", "Scapular flap"])
q(391, S6, "In the free fibular flap diagram the artery proximal to the pedicle is:", "Popliteal artery", ["Femoral artery", "Anterior tibial artery", "Dorsalis pedis artery"])
q(391, S6, "The fibular pedicle in the diagram is taken with a:", "Muscle cuff", ["Skin paddle only", "Fascial sleeve only", "Bone-only segment"])

# ------------------------------------------------------------------ p392
S7 = "Composite/Conjoined/Chimeric Flaps, Flap Failure and Skin Banking"
q(392, S7, "A composite flap is one with:", "More than one component present", ["A single component", "No vascular component", "Only skin"])
q(392, S7, "Examples of composite flaps include:", "PMMC, TRAM, DIEP", ["Z-plasty and V-Y plasty", "Rhomboid and bilobed flaps", "STSG and FTSG"])
q(392, S7, "In the conjoined flap diagram, territories A and B are joined by:", "Skin over perforators of one mother vessel", ["Separate mother vessels", "A vein graft", "No connection"])
q(392, S7, "In the chimeric flap diagram, territories A and B each receive:", "Perforators from the same mother vessel", ["Perforators from different mother vessels", "Direct cutaneous veins", "Random dermal supply"])
q(392, S7, "The best method of flap monitoring is:", "Handheld doppler", ["Pinprick method", "Clinical colour only", "Temperature probe only"])
q(392, S7, "In the pinprick method the flap is pricked to check:", "Perfusion (bleeding)", ["Sensation", "Tension", "Thickness"])
q(392, S7, "In arterial flap failure the temperature is:", "Cold", ["Warm", "Hot", "Normal"])
q(392, S7, "In venous flap failure the temperature is:", "Warm", ["Cold", "Cool", "Frozen"])
q(392, S7, "In arterial flap failure the colour is:", "Pale", ["Congested", "Blue-black", "Flushed"])
q(392, S7, "In venous flap failure the colour is:", "Congested", ["Pale", "White", "Blanched"])
q(392, S7, "In arterial flap failure capillary refill is:", "Delayed", ["Quick", "Absent always", "Normal"])
q(392, S7, "In venous flap failure capillary refill is:", "Quick", ["Delayed", "Absent", "Normal"])
q(392, S7, "Pin-prick in arterial flap failure shows:", "↓ blood flow", ["↑ blood flow", "Brisk bleeding", "No change"])
q(392, S7, "Pin-prick in venous flap failure shows:", "↑ blood flow", ["↓ blood flow", "Dry prick", "No bleeding"])
q(392, S7, "In skin banking, split thickness skin grafts can be stored for:", "2-3 weeks", ["2-3 days", "2-3 months", "1 year"])
q(392, S7, "Skin banking preserves grafts using:", "Liquid nitrogen/CO2 snow at 4°C", ["Formalin at room temperature", "Saline at 37°C", "Dry ice at −80°C"])

# ------------------------------------------------------------------ units
def first_page(title):
    return next(x["page"] for x in Q if x["sec"] == title)

UNIT_DEFS = [
    (S1, "Grafts borrow their blood supply from the recipient bed while flaps carry their own: autografts come from the same person, isografts from identical twins, allografts from the same species and xenografts across species. Split-thickness Thiersch grafts (epidermis plus parts of dermis) are cut from the anterolateral thigh or buttocks with minimal, re-usable donor morbidity, take better and resist trauma less, contracting less primarily but more secondarily and darkening with time; full-thickness Wolfe grafts (whole skin) come from infra/supraclavicular fossa or post-auricular skin, never the axilla, need sutures at a non-re-usable donor site, contract more primarily but less secondarily, take worse yet resist trauma and match colour better."),
    (S2, "First-degree contracture shrinks the graft as it leaves the donor site in proportion to dermis, while second-degree contracture shrinks it on the recipient bed in inverse proportion; meshing cuts STSG to raise surface area 1.5-fold and prevent seroma. Survival runs imbibition (24-48 h, plasmatic nutrient transfer) through inosculation (2-4 days, donor buds extract nutrition) to neovascularisation (after 4 days, both ends form new vessels). Failure is led by seroma/hematoma lifting the graft and blocking imbibition, then β-hemolytic streptococcal/staphylococcal infection, shearing movement and poor beds rich in fibrotic/granulation tissue that must be debrided or lacking periosteum, perichondrium or perineurium."),
    (S3, "A flap is tissue with its own blood supply; random flaps pivot on the dermal plexus at an ideal 3:1 length-to-breadth ratio because longer narrow-based flaps die, serving post-burn contractures and cleft palate repair. Their workhorses are Z-plasty (30°, 45°, 60° angles to lengthen wounds, the 60° version gaining 75% for maximal elongation), V-Y plasty for wound elongation and the rhomboid flap for tissue reconstruction, classically shown closing basal cell carcinoma and pilonidal sinus defects."),
    (S4, "Bilobed flaps rebuild the nasal tip and bipedicled flaps the eyelid, both classically in basal cell carcinoma. Axial flaps rotate on a named vessel while staying attached to the donor site, graded by the Mathes-Nahai pedicle classification whose Type V (one dominant plus multiple minor pedicles) covers pectoralis major and latissimus dorsi; for head and neck work the deltopectoral flap rides internal mammary perforators, PMMC (pectoral branch of thoracoacromial artery) is the surgeon's workhorse for floor-of-mouth cancer, and the labial-vessel Abbe-Estlander flap plus the Karapandzic lip-switch flap reconstruct the oral cavity, floor, angle of mouth and lip cancers."),
    (S5, "Breast reconstruction options run from the latissimus dorsi flap to abdominal flaps: TRAM carries skin, subcutis, fat and muscle on superior epigastric (axial) or inferior epigastric (free) vessels, both together making a 'supercharged TRAM', whereas DIEP carries only skin, subcutis and fat on the deep inferior epigastric artery perforator as a free flap. Because TRAM sacrifices muscle it doubles abdominal wall morbidity and incisional hernia risk while DIEP spares muscle and lowers both, through the same elliptical abdominal incision; DIEP is the best breast flap, alongside the superficial inferior epigastric artery (SIA) flap."),
    (S6, "Free flaps are disconnected from the donor and re-plumbed by microvascular anastomosis at the recipient: the radial artery forearm flap leaves the arm with the cephalic vein between brachioradialis and flexor carpi ulnaris after Allen's test proves radio-ulnar patency (modified test clenches a blanched palm with both arteries occluded; positive = ulnar release refills a patent palm, negative = no refill). The free fibular flap rides the peroneal vessels off the popliteal axis with a muscle cuff beside the anterior tibial artery and is the best flap for mandibular reconstruction."),
    (S7, "Composite flaps carry more than one component (PMMC, TRAM, DIEP), conjoined flaps join two territories by skin over perforators of one mother vessel and chimeric flaps take separate territories on perforators of the same mother vessel. Failing flaps are watched best with a handheld doppler or by pinprick bleeding; arterial failure is cold, pale, slow-refilling with ↓ pinprick flow while venous failure is warm, congested, quick-refilling with ↑ flow. Spare split-thickness grafts are banked for 2-3 weeks under liquid nitrogen or CO2 snow at 4°C."),
]

UNITS = []
for i, (title, guide) in enumerate(UNIT_DEFS, 1):
    UNITS.append({
        "id": f"SURG-U51-{i}",
        "ch": 51,
        "n": i,
        "title": title,
        "sec": f"{title} · p{first_page(title)}",
        "qs": [x["id"] for x in Q if x["sec"] == title],
        "guide": guide,
    })

covered = [x for u in UNITS for x in u["qs"]]
assert covered == [x["id"] for x in Q]
assert len(set(covered)) == len(covered)
with open("data/ch51.json", "w", encoding="utf-8") as f:
    json.dump({"questions": Q, "units": UNITS}, f, ensure_ascii=False, indent=1)
print(f"ch51: {len(Q)} questions, {len(UNITS)} units")
