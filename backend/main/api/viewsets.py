from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from main.models import pontoTuristico
from atracoes.models import Atracao
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import permission_classes
from .serializers import pontoTuristicoSerializer
from rest_framework.permissions import IsAuthenticated


class pontoTuristicoViewSet(ModelViewSet):
    queryset = pontoTuristico.objects.filter()
    serializer_class = pontoTuristicoSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('id', 'nome', 'descricao')

    @permission_classes([IsAuthenticated])
    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome__iexact', None)
        descricao = self.request.query_params.get('descricao__iexact', None)
        queryset = pontoTuristico.objects.all()

        if id:
            queryset = pontoTuristico.objects.filter(pk=id)
        if nome:
            queryset = queryset.filter(nome=nome)
        if descricao:
            queryset = queryset.filter(descricao=descricao)

        return queryset
    
    @action(detail=True, methods=['post'], url_path='associar-atracoes')
    def associar_atracoes(self, request, pk=None):
        ponto_turistico = self.get_object()
        atracoes_ids = request.data.get('atracoes_ids', [])
        
        if not atracoes_ids:
            return Response({"detail": "Nenhuma atração foi fornecida."}, status=status.HTTP_400_BAD_REQUEST)
        atracoes = Atracao.objects.filter(id__in=atracoes_ids)

        ponto_turistico.atracoes.add(*atracoes)

        return Response({"detail": "Atrações associadas com sucesso ao ponto turístico."}, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        return super(pontoTuristicoViewSet, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(pontoTuristicoViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(pontoTuristicoViewSet, self).partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(pontoTuristicoViewSet, self).destroy(request, *args, **kwargs)
