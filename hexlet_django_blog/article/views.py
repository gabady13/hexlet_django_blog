from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class IndexView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'article/index.html', context={
        'test': 'Yes, its working!',
    })


def index(request):
    return render(request, 'article/index.html', context={
        'test': 'article',
    })
