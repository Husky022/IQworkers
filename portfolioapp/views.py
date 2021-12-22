from django.shortcuts import render
from django.views.generic import View, ListView
from portfolioapp.models import PortfolioObject, PortfolioImage


class Objects(ListView):
    """ CBV Страницы с портфолио """

    model = PortfolioObject
    template_name = 'portfolioapp/objects.html'
    context_object_name = 'portfolio'
    extra_context = {
        'title': 'Портфолио'
    }



class ObjectPage(View):
    """ CBV Главной страницы """
    template_name = 'portfolioapp/objectepage.html'
    extra_context = {'title': 'Объект'}

    def get(self, request):
        context = {
        }
        return render(request, self.template_name, context)
