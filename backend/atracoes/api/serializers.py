from rest_framework.serializers import ModelSerializer
from atracoes.models import Atracao

class atracaoSerializer(ModelSerializer):
    class Meta:
        model = Atracao
        fields = ('id','nome', 'descricao', 'horario', 'idade_minima')