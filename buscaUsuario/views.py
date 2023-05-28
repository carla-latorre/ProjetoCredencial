from django.shortcuts import render, get_object_or_404
from criarConta.models import Funcionario
from cadastroUsuario.models import Usuario

def buscaUsuario(request):
    return render(request, 'buscaUsuario/buscar_usuario.html')

def Pesquisa(request):

    if request.method == 'POST':
        nome = request.POST.get('nome_completo')
        
        if nome:

            usuarios = Usuario.objects.filter(nome__icontains=nome)

            if not usuarios:
                erros = {}
                context = {}
                erros['usuario'] = "Nenhum usuário encontrado! "
                if erros:
                    context['erro'] = erros
                    return render(request, 'buscaUsuario/buscar_usuario.html', context=context)

            else:

                return render(request, 'buscaUsuario/buscar_usuario.html', {'usuarios': usuarios})
            
    return buscaUsuario(request) 

def credencial(request, user_id):
    usuario = get_object_or_404(Usuario, idusuario=user_id)
    return render (request, 'credencial/credencial.html', {'usuario': usuario})
