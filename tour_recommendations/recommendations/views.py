from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login

from tour_recommendations.account.forms import LoginForm


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Вход произведен успешно!')
                else:
                    return HttpResponse('Аккаунт неактивен!')
            else:
                return HttpResponse('Пароль и/или логин неверны!')
    else:
        form = LoginForm()
        return render(request, 'account/login.html', {'form': form})


def index(request):
    return render(request, 'recommendations/index.html')
