from django import forms
from .models import Usuario, Tarefa

class CadastroModelForm(forms.ModelForm):
   class Meta:
       model = Usuario
       fields = ['nome', 'email', 'senha']


class CadastroModelTarefa(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ['descricao']