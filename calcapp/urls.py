from django.urls import path

from .views import Calculator

app_name = 'calcapp'

urlpatterns = [
    path('calculate/', Calculator.as_view(), name='calculate')
]
