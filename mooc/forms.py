#coding:utf-8
from django import forms
from models import ScoreChoice
class ScoreForm(forms.Form):
    score = forms.CharField(max_length=2,widget=forms.Select(choices=ScoreChoice))

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()