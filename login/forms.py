from django import forms
from criarConta.models import Funcionario

class loginForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['email', 'senha']


