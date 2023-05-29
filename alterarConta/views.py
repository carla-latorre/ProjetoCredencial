from django.shortcuts import render, get_object_or_404, redirect
from criarConta.models import Funcionario
import bcrypt

def alteraUsuario(request, user_id):

    usuario = get_object_or_404(Funcionario, idfunc=user_id)

    return render(request, 'alterarConta/alterar_conta.html', {'usuario': usuario})


def salvaAltera(request, user_id):
    usuario = get_object_or_404(Funcionario, idfunc=user_id)

    if request.method == 'POST':

        novasenha = request.POST.get('senha1')
        novasenha2 = request.POST.get('senha2')

        if novasenha == novasenha2:

            senha_hash = bcrypt.hashpw(novasenha2.encode('utf-8'), bcrypt.gensalt())
            usuario.senha = senha_hash.decode('utf-8')
            usuario.save()
            return render(request, 'alterarConta/alterar_conta.html', {'usuario': usuario})

            
    

    return render(request, 'alterarConta/alterar_conta.html', {'usuario': usuario})