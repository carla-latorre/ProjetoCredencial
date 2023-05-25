from django.db import models
<<<<<<< HEAD
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class GerenciaFuncionario(BaseUserManager):
    def create_user(self, email, senha, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        if not email:
            raise ValueError('O campo de e-mail é obrigatório')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(senha)
        user.save()
        return user

    def create_superuser(self, email, senha, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, senha, **extra_fields)

class Funcionario(AbstractBaseUser, PermissionsMixin):
=======

#Criar tabelas do banco. Cada tabela corresponde a uma classe e as colunas ficam dentro dentro de cada classe.
# null = não pode ser nulo, blank = não pode ser vazio/preenchido com espaços
class Funcionario(models.Model):
>>>>>>> 6fc9a8ee62cef2fd5ef5db37afcb608da0febef4
    idfunc = models.AutoField(primary_key=True) #chave primária
    nome = models.CharField(max_length=100, null=False, blank=False) #nome
    regfuncional = models.CharField(max_length=12, null=False, blank=False) #registro funcional
    doc = models.CharField(max_length=12, null=True, blank=True) #documento
<<<<<<< HEAD
    email = models.EmailField(max_length=100, unique=True)
    senha = models.CharField(max_length=20) #senha, onde vamos tratar 
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'  # Define o campo 'email' como o identificador de login
    REQUIRED_FIELDS = ['nome']  # Campos extras requeridos ao criar um superusuário

    objects = GerenciaFuncionario()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.nome

    def get_short_name(self):
        return self.nome
=======
    email = models.EmailField(max_length=100)
    senha = models.CharField(max_length=15) #senha, onde vamos tratar 


# Create your models here.
>>>>>>> 6fc9a8ee62cef2fd5ef5db37afcb608da0febef4
