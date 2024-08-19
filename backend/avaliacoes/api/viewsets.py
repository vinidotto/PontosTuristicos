from rest_framework.viewsets import ModelViewSet
from avaliacoes.models import Avaliacao
from .serializers import avaliacaoSerializer

class avaliacoesViewSet(ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = avaliacaoSerializer

    def __str__(self) -> str:
        return self.nome