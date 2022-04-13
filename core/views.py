from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator
from .forms import MessageForm

from .models import Game


def home(request):
    games = Game.objects.order_by('-id')

    paginator = Paginator(games, 7)
    page = request.GET.get('page')
    games = paginator.get_page(page)

    return render(request, 'core/home.html', {'games': games})


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
