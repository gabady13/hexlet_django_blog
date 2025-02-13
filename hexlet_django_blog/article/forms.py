from django import forms # Импортируем формы Django
from django.db import models
from django.forms import ModelForm
from .models import Article

class CommentArticleForm(forms.Form):
    content = forms.CharField(label='Комментарий', max_length=200)


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'body']
