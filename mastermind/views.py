from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponseRedirect
from mastermind.models import Ball, Participant, BallForm
from django.utils import timezone
from django.forms.models import formset_factory

def return_all_participants_list():
	participant_list = Participant.objects.order_by('time_needed')
	context = {'participant_list': participant_list}
	return context

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
		context = return_all_participants_list()
		context['participant_id'] = participant_id
		return render(request, 'mastermind/ranking.html', context)

def ranking(request):
	context = return_all_participants_list()
	return render(request, 'mastermind/ranking.html', context)

def insert_balls_data(request):
    balls_formset = formset_factory(BallForm)
    if request.method == 'POST':
    	print 'POST:', request.POST
    	print "Colour:", request.POST['form-0-colour']
    	print "Liquid:", request.POST['form-0-liquid_contained']
    	print "Density:", request.POST['form-0-liquid_contained_density']
        formset = balls_formset(request.POST)
        print formset
        print balls_formset
        print formset.is_valid()
        if formset.is_valid():
            new_ball = formset.save()
            pass
    else:
        formset = balls_formset()
    return render_to_response('mastermind/insert_balls_data.html', {'balls_formset': balls_formset})
