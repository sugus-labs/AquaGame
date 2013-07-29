from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^', 'mastermind.views.index', name='index'),
    #url(r'^accounts/login/','django.contrib.auth.views.login', {'template_name': 'registration/login_bootstrapped.html'}),
    #url(r'^accounts/logout/','django.contrib.auth.views.logout', {'template_name': 'registration/logged_out_bootstrapped.html'}),
)