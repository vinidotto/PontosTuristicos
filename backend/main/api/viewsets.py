from rest_framework.viewsets import ModelViewSet
from main.models import pontoTuristico
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

    def create(self, request, *args, **kwargs):
        return super(pontoTuristicoViewSet, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(pontoTuristicoViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(pontoTuristicoViewSet, self).partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(pontoTuristicoViewSet, self).destroy(request, *args, **kwargs)
