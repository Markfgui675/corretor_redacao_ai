from django.db import models
from django.contrib.auth.models import User

class Redacao(models.Model):
    redacao = models.TextField(verbose_name='Redação')

class RedacaoComentario(models.Model):
    comentario = models.TextField(verbose_name='Comentário')
    avaliacoes = models.ManyToManyField(User, null=True, related_name='avaliacoes')

