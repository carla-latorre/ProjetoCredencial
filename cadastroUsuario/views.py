from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario, Funcionario
from buscaUsuario.views import buscaUsuario

# criar uma loogica aonde eu busco os registros do funcionario
# pelo nome que eu incluir no campo de busca e se achar o registro, me retornar na tela.

def passo1(request):

    #numero_certidao = None
    if request.method == 'POST':
        request.session['passo1_data'] = { 
                'numcadastro': request.POST.get('numero_cadastro'),
                'eol': request.POST.get('eol'),
                'nome': request.POST.get('nome_completo'),
                'nomesocial': request.POST.get('nome_social'),
                'raca': request.POST.get('raca_cor'),
                'cidade': request.POST.get('cidade'),
                'uf': request.POST.get('uf'),
                'idade': request.POST.get('idade'),
                'datanasc': request.POST.get('data_nascimento'),
                'certidao': request.POST.get('certidao_nascimento'),
                'folha': request.POST.get('folha'),
                'livro': request.POST.get('livro'),
                #'numero_certidao': request.POST.get('numero_certidao'),
                'rg': request.POST.get('rg'),
                'dataexp': request.POST.get('data_expedicao'),
                'nespecial': request.POST.get('necessidade_especial'),
                'nomemae': request.POST.get('nome_completo_responsavel')
        }
        return redirect('passo_dois') #redireciono dentro da view, pois no html não vou redirecionar no botão, o proprio form faz isso
    else:
        return render(request,'cadastroUsuario/passo1_dadospessoais.html')


def passo2(request):

    if request.method == 'POST':

        request.session['passo2_data'] = { 
            'endereco': request.POST.get('endereco'),
            'numendereco': request.POST.get('endereco_numero'),
            'complemento': request.POST.get('complemento'),
            'cep': request.POST.get('cep'),
            'tel': request.POST.get('telefone_residencial'),
            'celular': request.POST.get('telefone_celular'),
            'telrecado': request.POST.get('telefone_recado'),
            'nomerecado': request.POST.get('nome_telefone_recado')
        }
        return redirect('passo_tres')

    else:
        return render(request,'cadastroUsuario/passo2_endereco.html')

def passo3(request):

    if request.method== 'POST':

        request.session['passo3_data'] = {
            'tpsanguineo': request.POST.get('tipo_sanguineo'),
            'convenio': request.POST.get('convenio'),
            'usamedicamento': request.POST.get('tratamento_medico'),
            'possuialergia': request.POST.get('alergias'),
            'restricaoativ': request.POST.get('restricao_ativfisica'),
            'problemasaude': request.POST.get('problemas_saude'),
            'possuilesao': request.POST.get('lesao_fratura_cirurgia')
        }
        return redirect('passo_quatro')

    else:
        return render (request,'cadastroUsuario/passo3_dadosmedicos.html')

def passo4(request):

    if request.method == 'POST':
        passo1_dados = request.session.get('passo1_data')
        passo2_dados = request.session.get('passo2_data')
        passo3_dados = request.session.get('passo3_data')

        idfunc = request.session.get('user_id') #recuperando id da sessão

        funcionario = get_object_or_404(Funcionario, idfunc=idfunc)

        dados_completos = {
            'idfunc': funcionario,
            'eol': passo1_dados.get('eol', ''),
            'nome': passo1_dados.get('nome', ''),
            'nomesocial': passo1_dados.get('nomesocial', ''),
            'raca': passo1_dados.get('raca', ''),
            'cidade': passo1_dados.get('cidade', ''),
            'uf': passo1_dados.get('uf', ''),
            'datanasc': passo1_dados.get('datanasc') or None,
            'idade': passo1_dados.get('datanasc', ''),
            'certidao': passo1_dados.get('certidao', ''),
            'folha': passo1_dados.get('folha', ''),
            'livro': passo1_dados.get('livro', ''),
            'rg': passo1_dados.get('rg', ''),
            'dataexp': passo1_dados.get('dataexp') or None,
            'nespecial': passo1_dados.get('nespecial', ''),
            'nomemae': passo1_dados.get('nomemae', ''),
            'endereco': passo2_dados.get('endereco', ''),
            'numendereco': passo2_dados.get('numero', ''),
            'complemento': passo2_dados.get('complemento', ''),
            'cep': passo2_dados.get('cep', ''),
            'tel': passo2_dados.get('tel', ''),
            'celular': passo2_dados.get('celular', ''),
            'telrecado': passo2_dados.get('telrecado', ''),
            'nomerecado': passo2_dados.get('nomerecado', ''),
            'tpsanguineo': passo3_dados.get('tpsanguineo', ''),
            'convenio': passo3_dados.get('convenio', ''),
            'usamedicamento': passo3_dados.get('usamedicamento', ''),
            'possuialergia': passo3_dados.get('possuialergia', ''),
            'restricaoativ': passo3_dados.get('restricao_ativfisica', ''),
            'problemasaude': passo3_dados.get('problemas_saude', ''),
            'possuilesao': passo3_dados.get('lesao_fratura_cirurgia', '')
        }
    
        formulario_completo = Usuario(**dados_completos)
        formulario_completo.save()

        return buscaUsuario(request)

    else:
        return render (request,'cadastroUsuario/passo4_enviardocumentos.html')




# Create your views here.
