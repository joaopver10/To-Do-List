from django.contrib import admin
from .models import Tarefa

class TarefasAdmin(admin.ModelAdmin):
    list_display = ('id','tarefa','usuario', 'usuario_id')


admin.site.register(Tarefa, TarefasAdmin)

