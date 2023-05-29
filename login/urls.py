from django.urls import path, include
from login.views import loginview, buscaLogin


urlpatterns = [
        path('', loginview, name='conta'),
        path('inicio/', buscaLogin, name='buscar_login'),
        path('', include('alterarConta.urls')),
]
