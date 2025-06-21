from django import forms

class UploadFileForm(forms.Form):
    resume = forms.FileField(label="Upload Resume")
    jd     = forms.FileField(label="Upload Job Description")
