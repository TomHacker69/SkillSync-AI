from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_match_score(resume_text: str, jd_text: str) -> float:
    """
    Calculate similarity score between resume and job description.
    """
    documents = [resume_text, jd_text]
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(documents)
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
    return round(similarity * 100, 2)


def compare_skills(resume_skills: list, jd_skills: list) -> dict:
    """
    Compare resume skills and job description skills.
    """
    resume_set = set(resume_skills)
    jd_set = set(jd_skills)

    matched = sorted(list(resume_set.intersection(jd_set)))
    missing = sorted(list(jd_set - resume_set))

    return {
        "matched_skills": matched,
        "missing_skills": missing
    }
