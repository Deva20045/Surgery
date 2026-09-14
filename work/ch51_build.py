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
S1 = "Types of Grafts and STSG vs FTSG"
q(386, S1, "Autograft is a graft from:", "Same person", ["Identical twin", "Same species", "Different species"])
q(386, S1, "Isograft is a graft between:", "Identical twins", ["Same person", "Same species", "Different species"])
q(386, S1, "Allograft is a graft between:", "Same species", ["Same person", "Identical twins", "Different species"])
q(386, S1, "Xenograft is a graft between:", "Different species", ["Same person", "Identical twins", "Same species"])
q(386, S1, "A graft taken from the same person is called:", "Autograft", ["Isograft", "Allograft", "Xenograft"])
q(386, S1, "A graft between identical twins is called:", "Isograft", ["Autograft", "Allograft", "Xenograft"])
q(386, S1, "A graft between individuals of the same species is called:", "Allograft", ["Autograft", "Isograft", "Xenograft"])
q(386, S1, "A graft between different species is called:", "Xenograft", ["Autograft", "Isograft", "Allograft"])
q(386, S1, "Grafts don't have their own blood supply and therefore:", "Rely on recipient tissue", ["Rely on donor vessels", "Carry a vascular pedicle", "Never survive"])
q(386, S1, "Unlike grafts, flaps:", "Have their own blood supply", ["Rely on recipient tissue", "Are always avascular", "Never carry vessels"])
q(386, S1, "Split thickness skin graft (STSG) is also known as:", "Thiersch graft (Thin)", ["Wolfe graft", "Whole skin graft", "Pedicle graft"])
q(386, S1, "Full thickness skin graft (FTSG) is also known as:", "Wolfe graft (Whole skin)", ["Thiersch graft", "Thin graft", "Mesh graft"])
q(386, S1, "The m/c donor site for STSG is:", "Anterolateral thigh", ["Buttocks", "Post-auricular region", "Infraclavicular fossa"])
q(386, S1, "Another donor site for STSG is:", "Buttocks", ["Post-auricular region", "Supraclavicular fossa", "Sole"])
q(386, S1, "Donor sites for FTSG include:", "Infra/supraclavicular fossa", ["Anterolateral thigh", "Buttocks", "Scalp only"])
q(386, S1, "Another donor site for FTSG is:", "Post-auricular region", ["Buttocks", "Anterolateral thigh", "Sole"])
q(386, S1, "FTSG is never taken from:", "Axilla", ["Post-auricular region", "Supraclavicular fossa", "Infraclavicular fossa"])
q(386, S1, "Donor site mortality in STSG is:", "Minimal (Only dressing required)", ["Higher (Sutures required)", "Always needs suturing", "Needs flap cover"])
q(386, S1, "At an STSG donor site:", "Site can be re-used", ["Site cannot be re-used", "Sutures are mandatory", "Skin is lost fully"])
q(386, S1, "Donor site mortality in FTSG is:", "Higher (Sutures required)", ["Minimal (Only dressing)", "Nil", "Same as STSG"])
q(386, S1, "At an FTSG donor site:", "Site cannot be re-used", ["Site can be re-used", "Only dressing suffices", "Heals without sutures"])
q(386, S1, "Composition of STSG is:", "Epidermis + parts of dermis", ["Epidermis + entire dermis", "Epidermis only", "Dermis only"])
q(386, S1, "Composition of FTSG is:", "Epidermis + entire dermis", ["Epidermis + parts of dermis", "Epidermis only", "Dermis + fat"])
q(386, S1, "Primary contracture in STSG is:", "Less", ["More", "Equal to FTSG", "Absent"])
q(386, S1, "Primary contracture in FTSG is:", "More", ["Less", "Equal to STSG", "Absent"])
q(386, S1, "Secondary contracture in STSG is:", "More", ["Less", "Equal to FTSG", "Absent"])
q(386, S1, "Secondary contracture in FTSG is:", "Less", ["More", "Equal to STSG", "Absent"])
q(386, S1, "Survival/take-up of STSG is:", "Better", ["Worse", "Equal to FTSG", "Nil"])
q(386, S1, "Survival/take-up of FTSG is:", "Worse", ["Better", "Equal to STSG", "Always 100%"])
q(386, S1, "Resistance to trauma in STSG is:", "Less resistant", ["More resistant", "Equal to FTSG", "Fully resistant"])
q(386, S1, "Resistance to trauma in FTSG is:", "More resistant", ["Less resistant", "Equal to STSG", "Nil"])
q(386, S1, "Cosmetic result of STSG is:", "Worse (Darkens with time)", ["Better colour matching", "Always excellent", "Same as FTSG"])
q(386, S1, "Cosmetic result of FTSG is:", "Better colour matching", ["Worse (Darkens with time)", "Always poor", "Same as STSG"])

# ------------------------------------------------------------------ p387
S2 = "Contracture, Meshing, Graft Survival and Graft Failure"
q(387, S2, "1° contracture is graft shrinkage upon:", "Lifting from donor site", ["Placing at recipient site", "Meshing", "Storage in cold"])
q(387, S2, "1° contracture is proportional to:", "Dermis", ["1/dermis", "Epidermis", "Fat"])
q(387, S2, "2° contracture is graft shrinkage upon:", "Placing at recipient site", ["Lifting from donor site", "Harvesting", "Meshing"])
q(387, S2, "2° contracture is proportional to:", "1/dermis", ["Dermis", "Epidermis", "Fat"])
q(387, S2, "Meshing cuts made to STSG increase surface area by:", "1.5 times", ["2.5 times", "3 times", "0.5 times"])
q(387, S2, "Meshing of STSG also:", "Prevents seroma formation", ["Causes seroma", "Increases contracture", "Delays take"])
q(387, S2, "The imbibition phase of graft survival lasts:", "24-48 hours", ["2-4 days", "After 4 days", "6-8 days"])
q(387, S2, "During imbibition the graft survives by:", "Plasmatic transfer of nutrients", ["Buds from donor", "New vessels", "Diffusion from air"])
q(387, S2, "The inosculation phase of graft survival lasts:", "2-4 days", ["24-48 hours", "After 4 days", "1 week"])
q(387, S2, "During inosculation:", "Buds from donor extract nutrition", ["Plasmatic transfer occurs", "Both ends form new vessels", "Graft is avascular"])
q(387, S2, "Neovascularisation of a graft occurs:", "After 4 days", ["At 24-48 hours", "At 2-4 days", "At 12 hours"])
q(387, S2, "In neovascularisation:", "Both ends form new vessels", ["Only donor forms vessels", "Only recipient forms vessels", "No vessels form"])
q(387, S2, "The m/c cause of graft failure is:", "Seroma/hematoma beneath the graft", ["Infection", "Movement", "Poor recipient bed"])
q(387, S2, "Seroma/hematoma causes graft failure by:", "Hampering imbibition", ["Hampering inosculation only", "Causing rejection", "Drying the graft"])
q(387, S2, "Seroma/hematoma beneath the graft:", "Lifts it up", ["Fixes it down", "Improves take", "Prevents infection"])
q(387, S2, "Infection causing graft failure is classically due to:", "Beta-hemolytic streptococci, staphylococcus", ["E. coli only", "Pseudomonas only", "Candida only"])
q(387, S2, "Movement causes graft failure through:", "Shearing force", ["Compression", "Tension only", "Ischemia only"])
q(387, S2, "A poor recipient bed shows increased:", "Fibrotic/granulation tissue", ["Vascularity", "Fat", "Muscle"])
q(387, S2, "Excess fibrotic/granulation tissue on a recipient bed:", "Must be debrided", ["Must be grafted directly", "Improves take", "Needs steroids"])
q(387, S2, "A poor recipient bed lacks:", "Periosteum/perichondrium/perineurium", ["Fat", "Muscle", "Lymphatics"])

# ------------------------------------------------------------------ p388-389
S3 = "Flaps: Random Flaps and Local Flap Techniques"
q(388, S3, "A flap is a piece of tissue having:", "Its own blood supply", ["No blood supply", "Recipient-dependent supply", "Only venous drainage"])
q(388, S3, "A random flap is rotated on:", "Dermal plexus", ["A named artery", "A named vein", "Muscle perforators only"])
q(388, S3, "A random flap is based on:", "Dermal blood supply", ["Named axial vessels", "Deep fascia vessels", "Bone vessels"])
q(388, S3, "The ideal length : breadth ratio of a random flap is:", "3:1", ["1:1", "2:1", "4:1"])
q(388, S3, "Long random flaps with a narrower base:", "Do not survive", ["Survive best", "Need delay always", "Become axial"])
q(388, S3, "Uses of random flaps include:", "Post burn contractures, cleft palate repair", ["Mandibular reconstruction", "Breast reconstruction", "Limb replantation"])
q(388, S3, "Angles that can be made in Z-plasty are:", "30°, 45° and 60°", ["15°, 30° and 45°", "45°, 60° and 90°", "60°, 75° and 90°"])
q(388, S3, "Z-plasty is used to:", "Increase length of wound", ["Decrease length of wound", "Close wounds under no tension", "Drain seroma"])
q(388, S3, "A 60° angle Z-plasty gives a length gain of:", "75% (Max elongation)", ["50%", "100%", "25%"])
q(388, S3, "Maximum elongation in Z-plasty is obtained at:", "60° angle", ["30° angle", "45° angle", "90° angle"])
q(388, S3, "V-Y plasty is used for:", "Elongation of wound", ["Shortening of wound", "Widening of scar", "Deepening of defect"])
q(388, S3, "Rhomboid flap is used for:", "Reconstruction of tissue", ["Elongation of wound", "Debridement", "Drainage"])
q(388, S3, "Rhomboid flap is used for basal cell carcinoma and:", "Pilonidal sinus", ["Bed sore only", "Burn contracture", "Cleft palate"])
q(389, S3, "Bilobed flap is used for:", "Tip of nose reconstruction", ["Eyelid reconstruction", "Lip reconstruction", "Cheek reconstruction"])
q(389, S3, "Bipedicled flap is used for:", "Eyelid reconstruction", ["Tip of nose reconstruction", "Floor of mouth", "Forehead defects"])
q(389, S3, "Bilobed and bipedicled flaps are classically used in:", "Basal cell carcinoma", ["Squamous cell carcinoma", "Melanoma", "Sarcoma"])

# ------------------------------------------------------------------ p389
S4 = "Axial Flaps and Head & Neck Reconstruction Flaps"
q(389, S4, "An axial flap is rotated on:", "A named blood vessel", ["Dermal plexus", "Random vessels", "Subdermal plexus only"])
q(389, S4, "In an axial flap the tissue:", "Is still attached to donor site", ["Is fully disconnected", "Needs microvascular anastomosis", "Is always free"])
q(389, S4, "The Mathes and Nahai classification divides axial flaps based on:", "Pedicles", ["Size", "Site", "Thickness"])
q(389, S4, "Mathes and Nahai type V flap has:", "Dominant pedicle (1) + minor pedicles (multiple)", ["Only one pedicle", "Two dominant pedicles", "No pedicle"])
q(389, S4, "Examples of Mathes and Nahai type V flaps are:", "Pectoralis major flap and latissimus dorsi flap", ["Deltopectoral flap", "Radial forearm flap", "Fibular flap"])
q(389, S4, "The deltopectoral flap (DP) is based on:", "Perforators of internal mammary artery", ["Pectoral branch of thoracoacromial artery", "Labial vessels", "Submental vessels"])
q(389, S4, "The m/c used flap by head and neck surgeons is:", "Pectoralis major myocutaneous flap (PMMC)", ["Deltopectoral flap", "Latissimus dorsi flap", "Karapandzic flap"])
q(389, S4, "PMMC flap is based on:", "Pectoral branch of thoracoacromial artery", ["Perforators of internal mammary artery", "Labial vessels", "Thoracodorsal artery"])
q(389, S4, "PMMC flap is shown classically for:", "Floor of mouth cancer", ["Tip of nose", "Eyelid", "Scalp defects"])
q(389, S4, "Abbe-Estlander flap is based on:", "Labial vessels", ["Internal mammary perforators", "Thoracoacromial artery", "Facial artery only"])
q(389, S4, "Abbe-Estlander flap serves the:", "Oral cavity, floor and angle of mouth", ["Nasal tip", "Eyelid", "Hard palate"])
q(389, S4, "Karapandzic flap is a:", "Lip switch flap for oral cancer reconstruction", ["Nasal switch flap", "Cheek advancement flap", "Brow flap"])

# ------------------------------------------------------------------ p390
S5 = "Axial Flaps for Breast Reconstruction: LD, TRAM, DIEP and SIA"
q(390, S5, "Latissimus dorsi flap is used for:", "Breast reconstruction", ["Nose reconstruction", "Eyelid reconstruction", "Penile reconstruction"])
q(390, S5, "Tissue included in a TRAM flap is:", "Skin + s/c + fat + muscle", ["Skin + s/c + fat", "Skin + fat only", "Skin only"])
q(390, S5, "Tissue included in a DIEP flap is:", "Skin + s/c + fat", ["Skin + s/c + fat + muscle", "Muscle only", "Skin + muscle"])
q(390, S5, "TRAM flap with superior epigastric vessels works as a:", "Axial flap", ["Free flap", "Random flap", "Perforator-only flap"])
q(390, S5, "TRAM flap with inferior epigastric vessels works as a:", "Free flap", ["Axial flap", "Random flap", "Pedicle flap"])
q(390, S5, "Using both epigastric systems in a TRAM flap gives a:", "'Supercharged TRAM'", ["Delayed TRAM", "Standard TRAM", "Failed TRAM"])
q(390, S5, "Abdominal wall morbidity after TRAM flap is:", "Increased (d/t muscle removal)", ["Decreased (muscle spared)", "Absent", "Same as DIEP"])
q(390, S5, "TRAM flap increases the risk of:", "Incisional hernia", ["Inguinal hernia", "Femoral hernia", "Umbilical hernia only"])
q(390, S5, "The DIEP flap is based on:", "Deep inferior epigastric artery perforator", ["Superior epigastric artery", "Superficial inferior epigastric artery", "Internal mammary perforator"])
q(390, S5, "The DIEP flap is used as a:", "Free flap", ["Random flap", "Delay flap", "Local flap"])
q(390, S5, "Abdominal wall morbidity after DIEP flap is:", "Decreased (muscle not removed)", ["Same as TRAM", "Very high", "Unknown"])
q(390, S5, "DIEP flap decreases the risk of:", "Incisional hernia", ["Hiatus hernia", "Femoral hernia", "No effect on hernia"])
q(390, S5, "The abdominal incision for TRAM/DIEP flap is:", "Elliptical (Same for both TRAM/DIEP)", ["Transverse only for DIEP", "Oblique", "Circular"])
q(390, S5, "The best flap for breast reconstruction is:", "DIEP flap", ["LD flap", "SIA flap", "PMMC flap"])
q(390, S5, "SIA flap stands for:", "Superficial inferior epigastric artery flap", ["Subcutaneous inferior artery flap", "Superficial internal axillary flap", "Septal inferior artery flap"])

# ------------------------------------------------------------------ p391
S6 = "Free Flaps, Allen's Test and Fibular Flap"
q(391, S6, "A free flap is:", "Disconnected from donor site", ["Rotated on dermal plexus", "Always pedicled", "Never revascularised"])
q(391, S6, "At the recipient site a free flap needs:", "Microvascular anastomosis", ["Skin grafting", "Delay procedure", "No vessels joined"])
q(391, S6, "In a radial artery forearm flap the flap is disconnected from:", "Arm", ["Forearm never disconnected", "Chest", "Back"])
q(391, S6, "Before excising a radial artery forearm flap one must do:", "Allen's test", ["Adson's test", "Tinel test", "Phalen test"])
q(391, S6, "Allen's test checks:", "Radio-ulnar patency", ["Brachial patency", "Digital veins", "Ulnar nerve"])
q(391, S6, "In the modified Allen's test the palm becomes:", "Blanched on clinching", ["Flushed on clinching", "Cyanosed at rest", "Pulseless"])
q(391, S6, "In the modified Allen's test initially:", "Ulnar and radial arteries are occluded", ["Only radial is occluded", "Brachial is occluded", "No occlusion"])
q(391, S6, "Allen's test is positive when the released ulnar artery is:", "Patent", ["Not patent", "Spasmodic", "Absent"])
q(391, S6, "Allen's test is negative when the released ulnar artery is:", "Not patent", ["Patent", "Dilated", "Normal"])
q(391, S6, "The radial artery forearm flap harvest includes the:", "Cephalic vein", ["Basilic vein", "Subclavian vein", "No vein"])
q(391, S6, "Muscles related to the radial forearm flap diagram are brachioradialis and:", "Flexor carpi ulnaris", ["Flexor carpi radialis only", "Palmaris longus", "Extensor digitorum"])
q(391, S6, "The free fibular flap is based on:", "Peroneal vessels", ["Anterior tibial vessels", "Posterior tibial vessels", "Popliteal vessels"])
q(391, S6, "The best flap for mandibular reconstruction is:", "Free fibular flap", ["Radial forearm flap", "Deltopectoral flap", "TRAM flap"])
q(391, S6, "In the free fibular flap diagram the artery arising from the popliteal artery is:", "Anterior tibial artery", ["Musculocutaneous artery", "Posterior tibial artery only", "Genicular artery"])
q(391, S6, "The free fibular flap harvest carries a:", "Muscle cuff", ["Skin paddle only", "Nerve graft", "Vein only"])

# ------------------------------------------------------------------ p392
S7 = "Composite/Conjoined/Chimeric Flaps, Flap Failure and Skin Banking"
q(392, S7, "A composite flap has:", "More than one component present", ["A single component", "Only muscle", "Only bone"])
q(392, S7, "Examples of composite flaps are:", "PMMC, TRAM, DIEP", ["Z-plasty, V-Y plasty", "Rhomboid, bilobed", "Random flaps only"])
q(392, S7, "In a conjoined flap the components share:", "Perforators from a common mother vessel with skin between", ["Separate mother vessels", "Only venous drainage", "Random supply"])
q(392, S7, "In a chimeric flap the components A and B are:", "Separate, each on perforators of the same mother vessel", ["Joined by a skin bridge", "On different mother vessels", "Randomly supplied"])
q(392, S7, "The best method of flap monitoring is:", "Handheld doppler", ["Pinprick method", "Temperature probe", "Daily angiography"])
q(392, S7, "In the pinprick method of flap monitoring the flap is pricked to check:", "Perfusion (Bleeding)", ["Sensation", "Colour only", "Turgor"])
q(392, S7, "In arterial flap failure the temperature is:", "Cold", ["Warm", "Hot", "Variable"])
q(392, S7, "In venous flap failure the temperature is:", "Warm", ["Cold", "Freezing", "Normal"])
q(392, S7, "In arterial flap failure the colour is:", "Pale", ["Congested", "Blue", "Red"])
q(392, S7, "In venous flap failure the colour is:", "Congested", ["Pale", "Yellow", "Pale pink"])
q(392, S7, "Capillary refill in arterial flap failure is:", "Delayed", ["Quick", "Absent always", "Brisk"])
q(392, S7, "Capillary refill in venous flap failure is:", "Quick", ["Delayed", "Slow", "Normal"])
q(392, S7, "On pin-prick an arterial flap shows:", "Decreased blood flow", ["Increased blood flow", "Venous ooze", "No prick response"])
q(392, S7, "On pin-prick a venous flap shows:", "Increased blood flow", ["Decreased blood flow", "Arterial spurting", "Dry surface"])
q(392, S7, "In skin banking, split thickness skin grafts can be stored for:", "2-3 weeks", ["2-3 days", "1 week", "6 months"])
q(392, S7, "Skin banking preserves grafts using:", "Liquid nitrogen/CO2 snow at 4°C", ["Room temperature saline", "Formalin at 37°C", "Alcohol at −20°C"])

# ------------------------------------------------------------------ units
def first_page(title):
    return next(x["page"] for x in Q if x["sec"] == title)

UNIT_DEFS = [
    (S1, "Grafts are avascular pieces of tissue that live off the recipient bed — autograft from self, isograft between identical twins, allograft within a species and xenograft across species — while flaps carry their own blood supply. Split-thickness Thiersch grafts (epidermis plus part of dermis) from anterolateral thigh or buttocks take better, contract secondarily, reuse their donor site with only a dressing but darken with time, whereas full-thickness Wolfe grafts (epidermis plus entire dermis) from infra/supraclavicular fossa or post-auricular skin (never axilla) need sutures, lose their donor site, resist trauma and match colour best."),
    (S2, "Primary contracture shrinks the graft as it leaves the donor site in proportion to dermis, while secondary contracture shrinks it on the recipient bed in proportion to 1/dermis; meshing multiplies STSG surface area 1.5 times and prevents seroma. Take proceeds through imbibition (24-48 h of plasmatic nutrition), inosculation (2-4 days of donor buds extracting nutrition) and neovascularisation after 4 days when both ends form new vessels. Failure is led by seroma/hematoma lifting the graft and hampering imbibition, then beta-hemolytic streptococcal/staphylococcal infection, shearing movement and poor beds loaded with fibrotic/granulation tissue or lacking periosteum, perichondrium or perineurium."),
    (S3, "A flap is tissue with its own blood supply; random flaps pivot on the dermal plexus at an ideal 3:1 length-breadth ratio because longer flaps with narrow bases die, and they serve post-burn contractures and cleft palate. Z-plasty at 30, 45 or 60 degrees lengthens wounds with 75% gain at 60 degrees, V-Y plasty elongates wounds and rhomboid flaps reconstruct tissue in BCC and pilonidal sinus. Bilobed flaps rebuild the nasal tip and bipedicled flaps the eyelid, both classically in basal cell carcinoma."),
    (S4, "Axial flaps rotate on named vessels while staying attached to the donor site, and Mathes-Nahai type V flaps pair one dominant pedicle with multiple minor ones as in pectoralis major and latissimus dorsi. For head and neck reconstruction the deltopectoral flap runs on internal mammary perforators while the pectoralis-major myocutaneous flap on the pectoral branch of the thoracoacromial artery is the workhorse, typically for floor-of-mouth cancer. The Abbe-Estlander flap on labial vessels covers oral cavity, floor and angle of mouth, and the Karapandzic lip-switch flap reconstructs oral cancer lips."),
    (S5, "Breast reconstruction options run from the latissimus dorsi flap to abdominal flaps: TRAM carries skin, subcutis, fat and muscle on superior epigastric (axial) or inferior epigastric (free) vessels, both together giving a supercharged TRAM, but muscle sacrifice doubles abdominal morbidity and incisional hernia risk. DIEP takes only skin, subcutis and fat on the deep inferior epigastric perforator as a free flap, sparing muscle, cutting hernia risk and ranking as the best breast flap, with the same elliptical abdominal incision as TRAM. The superficial inferior epigastric artery (SIA) flap completes the set."),
    (S6, "Free flaps are disconnected from the donor site and revascularised by microvascular anastomosis at the recipient bed. The radial artery forearm flap is lifted from the arm only after Allen's test proves radio-ulnar patency — clinched blanched palm with both arteries occluded, then ulnar release: refill is a positive test, no refill negative — and carries the cephalic vein between brachioradialis and flexor carpi ulnaris. The free fibular flap on peroneal vessels, with its muscle cuff off the anterior tibial-peroneal axis, is the best flap for mandibular reconstruction."),
    (S7, "Composite flaps bundle more than one component (PMMC, TRAM, DIEP), conjoined flaps keep components joined by skin over shared perforators of one mother vessel, and chimeric flaps hang separate components off perforators of the same mother vessel. Failing flaps are monitored best by handheld doppler or by pinprick bleeding; arterial failure is cold, pale, slow-refilling with decreased pinprick flow while venous failure is warm, congested, quick-refilling with increased flow. Banked split-thickness grafts keep for 2-3 weeks under liquid nitrogen or CO2 snow at 4°C."),
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
