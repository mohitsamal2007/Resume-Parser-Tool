
import re
import pdfplumber
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# -----------------------------------
# PAGE TITLE
# -----------------------------------

st.set_page_config(page_title="AI Resume Parser")

st.title("AI Resume Parser")


# -----------------------------------
# PDF TEXT EXTRACTION
# -----------------------------------

def extract_text_from_pdf(pdf_file):

    text = ""

    with pdfplumber.open(pdf_file) as pdf:

        for page in pdf.pages:

            extracted = page.extract_text()

            if extracted:
                text += extracted

    return text


# -----------------------------------
# SKILLS LIST
# -----------------------------------

skills_list = [
    "python",
    "java",
    "c",
    "c++",
    "machine learning",
    "deep learning",
    "sql",
    "html",
    "css",
    "javascript",
    "react",
    "nodejs",
    "data science",
    "nlp",
    "flask",
    "django"
]


# -----------------------------------
# SKILL EXTRACTION
# -----------------------------------

def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in skills_list:

        if skill.lower() in text:
            found_skills.append(skill)

    return found_skills


# -----------------------------------
# FILE UPLOAD
# -----------------------------------

uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)


# -----------------------------------
# PROCESS RESUME
# -----------------------------------

if uploaded_file is not None:

    # Extract Text
    resume_text = extract_text_from_pdf(uploaded_file)

    st.subheader("Resume Text")

    st.text_area(
        "Resume Content",
        resume_text[:3000],
        height=250
    )


    # -----------------------------------
    # EMAIL EXTRACTION
    # -----------------------------------

    email = re.findall(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}",
        resume_text
    )


    # -----------------------------------
    # PHONE EXTRACTION
    # -----------------------------------

    phone = re.findall(
        r"\+?\d[\d -]{8,12}\d",
        resume_text
    )


    # -----------------------------------
    # SKILL EXTRACTION
    # -----------------------------------

    skills = extract_skills(resume_text)


    # -----------------------------------
    # JOB DESCRIPTION
    # -----------------------------------

    job_description = """
    We are looking for a Python Developer with knowledge of
    Machine Learning, SQL, Flask, and Data Science.
    """


    # -----------------------------------
    # MATCH SCORE
    # -----------------------------------

    documents = [resume_text, job_description]

    tfidf = TfidfVectorizer()

    matrix = tfidf.fit_transform(documents)

    similarity = cosine_similarity(
        matrix[0:1],
        matrix[1:2]
    )

    score = similarity[0][0] * 100


    # -----------------------------------
    # DISPLAY INFORMATION
    # -----------------------------------

    st.subheader("Extracted Information")

    st.write(
        "Email:",
        email[0] if len(email) > 0 else "Not Found"
    )

    st.write(
        "Phone:",
        phone[0] if len(phone) > 0 else "Not Found"
    )

    st.write("Skills:", skills)

    st.write(f"Resume Match Score: {score:.2f}%")


    # -----------------------------------
    # RATING
    # -----------------------------------

    if score >= 80:

        st.success("Excellent Match")

    elif score >= 60:

        st.info("Good Match")

    elif score >= 40:

        st.warning("Average Match")

    else:

        st.error("Poor Match")


    # -----------------------------------
    # DATAFRAME
    # -----------------------------------

    df = pd.DataFrame({

        "Email": [
            email[0] if len(email) > 0 else "Not Found"
        ],

        "Phone": [
            phone[0] if len(phone) > 0 else "Not Found"
        ],

        "Skills": [
            ", ".join(skills)
        ],

        "Match Score": [
            score
        ]
    })

    st.subheader("Candidate Data")

    st.dataframe(df)


    # -----------------------------------
    # DOWNLOAD CSV
    # -----------------------------------

    csv = df.to_csv(index=False)

    st.download_button(
        label="Download CSV",
        data=csv,
        file_name="parsed_resume.csv",
        mime="text/csv"
    )


    # -----------------------------------
    # VISUALIZATION
    # -----------------------------------

    st.subheader("Resume Score Visualization")

    fig, ax = plt.subplots(figsize=(5, 4))

    ax.bar(["Candidate"], [score])

    ax.set_ylabel("Match Score")

    ax.set_title("Resume Matching Score")

    st.pyplot(fig)


# -----------------------------------
# FOOTER
# -----------------------------------

st.markdown("---")

st.write("Resume Parser Project using Streamlit")
