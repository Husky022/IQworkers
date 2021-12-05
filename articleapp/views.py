from django.shortcuts import render
from django.views.generic import View


class Articles(View):
    """ CBV Главной страницы """
    template_name = 'articleapp/articles.html'
    extra_context = {'title': 'Статьи'}

    def get(self, request):
        context = {
        }
        return render(request, self.template_name, context)


class ArticlePage(View):
    """ CBV Главной страницы """
    template_name = 'articleapp/articlepage.html'
    extra_context = {'title': 'Статья'}

    def get(self, request):
        context = {
        }
        return render(request, self.template_name, context)
