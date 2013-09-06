from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^basic', 'mastermind.views.basic_game', name='basic_game'),
    url(r'^normal', 'mastermind.views.normal_game', name='normal_game'),
    url(r'^ranking', 'mastermind.views.ranking', name='ranking'),
    url(r'^balls_data', 'mastermind.views.insert_balls_data', name='insert_balls_data'),
    url(r'^move', 'mastermind.views.move', name='move'),
    #url(r'^accounts/login/','django.contrib.auth.views.login', {'template_name': 'registration/login_bootstrapped.html'}),
    #url(r'^accounts/logout/','django.contrib.auth.views.logout', {'template_name': 'registration/logged_out_bootstrapped.html'}),
    url(r'', 'mastermind.views.index', name='index'),
)