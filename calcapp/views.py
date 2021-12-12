from compat import JsonResponse, render_to_string
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import View

options = {
    'chk-light': 0.5,
    'chk-shutters': 0.5,
    'chk-ventilation': 0.5,
    'chk-condition': 0.5,
    'chk-warm-floors': 0.5,
    'chk-security': 0.5,
    'chk-outdoor-management': 0.5,
    'chk-voice-helpers': 0.5,
    'chk-flat': 0.5,
    'chk-house': 0.5,
    'chk-office': 0.5,
}



class Calculator(View):
    template_name = 'calcapp/calculate.html'
    extra_context = {'title': 'Стоимость'}

    def get(self, request):
        context = {
        }
        return render(request, self.template_name, context)

    def post(self, request):
        print(request.POST)


def get_calculation(request):
    if request.is_ajax():
        print(request.POST.dict())
        print(request.POST.dict()['checked'].split('&'))
        checkbox_dict = {}
        if request.POST.dict()['checked']:
            for item in request.POST.dict()['checked'].split('&'):
                item_parse = item.split('=')
                checkbox_dict.update({item_parse[1]: 'add'})
            print(checkbox_dict)

        base_ratio = 1


        project_price = '1'
        equipment_price = '2'
        montage_price = '3'
        programming_price = '4'
        result_price = project_price + equipment_price + montage_price + programming_price

        if not request.POST.dict()['square']:
            page = '<div id="calc-result" class="calc-result">' \
                   '<p>Укажите площадь объекта' \
                   '</div>'
            return JsonResponse({'result': page})

        page = '<div id="calc-result" class="calc-result">' \
               f'<p>Проектирование: {project_price} руб.' \
               f'<p>Оборудование: {equipment_price} руб.' \
               f'<p>Монтажные работы: {montage_price} руб.' \
               f'<p>Программирование: {programming_price} руб.' \
               f'<p>ИТОГО: {result_price} руб.' \
               '</div>'

        return JsonResponse({'result': page})
    return HttpResponseRedirect(reverse('mainapp:main'))


def reset_calculation(request):
    if request.is_ajax():
        return JsonResponse({'result': '200'})
    return HttpResponseRedirect(reverse('mainapp:main'))
