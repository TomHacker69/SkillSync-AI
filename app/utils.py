import re


def clean_text(text: str) -> str:
    """
    Clean extracted text by removing extra spaces and unwanted characters.
    """
    if not text:
        return ""

    text = text.replace("\n", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def normalize_text(text: str) -> str:
    """
    Lowercase and clean text for comparison.
    """
    return clean_text(text).lower()
