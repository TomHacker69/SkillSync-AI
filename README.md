# SkillMatch AI

SkillMatch AI is an AI-powered resume analyzer and job matcher built using Python and Streamlit.

## Features
- Upload PDF or DOCX resume
- Extract text from resume
- Detect technical skills
- Compare resume with job description
- Calculate match score
- Identify missing skills
- Recommend suitable job roles
- Generate resume improvement feedback

## Tech Stack
- Python
- Streamlit
- PyMuPDF
- python-docx
- scikit-learn

## Project Structure
resume_analyzer/
├── app/
│   ├── main.py
│   ├── matcher.py
│   ├── parser.py
│   ├── recommender.py
│   ├── skills.py
│   └── utils.py
├── data/
│   ├── sample_jobs.json
│   └── skill_list.json
├── resumes/
├── README.md
└── requirements.txt

## Run the Project

```bash
pip install -r requirements.txt
streamlit run app/main.py
