from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name='Título do Comentário')
    message = models.TextField(verbose_name='Mensagem')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de envio')


class Game(models.Model):
    title = models.CharField(max_length=100, verbose_name='Título do Game')
    about = models.TextField(verbose_name='Sobre o jogo')
    developer = models.CharField(max_length=100, verbose_name='Desenvolvedora')
    distributor = models.CharField(max_length=100, verbose_name='Distribuidora')
    date_lauch = models.DateField(verbose_name='Data de lançamento')
    image = models.ImageField(upload_to='game_img/%Y/%m/%d', verbose_name='Imagem')
    tags = TaggableManager(verbose_name='Gêneros')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de envio')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Data de alteração')
