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
