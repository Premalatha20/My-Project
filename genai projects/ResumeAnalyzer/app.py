import streamlit as st
from utils import extract_text_from_pdf, calculate_score, suggest_improvements, rewrite_bullets

st.title("📄 AI Resume Analyzer & Improver")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

if uploaded_file:
    text = extract_text_from_pdf(uploaded_file)

    st.subheader("📊 Resume Score")
    score = calculate_score(text)
    st.progress(score)
    st.write(f"Your Resume Score: {score}/100")

    st.subheader("💡 Suggestions")
    suggestions = suggest_improvements(text)
    
    if suggestions:
        for s in suggestions:
            st.write("•", s)
    else:
        st.success("Your resume looks good!")

    st.subheader("✍ Improved Bullet Points")
    improved = rewrite_bullets(text)

    for point in improved:
        st.write(point)