from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponseRedirect
from mastermind.models import Ball, Participant, BallForm
from django.utils import timezone
from django.forms.models import modelformset_factory
import json
import random

attempts_num = 4

###################  UTIL FUNCTIONS!

def return_all_participants_list():
	participant_list = Participant.objects.order_by('time_needed')
	context = {'participant_list': participant_list}
	return context

def return_balls_to_HTML():
	balls_db = Ball.objects.all().reverse()
	balls_colour_list = []
	for ball in balls_db:
		print ball.get_colour_display()
		balls_colour_list.append('ball_' + ball.get_colour_display())
	random.shuffle(balls_colour_list)
	balls_colour_list.insert(0, "")
	balls_json = json.dumps([unicode(ball) for ball in balls_colour_list])
	return balls_json, balls_db

#################### URL FUNCTIONS!

def index(request):
    return render(request, 'mastermind/index.html')

def basic_game(request):
	if request.method == 'GET':
		#print "Basic template called"
		balls_json, balls_db = return_balls_to_HTML()
		return render(request, 'mastermind/basic_game.html', {"balls_json": balls_json, "balls_db": balls_db, "attempts": range(attempts_num)})
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
		#print "Normal template called"
		balls_json, balls_db = return_balls_to_HTML()
		return render(request, 'mastermind/normal_game.html', {"balls_json": balls_json, "balls_db": balls_db, "attempts": range(attempts_num)})
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
    else:
        balls_formset = BallFormSet()
    return render_to_response('mastermind/insert_balls_data.html', {'balls_formset': balls_formset})
