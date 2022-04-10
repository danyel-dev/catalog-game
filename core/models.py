from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name='Título do Comentário')
    message = models.TextField(verbose_name='Mensagem')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de envio')
    