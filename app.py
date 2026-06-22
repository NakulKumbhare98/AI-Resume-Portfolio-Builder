import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# =========================
# CONFIGURATION
# =========================

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

st.set_page_config(
    page_title="AI Resume & Portfolio Builder",
    page_icon="🚀",
    layout="wide"
)

# =========================
# GEMINI FUNCTION
# =========================

def get_gemini_response(prompt):
    try:
        model = genai.GenerativeModel("models/gemini-2.5-flash")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# =========================
# SIDEBAR
# =========================

with st.sidebar:
    st.title("🚀 AI Resume Builder")

    st.markdown("""
### Features

 ATS Resume Generator

 Cover Letter Generator

 Portfolio Generator

 ATS Match Analysis

 Interview Question Generator

 Job Description Based Optimization

---

Built with:

- Streamlit
- Google Gemini Flash
- Python

Made with ❤️ by Nakul
""")

# =========================
# MAIN TITLE
# =========================

st.title("🚀 AI Resume & Portfolio Builder")

st.write(
    "Generate ATS-Friendly Resume, Cover Letter, Portfolio and Interview Questions using AI."
)

st.divider()

# =========================
# PERSONAL INFORMATION
# =========================

st.header("👤 Personal Information")

col1, col2 = st.columns(2)

with col1:
    name = st.text_input("Full Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")

with col2:
    linkedin = st.text_input("LinkedIn URL")
    github = st.text_input("GitHub URL")
    location = st.text_input("Location")

# =========================
# EDUCATION
# =========================

st.header("🎓 Education")

education = st.text_area(
    "Education Details",
    height=150,
    placeholder="""
B.Tech Information Technology
Priyadarshini College of Engineering
CGPA: 8.2
2023 - 2027
"""
)

# =========================
# SKILLS
# =========================

st.header("💻 Skills")

skills = st.text_area(
    "Skills",
    height=150,
    placeholder="""
Python
Java
JavaScript
HTML
CSS
React
Node.js
MongoDB
Machine Learning
"""
)



# =========================
# JOB DESCRIPTION
# =========================

st.header("🎯 Job Description")

jd = st.text_area(
    "Paste Job Description",
    height=250
)

# =========================
# BUILD STUDENT PROFILE
# =========================

student_data = f"""
Name: {name}
Email: {email}
Phone: {phone}
Location: {location}

LinkedIn: {linkedin}
GitHub: {github}

Education:
{education}

Skills:
{skills}


"""

# =========================
# BUTTONS
# =========================

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    generate_resume = st.button("📄 Resume")

with col2:
    generate_cover = st.button("✉ Cover Letter")

with col3:
    generate_portfolio = st.button("🌐 Portfolio")

with col4:
    generate_analysis = st.button("📊 ATS Analysis")

with col5:
    generate_interview = st.button("🎤 Interview Prep")

# =========================
# RESUME GENERATOR
# =========================

if generate_resume:

    with st.spinner("Generating ATS Resume..."):

        prompt = f"""
Act as a Professional Resume Writer and ATS Expert.

Create a highly professional ATS-friendly resume.

Student Information:

{student_data}

Job Description:

{jd}

Requirements:

1. Professional Summary
2. Technical Skills
3. Education
4. Projects
5. Experience
6. Certifications
7. Achievements
8. ATS Optimized Keywords
9. Professional Formatting

Return only the resume.
"""

        resume = get_gemini_response(prompt)

        st.subheader("📄 Generated ATS Resume")

        st.markdown(resume)

        st.download_button(
            "⬇ Download Resume",
            resume,
            file_name="ATS_Resume.txt",
            mime="text/plain"
        )

# =========================
# COVER LETTER
# =========================

if generate_cover:

    with st.spinner("Generating Cover Letter..."):

        prompt = f"""
Act as a Professional HR Manager.

Generate a professional cover letter.

Student Information:

{student_data}

Job Description:

{jd}

Requirements:

- Formal
- Professional
- Personalized
- Job Specific

Return only cover letter.
"""

        cover_letter = get_gemini_response(prompt)

        st.subheader("✉ Cover Letter")

        st.markdown(cover_letter)

        st.download_button(
            "⬇ Download Cover Letter",
            cover_letter,
            file_name="Cover_Letter.txt",
            mime="text/plain"
        )

# =========================
# PORTFOLIO
# =========================

if generate_portfolio:

    with st.spinner("Generating Portfolio..."):

        prompt = f"""
Act as a Professional Portfolio Website Designer.

Create a complete personal portfolio.

Student Information:

{student_data}

Generate:

1. Hero Section
2. About Me
3. Skills
4. Experience
5. Projects
6. Education
7. Certifications
8. Achievements
9. Contact Section

Return in Markdown format.
"""

        portfolio = get_gemini_response(prompt)

        st.subheader("🌐 Portfolio Content")

        st.markdown(portfolio)

        st.download_button(
            "⬇ Download Portfolio",
            portfolio,
            file_name="Portfolio.md",
            mime="text/markdown"
        )

# =========================
# ATS ANALYSIS
# =========================

if generate_analysis:

    with st.spinner("Analyzing Profile..."):

        prompt = f"""
Act as an ATS System.

Student Information:

{student_data}

Job Description:

{jd}

Analyze:

1. ATS Match Score %
2. Missing Keywords
3. Strengths
4. Weaknesses
5. Improvement Suggestions
6. Recommended Skills

Return professional report.
"""

        analysis = get_gemini_response(prompt)

        st.subheader("📊 ATS Analysis")

        st.markdown(analysis)

# =========================
# INTERVIEW QUESTIONS
# =========================

if generate_interview:

    with st.spinner("Generating Interview Questions..."):

        prompt = f"""
Act as a Senior Technical Interviewer.

Student Information:

{student_data}

Job Description:

{jd}

Generate:

1. Technical Questions
2. HR Questions
3. Project Questions
4. Behavioral Questions
5. Scenario Based Questions

Provide answers and tips.

Return detailed interview preparation guide.
"""

        interview = get_gemini_response(prompt)

        st.subheader("🎤 Interview Preparation")

        st.markdown(interview)

        st.download_button(
            "⬇ Download Interview Guide",
            interview,
            file_name="Interview_Preparation.txt",
            mime="text/plain"
        )

