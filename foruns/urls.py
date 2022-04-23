from django.urls import path
from . import views


urlpatterns = [
    path('list/', views.list_foruns, name='list-foruns'),
    path('forum/<int:id_forum>', views.forum, name='forum'),
]
