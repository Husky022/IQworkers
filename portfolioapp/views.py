from django.shortcuts import render
from django.views.generic import View


class Objects(View):
    """ CBV Главной страницы """
    template_name = 'portfolioapp/objects.html'
    extra_context = {'title': 'Объекты'}

    def get(self, request):
        context = {
        }
        return render(request, self.template_name, context)


class ObjectPage(View):
    """ CBV Главной страницы """
    template_name = 'portfolioapp/objectepage.html'
    extra_context = {'title': 'Объект'}

    def get(self, request):
        context = {
        }
        return render(request, self.template_name, context)
