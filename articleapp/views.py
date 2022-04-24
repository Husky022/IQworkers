from django.shortcuts import render
from django.views.generic import View, ListView
from articleapp.models import Article
from mainapp.forms import AppForm

appform = AppForm()


class Articles(ListView):
    """ CBV Страницы со статьями """
    model = Article
    template_name = 'articleapp/articles.html'
    context_object_name = 'articles'
    extra_context = {
        'title': 'Статьи',
        'appform': appform
    }


class ArticlePage(View):
    """ CBV Страницы статьи """
    template_name = 'articleapp/articlepage.html'
    extra_context = {'title': 'Статья'}

    def get(self, request, pk):
        article = Article.objects.filter(id=pk).first()
        context = {
            'title': 'Статья',
            'article': article,
            'appform': appform
        }
        return render(request, self.template_name, context)
