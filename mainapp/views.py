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


class Services(View):
    """ CBV Главной страницы """
    template_name = 'mainapp/services.html'
    extra_context = {'title': 'Услуги'}

    def get(self, request):
        context = {
        }
        return render(request, self.template_name, context)


class Contacts(View):
    """ CBV Главной страницы """
    template_name = 'mainapp/contacts.html'
    extra_context = {'title': 'Контакты'}

    def get(self, request):
        context = {
        }
        return render(request, self.template_name, context)


class Command(View):
    """ CBV Главной страницы """
    template_name = 'mainapp/command.html'
    extra_context = {'title': 'Команда'}

    def get(self, request):
        context = {
        }
        return render(request, self.template_name, context)
