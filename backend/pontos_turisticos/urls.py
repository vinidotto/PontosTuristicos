
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from main.api.viewsets import pontoTuristicoViewSet
from atracoes.api.viewsets import atracoesViewSet
from avaliacoes.api.viewsets import avaliacoesViewSet
from comentarios.api.viewsets import comentariosViewSet
from enderecos.api.viewsets import enderecosViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView




router = routers.DefaultRouter()
router.register(r'pontoturistico', pontoTuristicoViewSet, basename='PontoTuristico')
router.register(r'atracoes', atracoesViewSet)
router.register(r'avaliacoes', avaliacoesViewSet)
router.register(r'comentarios', comentariosViewSet)
router.register(r'enderecos', enderecosViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

