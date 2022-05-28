
from django.urls import path

from .views import index, inicio, login, deletar


urlpatterns = [
    path('', index, name='index'),
    path('inicio/', inicio ,name='inicio'),
    path('login', login, name='login'),
    path('deletar/<int:id>/', deletar, name='deletar'),

]