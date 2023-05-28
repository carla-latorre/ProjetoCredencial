from django.shortcuts import render
from criarConta.models import Funcionario
from buscaUsuario.views import buscaUsuario
import bcrypt

#função para requisição do html
def loginview(request): 
    return render(request, 'login/login.html')


def buscaLogin(request):

    erros = {}
    context = {}

    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        try:
            funcionario = Funcionario.objects.get(email=email) 

        except Funcionario.DoesNotExist: #tratamento para caso não seja encontrado nenhum registro com o get acima
            funcionario = None
        
        if funcionario and bcrypt.checkpw(senha.encode('utf-8'), funcionario.senha.encode('utf-8')):

            request.session['user_id'] = funcionario.idfunc
            return buscaUsuario(request)

        else:
            erros['senha'] = "Usuário e /ou senha inválidos"
            if erros:
                context['erro'] = erros
                return render(request, 'login/login.html', context=context) 
    else:
        return loginview(request)