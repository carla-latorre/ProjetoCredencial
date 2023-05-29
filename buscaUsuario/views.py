from django.shortcuts import render, get_object_or_404
from cadastroUsuario.models import Usuario
from django.contrib import messages

def buscaUsuario(request):
    return render(request, 'buscaUsuario/buscar_usuario.html')

def Pesquisa(request):

    if request.method == 'GET':
        nome = request.GET.get('nome_completo')
        
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

def excluiUsuario(request, user_id):
    usuario = get_object_or_404(Usuario, idusuario=user_id)
    usuario.delete()
    messages.success(request, 'Usuário excluído com sucesso.')
    return render (request, 'buscaUsuario/buscar_usuario.html', {'usuario': usuario })