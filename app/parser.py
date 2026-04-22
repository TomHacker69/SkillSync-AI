import os
import fitz  # PyMuPDF
from docx import Document
from app.utils import clean_text


def extract_text_from_pdf(file_path: str) -> str:
    """
    Extract text from a PDF file using PyMuPDF.
    """
    text = ""
    try:
        pdf = fitz.open(file_path)
        for page in pdf:
            text += page.get_text()
        pdf.close()
    except Exception as e:
        raise Exception(f"Error reading PDF: {e}")

    return clean_text(text)


def extract_text_from_docx(file_path: str) -> str:
    """
    Extract text from a DOCX file.
    """
    try:
        doc = Document(file_path)
        text = "\n".join([para.text for para in doc.paragraphs])
    except Exception as e:
        raise Exception(f"Error reading DOCX: {e}")

    return clean_text(text)


def extract_resume_text(file_path: str) -> str:
    """
    Detect file type and extract text accordingly.
    """
    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".pdf":
        return extract_text_from_pdf(file_path)
    elif ext == ".docx":
        return extract_text_from_docx(file_path)
    else:
        raise ValueError("Unsupported file format. Please upload PDF or DOCX.")
