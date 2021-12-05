from django.urls import path


from .views import Articles, ArticlePage

app_name = 'articleapp'

urlpatterns = [
    path('articles/', Articles.as_view(), name='articles'),
    path('articlepage/<int:pk>/', ArticlePage.as_view(), name='articlepage'),
]
