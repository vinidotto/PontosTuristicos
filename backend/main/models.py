from django.db import models
from atracoes.models import Atracao
from comentarios.models import Comentario
from avaliacoes.models import Avaliacao
from enderecos.models import Endereco

class pontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    status = models.BooleanField(default=False)
    atracoes =  models.ManyToManyField(Atracao)
    comentarios = models.ManyToManyField(Comentario)
    avaliacao = models.ManyToManyField(Avaliacao)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE, null = True, blank=True)
    foto = models.ImageField(upload_to='pontos_turisticos', null =True)


    def __str__(self):
        return self.nome