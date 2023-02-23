from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        print(username)
        client = authenticate(request, username=username, password=password)
        if client is not None:
            login(request, client)
            return redirect('pizzaria')
    return render(request, 'Pizzaria/index.html', {'form': form})