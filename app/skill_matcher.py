from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

REQUIRED_SKILLS = [
    "python",
    "fastapi",
    "sql",
    "docker",
    "aws",
    "machine learning",
    "git",
    "rest api"
]

def find_matching_skills(resume_text: str):
    resume_text = resume_text.lower()
    
    matched = []
    missing = []
    
    for skill in REQUIRED_SKILLS:
        if skill in resume_text:
            matched.append(skill)
        else:
            missing.append(skill)
            
    return matched, missing

def calculate_resume_score(resume_text: str):
    job_description = " ".join(REQUIRED_SKILLS)
    
    documents = [resume_text, job_description]
    
    vectorizer = CountVectorizer()
    
    matrix = vectorizer.fit_transform(documents)
    
    similarity = cosine_similarity(matrix)[0][1]
    
    return round(similarity * 100, 2)
