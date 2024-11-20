from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from atracoes.models import Atracao
from .serializers import atracaoSerializer

class atracoesViewSet(ModelViewSet):
    queryset = Atracao.objects.all()
    serializer_class = atracaoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Atracao.objects.all()
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)

        if id:
            queryset = queryset.filter(pk=id)
        if nome:
            queryset = queryset.filter(nome__iexact=nome)
        if descricao:
            queryset = queryset.filter(descricao__iexact=descricao)

        return queryset

    @action(detail=True, methods=['put'], url_path='atualizar')
    def atualizar_atracao(self, request, pk=None):
        # Obtém a atração pelo id (pk)
        atracao = self.get_object()
        
        # Usa o serializer para validar e atualizar os dados
        serializer = self.get_serializer(atracao, data=request.data)
        
        if serializer.is_valid():
            serializer.save()  # Salva as mudanças feitas na atração
            return Response(serializer.data)  # Retorna a atração atualizada
        else:
            return Response(serializer.errors, status=400)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
