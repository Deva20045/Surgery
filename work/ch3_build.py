#!/usr/bin/env python3
"""Build data/ch3.json for PULSE Surgery ch3 (Surgical Drains, Knots and Sutures, book p10-17)."""
import json

Q = []
def q(page, sec, text, opts, ans, exp):
    Q.append({"id": f"SURG-C3-{len(Q)+1:03d}", "sec": sec, "page": page,
              "q": text, "opts": opts, "ans": ans, "exp": exp})

# ---------------- p10 · DRAIN TYPES ----------------
q(10, "Drains", "Open drains are described in the book as:",
  ["Obsolete", "First choice for the abdomen", "Always kept under negative pressure", "Connected to a collection bag"], 0,
  "Open: Obsolete. (Book p10)")
q(10, "Drains", "In the open-drain diagram, discharge from the abscess cavity ends up in a:",
  ["Closed bag", "Soak dressing", "Underwater seal", "Suction bulb"], 1,
  "The open-drain diagram shows the drain leading from the abscess cavity to a soak dressing. (Book p10)")
q(10, "Drains", "Closed drains:",
  ["Drain onto a soak dressing", "Empty into a container/bag", "Are obsolete", "Need no collection system"], 1,
  "Closed: Empty into a container/bag. (Book p10)")
q(10, "Drains", "The Romovac suction drain is a:",
  ["Open drain", "Closed drain with -ve pressure", "Closed drain with no pressure", "Underwater seal drain"], 1,
  "Romovac suction drain: Closed drain with -ve pressure. (Book p10)")
q(10, "Drains", "A Romovac drain is used after all of the following EXCEPT:",
  ["Mastectomy", "Thyroidectomy", "Neck dissection", "Laparotomy"], 3,
  "Romovac used after mastectomy, thyroidectomy, neck dissection. (Book p10)")
q(10, "Drains", "Which operation is a listed indication for a Romovac suction drain?",
  ["Mastectomy", "Inguinal hernia repair", "Appendectomy", "Haemorrhoidectomy"], 0,
  "Romovac used after mastectomy, thyroidectomy, neck dissection. (Book p10)")
q(10, "Drains", "A Romovac drain is avoided in the abdomen because it is a rounded drain with a risk of:",
  ["Perforation", "Excessive suction", "Tube kinking", "Bag overflow"], 0,
  "Avoided in abdomen d/t rounded drain risk of perforation. (Book p10)")
q(10, "Drains", "The Romovac assembly diagram labels all of the following EXCEPT:",
  ["Connected to bag", "Bag", "Inserted to body", "Underwater seal"], 3,
  "The Romovac diagram labels Connected to bag, Bag and Inserted to body. (Book p10)")
q(10, "Drains", "The minivac drain is used after:",
  ["Sentinel LN biopsy", "Mastectomy", "Thyroidectomy", "Laparotomy"], 0,
  "Minivac drain: used after sentinel LN biopsy. (Book p10)")
q(10, "Drains: JP & Abdominal", "The Jackson Pratt drain is a:",
  ["Open drain", "-ve pressure drain", "Passive bag drain", "Underwater seal drain"], 1,
  "Jackson Pratt drain: -ve pressure drain. (Book p10)")
q(10, "Drains: JP & Abdominal", "The Jackson Pratt drain can be used in the abdomen because it has:",
  ["Rounded tubes", "Flat tubes", "No tubes", "Rigid metal tubes"], 1,
  "Jackson Pratt: Flat tubes -> Can be used in abdomen. (Book p10)")
q(10, "Drains: JP & Abdominal", "In the Jackson Pratt diagram, the squeezable reservoir is labelled as the:",
  ["Bag", "Bulb", "Bellows", "Bottle"], 1,
  "The Jackson Pratt diagram labels the reservoir Bulb and the tube Flat. (Book p10)")
q(10, "Drains: JP & Abdominal", "In the Jackson Pratt diagram, the drainage tube is labelled as:",
  ["Round", "Flat", "Ribbed", "Fenestrated"], 1,
  "The Jackson Pratt diagram labels the reservoir Bulb and the tube Flat. (Book p10)")
q(10, "Drains: JP & Abdominal", "The abdominal drain is a:",
  ["Closed drain, no -ve pressure", "Closed drain with -ve pressure", "Open drain", "Underwater seal drain"], 0,
  "Abdominal drain: Closed drain, no -ve pressure. (Book p10)")
q(10, "Drains: JP & Abdominal", "A rounded suction drain that is avoided in the abdomen is the:",
  ["Jackson Pratt drain", "Romovac drain", "Abdominal drain", "Minivac drain"], 1,
  "Romovac: avoided in abdomen d/t rounded drain risk of perforation. (Book p10)")
q(10, "Drains: JP & Abdominal", "A suction drain with flat tubes that can be used in the abdomen is the:",
  ["Romovac drain", "Minivac drain", "Jackson Pratt drain", "Open corrugated drain"], 2,
  "Jackson Pratt: Flat tubes -> Can be used in abdomen. (Book p10)")

# ---------------- p11 · UNDERWATER SEAL ----------------
q(11, "Underwater Seal", "In the underwater seal bag, the tube is kept submerged underwater:",
  ["To measure output", "To prevent air being sucked in", "To warm the fluid", "To create positive pressure"], 1,
  "Underwater seal bag: Tube submerged underwater (To prevent air being sucked in). (Book p11)")
q(11, "Underwater Seal", "The underwater seal bag is connected to a:",
  ["Chest tube", "Urinary catheter", "Ryle's tube", "Central line"], 0,
  "Underwater seal bag: Connected to chest tube. (Book p11)")

# ---------------- p11 · KNOT TYPES ----------------
q(11, "Knots", "The most basic knot is the:",
  ["Surgeon's knot", "Square/Reef knot", "Granny knot", "Aberdeen's knot"], 1,
  "Square/Reef knot: most basic knot. (Book p11)")
q(11, "Knots", "A square/reef knot is tied as:",
  ["One square throw followed by another square throw", "Two throws followed by a single throw", "Three identical throws", "A single throw pulled tight"], 0,
  "Square knot: One square throw Followed by Another square throw. (Book p11)")
q(11, "Knots", "When the crossings are the same (black over pink), the result is a:",
  ["Granny/slip knot", "Surgeon's knot", "Reef or square knot", "Aberdeen's knot"], 2,
  "Crossings are same (Black over pink): Reef or square knot. (Book p11)")
q(11, "Knots", "When the crossings are opposite (black/pink), the result is a:",
  ["Reef knot", "Square knot", "Surgeon's knot", "Granny/slip knot"], 3,
  "Crossings are opposite (Black/pink): Granny/slip knot. (Book p11)")
q(11, "Knots", "The problem with a granny/slip knot is that its throws:",
  ["Cut through tissue", "Don't cross and open up", "Are too bulky", "Need cutting to untie"], 1,
  "Granny/slip knot: Don't cross, Open up. (Book p11)")
q(11, "Knots", "A slip knot is another name for a:",
  ["Square knot", "Reef knot", "Granny knot", "Surgeon's knot"], 2,
  "Crossings opposite: Granny/slip knot - Don't cross, Open up. (Book p11)")
q(11, "Knots", "The surgeon's knot is tied as:",
  ["One throw followed by one throw", "2 throws followed by single throw", "Single throw followed by 2 throws", "Three single throws"], 1,
  "Surgeon's knot: 2 throws Followed by Single throw. (Book p11)")
q(11, "Knots", "The reef knot is also called the:",
  ["Granny knot", "Slip knot", "Square knot", "Surgeon's knot"], 2,
  "Square/Reef knot: most basic knot - crossings same. (Book p11)")

# ---------------- p11 · SKIN SUTURING ----------------
q(11, "Skin Suturing", "Skin suturing requires:",
  ["Inverted edges", "Everted edges", "Overlapping edges", "Gaped edges"], 1,
  "Skin suturing: Everted edges. (Book p11)")
q(11, "Skin Suturing", "While suturing skin, the needle enters the skin at:",
  ["45 degrees", "90 degrees", "30 degrees", "180 degrees"], 1,
  "Skin suturing: Enter skin at 90 degrees. (Book p11)")
q(11, "Skin Suturing", "As per the principles of suturing, the bite on each side is:",
  ["x", "2x", "x/2", "3x"], 0,
  "Principles of suturing: Bite on each side: x; Distance b/w 2 sutures: 2x. (Book p11)")
q(11, "Skin Suturing", "As per the principles of suturing, the distance between 2 sutures is:",
  ["x", "2x", "x/2", "4x"], 1,
  "Principles of suturing: Bite on each side: x; Distance b/w 2 sutures: 2x. (Book p11)")

# ---------------- p12 · SUTURE TYPES ----------------
q(12, "Suture Types", "The simple suture:",
  ["Causes eversion", "Fails to cause eversion", "Gives hemostasis", "Leaves no marks"], 1,
  "Simple suture: Fail to cause eversion. (Book p12)")
q(12, "Suture Types", "Mattress sutures:",
  ["Fail to cause eversion", "Cause eversion", "Invert the edges", "Cannot achieve hemostasis"], 1,
  "Mattress suture: Cause eversion; Hemostasis. (Book p12)")
q(12, "Suture Types", "An advantage of mattress sutures is:",
  ["Hemostasis", "No marks", "Single layer closure", "No needle needed"], 0,
  "Mattress suture: Cause eversion; Hemostasis. (Book p12)")
q(12, "Suture Types", "The vertical mattress suture passes at:",
  ["The same depth on both sides", "Superficial and deep levels", "Subcuticular plane only", "Fascial level only"], 1,
  "Vertical mattress: passes Superficial and Deep. (Book p12)")
q(12, "Suture Types", "The horizontal mattress suture passes at:",
  ["Superficial and deep levels", "The same depth on both sides", "Fascial level only", "Subcuticular plane only"], 1,
  "Horizontal mattress: Same depth. (Book p12)")
q(12, "Suture Types", "The suture with the least cut through rate is the:",
  ["Simple suture", "Vertical mattress", "Horizontal mattress", "Subcuticular suture"], 2,
  "Horizontal mattress: Least cut through rate. (Book p12)")
q(12, "Suture Types", "Subcuticular sutures are preferred because they are:",
  ["Strongest", "Cosmetically better (No marks)", "Fastest to apply", "Usable on fascia"], 1,
  "Subcuticular sutures: Cosmetically better (No marks). (Book p12)")
q(12, "Suture Types", "The suture material for subcuticular closure is:",
  ["3-0 monocryl on a cutting needle", "1-0 silk on a round body needle", "2-0 prolene on a cutting needle", "5-0 vicryl on a round body needle"], 0,
  "Subcuticular suture material: 3-0 monocryl on a cutting needle. (Book p12)")

# ---------------- p12 · OTHER SUTURES ----------------
q(12, "Other Sutures", "The knot used for closure of a continuous suture is:",
  ["Square knot", "Surgeon's knot", "Aberdeen's/Cobbler's knot", "Granny knot"], 2,
  "Aberdeen's/Cobbler's knot for closure (of continuous suture). (Book p12)")
q(12, "Other Sutures", "The book's 'Other sutures' panel includes all of the following EXCEPT:",
  ["Continuous suture", "Interrupted suture", "Buried mattress suture", "Horizontal mattress suture"], 3,
  "Other sutures: Continuous, Interrupted, Buried mattress, Lock and Purse string sutures. (Book p12)")
q(12, "Other Sutures", "The lock suture is a:",
  ["Interrupted suture", "Continuous suture with locking", "Subcuticular suture", "Purse string suture"], 1,
  "Lock suture: Continuous suture with locking. (Book p12)")
q(12, "Other Sutures", "The lock suture gives:",
  ["Distribution of tension", "Eversion only", "Inversion of edges", "No marks"], 0,
  "Lock suture: Distribution of tension. (Book p12)")
q(12, "Other Sutures", "The purse string suture is used to:",
  ["Close skin", "Bury appendicular stump", "Repair fascia", "Close a fasciotomy wound"], 1,
  "Purse string Suture uses: Bury appendicular stump; Cervical encerclage. (Book p12)")
q(12, "Other Sutures", "Cervical encerclage is a listed use of the:",
  ["Lock suture", "Purse string suture", "Vertical mattress", "Far-near-near-far suture"], 1,
  "Purse string Suture uses: Bury appendicular stump; Cervical encerclage. (Book p12)")

# ---------------- p13 · SPECIAL SUTURES ----------------
q(13, "Special Sutures", "The Far-Near-Near-Far suture is used for:",
  ["Skin closure", "Obliteration of a large cavity", "Bowel anastomosis", "Cervical encerclage"], 1,
  "Far-Near-Near-Far suture uses: Obliteration of a large cavity. (Book p13)")
q(13, "Special Sutures", "Obliteration of a large cavity is the listed use of the:",
  ["Shoe string technique", "Far-Near-Near-Far suture", "Purse string suture", "Lock suture"], 1,
  "Far-Near-Near-Far suture uses: Obliteration of a large cavity. (Book p13)")
q(13, "Special Sutures", "The shoe string technique is used for:",
  ["Fasciotomy wound closure", "Bowel anastomosis", "Skin graft fixation", "Hernia mesh fixation"], 0,
  "Shoe string technique uses: Fasciotomy wound closure. (Book p13)")
q(13, "Special Sutures", "The shoe string technique involves:",
  ["Immediate tight closure", "Gradual tightening of suture", "Daily dressing only", "Negative pressure"], 1,
  "Shoe string technique: Gradual tightening of suture. (Book p13)")
q(13, "Special Sutures", "Wound healing in the shoe string technique is by:",
  ["Primary intention", "Secondary intention", "3 degree intention / delayed 1 degree closure", "Skin grafting"], 2,
  "Shoe string technique: Healing by 3 degree intention / delayed 1 degree closure. (Book p13)")

# ---------------- p13 · NEEDLE TYPES ----------------
q(13, "Needles: Types", "A round body needle:",
  ["Cuts tissue", "Splits tissue", "Burns tissue", "Crushes tissue"], 1,
  "Round body: Splits tissue; Relatively atraumatic. (Book p13)")
q(13, "Needles: Types", "A round body needle is:",
  ["More traumatic", "Relatively atraumatic", "Used for skin", "Used for fascia"], 1,
  "Round body: Splits tissue; Relatively atraumatic. (Book p13)")
q(13, "Needles: Types", "Round body needles are used for delicate structures (the B's) - all of the following EXCEPT:",
  ["Bowel", "Bladder", "Skin", "CBD"], 2,
  "Round body for delicate structures (B's): Bowel, Bladder, Blood vessels, CBD. (Book p13)")
q(13, "Needles: Types", "The common bile duct (CBD) is repaired with a:",
  ["Cutting needle", "Round body needle", "Reverse cutting needle", "Tapered drill"], 1,
  "Round body for delicate structures: Bowel, Bladder, Blood vessels, CBD. (Book p13)")
q(13, "Needles: Types", "Blood vessel anastomosis uses a:",
  ["Cutting needle", "Round body needle", "Reverse cutting needle", "Shoe string suture"], 1,
  "Round body for delicate structures: Bowel, Bladder, Blood vessels, CBD. (Book p13)")
q(13, "Needles: Types", "A cutting/reverse cutting needle:",
  ["Splits tissue", "Cuts tissue", "Coagulates tissue", "Staples tissue"], 1,
  "Cutting/reverse cutting: Cuts tissue; more traumatic. (Book p13)")
q(13, "Needles: Types", "A cutting needle is:",
  ["Relatively atraumatic", "More traumatic", "Used for bowel", "Used for bladder"], 1,
  "Cutting/reverse cutting: Cuts tissue; more traumatic. (Book p13)")
q(13, "Needles: Types", "Cutting needles are used for tough structures (the S's) - all of the following EXCEPT:",
  ["Sheath", "Skin", "Fascia", "Small bowel"], 3,
  "Cutting for tough structures (S's): Sheath, Skin, Fascia. (Book p13)")
q(13, "Needles: Types", "Skin is closed with a:",
  ["Round body needle", "Cutting/reverse cutting needle", "Blunt needle", "No needle - glue only"], 1,
  "Cutting for tough structures (S's): Sheath, Skin, Fascia. (Book p13)")
q(13, "Needles: Types", "Sheath and fascia are sutured with a:",
  ["Round body needle", "Cutting/reverse cutting needle", "Blunt needle", "Curved blade"], 1,
  "Cutting for tough structures (S's): Sheath, Skin, Fascia. (Book p13)")

# ---------------- p13 · NEEDLE PARTS ----------------
q(13, "Needles: Parts", "The swaged end of a needle is the:",
  ["Sharp tip", "End to which suture material is attached", "Middle of the shaft", "Eye of the needle"], 1,
  "Swaged end: End to which suture material is attached. (Book p13)")
q(13, "Needles: Parts", "The swaged end forms what proportion of the needle?",
  ["1/3rd", "2/3rd", "1/2", "Entire needle"], 0,
  "Swaged end: 1/3rd; Body (Shaft): 2/3rd. (Book p13)")
q(13, "Needles: Parts", "The body (shaft) of the needle forms:",
  ["1/3rd", "2/3rd", "1/4th", "Entire needle"], 1,
  "Body (Shaft): 2/3rd; Swaged end: 1/3rd. (Book p13)")
q(13, "Needles: Parts", "The needle is grasped with a:",
  ["Thumb forceps", "Needle holder", "Sponge holder", "Towel clip"], 1,
  "Needle diagram: Point, Body (Shaft), Swaged end, Needle holder. (Book p13)")
q(13, "Needles: Parts", "The tip of the needle is labelled as the:",
  ["Swaged end", "Body", "Point", "Eye"], 2,
  "Needle diagram labels: Point, Body (Shaft), Swaged end. (Book p13)")

# ---------------- p13 · SUTURE CODING ----------------
q(13, "Suture Coding", "Brown color codes the suture:",
  ["Vicryl", "Prolene", "Silk", "Catgut"], 3,
  "Color coding: Brown - Catgut; Violet - Vicryl; Blue - Prolene; Black - Silk. (Book p13)")
q(13, "Suture Coding", "Violet color codes the suture:",
  ["Catgut", "Vicryl", "Prolene", "Silk"], 1,
  "Color coding: Violet - Vicryl. (Book p13)")
q(13, "Suture Coding", "Blue color codes the suture:",
  ["Catgut", "Vicryl", "Prolene", "Silk"], 2,
  "Color coding: Blue - Prolene. (Book p13)")
q(13, "Suture Coding", "Black color codes the suture:",
  ["Catgut", "Vicryl", "Prolene", "Silk"], 3,
  "Color coding: Black - Silk. (Book p13)")
q(13, "Suture Coding", "Suture diameter equals:",
  ["1/10th of a mm", "1 mm", "1 cm", "1/100th of a mm"], 0,
  "Suture numbering: Suture diameter = 1/10th of a mm. (Book p13)")
q(13, "Suture Coding", "The thickest suture is:",
  ["11.0", "No 1", "2.0", "10-0"], 1,
  "Suture numbering: No 1 -> Thickest ... 11.0 -> Finest. (Book p13)")
q(13, "Suture Coding", "The finest suture is:",
  ["No 1", "1.0", "2.0", "11.0"], 3,
  "Suture numbering: No 1 -> Thickest ... 11.0 -> Finest. (Book p13)")
q(13, "Suture Coding", "Higher suture numbers (toward 11.0) mean:",
  ["Thicker suture", "Finer suture (more finesse)", "Longer suture", "Braided suture"], 1,
  "Suture numbering: No 1 -> Thickest; 1.0, 2.0 ... 11.0 -> Finest (Finesse increases). (Book p13)")

# ---------------- p14 · CLASSIFICATION ----------------
q(14, "Classification", "The natural suture materials listed are:",
  ["Prolene and PDS", "Silk and catgut", "Vicryl and monocryl", "Nylon and steel"], 1,
  "Natural: Eg - Silk, Catgut. (Book p14)")
q(14, "Classification", "Natural sutures are antigens (+) and hence:",
  ["Cause no reaction", "Mount strong inflammatory reaction", "Dissolve by hydrolysis", "Are most inert"], 1,
  "Natural: Antigens (+) -> mount strong inflammatory reaction. (Book p14)")
q(14, "Classification", "Natural sutures dissolve by:",
  ["Hydrolysis", "Proteolysis", "Phagocytosis only", "Evaporation"], 1,
  "Natural: Dissolution by proteolysis. (Book p14)")
q(14, "Classification", "The synthetic sutures listed include all of the following EXCEPT:",
  ["Prolene", "PDS", "Vicryl", "Silk"], 3,
  "Synthetic: Eg - Prolene, PDS, Vicryl. (Book p14)")
q(14, "Classification", "Synthetic sutures are inert and cause:",
  ["Strong inflammation", "Less tissue inflammation", "No healing", "Proteolysis"], 1,
  "Synthetic: Inert - Less tissue inflammation. (Book p14)")
q(14, "Classification", "The most inert suture (least inflammation) is:",
  ["Natural absorbable", "Natural non absorbable", "Synthetic non absorbable", "Natural braided"], 2,
  "Most inert: Synthetic non absorbable (Least inflammation). (Book p14)")
q(14, "Classification", "Synthetic sutures dissolve by:",
  ["Proteolysis", "Hydrolysis", "Oxidation", "Ionization"], 1,
  "Synthetic: Dissolution by hydrolysis. (Book p14)")
q(14, "Classification", "Monofilament sutures include all of the following EXCEPT:",
  ["Catgut", "Prolene", "PDS", "Vicryl"], 3,
  "Monofilament: Catgut, Prolene, PDS, Nylon, Monocryl. (Book p14)")
q(14, "Classification", "Nylon and monocryl are:",
  ["Braided sutures", "Monofilament sutures", "Natural sutures", "Steel sutures"], 1,
  "Monofilament: Catgut, Prolene, PDS, Nylon, Monocryl. (Book p14)")
q(14, "Classification", "Monofilament sutures are:",
  ["Easier to handle", "Difficult to handle", "Braided", "High infection risk"], 1,
  "Monofilament: Difficult to handle; Strong memory -> more knots. (Book p14)")
q(14, "Classification", "Monofilament sutures have a strong memory, so they need:",
  ["Fewer knots", "More knots", "No knots", "Glue instead"], 1,
  "Monofilament: Strong memory -> more knots. (Book p14)")
q(14, "Classification", "The braided sutures listed are:",
  ["Prolene and PDS", "Vicryl and silk", "Nylon and monocryl", "Catgut and steel"], 1,
  "Braided: Eg - Vicryl, Silk. (Book p14)")
q(14, "Classification", "Braided sutures are:",
  ["Difficult to handle", "Easier to handle", "Monofilament", "Memory-free"], 1,
  "Braided: Easier to handle; increased risk of infection. (Book p14)")
q(14, "Classification", "A disadvantage of braided sutures is:",
  ["Strong memory", "Increased risk of infection", "Difficult handling", "Early dissolution"], 1,
  "Braided: Easier to handle; increased risk of infection. (Book p14)")
q(14, "Classification", "In the book's tree, absorbable and non-absorbable sutures are each divided into:",
  ["Monofilament and braided", "Natural and synthetic", "Thick and fine", "Cutting and round body"], 1,
  "Classification tree: Absorbable (Natural/Synthetic) and Non-absorbable (Natural/Synthetic). (Book p14)")

# ---------------- p15 · NATURAL ABSORBABLE ----------------
q(15, "Natural Absorbable", "Catgut is derived from the:",
  ["Serosa of human gut", "Submucosa of a sheep gut", "Skin of a silkworm", "Tendon of cattle"], 1,
  "Catgut: Derived from submucosa of a sheep gut. (Book p15)")
q(15, "Natural Absorbable", "Catgut undergoes phagocytosis and enzymatic degradation within:",
  ["7-10 days", "21-28 days", "60-90 days", "180 days"], 0,
  "Catgut: phagocytosis & enzymatic degradation within 7-10 days. (Book p15)")
q(15, "Natural Absorbable", "The tensile strength of chromic catgut lasts:",
  ["7-10 days", "21-28 days", "60-90 days", "180 days"], 1,
  "Chromic catgut: Tensile strength: 21-28 days. (Book p15)")
q(15, "Natural Absorbable", "Chromic catgut is completely absorbed in:",
  ["7-10 days", "21-28 days", "90 days", "180 days"], 2,
  "Chromic catgut: Complete absorption in 90 days. (Book p15)")

# ---------------- p15 · SYNTHETIC ABSORBABLE ----------------
q(15, "Synthetic Absorbable", "Monocryl is:",
  ["Polyglactin", "Poliglecaprone", "Polydiaxone", "Polyglycolic acid"], 1,
  "Monocryl (Poliglecaprone). (Book p15)")
q(15, "Synthetic Absorbable", "Monocryl is a:",
  ["Braided suture", "Monofilament suture", "Steel suture", "Natural suture"], 1,
  "Monocryl: monofilament. (Book p15)")
q(15, "Synthetic Absorbable", "Monocryl for subcuticular closure is used as:",
  ["3-0/4-0 cutting/reverse cutting needle", "1/1-0/2-0 round body", "5-0 round body", "10-0 cutting"], 0,
  "Monocryl: Subcuticular: 3-0/4-0 cutting/reverse cutting needle. (Book p15)")
q(15, "Synthetic Absorbable", "Vicryl is:",
  ["Poliglecaprone", "Polyglactin", "Polydiaxone", "Polypropylene"], 1,
  "Vicryl (Polyglactin). (Book p15)")
q(15, "Synthetic Absorbable", "Vicryl is a:",
  ["Monofilament suture", "Braided suture", "Steel suture", "Natural suture"], 1,
  "Vicryl: Braided; Dissolves in 60-90 days. (Book p15)")
q(15, "Synthetic Absorbable", "Vicryl dissolves in:",
  ["7-10 days", "21-28 days", "60-90 days", "180 days"], 2,
  "Vicryl: Dissolves in 60-90 days. (Book p15)")
q(15, "Synthetic Absorbable", "Vicryl for CBD repair is:",
  ["3-0", "5-0", "2-0", "10-0"], 1,
  "Vicryl uses: CBD: 5-0; Bowel: 3-0; Bladder: 3-0 (Round body). (Book p15)")
q(15, "Synthetic Absorbable", "Vicryl for bowel and bladder repair is:",
  ["5-0", "3-0", "2-0", "1-0"], 1,
  "Vicryl uses: CBD: 5-0; Bowel: 3-0; Bladder: 3-0 (Round body). (Book p15)")
q(15, "Synthetic Absorbable", "Vicryl for CBD/bowel/bladder is mounted on a:",
  ["Cutting needle", "Round body needle", "Reverse cutting needle", "Straight needle"], 1,
  "Vicryl uses: CBD/bowel/bladder - Round body. (Book p15)")
q(15, "Synthetic Absorbable", "Vicryl plus is coated with antibiotic triclosan, which:",
  ["Increases strength", "Decreases risk of infection", "Speeds absorption", "Adds color"], 1,
  "Vicryl plus: Coated with antibiotic triclosan (decreased risk of infection). (Book p15)")
q(15, "Synthetic Absorbable", "Barbed vicryl is characterized by:",
  ["A triclosan coat", "Thorns on suture", "Rapid dissolution", "Steel core"], 1,
  "Barbed vicryl: Thorns on suture. (Book p15)")
q(15, "Synthetic Absorbable", "Barbed vicryl is used for:",
  ["Bowel anastomosis", "Face lift Sx", "Cataract Sx", "Sternotomy closure"], 1,
  "Barbed vicryl: Used: Face lift Sx; Disadvantage: Painful. (Book p15)")
q(15, "Synthetic Absorbable", "A disadvantage of barbed vicryl is that it is:",
  ["Weak", "Painful", "Braided", "Non-absorbable"], 1,
  "Barbed vicryl: Disadvantage: Painful. (Book p15)")
q(15, "Synthetic Absorbable", "Vicryl rapide is:",
  ["Polyglactin 910", "Poliglecaprone", "Polydiaxone", "Plain catgut"], 0,
  "Vicryl rapide: Polyglactin 910; Rapidly dissolves within 21-28 days. (Book p15)")
q(15, "Synthetic Absorbable", "Vicryl rapide dissolves:",
  ["Within 7-10 days", "Within 21-28 days", "In 60-90 days", "In 180 days"], 1,
  "Vicryl rapide: Rapidly dissolves within 21-28 days. (Book p15)")
q(15, "Synthetic Absorbable", "PDS (polydiaxone) is a:",
  ["Braided suture", "Monofilament suture", "Natural suture", "Steel suture"], 1,
  "PDS: monofilament; Dissolves: 180 days. (Book p15)")
q(15, "Synthetic Absorbable", "PDS dissolves in:",
  ["7-10 days", "21-28 days", "60-90 days", "180 days"], 3,
  "PDS: Dissolves: 180 days. (Book p15)")
q(15, "Synthetic Absorbable", "PDS is used for:",
  ["Same as vicryl + tracheobronchial repair", "Skin only", "Cataract Sx", "Sternotomy closure"], 0,
  "PDS uses: Same as vicryl + tracheobronchial repair. (Book p15)")

# ---------------- p16 · SILK ----------------
q(16, "Silk", "Silk is a:",
  ["Blue monofilament suture", "Black, braided suture", "Violet braided suture", "Brown monofilament suture"], 1,
  "Silk: Black, braided suture; Source: Silkworm. (Book p16)")
q(16, "Silk", "The source of silk suture is the:",
  ["Sheep gut", "Silkworm", "Catgut plant", "Petroleum lab"], 1,
  "Silk: Source: Silkworm. (Book p16)")
q(16, "Silk", "Silk for skin closure is used as:",
  ["2-0/3-0 cutting", "5-0 round body", "10-0 cutting", "No 1 round body"], 0,
  "Silk uses: Skin: 2-0/3-0 cutting. (Book p16)")
q(16, "Silk", "Silk to fix a surgical drain is:",
  ["3-0 round body", "5-0 round body", "No 1/1-0/2-0", "10-0 cutting"], 2,
  "Silk uses: Fix drain: No 1/1-0/2-0. (Book p16)")
q(16, "Silk", "The 2nd layer of bowel anastomosis uses silk as:",
  ["3-0 round body", "5-0 round body", "2-0 cutting", "10-0 cutting"], 0,
  "Silk uses: 2nd layer of bowel anastomosis: 3-0 round body. (Book p16)")

# ---------------- p16 · SYNTHETIC NON-ABSORBABLE ----------------
q(16, "Synthetic Non-absorbable", "Prolene is a:",
  ["Black braided suture", "Blue monofilament suture", "Violet braided suture", "Brown monofilament suture"], 1,
  "Prolene: Blue monofilament suture. (Book p16)")
q(16, "Synthetic Non-absorbable", "Prolene is used for:",
  ["Hernia mesh", "Cataract Sx", "Face lift", "Bowel mucosa"], 0,
  "Prolene uses: Hernia mesh; Close abdominal sheath; Vascular repair. (Book p16)")
q(16, "Synthetic Non-absorbable", "Jenkin's rule for closing the abdominal sheath states: Length of suture:",
  ["= length of wound", ">= 4x length of wound", "<= length of wound", "= 2x length of wound"], 1,
  "Prolene: Close abdominal sheath: Jenkin's rule: Length of suture >= 4x length of wound. (Book p16)")
q(16, "Synthetic Non-absorbable", "Prolene for aortic repair is:",
  ["6-0", "4-0", "2-0", "10-0"], 2,
  "Prolene vascular repair: Aorta: 2-0; Femoral artery: 4-0; Popliteal artery: 6-0. (Book p16)")
q(16, "Synthetic Non-absorbable", "Prolene for femoral artery repair is:",
  ["2-0", "4-0", "6-0", "10-0"], 1,
  "Prolene vascular repair: Aorta: 2-0; Femoral artery: 4-0; Popliteal artery: 6-0. (Book p16)")
q(16, "Synthetic Non-absorbable", "Prolene for popliteal artery repair is:",
  ["2-0", "4-0", "6-0", "1-0"], 2,
  "Prolene vascular repair: Aorta: 2-0; Femoral artery: 4-0; Popliteal artery: 6-0. (Book p16)")
q(16, "Synthetic Non-absorbable", "Nylon/Ethilon is a:",
  ["Braided suture", "Monofilament suture", "Natural suture", "Absorbable suture"], 1,
  "Nylon/Ethilon: monofilament suture. (Book p16)")
q(16, "Synthetic Non-absorbable", "Nylon is used as a:",
  ["Bowel suture", "Skin suture", "CBD suture", "Bladder suture"], 1,
  "Nylon uses: Skin suture; Cataract Sx: 10-0; Nerve & tendon repair. (Book p16)")
q(16, "Synthetic Non-absorbable", "Cataract surgery uses nylon as:",
  ["2-0", "6-0", "10-0", "No 1"], 2,
  "Nylon uses: Cataract Sx: 10-0. (Book p16)")
q(16, "Synthetic Non-absorbable", "Nerve and tendon repair is a listed use of:",
  ["Catgut", "Nylon/Ethilon", "Vicryl rapide", "Steel"], 1,
  "Nylon uses: Nerve & tendon repair. (Book p16)")
q(16, "Synthetic Non-absorbable", "Steel suture is used for:",
  ["Sternotomy incision following CABG", "Skin closure", "Bowel anastomosis", "Cataract Sx"], 0,
  "Steel suture uses: Sternotomy incision following CABG. (Book p16)")
q(16, "Synthetic Non-absorbable", "Polyester/Ethibond is used for the:",
  ["Skin", "CBD", "Rectus sheath", "Cornea"], 2,
  "Polyester/Ethibond uses: Rectus sheath; Tendon repair. (Book p16)")
q(16, "Synthetic Non-absorbable", "Tendon repair is a listed use of:",
  ["Polyester/Ethibond", "Catgut", "Vicryl rapide", "Steel suture"], 0,
  "Polyester/Ethibond uses: Rectus sheath; Tendon repair. (Book p16)")
q(16, "Synthetic Non-absorbable", "Polybutester is used for:",
  ["Plastic Sx (Rarely used)", "Hernia mesh", "Sternotomy closure", "Bowel anastomosis"], 0,
  "Polybutester uses: Plastic Sx (Rarely used). (Book p16)")

# ---------------- p17 · SUTURE REMOVAL ----------------
q(17, "Suture Removal", "Suture removal timings apply to:",
  ["Absorbable sutures", "Non-absorbable sutures", "All sutures", "Staples only"], 1,
  "Suture removal: For non-absorbable sutures. (Book p17)")
q(17, "Suture Removal", "Scalp sutures are removed in:",
  ["3-5 days", "5-7 days", "10-12 days", "12-14 days"], 1,
  "Suture removal: Scalp: 5-7 days. (Book p17)")
q(17, "Suture Removal", "Face sutures are removed in:",
  ["3-5 days (Earliest)", "5-7 days", "10-12 days", "12-14 days"], 0,
  "Suture removal: Face: 3-5 days (Earliest). (Book p17)")
q(17, "Suture Removal", "Neck sutures are removed in:",
  ["3-5 days", "5-7 days", "10-12 days", "12-14 days"], 1,
  "Suture removal: Neck: 5-7 days. (Book p17)")
q(17, "Suture Removal", "Thorax sutures are removed in:",
  ["3-5 days", "5-7 days", "10-12 days", "12-14 days"], 2,
  "Suture removal: Thorax: 10-12 days. (Book p17)")
q(17, "Suture Removal", "Abdominal sutures are removed in:",
  ["3-5 days", "5-7 days", "10-12 days", "12-14 days"], 3,
  "Suture removal: Abdomen: 12-14 days. (Book p17)")
q(17, "Suture Removal", "Perineal sutures are removed in:",
  ["3-5 days", "5-7 days", "10-12 days", "12-14 days"], 2,
  "Suture removal: Perineum: 10-12 days. (Book p17)")
q(17, "Suture Removal", "The earliest suture removal is from the:",
  ["Scalp", "Face (3-5 days)", "Abdomen", "Thorax"], 1,
  "Suture removal: Face: 3-5 days (Earliest). (Book p17)")

# ---------------- p17 · BOWEL ANASTOMOSIS ----------------
q(17, "Bowel Anastomosis", "Bowel anastomosis requires:",
  ["Everted edges", "Inverted edges", "Gaped edges", "Overlapping edges"], 1,
  "Bowel anastomosis: Inverted Edges; Strongest layer: Submucosa. (Book p17)")
q(17, "Bowel Anastomosis", "The strongest layer of the bowel wall is the:",
  ["Serosa", "Mucosa", "Submucosa", "Muscle"], 2,
  "Bowel anastomosis: Strongest layer: Submucosa. (Book p17)")
q(17, "Bowel Anastomosis", "The book states that the result is ___ despite the technique used:",
  ["Different", "Same", "Better with staplers", "Worse with sutures"], 1,
  "Techniques: Same result despite technique used. (Book p17)")
q(17, "Bowel Anastomosis", "Single layer bowel repair is:",
  ["Seromuscular repair", "Extramucosal repair", "Full thickness repair", "Stapled repair"], 1,
  "Single layer: Extramucosal repair. (Book p17)")
q(17, "Bowel Anastomosis", "In the anastomosis diagrams, 'S/m' denotes the:",
  ["Serosa", "Mucosa", "Submucosa", "Muscle"], 2,
  "Diagram key: S: Serosa; m: mucosa; S/m: Submucosa; muscle. (Book p17)")
q(17, "Bowel Anastomosis", "The Albert layer is:",
  ["Outer seromuscular interrupted nonabsorbable suture", "Inner continuous absorbable suture with stitching of all layers", "Single extramucosal layer", "Stapled layer"], 1,
  "2 layer: inner continuous absorbable suture with stitching of all layers: Albert layer. (Book p17)")
q(17, "Bowel Anastomosis", "The Lembert layer is:",
  ["Inner continuous absorbable suture of all layers", "Outer seromuscular interrupted nonabsorbable suture", "Single extramucosal layer", "Stapled layer"], 1,
  "2 layer: outer seromuscular interrupted nonabsorbable suture: Lembert layer. (Book p17)")
q(17, "Bowel Anastomosis", "Side-to-side anastomosis is a listed use of the:",
  ["Circular stapler", "Linear stapler", "Purse string suture", "Lock suture"], 1,
  "Linear stapler uses: Side-to-side anastomosis; Sleeve gastrectomy; Zenker's diverticulum. (Book p17)")
q(17, "Bowel Anastomosis", "Sleeve gastrectomy (bariatric Sx) uses a:",
  ["Circular stapler", "Linear stapler", "Purse string suture", "Barbed suture"], 1,
  "Linear stapler uses: Sleeve gastrectomy (Bariatric Sx). (Book p17)")
q(17, "Bowel Anastomosis", "Zenker's diverticulum surgery uses a:",
  ["Circular stapler", "Linear stapler", "Purse string suture", "Far-near-near-far suture"], 1,
  "Linear stapler uses: Zenker's diverticulum. (Book p17)")
q(17, "Bowel Anastomosis", "Stapler hemorrhoidopexy (hemorrhoid repair) uses a:",
  ["Linear stapler", "Circular stapler", "Purse string suture", "Lock suture"], 1,
  "Circular stapler uses: Stapler hemorrhoidopexy: Hemorrhoid repair. (Book p17)")
q(17, "Bowel Anastomosis", "LAR (low anterior resection) for sigmoid colon cancer surgery uses a:",
  ["Linear stapler", "Circular stapler", "Purse string suture", "Subcuticular suture"], 1,
  "Circular stapler uses: LAR (Low anterior resection): Sigmoid colon cancer Sx. (Book p17)")
q(17, "Bowel Anastomosis", "Cheatle's slit is a:",
  ["Transverse cut on mesenteric border", "Longitudinal split along anti mesenteric border", "Circular stapler line", "Seromuscular bite"], 1,
  "Cheatle's slit: Longitudinal split along anti mesenteric border -> Enlarges lumen. (Book p17)")
q(17, "Bowel Anastomosis", "Cheatle's slit enlarges the lumen for:",
  ["Side-to-side anastomosis", "End-to-end anastomosis", "Stapler firing", "Stoma creation"], 1,
  "Cheatle's slit: Enlarges lumen for end-to-end anastomosis. (Book p17)")
q(17, "Bowel Anastomosis", "The Connel loop is taken at the edge of the anastomosis and ensures:",
  ["Hemostasis", "Bowel inversion", "Eversion", "Lumen enlargement"], 1,
  "Connel loop: Taken at edge of anastomosis -> Ensures bowel inversion. (Book p17)")

# ---------------- UNITS ----------------
def uid(n): return {"id": f"SURG-U3-{n}", "ch": 3, "n": n}
def rng(a, b): return [f"SURG-C3-{i:03d}" for i in range(a, b + 1)]
UNITS = [
    {**uid(1), "title": "Drains: Open, Closed, Romovac & Minivac", "sec": "Drains \u00b7 p10",
     "qs": rng(1, 9),
     "guide": "Open drains are obsolete museum pieces that stain a soak dressing, while closed drains empty into a container or bag. Romovac - a closed negative-pressure system for mastectomy, thyroidectomy and neck dissection - must never enter the abdomen, where its rounded tip risks perforation; the tiny minivac instead follows sentinel node biopsy."},
    {**uid(2), "title": "Drains: Jackson Pratt, Abdominal & Underwater Seal", "sec": "Drains \u00b7 p10",
     "qs": rng(10, 18),
     "guide": "The Jackson Pratt pairs a squeezable bulb with flat tubes that slide safely into the abdomen, unlike the rounded Romovac. A plain abdominal drain is closed but pressure-free, while chest tubes bubble through an underwater seal whose submerged tip bars air from being sucked in."},
    {**uid(3), "title": "Knot Types: Reef, Granny & Surgeon's", "sec": "Knots \u00b7 p11",
     "qs": rng(19, 26),
     "guide": "The reef (square) knot - one square throw on another with matching crossings - is the most basic knot in surgery. Cross the throws oppositely and you get a granny or slip knot that opens up, while the surgeon's knot doubles the first throw for extra grip before a single locking throw."},
    {**uid(4), "title": "Skin Suturing & Principles", "sec": "Skin Suturing \u00b7 p11",
     "qs": rng(27, 30),
     "guide": "Skin heals kindest when its edges are everted and the needle bites at a full 90 degrees. The geometry is simple arithmetic: take a bite of x on each side and space the sutures 2x apart."},
    {**uid(5), "title": "Suture Types: Simple, Mattress & Subcuticular", "sec": "Suture Types \u00b7 p12",
     "qs": rng(31, 38),
     "guide": "Simple sutures fail to evert, but mattress sutures evert and staunch bleeding - vertical at two depths, horizontal at one depth with the least cut-through. When scars must vanish, a 3-0 monocryl on a cutting needle runs hidden beneath the skin in a mark-free subcuticular line."},
    {**uid(6), "title": "Other Sutures: Lock & Purse String", "sec": "Other Sutures \u00b7 p12",
     "qs": rng(39, 44),
     "guide": "A continuous suture closes with an Aberdeen's or Cobbler's knot, and locking each loop spreads tension evenly along the wound. The purse string instead cinches like a drawstring - burying the appendicular stump or encircling the cervix."},
    {**uid(7), "title": "Far-Near-Near-Far & Shoe String", "sec": "Special Sutures \u00b7 p13",
     "qs": rng(45, 49),
     "guide": "The far-near-near-far stitch collapses and obliterates a large dead cavity in one pass. Fasciotomy wounds instead close slowly with the shoe string technique - gradual tightening that heals by tertiary intention, a delayed primary closure."},
    {**uid(8), "title": "Needles: Round Body vs Cutting", "sec": "Needles \u00b7 p13",
     "qs": rng(50, 59),
     "guide": "Round-bodied needles split tissue atraumatically, gliding through the delicate B's - bowel, bladder, blood vessels and CBD. Cutting and reverse-cutting needles slice through the tough S's - sheath, skin and fascia - at the price of greater trauma."},
    {**uid(9), "title": "Needle Parts, Color Codes & Numbering", "sec": "Suture Coding \u00b7 p13",
     "qs": rng(60, 72),
     "guide": "Every needle runs from point through a two-thirds shaft to a one-third swaged end that carries the suture, gripped by a needle holder. Colors speak instantly - brown catgut, violet vicryl, blue prolene, black silk - while numbers whisper finesse: No. 1 is thickest and 11-0 the finest."},
    {**uid(10), "title": "Suture Classification", "sec": "Classification \u00b7 p14",
     "qs": rng(73, 87),
     "guide": "Natural sutures like silk and catgut are antigenic, provoke strong inflammation and dissolve by proteolysis. Synthetic sutures - prolene, PDS, vicryl - stay inert and dissolve by hydrolysis, with synthetic non-absorbables the most inert of all; monofilaments handle stiffly with strong memory while braids handle sweetly but invite infection."},
    {**uid(11), "title": "Natural Absorbable: Catgut", "sec": "Natural Absorbable \u00b7 p15",
     "qs": rng(88, 91),
     "guide": "Plain catgut - sheep gut submucosa - vanishes by phagocytosis within 7 to 10 days. Chromic tanning stretches its tensile strength to 21-28 days and full absorption to 90 days."},
    {**uid(12), "title": "Synthetic Absorbable: Monocryl, Vicryl & PDS", "sec": "Synthetic Absorbable \u00b7 p15",
     "qs": rng(92, 109),
     "guide": "Monofilament monocryl runs subcuticular lines on cutting needles, while braided vicryl holds CBD, bowel and bladder on round-bodied needles for 60-90 days - with triclosan-coated, barbed and rapide avatars. PDS outlasts them all at 180 days and even repairs the tracheobronchial tree."},
    {**uid(13), "title": "Silk: Natural Non-absorbable", "sec": "Silk \u00b7 p16",
     "qs": rng(110, 114),
     "guide": "Silk - black, braided, spun by silkworms - closes skin with 2-0 or 3-0 on cutting needles, anchors drains with stout No. 1 to 2-0, and lays the second layer of bowel anastomosis with 3-0 on a round body."},
    {**uid(14), "title": "Synthetic Non-absorbable: Prolene to Polybutester", "sec": "Synthetic Non-absorbable \u00b7 p16",
     "qs": rng(115, 128),
     "guide": "Blue monofilament prolene weaves hernia mesh, closes sheaths by Jenkin's four-to-one rule, and steps down vessels from 2-0 aorta to 6-0 popliteal. Nylon serves skin, cataract and nerve-tendon repairs, steel wires post-CABG sternums, polyester holds rectus and tendon, and polybutester lingers rarely in plastic surgery."},
    {**uid(15), "title": "Suture Removal Timings", "sec": "Suture Removal \u00b7 p17",
     "qs": rng(129, 136),
     "guide": "Only non-absorbable sutures come out: face first at 3-5 days, scalp and neck at 5-7, thorax and perineum at 10-12, and abdomen last at 12-14 days."},
    {**uid(16), "title": "Bowel Anastomosis & Staplers", "sec": "Bowel Anastomosis \u00b7 p17",
     "qs": rng(137, 151),
     "guide": "Bowel demands inverted edges, trusting the submucosa as its strongest layer - whether joined by single extramucosal, two-layer Albert-plus-Lembert, or stapler. Linear staplers fire side-to-side joins, sleeves and Zenker's pouches; circular staplers fix haemorrhoids and low anterior resections; Cheatle's slit widens narrow ends and the Connel loop guarantees inversion."},
]

data = {"questions": Q, "units": UNITS}
with open("data/ch3.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
print(f"ch3: {len(Q)} questions, {len(UNITS)} units")
