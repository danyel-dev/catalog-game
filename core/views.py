from django.shortcuts import render
from django.http import HttpResponse
from .forms import MessageForm


def home(request):
    return render(request, 'core/home.html')


def about(request):
    return render(request, 'core/about.html')


def contact(request):
    form = MessageForm()
    return render(request, 'core/contact.html', {'form': form})
