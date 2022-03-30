from django.shortcuts import redirect, render
from django.http import HttpResponse

from .forms import UserCreationForm


def register(request):  
    form = UserCreationForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request, 'accounts/register.html', {'form': form})
