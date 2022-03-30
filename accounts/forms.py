from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _


class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Unique identifier for the student')

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]

        if commit:
            user.save()
        return user
