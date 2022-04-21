from django.shortcuts import render
from django.http import HttpResponse


def list_foruns(request):
    return HttpResponse('está é a página dos foruns')

