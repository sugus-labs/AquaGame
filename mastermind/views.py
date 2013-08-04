from django.shortcuts import render
from mastermind.models import Ball, Participant

def index(request):
    return render(request, 'mastermind/index.html')

def basic_game(request):
    return render(request, 'mastermind/basic_game.html')

def ranking(request):
	participant_list = Participant.objects.order_by('time_needed')
	context = {'participant_list': participant_list}
	print participant_list
	return render(request, 'mastermind/ranking.html', context)
