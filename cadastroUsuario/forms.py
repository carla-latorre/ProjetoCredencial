from django import forms
from .models import Usuario

class CadUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [ 
        'numcadastro',
        'idfunc', 
        'eol',
        'nome',
        'nomesocial' ,
        'raca', 
        'cidade', 
        'uf', 
        'datanasc' ,
        'idade ', 
        'certidao' , 
        'folha ',
        'livro ',
        'rg', 
        'dataexp', 
        'nespecial', 
        'nomemae ',
        'endereco',
        'numendereco' ,
        'complemento ',
        'tel ',
        'telrecado',
        'nomerecado',
        'celular',
        'foto',
        'fotodoc',
        'fotodocresp', 
        'tpsanguineo', 
        'convenio',
        'usamedicamento', 
        'possuialergia', 
        'restricaoativ', 
        'problemasaude',
        'possuilesao']
