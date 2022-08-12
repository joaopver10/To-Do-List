
from django.urls import path

from .views import index, login, deletar, cadastro, sair, contato


urlpatterns = [
    path('', index, name='index'),
    path('login', login, name='login'),
    path('contato', contato, name='contato'),
    path('cadastro', cadastro, name='cadastro'),
    path('deletar/<int:id>/', deletar, name='deletar'),
    path('deslogar', sair, name='sair')
]