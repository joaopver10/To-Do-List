from django import forms as fm
from .models import Tarefa


class CadastroModelTarefa(fm.ModelForm):
    class Meta:
        model = Tarefa
        fields = ['tarefa']