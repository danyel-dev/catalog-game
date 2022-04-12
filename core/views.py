from email import message
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from .forms import MessageForm


def home(request):
    return render(request, 'core/home.html')


def about(request):
    return render(request, 'core/about.html')


def contact(request):
    form = MessageForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            messages.success(request, 'Sua mensagem foi enviada com sucesso!')
        
        return redirect('contact')

    return render(request, 'core/contact.html', {'form': form})
