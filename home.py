import streamlit as st
from setStyles import set_styles

# Page setup with collapsible sidebar
st.set_page_config(page_title="Career Assistant", layout="wide", initial_sidebar_state="collapsed")

# Initialize navigation state
if "page" not in st.session_state:
    st.session_state.page = "Home"

# Sidebar navigation
with st.sidebar:
    st.title("🔍 Career Tools")
    choice = st.radio("Choose a page", ["Home", "Resume Scorer", "Job Finder"], index=["Home", "Resume Scorer", "Job Finder"].index(st.session_state.page))
    if choice != st.session_state.page:
        st.session_state.page = choice
        st.rerun()

# Main content
if st.session_state.page == "Home":
    # set_styles("Background_Image.jpg")

    st.title("🏆 Welcome to Career Assistant")
    st.markdown("Boost your career with smart tools:")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🧠 Resume Scorer")
        st.markdown("Check how well your resume matches a job description.")
        if st.button("🔗 Go to Resume Scorer"):
            st.session_state.page = "Resume Scorer"
            st.rerun()

    with col2:
        st.markdown("### 💼 Job Finder")
        st.markdown("Upload your resume to find matching jobs.")
        if st.button("🔗 Go to Job Finder"):
            st.session_state.page = "Job Finder"
            st.rerun()

# Routing logic
if st.session_state.page == "Resume Scorer":
    import resumeScorer
    resumeScorer.run()
elif st.session_state.page == "Job Finder":
    import jobFinder
    jobFinder.run()
