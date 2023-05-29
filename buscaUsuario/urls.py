from django.urls import path, include
from buscaUsuario.views import buscaUsuario, Pesquisa, credencial, excluiUsuario


urlpatterns = [
        path('pesquisa', Pesquisa, name='pesquisa'),
        path('buscar_usuario', buscaUsuario, name='buscar_usuario'),
        path('credencial/<str:user_id>/', credencial, name='gera_credencial'),   
        path('p/', include('cadastroUsuario.urls')),
        path('exclui_usuario/<str:user_id>/', excluiUsuario, name='exclui_usuario')
]
