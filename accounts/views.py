from django.shortcuts import render
# from django.http import HttpResponse
from django.contrib.auth.models import User


def register(request):  
    return render(request, 'accounts/register.html')
