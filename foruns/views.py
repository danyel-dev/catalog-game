from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Forum


def list_foruns(request):
    foruns = Forum.objects.order_by('-id')
    
    paginator = Paginator(foruns, 2)
    page = request.GET.get('page')
    foruns = paginator.get_page(page)

    return render(request, 'foruns/list_foruns.html', {'list_objects': foruns})


def forum(request, id_forum):
    forum = get_object_or_404(Forum, id = id_forum)
    return render(request, 'foruns/forum.html', {'forum': forum})
