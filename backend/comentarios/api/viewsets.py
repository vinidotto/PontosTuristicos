from rest_framework.viewsets import ModelViewSet
from comentarios.models import Comentario
from .serializers import comentarioSerializer

class comentariosViewSet(ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = comentarioSerializer

    def __str__(self) -> str:
        return self.nome