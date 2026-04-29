from django import forms

class UploadPDFForm(forms.Form):
    arquivo = forms.FileField()