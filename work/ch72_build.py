#!/usr/bin/env python3
"""Build data/ch72.json — Surgical Instruments (pp550-557; p558 is a quote page)."""
import json

Q = []


def q(page, sec, text, correct, wrongs, note=None):
    opts = [correct] + list(wrongs)
    assert len(opts) == 4
    Q.append({
        "id": f"SURG-C72-{len(Q)+1:03d}",
        "sec": sec,
        "page": page,
        "q": text,
        "opts": opts,
        "ans": 0,
        "exp": (note or correct) + f" (Book p{page})",
    })


# --------------------------------------------------------- p550
S1 = "Parts of a Surgical Instrument"
q(550, S1, "Function of the 2 rings of a surgical instrument:", "Gripping", ["Cutting", "Locking only", "Suction"])
q(550, S1, "Purpose of multiple ratchets on an instrument:", "Prevent wear and tear", ["Increase weight", "Allow suction", "Sharpen blades"])
q(550, S1, "Disadvantage of a SCREW joint compared to a box joint:", "Increased incidence of thread getting stuck", ["It is heavier", "It cannot be sterilised", "It has no ratchets"])
q(550, S1, "Types of instrument blades:", "Fenestrated and serrated", ["Sharp and blunt only", "Curved and straight only", "Toothed and ringed"])

S2 = "Sponge Holder, Towel Clips and BP Handle"
q(550, S2, "Blade design of Rampley's sponge holder:", "Fenestrated blade with serrations", ["Toothed solid blade", "Plain smooth blade", "Clawed blade"])
q(550, S2, "Use of Rampley's sponge holder:", "Grip sponge for part preparation", ["Hold bowel", "Clamp vessels", "Retract skin"])
q(550, S2, "Uses of towel clips include all EXCEPT:", "Clamping the aorta", ["Hold towels post draping", "Pass and hold suction catheter/cautery", "Hold tongue during tongue resection"])
q(550, S2, "Mayo's towel clip is characterised by:", "Hooks at the tips", ["Pinch cork effect", "Fenestrated blades", "Longitudinal serrations"])
q(550, S2, "Doyen's towel clip works by:", "The pinch cork effect", ["Hooks piercing tissue", "A ratchet lock only", "Screw joint"])
q(550, S2, "BP handle stands for:", "Brad Parker handle", ["Blunt point handle", "Blade positioning handle", "Basic procedure handle"])
q(550, S2, "Use of the BP handle:", "To mount blades", ["To grip needles", "To retract tissue", "To clamp vessels"])
q(550, S2, "Holding positions of the BP handle:", "Like a paint brush, and the palming grip", ["Pencil grip and tripod grip only", "Two handed grip", "Ring grip"])

# --------------------------------------------------------- p551
S3 = "Suction Cannula and Forceps"
q(551, S3, "Use of Yankauer's suction cannula:", "Suction blood/fumes during surgery", ["Irrigation of the peritoneum", "Insufflation of CO2", "Tissue dissection"])
q(551, S3, "Types of Yankauer's suction cannula:", "Plastic and metallic", ["Curved and straight only", "Toothed and plain", "Fenestrated and serrated"])
q(551, S3, "Forceps used to hold tissues are:", "Spring loaded", ["Ratchet locked", "Screw jointed", "Self retaining"])
q(551, S3, "Types of forceps:", "Plain, toothed, vascular and special", ["Straight and curved only", "Sharp and blunt", "Fenestrated and clawed"])
q(551, S3, "Plain forceps have:", "Transverse serrations without teeth, making them relatively atraumatic", ["Teeth for tough structures", "Minute serrations with raised edges", "No serrations at all"])
q(551, S3, "Toothed forceps are used for:", "Gripping tough structures, but they are traumatic", ["Gripping vessels atraumatically", "Holding sponges", "Retracting bowel"])
q(551, S3, "DeBakey's vascular forceps have:", "Minute serrations with raised edges to grip vascular structures", ["Teeth", "Fenestrated blades", "Longitudinal ridges only"])
q(551, S3, "Russian forceps are characterised by:", "Transverse serration with a gap in between", ["Teeth at the tip", "Minute serrations with raised edges", "No serrations"])

S4 = "Needle Holder and Scissors"
q(551, S4, "Use of a needle holder:", "Grip the needle", ["Hold sponges", "Clamp bleeders", "Retract skin"])
q(551, S4, "Purpose of criss cross serrations on a needle holder:", "Prevent needle movement", ["Increase grip on tissue", "Cut sutures", "Reduce weight"])
q(551, S4, "Where should the needle be held in the needle holder:", "At the 1/3rd-2/3rd junction from the swaged and pointed end respectively", ["At the swaged end", "At the tip", "At the exact midpoint"])
q(551, S4, "Angle at which the needle should enter the skin:", "90°", ["45°", "30°", "60°"])
q(551, S4, "Which forceps grip the needle while suturing:", "Toothed forceps", ["Plain forceps", "DeBakey's forceps", "Babcock forceps"])
q(551, S4, "Mayo scissors are:", "Heavy scissors with a screw joint and blades, used to cut sutures and sheaths", ["Light tissue dissecting scissors", "Fine scissors for ophthalmic surgery", "Scissors for vessels only"])

# --------------------------------------------------------- p552
S5 = "Metzenbaum and McIndoe Scissors"
q(552, S5, "Metzenbaum scissors are also known as:", "Tissue dissecting scissors", ["Heavy suture scissors", "Bone scissors", "Vascular scissors"])
q(552, S5, "Metzenbaum scissors compared with Mayo scissors are:", "Lighter, and suture cutting with them is avoided", ["Heavier, and used to cut sutures", "The same weight", "Used only for bone"])
q(552, S5, "McIndoe scissors are:", "Finer than Metzenbaum, used to cut fine tissues in ophthalmic/ENT surgeries", ["Heavier than Mayo's", "Used for cutting sheaths", "Used for bone nibbling"])
q(552, S5, "Instruments used in skin suturing:", "Needle holder, toothed forceps and scissors", ["Sponge holder, towel clip and BP handle", "Babcock, Allis and Kocher forceps", "Retractors and suction cannula"])

S6 = "Non-self Retaining Retractors"
q(552, S6, "Non-self retaining retractors:", "Need to be held", ["Lock in position themselves", "Attach to the operating table", "Are used only in laparoscopy"])
q(552, S6, "Use of skin hooks:", "Hold raised flaps in mastectomy, thyroidectomy and parotidectomy", ["Retract bowel", "Clamp vessels", "Hold sponges"])
q(552, S6, "Types of skin hooks:", "Single and double handle hooks", ["Sharp and blunt only", "Fenestrated and plain", "Curved and clawed"])
q(552, S6, "Use of the cats paw retractor:", "Retract superficial tissue", ["Retract the bladder", "Retract bowel", "Retract the lung"])
q(552, S6, "Langenbeck retractor is a:", "Right angle retractor used to retract superficial tissue", ["Clawed retractor for suturing", "Self retaining retractor", "Bladder retractor"])
q(552, S6, "Purpose of fenestration in the Langenbeck retractor:", "Makes the instrument lighter", ["Improves visualisation of vessels", "Allows suction", "Prevents slipping"])
q(552, S6, "Broader Langenbeck retractor is used in:", "Cholecystectomy", ["Thyroidectomy", "Parotidectomy", "Mastectomy"])
q(552, S6, "Design of the army navy / Czerney's retractor:", "One end at 90°, the other clawed with a gap", ["Both ends at 90°", "Both ends clawed", "One end fenestrated, one end solid"])
q(552, S6, "Use of the army navy / Czerney's retractor:", "Suturing tissues while retracted", ["Bladder retraction", "Bowel retraction", "Lung retraction"])
q(552, S6, "Advantages of the Morris retractor over Langenbeck's:", "Broader — prevents slipping away of structures, better grip and lighter", ["Narrower and heavier", "Self retaining", "Fenestrated blade for lung expansion"])

# --------------------------------------------------------- p553
S7 = "Doyen's, Malleable and Self-retaining Retractors"
q(553, S7, "Use of Doyen's retractor:", "Bladder retraction", ["Bowel retraction", "Lung retraction", "Thyroid retraction"])
q(553, S7, "Advantage of Doyen's retractor:", "Increased convexity allows easy retraction", ["It is self retaining", "It is fenestrated", "It has claws"])
q(553, S7, "Common use of the malleable retractor:", "Abdominal surgeries for bowel retraction", ["Bladder retraction", "Thyroid retraction", "Rib retraction"])
q(553, S7, "Mastoid retractors are:", "Self retaining superficial tissue retractors used in thyroid/parotid surgeries", ["Non-self retaining bladder retractors", "Deep abdominal retractors", "Rib spreaders"])
q(553, S7, "Balfour self retaining retractor is used for:", "Deeper abdominal structures", ["Superficial neck tissue", "Lung retraction", "Bladder only"])
q(553, S7, "Parts of the Balfour self retaining retractor:", "A bar inserted in the abdomen and adjusted, blades for retraction, and space to attach Doyen's retractor", ["A ring attached to the table with multiple retractors", "Two hooks and a lock", "Fenestrated blades only"])
q(553, S7, "Bookwalter retractor is used in:", "Complex abdominal malignancy surgery", ["Thyroid surgery", "Parotid surgery", "Rib resection"])
q(553, S7, "Parts of the Bookwalter retractor:", "A ring attached to the operating table with space for attachment of multiple retractors", ["A bar with blades only", "Two locking arms", "A fenestrated single blade"])

S8 = "Artery Forceps"
q(553, S8, "Spencer Wells forceps are:", "Straight artery forceps used to hold bleeders, available in various sizes", ["Curved bowel clamps", "Vascular clamps", "Tissue dissecting scissors"])
q(553, S8, "Advantage of curved artery forceps:", "Better visualization", ["Stronger grip only", "Lighter weight", "Self retaining"])
q(553, S8, "Smallest artery forceps:", "Mosquito forceps", ["Spencer Wells forceps", "Kelly's forceps", "Kocher forceps"])

# --------------------------------------------------------- p554
S9 = "Special Forceps"
q(554, S9, "Kelly's forceps are:", "Curved, much bigger forceps with a more gradual curve, used in abdominal surgeries", ["Right angle forceps for pedicles", "Small mosquito forceps", "Fenestrated bowel forceps"])
q(554, S9, "Use of right angle forceps:", "Tie pedicles", ["Hold sponges", "Retract bowel", "Cut sutures"])
q(554, S9, "Allis forceps have:", "Blades with serrations and teeth, making them traumatic", ["Fenestrated ends with a gap", "Plain atraumatic blades", "Interlocking teeth that crush"])
q(554, S9, "Use of Allis forceps:", "Hold tough structures such as sheath/fascia", ["Hold tubular structures", "Hold the cervix", "Clamp vessels"])
q(554, S9, "Babcock forceps are characterised by:", "A gap between two fenestrated ends", ["Serrated toothed blades", "Interlocking teeth", "A right angle curve"])
q(554, S9, "Use and advantage of Babcock forceps:", "Hold tubular structures (appendix/vas/fallopian tubes) without crushing them", ["Crush tough fascia", "Clamp large vessels", "Retract the bladder"])
q(554, S9, "Kocher tissue forceps:", "Interlock and crush tissue", ["Are atraumatic", "Have fenestrated ends", "Are spring loaded"])
q(554, S9, "Uses of Kocher tissue forceps:", "Hold tough structures and hold the cervix during hysterectomy", ["Hold the appendix atraumatically", "Suction fumes", "Retract bowel"])

S10 = "Laparoscopic Instruments and the Veress Needle"
q(554, S10, "Why are laparoscopic instruments long:", "They are operated at depth", ["To reduce weight", "For better sterilisation", "To allow suction"])
q(554, S10, "Why are laparoscopic instruments insulated:", "To prevent current leaking out from cautery", ["To improve grip", "To reduce reflection", "To prevent rusting"])
q(554, S10, "Veress needle is used for:", "The closed method of creating pneumoperitoneum", ["The open Hassan method", "Tissue dissection", "Specimen retrieval"])
q(554, S10, "Mechanism of the Veress needle:", "It is spring loaded — a blunt tip in front that retracts to a bevelled tip on pressing, preventing tissue injury", ["A fixed sharp tip", "A blunt tip only", "A bladeless optical tip"])
q(554, S10, "Parts of the Veress needle include:", "An outlet/inlet valve and a spring loaded blunt tip", ["A ring and ratchets", "Fenestrated blades", "Criss cross serrations"])

# --------------------------------------------------------- p555
S11 = "Laparoscopic Ports and Dissector"
q(555, S11, "Which laparoscopic port is inserted blindly:", "The 1st port", ["The 2nd port", "The last port", "None"])
q(555, S11, "Types of laparoscopic trocar:", "Sharp, blunt (Hassan's trocar) and bladeless (Optiport)", ["Only sharp and curved", "Only metallic and plastic", "Only fenestrated"])
q(555, S11, "Blunt laparoscopic trocar is known as:", "Hassan's trocar", ["Optiport", "Veress trocar", "Maryland trocar"])
q(555, S11, "Advantage of the bladeless Optiport:", "Better visualization", ["Faster insertion only", "Cheaper", "Reusable"])
q(555, S11, "Maryland's dissector is:", "Curved with serrations like an artery forceps — the workhorse of laparoscopic surgery", ["A straight grasper without serrations", "A suction device", "A port"])

S12 = "Thoracotomy Instruments"
q(555, S12, "Periosteal elevator is also called:", "Farabeuf's periosteal elevator", ["Doyen's raspatory", "Allison retractor", "Bone nibbler"])
q(555, S12, "Use of the periosteal elevator:", "Raise periosteum over the rib", ["Cut the rib", "Nibble sharp bone edges", "Retract the lung"])
q(555, S12, "Doyen's rib raspatory is used to:", "Resect periosteum and muscles, with one instrument for each side", ["Cut through the rib", "Retract the lung", "Elevate periosteum only"])
q(555, S12, "Correct position of the rib raspatory:", "Handle lateral, convexity upwards, tip downwards", ["Handle medial, convexity downwards", "Handle lateral, tip upwards", "Convexity downwards, tip upwards"])
q(555, S12, "Why does a rib cutter have a blunt lower edge:", "To prevent pleural injury", ["To make it lighter", "To increase cutting force", "To grip the rib"])
q(555, S12, "Difference between a rib cutter and a bone cutter:", "A bone cutter has sharp edges, while the rib cutter has a blunt lower edge", ["Both have blunt edges", "Both have sharp edges", "The rib cutter is sharper"])
q(555, S12, "Use of the bone nibbler:", "Nibble off sharp edges after cutting bone", ["Cut the rib", "Raise periosteum", "Retract the lung"])

# --------------------------------------------------------- p556
S13 = "Lung and Thyroid Retractors"
q(556, S13, "Why is the blade of the lung (Allison) retractor fenestrated:", "It allows lung expansion on retraction", ["It makes it lighter only", "It allows suction", "It prevents slipping"])
q(556, S13, "Use of lung forceps:", "Resection of small tissues such as hamartomas/nodules", ["Retraction of the lung", "Clamping the aorta", "Rib cutting"])
q(556, S13, "Purpose of the triangular end of lung forceps:", "Provides a bloodless field", ["Increases grip on the rib", "Allows suction", "Prevents current leakage"])
q(556, S13, "Joll's thyroid retractor is:", "Obsolete, with 2 retractors on either side to retract the thyroid", ["The current standard for thyroidectomy", "A single bladed retractor", "A bladder retractor"])

S14 = "Vascular Surgical Instruments"
q(556, S14, "Bulldog clamp is:", "A self retaining clamp with a pinch cork effect and serrations", ["A curved clamp used over a pedicle", "A J hook", "A crushing bowel clamp"])
q(556, S14, "Advantage of the bulldog clamp:", "Clamps temporarily without crushing structures", ["Crushes tissue for haemostasis", "Provides suction", "Cuts vessels"])
q(556, S14, "Satinsky vascular clamp is:", "A curved clamp with serrations used over a pedicle, giving better visualization", ["A self retaining pinch cork clamp", "A straight artery forceps", "A bowel crushing clamp"])
q(556, S14, "Aneurysm needle is:", "A J hook with an opening at the end, used for ligation of an aneurysm", ["A straight needle for suturing vessels", "A curved clamp", "A bladeless trocar"])

# --------------------------------------------------------- p557
S15 = "Other Instruments: Ovum, Cheatle's and Stone Forceps"
q(557, S15, "Ovum forceps have:", "2 convex ends with fenestrations", ["2 ends without lock", "Interlocking teeth", "A J hook"])
q(557, S15, "Use of ovum forceps:", "Remove retained placental/fetal tissue", ["Pick up gauze pieces", "Remove bladder stones", "Bring down CBD stones"])
q(557, S15, "Cheatle's forceps have:", "2 ends without a lock", ["2 convex fenestrated ends", "Interlocking teeth", "Longitudinal serrations"])
q(557, S15, "Use of Cheatle's forceps:", "Pick up gauze pieces", ["Remove retained placenta", "Clamp bowel", "Hold the cervix"])
q(557, S15, "Design of cystolithotomy forceps:", "One complete ring for the thumb and one open part for the other 4 fingers", ["Two complete rings", "No rings at all", "A single handle"])
q(557, S15, "Why do cystolithotomy forceps have NO lock:", "To prevent crushing of the stone", ["To reduce weight", "To allow suction", "To improve visualisation"])
q(557, S15, "Purpose of studs at the end of cystolithotomy forceps:", "Better grip", ["Crushing the stone", "Preventing tissue injury", "Locking the instrument"])
q(557, S15, "Pyelolithotomy forceps are:", "Obsolete, with varied angulations for better calyceal access and transverse serrations without a lock", ["Currently the standard instrument with a locking ratchet", "Used for CBD stones", "Used for bladder stones only"])

S16 = "Bowel Clamps and Choledocholithotomy Forceps"
q(557, S16, "Non crushing bowel clamp:", "Doyen's intestinal clamp", ["Payr's crushing clamp", "Kocher forceps", "Satinsky clamp"])
q(557, S16, "Purpose of longitudinal serrations on Doyen's intestinal clamp:", "Prevent tissue crushing", ["Increase crushing force", "Cut the bowel", "Allow suction"])
q(557, S16, "Functional purpose of a non crushing bowel clamp:", "Prevent spillage of fecal matter", ["Divide the bowel", "Ligate mesenteric vessels", "Retract the bowel"])
q(557, S16, "Payr's crushing clamp is used to:", "Remove portions of bowel", ["Prevent faecal spillage without crushing", "Clamp vessels", "Hold the cervix"])
q(557, S16, "Choledocholithotomy forceps are also called:", "Desjardin's forceps", ["Doyen's forceps", "Payr's clamp", "Babcock forceps"])
q(557, S16, "Use of Desjardin's forceps:", "Bring down CBD stones", ["Remove bladder stones", "Remove renal calyceal stones", "Remove retained placenta"])
q(557, S16, "Serrations on Desjardin's forceps:", "None — they have no serrations", ["Longitudinal serrations", "Criss cross serrations", "Transverse serrations with a gap"])

UNIT_DEFS = [
    (S1, "Every instrument has 2 rings for gripping, multiple ratchets that prevent wear and tear, a joint — box or screw, the screw joint more often catching thread — and blades that are fenestrated or serrated."),
    (S2, "Rampley's sponge holder has a fenestrated serrated blade to grip sponges for part preparation. Towel clips hold towels after draping, pass and hold the suction catheter or cautery, and hold the tongue during tongue resection — Mayo's has hooks, Doyen's works by the pinch cork effect. The BP (Brad Parker) handle mounts blades and is held like a paint brush or in a palming grip."),
    (S3, "Yankauer's suction cannula (plastic or metallic) suctions blood and fumes. Spring loaded forceps hold tissue: plain with transverse serrations and no teeth are relatively atraumatic; toothed grip tough structures but are traumatic; DeBakey's vascular forceps have minute serrations with raised edges for vessels; Russian forceps show transverse serration with a gap in between."),
    (S4, "The needle holder grips the needle with criss cross serrations that stop it moving; hold the needle at the 1/3rd-2/3rd junction from the swaged and pointed ends, enter skin at 90°, and grip the needle with toothed forceps while suturing. Mayo scissors are heavy with a screw joint, for cutting sutures and sheaths."),
    (S5, "Metzenbaum scissors are lighter tissue dissecting scissors and should not cut sutures; McIndoe scissors are finer still, for fine tissues in ophthalmic and ENT surgery. Skin suturing needs a needle holder, toothed forceps and scissors."),
    (S6, "Non-self retaining retractors must be held. Skin hooks (single or double handled) hold raised flaps in mastectomy, thyroidectomy and parotidectomy. The cats paw and the fenestrated right angle Langenbeck retract superficial tissue — a broader Langenbeck serves cholecystectomy. The army navy/Czerney's retractor has one 90° end and one clawed end with a gap for suturing while retracted, and the Morris retractor is broader than Langenbeck's, preventing slipping with better grip and less weight."),
    (S7, "Doyen's retractor retracts the bladder, its increased convexity easing retraction, while the malleable retractor retracts bowel in abdominal surgery. Self-retaining: mastoid retractors lock to retract superficial tissue in thyroid and parotid surgery; Balfour reaches deeper abdominal structures with a bar, blades and space to attach Doyen's; Bookwalter attaches a ring to the operating table with space for multiple retractors in complex abdominal malignancy surgery."),
    (S8, "Spencer Wells are straight artery forceps of various sizes for holding bleeders; curved artery forceps give better visualization; the mosquito forceps is the smallest artery forceps."),
    (S9, "Special forceps: Kelly's are big curved forceps with a gradual curve for abdominal surgery; right angle forceps tie pedicles; Allis, with serrations and teeth, traumatically holds tough sheath and fascia; Babcock, with a gap between two fenestrated ends, holds tubular structures — appendix, vas, fallopian tubes — without crushing; Kocher interlocks and crushes, holding tough structures and the cervix during hysterectomy."),
    (S10, "Laparoscopic instruments are long because they work at depth, and insulated to stop cautery current leaking. The Veress needle makes pneumoperitoneum by the closed method; it is spring loaded with an outlet/inlet valve and a blunt tip in front that gives way to a bevelled tip on pressing, preventing tissue injury."),
    (S11, "The 1st laparoscopic port goes in blindly. Trocars are sharp, blunt (Hassan's) or bladeless (Optiport, giving better visualization). Maryland's dissector — curved with artery-forceps-like serrations — is the workhorse of laparoscopic surgery."),
    (S12, "Thoracotomy set: Farabeuf's periosteal elevator raises periosteum over the rib; Doyen's rib raspatory, one for each side, resects periosteum and muscles held with handle lateral, convexity upwards and tip downwards; the rib cutter has a blunt lower edge to spare the pleura (unlike the sharp bone cutter); the bone nibbler smooths sharp edges after cutting."),
    (S13, "The Allison lung retractor's fenestrated blade lets the lung expand while retracted. Lung forceps resect small tissues such as hamartomas and nodules, their triangular end giving a bloodless field. Joll's thyroid retractor, now obsolete, uses 2 retractors on either side."),
    (S14, "Vascular instruments: the bulldog clamp is self retaining with a pinch cork effect and serrations, clamping temporarily without crushing; the Satinsky clamp is curved with serrations for use over a pedicle with better visualization; the aneurysm needle is a J hook with an opening at the end for ligating an aneurysm."),
    (S15, "Ovum forceps have 2 convex fenestrated ends to remove retained placental or fetal tissue; Cheatle's forceps have 2 ends without a lock to pick up gauze. Cystolithotomy forceps have one complete ring for the thumb and an open part for the other four fingers, no lock so the stone is not crushed, and studs for grip. Pyelolithotomy forceps are obsolete, with varied angulations for calyceal access and transverse serrations without a lock."),
    (S16, "Doyen's intestinal clamp is the non crushing bowel clamp, its longitudinal serrations preventing tissue crushing and stopping faecal spillage, while Payr's crushing clamp removes portions of bowel. Choledocholithotomy (Desjardin's) forceps, which have no serrations, bring down CBD stones."),
]

first_page = {}
for x in Q:
    first_page.setdefault(x["sec"], x["page"])

UNITS = []
for i, (title, guide) in enumerate(UNIT_DEFS, 1):
    UNITS.append({
        "id": f"SURG-U72-{i}",
        "ch": 72,
        "n": i,
        "title": title,
        "sec": f"{title} · p{first_page[title]}",
        "qs": [x["id"] for x in Q if x["sec"] == title],
        "guide": guide,
    })

covered = [x for u in UNITS for x in u["qs"]]
assert covered == [x["id"] for x in Q]
with open("data/ch72.json", "w", encoding="utf-8") as f:
    json.dump({"questions": Q, "units": UNITS}, f, ensure_ascii=False, indent=1)
print(f"ch72: {len(Q)} questions, {len(UNITS)} units")
