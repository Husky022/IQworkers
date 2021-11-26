from django.shortcuts import render
from django.views.generic import View


class Main(View):
    """ CBV Главной страницы """
    template_name = 'mainapp/index.html'
    extra_context = {'title': 'Главная'}

    def get(self, request):
        context = {
        }
        return render(request, self.template_name, context)
