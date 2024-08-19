
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from main.api.viewsets import pontoTuristicoViewSet
from atracoes.api.viewsets import atracoesViewSet
from avaliacoes.api.viewsets import avaliacoesViewSet
from comentarios.api.viewsets import comentariosViewSet
from enderecos.api.viewsets import enderecosViewSet



router = routers.DefaultRouter()
router.register(r'pontoturistico', pontoTuristicoViewSet)
router.register(r'atracoes', atracoesViewSet)
router.register(r'avaliacoes', avaliacoesViewSet)
router.register(r'comentarios', comentariosViewSet)
router.register(r'enderecos', enderecosViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
