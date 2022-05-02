from ast import Subscript
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator
from .forms import ContactForm, CommentForm

from .models import Game, GameUser


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

    return render(request, 'core/home.html', {'list_objects': games})


def game_detail(request, id_game):
    game = get_object_or_404(Game, id = id_game)
    subscribe = GameUser.objects.filter(user=request.user, game=game).first()

    form = CommentForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.game = game 
            form.save()

        return redirect('game-detail', id_game)

    return render(request, 'core/game_detail.html', {'game': game, 'form': form, 'subscribe': subscribe})


def subscribe_game(request, id_game):
    status = request.GET.get('status')
    favorite = request.GET.get('favorite')

    game = get_object_or_404(Game, id=id_game)
    subscribe_game = GameUser.objects.filter(user=request.user, game=game)
    
    if subscribe_game:
        if favorite:
            sub_favorite = subscribe_game.values()[0]['favorite']
            subscribe_game.update(favorite=not(sub_favorite))
        else:
            subscribe_game.update(status=status)
    else:
        if favorite:
            GameUser.objects.create(user=request.user, game=game, favorite=True)
        else:
            GameUser.objects.create(user=request.user, game=game, status=status)

    return redirect('game-detail', id_game)


def dashboard(request):
    subscribes = GameUser.objects.order_by('-id').filter(user=request.user, favorite=True)

    status = request.GET.get('status')

    if status:
        subscribes = GameUser.objects.order_by('-id').filter(user=request.user, status=status)

    paginator = Paginator(subscribes, 2)
    page = request.GET.get('page')
    subscribes = paginator.get_page(page)

    return render(request, 'core/dashboard.html', {'subscribes': subscribes})


def contact(request):
    form = ContactForm(request.POST or None)

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
