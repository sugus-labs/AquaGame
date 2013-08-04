from django.shortcuts import render
from mastermind.models import Ball, Participant

def index(request):
    return render(request, 'mastermind/index.html')

def basic_game(request):
	if request.method == 'GET':
		return render(request, 'mastermind/basic_game.html')
	else:
		print 'Nickname:', request.POST['nickname']
		print 'Time:', request.POST['time_needed']
		return render(request, 'mastermind/ranking.html')

def ranking(request):
	participant_list = Participant.objects.order_by('time_needed')
	context = {'participant_list': participant_list}
	print participant_list
	return render(request, 'mastermind/ranking.html', context)
