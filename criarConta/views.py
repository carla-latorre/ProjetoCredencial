from django.shortcuts import render, redirect
from .models import Funcionario

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
<<<<<<< HEAD
            
=======

>>>>>>> 6fc9a8ee62cef2fd5ef5db37afcb608da0febef4
        if erros:
            context['erros'] = erros
        
        else:
        
            #gravar os dados caso não tenha ocorrido erros
            gravaDados = Funcionario(regfuncional=regfuncional, nome=nome,email=email, senha=senha)
            gravaDados.save()
            
            
        return render(request, 'criarConta/criar_conta.html', context=context)



