from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


class Forum(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário')
    title = models.CharField('Título', max_length=100)  
    description = models.TextField('Descrição')
    tags = TaggableManager()
    image = models.ImageField('Imagem', upload_to='forum_img/%Y/%m/%d')
    created_at = models.DateTimeField('Data de criação', auto_now_add=True)
    updated_at = models.DateTimeField('Data de atualização', auto_now=True)
