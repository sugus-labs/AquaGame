from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponseRedirect
from mastermind.models import Ball, Participant, BallForm
from django.utils import timezone
from django.forms.models import modelformset_factory

def return_all_participants_list():
	participant_list = Participant.objects.order_by('time_needed')
	context = {'participant_list': participant_list}
	return context

def index(request):
    return render(request, 'mastermind/index.html')

def basic_game(request):
	if request.method == 'GET':
		balls = Ball.objects.all()
		balls_colour_list = []
		for ball in balls:
			#print ball.colour
			balls_colour_list.append(ball.colour)
		#print balls_colour_list
		context = balls_colour_list
		return render(request, 'mastermind/basic_game.html', context)
	else:
		nickname = request.POST['nickname']
		time = request.POST['time_needed']
		participant = Participant(nick_name=nickname, time_needed=time, date_created=timezone.now())
		participant.save()
		participant_id = participant.id
		context = return_all_participants_list()
		context['participant_id'] = participant_id
		return render(request, 'mastermind/ranking.html', context)

def normal_game(request):
	if request.method == 'GET':
		return render(request, 'mastermind/normal_game.html')
	else:
		nickname = request.POST['nickname']
		time = request.POST['time_needed']
		participant = Participant(nick_name=nickname, time_needed=time, date_created=timezone.now())
		participant.save()
		participant_id = participant.id
		context = return_all_participants_list()
		context['participant_id'] = participant_id
		return render(request, 'mastermind/ranking.html', context)

def ranking(request):
	context = return_all_participants_list()
	return render(request, 'mastermind/ranking.html', context)

def insert_balls_data(request):
    BallFormSet = modelformset_factory(Ball)
    if request.method == 'POST':
        balls_formset = BallFormSet(request.POST, request.FILES)
        print balls_formset.errors
        if balls_formset.is_valid():
            balls_formset.save()
            # do something.
    else:
        balls_formset = BallFormSet()
    return render_to_response('mastermind/insert_balls_data.html', {'balls_formset': balls_formset})
