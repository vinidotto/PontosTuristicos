from rest_framework.serializers import ModelSerializer
from atracoes.models import Atracao

class atracaoSerializer(ModelSerializer):
    class Meta:
        model = Atracao
        fields = ('nome', 'descricao', 'horario', 'idade_minima')