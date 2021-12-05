from django.urls import path

from .views import Calculator, get_calculation

app_name = 'calcapp'

urlpatterns = [
    path('calculate/', Calculator.as_view(), name='calculate'),
    path('get_calculation/', get_calculation, name='get_calculation'),
]
