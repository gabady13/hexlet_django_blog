from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from hexlet_django_blog.article.models import Article


class IndexView(View):

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'article/index.html', context={
        'articles': articles,
    })


def index(request, tags, article_id):
    response_text = f"Статья номер {article_id}. Тег {tags}"
    return HttpResponse(response_text)
