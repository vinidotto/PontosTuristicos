from rest_framework.viewsets import ModelViewSet
from main.models import pontoTuristico
from .serializers import pontoTuristicoSerializer

class pontoTuristicoViewSet(ModelViewSet):
    queryset = pontoTuristico.objects.filter(status=True)
    serializer_class = pontoTuristicoSerializer
