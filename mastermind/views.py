from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from mastermind.models import Ball, Participant, BallForm
from django.utils import timezone
from django.forms.models import modelformset_factory
import json
import random
import time

from weblabdeusto.weblabdeusto_client import WebLabDeustoClient
from weblabdeusto.weblabdeusto_data import ExperimentId, Reservation, Command

attempts_num = 4
global client
global reservation
###################  UTIL FUNCTIONS!

def return_all_participants_list():
	participant_list = Participant.objects.order_by('time_needed')
	context = {'participant_list': participant_list}
	return context

def return_balls_to_HTML():
	balls_db = Ball.objects.all().reverse()
	balls_colour_list = []
	balls_liquid_list = []
	for ball in balls_db:
		#print ball.get_colour_display()
		balls_colour_list.append('ball_' + ball.get_colour_display())
	random.shuffle(balls_colour_list)
	#print "LIST: ",balls_colour_list
	for ball_colour in balls_colour_list:
		for ball in balls_db:
			if ball_colour[5:] == ball.get_colour_display():
				balls_liquid_list.append(ball.liquid_contained)
	balls_colour_list.insert(0, '')
	balls_liquid_list.insert(0, '')
	balls_json = json.dumps([unicode(ball) for ball in balls_colour_list])
	liquids_json = json.dumps([unicode(liquid) for liquid in balls_liquid_list])
	#print liquids_json
	return balls_json, balls_db, liquids_json

def login_on_weblab():
	client = WebLabDeustoClient("http://www.weblab.deusto.es/weblab/")
	session_id = client.login("gustavo.martin", "221186")
	exp_id = ExperimentId("aquarium", "Aquatic experiments")
	reservation = client.reserve_experiment(session_id, exp_id, "{}", "{}")
	reservation_id = reservation.reservation_id
	while reservation.status != Reservation.CONFIRMED:
		print "Retrieving status"
		reservation = client.get_reservation_status(reservation_id)
		print reservation.status
		time.sleep(3)
	return reservation, client

def retrieve_status(reservation, client):
	reservation_id = reservation.reservation_id
	response = client.send_command(reservation_id, Command("get-status"))
	commandstring = response.commandstring
	# FALSE = DOWN
	print commandstring
	#blue_ball = json.loads(commandstring)['blue']
	#json.loads(commandstring)
	return commandstring 

#################### URL FUNCTIONS!

def move(request):
	if request.method == 'POST':
		print request.REQUEST
		status_list = retrieve_status(reservation, client)
		print status_list
		return HttpResponse("POST to Server OK")

def index(request):
	return render(request, 'mastermind/index.html')

def basic_game(request):
	if request.method == 'GET':
		reservation, client = login_on_weblab()
		status_list = retrieve_status(reservation, client)
		balls_json, balls_db, liquids_json = return_balls_to_HTML()
		return render(request, 'mastermind/basic_game.html', {"balls_json": balls_json, "balls_db": balls_db, "attempts": range(attempts_num), "liquids_json": liquids_json })
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
		reservation, client = login_on_weblab()
		status_list = retrieve_status(reservation, client)
		balls_json, balls_db, liquids_json = return_balls_to_HTML()
		return render(request, 'mastermind/normal_game.html', {"balls_json": balls_json, "balls_db": balls_db, "attempts": range(attempts_num), "liquids_json": liquids_json, "status_list": status_list })
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
