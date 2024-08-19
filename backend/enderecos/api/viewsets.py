from rest_framework.viewsets import ModelViewSet
from enderecos.models import Endereco
from .serializers import enderecosSerializer

class enderecosViewSet(ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = enderecosSerializer

    def __str__(self) -> str:
        return self.nome