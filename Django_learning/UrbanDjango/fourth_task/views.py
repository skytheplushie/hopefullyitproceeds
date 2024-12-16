from django.shortcuts import render


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
