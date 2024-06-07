from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(max_length=100, unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class Redacao(models.Model):
    redacao = models.TextField(verbose_name='Redação')

class RedacaoComentario(models.Model):
    comentario = models.TextField(verbose_name='Comentário')
    avaliacoes = models.ManyToManyField(CustomUser, related_name='avaliacoes')

