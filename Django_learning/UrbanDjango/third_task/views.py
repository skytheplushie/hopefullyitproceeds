from django.shortcuts import render


def shop_view(request):
    return render(request, 'third_task/platform.html.html')


def cart_view(request):
    return render(request, 'third_task/cart.html.html')


def game_view(request):
    games = {
        'first': 'Pokemon SoulSilver',
        'second': 'Pokemon Unbound',
        'third': 'Monster Super League'
    }
    return render(request, 'third_task/games.html.html', context=games)
# Create your views here.
