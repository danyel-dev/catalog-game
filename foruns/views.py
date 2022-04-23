from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Forum


def list_foruns(request):
    foruns = Forum.objects.order_by('-id')
    
    paginator = Paginator(foruns, 2)
    page = request.GET.get('page')
    foruns = paginator.get_page(page)

    return render(request, 'foruns/list_foruns.html', {'list_objects': foruns})
    