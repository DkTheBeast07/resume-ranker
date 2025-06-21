import spacy

nlp = spacy.load("en_core_web_sm")

def extract_skills(text):
    doc = nlp(text)
    skills = set()
    for token in doc:
        if token.pos_ in ["PROPN", "NOUN"]:
            if len(token.text) > 2:
                skills.add(token.text.lower())
    return skills

def get_matched_skills(resume_text, jd_text):
    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(jd_text)

    matched = resume_skills.intersection(jd_skills)
    return list(matched)
