<<<<<<< HEAD
from django.urls import path, include
=======
from django.urls import path
>>>>>>> 6fc9a8ee62cef2fd5ef5db37afcb608da0febef4
from buscaUsuario.views import buscaUsuario, Pesquisa, credencial


urlpatterns = [
        path('pesquisa', Pesquisa, name='pesquisa'),
        path('buscar_usuario', buscaUsuario, name='buscar_usuario'),
<<<<<<< HEAD
        path('credencial/<str:user_id>/', credencial, name='gera_credencial'),   
        path('p/', include('cadastroUsuario.urls')),
=======
        path('credencial', credencial, name='credencial'),
>>>>>>> 6fc9a8ee62cef2fd5ef5db37afcb608da0febef4
]
