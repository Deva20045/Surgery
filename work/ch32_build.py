#!/usr/bin/env python3
"""Build data/ch32.json for PULSE Surgery ch32 (Colorectal Polyps and Cancer: Part 2, p227-232)."""
import json

Q = []

def q(page, sec, text, opts, ans, exp):
    Q.append({
        "id": f"SURG-C32-{len(Q)+1:03d}",
        "sec": sec,
        "page": page,
        "q": text,
        "opts": opts,
        "ans": ans,
        "exp": exp,
    })

# ---------------- p227 ----------------
S1 = "Colorectal Cancer Surgery: Vascular Anatomy and Watershed Zones"
q(227, S1, "Griffith's point is located at the:",
  ["Splenic flexure", "Hepatic flexure", "Ileocecal junction", "Anal verge"], 0,
  "The diagram labels Griffith's point at the splenic flexure. (Book p227)")
q(227, S1, "Why is Griffith's point surgically important?",
  ["It is a watershed area with insufficient blood supply", "It contains the appendicular artery", "It marks the dentate line", "It is the most common site of anal cancer"], 0,
  "The page states that Griffith's point is a watershed area with insufficient blood supply, making healing less reliable. (Book p227)")
q(227, S1, "Which statement best explains why the splenic flexure is a difficult area for colorectal resection and anastomosis?",
  ["Its blood supply is relatively poor", "It lacks lymphatic drainage", "It has no marginal artery", "It always lies retroperitoneally"], 0,
  "The page specifically links the splenic flexure with difficult resection and anastomosis because it is a watershed zone with poor blood supply. (Book p227)")
q(227, S1, "Sudeck point is another classical:",
  ["Watershed area", "Zone of appendicular perforation", "Plane for TME", "Site of rectal pain sensation loss"], 0,
  "Sudeck point is explicitly labeled as a watershed area on the vascular diagram. (Book p227)")
q(227, S1, "The collateral arcade running along the colorectum in this diagram is the:",
  ["Marginal artery of Drummond", "Artery of Seshachalam", "Arc of Buhler", "Inferior epigastric artery"], 0,
  "The figure names the longitudinal collateral supply as the marginal artery of Drummond. (Book p227)")
q(227, S1, "In the vascular diagram, SMA stands for:",
  ["Superior mesenteric artery", "Superior mesorectal artery", "Submucosal arterial arcade", "Splenic marginal artery"], 0,
  "The boxed note on the page expands SMA as superior mesenteric artery. (Book p227)")
q(227, S1, "In the vascular diagram, IMA stands for:",
  ["Inferior mesenteric artery", "Internal mesorectal artery", "Ileo-marginal artery", "Inferior mucosal artery"], 0,
  "The same note expands IMA as inferior mesenteric artery. (Book p227)")
q(227, S1, "Griffith's point lies between which two arterial territories in the diagram?",
  ["Middle colic and left colic", "Ileocolic and right colic", "Sigmoid and superior rectal", "Inferior rectal and middle rectal"], 0,
  "The splenic flexure watershed lies between the middle colic and left colic territories. (Book p227)")
q(227, S1, "Sudeck point in the diagram corresponds to the watershed around the junction of the:",
  ["Sigmoid and superior rectal territories", "Middle colic and left colic territories", "Ileocolic and right colic territories", "Internal and external iliac territories"], 0,
  "The rectosigmoid watershed shown as Sudeck point lies at the junction of the sigmoid and superior rectal supply. (Book p227)")
q(227, S1, "The artery continuing distally toward the rectum in the diagram is the:",
  ["Superior rectal artery", "Middle colic artery", "Right colic artery", "Ileocolic artery"], 0,
  "The distal continuation of the IMA in the diagram is labeled as the superior rectal artery. (Book p227)")

S2 = "Colorectal Cancer Surgery: Segmental Resections for Colonic Tumours"
q(227, S2, "A caecal carcinoma in this table is treated by:",
  ["Right hemicolectomy", "Left hemicolectomy", "Sigmoidectomy", "APR"], 0,
  "The surgical management table maps caecal tumours to right hemicolectomy. (Book p227)")
q(227, S2, "Which bowel segment is specifically included in a right hemicolectomy according to the page?",
  ["Terminal 10-12 cm of ileum", "Entire jejunum", "Rectum", "Distal sigmoid only"], 0,
  "The table lists the terminal 10-12 cm of ileum among the parts removed in right hemicolectomy. (Book p227)")
q(227, S2, "Right hemicolectomy for caecal tumour removes all of the following EXCEPT:",
  ["Descending colon", "Caecum", "Ascending colon", "Hepatic flexure"], 0,
  "For a caecal tumour, right hemicolectomy includes terminal ileum, caecum, ascending colon, hepatic flexure, and right transverse colon, not descending colon. (Book p227)")
q(227, S2, "In right hemicolectomy, the transverse colon is removed up to the:",
  ["Right middle colic artery", "Left branch of middle colic", "Splenic flexure only", "Superior rectal artery"], 0,
  "The table specifies removal of the right part of transverse colon until the right middle colic artery. (Book p227)")
q(227, S2, "Arterial ligation in right hemicolectomy includes all of the following EXCEPT:",
  ["Left colic artery", "Right branch of middle colic", "Ileocolic artery", "Right colic artery"], 0,
  "The right hemicolectomy row lists ligation of the right branch of middle colic, ileocolic, and right colic arteries, not the left colic artery. (Book p227)")
q(227, S2, "Tumours of the ascending colon, hepatic flexure, or transverse colon are treated in this chapter by:",
  ["Extended right hemicolectomy", "Sigmoidectomy", "Left hemicolectomy", "Transanal excision"], 0,
  "The table groups ascending colon, hepatic flexure, and transverse colon tumours under extended right hemicolectomy. (Book p227)")
q(227, S2, "Which of the following is specifically included in an extended right hemicolectomy?",
  ["Right part of transverse colon", "Anal canal", "Only caecum and appendix", "Descending colon only"], 0,
  "Extended right hemicolectomy includes terminal ileum, caecum, ascending colon, hepatic flexure, and the right part of the transverse colon. (Book p227)")
q(227, S2, "The page notes that which segment may occasionally also be removed during extended right hemicolectomy to improve the anastomotic outcome?",
  ["Splenic flexure", "Rectum", "Anal canal", "Jejunum"], 0,
  "The note in the extended right hemicolectomy row states that the splenic flexure is occasionally removed to obtain a better outcome during anastomosis. (Book p227)")
q(227, S2, "Arterial ligation in extended right hemicolectomy includes:",
  ["Middle colic, ileocolic, and right colic arteries", "Left colic, sigmoid, and superior rectal arteries", "Only ileocolic artery", "Inferior epigastric artery and IMA"], 0,
  "The extended right hemicolectomy row lists middle colic, ileocolic, and right colic as the arteries ligated. (Book p227)")

# ---------------- p228 ----------------
S3 = "Colorectal Cancer Surgery: Left-sided Colonic Resections"
q(228, S3, "A tumour confined to the transverse colon only is treated by:",
  ["Transverse colectomy", "Extended right hemicolectomy", "Left hemicolectomy", "Sigmoidectomy"], 0,
  "The table on page 228 assigns transverse-colon-only lesions to transverse colectomy. (Book p228)")
q(228, S3, "What disadvantage of transverse colectomy is highlighted in the chapter?",
  ["Poor blood supply of the splenic flexure", "Very high risk of ureteric injury", "Need for permanent colostomy", "Cannot remove lymph nodes"], 0,
  "The page explicitly states that transverse colectomy has the disadvantage of poor blood supply of the splenic flexure. (Book p228)")
q(228, S3, "Tumours of the splenic flexure, descending colon, and proximal sigmoid colon are managed by:",
  ["Left hemicolectomy", "Right hemicolectomy", "APR", "Transanal total mesorectal excision"], 0,
  "The page groups splenic flexure, descending colon, and proximal sigmoid tumours under left hemicolectomy. (Book p228)")
q(228, S3, "Which of the following arteries is listed among those ligated in left hemicolectomy?",
  ["Left branch of middle colic", "Ileocolic", "Right colic", "Inferior epigastric"], 0,
  "The left hemicolectomy row lists the left branch of middle colic as one of the arteries ligated. (Book p228)")
q(228, S3, "In left hemicolectomy, which additional named artery is specifically ligated?",
  ["Left colic artery", "Appendicular artery", "Right branch of middle colic", "Gastroduodenal artery"], 0,
  "The table lists left colic artery ligation as part of left hemicolectomy. (Book p228)")
q(228, S3, "The third vessel listed in the arterial ligation column for left hemicolectomy is the:",
  ["Sigmoid artery", "Superior rectal artery", "Middle rectal artery", "Marginal artery"], 0,
  "The row shows left branch of middle colic, left colic, and sigmoid arteries as the vessels ligated. (Book p228)")
q(228, S3, "High ligation of the IMA during left hemicolectomy is considered acceptable on this page because the rectum still has blood supply from the:",
  ["Middle and inferior rectal arteries", "Ileocolic and right colic arteries", "Inferior epigastric and obturator arteries", "Superior gluteal and internal pudendal arteries"], 0,
  "The note beside high IMA ligation says the rectum continues to receive blood supply from the middle and inferior rectal arteries. (Book p228)")
q(228, S3, "A tumour confined to the sigmoid colon only is treated by:",
  ["Sigmoidectomy", "Left hemicolectomy", "Right hemicolectomy", "APR"], 0,
  "The last row of the table maps sigmoid-colon-only lesions to sigmoidectomy. (Book p228)")
q(228, S3, "Which operation in the illustrated sequence corresponds to resection for proximal sigmoid tumour rather than sigmoid-only tumour?",
  ["Left hemicolectomy", "Right hemicolectomy", "Transverse colectomy", "APR"], 0,
  "The table distinguishes proximal sigmoid colon lesions, which require left hemicolectomy, from sigmoid-only lesions, which are treated by sigmoidectomy. (Book p228)")

S4 = "Rectal Cancer Surgery: Landmarks and Continence-related Anatomy"
q(228, S4, "The anorectal ring is formed by the:",
  ["Levator ani", "Puborectalis alone", "Internal sphincter", "Taenia coli"], 0,
  "The diagram states that the anorectal ring is formed by the levator ani. (Book p228)")
q(228, S4, "The dentate line lies approximately how far below the anorectal ring on the diagram?",
  ["2-2.5 cm", "5 cm", "10 cm", "1 cm"], 0,
  "The measurement shown between the anorectal ring and dentate line is 2-2.5 cm. (Book p228)")
q(228, S4, "The anal verge lies approximately how far below the dentate line on the diagram?",
  ["2-2.5 cm", "5 cm", "10 cm", "0.5 cm"], 0,
  "The measurement from dentate line to anal verge is also shown as 2-2.5 cm. (Book p228)")
q(228, S4, "Above the dentate line there are usually:",
  ["No pain sensations", "Marked somatic pain sensations", "Only temperature sensations", "Only proprioceptive sensations"], 0,
  "The diagram explicitly says that above the dentate line there are no pain sensations. (Book p228)")
q(228, S4, "Below the dentate line, pain sensation is:",
  ["Present", "Absent", "Only visceral", "Always referred to the umbilicus"], 0,
  "The page states that below the dentate line pain sensations are present. (Book p228)")
q(228, S4, "Which structures are shown within 5 cm of the anal canal and are important for continence?",
  ["Internal and external anal sphincters", "Middle and inferior rectal arteries", "Superior hypogastric plexus and pelvic plexus", "Taenia coli and mesoappendix"], 0,
  "The diagram notes the internal and external anal sphincters within 5 cm of the anal canal and states that they maintain continence. (Book p228)")
q(228, S4, "Why is a very low rectal tumour surgically challenging according to this anatomical diagram?",
  ["It may involve the continence-preserving sphincters", "It always metastasizes to the liver first", "It has no lymphatic drainage", "It lies above the dentate line only"], 0,
  "The page emphasizes that the continence-maintaining internal and external sphincters lie within 5 cm of the anal canal. (Book p228)")

# ---------------- p229 ----------------
S5 = "Rectal Cancer Surgery: Margins, LAR versus APR and Total Mesorectal Excision"
q(229, S5, "The proximal margin recommended for rectal cancer surgery on this page is:",
  ["5 cm", "2 cm", "1 cm", "10 cm"], 0,
  "The principles box lists a proximal margin of 5 cm. (Book p229)")
q(229, S5, "The distal margin recommended for rectal cancer surgery on this page is:",
  ["2 cm", "5 cm", "1 mm", "8 cm"], 0,
  "The same box specifies a distal margin of 2 cm. (Book p229)")
q(229, S5, "The radial margin recommended in this chapter is:",
  ["5 cm", "2 cm", "1 cm", "0.5 cm"], 0,
  "A radial margin of 5 cm is listed, with the note that this relates to radially situated lymph nodes. (Book p229)")
q(229, S5, "Why is a wider radial margin emphasized in the page's schematic?",
  ["Because lymph nodes are radially situated", "Because the appendix is retrocaecal", "Because the dentate line has no pain fibres", "Because the IMA has no collaterals"], 0,
  "The page directly explains the radial margin by the presence of radially situated lymph nodes. (Book p229)")
q(229, S5, "A tumour more than 5 cm from the anal verge, especially in the mid-rectum or distal sigmoid, is treated by:",
  ["Low anterior resection", "Abdominoperineal resection", "Sigmoidectomy only", "Local excision only"], 0,
  "The algorithm maps tumours more than 5 cm from the anal verge, including mid-rectal and distal sigmoid lesions, to low anterior resection. (Book p229)")
q(229, S5, "A tumour within 5 cm from the anal verge is treated by:",
  ["Abdominoperineal resection", "Low anterior resection", "Only chemoradiation", "Right hemicolectomy"], 0,
  "The opposite branch of the algorithm shows tumours within 5 cm from the anal verge going to APR. (Book p229)")
q(229, S5, "Why does APR commonly sacrifice continence?",
  ["A major part of the sphincter is resected", "The marginal artery is divided", "Only the serosa is preserved", "Because the ileum is also removed"], 0,
  "The figure notes that APR involves resection of a major part of the sphincter, leading to incontinence. (Book p229)")
q(229, S5, "The permanent stoma associated with APR is a:",
  ["End colostomy", "Loop ileostomy", "Mucus fistula", "Jejunostomy"], 0,
  "APR is shown ending in a permanent end colostomy. (Book p229)")
q(229, S5, "Which statement correctly describes low anterior resection (LAR) on this page?",
  ["Most of the sphincter is retained, so incontinence is avoided", "The anal canal is removed completely", "It always requires permanent colostomy", "It is used only for caecal cancer"], 0,
  "The LAR branch states that the majority of sphincter is retained and there is no incontinence. (Book p229)")
q(229, S5, "The parts removed during LAR are the:",
  ["Rectum and part of sigmoid", "Anal canal and rectum", "Only anal canal", "Terminal ileum and caecum"], 0,
  "The LAR notes list removal of the rectum and part of sigmoid. (Book p229)")
q(229, S5, "What proportion of the rectum is covered by peritoneum according to this page?",
  ["Upper one-third", "Lower one-third", "Entire rectum", "Rectum is completely extraperitoneal"], 0,
  "The page states that the peritoneum covers the upper one-third of the rectum. (Book p229)")
q(229, S5, "After opening the peritoneum in LAR, resection proceeds:",
  ["Below the level of the peritoneum", "Only above the pelvic brim", "Within the mesoappendix", "Through the anal sphincter complex"], 0,
  "The sequence on the page is peritoneum opened, then resection below the level of the peritoneum. (Book p229)")
q(229, S5, "The coloanal anastomosis in LAR is shown being created with a:",
  ["Circular stapler", "Linear stapler", "Hand-sewn purse string only", "Mesh ring"], 0,
  "The figure specifically mentions coloanal anastomosis by circular stapler. (Book p229)")
q(229, S5, "APR removes which parts according to the page?",
  ["Anal canal and rectum", "Rectum and part of sigmoid only", "Caecum and ascending colon", "Distal ileum and caecum"], 0,
  "The APR notes list the anal canal and rectum as the parts removed. (Book p229)")
q(229, S5, "The page highlights careful choice of dissection plane in APR mainly to avoid:",
  ["Nerve injury", "Bile leak", "Short bowel syndrome", "Anastomotic stricture"], 0,
  "A bullet point under APR explicitly says the plane of dissection is chosen to avoid nerve injury. (Book p229)")
q(229, S5, "The anterior fascial landmark shown near the prostate and seminal vesicle is:",
  ["Denonvilliers' fascia", "Gerota's fascia", "Buck's fascia", "Scarpa's fascia"], 0,
  "The lower-right cross-sectional diagram labels Denonvilliers' fascia anteriorly. (Book p229)")
q(229, S5, "The ideal dissection plane highlighted in the rectal surgery diagram is called the:",
  ["Holy plane", "Critical view", "Calot plane", "Plane of Toldt"], 0,
  "The figure explicitly labels the mesorectal dissection plane as the 'holy plane'. (Book p229)")
q(229, S5, "Total mesorectal excision (TME) on this page includes removal of at least how many lymph nodes?",
  ["12", "6", "20", "2"], 0,
  "The note under the bracket for total mesorectal excision says removal of a minimum of 12 lymph nodes. (Book p229)")

# ---------------- p230 ----------------
S6 = "Rectal Cancer Surgery: TaTME, Complications, Nerve Injury and Obstruction"
q(230, S6, "Transanal total mesorectal excision (TaTME) is described as a:",
  ["NOTES procedure", "Open transabdominal bypass", "Purely radiologic intervention", "Perineal flap reconstruction"], 0,
  "The page defines TaTME as a natural orifice transluminal endoscopic surgery (NOTES) procedure. (Book p230)")
q(230, S6, "The indications listed for TaTME are:",
  ["T1 and T2 tumours", "T3 and T4 tumours only", "Only metastatic disease", "Only recurrent anal cancer"], 0,
  "The indication line specifically mentions T1 and T2 tumours. (Book p230)")
q(230, S6, "One major functional advantage of TaTME noted on the page is:",
  ["Sphincter preservation", "Guaranteed fertility preservation", "Avoidance of lymphadenectomy", "Need for no bowel preparation"], 0,
  "The page states that the sphincter is preserved in TaTME. (Book p230)")
q(230, S6, "How are the initial trial results of TaTME summarized in the chapter?",
  ["Safe procedure", "Unsafe and abandoned", "Useful only in children", "Inferior to APR in every case"], 0,
  "The line under TaTME states that initial trials found it to be a safe procedure. (Book p230)")
q(230, S6, "Which of the following is listed as a complication of colorectal surgery?",
  ["Anastomotic leak", "Biliary peritonitis", "Hemobilia", "Portal cavernoma"], 0,
  "The complication list includes bleeding, infection, leak, abscesses, recurrence, and nerve injuries. (Book p230)")
q(230, S6, "All of the following are listed complications of colorectal surgery EXCEPT:",
  ["Chylothorax", "Bleeding", "Abscesses", "Recurrence"], 0,
  "The page lists bleeding, infection, leak, abscesses, recurrence, and nerve injuries; chylothorax is not listed. (Book p230)")
q(230, S6, "High ligation of the IMA risks injury to which nerve plexus?",
  ["Superior hypogastric plexus near the sacral promontory", "Periprostatic plexus", "Pelvic plexus with nervi erigentes", "Pudendal plexus"], 0,
  "The nerve-injury table links high IMA ligation with superior hypogastric plexus injury near the sacral promontory. (Book p230)")
q(230, S6, "The characteristic consequence of superior hypogastric plexus injury during high IMA ligation is:",
  ["Retrograde ejaculation in men", "True urinary incontinence", "Foot drop", "Constipation only"], 0,
  "The table specifically lists retrograde ejaculation in men due to sympathetic dysfunction. (Book p230)")
q(230, S6, "Division of lateral stalks close to the pelvic sidewall may injure the:",
  ["Pelvic plexus and nervi erigentes", "Superior hypogastric plexus alone", "Periprostatic plexus only", "Femoral nerve"], 0,
  "The second row of the table names the pelvic plexus and nervi erigentes. (Book p230)")
q(230, S6, "Which clinical problem best fits pelvic plexus and nervi erigentes injury during rectal surgery?",
  ["Erectile dysfunction, impotence, and atonic bladder", "Retrograde ejaculation only", "Bowel obstruction from mucus", "Isolated perianal pain"], 0,
  "The table associates pelvic plexus and nervi erigentes injury with erectile dysfunction, impotence, and atonic bladder. (Book p230)")
q(230, S6, "Anterior dissection during rectal surgery risks injury to the:",
  ["Periprostatic plexus", "Superior hypogastric plexus", "Vagus nerve", "Inferior mesenteric vein"], 0,
  "The third row in the nerve-injury table lists the periprostatic plexus. (Book p230)")
q(230, S6, "Periprostatic plexus injury during anterior dissection causes:",
  ["Sexual and bladder dysfunction", "Retrograde ejaculation only", "Blindness", "Upper limb weakness"], 0,
  "The table summarizes the consequences of periprostatic plexus injury as sexual and bladder dysfunction. (Book p230)")
q(230, S6, "In obstructing colorectal cancer, endoscopic stent placement is used mainly as a bridge to:",
  ["Definitive surgery", "Permanent conservative treatment", "Radiotherapy only", "Chemotherapy only"], 0,
  "The emergency management section shows endoscopic stent placement followed by definitive surgery. (Book p230)")
q(230, S6, "Hartmann/Paul Mikulicz procedure in the chapter creates a proximal:",
  ["Colostomy", "Ileostomy", "Jejunostomy", "Gastrostomy"], 0,
  "The diagram labels the proximal end as a colostomy. (Book p230)")
q(230, S6, "In Hartmann/Paul Mikulicz procedure, the distal end is fashioned as a:",
  ["Mucus fistula", "Blind pouch with no decompression", "Ileal conduit", "Feeding jejunostomy"], 0,
  "The distal end is labeled as a mucus fistula in the schematic. (Book p230)")
q(230, S6, "Why is a distal mucus fistula created in the obstructed colon according to the page?",
  ["To prevent perforation due to mucus accumulation", "To improve urinary drainage", "To preserve anal sphincters", "To reduce postoperative jaundice"], 0,
  "The diagram explicitly says the mucus fistula prevents perforation due to mucus accumulation. (Book p230)")
q(230, S6, "Definitive surgery after a Hartmann/Paul Mikulicz decompressive procedure is planned after:",
  ["A few weeks", "24 hours", "6 months", "Only after recurrence"], 0,
  "The arrow in the diagram indicates definitive surgery after a few weeks. (Book p230)")
q(230, S6, "Chemotherapy is indicated for colorectal cancer on this page in all of the following EXCEPT:",
  ["T1 node-negative localized lesion", "T3 lesion", "T4 lesion", "Metastatic disease"], 0,
  "The indication bullets mention T3/T4 lesions, lymph node positivity, and metastasis. T1 node-negative disease is not listed. (Book p230)")
q(230, S6, "Lymph node positivity is an indication for:",
  ["Chemotherapy", "TaTME only", "APR only", "No additional treatment"], 0,
  "The chemotherapy section explicitly includes lymph node positive disease among the indications. (Book p230)")

# ---------------- p231 ----------------
S7 = "Colorectal Cancer: Chemotherapy Regimens, Radiotherapy, Immunotherapy and Liver Metastasis"
q(231, S7, "Which combination correctly defines FOLFOX in this chapter?",
  ["5-fluorouracil + folinic acid + oxaliplatin", "5-fluorouracil + folinic acid + irinotecan", "Cetuximab + bevacizumab + folinic acid", "Mitomycin C + 5-fluorouracil + paclitaxel"], 0,
  "The regimen list shows FOLFOX as 5-fluorouracil, folinic acid, and oxaliplatin. (Book p231)")
q(231, S7, "Which drug differentiates FOLFIRI from FOLFOX on this page?",
  ["Irinotecan replaces oxaliplatin", "Cetuximab replaces folinic acid", "Bevacizumab replaces 5-FU", "Mitomycin replaces irinotecan"], 0,
  "FOLFIRI contains irinotecan, whereas FOLFOX contains oxaliplatin; both retain 5-FU and folinic acid. (Book p231)")
q(231, S7, "Which two drugs are common to both FOLFOX and FOLFIRI?",
  ["5-fluorouracil and folinic acid", "Oxaliplatin and irinotecan", "Cetuximab and bevacizumab", "Mitomycin C and pembrolizumab"], 0,
  "Both listed regimens contain 5-fluorouracil and folinic acid. (Book p231)")
q(231, S7, "Radiotherapy is indicated for:",
  ["Rectal cancer, not colonic cancer", "Colonic cancer, not rectal cancer", "All right-sided colonic cancers only", "Only liver metastasis"], 0,
  "The radiotherapy section explicitly says it is for rectal cancer and not for colonic cancer. (Book p231)")
q(231, S7, "Advanced rectal cancer on this page is treated with:",
  ["Neoadjuvant chemoradiation followed by surgery", "Immediate APR without staging", "Chemotherapy alone", "Radiotherapy only after liver resection"], 0,
  "The indicated sequence for advanced rectal cancer is neoadjuvant chemoradiation followed by surgery. (Book p231)")
q(231, S7, "A major advantage of neoadjuvant chemoradiation for rectal cancer according to the chapter is:",
  ["Sphincter preservation", "Prevention of all metastasis", "Avoidance of biopsy", "Elimination of need for surgery in all patients"], 0,
  "The page specifically notes sphincter preservation as the advantage. (Book p231)")
q(231, S7, "The short-course duration of radiotherapy in rectal cancer is:",
  ["5-6 days", "2-3 weeks", "6 months", "24 hours"], 0,
  "The page lists short-course rectal radiotherapy as 5-6 days. (Book p231)")
q(231, S7, "The long-course duration of rectal radiotherapy is described as:",
  ["A few weeks", "5-6 days", "One day", "Several months of daily treatment without surgery"], 0,
  "The page contrasts short course with long course, which it describes as lasting a few weeks. (Book p231)")
q(231, S7, "The named intracavity radiotherapy technique for rectal cancer is:",
  ["Papillon", "Nigro", "PAIR", "Whipple"], 0,
  "The radiotherapy section lists Papillon as the intracavity radiotherapy technique. (Book p231)")
q(231, S7, "Immunotherapy for colorectal cancer is indicated on this page mainly in the setting of:",
  ["Metastatic disease", "T1 mucosal carcinoma only", "Benign adenomatous polyp", "Solitary juvenile polyp"], 0,
  "The immunotherapy section gives metastasis as the indication. (Book p231)")
q(231, S7, "The most common metastatic site highlighted for colorectal cancer is the:",
  ["Liver", "Brain", "Adrenal gland", "Bone"], 0,
  "The page specifically notes liver as the most common site of metastasis. (Book p231)")
q(231, S7, "Bevacizumab is listed as an:",
  ["Anti-VEGF agent", "Anti-EGFR agent", "PDL1 inhibitor", "Topoisomerase inhibitor"], 0,
  "The drug-function table lists bevacizumab as anti-VEGF, a vascular growth factor inhibitor. (Book p231)")
q(231, S7, "Cetuximab is listed as an:",
  ["Anti-EGFR agent", "Anti-VEGF agent", "PDL1 inhibitor", "Antimetabolite"], 0,
  "The same table lists cetuximab as anti-EGFR, an epidermal growth factor inhibitor. (Book p231)")
q(231, S7, "According to the source table, which agent is grouped with pembrolizumab under the PDL1-inhibitor row?",
  ["Pantimunab", "Bevacizumab", "Cetuximab", "Oxaliplatin"], 0,
  "The page's table groups Pantimunab and Pembrolizumab together under the PDL1 inhibitor row. (Book p231)")
q(231, S7, "Liver metastasis is said to occur in approximately what proportion of colorectal carcinomas?",
  ["60%", "10%", "25%", "90%"], 0,
  "The liver metastasis section states that liver metastases are seen in 60% of colorectal carcinoma. (Book p231)")
q(231, S7, "Synchronous colorectal liver metastasis refers to liver metastasis occurring:",
  ["Within 1 year of colorectal cancer", "More than 1 year after colorectal cancer", "Only before the primary tumour is diagnosed", "Only after colostomy closure"], 0,
  "The diagram defines synchronous liver metastasis as occurring within 1 year of colorectal cancer. (Book p231)")
q(231, S7, "Metachronous colorectal liver metastasis refers to liver metastasis occurring:",
  [">1 year after colorectal cancer", "Within 1 year of colorectal cancer", "Only in rectal cancer", "Only after chemotherapy"], 0,
  "The opposite branch of the diagram defines metachronous liver metastasis as occurring more than 1 year after colorectal cancer. (Book p231)")
q(231, S7, "Which statement about resection of colorectal liver metastasis is emphasized on the page?",
  ["It improves survival", "It is never beneficial", "It is contraindicated if there are multiple lesions", "It is replaced entirely by immunotherapy"], 0,
  "Under management, the page clearly states that resection improves survival. (Book p231)")
q(231, S7, "The chapter gives the minimum functional liver reserve (FLR) required for resection of colorectal liver metastasis as:",
  [">25%", ">10%", ">50%", ">75%"], 0,
  "The page lists an FLR of more than 25% as the indication threshold for safe resection. (Book p231)")
q(231, S7, "Regarding resection of colorectal liver metastasis, the page specifically states that the number of metastases is:",
  ["Not a criterion for resection", "An absolute contraindication if more than one", "More important than FLR", "Irrelevant only in synchronous disease"], 0,
  "A separate bullet explicitly says the number of liver metastases is not a criterion for resection. (Book p231)")

# ---------------- p232 ----------------
S8 = "Anal Cancer: Prognostic Factors, Diagnosis and Nigro Regimen"
q(232, S8, "The most important prognostic factor for colorectal carcinoma on this page is:",
  ["Lymph node status", "CEA alone", "Tumour side", "Patient sex"], 0,
  "The first bullet under prognostic factors identifies lymph node status as the most important factor. (Book p232)")
q(232, S8, "The tumour marker listed for colorectal carcinoma and used for follow-up is:",
  ["CEA", "AFP", "CA 19-9", "PSA"], 0,
  "The page names CEA as the tumour marker and specifically notes it is used for follow-up. (Book p232)")
q(232, S8, "The most common histology of anal cancer mentioned in this chapter is:",
  ["Squamous cell carcinoma", "Adenocarcinoma", "Neuroendocrine tumour", "Melanoma"], 0,
  "Under anal cancer, squamous cell carcinoma is marked as the most common type. (Book p232)")
q(232, S8, "Anal adenocarcinoma is described as:",
  ["Uncommon", "The commonest anal cancer", "Always metastatic at presentation", "A premalignant lesion"], 0,
  "The branch for adenocarcinoma explicitly labels it uncommon. (Book p232)")
q(232, S8, "Treatment of anal adenocarcinoma on this page is said to be the same as treatment of:",
  ["Rectal cancer within 5 cm from the anal verge", "Caecal cancer", "Anal fissure", "Pilonidal sinus"], 0,
  "The adenocarcinoma branch says it is treated the same as rectal cancer within 5 cm from the anal verge. (Book p232)")
q(232, S8, "Which viral infection is listed as a risk factor for squamous cell carcinoma of the anus?",
  ["Human papilloma virus", "Hepatitis B virus", "Epstein-Barr virus", "CMV"], 0,
  "Human papilloma virus is explicitly listed among the risk factors. (Book p232)")
q(232, S8, "Which immunodeficiency-associated infection is also listed as a risk factor for anal squamous carcinoma?",
  ["HIV", "HCV", "Tuberculosis", "Helicobacter pylori"], 0,
  "HIV is one of the stated risk factors for anal squamous cell carcinoma. (Book p232)")
q(232, S8, "Which population is specifically mentioned on the page as being at higher risk for anal squamous carcinoma?",
  ["Homosexual individuals, with males more affected than females", "Postmenopausal women alone", "Children with Meckel's diverticulum", "Patients after appendicectomy"], 0,
  "The page lists homosexual individuals and notes male predominance over females. (Book p232)")
q(232, S8, "Common clinical features of anal cancer listed on the page include:",
  ["Mass and bleeding", "Jaundice and ascites", "Hematemesis and dysphagia", "Constipation and biliary colic"], 0,
  "The clinical-features bullets list mass and bleeding. (Book p232)")
q(232, S8, "The investigation of choice for tissue diagnosis of anal cancer is:",
  ["Biopsy", "CEA", "FOBT", "Virtual colonoscopy"], 0,
  "The page states 'Biopsy: IOC,' making biopsy the key diagnostic test. (Book p232)")
q(232, S8, "MRI in anal cancer is used mainly for:",
  ["Local staging", "Detecting synchronous liver metastasis only", "Screening relatives", "Assessing vascular watershed areas"], 0,
  "The investigation section specifies MRI for local staging. (Book p232)")
q(232, S8, "The Nigro regimen is the:",
  ["Management of anal cancer with combined chemoradiation", "Named operation for low rectal cancer", "Screening strategy for FAP", "Emergency procedure for obstructed colon"], 0,
  "The page defines the Nigro regime as the management of anal cancer using combined chemoradiation. (Book p232)")
q(232, S8, "The Nigro regimen is administered approximately how long before surgery according to the page?",
  ["1 month", "24 hours", "6 months", "Only after recurrence"], 0,
  "A bullet under the Nigro regimen says it is administered 1 month prior to surgery. (Book p232)")
q(232, S8, "The chemotherapeutic agents listed with radiotherapy in the Nigro regimen are:",
  ["5-fluorouracil and mitomycin C", "Oxaliplatin and irinotecan", "Cetuximab and bevacizumab", "Paclitaxel and cisplatin"], 0,
  "The page states RT plus chemotherapy with 5-FU and mitomycin C. (Book p232)")
q(232, S8, "The intended effect of the Nigro regimen before surgery is:",
  ["Downstaging", "Immediate cure without monitoring", "Only symptom relief without tumour response", "Induction of jaundice"], 0,
  "The central arrow beneath the regimen is labeled downstaging. (Book p232)")
q(232, S8, "If complete response occurs after the Nigro regimen, the next step shown is:",
  ["Monitor", "Immediate APR", "Immediate sigmoidectomy", "No follow-up required"], 0,
  "The flowchart shows complete response leading to monitoring. (Book p232)")
q(232, S8, "The recurrence rate after complete response mentioned in the flowchart is:",
  ["20-30%", "1-2%", "50-60%", "90%"], 0,
  "Beneath the monitoring branch, the page notes recurrence in about 20-30% of cases. (Book p232)")
q(232, S8, "Recurrence after an initial complete response to the Nigro regimen is treated by:",
  ["Abdominoperineal resection", "Repeat appendicectomy", "Left hemicolectomy", "Observation only"], 0,
  "The recurrence arrow in the flowchart leads to abdominoperineal resection. (Book p232)")
q(232, S8, "Residual tumour after the Nigro regimen, when located within 5 cm, is managed by:",
  ["Abdominoperineal resection", "Simple local excision only", "Chemotherapy alone", "Sigmoidectomy"], 0,
  "The residual-tumour branch points to APR for tumour within 5 cm. (Book p232)")

# ---------------- units ----------------
def sec_ids(*labels):
    return [x["id"] for x in Q if x["sec"] in labels]

def first_page(label):
    for x in Q:
        if x["sec"] == label:
            return x["page"]
    return 0

UNIT_DEFS = [
    (S1, "Before operations make sense, the vascular map must be clear. Griffith's point at the splenic flexure and Sudeck point at the rectosigmoid are classic watershed zones, so poor perfusion explains difficult anastomoses and segment-specific surgical caution."),
    (S2, "The colonic resection table is a practical anatomy exam: caecum means right hemicolectomy, more proximal transverse involvement pushes you toward extended right hemicolectomy, and every answer must be anchored to which bowel is removed and which vessels are tied."),
    (S3, "Left-sided colon surgery is the mirror image but not a clone. Know when to choose transverse colectomy, left hemicolectomy, or sigmoidectomy, and remember why high IMA ligation is tolerated - the rectum still receives middle and inferior rectal arterial supply."),
    (S4, "Low rectal surgery is governed by landmarks, not guesswork. The anorectal ring, dentate line, anal verge, and sphincters explain pain patterns as well as why a tumour within the lowest 5 cm threatens continence-preserving surgery."),
    (S5, "Rectal cancer surgery lives on margins and sphincter preservation. LAR is for higher lesions and preserves continence, APR is for very low tumours and ends with a permanent colostomy, and TME succeeds only when the holy plane is respected."),
    (S6, "This unit links innovation with complications. TaTME is a NOTES-based sphincter-preserving option for early tumours, but the surgeon must also anticipate leaks, abscesses, recurrence and the very specific sexual/bladder deficits produced by injury at different pelvic dissection levels."),
    (S7, "Systemic and local adjuvant therapy becomes structured here: FOLFOX versus FOLFIRI, radiotherapy for rectum not colon, and the source table's immunotherapy pairings. Finish by thinking surgically about liver metastasis - resectability depends on reserve and biology, not simply lesion count."),
    (S8, "The chapter ends by turning to anal cancer. Node status still dominates prognosis, CEA is for follow-up, squamous cancer carries HPV/HIV associations, and the Nigro regimen is the central treatment pathway, with APR reserved for recurrence or persistent very low disease."),
]

UNITS = []
for i, (title, guide) in enumerate(UNIT_DEFS, 1):
    UNITS.append({
        "id": f"SURG-U32-{i}",
        "ch": 32,
        "n": i,
        "title": title,
        "sec": f"{title} · p{first_page(title)}",
        "qs": sec_ids(title),
        "guide": guide,
    })

covered = [i for u in UNITS for i in u["qs"]]
assert covered == [x["id"] for x in Q], "units must cover questions in order"

data = {"questions": Q, "units": UNITS}
with open("data/ch32.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
print(f"ch32: {len(Q)} questions, {len(UNITS)} units")
