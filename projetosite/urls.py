from django.urls import path
from projetosite.views import home, contato, sobre

urlpatterns = [
    path('', home),
    path('sobre/', sobre),
    path('contato/', contato),
]
