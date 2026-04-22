import os
import streamlit as st

from app.parser import extract_resume_text
from app.skills import load_skill_list, extract_skills_from_text
from app.matcher import calculate_match_score, compare_skills
from app.recommender import load_sample_jobs, recommend_roles, generate_feedback


st.set_page_config(page_title="SkillMatch AI", layout="wide")

st.title("SkillMatch AI")
st.subheader("AI Resume Analyzer and Job Matcher")

uploaded_file = st.file_uploader("Upload your resume (PDF or DOCX)", type=["pdf", "docx"])
job_description = st.text_area("Paste Job Description Here", height=250)

if uploaded_file:
    os.makedirs("resumes", exist_ok=True)
    file_path = os.path.join("resumes", uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("Resume uploaded successfully.")

    try:
        resume_text = extract_resume_text(file_path)
        skill_list = load_skill_list()
        sample_jobs = load_sample_jobs()

        resume_skills = extract_skills_from_text(resume_text, skill_list)

        st.markdown("## Extracted Resume Skills")
        if resume_skills:
            st.write(", ".join(resume_skills))
        else:
            st.warning("No known skills detected from the resume.")

        if job_description.strip():
            jd_skills = extract_skills_from_text(job_description, skill_list)
            match_score = calculate_match_score(resume_text, job_description)
            skill_comparison = compare_skills(resume_skills, jd_skills)
            role_recommendations = recommend_roles(resume_skills, sample_jobs)
            feedback = generate_feedback(skill_comparison["missing_skills"], match_score)

            col1, col2 = st.columns(2)

            with col1:
                st.markdown("## Match Score")
                st.metric(label="Resume Match Percentage", value=f"{match_score}%")

                st.markdown("## Matched Skills")
                if skill_comparison["matched_skills"]:
                    st.write(", ".join(skill_comparison["matched_skills"]))
                else:
                    st.write("No matching skills found.")

            with col2:
                st.markdown("## Missing Skills")
                if skill_comparison["missing_skills"]:
                    st.write(", ".join(skill_comparison["missing_skills"]))
                else:
                    st.write("No major skill gaps detected.")

            st.markdown("## Recommended Roles")
            for role_data in role_recommendations:
                st.write(
                    f"**{role_data['role']}** — {role_data['score']}% match "
                    f"(Matched Skills: {', '.join(role_data['matched_skills']) if role_data['matched_skills'] else 'None'})"
                )

            st.markdown("## Resume Feedback")
            for item in feedback:
                st.write(item)

        else:
            st.info("Paste a job description to calculate score and recommendations.")

    except Exception as e:
        st.error(f"Error: {e}")
