from django.urls import path
from alterarConta.views import alteraUsuario, salvaAltera
from criarConta.urls import sucesso

urlpatterns = [
        path('alterarusuarios/<str:user_id>', alteraUsuario, name='altera_usuario'),
        path('alterarusuarios/<str:user_id>/salvar_alteracoes/', salvaAltera, name='salvar_alteracoes'),
        path('sucesso/<str:user_id>', sucesso, name='sucesso')
]