from django.contrib import admin
from django.urls import path, include

app_name = 'treecePythonDjango'
# urlpatterns contém a lista de roteamentos de URLs

urlpatterns = [
    # Inclui as URLs do app ‘usuario’
    path('', include('nucleo.urls', namespace='nucleo')),

    path('accounts/', include('django.contrib.auth.urls')),

    path('usuario/', include('usuario.urls', namespace='usuario')),

    path('admin/', admin.site.urls),
]
