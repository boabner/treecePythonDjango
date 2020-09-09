from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from usuario.viewss import UsuarioDeleteView, RecuperarView, PostCreateView, PostUpdateView

app_name = 'usuario'


urlpatterns = [

    path('usuarios/cadastrar/', PostCreateView.as_view(), name="cadastra_usuario"),

    path('usuarios/recuperar/<op>', RecuperarView.as_view(), name="recuperar_senha"),

    path('usuarios/recuperar/sendemail', RecuperarView.as_view(), name="recuperar"),

    path('usuarios/<pk>', PostUpdateView.as_view(), name="atualiza_usuario"),

    path('usuarios/excluir/<pk>', UsuarioDeleteView.as_view(), name="deleta_usuario"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
