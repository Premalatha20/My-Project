import PyPDF2

def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()
    return text


def calculate_score(text):
    score = 0
    text = text.lower()

    keywords = ["education", "skills", "project", "internship", "experience"]

    for word in keywords:
        if word in text:
            score += 20

    if len(text) > 1000:
        score += 10

    return min(score, 100)


def suggest_improvements(text):
    suggestions = []
    text = text.lower()

    if "objective" not in text:
        suggestions.append("Add career objective section.")
    if "project" not in text:
        suggestions.append("Add at least one project.")
    if "skills" not in text:
        suggestions.append("Mention technical skills clearly.")
    if len(text) < 800:
        suggestions.append("Resume content is too short.")

    return suggestions


def rewrite_bullets(text):
    lines = text.split("\n")
    improved = []

    for line in lines:
        if len(line.strip()) > 20:
            improved.append("✔ Successfully worked on: " + line.strip())

    return improved[:5]