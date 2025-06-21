from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime
import os

def generate_match_report(resume_text, jd_text, score, output_path):
    c = canvas.Canvas(output_path, pagesize=A4)
    width, height = A4

    # Title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 50, "Resume–Job Match Report")

    # Date
    c.setFont("Helvetica", 10)
    c.drawString(50, height - 70, f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # Match Score
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, height - 100, f"Match Score: {score}%")

    # Resume Summary
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, height - 130, "Resume Summary:")
    c.setFont("Helvetica", 10)
    c.drawString(50, height - 145, resume_text[:300].replace('\n', ' '))  # Show first 300 chars

    # JD Summary
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, height - 180, "Job Description Summary:")
    c.setFont("Helvetica", 10)
    c.drawString(50, height - 195, jd_text[:300].replace('\n', ' '))  # Show first 300 chars

    # Footer
    c.setFont("Helvetica-Oblique", 8)
    c.drawString(50, 40, "This is an AI-generated match report for educational/demo purposes.")

    c.save()
    


