from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
from pkg_resources import require

from .models import Usuario, Tarefa


from django.contrib import messages

from .forms import CadastroModelForm, CadastroModelTarefa


def index(request):
    if request.method == 'POST':
        form = CadastroModelForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, 'Cadastro feito com sucesso!')
            form = CadastroModelForm()
        else:
            messages.error(request, "Erro ao se cadastrar")
    else:
        form = CadastroModelForm()


    context = {
        'form': form
    }
    return render(request, 'index.html', context)

@csrf_exempt
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']

        print(email, senha)
        user = Usuario.objects.filter(email=email, senha=senha).first()
        print(user)


        if user is not None:
            return HttpResponseRedirect('/inicio/')

    return HttpResponseRedirect('/')


def deletar(request, id):
    task = get_object_or_404(Tarefa, pk=id)
    task.delete()
    return HttpResponseRedirect('/inicio/')


def inicio(request):
    tasks = Tarefa.objects.all()

    if str(request.method) == 'POST' :
        form = CadastroModelTarefa(request.POST)
        if form.is_valid():
            form.save()


    return render(request, 'inicio.html', {'tasks': tasks})
