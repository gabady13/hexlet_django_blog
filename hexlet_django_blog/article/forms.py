from django import forms # Импортируем формы Django
from django.db import models
from django.forms import ModelForm

class CommentArticleForm(forms.Form):
    content = forms.CharField(label='Комментарий', max_length=200)
