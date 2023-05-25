from django.db import models
from criarConta.models import Funcionario

<<<<<<< HEAD
class Usuario(models.Model):
    idusuario = models.AutoField(primary_key=True)
    numcadastro= models.IntegerField(null=True, blank=True)
    idfunc = models.ForeignKey(Funcionario, on_delete=models.PROTECT, editable=False) #chave estrangeira
=======

class DadosMedicos(models.Model):
    iddadosmed = models.AutoField(primary_key=True)
    tpsanguineo = models.CharField(max_length=2, null=True, blank=True)
    convenio = models.CharField(max_length=100, null=True, blank=True)
    usamedicamento = models.CharField(max_length=100, null=True, blank=True)
    possuialergia = models.CharField(max_length=100, null=True, blank=True)
    restricaoativ = models.CharField(max_length=100, null=True, blank=True)
    problemasaude = models.CharField(max_length=100, null=True, blank=True)
    possuilesao = models.CharField(max_length=100, null=True, blank=True)

class Usuario(models.Model):
    idusuario = models.AutoField(primary_key=True)
    idfunc = models.ForeignKey(Funcionario, on_delete=models.PROTECT, editable=False) #chave estrangeira
    iddadosmed = models.ForeignKey(DadosMedicos, on_delete=models.SET_DEFAULT, default=None)
>>>>>>> 6fc9a8ee62cef2fd5ef5db37afcb608da0febef4
    eol = models.IntegerField(null=True, blank=True)
    nome = models.CharField(max_length=100, null=True, blank=True)
    nomesocial = models.CharField(max_length=100, null=True, blank=True)
    raca = models.CharField(max_length=20, null=True, blank=True)
    cidade = models.CharField(max_length=100, null=True, blank=True)
    uf = models.CharField(max_length=2, null=True, blank=True)
    datanasc = models.DateField(null=True, blank=True)
    idade = models.IntegerField(null=True, blank=True)
    certidao = models.CharField(max_length=10, null=True, blank=True)
    folha = models.CharField(max_length=10, null=True, blank=True)
    livro = models.CharField(max_length=10, null=True, blank=True)
    rg = models.CharField(max_length=27, null=True, blank=True)
    dataexp = models.DateField(null=True, blank=True)
    nomemae = models.CharField(max_length=100, null=True, blank=True)
    endereco = models.CharField(max_length=100, null=True, blank=True)
    numendereco = models.CharField(max_length=10, null=True, blank=True)
    complemento = models.CharField(max_length=10, null=True, blank=True)
    tel = models.CharField(max_length=15, null=True, blank=True)
    telrecado = models.CharField(max_length=15, null=True, blank=True)
    celular = models.CharField(max_length=15, null=True, blank=True)
    foto = models.ImageField(upload_to='fotos_usuarios/', blank=True)
    fotodoc = models.ImageField(upload_to = 'fotos_doc/', blank=True)
    fotodocresp = models.ImageField(upload_to = 'fotos_doc/', blank=True)
<<<<<<< HEAD
    tpsanguineo = models.CharField(max_length=2, null=True, blank=True)
    convenio = models.CharField(max_length=100, null=True, blank=True)
    usamedicamento = models.CharField(max_length=100, null=True, blank=True)
    possuialergia = models.CharField(max_length=100, null=True, blank=True)
    restricaoativ = models.CharField(max_length=100, null=True, blank=True)
    problemasaude = models.CharField(max_length=100, null=True, blank=True)
    possuilesao = models.CharField(max_length=100, null=True, blank=True)
=======

# Create your models here.
>>>>>>> 6fc9a8ee62cef2fd5ef5db37afcb608da0febef4
