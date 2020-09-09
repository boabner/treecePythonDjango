from django.urls import path

from .viewss import IndexTemplateView

app_name = 'nucleo'
# urlpatterns contém a lista de roteamentos de URLs

urlpatterns = [
    # GET /
    path('', IndexTemplateView.as_view(), name='index'),
]
