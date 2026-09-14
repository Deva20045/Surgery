#!/usr/bin/env python3
"""Build data/ch31.json for PULSE Surgery ch31 (Colorectal Polyps and Cancer: Part 1, p218-226)."""
import json

Q = []
def q(page, sec, text, opts, ans, exp):
    Q.append({"id": f"SURG-C31-{len(Q)+1:03d}", "sec": sec, "page": page,
              "q": text, "opts": opts, "ans": ans, "exp": exp})

# ---------------- p218 ----------------
S1 = "Colorectal Polyps: Presentation, Inflammatory Polyps and Hyperplastic Polyps"
q(218, S1, "A colorectal polyp may present with all of the following EXCEPT:",
  ["Jaundice", "Pain", "Bleeding", "Obstruction"], 0,
  "The page lists pain, bleeding, and obstruction as presentations of colorectal polyps; jaundice is not listed. (Book p218)")
q(218, S1, "Inflammatory polyps are also called:",
  ["Pseudopolyps", "Tubular adenomas", "Villous adenomas", "Sessile serrated lesions"], 0,
  "Inflammatory polyp is equated with pseudopolyp on the page. (Book p218)")
q(218, S1, "Inflammatory pseudopolyps are classically seen in:",
  ["Ulcerative colitis", "Crohn's disease alone", "Diverticulosis", "Familial adenomatous polyposis"], 0,
  "The chapter specifically notes inflammatory polyps in ulcerative colitis. (Book p218)")
q(218, S1, "Inflammatory polyps are considered:",
  ["Not premalignant", "Always premalignant", "Obligate precursors of carcinoma", "Pathognomonic of FAP"], 0,
  "Inflammatory pseudopolyps are explicitly marked as not premalignant. (Book p218)")
q(218, S1, "The most common colorectal polyp mentioned in the chapter is:",
  ["Hyperplastic polyp", "Villous adenoma", "Juvenile polyp", "Inflammatory polyp"], 0,
  "Hyperplastic polyps are labelled the most common colorectal polyp. (Book p218)")
q(218, S1, "Hyperplastic polyps are typically seen in the:",
  ["6th-7th decade", "First decade", "Teenage years", "Third decade"], 0,
  "The age range given for hyperplastic polyps is the 6th-7th decade. (Book p218)")
q(218, S1, "The pathogenesis of hyperplastic polyps on the page is best summarized as:",
  ["Decreased epithelial turnover causing piling up of goblet cells and mucus secretion", "Accelerated dysplasia with APC loss", "Infective granuloma formation", "Hamartomatous overgrowth with smooth muscle arborization"], 0,
  "Hyperplastic polyps are described as arising from decreased epithelial turnover with piling of goblet cells and increased mucus secretion. (Book p218)")
q(218, S1, "The investigation mentioned for hyperplastic polyps is:",
  ["Colonoscopy", "Barium enema", "MR fistulogram", "PET-CT"], 0,
  "The page lists colonoscopy as the diagnostic test for hyperplastic polyps. (Book p218)")
q(218, S1, "Symptomatic hyperplastic polyps are treated by:",
  ["Endoscopic resection", "Total colectomy", "Radiotherapy", "Chemotherapy"], 0,
  "Management is endoscopic resection when hyperplastic polyps are symptomatic. (Book p218)")
q(218, S1, "Which of the following polyps on this page is not premalignant and most common in older adults?",
  ["Hyperplastic polyp", "Villous adenoma", "Peutz-Jeghers polyp", "Juvenile polyposis"], 0,
  "Hyperplastic polyps are specifically described as common in the 6th-7th decade and not premalignant. (Book p218)")

S2 = "Hamartomatous Polyps: Juvenile Polyps, Juvenile Polyposis and Peutz-Jeghers Syndrome"
q(218, S2, "A solitary juvenile polyp is usually:",
  ["Single and not premalignant", "Multiple and premalignant", "Associated with APC mutation", "Treated by right hemicolectomy"], 0,
  "A single juvenile polyp is described as solitary and not premalignant. (Book p218)")
q(218, S2, "The screening investigation mentioned for a single juvenile polyp is:",
  ["Screening colonoscopy", "Upper GI endoscopy", "CECT abdomen", "MRCP"], 0,
  "The page lists screening colonoscopy for diagnosis of a single juvenile polyp. (Book p218)")
q(218, S2, "Juvenile polyposis syndrome is characterized by:",
  ["Multiple juvenile polyps with SMAD4 mutation and premalignant potential", "Single rectal polyp with no cancer risk", "APC mutation with osteomas", "PTEN mutation with lipomas"], 0,
  "Juvenile polyposis syndrome is multiple, linked to SMAD4, inherited as autosomal dominant, and premalignant. (Book p218)")
q(218, S2, "The mutation associated with juvenile polyposis syndrome is in:",
  ["SMAD4", "MSH2", "APC", "PTEN"], 0,
  "Juvenile polyposis syndrome is linked with SMAD4 mutation on this page. (Book p218)")
q(218, S2, "Peutz-Jeghers syndrome is inherited as:",
  ["Autosomal dominant", "Autosomal recessive", "X-linked recessive", "Mitochondrial"], 0,
  "The chapter describes Peutz-Jeghers syndrome as autosomal dominant. (Book p218)")
q(218, S2, "The gene mutation classically associated with Peutz-Jeghers syndrome is:",
  ["LKB1/STK11 on chromosome 19", "PTEN on chromosome 10", "APC on chromosome 5", "MSH2 on chromosome 2"], 0,
  "Peutz-Jeghers syndrome is linked to LKB1/STK11 mutation on chromosome 19. (Book p218)")
q(218, S2, "The characteristic microscopic architecture of Peutz-Jeghers polyp is:",
  ["Arborizing tree-like pattern", "Saw-tooth serration", "Crypt abscess", "Honeycomb cysts"], 0,
  "The page describes Peutz-Jeghers polyps as having an arborizing or tree-like pattern. (Book p218)")
q(218, S2, "The most common site of Peutz-Jeghers hamartomatous polyps is the:",
  ["Jejunum", "Rectum", "Caecum", "Sigmoid colon"], 0,
  "The most common site is explicitly given as the jejunum. (Book p218)")
q(218, S2, "The pathognomonic sign of Peutz-Jeghers syndrome is:",
  ["Perioral melanosis", "CHRPE", "Aphthous ulcers", "Koilonychia"], 0,
  "Perioral melanosis is specifically labelled pathognomonic for Peutz-Jeghers syndrome. (Book p218)")
q(218, S2, "Peutz-Jeghers syndrome is classified on this page as:",
  ["Premalignant", "Not premalignant", "Purely inflammatory", "A vascular malformation"], 0,
  "The page marks Peutz-Jeghers syndrome as premalignant. (Book p218)")

# ---------------- p219 ----------------
S3 = "Hamartomatous Syndromes: Complications, Cowden Syndrome, Bannayan-Riley-Ruvalcaba and Cronkhite-Canada"
q(219, S3, "The most common clinical presentation of Peutz-Jeghers syndrome on this page is:",
  ["Intussusception", "Painless jaundice", "Hematemesis", "Tenesmus"], 0,
  "The page lists intussusception, due to telescoping of bowel, as the common presentation. (Book p219)")
q(219, S3, "Why does bowel obstruction occur in Peutz-Jeghers syndrome?",
  ["The polyp acts as a pathological lead point", "The anus is stenosed", "There is diffuse carcinomatosis", "The bowel is denervated"], 0,
  "The chapter explains that the hamartomatous polyp acts as a pathological lead point, producing intussusception and obstruction. (Book p219)")
q(219, S3, "Which malignancy risk is particularly emphasized in Peutz-Jeghers syndrome?",
  ["Pancreatic cancer", "Glioma", "Renal cell carcinoma", "Hepatoblastoma"], 0,
  "Peutz-Jeghers syndrome is associated with a marked increase in pancreatic cancer risk, noted as about 100 times. (Book p219)")
q(219, S3, "The approximate increase in pancreatic cancer risk in Peutz-Jeghers syndrome is:",
  ["100 times", "5 times", "10 times", "1000 times"], 0,
  "The page explicitly states pancreatic cancer risk is increased around 100 times in Peutz-Jeghers syndrome. (Book p219)")
q(219, S3, "Other malignancies listed with Peutz-Jeghers syndrome include:",
  ["Thyroid and periampullary cancers", "Glioma and medulloblastoma", "Renal cell carcinoma and HCC", "Rectal atresia and vestibular fistula"], 0,
  "The page adds thyroid cancer and periampullary cancer to the malignant associations of Peutz-Jeghers syndrome. (Book p219)")
q(219, S3, "Cowden syndrome is associated with mutation of:",
  ["PTEN on chromosome 10", "APC on chromosome 5", "LKB1 on chromosome 19", "SMAD4 on chromosome 18"], 0,
  "Cowden syndrome is linked with PTEN gene mutation on chromosome 10. (Book p219)")
q(219, S3, "Cowden syndrome is best described as:",
  ["Autosomal dominant hamartomatous polyposis that is not premalignant", "Autosomal recessive adenomatous polyposis", "X-linked inflammatory polyposis", "Sporadic rectal villous adenoma"], 0,
  "The syndrome is described as autosomal dominant, hamartomatous, and not premalignant. (Book p219)")
q(219, S3, "A characteristic cutaneous association of Cowden syndrome is:",
  ["Lipoma and ganglioneuromas", "Sebaceous cyst and osteoma", "Perioral melanosis", "Sentinel pile"], 0,
  "The page lists lipoma and ganglioneuromas as skin lesions associated with Cowden syndrome. (Book p219)")
q(219, S3, "Cowden syndrome increases the risk of all of the following EXCEPT:",
  ["Pancreatic cancer", "Breast cancer", "Thyroid cancer", "Uterine cancer"], 0,
  "On this page Cowden syndrome is linked with breast, thyroid, and uterine cancer risk, not pancreatic cancer. (Book p219)")
q(219, S3, "Bannayan-Riley-Ruvalcaba syndrome is associated with:",
  ["Multiple hamartomatous GI polyps and macrocephaly", "Hundreds of adenomatous colonic polyps", "Rectal bleeding with villous adenoma only", "Microsatellite instability and Lynch I"], 0,
  "The chapter lists multiple hamartomatous GI polyps and macrocephaly in Bannayan-Riley-Ruvalcaba syndrome. (Book p219)")
q(219, S3, "Which feature is specifically mentioned in Bannayan-Riley-Ruvalcaba syndrome?",
  ["Penile pigmentation", "Perioral melanosis", "CHRPE", "Portal pyaemia"], 0,
  "Penile pigmentation is one of the listed features of Bannayan-Riley-Ruvalcaba syndrome. (Book p219)")
q(219, S3, "Cronkhite-Canada syndrome is associated with all of the following EXCEPT:",
  ["Premalignant adenomatous polyposis", "Multiple GI polyps", "Ectodermal dysplasia", "Alopecia"], 0,
  "Cronkhite-Canada syndrome is described as multiple GI polyps that are not premalignant, with ectodermal dysplasia and alopecia. (Book p219)")
q(219, S3, "Which nail change is mentioned with Cronkhite-Canada syndrome?",
  ["Koilonychia", "Clubbing", "Leukonychia", "Beau lines"], 0,
  "Koilonychia is listed among the ectodermal associations of Cronkhite-Canada syndrome. (Book p219)")

# ---------------- p220-221 ----------------
S4 = "Adenomatous Polyps: Types, Malignant Potential and Endoscopic Resection"
q(220, S4, "Adenomatous polyps are considered:",
  ["Premalignant", "Never malignant", "Purely inflammatory", "Hamartomatous"], 0,
  "Adenomatous polyps are explicitly labeled premalignant. (Book p220)")
q(220, S4, "Which sequence correctly ranks adenomatous polyp types by malignant potential according to the chapter?",
  ["Villous > tubular", "Tubular > villous", "Tubulovillous > villous > tubular is not discussed", "All have identical risk"], 0,
  "The page specifically states villous polyps have greater malignant risk than tubular polyps. (Book p220)")
q(220, S4, "What happens to malignant risk as the size of an adenomatous polyp increases?",
  ["Risk increases", "Risk decreases", "Risk disappears", "Risk depends only on age"], 0,
  "The risk of malignant conversion rises as adenomatous polyps become larger. (Book p220)")
q(220, S4, "What happens to malignant risk as the number of adenomatous polyps increases?",
  ["Risk increases", "Risk decreases", "Risk stays unchanged", "Risk depends only on site"], 0,
  "The page clearly notes that increasing polyp number also increases malignant risk. (Book p220)")
q(220, S4, "Which morphology has greater malignant potential in the chapter?",
  ["Sessile polyp", "Pedunculated polyp", "Both are equal", "Mucosal tag"], 0,
  "The risk section states sessile lesions carry more risk than pedunculated ones. (Book p220)")
q(220, S4, "A villous polyp in a child most commonly occurs in the:",
  ["Rectum", "Jejunum", "Terminal ileum", "Caecum"], 0,
  "The page notes that villous polyps in children are most commonly found in the rectum. (Book p220)")
q(220, S4, "A child with a rectal villous polyp producing mucus-rich bicarbonate loss is prone to:",
  ["Metabolic acidosis and hypokalemia", "Metabolic alkalosis and hypernatremia", "Hypercalcemia and constipation", "Hypoglycemia and jaundice"], 0,
  "Villous polyps may secrete bicarbonate-rich mucus, leading to metabolic acidosis and hypokalemia. (Book p220)")
q(220, S4, "Clinical features of a villous polyp in a child include:",
  ["Bleeding and pain", "Hematuria and dysuria", "Jaundice and pruritus", "Weight gain and constipation only"], 0,
  "The page lists bleeding and pain among the clinical features of villous polyps in children. (Book p220)")
q(220, S4, "The recommended treatment for villous polyp in the chapter is:",
  ["Endoscopic resection", "Right hemicolectomy in all cases", "Radiotherapy", "Observation only"], 0,
  "Management of villous polyp on the page is endoscopic resection. (Book p220)")
q(220, S4, "A pedunculated colorectal polyp is resected endoscopically by:",
  ["Passing a snare around the polyp stalk", "Injecting sclerosant into the stalk only", "Applying a stapler from the anal verge", "Performing APR"], 0,
  "The diagram shows a pedunculated polyp removed by passing a snare around the stalk. (Book p220)")
q(220, S4, "In endoscopic mucosal resection of a non-pedunculated lesion, saline is injected to:",
  ["Lift the lesion away from the underlying muscular layer", "Cause thrombosis of the lesion", "Demonstrate lymphatic spread", "Mark the caecum"], 0,
  "The diagram explains that saline injection raises the lesion and separates it from underlying muscle. (Book p220)")
q(220, S4, "After saline lift of a non-pedunculated polyp, the next step shown is:",
  ["Passing a diathermy snare over the raised lesion", "Immediate APR", "CT-guided biopsy", "Rubber band ligation"], 0,
  "The resection sequence shown is identification, saline lift, diathermy snare, and complete excision. (Book p220)")
q(220, S4, "Which layer must be protected during endoscopic resection of a sessile lesion?",
  ["Muscularis propria", "Falciform ligament", "Taenia coli", "Mesoappendix"], 0,
  "The saline-lift diagram emphasizes separation of the lesion from the underlying muscularis propria. (Book p220)")

S5 = "Cancer in a Polyp and the Adenoma-Carcinoma Sequence"
q(221, S5, "In Haggitt classification, invasion restricted to the head of a pedunculated polyp is:",
  ["Level 1", "Level 2", "Level 3", "Level 4"], 0,
  "Haggitt level 1 means carcinoma is restricted to the head of a pedunculated polyp. (Book p221)")
q(221, S5, "In Haggitt classification, invasion into the neck of the polyp is:",
  ["Level 2", "Level 1", "Level 3", "Level 4"], 0,
  "Haggitt level 2 indicates invasion into the neck of the polyp. (Book p221)")
q(221, S5, "In Haggitt classification, invasion into the stalk of a pedunculated polyp is:",
  ["Level 3", "Level 1", "Level 2", "Level 4"], 0,
  "Haggitt level 3 indicates stalk invasion. (Book p221)")
q(221, S5, "In Haggitt classification, invasion into the submucosa is:",
  ["Level 4", "Level 3", "Level 2", "Level 1"], 0,
  "Haggitt level 4 corresponds to invasion into submucosa beyond the stalk. (Book p221)")
q(221, S5, "According to the page, Haggitt level 1 and 2 lesions in a polyp can be treated by:",
  ["Endoscopic resection", "APR", "Chemoradiation", "Total colectomy"], 0,
  "The note to the right of the figure states level 1 and 2 lesions are suitable for endoscopic resection. (Book p221)")
q(221, S5, "Cancer in a sessile polyp is considered equivalent to:",
  ["Level 4 disease", "Level 1 disease", "Level 2 disease", "No invasion"], 0,
  "The page specifically says cancer in a sessile polyp corresponds to level 4. (Book p221)")
q(221, S5, "Why is cancer in a sessile polyp particularly concerning on this page?",
  ["It spreads faster", "It never bleeds", "It always stays intramucosal", "It cannot be seen on colonoscopy"], 0,
  "The note beside the figure states that cancer in a sessile polyp shows faster spread. (Book p221)")
q(221, S5, "The adenoma-carcinoma sequence is classically formulated by:",
  ["Vogelstein", "Couinaud", "Parks", "Goodsall"], 0,
  "The page attributes the adenoma-carcinoma sequence to Vogelstein. (Book p221)")
q(221, S5, "The earliest major 'first hit' in the adenoma-carcinoma sequence on this page is loss of:",
  ["APC on chromosome 5", "p53", "SMAD4", "MSH2"], 0,
  "The diagram shows APC loss on chromosome 5 as the first hit producing early adenoma and dysplastic crypts. (Book p221)")
q(221, S5, "KRAS mutation in the adenoma-carcinoma sequence is associated with progression to:",
  ["Intermediate adenoma", "Normal epithelium", "Carcinoma in situ only", "Hydatid cyst"], 0,
  "KRAS is placed at the stage of intermediate adenoma in the sequence. (Book p221)")
q(221, S5, "Loss of 18q with genes such as SMAD4 and CDC4 is associated with:",
  ["Late adenoma progression", "Juvenile polyp formation", "Anal fissure", "Immediate metastatic spread"], 0,
  "The diagram places loss of 18q, SMAD4, and CDC4 later in the adenoma-carcinoma pathway before frank cancer. (Book p221)")
q(221, S5, "The final hit driving progression to carcinoma in the mnemonic AKS3 is loss of:",
  ["p53", "PTEN", "BRAF", "CEA"], 0,
  "The page's mnemonic AKS3 stands for APC, KRAS, and p53 as the key progression events. (Book p221)")
q(221, S5, "Microsatellite instability pathway in colorectal carcinogenesis involves:",
  ["MMR gene inactivation and hypermethylation", "Portal venous thrombosis", "Pudendal nerve injury", "HBV integration"], 0,
  "The figure separately highlights microsatellite instability through mismatch-repair gene inactivation and hypermethylation. (Book p221)")
q(221, S5, "Which signalling pathway is shown near the earliest dysplastic transformation in the adenoma-carcinoma sequence?",
  ["Wnt signalling", "Hedgehog signalling", "Notch only", "VEGF pathway only"], 0,
  "The diagram marks Wnt signalling near the earliest APC-related dysplastic stage. (Book p221)")

# ---------------- p222-224 ----------------
S6 = "Familial Adenomatous Polyposis, MAP and HNPCC"
q(222, S6, "Familial adenomatous polyposis (FAP) is inherited as:",
  ["Autosomal dominant", "Autosomal recessive", "X-linked dominant", "Mitochondrial"], 0,
  "FAP is described as an autosomal dominant disorder. (Book p222)")
q(222, S6, "The gene mutated in FAP is:",
  ["APC on chromosome 5", "PTEN on chromosome 10", "MSH2 on chromosome 2", "STK11 on chromosome 19"], 0,
  "The FAP page identifies APC gene mutation on chromosome 5. (Book p222)")
q(222, S6, "The hallmark of FAP is:",
  [">100 adenomatous polyps with nearly 100% colorectal cancer risk", "A single rectal juvenile polyp", "Only extracolonic tumours", "Multiple pseudopolyps in UC"], 0,
  "FAP is defined on the page by more than 100 adenomatous polyps carrying a 100% risk of colorectal cancer. (Book p222)")
q(222, S6, "The most common site prominently mentioned in FAP is the:",
  ["Rectum", "Jejunum", "Anal canal", "Appendix"], 0,
  "FAP most commonly involves the rectum, although the entire colon may be involved. (Book p222)")
q(222, S6, "A classic extraintestinal manifestation of FAP is:",
  ["Congenital hypertrophy of retinal pigment epithelium (CHRPE)", "Perioral melanosis", "Sentinel pile", "Koilonychia"], 0,
  "The page specifically lists CHRPE as an extraintestinal manifestation of FAP. (Book p222)")
q(222, S6, "Gardner variant of FAP includes all EXCEPT:",
  ["Glioma", "Osteoma", "Sebaceous cyst", "Desmoid tumour"], 0,
  "Gardner variant includes osteomas, sebaceous cysts and desmoid tumour; glioma belongs to Turcot variant. (Book p222)")
q(222, S6, "Turcot variant of FAP is associated with CNS tumours, especially:",
  ["Glioma", "Meningioma", "Pituitary adenoma", "Acoustic neuroma"], 0,
  "Turcot variant is linked with CNS tumours, glioma being the most common on the page. (Book p222)")
q(222, S6, "Which childhood CNS tumour is also listed in Turcot variant?",
  ["Medulloblastoma", "Ependymoma", "Craniopharyngioma", "Schwannoma"], 0,
  "The page adds medulloblastoma, especially in children, under Turcot variant. (Book p222)")
q(222, S6, "The definitive colorectal surgery shown for FAP is:",
  ["Total proctocolectomy with ileoanal pouch anastomosis", "Right hemicolectomy", "Sigmoidectomy", "APR in every patient"], 0,
  "The management section recommends total proctocolectomy with ileoanal pouch anastomosis. (Book p222)")
q(222, S6, "The anastomosis for FAP surgery on this page is done using a:",
  ["Circular stapler", "Linear stapler only", "Hand-sewn end ileostomy", "Mesh ring"], 0,
  "The page specifically says the ileoanal pouch anastomosis is done with a circular stapler. (Book p222)")
q(223, S6, "A first-degree relative of a patient with FAP should first undergo:",
  ["Genetic counselling and testing", "Immediate colectomy", "PET-CT", "Only annual CEA"], 0,
  "The algorithm begins with genetic counselling and testing for first-degree relatives. (Book p223)")
q(223, S6, "If APC mutation is present in a first-degree relative of a patient with FAP, screening should begin at:",
  ["10 years", "18 years", "25 years", "50 years"], 0,
  "The page directs APC-positive relatives to begin screening at 10 years. (Book p223)")
q(223, S6, "The recommended screening method for APC-positive children in FAP is:",
  ["Annual sigmoidoscopy", "Annual colon capsule endoscopy", "PET-CT every year", "Barium enema"], 0,
  "Annual sigmoidoscopy is the surveillance test specified for APC-positive first-degree relatives. (Book p223)")
q(223, S6, "If polyps are found during surveillance in a genetically positive FAP relative, the next step is:",
  ["Surgery", "Observation until age 18", "Radiotherapy", "Antibiotics"], 0,
  "The algorithm is straightforward: once polyps are present, surgery is advised. (Book p223)")
q(223, S6, "If no polyps appear until 18 years of age in an APC-positive FAP relative, the chapter advises:",
  ["Screen as the general population", "Immediate prophylactic APR", "Stop all surveillance permanently", "Yearly PET-CT"], 0,
  "The flowchart says those without polyps until 18 years are thereafter screened like the general population. (Book p223)")
q(223, S6, "MUTYH-associated polyposis (MAP) is inherited as:",
  ["Autosomal recessive", "Autosomal dominant", "X-linked recessive", "Sporadic only"], 0,
  "MAP is described on the page as autosomal recessive. (Book p223)")
q(223, S6, "Multiple colonic polyps with absent APC mutation should suggest:",
  ["MUTYH-associated polyposis", "Peutz-Jeghers syndrome", "Ulcerative colitis", "Turcot syndrome"], 0,
  "The chapter specifically points out multiple polyps without APC mutation as a clue to MAP. (Book p223)")
q(223, S6, "Surveillance in MUTYH-associated polyposis is:",
  ["Colonoscopy every 2 years", "Sigmoidoscopy once in 10 years", "No follow-up required", "Only ultrasound"], 0,
  "The follow-up schedule shown for MAP is 2-yearly colonoscopy. (Book p223)")
q(223, S6, "During follow-up of MAP, the clinician should also assess for:",
  ["Duodenal adenomas", "Hydatid cysts", "Varicose veins", "Anorectal malformation"], 0,
  "The page explicitly instructs assessment for duodenal adenomas in MAP follow-up. (Book p223)")
q(223, S6, "HNPCC develops through an alternate pathway characterized by:",
  ["Microsatellite instability without a preceding polyp", "Massive adenomatous polyposis", "Portal pyaemia", "Hyperplastic goblet cell piling"], 0,
  "The pathogenesis line describes HNPCC as microsatellite instability leading to cancer through an alternate pathway without polyp formation. (Book p223)")
q(223, S6, "The most common gene mutation listed in HNPCC is:",
  ["MSH2", "APC", "PTEN", "SMAD4"], 0,
  "MSH2 is mentioned as the most common gene involved in HNPCC, with MLH1 also listed. (Book p223)")
q(223, S6, "Microsatellite instability in HNPCC is studied by the:",
  ["Bethesda classification", "Montreal classification", "Child-Pugh score", "Hinchey staging"], 0,
  "The chapter states that microsatellite instability is studied using the Bethesda classification. (Book p223)")
q(223, S6, "Lynch I syndrome in HNPCC refers predominantly to:",
  ["Colonic cancer", "Ovarian cancer", "Pancreatic cancer", "Thyroid cancer"], 0,
  "Lynch I is the colonic cancer form of HNPCC, with a risk given as about 60-70%. (Book p223)")
q(223, S6, "The most common extracolonic malignancy listed in Lynch II syndrome is:",
  ["Uterine cancer", "Liver cancer", "Bladder cancer", "Medulloblastoma"], 0,
  "For Lynch II, the page specifically notes uterine cancer as the most common extracolonic malignancy. (Book p223)")
q(223, S6, "Which of the following is listed as an extracolonic cancer in Lynch II syndrome?",
  ["Ovarian cancer", "Glioma", "Breast cancer", "Renal cell carcinoma"], 0,
  "The page lists ovarian cancer among the extracolonic malignancies seen in Lynch II syndrome. (Book p223)")

S7 = "Amsterdam Criteria, FAP versus HNPCC, Risk Factors and Screening"
q(224, S7, "One component of the modified Amsterdam criteria for HNPCC is:",
  ["Three or more HNPCC-related cancers in more than one generation", "More than 100 adenomatous polyps", "Perioral melanosis", "Microsatellite stability"], 0,
  "The modified Amsterdam criteria include at least 3 HNPCC-related cancers across more than one generation. (Book p224)")
q(224, S7, "According to the modified Amsterdam criteria, one affected person should be a:",
  ["First-degree relative of the other two", "Twin of the youngest patient", "Male relative only", "Second-degree relative of all affected members"], 0,
  "The criteria specify that one affected individual must be a first-degree relative of the other two. (Book p224)")
q(224, S7, "Which age criterion is part of the modified Amsterdam criteria?",
  ["At least one HNPCC-related cancer diagnosed before 50 years", "At least one diagnosed after 70 years", "All cancers diagnosed in childhood", "No age criterion exists"], 0,
  "The page includes one HNPCC-related cancer diagnosed before 50 years. (Book p224)")
q(224, S7, "Which of the following must be excluded before diagnosing HNPCC by Amsterdam criteria?",
  ["Familial adenomatous polyposis", "Ulcerative colitis", "Crohn's disease", "Hyperplastic polyposis"], 0,
  "Exclusion of familial adenomatous polyposis is one of the required Amsterdam criteria. (Book p224)")
q(224, S7, "The last requirement in the modified Amsterdam criteria is:",
  ["Histologically confirmed cancer", "Positive AFP", "CEA above 100", "Presence of liver metastasis"], 0,
  "Histologic confirmation of cancer is specifically included in the criteria. (Book p224)")
q(224, S7, "Compared with HNPCC, tumour initiation in FAP is:",
  ["Accelerated", "Normal", "Absent", "Delayed by polyps"], 0,
  "The comparison table states tumour initiation is accelerated in FAP. (Book p224)")
q(224, S7, "Compared with FAP, tumour progression in HNPCC is:",
  ["Accelerated", "Normal", "Impossible", "Confined to the rectum"], 0,
  "Because HNPCC lacks a long polyp phase, tumour progression is shown as accelerated. (Book p224)")
q(224, S7, "Which of the following is a risk factor for colorectal cancer listed on the page?",
  ["High-fat diet", "Smoking cessation", "Low-fibre stool softeners", "Hyperthyroidism"], 0,
  "High-fat diet is among the colorectal cancer risk factors listed on the page. (Book p224)")
q(224, S7, "Ureterosigmoid anastomosis is mentioned as:",
  ["An obsolete but very high-risk factor for colorectal cancer", "A protective factor", "A treatment for rectal prolapse", "A cause of thrombosed piles"], 0,
  "The page notes ureterosigmoid anastomosis is obsolete but increases colorectal cancer risk by around 100 times. (Book p224)")
q(224, S7, "Long-standing ulcerative colitis and Crohn's disease increase colorectal cancer risk because they are forms of:",
  ["Inflammatory bowel disease", "Vascular disease", "Congenital anomaly", "Endocrine neoplasia"], 0,
  "Inflammatory bowel disease, especially long-standing UC and Crohn's disease, is listed as a colorectal cancer risk factor. (Book p224)")
q(224, S7, "Which of the following is listed as protective against colorectal cancer?",
  ["NSAIDs", "Red meat", "Alcohol", "Diverticular disease"], 0,
  "NSAIDs are specifically listed as protective factors on the page. (Book p224)")
q(224, S7, "Which antidiabetic drug is mentioned as protective against colorectal cancer?",
  ["Metformin", "Sulfonylurea", "Acarbose", "Insulin glargine"], 0,
  "Metformin is named among the protective factors for colorectal cancer. (Book p224)")
q(224, S7, "Routine colorectal cancer screening in the general population begins at:",
  ["50 years", "30 years", "18 years", "70 years"], 0,
  "The page gives 50 years as the screening age for colorectal cancer. (Book p224)")
q(224, S7, "In a person with family history, screening should start:",
  ["10 years before diagnosis of the youngest affected relative", "At exactly the same age as the relative", "Only after symptoms begin", "At 70 years"], 0,
  "The page directs screening 10 years before the age at diagnosis of the youngest relative. (Book p224)")
q(224, S7, "The best screening investigation for colorectal cancer on this page is:",
  ["Colonoscopy", "Sigmoidoscopy", "FOBT alone", "Virtual colonoscopy"], 0,
  "Colonoscopy is explicitly labelled the best screening test. (Book p224)")
q(224, S7, "Recommended interval for screening colonoscopy in average-risk individuals is:",
  ["Once in 10 years", "Every year", "Every 2 years", "Once in 20 years"], 0,
  "The screening section states colonoscopy should be done once in 10 years. (Book p224)")
q(224, S7, "Colonoscopy visualizes the bowel from:",
  ["Anal canal to caecum", "Rectum to splenic flexure only", "Ileocecal valve to terminal ileum only", "Anal verge to dentate line only"], 0,
  "The page states colonoscopy visualizes the colon from the anal canal to the caecum. (Book p224)")
q(224, S7, "The length of colonoscope mentioned in the chapter is:",
  ["110-140 cm", "10 cm", "13 cm", "60-90 cm"], 0,
  "The screening page lists the colonoscope length as 110-140 cm. (Book p224)")
q(224, S7, "Flexible sigmoidoscopy is recommended at what interval on this page?",
  ["Once in 5 years", "Once in 10 years", "Yearly", "Every month"], 0,
  "Sigmoidoscopy is listed as a screening tool to be done once in 5 years. (Book p224)")
q(224, S7, "The visualized length of the sigmoidoscope is approximately:",
  ["60-90 cm", "10 cm", "13 cm", "110-140 cm"], 0,
  "The page gives the visualized length of sigmoidoscopy as about 60-90 cm. (Book p224)")

# ---------------- p225-226 ----------------
S8 = "Clinical Features, Investigations, Spread and Staging of Colorectal Cancer"
q(225, S8, "Fecal occult blood testing (FOBT) is recommended with what frequency on this page?",
  ["Yearly", "Once in 10 years", "Once in 5 years", "Only when symptomatic"], 0,
  "The page lists fecal occult blood testing as a yearly screening modality. (Book p225)")
q(225, S8, "Virtual colonoscopy is essentially:",
  ["CECT with 3D reconstruction", "MRI pelvis with endorectal coil", "Capsule endoscopy", "Barium enema only"], 0,
  "The chapter defines virtual colonoscopy as contrast-enhanced CT with 3D reconstruction. (Book p225)")
q(225, S8, "An advantage of virtual colonoscopy listed on the page is:",
  ["It is non-invasive and gives better extracolonic detail", "It provides biopsy better than colonoscopy", "It stages lymph nodes more accurately than PET-CT", "It is therapeutic in obstruction"], 0,
  "Virtual colonoscopy is described as non-invasive and better for extra-colonic details. (Book p225)")
q(225, S8, "The most common site of colorectal cancer mentioned on the page is the:",
  ["Rectum", "Caecum", "Descending colon", "Appendix"], 0,
  "The chapter states rectum is the most common site, followed by sigmoid colon. (Book p225)")
q(225, S8, "A right-sided colonic cancer most commonly appears as:",
  ["Ulceroproliferative or exophytic growth", "Annular napkin-ring lesion", "Diffuse mucosal prolapse", "Circumferential fibrotic fistula"], 0,
  "Right-sided cancers are described as ulceroproliferative or exophytic lesions. (Book p225)")
q(225, S8, "Iron deficiency anemia is classically associated with:",
  ["Right-sided colonic cancer", "Left-sided colonic cancer", "Anal fissure", "Thrombosed piles"], 0,
  "The chapter lists iron deficiency anemia under right-sided colonic cancers. (Book p225)")
q(225, S8, "Why does right-sided colon cancer tend to cause obstruction later?",
  ["Fecal matter is more liquid on the right side", "Right colon has no lymphatics", "It never encircles the lumen", "The caecum is fixed"], 0,
  "The page explains delayed obstruction on the right by the liquid consistency of fecal matter. (Book p225)")
q(225, S8, "A left-sided colonic cancer often produces which lesion?",
  ["Annular apple-core or napkin-ring lesion", "Exophytic cauliflower mass only", "Flask-shaped ulcer", "Water-lily sign"], 0,
  "Left-sided cancers are classically constricting and are described as annular, apple-core, or napkin-ring lesions. (Book p225)")
q(225, S8, "Altered bowel habits with early obstruction is more typical of:",
  ["Left-sided colonic cancer", "Right-sided colonic cancer", "Single juvenile polyp", "Crohn's ileitis"], 0,
  "Because left-sided cancers are constricting, they tend to produce alteration in bowel habits and obstruction early. (Book p225)")
q(225, S8, "The investigation of choice for confirming colorectal cancer is:",
  ["Colonoscopic biopsy", "FOBT", "CEA", "USG abdomen"], 0,
  "The page labels colonoscopic biopsy as the investigation of choice. (Book p225)")
q(225, S8, "PET-CT in colorectal cancer is mainly used for:",
  ["Overall staging", "Detecting hemorrhoids", "Diagnosing fissure", "Assessing rectal prolapse"], 0,
  "PET-CT is listed as the study for overall staging. (Book p225)")
q(225, S8, "MRI with an endorectal coil is specifically used for:",
  ["T and N staging of rectal cancer", "Diagnosing right colon cancer", "Screening asymptomatic FAP", "Detecting colonic diverticulosis"], 0,
  "The chapter specifies MRI with endorectal coil for T and N staging of rectal cancer. (Book p225)")
q(225, S8, "The tumour marker used in colorectal cancer is:",
  ["CEA", "AFP", "CA-125", "PIVKA"], 0,
  "CEA is the tumour marker listed for colorectal cancer. (Book p225)")
q(225, S8, "The most common site of distant spread of colorectal cancer is the:",
  ["Liver", "Lung", "Brain", "Bone marrow"], 0,
  "The spread section states liver is the most common site of distant spread. (Book p225)")
q(226, S8, "In TNM staging of colorectal cancer, T1 means tumour invades the:",
  ["Submucosa", "Mucosa only", "Muscularis propria", "Adjacent structures"], 0,
  "The TNM page defines T1 as tumour invading the submucosa. (Book p226)")
q(226, S8, "In TNM staging of colorectal cancer, T2 means tumour invades the:",
  ["Muscularis propria", "Submucosa", "Serosa only", "Adjacent structures"], 0,
  "T2 is defined as tumour invading the muscularis propria. (Book p226)")
q(226, S8, "In TNM staging of colorectal cancer, T3 means tumour:",
  ["Passes through the muscularis propria", "Invades adjacent structures", "Is carcinoma in situ", "Has no tumour"], 0,
  "The page describes T3 as tumour extending through the muscularis propria. (Book p226)")
q(226, S8, "In TNM staging, T4 colorectal cancer invades:",
  ["Adjacent structures", "Only muscularis mucosa", "Submucosa only", "No tissue at all"], 0,
  "T4 is defined on the page as tumour invading adjacent structures. (Book p226)")
q(226, S8, "For adequate nodal assessment in colorectal cancer, at least how many lymph nodes should be removed?",
  ["12", "6", "20", "2"], 0,
  "The page specifies a minimum of 12 lymph nodes should be removed. (Book p226)")
q(226, S8, "Duke's/modified Astler-Coller stage B1 corresponds to tumour extending:",
  ["Into the muscle layer", "Beyond the muscle layer", "With distant metastasis", "Only in mucosa and submucosa"], 0,
  "In the table, B1 means the tumour has reached into the muscle layer. (Book p226)")
q(226, S8, "Duke's/modified Astler-Coller stage B2 corresponds to tumour extending:",
  ["Beyond the muscle layer", "Only into submucosa", "With lymph node metastasis only", "With distant metastasis"], 0,
  "B2 is defined as tumour beyond the muscle layer. (Book p226)")
q(226, S8, "Duke's/modified Astler-Coller stage C1 means:",
  ["B1 lesion with positive lymph nodes", "B2 lesion with positive lymph nodes", "Distant metastasis", "Only mucosa involved"], 0,
  "The table shows C1 as B1 plus lymph node involvement. (Book p226)")
q(226, S8, "Duke's/modified Astler-Coller stage C2 means:",
  ["B2 lesion with positive lymph nodes", "B1 lesion with positive nodes", "Stage with distant metastasis", "Tumour confined to mucosa"], 0,
  "C2 is the B2 lesion with lymph node positivity. (Book p226)")
q(226, S8, "Duke's/modified Astler-Coller stage D indicates:",
  ["Distant metastasis", "Tumour into muscle only", "Only nodal disease", "Only submucosal disease"], 0,
  "Stage D in the table denotes distant metastasis. (Book p226)")

# ---------------- units ----------------
def sec_ids(*labels):
    return [x["id"] for x in Q if x["sec"] in labels]

def first_page(label):
    for x in Q:
        if x["sec"] == label:
            return x["page"]
    return 0

UNIT_DEFS = [
    (S1, "Start with the simple polyps and make them separate in your head: inflammatory pseudopolyps belong to ulcerative colitis and are not premalignant, while hyperplastic polyps are the common late-life, mucus-rich lesions with reduced epithelial turnover. They matter because you must not confuse frequency with malignancy risk."),
    (S2, "Hamartomatous lesions split into benign and premalignant syndromes. A solitary juvenile polyp is usually innocent, juvenile polyposis is SMAD4-driven and premalignant, and Peutz-Jeghers is the classic STK11 syndrome with jejunal arborizing polyps and perioral melanosis."),
    (S3, "Peutz-Jeghers does not stay theoretical - it intussuscepts, bleeds and predisposes to pancreatic and periampullary malignancy. Then come the other hamartomatous syndromes: PTEN-based Cowden, macrocephalic Bannayan-Riley-Ruvalcaba, and ectodermal Cronkhite-Canada."),
    (S4, "Adenomatous polyps are where cancer risk starts to rise in a structured way: bigger, more numerous, villous and sessile means worse. Endoscopic treatment also differs by shape - stalked lesions are snared, while flat ones are lifted off muscle with saline before diathermy excision."),
    (S5, "Cancer in a polyp is staged by depth. Haggitt levels tell you when endoscopic therapy is enough and when submucosal spread changes the game, especially in sessile lesions. Behind this lies Vogelstein's adenoma-carcinoma sequence - APC first, KRAS next, p53 late - with a parallel microsatellite instability pathway."),
    (S6, "FAP is APC-driven, rectum-heavy, CHRPE-associated, and cancer-prone enough to justify total proctocolectomy with ileoanal pouch. Know Gardner and Turcot variants, the screening algorithm for relatives, how MAP differs by inheritance, and how HNPCC/Lynch bypasses the polyp phase through mismatch-repair failure."),
    (S7, "Amsterdam criteria and the FAP-versus-HNPCC table turn genetics into clinic. Then zoom out to population medicine: alcohol, red meat, IBD and obsolete ureterosigmoidostomy raise colorectal cancer risk, whereas NSAIDs and metformin protect. Colonoscopy is the best screen, but the exam loves intervals, ages, and scope lengths."),
    (S8, "Finish with how cancers behave. Rectum leads the site list, right-sided tumors bleed and cause anemia before obstructing, left-sided tumors constrict early, and colonoscopic biopsy is the diagnostic anchor. Then stage them with TNM and Duke's/Astler-Coller so treatment decisions make anatomical sense."),
]

UNITS = []
for i, (title, guide) in enumerate(UNIT_DEFS, 1):
    UNITS.append({"id": f"SURG-U31-{i}", "ch": 31, "n": i, "title": title,
                  "sec": f"{title} · p{first_page(title)}", "qs": sec_ids(title),
                  "guide": guide})

covered = [i for u in UNITS for i in u["qs"]]
assert covered == [x["id"] for x in Q], "units must cover questions in order"

data = {"questions": Q, "units": UNITS}
with open("data/ch31.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
print(f"ch31: {len(Q)} questions, {len(UNITS)} units")
