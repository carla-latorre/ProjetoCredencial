from django.urls import path
from cadastroUsuario.views import passo1, passo2, passo3, passo4


urlpatterns = [
        path('passo1/', passo1 , name='passo_um'),
        path('passo2/', passo2 , name='passo_dois'),
        path('passo3/', passo3 , name='passo_tres'),
        path('passo4/', passo4 , name='passo_quatro'),
]
