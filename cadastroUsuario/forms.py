from django import forms
from .models import Usuario

class CadUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [ 'numcadastro', 'idfunc', 'iddadosmed', 'eol','nome','nomesocial' ,' raca', 'cidade', 'uf', 
        'datanasc' , 'idade ', 'certidao' , 'folha ','livro ','rg ', 'dataexp', 'nomemae ','endereco','numendereco' ,
        'complemento ','tel ','telrecado','celular','foto','fotodoc','fotodocresp']