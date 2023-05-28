from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

class Funcionario(AbstractBaseUser, PermissionsMixin):
    idfunc = models.AutoField(primary_key=True) #chave primária
    nome = models.CharField(max_length=100, null=False, blank=False) #nome
    regfuncional = models.CharField(max_length=12, null=False, blank=False) #registro funcional
    doc = models.CharField(max_length=12, null=True, blank=True) #documento
    email = models.EmailField(max_length=100, unique=True)
    senha = models.CharField(max_length=128) #senha, onde vamos tratar 
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome']  # Campos extras requeridos ao criar um superusuário


    def __str__(self):
        return str(self.idfunc)

