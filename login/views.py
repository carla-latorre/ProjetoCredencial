<<<<<<< HEAD
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
=======
from django.shortcuts import render
>>>>>>> 6fc9a8ee62cef2fd5ef5db37afcb608da0febef4
from criarConta.models import Funcionario
from buscaUsuario.views import buscaUsuario

#função para requisição do html
<<<<<<< HEAD
def loginview(request): 
=======
def login(request): 
  
>>>>>>> 6fc9a8ee62cef2fd5ef5db37afcb608da0febef4
    return render(request, 'login/login.html')


def buscaLogin(request):

    erros = {}
    context = {}

    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
<<<<<<< HEAD

        try:
            funcionario = Funcionario.objects.get(email=email) 

        except Funcionario.DoesNotExist: #tratamento para caso não seja encontrado nenhum registro com o get acima
            funcionario = None
        
        if funcionario and funcionario.senha == senha: #se achar o funcionário
            request.session['user_id'] = funcionario.idfunc
=======
        nome = request.POST.get('nome') 

        funcionario = None 
        try:
            funcionario = Funcionario.objects.get(email=email, senha=senha) 
            nome = funcionario.nome
            context['funcionario'] = "BemVindo "+ nome + "!"

        except Funcionario.DoesNotExist: #tratamento para caso não seja encontrado nenhum registro com o get acima
            pass
        
        if funcionario: #se achar o funcionário
>>>>>>> 6fc9a8ee62cef2fd5ef5db37afcb608da0febef4
            return buscaUsuario(request)

        else:
            erros['senha'] = "Usuário e /ou senha inválidos"
            if erros:
                context['erro'] = erros
<<<<<<< HEAD
                return render(request, 'login/login.html', context=context) 
=======
                return render(request, 'login/login.html', context=context)

>>>>>>> 6fc9a8ee62cef2fd5ef5db37afcb608da0febef4

