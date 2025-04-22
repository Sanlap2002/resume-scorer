import streamlit as st
import re
from setStyles import set_styles
from getResult import get_result
from getResumeText import extract_resume_text

def run():
    set_styles("Background_Image.jpg")

    def extract_number(text, fallback=0):
        match = re.search(r'\d+', text)
        return int(match.group()) if match else fallback

    # --- Resume Scoring App UI ---
    st.title("🧠 Resume Scorer")
    st.write("Upload your resume and paste a job description to see how well they match.")

    uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
    job_desc = st.text_area("Paste Job Description")

    if uploaded_file and job_desc:
        resume_text = extract_resume_text(uploaded_file)
        
        # Track changes to resume file and job description
        if "prev_file" not in st.session_state:
            st.session_state.prev_file = None
        if "prev_job_desc" not in st.session_state:
            st.session_state.prev_job_desc = ""

        # If file or job desc has changed, reset the score
        if uploaded_file != st.session_state.prev_file or job_desc != st.session_state.prev_job_desc:
            st.session_state.pop("score", None)
            st.session_state.pop("show_improvements", None)

        # Update the tracked values
        st.session_state.prev_file = uploaded_file
        st.session_state.prev_job_desc = job_desc

        if st.button("Get Score"):
            with st.spinner("Analyzing..."):
                raw_score = get_result("score", resume_text, job_desc)
                score = extract_number(raw_score, fallback=0)
                st.session_state.score = score
                st.session_state.resume_text = resume_text
                st.session_state.job_desc = job_desc
                st.session_state.show_improvements = False  # reset improvements state

        if "score" in st.session_state:
            score = st.session_state.score
            st.success(f"✅ Resume Match Score: **{score}/100**")

            if score > 75:
                st.info("🟢 Strong match! Great job aligning your resume.")
            elif score > 50:
                st.warning("🟡 Decent match. You may want to tweak a few sections.")

                if st.button("Get Improvements"):
                    st.session_state.show_improvements = True

            else:
                st.error("🔴 Low match. Consider tailoring your resume more to this job.")

                if st.button("Get Improvements"):
                    st.session_state.show_improvements = True

            if st.session_state.get("show_improvements", False):
                with st.spinner("Fetching Improvements..."):
                    improvements = get_result("improvements", st.session_state.resume_text, st.session_state.job_desc)
                    st.markdown(improvements)
    else:
        st.button("Get Score", disabled=True)
