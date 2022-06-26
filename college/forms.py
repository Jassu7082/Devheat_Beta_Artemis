from django import forms
from .models import ExamQp, result

class ExamForm(forms.ModelForm):
    class Meta:
        model = ExamQp
        fields = {'examName', 'pdf', 'date'}

class ResultForm(forms.ModelForm):
    class Meta:
        model = result
        fields = {'examName', 'pdf'}