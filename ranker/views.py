from .skill_matcher import get_matched_skills 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from django.shortcuts import render
from .forms import UploadFileForm
from django.conf import settings
import os
from .pdf_report import generate_match_report

from .text_extractor import extract_text_from_pdf, extract_text_from_docx, extract_text_from_txt

def save_file(file, folder):
    path = os.path.join(settings.MEDIA_ROOT, folder)
    os.makedirs(path, exist_ok=True)
    with open(os.path.join(path, file.name), 'wb+') as f:
        for chunk in file.chunks():
            f.write(chunk)


def extract_text(file_path):
    if file_path.endswith('.pdf'):
        return extract_text_from_pdf(file_path)
    elif file_path.endswith('.docx'):
        return extract_text_from_docx(file_path)
    elif file_path.endswith('.txt'):
        return extract_text_from_txt(file_path)
    else:
        return "Unsupported file type"

def upload_view(request):
    form = UploadFileForm(request.POST or None, request.FILES or None)
    context = {'form': form, 'message': ''}
    
    if request.method == 'POST' and form.is_valid():
        resume_file = request.FILES['resume']
        jd_file = request.FILES['jd']

        # Save files
        save_file(resume_file, 'resumes')
        save_file(jd_file, 'jds')

        # Get saved paths
        resume_path = os.path.join(settings.MEDIA_ROOT, 'resumes', resume_file.name)
        jd_path = os.path.join(settings.MEDIA_ROOT, 'jds', jd_file.name)

        # Extract text
        resume_text = extract_text(resume_path)
        jd_text = extract_text(jd_path)
        
                # ✅ Skill Matching
        matched_skills = get_matched_skills(resume_text, jd_text)
        context['matched_skills'] = matched_skills
        context['matched_count'] = len(matched_skills)

        # AI Match Score using TF-IDF and Cosine Similarity
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform([resume_text, jd_text])
        similarity_score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0] * 100
        similarity_score = round(similarity_score, 2)
        
        # After calculating the match score:
        # pdf report 
        report_path = os.path.join(settings.MEDIA_ROOT, 'reports')
        os.makedirs(report_path, exist_ok=True)

        # Get base names without extensions for cleaner PDF filename
        resume_base_name = os.path.splitext(resume_file.name)[0]
        jd_base_name = os.path.splitext(jd_file.name)[0]

        pdf_filename = f"match_report_{resume_base_name}_{jd_base_name}.pdf"
        pdf_path = os.path.join(report_path, pdf_filename)

        # Generate the PDF report
        generate_match_report(resume_text, jd_text, similarity_score, pdf_path)

        # Save the PDF path to use in the template
        context['report_url'] = f"{settings.MEDIA_URL}reports/{pdf_filename}"

        # Add results to context
        # Final results to context
        context['message'] = (
            f"Files uploaded and text extracted! | "
            f"Match Score: {similarity_score}% | "
            f"Matched Skills: {len(matched_skills)}"
        )
    return render(request, 'ranker/upload.html', context)

