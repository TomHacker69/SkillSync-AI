import json


def load_sample_jobs(file_path: str = "data/sample_jobs.json") -> dict:
    """
    Load sample job roles and their required skills.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def recommend_roles(resume_skills: list, sample_jobs: dict) -> list:
    """
    Recommend roles based on skill overlap.
    """
    recommendations = []

    resume_skill_set = set(skill.lower() for skill in resume_skills)

    for role, required_skills in sample_jobs.items():
        required_set = set(skill.lower() for skill in required_skills)
        matched = resume_skill_set.intersection(required_set)
        score = 0

        if required_set:
            score = round((len(matched) / len(required_set)) * 100, 2)

        recommendations.append({
            "role": role,
            "score": score,
            "matched_skills": sorted(list(matched))
        })

    recommendations.sort(key=lambda x: x["score"], reverse=True)
    return recommendations[:5]


def generate_feedback(missing_skills: list, match_score: float) -> list:
    """
    Generate improvement suggestions.
    """
    feedback = []

    if match_score >= 75:
        feedback.append("Your resume is strongly aligned with the job description.")
    elif match_score >= 50:
        feedback.append("Your resume has moderate alignment. Adding more relevant keywords can improve it.")
    else:
        feedback.append("Your resume has low alignment with the job description. Consider tailoring it for this role.")

    if missing_skills:
        feedback.append("Consider adding or learning these missing skills:")
        feedback.extend([f"- {skill}" for skill in missing_skills[:10]])

    return feedback
