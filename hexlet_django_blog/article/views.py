from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class IndexView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'article/index.html', context={
        'test': 'Yes, its working!',
    })


def index(request, tags, article_id):
    response_text = f"Статья номер {article_id}. Тег {tags}"
    return HttpResponse(response_text)
