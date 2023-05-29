from django.shortcuts import render, redirect
from .models import Funcionario
import bcrypt

def criarConta(request):
    return render(request, 'criarConta/criar_conta.html')


def criarFuncionario(request):

    erros = {}
    senha2 = ""
    context = {}

    if request.method == 'POST':
        #coletar os dados do formulario
        regfuncional = request.POST.get('registro_funcional')
        nome = request.POST.get('nome_completo')  
        email = request.POST.get('email')
        senha = request.POST.get('senha1')
        senha2 = request.POST.get('senha2')
        
        #validação caso as senhas digitadas sejam diferentes
        if senha != senha2:
            erros["senha"] = "As senhas não correspondem! Preencha novamente."

        if Funcionario.objects.filter(email__iexact=email).exists():

            erros["senha"] = "Email já utilizado, utilize outro email!"
            
        if erros:
            context['erros'] = erros
        
        else:
            #gravar os dados caso não tenha ocorrido erros
            senha_hash = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())
            gravaDados = Funcionario(regfuncional=regfuncional, nome=nome, email=email, senha=senha_hash.decode('utf-8'))
            gravaDados.save()
            return redirect('sucesso')
            
            
        return render(request, 'criarConta/criar_conta.html', context=context)

def sucesso(request):
    return render(request, 'criarConta/sucesso.html')


