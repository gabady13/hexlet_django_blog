from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import View
from .forms import CommentArticleForm
from hexlet_django_blog.article.models import Article, Comment


class IndexView(View):

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'article/index.html', context={
        'articles': articles,
    })


def index(request, tags, article_id):
    response_text = f"Статья номер {article_id}. Тег {tags}"
    return HttpResponse(response_text)


class ArticleView(View):

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, 'article/show.html', context={
            'article': article,
        })


class CommentArticleView(View):
    # если метод POST, то мы обрабатываем данные
    def post(self, request, *args, **kwargs):
        form = CommentArticleForm(request.POST) # Получаем данные формы из запроса
        if form.is_valid(): # Проверяем данные формы на корректность
            comment = Comment(
                name = form.cleaned_data['content'], # Получаем очищенные данные из поля content
                ) #  и создаем новый комментарий
            comment.save()

    # если метод GET, то создаем пустую форму
    def get(self, request, *args, **kwargs):
        form = CommentArticleForm() # Создаем экземпляр нашей формы
        return render(request, 'article/comment.html', {'form': form}) 
