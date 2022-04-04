from django.shortcuts import redirect, render
from django.http import HttpResponse

from .forms import UserCreationForm
from django.contrib import messages, auth


def register(request):  
    form = UserCreationForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('login')

    return render(request, 'registration/register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(request, username=username, password=password)

        if not user:
            messages.error(request, 'Campos incorretos, nome de usuário ou senha inválidos.')
        else:
            auth.login(request, user)
            messages.success(request, 'Você fez login com sucesso!')
            return redirect('/')

    return render(request, 'registration/login.html')
