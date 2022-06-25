from django import forms
from .models import ExamUpl

class ExamForm2(forms.ModelForm):
    class Meta:
        model = ExamUpl
        fields = {'examCode', 'pdf'}