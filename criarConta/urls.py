from django.urls import path
from criarConta.views import criarConta, criarFuncionario, sucesso

urlpatterns = [
        path('cadastro/', criarConta, name='cadastro'), #name = nome da path para indicar em outra página que eu vou clicar e ir para essa página
        path('dados/', criarFuncionario, name='criafunc'),
        path('sucesso/', sucesso, name='sucesso')
]