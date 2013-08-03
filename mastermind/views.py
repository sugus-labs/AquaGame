from django.shortcuts import render

def index(request):
    return render(request, 'mastermind/index.html')

def basic_game(request):
    return render(request, 'mastermind/basic_game.html')

def ranking(request):
    return render(request, 'mastermind/ranking.html')
