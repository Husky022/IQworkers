from django.urls import path
import mainapp.views as mainapp

from .views import Main

app_name = 'mainapp'

urlpatterns = [
    path('', Main.as_view(), name='main')
]
