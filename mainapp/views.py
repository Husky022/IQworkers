from django.shortcuts import render
from django.views.generic import View


class Main(View):
    """ CBV Главной страницы """
    template_name = 'mainapp/index.html'

    def get(self, request):
        context = {
            'title': 'Главная'
        }
        return render(request, self.template_name, context)


class Services(View):
    """ CBV Главной страницы """
    template_name = 'mainapp/services.html'

    def get(self, request):
        context = {
            'title': 'Услуги'
        }
        return render(request, self.template_name, context)


class Contacts(View):
    """ CBV Главной страницы """
    template_name = 'mainapp/contacts.html'

    def get(self, request):
        context = {
            'title': 'Контакты'
        }
        return render(request, self.template_name, context)


class Command(View):
    """ CBV Главной страницы """
    template_name = 'mainapp/command.html'

    def get(self, request):
        context = {
            'title': 'Команда'
        }
        return render(request, self.template_name, context)


class Privacy(View):
    """ CBV страницы политики конфиденциальности """
    template_name = 'mainapp/privacy.html'

    def get(self, request):
        context = {
            'title': 'Приватность'
        }
        return render(request, self.template_name, context)
