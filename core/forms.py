from dataclasses import field, fields
from django import forms
from .models import Message, Comment


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('title', 'message')

        widgets = {
            'title': forms.TextInput(attrs={ 
                'placeholder': 'O título é o assunto da sua mensagem',
            }),
            
            'message': forms.Textarea(attrs={
                'placeholder': 'Digite a sua mensagem aqui',
            }),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)

        widgets = {
            'comment': forms.TextInput(attrs={
                'placeholder': 'Digite o seu comentário aqui'
            })
        }
