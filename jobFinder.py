import streamlit as st
from getResumeText import extract_resume_text
from searchJobs import search_jobs
from getResult import get_result
from setStyles import set_styles

def run():
    set_styles("Background_Image.jpg")
    st.title("📄 Resume-Based Job Finder")

    uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

    if uploaded_file:
        resume_text = extract_resume_text(uploaded_file)
        st.subheader("🔍 Extracted Resume Text Preview")
        st.text_area("Resume Content", resume_text, height=200)

        if "keywords" not in st.session_state:
            st.session_state.keywords = ""

        if st.button("Extract Keywords"):
            with st.spinner("Extracting Keywords..."):
                keywords = get_result("keywords", resume_text, "")
                st.session_state.keywords = keywords  # Store in session

        if st.session_state.keywords:
            st.write(f"✅ Extracted Keywords for Job Search: `{st.session_state.keywords}`")

            if st.button("Search Jobs"):
                jobs = search_jobs(st.session_state.keywords)
                st.subheader("💼 Matching Jobs")

                if not jobs:
                    st.warning("No jobs found.")
                else:
                    for job in jobs:
                        st.markdown(f"**{job['title']}** at *{job['company']['display_name']}*")
                        st.markdown(f"📍 {job.get('location', {}).get('display_name', 'N/A')}")
                        st.markdown(f"🔗 [View Job Posting]({job['redirect_url']})")
                        st.markdown("---")
