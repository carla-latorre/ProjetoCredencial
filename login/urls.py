from django.urls import path
<<<<<<< HEAD
from login.views import loginview, buscaLogin


urlpatterns = [
        path('', loginview, name='conta'),
=======
from login.views import login, buscaLogin


urlpatterns = [
        path('', login, name='conta'),
>>>>>>> 6fc9a8ee62cef2fd5ef5db37afcb608da0febef4
        path('inicio/', buscaLogin, name='buscar_login'),
]
