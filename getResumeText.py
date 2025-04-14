from langchain_community.document_loaders import PyPDFLoader

def extract_resume_text(uploaded_file):
    with open("temp_resume.pdf", "wb") as f:
        f.write(uploaded_file.read())
    loader = PyPDFLoader("temp_resume.pdf")
    pages = loader.load()
    return " ".join([page.page_content for page in pages])

