#!/usr/bin/env python3
"""Build data/ch33.json — ch33 Rectum and Anal Canal (Marrow Surgery Ed 8, book p233-244)."""
import json

Q = []


def q(page, sec, text, opts, ans, exp):
    Q.append({
        "id": f"SURG-C33-{len(Q)+1:03d}",
        "sec": sec,
        "page": page,
        "q": text,
        "opts": opts,
        "ans": ans,
        "exp": exp,
    })


# ------------------------------------------------------------------ p233
S1 = "Surgical Anatomy of the Rectum"
q(233, S1, "The rectum measures approximately how much in length?",
  ["12-14 cm", "5-7 cm", "20-25 cm", "30-35 cm"], 0,
  "The chapter states that the rectum is 12-14 cm in length. (Book p233)")
q(233, S1, "The upper and the lower parts of the rectum are convex towards the:",
  ["Right", "Left", "Anteriorly", "Posteriorly"], 0,
  "Upper and lower parts of the rectum are convex towards the right. (Book p233)")
q(233, S1, "The middle part of the rectum is convex towards the:",
  ["Left", "Right", "Anteriorly", "Posteriorly"], 0,
  "The middle part of the rectum is convex towards the left — the rectum has three lateral curves. (Book p233)")
q(233, S1, "Which part of the rectum is not covered with peritoneum?",
  ["Lower part", "Upper third only", "Middle part", "Whole rectum"], 0,
  "Only the lower part of the rectum is not covered with peritoneum; the upper part is intraperitoneal. (Book p233)")
q(233, S1, "Resection of the rectum below the peritoneum is the applied anatomy of:",
  ["Low anterior resection", "Abdominoperineal resection only", "Right hemicolectomy", "Hartmann's procedure"], 0,
  "The applied anatomy note says that resection of rectum below the peritoneum is a low anterior resection. (Book p233)")

S2 = "Anal Canal: Landmarks and Epithelium"
q(233, S2, "The anorectal ring is formed by the:",
  ["Levator ani", "External sphincter only", "Internal sphincter only", "Pubococcygeus and iliococcygeus only"], 0,
  "The anorectal ring is formed by the levator ani. (Book p233)")
q(233, S2, "The distance from the anorectal ring to the dentate line is approximately:",
  ["2-2.5 cm", "0.5-1 cm", "5-6 cm", "8-10 cm"], 0,
  "The diagram labels the anorectal ring to dentate line distance as 2-2.5 cm. (Book p233)")
q(233, S2, "The distance from the dentate line to the anal verge is approximately:",
  ["2-2.5 cm", "0.5-1 cm", "5-6 cm", "8-10 cm"], 0,
  "The dentate line to anal verge distance is also labelled 2-2.5 cm, so the whole surgical anal canal is roughly 4-5 cm. (Book p233)")
q(233, S2, "Sensation above the dentate line is characterised by:",
  ["No pain sensations", "Exquisite pain sensation", "Only temperature sensation", "Only touch sensation"], 0,
  "Above the dentate line there are no pain sensations — that is why painless banding and injection are done there. (Book p233)")
q(233, S2, "Pain sensation below the dentate line is:",
  ["Present", "Absent", "Present only on the right side", "Absent because of pudendal blockade"], 0,
  "Below the dentate line pain sensations are present — the lining is somatic sensitive squamous epithelium. (Book p233)")
q(233, S2, "Injury to the anal sphincters results in:",
  ["Incontinence", "Rectal prolapse only", "Constipation only", "No functional deficit"], 0,
  "The page notes that injury to the sphincters causes incontinence. (Book p233)")
q(233, S2, "The epithelium proximal to the dentate line is:",
  ["Columnar", "Modified squamous", "Stratified keratinised squamous", "Transitional"], 0,
  "Proximal to the dentate line the epithelium is columnar. (Book p233)")
q(233, S2, "The tumour that arises from the epithelium proximal to the dentate line is:",
  ["Adenocarcinoma", "Squamous cell carcinoma", "Melanoma", "Basal cell carcinoma"], 0,
  "Columnar epithelium above the dentate line gives rise to adenocarcinoma. (Book p233)")
q(233, S2, "The epithelium distal to the dentate line is:",
  ["Modified squamous", "Columnar", "Cuboidal", "Transitional"], 0,
  "Distal to the dentate line the epithelium is modified squamous. (Book p233)")
q(233, S2, "A malignant growth of the epithelium distal to the dentate line is a:",
  ["Squamous cell carcinoma", "Adenocarcinoma", "Carcinoid", "Lymphoma"], 0,
  "Modified squamous epithelium below the dentate line gives rise to squamous cell carcinoma. (Book p233)")
q(233, S2, "A 60-year-old has a painful 1 cm ulcer at the anal margin. Pain localises the lesion to:",
  ["Below the dentate line", "Above the dentate line", "The rectosigmoid junction", "The anorectal ring"], 0,
  "Pain means somatic sensory epithelium, i.e. the lesion lies below the dentate line; lesions above it are painless. (Book p233)")

S3 = "Columns, Crypts and Haemorrhoidal Cushions"
q(233, S3, "The columns of Morgagni are:",
  ["Folds of mucosa above the dentate line", "Folds of mucosa below the dentate line", "Anal glands", "The three haemorrhoidal vessels"], 0,
  "Columns of Morgagni are folds of the mucosa above the dentate line. (Book p233)")
q(233, S3, "The communication between the anal crypts and the anal glands is clinically important because it is the:",
  ["Site of abscess formation", "Site of haemorrhoids", "Site of the dentate line", "Route of lymphatic spread to the liver"], 0,
  "The cryptoglandular communication is the site of abscess — the basis of the cryptoglandular hypothesis of fistula-in-ano. (Book p233)")
q(233, S3, "The submucosa of the distal anal canal contains:",
  ["3 haemorrhoidal cushions / vascular channels", "Only fat", "Only lymphatics", "Only smooth muscle"], 0,
  "There are 3 haemorrhoidal cushions (vascular channels) in the submucosa of the distal anal canal. (Book p233)")
q(233, S3, "Which of the following is NOT one of the three classical positions of the anal cushions?",
  ["Left posterior", "Left anterior", "Right anterior", "Right posterior"], 0,
  "The three primary positions are left anterior, right anterior and right posterior — not left posterior. (Book p233)")
q(233, S3, "Prolapse of the anal cushions produces:",
  ["Haemorrhoids", "Fissure", "Fistula", "Abscess"], 0,
  "The cushions prolapse to produce haemorrhoids; their position is the classical position of primary haemorrhoids. (Book p233)")

S4 = "Nerve Supply of the Anal Sphincters"
q(233, S4, "The internal anal sphincter receives parasympathetic fibres from:",
  ["S2, S3, S4", "L5", "T10-L1", "S1 only"], 0,
  "Internal sphincter: parasympathetic from S2, S3, S4. (Book p233)")
q(233, S4, "The sympathetic supply of the internal anal sphincter comes from:",
  ["L5", "T12", "S1", "S5"], 0,
  "Internal sphincter also receives sympathetic fibres from L5. (Book p233)")
q(233, S4, "The external anal sphincter is supplied by the:",
  ["Pudendal nerve (S2, S3, S4)", "Pelvic splanchnic nerves only", "Sympathetic chain only", "Ilioinguinal nerve"], 0,
  "External sphincter: pudendal nerve, S2, S3, S4. (Book p233)")
q(233, S4, "Bilateral injury of the pudendal nerve causes:",
  ["Incontinence", "No incontinence", "Only constipation", "Only rectal prolapse"], 0,
  "Bilateral (B/L) injury of the pudendal nerve causes incontinence. (Book p233)")
q(233, S4, "Unilateral injury of the pudendal nerve causes:",
  ["No incontinence", "Immediate incontinence", "Rectal prolapse", "Faecal impaction"], 0,
  "Unilateral (U/L) injury does not cause incontinence because the opposite side maintains the sphincter. (Book p233)")

# ------------------------------------------------------------------ p234
S5 = "Rectal Examination: Position, Inspection and DRE"
q(234, S5, "Digital rectal examination is performed with the patient in the:",
  ["Sim's / left lateral position", "Prone jack-knife position only", "Standing position", "Right lateral position only"], 0,
  "The position for DRE is Sim's (left lateral) position. (Book p234)")
q(234, S5, "Before performing a DRE the examinee must remember to do what the page lists first?",
  ["Inform the procedure and receive consent", "Give an enema", "Give sedation", "Catheterise the bladder"], 0,
  "The page lists informing the procedure and receiving consent as the first step. (Book p234)")
q(234, S5, "All of the following are looked for on inspection of the anal region EXCEPT:",
  ["Prostate size", "External opening of a fistula", "External haemorrhoids", "Growth"], 0,
  "Inspection looks for external opening of fistula, external haemorrhoids, a painful fissure and growth — the prostate is assessed by the examining finger, not by inspection. (Book p234)")
q(234, S5, "DRE is contraindicated when inspection shows:",
  ["A fissure", "External haemorrhoids", "A skin tag", "An external fistulous opening"], 0,
  "A fissure is painful, so DRE is contraindicated. (Book p234)")
q(234, S5, "The digit used for DRE in adults is the:",
  ["Right index finger", "Left index finger", "Thumb", "Middle finger"], 0,
  "In adults the (R) index finger is used. (Book p234)")
q(234, S5, "The digit used for DRE in children is the:",
  ["Little finger", "Index finger", "Thumb", "Ring finger"], 0,
  "In children the little finger is used. (Book p234)")
q(234, S5, "On DRE the anterior (12 o'clock) relation in a male is the:",
  ["Prostate", "Cervix", "Pouch of Douglas", "Sacral hollow"], 0,
  "Anteriorly in males the finger feels the prostate. (Book p234)")
q(234, S5, "On DRE the anterior relation in a female is the:",
  ["Cervix and pouch of Douglas", "Prostate", "Seminal vesicles", "Bladder neck only"], 0,
  "Anteriorly in females the finger feels the cervix and the pouch of Douglas. (Book p234)")
q(234, S5, "The lateral wall of the rectum on the clock face corresponds to:",
  ["3 o'clock", "12 o'clock", "6 o'clock", "8 o'clock"], 0,
  "The lateral wall is described as 3 o'clock (with the opposite lateral wall completing the clock face). (Book p234)")
q(234, S5, "The posterior relation felt on DRE corresponds to:",
  ["6 o'clock", "12 o'clock", "3 o'clock", "9 o'clock"], 0,
  "The posterior position (sacral hollow) is 6 o'clock. (Book p234)")

S6 = "Endoscopic Visualization of the Anorectum"
q(234, S6, "The approximate length of an anoscope is:",
  ["10 cm", "13 cm", "25 cm", "60 cm"], 0,
  "Anoscope: ~10 cm. (Book p234)")
q(234, S6, "The approximate length of a proctoscope is:",
  ["13 cm", "10 cm", "60 cm", "140 cm"], 0,
  "Proctoscope: ~13 cm. (Book p234)")
q(234, S6, "The length of a colonoscope as quoted in this chapter is:",
  ["110-140 cm", "10-13 cm", "60-70 cm", "200-250 cm"], 0,
  "Colonoscope: length 110-140 cm. (Book p234)")
q(234, S6, "The instrument that is visualised from the anal canal till the caecum is the:",
  ["Colonoscope", "Anoscope", "Proctoscope", "Sigmoidoscope"], 0,
  "The colonoscope is described as visualising from the anal canal till the caecum. (Book p234)")
q(234, S6, "The 60 cm instrument listed under visualization is taken up to the:",
  ["Sigmoid colon", "Caecum", "Terminal ileum", "Anal canal only"], 0,
  "The 60 cm instrument (sigmoidoscope) is visualised until the sigmoid colon. (Book p234)")
q(234, S6, "Arrange the instruments in increasing order of the length of bowel they can inspect:",
  ["Anoscope < proctoscope < sigmoidoscope < colonoscope",
   "Proctoscope < anoscope < sigmoidoscope < colonoscope",
   "Colonoscope < sigmoidoscope < proctoscope < anoscope",
   "Sigmoidoscope < anoscope < proctoscope < colonoscope"], 0,
  "Anoscope ~10 cm, proctoscope ~13 cm, sigmoidoscope ~60 cm (till sigmoid colon), colonoscope 110-140 cm (till caecum). (Book p234)")

# ------------------------------------------------------------------ p235
S7 = "Haemorrhoids: Pathology and Clinical Features"
q(235, S7, "Haemorrhoids are:",
  ["Dilated vascular channels", "Dilated lymphatics", "Hypertrophied anal papillae", "Herniations of rectal muscle"], 0,
  "Haemorrhoids are dilated vascular channels. (Book p235)")
q(235, S7, "The bleeding in haemorrhoids is:",
  ["Arterial", "Venous", "Capillary oozing only", "Mixed venous and lymphatic"], 0,
  "The chapter emphasises that haemorrhoidal bleeding is arterial. (Book p235)")
q(235, S7, "The most common cause of bleeding per rectum is:",
  ["Haemorrhoids", "Carcinoma rectum", "Anal fissure", "Ulcerative colitis"], 0,
  "Haemorrhoids are stated to be the most common (m/c) cause of bleeding per rectum. (Book p235)")
q(235, S7, "Bleeding per rectum in haemorrhoids is usually:",
  ["Painless", "Severely painful", "Associated with tenesmus", "Associated with mucus only"], 0,
  "Bleeding P/R is painless (usually). (Book p235)")
q(235, S7, "Painful bleeding per rectum is seen with all EXCEPT:",
  ["Uncomplicated first degree internal haemorrhoids", "External haemorrhoids (below the dentate line)",
   "Thrombosed haemorrhoids", "Anal fissure"], 0,
  "Painful bleeding is seen with external haemorrhoids (because of their location below the dentate line) and with thrombosed haemorrhoids; uncomplicated internal haemorrhoids above the dentate line bleed painlessly. (Book p235)")
q(235, S7, "External haemorrhoids are painful because they lie:",
  ["Below the dentate line", "Above the dentate line", "Within the rectal ampulla", "Intersphincterically"], 0,
  "External haemorrhoids lie below the dentate line, where pain sensation is present. (Book p235)")
q(235, S7, "Which associated symptom is listed under the clinical features of haemorrhoids?",
  ["Constipation", "Jaundice", "Haematuria", "Dysphagia"], 0,
  "Constipation is listed as a clinical feature/association of haemorrhoids. (Book p235)")
q(235, S7, "The investigation of choice for haemorrhoids is:",
  ["Proctoscopy", "Barium enema", "Colonoscopy", "MRI pelvis"], 0,
  "Investigation of choice: proctoscopy (haemorrhoids are visualised by the proctoscope). (Book p235)")

S8 = "Thrombosed Piles"
q(235, S8, "A thrombosed pile is described in this chapter as:",
  ["A 5 day self healing lesion", "A life-long lesion needing immediate surgery",
   "A premalignant condition", "A complication of Crohn's disease"], 0,
  "Thrombosed piles are described as a 5 day self healing lesion. (Book p235)")
q(235, S8, "Which statement about palpation in anorectal disease is correct?",
  ["Thrombosed piles are palpable on DRE but haemorrhoids are not",
   "Both haemorrhoids and thrombosed piles are always palpable",
   "Neither is ever palpable", "Only internal haemorrhoids are palpable"], 0,
  "DRE: thrombosed piles are palpable, whereas haemorrhoids are not palpable. (Book p235)")
q(235, S8, "A thrombosed pile presents as:",
  ["A mass felt on DRE", "A painless swelling that is never felt", "A fungating growth", "A fluid thrill"], 0,
  "The chapter lists a mass felt on DRE in thrombosed piles. (Book p235)")
q(235, S8, "Emergency surgery for a thrombosed pile offers:",
  ["Excision or evacuation of the clot", "Immediate abdominoperineal resection",
   "Only antibiotics", "Only sclerotherapy"], 0,
  "Emergency surgery is either excision or evacuation of the clot. (Book p235)")
q(235, S8, "Conservative treatment of a thrombosed pile is followed by definitive surgery after:",
  ["A few days to weeks", "6 months", "2 years", "24 hours"], 0,
  "Conservative management lets the lesion heal (about 5 days) and definitive surgery is done after a few days to weeks. (Book p235)")
q(235, S8, "Which intervention is the investigation of choice in thrombosed piles?",
  ["Proctoscopy", "Colonoscopy", "MR fistulogram", "Barium enema"], 0,
  "Investigation of choice: proctoscopy. (Book p235)")

S9 = "Grading of Haemorrhoids"
q(235, S9, "Grade I haemorrhoids:",
  ["Only bleed and do not prolapse", "Prolapse and reduce spontaneously",
   "Prolapse and need manual reduction", "Remain permanently prolapsed"], 0,
  "Grade I: only bleed, do not prolapse. (Book p235)")
q(235, S9, "Grade II haemorrhoids:",
  ["Prolapse and reduce spontaneously", "Only bleed",
   "Need manual reduction", "Remain prolapsed"], 0,
  "Grade II: prolapse, spontaneously reduced. (Book p235)")
q(235, S9, "Grade III haemorrhoids:",
  ["Prolapse and are manually reduced", "Only bleed",
   "Reduce spontaneously", "Are permanently prolapsed and irreducible"], 0,
  "Grade III: prolapse, manually reduced. (Book p235)")
q(235, S9, "Grade IV haemorrhoids:",
  ["Remain prolapsed", "Only bleed", "Reduce spontaneously", "Reduce with manual pressure only"], 0,
  "Grade IV: remain prolapsed. (Book p235)")
q(235, S9, "A patient who has to push a bleeding prolapsing mass back with his finger after every motion has:",
  ["Grade III haemorrhoids", "Grade I haemorrhoids", "Grade II haemorrhoids", "Grade IV haemorrhoids"], 0,
  "Prolapse needing manual reduction is grade III. (Book p235)")

# ------------------------------------------------------------------ p236
S10 = "Conservative and Office Management of Haemorrhoids"
q(236, S10, "Conservative management of grade I haemorrhoids includes all of the following EXCEPT:",
  ["Emergency haemorrhoidectomy", "Laxatives", "Sitz bath with lukewarm water", "Life style modification"], 0,
  "Grade I is managed conservatively — laxatives, sitz bath and life style changes; surgery belongs to the higher grades. (Book p236)")
q(236, S10, "A sitz bath helps because:",
  ["Lukewarm water relaxes the sphincter", "Hot water scleroses the vessels",
   "Cold water thromboses the pile", "It sterilises the anal canal"], 0,
  "Sitz bath: lukewarm water relaxes the sphincter. (Book p236)")
q(236, S10, "Management of grade II haemorrhoids is:",
  ["Management of grade I plus an office procedure", "Immediate haemorrhoidectomy",
   "Only observation", "Seton insertion"], 0,
  "Grade II is managed as grade I plus an office procedure (banding / sclerotherapy). (Book p236)")
q(236, S10, "Rubber band ligation works by:",
  ["Cutting off the blood supply so the haemorrhoid sloughs off",
   "Injecting a sclerosant into the pile",
   "Stapling the mucosa back into position",
   "Ligating the hemorrhoidal artery under Doppler guidance"], 0,
  "Banding cuts off the blood supply and the haemorrhoid sloughs off spontaneously. (Book p236)")
q(236, S10, "Rubber band ligation must be applied:",
  ["Above the dentate line", "Below the dentate line", "At the anal verge", "Within the intersphincteric plane"], 0,
  "Banding is done above the dentate line, which is painless. (Book p236)")
q(236, S10, "Sclerotherapy injects the sclerosant:",
  ["Above the dentate line", "Below the dentate line", "Into the external sphincter", "Into the ischiorectal fossa"], 0,
  "Application of sclerosing agents is above the dentate line. (Book p236)")
q(236, S10, "The effect of sclerotherapy on the pile is to:",
  ["Pull the haemorrhoids up so that they slough off", "Thrombose them immediately",
   "Divide the sphincter", "Create a fibrous ring at the anorectal ring"], 0,
  "Sclerotherapy pulls the haemorrhoids up and they slough off. (Book p236)")
q(236, S10, "The most commonly used sclerosing agent for haemorrhoids is:",
  ["Sodium tetradecyl sulfate", "Polidocanol", "Phenol in almond oil", "Sodium morrhuate"], 0,
  "Sodium tetradecyl sulfate is listed as the most common (m/c) sclerosing agent. (Book p236)")
q(236, S10, "Which of the following is NOT listed as a sclerosing agent for piles?",
  ["Ethanolamine oleate", "Sodium morrhuate", "Polidocanol", "Phenol in almond oil"], 0,
  "The listed agents are sodium tetradecyl sulfate, sodium morrhuate, polidocanol and phenol in almond oil. (Book p236)")
q(236, S10, "Deep sclerotherapy can cause all of the following EXCEPT:",
  ["Retrograde ejaculation", "Pain", "Infection", "Prostatitis (when done anteriorly)"], 0,
  "Deep sclerotherapy causes pain, infection and prostatitis when done anteriorly; retrograde ejaculation is listed as a complication of rectal prolapse surgery. (Book p236)")
q(236, S10, "Prostatitis after sclerotherapy is due to injection:",
  ["Anteriorly", "Posteriorly", "At 6 o'clock", "Into the rectum above the peritoneal reflection"], 0,
  "Anterior injection of sclerosant can produce prostatitis. (Book p236)")

S11 = "Operative Management of Haemorrhoids"
q(236, S11, "Grade III haemorrhoids are treated by:",
  ["Management of grade II ± surgery", "Surgery alone in every case",
   "Only sitz baths", "Abdominoperineal resection"], 0,
  "Grade III: management of grade II ± surgery. (Book p236)")
q(236, S11, "Grade IV haemorrhoids are treated by:",
  ["Surgery", "Banding alone", "Laxatives alone", "Sclerotherapy alone"], 0,
  "Grade IV: surgery. (Book p236)")
q(236, S11, "The Milligan-Morgan operation is the:",
  ["Open haemorrhoidectomy", "Closed haemorrhoidectomy", "Stapled haemorrhoidopexy", "Doppler guided artery ligation"], 0,
  "Open haemorrhoidectomy is the Milligan-Morgan operation. (Book p236)")
q(236, S11, "The Ferguson operation is the:",
  ["Closed haemorrhoidectomy", "Open haemorrhoidectomy", "Stapled haemorrhoidopexy", "Lateral sphincterotomy"], 0,
  "Closed haemorrhoidectomy is the Ferguson operation. (Book p236)")
q(236, S11, "The surgery of choice for haemorrhoids according to this chapter is:",
  ["Stapled haemorrhoidopexy", "Open haemorrhoidectomy",
   "Closed haemorrhoidectomy", "Injection sclerotherapy"], 0,
  "Stapled haemorrhoidopexy is stated to be the surgery of choice. (Book p236)")
q(236, S11, "DGHAL expands to:",
  ["Doppler guided haemorrhoidal artery ligation", "Direct guided haemorrhoidal ablation ligation",
   "Distal haemorrhoidal artery ligation", "Doppler guided hemorrhoidopexy and ligation"], 0,
  "DGHAL = Doppler guided haemorrhoidal artery ligation. (Book p236)")
q(236, S11, "Which of the following is a non-excisional, Doppler guided day-care option for piles?",
  ["DGHAL", "Milligan-Morgan haemorrhoidectomy", "Ferguson haemorrhoidectomy", "Fistulectomy"], 0,
  "Doppler guided haemorrhoidal artery ligation (DGHAL) is listed among the surgical options and does not excise tissue. (Book p236)")

# ------------------------------------------------------------------ p237
S12 = "Complications of Haemorrhoids and Their Surgery"
q(237, S12, "Reactionary haemorrhage after piles surgery is bleeding that occurs:",
  ["Within 24 hours of surgery", "After 7 days", "Only during defecation", "Only after discharge"], 0,
  "Reactionary haemorrhage is listed as a complication (bleeding in the immediate post-operative period, within 24 hours). (Book p237)")
q(237, S12, "Incontinence after piles surgery is due to:",
  ["Injury to the sphincter", "Injury to the mucosa", "Division of the dentate line", "Ligation of the hemorrhoidal artery"], 0,
  "Incontinence is caused by injury to the sphincter. (Book p237)")
q(237, S12, "Which of the following is listed as a complication of the surgery for piles?",
  ["Recurrence", "Portal pyaemia", "Ulceration", "Fibrosis"], 0,
  "Complications listed under surgery are reactionary haemorrhage, incontinence (sphincter injury) and recurrence. (Book p237)")
q(237, S12, "Which of the following is a complication of haemorrhoids themselves and not of their surgery?",
  ["Portal pyaemia", "Reactionary haemorrhage", "Incontinence from sphincter injury", "Recurrence after excision"], 0,
  "Complications of haemorrhoids are thrombosis, gangrene, fibrosis, portal pyaemia and ulceration. (Book p237)")
q(237, S12, "All of the following are complications of haemorrhoids EXCEPT:",
  ["Retrograde ejaculation", "Thrombosis", "Gangrene", "Ulceration"], 0,
  "Thrombosis, gangrene, fibrosis, portal pyaemia and ulceration are complications of haemorrhoids. (Book p237)")

S13 = "Anal Fissure: Pathology and Diagnosis"
q(237, S13, "An anal fissure is:",
  ["A breach in the continuity of the anal epithelium", "A dilated vascular channel",
   "A communication between two epithelial surfaces", "A prolapse of rectal mucosa"], 0,
  "Anal fissure is a breach in the continuity of the anal epithelium. (Book p237)")
q(237, S13, "An anal fissure lies:",
  ["Below the dentate line", "Above the dentate line", "At the anorectal ring", "In the rectum"], 0,
  "The fissure lies below the dentate line. (Book p237)")
q(237, S13, "The most common site of an anal fissure is:",
  ["6 o'clock (posterior midline)", "3 o'clock", "9 o'clock", "12 o'clock"], 0,
  "The m/c position is 6 o'clock, i.e. the posterior midline. (Book p237)")
q(237, S13, "An anal fissure at 12 o'clock in a woman is classically associated with:",
  ["Obstructed labour", "Crohn's disease", "Tuberculosis", "Previous haemorrhoidectomy"], 0,
  "A 12 o'clock (anterior) fissure is seen in obstructed labour. (Book p237)")
q(237, S13, "Which two symptoms are listed as the clinical features of an anal fissure?",
  ["Bleeding per rectum and constipation", "Bleeding per rectum and jaundice",
   "Constipation and haematuria", "Discharge and prolapse"], 0,
  "Clinical features: bleeding P/R and constipation. (Book p237)")
q(237, S13, "The classical triad seen in chronic anal fissure comprises the fissure, a hypertrophic papilla and:",
  ["A skin tag (sentinel pile)", "A perianal abscess", "An external opening", "A haemorrhoidal cushion"], 0,
  "The diagram shows the triad of skin tag, fissure and hypertrophic papilla. (Book p237)")
q(237, S13, "The investigation of choice for an anal fissure is:",
  ["External inspection", "DRE", "Proctoscopy", "Colonoscopy"], 0,
  "External inspection is the investigation of choice (IOC); DRE is contraindicated. (Book p237)")
q(237, S13, "The sentinel pile is another name for the:",
  ["Skin tag of a chronic fissure", "Hypertrophic anal papilla", "Thrombosed external pile", "Perianal haematoma"], 0,
  "Skin tag is AKA sentinel pile and is seen in chronic fissure. (Book p237)")
q(237, S13, "The skin tag of a fissure is formed by:",
  ["Accumulation of lymphatics", "Prolapsed mucosa", "Thrombosed vessels", "Granulation tissue only"], 0,
  "The sentinel pile results from accumulation of lymphatics. (Book p237)")
q(237, S13, "A 30-year-old man has severe cutting pain during defecation and a drop of blood on the stool. On examination the doctor avoids doing a DRE because:",
  ["It is contraindicated in a painful fissure", "It may cause a perforation",
   "It can convert the fissure into a fistula", "It precipitates gangrene"], 0,
  "DRE is contraindicated in fissure — diagnosis is by gentle external inspection. (Book p237)")

S14 = "Medical Management of Anal Fissure"
q(237, S14, "Dietary advice in anal fissure includes all of the following EXCEPT:",
  ["A low residue diet", "High fibre diet", "Increased liquid intake", "Avoiding fried and fatty food"], 0,
  "Life style changes recommended are a high fibre diet, increased liquid intake and avoiding fried/fatty food. (Book p237)")
q(237, S14, "The local anaesthetic jelly used before and after defecation in anal fissure is:",
  ["2% xylocaine jelly", "0.5% xylocaine jelly", "5% lidocaine patch", "2% prilocaine cream"], 0,
  "2% xylocaine jelly is applied before and after defecation. (Book p237)")
q(237, S14, "Diltiazem cream is used in anal fissure because it:",
  ["Relaxes the sphincter", "Acts as a local anaesthetic", "Is an antibiotic", "Hardens the stool"], 0,
  "Diltiazem cream is listed as relaxing the sphincter — it is a calcium channel blocker used as a chemical sphincterotomy. (Book p237)")
q(237, S14, "Topical nitrate gel for anal fissure is associated with which side effect?",
  ["Headache", "Bradycardia", "Hypoglycaemia", "Bladder dysfunction"], 0,
  "The side effects listed for nitrate gel are headache and hypertension. (Book p237)")
q(237, S14, "Which of the following is a sphincter-relaxing measure used in fissure-in-ano?",
  ["Both diltiazem cream and nitrate gel", "Only xylocaine jelly", "Only laxatives", "Only a high fibre diet"], 0,
  "Diltiazem cream (relaxes the sphincter) and nitrate gel are the pharmacological sphincter relaxants; xylocaine gives analgesia. (Book p237)")

# ------------------------------------------------------------------ p238
S15 = "Surgical Management of Anal Fissure"
q(238, S15, "The standard operation for chronic anal fissure is:",
  ["Lateral anal sphincterotomy", "Fissurectomy alone", "Anal advancement flap", "Stapled haemorrhoidopexy"], 0,
  "Lateral anal sphincterotomy is the first surgical option listed. (Book p238)")
q(238, S15, "In lateral anal sphincterotomy the structure divided is the:",
  ["Internal sphincter", "External sphincter", "Puborectalis", "Anococcygeal ligament"], 0,
  "The internal sphincter is cut. (Book p238)")
q(238, S15, "Division of the internal sphincter heals a fissure because:",
  ["The sphincter relaxes and the fissure heals", "It excises the fissure",
   "It denervates the anal canal", "It drains the intersphincteric abscess"], 0,
  "Cutting the internal sphincter relaxes the sphincter and the fissure heals. (Book p238)")
q(238, S15, "The second surgical option listed for anal fissure is:",
  ["An anal advancement flap", "A seton", "A Karydakis flap", "A Delorme repair"], 0,
  "The second option is an anal advancement flap. (Book p238)")

S16 = "Pilonidal Sinus"
q(238, S16, "Pilonidal sinus is also called:",
  ["Jeep driver's disease", "Carpenter's disease", "Baker's cyst", "Barber's disease"], 0,
  "Pilonidal sinus is called jeep driver's disease. (Book p238)")
q(238, S16, "The most common site of a pilonidal sinus is the:",
  ["Natal cleft", "Interdigital web", "Face", "Umbilicus"], 0,
  "The natal cleft is the m/c site. (Book p238)")
q(238, S16, "Pilonidal sinus in the interdigital area is classically seen in:",
  ["Barbers", "Jeep drivers", "Carpenters", "Radiologists"], 0,
  "The interdigital area is affected in barbers (hair in the web space). (Book p238)")
q(238, S16, "Which site of pilonidal sinus is mentioned in addition to the natal cleft and the interdigital area?",
  ["Face", "Scalp", "Axilla", "Groin"], 0,
  "The sites listed are natal cleft (m/c), interdigital area (barbers) and the face. (Book p238)")
q(238, S16, "Pilonidal sinus characteristically occurs in:",
  ["Hairy men", "Prepubertal girls", "Elderly women", "Neonates"], 0,
  "It is a disease of hairy men. (Book p238)")
q(238, S16, "The pathogenesis of pilonidal sinus is:",
  ["Friction → inward growth of hair → abscess → sinus",
   "Infection of an apocrine gland → abscess → sinus",
   "Congenital epithelial rests → abscess → sinus",
   "Ischaemic necrosis of the natal cleft skin"], 0,
  "Friction causes inward growth of hair, which produces an abscess and then a sinus. (Book p238)")
q(238, S16, "The clinical features of pilonidal sinus listed are:",
  ["Swelling and discharge", "Prolapse and bleeding", "Incontinence and tenesmus", "Pain and jaundice"], 0,
  "Clinical features: swelling and discharge. (Book p238)")
q(238, S16, "Incision and drainage of a pilonidal abscess must be accompanied by:",
  ["Removal of the hair to prevent recurrence", "Excision of the coccyx",
   "Insertion of a seton", "Sclerotherapy of the track"], 0,
  "Drain the abscess and remove the hair — done to prevent recurrence. (Book p238)")
q(238, S16, "Conservative measures listed for pilonidal sinus are:",
  ["Antibiotics and analgesics", "Antibiotics and steroids", "Radiotherapy and chemotherapy", "Sclerotherapy alone"], 0,
  "Antibiotics and analgesics are the conservative measures listed. (Book p238)")
q(238, S16, "Which flap repair is listed for pilonidal sinus?",
  ["Rhomboid (Limberg) flap", "Deltopectoral flap", "Free radial artery flap", "Rotation flap of the scalp"], 0,
  "The Rhomboid/Limberg flap is the first surgical option listed. (Book p238)")
q(238, S16, "Which of the following is NOT listed as a surgical option for pilonidal sinus?",
  ["Delorme's repair", "Rhomboid (Limberg) flap", "Bascom's technique", "Karydakis technique"], 0,
  "The surgical options listed are the Rhomboid/Limberg flap, Bascom's technique and the Karydakis technique; Delorme's repair is a procedure for rectal prolapse. (Book p238)")
q(238, S16, "Bascom's technique for pilonidal sinus uses:",
  ["An incision lateral to the midline with the sinus cleared and sutured",
   "A rhomboid transposition flap",
   "A midline excision left open",
   "A mesh placed over the natal cleft"], 0,
  "Bascom's technique is illustrated as an incision lateral to the midline, the sinus cleared and then sutured. (Book p238)")

# ------------------------------------------------------------------ p239
S17 = "Anorectal Abscess"
q(239, S17, "All of the following are clinical features of an anorectal abscess EXCEPT:",
  ["Fluctuation as an early sign", "Fever", "Swelling", "Pain"], 0,
  "Fever and swelling are listed, and fluctuation is specifically described as a LATE sign. (Book p239)")
q(239, S17, "Fluctuation is a late sign in all of the following EXCEPT:",
  ["Perianal haematoma", "Parotid abscess", "Breast abscess", "Palmar and plantar abscess"], 0,
  "The page lists fluctuation as a late sign in parotid abscess, breast abscess and palmar/plantar abscess. (Book p239)")
q(239, S17, "Which of the following is NOT one of the anorectal abscess types illustrated on this page?",
  ["Suprasphincteric", "Perianal", "Intersphincteric", "Ischiorectal"], 0,
  "The four types illustrated are perianal, intersphincteric, ischiorectal and supralevator — not suprasphincteric (which is a fistula type). (Book p239)")
q(239, S17, "The most superficial of the anorectal abscesses is the:",
  ["Perianal abscess", "Ischiorectal abscess", "Supralevator abscess", "Intersphincteric abscess"], 0,
  "The perianal abscess is the most superficial, lying just under the perianal skin. (Book p239)")
q(239, S17, "The abscess that lies above the levator ani in the diagram is the:",
  ["Supralevator abscess", "Perianal abscess", "Intersphincteric abscess", "Ischiorectal abscess"], 0,
  "The supralevator abscess is drawn above the levator ani. (Book p239)")
q(239, S17, "The intersphincteric abscess lies between the:",
  ["Internal and external sphincters", "Levator ani and the pelvic peritoneum",
   "Rectum and the sacrum", "Anal skin and the external sphincter"], 0,
  "As the name implies, the intersphincteric abscess lies in the plane between the internal and external anal sphincters. (Book p239)")
q(239, S17, "The treatment of an anorectal abscess is:",
  ["Incision and drainage", "Antibiotics alone", "Excision of the rectum", "Observation"], 0,
  "Management is incision and drainage. (Book p239)")
q(239, S17, "A poorly drained anorectal abscess is likely to result in:",
  ["A perianal sinus or fistula", "A supralevator extension", "A rectovaginal fistula", "Faecal incontinence"], 0,
  "The page states that a poorly drained abscess becomes a perianal sinus/fistula. (Book p239)")

S18 = "Fistula-in-Ano and Goodsall's Rule"
q(239, S18, "A perianal sinus/fistula is most often:",
  ["Secondary to anal sepsis", "Congenital in origin", "Due to tuberculosis in most cases", "A complication of haemorrhoids"], 0,
  "Perianal sinus/fistula is secondary to anal sepsis. (Book p239)")
q(239, S18, "The term 'water-can perineum' refers to:",
  ["Multiple external openings of a fistula", "A large ischiorectal abscess",
   "A prolapsing haemorrhoid", "A pilonidal sinus with discharge"], 0,
  "Water-can perineum is used when there are multiple external openings. (Book p239)")
q(239, S18, "The openings of a fistula-in-ano are described as:",
  ["One internal and one or more external openings", "Two internal openings",
   "Only external openings", "Only internal openings"], 0,
  "A fistula has an internal opening (in the anal canal) and one or more external openings. (Book p239)")
q(239, S18, "The mnemonic 'Krohn, krush, Kancer, Koch's' is used for the causes of:",
  ["Fistula-in-ano", "Anal fissure", "Pilonidal sinus", "Rectal prolapse"], 0,
  "The mnemonic lists the causes of fistula-in-ano: Crohn's, trauma (crush), cancer, Koch's (tuberculosis) and immunocompromise. (Book p239)")
q(239, S18, "Which of the following is listed as a cause of fistula-in-ano?",
  ["Crohn's disease", "Ulcerative colitis", "Diverticulosis", "Coeliac disease"], 0,
  "Crohn's disease, cancer and immunocompromised states are listed. (Book p239)")
q(239, S18, "Which of the following is a typical symptom of a perianal fistula?",
  ["Staining of the undergarment with pus", "Painless large bowel bleeding",
   "Profuse watery diarrhoea", "Haematuria"], 0,
  "Staining of the undergarment with pus and itching are the listed clinical features. (Book p239)")
q(239, S18, "On examination of a patient with a perianal fistula the key finding is:",
  ["An external opening on inspection", "A mass felt on DRE", "Absent anal sensation", "A bluish perianal swelling"], 0,
  "O/E: an external opening is seen on inspection. (Book p239)")
q(239, S18, "According to Goodsall's rule, a fistula with its external opening in the anterior half of the anal circumference usually has:",
  ["A straight radial tract", "A long curved tract opening in the midline posteriorly",
   "A horseshoe tract", "No internal opening"], 0,
  "Anterior fistulae run in straight, radial tracts to the internal opening. (Book p239)")
q(239, S18, "According to Goodsall's rule, a fistula opening posteriorly has:",
  ["A curved tract that opens in the midline", "A straight radial tract",
   "No internal opening", "A tract that always crosses the midline anteriorly"], 0,
  "Posterior fistulae have curved tracts that open in the midline (posteriorly). (Book p239)")
q(239, S18, "The exception to Goodsall's rule is:",
  ["A long anterior fistula (>3 cm) which behaves like a posterior fistula",
   "A short posterior fistula", "Any fistula in a female", "Any fistula secondary to Crohn's disease"], 0,
  "A long anterior fistula (>3 cm) is the exception — it curves back and opens in the midline at the 12 o'clock position. (Book p239)")
q(239, S18, "A horseshoe fistula is characteristically associated with which type of fistula?",
  ["Posterior", "Anterior", "Lateral", "Anterior long"], 0,
  "The page mentions a horse shoe fistula occurring with a posterior fistula. (Book p239)")

# ------------------------------------------------------------------ p240
S19 = "Investigations and Classification of Fistula-in-Ano"
q(240, S19, "The investigation of choice for fistula-in-ano is:",
  ["MR fistulogram", "Plain X-ray abdomen", "Barium enema", "Proctoscopy"], 0,
  "MR fistulogram is the investigation of choice (IOC). (Book p240)")
q(240, S19, "Park's classification of fistula-in-ano is based on:",
  ["MR fistulogram", "The external opening alone", "Goodsall's rule", "The number of setons used"], 0,
  "Park's classification is based on the MR fistulogram — i.e. the relation of the tract to the sphincters. (Book p240)")
q(240, S19, "The most common type of fistula-in-ano in Park's classification is:",
  ["Transsphincteric", "Intersphincteric", "Suprasphincteric", "Extrasphincteric"], 0,
  "Transsphincteric fistula is the most common (m/c). (Book p240)")
q(240, S19, "Which of the following is NOT one of Park's four types of fistula?",
  ["Supralevator", "Intersphincteric", "Transsphincteric", "Extrasphincteric"], 0,
  "Park's types are intersphincteric, transsphincteric, suprasphincteric and extrasphincteric; supralevator is an abscess type. (Book p240)")
q(240, S19, "The suprasphincteric fistula passes:",
  ["Over the top of the external sphincter (above the anorectal ring level of the sphincter complex)",
   "Through the intersphincteric plane only",
   "Outside both sphincters without relation to them",
   "Through the internal sphincter only"], 0,
  "Suprasphincteric means the tract passes above the sphincter complex before descending. (Book p240)")
q(240, S19, "The extrasphincteric fistula is one that:",
  ["Passes outside the sphincter complex from the rectum to the perianal skin",
   "Lies only in the intersphincteric plane",
   "Is confined to the submucosa",
   "Is always iatrogenic"], 0,
  "Extrasphincteric fistulae run outside the external sphincter, from the rectum to the perianal skin. (Book p240)")
q(240, S19, "The landmark used to classify a fistula as high or low, based on its internal opening, is the:",
  ["Anorectal ring", "Dentate line", "Anal verge", "Pectinate line"], 0,
  "The landmark is the anorectal ring: above it the fistula is high, below it low. (Book p240)")
q(240, S19, "A fistula whose internal opening lies above the anorectal ring is called a:",
  ["High fistula", "Low fistula", "Submucosal fistula", "Simple fistula"], 0,
  "Above the anorectal ring = high fistula. (Book p240)")
q(240, S19, "Which of the following is NOT one of the four principles of fistula surgery listed?",
  ["Routine faecal diversion in every case", "Eliminate all septic foci",
   "Delineate the anatomy of the epithelialised tracts", "Preserve continence and prevent recurrence"], 0,
  "The principles are: eliminate all septic foci, delineate the anatomy of the epithelialised tracts, preserve continence and prevent recurrence. (Book p240)")

S20 = "Operations for Fistula-in-Ano"
q(240, S20, "Fistulectomy involves:",
  ["Removal of the entire tract", "Opening the tract and curetting granulation tissue",
   "Insertion of a seton", "Division of the internal sphincter"], 0,
  "Fistulectomy is removal of the entire tract. (Book p240)")
q(240, S20, "Fistulotomy is described as:",
  ["Opening the tract and removing granulation tissue", "Removing the entire tract",
   "Excision of the internal opening alone", "Laying open the rectum"], 0,
  "Fistulotomy: the tract is opened and granulation tissue removed. (Book p240)")
q(240, S20, "An advantage of fistulectomy mentioned in the chapter is that it is:",
  ["Cost effective", "Free of any risk to continence", "Suitable for every high fistula", "Done without anaesthesia"], 0,
  "Fistulectomy is described as cost effective. (Book p240)")
q(240, S20, "Fistulectomy is avoided in a high fistula because:",
  ["It damages the sphincter and causes incontinence",
   "It is technically impossible",
   "It always leaves the internal open",
   "It requires a laparotomy"], 0,
  "Fistulectomy in a high fistula damages the sphincter and causes incontinence — hence it is avoided. (Book p240)")

# ------------------------------------------------------------------ p241
S21 = "Seton Treatment of High Fistula"
q(241, S21, "The treatment of choice for a high fistula described here is:",
  ["Seton treatment", "Fistulectomy", "Immediate abdominoperineal resection", "Injection sclerotherapy"], 0,
  "High fistula is managed by seton treatment. (Book p241)")
q(241, S21, "A seton is:",
  ["A thread inserted into the fistula and tightened at intervals",
   "A rubber band applied above the dentate line",
   "A mesh placed in the ischiorectal fossa",
   "A sclerosant injected into the tract"], 0,
  "A thread is inserted into the fistula and tightened over frequent intervals. (Book p241)")
q(241, S21, "The advantage of a cutting seton is:",
  ["Gradual cutting of the tract with less chance of incontinence",
   "Immediate cure in one sitting",
   "No need for any further surgery",
   "It prevents abscess formation permanently"], 0,
  "Gradual cutting of the tract gives less chance of incontinence because fibrosis holds the sphincter as it divides. (Book p241)")
q(241, S21, "The two types of seton are:",
  ["Draining seton and cutting seton", "Absorbable and non-absorbable seton",
   "Silk and catgut seton", "High and low seton"], 0,
  "Types: draining seton and cutting seton. (Book p241)")
q(241, S21, "A draining seton is preferred in:",
  ["Crohn's disease", "High fistula", "A low intersphincteric fistula", "A pilonidal sinus"], 0,
  "A draining seton is used in Crohn's disease (to keep sepsis draining without dividing the sphincter); a cutting seton is used for a high fistula. (Book p241)")
q(241, S21, "The material used for a seton is:",
  ["Prolene suture", "Catgut", "Silkworm gut", "Nylon tape"], 0,
  "Material: prolene suture. (Book p241)")

S22 = "Rectal Prolapse: Partial versus Complete"
q(241, S22, "In partial (mucosal) rectal prolapse the layer prolapsed is the:",
  ["Mucosa only", "All layers of the rectum", "Muscularis only", "Serosa only"], 0,
  "Partial prolapse is a mucosal prolapse; complete prolapse involves all layers. (Book p241)")
q(241, S22, "Partial rectal prolapse is typically seen in:",
  ["Children", "Adults", "Elderly nulliparous women", "Adolescents after trauma"], 0,
  "Partial prolapse is seen in children; complete prolapse in adults. (Book p241)")
q(241, S22, "Complete rectal prolapse is associated with:",
  ["A weak pelvic floor", "An incomplete sacral curve", "A hypertrophied internal sphincter", "Hirschsprung's disease"], 0,
  "Complete prolapse is associated with a weak pelvic floor; partial prolapse with an incomplete sacral curve. (Book p241)")
q(241, S22, "The first episode of a partial prolapse is treated by:",
  ["Digital reposition", "Immediate rectopexy", "Thiersch wiring", "Delorme's repair"], 0,
  "First episode: digital reposition. (Book p241)")
q(241, S22, "Recurrent partial prolapse in a child is treated by:",
  ["Thiersch wiring or sclerotherapy", "Immediate abdominoperineal resection",
   "Stapled haemorrhoidopexy", "Lateral sphincterotomy"], 0,
  "Recurrent cases are treated by Thiersch wiring or sclerotherapy. (Book p241)")
q(241, S22, "A 4-year-old child brings out a 3 cm mass after passing stool; the mucosa shows radial folds rather than the concentric rings of a full-thickness prolapse. This is:",
  ["Partial thickness prolapse", "Complete (full thickness) prolapse",
   "A prolapsed haemorrhoid", "A rectal polyp"], 0,
  "Partial thickness prolapse occurs in children and only mucosa prolapses; complete prolapse is full thickness. (Book p241)")

# ------------------------------------------------------------------ p242
S23 = "Surgery for Complete Rectal Prolapse"
q(242, S23, "Compared with perineal procedures, abdominal procedures for complete prolapse are:",
  ["More difficult with more operative complications",
   "Easier with fewer operative complications",
   "Associated with a higher recurrence rate",
   "Reserved for frail elderly patients"], 0,
  "Abdominal procedures are difficult and have more operative complications; perineal ones are easier with fewer complications. (Book p242)")
q(242, S23, "Recurrence after an abdominal procedure for prolapse is:",
  ["Much lower (recurrence ↓↓)", "Much higher (recurrence ↑↑)", "The same as after a perineal repair", "100%"], 0,
  "Abdominal procedures: recurrence ↓↓; perineal procedures: recurrence ↑↑. (Book p242)")
q(242, S23, "Perineal procedures for rectal prolapse are preferred in:",
  ["Frail, elderly patients with co-morbidity", "Young fit patients", "Children", "Pregnant women"], 0,
  "Perineal procedures are used in frail, elderly patients with co-morbidity; abdominal ones in young, fit patients. (Book p242)")
q(242, S23, "Which of the following is an abdominal procedure for complete prolapse?",
  ["Rectopexy", "Delorme's repair", "Thiersch wiring", "Altemeier repair"], 0,
  "Rectopexy (Well's / Ripstein / Frykman-Goldberg) is the abdominal procedure; Delorme, Thiersch and Altemeier are perineal. (Book p242)")
q(242, S23, "Rectopexy means:",
  ["Placing a mesh between the rectum and the sacrum", "Excision of the prolapsed mucosa",
   "Plication of the external sphincter", "Resection of the redundant sigmoid via the perineum"], 0,
  "Rectopexy: mesh placed between the rectum and the sacrum to prevent prolapse. (Book p242)")
q(242, S23, "Well's and Ripstein operations are examples of:",
  ["Rectopexy", "Perineal rectosigmoidectomy", "Thiersch wiring", "Sclerotherapy"], 0,
  "Well's and Ripstein are the named rectopexy operations listed. (Book p242)")
q(242, S23, "The Frykman-Goldberg operation is a:",
  ["Resection rectopexy", "Perineal rectosigmoidectomy", "Sphincteroplasty", "Stapled mucosal resection"], 0,
  "Frykman Goldberg is listed as a resection rectopexy. (Book p242)")
q(242, S23, "The Altemeier repair is also called:",
  ["Perineal rectosigmoidectomy", "Abdominal rectopexy", "Anterior resection", "Mucosal plication"], 0,
  "Altemeier repair = perineal rectosigmoidectomy. (Book p242)")
q(242, S23, "In the Altemeier (perineal rectosigmoidectomy) repair the redundant sigmoid is cut in order to:",
  ["Prevent recurrences", "Shorten the anaesthetic time", "Avoid a stoma", "Reduce blood loss"], 0,
  "The redundant sigmoid is cut and this is done to prevent recurrences. (Book p242)")
q(242, S23, "Thiersch wiring consists of:",
  ["Digital reduction of the prolapse followed by a purse-string suture (wire) around the anus",
   "Excision of the prolapsed mucosa",
   "Placement of a mesh between rectum and sacrum",
   "Plication of the levator ani"], 0,
  "The prolapse is reduced digitally and the anus is closed with a purse-string suture (wire). (Book p242)")
q(242, S23, "Delorme's repair consists of:",
  ["Plication of the mucosa and the prolapse", "Placement of a mesh in the sacrum",
   "Excision of the full thickness of the prolapse", "Division of the internal sphincter"], 0,
  "Delorme's repair: the mucosa and the prolapse are plicated. (Book p242)")

# ------------------------------------------------------------------ p243
S24 = "Complications of Prolapse Surgery"
q(243, S24, "The most common complication after surgery for rectal prolapse is:",
  ["Constipation", "Haemorrhage", "Faecal incontinence", "Small bowel obstruction"], 0,
  "Constipation is listed as the most common (m/c) complication. (Book p243)")
q(243, S24, "Which of the following is NOT listed as a complication of prolapse surgery?",
  ["Portal pyaemia", "Haemorrhage", "Recurrence", "Bladder dysfunction"], 0,
  "The complications listed are constipation (m/c), haemorrhage, recurrence, fistula (in females), bladder dysfunction and retrograde ejaculation. (Book p243)")
q(243, S24, "A rectovaginal fistula after prolapse surgery occurs due to:",
  ["Erosion into the vagina", "Injury to the ureter", "Division of the levator ani", "Mesh allergy"], 0,
  "Fistula in females is due to erosion into the vagina. (Book p243)")
q(243, S24, "Retrograde ejaculation after rectal prolapse surgery is due to injury to the:",
  ["Pelvic autonomic nerves", "Pudendal nerve", "External sphincter", "Inferior mesenteric artery"], 0,
  "Retrograde ejaculation is listed as a complication of pelvic dissection during prolapse surgery (autonomic nerve injury). (Book p243)")

S25 = "Solitary Rectal Ulcer Syndrome"
q(243, S25, "The ulcer of solitary rectal ulcer syndrome lies on the:",
  ["Anterior wall of the rectum", "Posterior wall of the rectum",
   "Lateral wall of the rectum", "Anal canal below the dentate line"], 0,
  "SRUS: ulcer in the anterior wall of the rectum. (Book p243)")
q(243, S25, "The ulcer of solitary rectal ulcer syndrome is located how far from the anal verge?",
  ["3-10 cm", "1-2 cm", "15-20 cm", "25-30 cm"], 0,
  "SRUS is located 3-10 cm from the anal verge. (Book p243)")
q(243, S25, "Solitary rectal ulcer syndrome is described as the starting point of:",
  ["Intussusception / prolapse", "A fistula-in-ano", "An anal fissure", "A malignant stricture"], 0,
  "The page says it is the starting point of intussusception/prolapse. (Book p243)")
q(243, S25, "The characteristic histopathology of solitary rectal ulcer syndrome is:",
  ["Fibromuscular obliteration of the lamina propria", "Caseating granulomas",
   "Transmural lymphoid aggregates", "Mucin-producing adenocarcinoma"], 0,
  "Fibromuscular obliteration of the lamina propria is the histological hallmark. (Book p243)")
q(243, S25, "Why is a biopsy mandatory in a rectal ulcer?",
  ["To rule out cancer", "To confirm Crohn's disease", "To grade a haemorrhoid", "To look for a fistula track"], 0,
  "Ulcer → biopsy → to rule out (r/o) cancer. (Book p243)")
q(243, S25, "STARR, used for solitary rectal ulcer syndrome, expands to:",
  ["Stapled transanal rectal resection", "Stapled transanal repair of rectum",
   "Subtotal transanal rectal reconstruction", "Suture transanal rectal repair"], 0,
  "STARR = stapled transanal rectal resection (of the intussusception). (Book p243)")

S26 = "Anorectal Malformation: Assessment"
q(243, S26, "An anorectal malformation is defined by:",
  ["Absence of a normal anal opening", "A stenosis of the rectum",
   "A duplicated anal canal", "An ectopic ureter"], 0,
  "Anorectal malformation: absence of a normal anal opening. (Book p243)")
q(243, S26, "VACTERL association includes all of the following EXCEPT:",
  ["Duodenal atresia", "Vertebral defects", "Tracheo-oesophageal fistula", "Renal anomalies"], 0,
  "VACTERL = vertebral, anorectal, cardiac, tracheo-oesophageal, renal and limb abnormalities. (Book p243)")
q(243, S26, "The letter 'C' in VACTERL stands for:",
  ["Cardiac abnormalities", "Cloacal anomaly", "Costal defects", "Caudal regression"], 0,
  "C = cardiac abnormalities. (Book p243)")
q(243, S26, "The best investigation to delineate the anatomy in an anorectal malformation is:",
  ["MRI", "Invertogram", "Plain X-ray abdomen", "Barium enema"], 0,
  "MRI is described as the best investigation to delineate the anatomy. (Book p243)")
q(243, S26, "An invertogram is performed after how many hours of birth?",
  ["24 hours", "2 hours", "6 hours", "72 hours"], 0,
  "It is done after 24 hours, by which time gas has reached the rectum. (Book p243)")
q(243, S26, "In an invertogram the metallic marker is placed:",
  ["At the proposed site of the anal opening", "Over the sacrum", "Over the symphysis pubis", "Inside the rectum"], 0,
  "A metallic coin is placed at the proposed site of the anal opening. (Book p243)")
q(243, S26, "The invertogram X-ray is taken with the baby:",
  ["In the inverted position", "Prone with hips extended", "Supine with legs flexed", "In the left lateral position"], 0,
  "The X-ray is taken in the inverted position. (Book p243)")
q(243, S26, "On an invertogram a distance of more than 2 cm between the coin and the gas shadow indicates:",
  ["A high anorectal malformation", "A low anorectal malformation",
   "A normal anus", "An associated fistula"], 0,
  "Distance >2 cm = high anorectal malformation; a short distance (<2 cm) = low anomaly. (Book p243)")

# ------------------------------------------------------------------ p244
S27 = "Anorectal Malformation: Classification and Management"
q(244, S27, "A male infant with an anorectal malformation classically passes faecal matter:",
  ["During urination", "Only through the vagina", "Only after 48 hours", "As ribbon-like stools"], 0,
  "In males: faecal matter passed during urination and recurrent UTI. (Book p244)")
q(244, S27, "Recurrent urinary tract infection in a male infant with an anorectal malformation suggests:",
  ["A rectourinary fistula", "A rectovaginal fistula", "An anal stenosis", "A ureterocele"], 0,
  "Rectourinary (rectovesical / rectourethral) fistulae present with faecal matter in urine and recurrent UTI. (Book p244)")
q(244, S27, "In females the anus in a low anomaly is:",
  ["Abnormally close to the vagina", "Absent with a bladder fistula", "Located in the perineal body", "Duplicated"], 0,
  "In females the anus is abnormally close to the vagina. (Book p244)")
q(244, S27, "Which of the following is a HIGH anomaly in males?",
  ["Rectovesical fistula", "Rectourethral fistula", "Anocutaneous fistula", "Anal stenosis"], 0,
  "High anomalies in males: anorectal agenesis and rectovesical fistula. (Book p244)")
q(244, S27, "Rectourethral fistula in a male is classified as:",
  ["An intermediate anomaly", "A high anomaly", "A low anomaly", "A miscellaneous anomaly"], 0,
  "Intermediate anomaly in males: rectourethral fistula. (Book p244)")
q(244, S27, "Rectovestibular fistula in a female is classified as:",
  ["An intermediate anomaly", "A high anomaly", "A low anomaly", "A miscellaneous anomaly"], 0,
  "Intermediate anomalies in females: rectovestibular fistula and rectovaginal fistula. (Book p244)")
q(244, S27, "Rectal atresia in a female is listed under:",
  ["High anomalies", "Intermediate anomalies", "Low anomalies", "Miscellaneous anomalies"], 0,
  "High anomalies in females: rectovaginal fistula and rectal atresia. (Book p244)")
q(244, S27, "Persistent cloacal anomaly is listed under:",
  ["Miscellaneous anomalies", "Low anomalies", "High anomalies", "Intermediate anomalies"], 0,
  "Miscellaneous (in females): anal stenosis and persistent cloacal anomaly. (Book p244)")
q(244, S27, "Management of a LOW anorectal malformation is:",
  ["Definitive surgery", "Initial diverting colostomy followed by definitive surgery",
   "Dilatation alone", "Observation till adulthood"], 0,
  "Low anomaly: definitive surgery. (Book p244)")
q(244, S27, "Management of a HIGH anorectal malformation is:",
  ["First a diverting colostomy, then definitive surgery",
   "Immediate definitive surgery in the neonatal period",
   "Serial dilatations only",
   "Permanent colostomy only"], 0,
  "High anomaly: 1st a diverting colostomy and 2nd definitive surgery. (Book p244)")
q(244, S27, "PSARP, the definitive surgery for anorectal malformation, expands to:",
  ["Posterior sagittal anorectoplasty", "Perineal sagittal anorectal pull-through",
   "Posterior sphincter-saving anoplasty", "Perineal sagittal ano-rectal plasty"], 0,
  "Definitive surgery: PSARP = posterior sagittal anorectoplasty. (Book p244)")

# ------------------------------------------------------------------ units
def sec_ids(*labels):
    return [x["id"] for x in Q if x["sec"] in labels]


def first_page(label):
    for x in Q:
        if x["sec"] == label:
            return x["page"]
    return 0


UNIT_DEFS = [
    (S1, "Start with the rectum itself: a 12-14 cm tube whose upper and lower parts bend to the right and its middle to the left, and whose lower part alone is bare of peritoneum. That last fact is the whole reason a low anterior resection is possible."),
    (S2, "The anal canal is a 4-5 cm gateway with three landmarks - anorectal ring, dentate line and anal verge. Everything the examiner does depends on whether a lesion sits above the dentate line (columnar, adenocarcinoma, painless) or below it (squamous, squamous carcinoma, painful)."),
    (S3, "Three tiny structures explain three common diseases: the columns of Morgagni (mucosal folds), the cryptoglandular communication that seeds abscesses, and the three vascular cushions of the distal anal submucosa that prolapse to become haemorrhoids at the classical left anterior, right anterior and right posterior positions."),
    (S4, "Continence is a nerve story. The internal sphincter runs on autonomic fibres (parasympathetic S2-S4, sympathetic L5), while the external sphincter is somatic via the pudendal nerve - and because it is paired, one side can be lost silently but both cannot."),
    (S5, "A good rectal examination is choreography, not force: consent, left lateral position, inspect first, then one finger. Know what the fingertip meets anteriorly in each sex and why a painful fissure stops you before you begin."),
    (S6, "Instruments only matter if you know how far they reach. Anoscope ~10 cm, proctoscope ~13 cm, a 60 cm instrument that stops at the sigmoid colon, and a 110-140 cm colonoscope that travels from the anal canal to the caecum."),
    (S7, "Haemorrhoids are dilated vascular channels that bleed arterially and are the commonest cause of bleeding per rectum. The bleed is painless unless the piles are external (below the dentate line) or thrombosed - that single distinction drives the whole history."),
    (S8, "A thrombosed pile is a 5 day self healing lesion that, unlike ordinary haemorrhoids, can actually be felt. Decide between clot evacuation/excision now, or settling it down and returning for definitive surgery a few days to weeks later."),
    (S9, "Grading is pure mechanics: I bleeds, II reduces itself, III needs a finger, IV stays out. Every management decision in the next units hangs off this four-step ladder."),
    (S10, "Office treatment is where most piles are cured. Banding strangulates the blood supply, sclerotherapy lifts and fixes the cushion, both are done above the painless dentate line - and both become dangerous if the sclerosant is injected too deep, especially anteriorly in a man."),
    (S11, "When the pile is grade III or IV the answer is an operation. Match the eponyms to the technique - Milligan-Morgan open, Ferguson closed - and remember that stapled haemorrhoidopexy is named as the surgery of choice, with DGHAL as the Doppler-guided alternative."),
    (S12, "Separate the two complication lists: the operation can bleed, damage the sphincter or recur, whereas the disease itself can thrombose, strangulate, fibrose, ulcerate or - rarely - seed portal pyaemia."),
    (S13, "A fissure is a split in the epithelium below the dentate line, classically at 6 o'clock, or at 12 o'clock after obstructed labour. Diagnose it by looking, never by pushing a finger in, and read the chronic triad of skin tag, fissure and hypertrophic papilla."),
    (S14, "Healing a fissure means breaking the pain-spasm-ischaemia cycle: fibre, fluids, sitz baths, laxatives, topical anaesthetic, and then a chemical sphincterotomy with diltiazem or nitrate - whose headache is the price of the smooth muscle relaxation."),
    (S15, "When medicines fail, the surgeon divides the internal sphincter laterally, so it relaxes and the fissure heals; when the sphincter must not be cut, an advancement flap brings healthy skin into the defect."),
    (S16, "Pilonidal disease is hairs driven under skin by friction - jeep drivers and barbers rather than surgeons. Treat the acute abscess by drainage and hair removal, then choose a definitive technique that flattens or shifts the natal cleft: Limberg, Bascom or Karydakis."),
    (S17, "Anorectal abscesses are named by the plane they occupy - perianal, intersphincteric, ischiorectal, supralevator. Remember that fluctuation is a late sign here just as it is in parotid, breast and palmar/plantar abscesses, and that inadequate drainage is what creates a fistula."),
    (S18, "A fistula is the chronic form of that abscess: an internal opening, one or many external openings, and a tract whose behaviour Goodsall's rule predicts from the external opening - with the long anterior fistula over 3 cm the famous exception."),
    (S19, "Classify before you cut. Park's four types come from the MR fistulogram, while the simpler high/low split is decided by whether the internal opening sits above or below the anorectal ring, and four principles - clear sepsis, map the tract, keep continence, avoid recurrence - govern the operation."),
    (S20, "Fistulectomy removes the whole tract and is cheap, but in a high fistula it would take the sphincter with it; fistulotomy merely opens the tract and cures the granulation tissue, trading completeness for safety."),
    (S21, "For a high fistula, a seton buys time and safety: a prolene thread tightened at intervals cuts slowly and fibroses behind itself, sparing continence, while a draining seton simply keeps sepsis quiet - the right choice in Crohn's disease."),
    (S22, "Prolapse splits cleanly by age and depth: mucosal prolapse in a child with a flat sacral curve, versus full-thickness prolapse in an adult with a weak pelvic floor. The child's first episode is reduced digitally; recurrence earns wiring or sclerotherapy."),
    (S23, "For complete prolapse the choice is abdominal or perineal. Abdominal rectopexy (Well's, Ripstein, Frykman-Goldberg) is harder but rarely recurs and suits the fit; the perineal options - Thiersch, Delorme, Altemeier - are gentler for the frail but recur more often."),
    (S24, "Every prolapse operation has a price: constipation is the commonest complaint, and pelvic dissection can cost a woman a rectovaginal fistula or a man bladder function and antegrade ejaculation."),
    (S25, "Solitary rectal ulcer syndrome is the anterior rectal ulcer 3-10 cm up that marks the start of an internal intussusception - fibromuscular obliteration of the lamina propria on biopsy, always biopsied to exclude cancer, and treated with stapled transanal rectal resection."),
    (S26, "In the newborn with no anal opening, look for the rest of VACTERL, then image. MRI best defines the anatomy, while the invertogram - done after 24 hours, coin on the proposed anus, baby upside down - turns the coin-to-gas distance into a simple high versus low answer."),
    (S27, "Finish by turning the anatomical level into a plan: boys leak stool into urine through rectovesical or rectourethral fistulae, girls present with the anus crowding the vagina, low anomalies go straight to PSARP, and high anomalies are staged behind a diverting colostomy."),
]

UNITS = []
for i, (title, guide) in enumerate(UNIT_DEFS, 1):
    UNITS.append({
        "id": f"SURG-U33-{i}",
        "ch": 33,
        "n": i,
        "title": title,
        "sec": f"{title} · p{first_page(title)}",
        "qs": sec_ids(title),
        "guide": guide,
    })

covered = [i for u in UNITS for i in u["qs"]]
assert covered == [x["id"] for x in Q], "units must cover questions in order"
assert len(set(covered)) == len(covered), "duplicate question in units"

data = {"questions": Q, "units": UNITS}
with open("data/ch33.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
print(f"ch33: {len(Q)} questions, {len(UNITS)} units")
