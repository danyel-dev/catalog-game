from dataclasses import field
from django import forms
from .models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('title', 'message')

        widgets = {
            'title': forms.TextInput(attrs={ 
                'placeholder': 'O título é o assunto da sua mensagem',
            }),
            
            'message': forms.Textarea(attrs={
                'placeholder': 'Digite seu comentario aqui',
            }),
        }
