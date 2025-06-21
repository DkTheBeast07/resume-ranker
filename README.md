# 🧠 AI Resume Ranker – Django + NLP Project

An intelligent web application that analyzes how well a resume matches a job description using Natural Language Processing (NLP). Built with Python and Django, this project extracts skills, computes match percentages, and generates downloadable PDF reports.

---

## 🚀 Key Features

- 📄 **Multi-format Upload**: Upload resumes and JDs in PDF, DOCX, or TXT format.
- 🧠 **NLP Matching**: Calculates match score using TF-IDF & cosine similarity.
- 🔍 **Skill Extraction**: Uses spaCy to identify and compare key skills.
- 📊 **Match Score Report**: Generates a professional PDF summary.
- 🌐 **Built with Django**: Scalable, web-ready architecture.
- 📁 **Media Handling**: Handles file uploads and static content seamlessly.

---

## 📌 Technologies Used

| Tool/Library     | Purpose                            |
|------------------|------------------------------------|
| Python, Django   | Backend and web framework          |
| scikit-learn     | TF-IDF, Cosine Similarity (NLP)    |
| spaCy            | Skill extraction                   |
| PyMuPDF, python-docx | File text extraction (PDF/DOCX) |
| ReportLab        | PDF report generation              |
| HTML/CSS         | Frontend template (upload page)    |

---

## 🧠 How It Works (Simple Terms)

1. User uploads a resume and job description.
2. System extracts text from both documents.
3. NLP is used to:
   - Calculate a match score based on similarity
   - Extract and match key skills
4. A downloadable PDF report is generated.
5. The user sees a summary on the web page.

---

## 📸 Screenshot (Coming Soon)

> Add a screenshot showing file upload + score + matched skills

---

## 💻 Setup Instructions (Run Locally)

```bash
git clone https://github.com/DkTheBeast07/resume-ranker.git
cd resume-ranker
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py runserver
