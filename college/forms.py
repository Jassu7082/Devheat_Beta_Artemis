from django import forms
from .models import ExamQp

class ExamForm(forms.ModelForm):
    class Meta:
        model = ExamQp
        fields = {'examName', 'pdf', 'date'}