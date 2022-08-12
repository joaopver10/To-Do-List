from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import Tarefa
from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as lg
from .forms import CadastroModelTarefa



@login_required(login_url="login")
def index(request):
    tasks = Tarefa.objects.filter(usuario_id=request.user)

    if str(request.method) == 'POST':
        form = CadastroModelTarefa(request.POST)
        if form.is_valid():
            vincula = form.save(commit=False)
            vincula.usuario = request.user
            vincula.save()

    return render(request, 'index.html',{'tasks': tasks})

def contato(request):
    return  render(request, 'contato.html')


def cadastro(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(username=username, email=email).first()

        if user:
            messages.error(request, 'Já existe uma conta com esse email',
                           extra_tags='cad')
            return redirect('cadastro')

        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()
        messages.success(request, 'Usuário cadastrado com sucesso.', extra_tags='cad')

    return render(request, 'cadastro.html')


def login(request):
    if request.method == 'POST':
        try:
            email = request.POST['email']
            username = User.objects.get(email=email).username
            senha = request.POST['senha']
            user = authenticate(request, username=username, password=senha)
            if user:
                lg(request, user)
                return redirect('index')
        except:
            messages.error(request, 'Email ou senha inválida', extra_tags='login')
            return redirect('login')

    return render(request, 'login.html')


def deletar(request, id):
    task = get_object_or_404(Tarefa, pk=id)
    task.delete()
    return HttpResponseRedirect('/')


def sair(request):
    logout(request)
    return HttpResponseRedirect('login')




