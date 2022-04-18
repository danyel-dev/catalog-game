from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário')
    title = models.CharField('Título do Comentário', max_length=100)
    message = models.TextField('Mensagem')
    created_at = models.DateTimeField('Data de envio', auto_now_add=True)


class Game(models.Model):
    title = models.CharField('Título do Game', max_length=100)
    description = models.CharField('Descrição do jogo', max_length=255)
    about = models.TextField('Sobre o jogo')
    developer = models.CharField('Desenvolvedora', max_length=100)
    distributor = models.CharField('Distribuidora', max_length=100)
    date_lauch = models.DateField('Data de lançamento')
    image = models.ImageField('Imagem', upload_to='game_img/%Y/%m/%d')
    tags = TaggableManager('Gêneros')
    created_at = models.DateTimeField('Data de envio', auto_now_add=True)
    updated_at = models.DateTimeField('Data de alteração', auto_now=True)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário', related_name='comment')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, verbose_name='Jogo', related_name='comment')
    comment = models.TextField('Comentário')
    created_at = models.DateTimeField('Data de criação', auto_now_add=True)
