import streamlit as st
from getScore import get_similarity_score
from getResumeText import extract_resume_text

# Streamlit UI
st.title("🧠 Resume Scoring App")
st.write("Upload your resume and paste a job description to see how well they match.")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
job_desc = st.text_area("Paste Job Description")

if uploaded_file and job_desc:
    if st.button("Get Score"):
        with st.spinner("Analyzing..."):
            resume_text = extract_resume_text(uploaded_file)
            score = int(get_similarity_score(resume_text, job_desc).strip('*'))

        st.success(f"✅ Resume Match Score: **{score}/100**")

        if score > 75:
            st.info("🟢 Strong match! Great job aligning your resume.")
        elif score > 50:
            st.warning("🟡 Decent match. You may want to tweak a few sections.")
        else:
            st.error("🔴 Low match. Consider tailoring your resume more to this job.")
else:
    st.button("Get Score", disabled=True)