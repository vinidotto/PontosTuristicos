from rest_framework.serializers import ModelSerializer
from comentarios.models import Comentario

class comentarioSerializer(ModelSerializer):
    class Meta:
        model = Comentario
        fields = ('usuarios', 'comentario', 'data', 'status')