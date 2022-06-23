
from django.urls import path

from .views import index, login, deletar, cadastro, sair


urlpatterns = [
    path('', index, name='index'),
    path('login', login, name='login'),
    path('cadastro', cadastro, name='cadastro'),
    path('deletar/<int:id>/', deletar, name='deletar'),
    path('deslogar', sair, name='sair')
]