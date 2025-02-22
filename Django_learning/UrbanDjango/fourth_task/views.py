from django.http import HttpResponse
from django.shortcuts import render

from fourth_task.models import Buyer


def sign_up(request):
    buyers = Buyer.objects.all()
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        if password == repeat_password and int(age) >= 18 and username not in str(buyers):
            Buyer.objects.create(username=username, balance=2000.0, age=age)
            return HttpResponse(f'Добро пожаловать {username}!')
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают!'
        elif int(age) <= 18:
            info['error'] = 'Вам ещё нет 18!'
        elif username in str(buyers):
            info['error'] = 'Такой пользователь уже существует!'
    return render(request, 'templates/registration_view.html', context=info)


def shop_view(request):
    return render(request, 'fourth_task/menu.html.html')


def cart_view(request):
    return render(request, 'fourth_task/cart.html.html')


def game_view(request):
    games = {
        'games': ['Pokemon SoulSilver', 'Pokemon Unbound', 'Monster Super League']
    }
    return render(request, 'fourth_task/games.html.html', context=games)
# Create your views here.
