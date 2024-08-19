from rest_framework.viewsets import ModelViewSet
from atracoes.models import Atracao
from .serializers import atracaoSerializer

class atracoesViewSet(ModelViewSet):
    queryset = Atracao.objects.all()
    serializer_class = atracaoSerializer

    def __str__(self) -> str:
        return self.nome