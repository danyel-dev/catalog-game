from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('game/<int:id_game>', views.game_detail, name='game-detail'),
    path('subscribe/<int:id_game>', views.subscribe_game, name='subscribe-game'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('dashboard/delete-game/<int:id_subscribe>', views.delete_game, name='delete-game'),
]
