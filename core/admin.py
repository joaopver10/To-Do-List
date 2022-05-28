from django.contrib import admin
from .models import Usuario, Tarefa


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'senha', 'criado', 'modificado', 'ativo')



admin.site.register(Tarefa)