import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import json

load_dotenv() ## load all our environment variables

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input):
    model = genai.GenerativeModel("models/gemini-2.5-flash")
    response = model.generate_content(input)
    return response.text

def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)

    number_of_pages = len(reader.pages)

    text = ""
    for page in reader.pages:
        text += str(page.extract_text())

    return text, number_of_pages

#Prompt Template

input_prompt="""
Hey Act Like a skilled or very experience ATS(Application Tracking System)
with a deep understanding of tech field, software engineering, data science,
data analyst and big data engineer.

Your task is to evaluate the resume based on the given job description.

resume:{text}

description:{jd}

Return ONLY valid JSON in the following format:

{{
  "Resume Match Score": "85%",
  "MissingKeywords": ["Python","AWS"],
  "Profile Summary": [
    "Point 1",
    "Point 2",
    "Point 3",
    "Point 4",
    "Point 5"
  ]
}}

Profile Summary must contain 5-6 points.
Each point should be short and on a separate line.
Do not return markdown.
Return only JSON.
"""

## streamlit app

with st.sidebar:
    st.title("Resume Analyzer")
    st.subheader("About")
    st.write("This sophisticated ATS project, developed with Gemini Pro and Streamlit, seamlessly incorporates advanced features including resume match percentage, keyword analysis to identify missing criteria, and the generation of comprehensive profile summaries, enhancing the efficiency and precision of the candidate evaluation process for discerning talent acquisition professionals.")
    
    st.markdown("""
    - [Streamlit](https://streamlit.io/)
    - [Gemini Pro](https://deepmind.google/technologies/gemini/#introduction)
    - [makersuit API Key](https://makersuite.google.com/)
                
    """)
    
    add_vertical_space(5)
    st.write("Made with ❤ by Nakul.")
    
    


st.title("Smart Application Tracking System")
st.text("Improve Your Resume ATS")
jd=st.text_area("Paste the Job Description")
uploaded_file=st.file_uploader("Upload Your Resume",type="pdf",help="Please uplaod the pdf")

submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        text, number_of_pages = input_pdf_text(uploaded_file)

        final_prompt = input_prompt.format(
            text=text,
            jd=jd
        )

        response = get_gemini_response(final_prompt)

        try:
            response_json = json.loads(response)

            st.subheader("📊 ATS Analysis")

            match_score = response_json.get("Resume Match Score", "0%")
            score = int(match_score.replace("%", ""))

            st.metric("🎯 ATS Match Score", match_score)
            st.progress(score)
            
            st.metric("📄 Resume Pages", number_of_pages)

            if number_of_pages <= 2:
                st.success("✅ Resume length is ATS friendly")
            else:
                st.warning("⚠ Resume is longer than 2 pages")

            st.markdown("### 🔍 Missing Keywords")
            st.warning(
                ", ".join(response_json.get("MissingKeywords", []))
            )

            st.markdown("### 📝 Profile Summary")
            st.success(
                response_json.get("Profile Summary", "")
            )

        except Exception:
            st.write(response)