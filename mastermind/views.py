from django.shortcuts import render, redirect
from mastermind.models import Ball, Participant
from django.utils import timezone

def index(request):
    return render(request, 'mastermind/index.html')

def basic_game(request):
	if request.method == 'GET':
		return render(request, 'mastermind/basic_game.html')
	else:
		nickname = request.POST['nickname']
		time = request.POST['time_needed']
		participant = Participant(nick_name=nickname, time_needed=time, date_created=timezone.now())
		participant.save()
		participant_id = participant.id
		return redirect('ranking')

def ranking(request):
	participant_list = Participant.objects.order_by('time_needed')
	context = {'participant_list': participant_list}
	print participant_list
	return render(request, 'mastermind/ranking.html', context)
