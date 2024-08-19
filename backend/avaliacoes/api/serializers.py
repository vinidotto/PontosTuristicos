from rest_framework.serializers import ModelSerializer
from avaliacoes.models import Avaliacao

class avaliacaoSerializer(ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = ('usuario', 'comentario', 'nota', 'data')