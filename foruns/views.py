from django.shortcuts import render
from django.http import HttpResponse


def list_foruns(request):
    return render(request, 'foruns/list_foruns.html')

    