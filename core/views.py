from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import Usuario
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as lg


@login_required(login_url="login")
def index(request):
    return render(request, 'index.html')


def cadastro(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = Usuario.objects.filter(username=username, email=email).first()

        if user:
            messages.error(request, 'Já existe uma conta com esse email',
                           extra_tags='cad')
            return redirect('cadastro')

        user = Usuario.objects.create_user(username=username, email=email, password=senha)
        user.save()
        messages.success(request, 'Usuário cadastrado com sucesso.', extra_tags='cad')

    return render(request, 'cadastro.html')


def login(request):
    if request.method == 'POST':
        try:
            email = request.POST['email']
            username = Usuario.objects.get(email=email).username
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
    pass





