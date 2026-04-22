import json
from app.utils import normalize_text


def load_skill_list(file_path: str = "data/skill_list.json") -> list:
    """
    Load skills from JSON file.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def extract_skills_from_text(text: str, skill_list: list) -> list:
    """
    Match skills from the resume/job description text.
    """
    text = normalize_text(text)
    found_skills = set()

    for skill in skill_list:
        if skill.lower() in text:
            found_skills.add(skill)

    return sorted(found_skills)
