from rest_framework import serializers
from main.models import pontoTuristico

class pontoTuristicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = pontoTuristico
        fields = ['id','nome','descricao']