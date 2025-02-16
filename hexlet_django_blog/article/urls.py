from django.urls import path
from hexlet_django_blog.article import views
from hexlet_django_blog.article.views import ArticleFormCreateView, IndexView, ArticleView, CommentArticleView, ArticleFormEditView

urlpatterns = [
    path('', IndexView.as_view(), name='article'),
    path('<int:id>/edit/', ArticleFormEditView.as_view(), name='articles_update'),
    path('<int:id>/', ArticleView.as_view()),
    path('forma/', CommentArticleView.as_view(), name = 'comment_create'),
    path('create/', ArticleFormCreateView.as_view(), name='articles_create'),
]
