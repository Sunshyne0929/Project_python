from django import forms

class ExamImageForm(forms.Form):
    exam_image = forms.ImageField()
