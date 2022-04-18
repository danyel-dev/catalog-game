from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator
from .forms import MessageForm, CommentForm

from .models import Game


def home(request):
    search = request.GET.get('search')
    
    if search:
        games = Game.objects.order_by('-id').filter(title__icontains=search)
        qtd_games = games.count()
        
        if qtd_games == 1:
            messages.success(request, f'1 resultado encontrado para "{search}"')
        elif qtd_games > 1:
            messages.success(request, f'{qtd_games} resultados encontrados para "{search}"')
        else:
            messages.error(request, f'Desculpe, não foi encontrado nenhum resultado para "{search}"')
    else:
        games = Game.objects.order_by('-id')

    paginator = Paginator(games, 6)
    page = request.GET.get('page')
    games = paginator.get_page(page)

    return render(request, 'core/home.html', {'games': games})


def game_detail(request, id_game):
    game = get_object_or_404(Game, id = id_game)
    
    form = CommentForm(request.POST or None)
    
    return render(request, 'core/game_detail.html', {'game': game, 'form': form})


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


def about(request):
    return render(request, 'core/about.html')
