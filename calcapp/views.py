from django.shortcuts import render
from django.views.generic import View


class Calculator(View):
    """ CBV Главной страницы """
    template_name = 'calcapp/calculate.html'
    extra_context = {'title': 'Стоимость'}

    def get(self, request):
        context = {
        }
        return render(request, self.template_name, context)
