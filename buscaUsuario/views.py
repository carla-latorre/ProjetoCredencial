<<<<<<< HEAD
from django.shortcuts import render, redirect
=======
from django.shortcuts import render
>>>>>>> 6fc9a8ee62cef2fd5ef5db37afcb608da0febef4
from criarConta.models import Funcionario

def buscaUsuario(request):
    return render(request, 'buscaUsuario/buscar_usuario.html')

def Pesquisa(request):

    if request.method == 'POST':
        nome = request.POST.get('nome_completo')
        
        if nome:

            usuarios = Funcionario.objects.filter(nome__icontains=nome)

            if not usuarios:

                semuser = {}
                semuser['usuario'] = usuarios
                return render(request, 'buscaUsuario/buscar_usuario.html', semuser=semuser)

            else:

                return render(request, 'buscaUsuario/buscar_usuario.html', {'usuarios': usuarios})
            
<<<<<<< HEAD
    return buscaUsuario(request) 

def credencial(request, user_id):
    usuario = Funcionario.objects.get(idfunc=user_id)
    return render (request, 'credencial/credencial.html', {'usuario': usuario})
=======
        
    return buscaUsuario(request) 


def credencial(request):
    return render (request, 'credencial/credencial.html')
>>>>>>> 6fc9a8ee62cef2fd5ef5db37afcb608da0febef4
