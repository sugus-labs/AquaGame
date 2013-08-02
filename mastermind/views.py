from django.shortcuts import render

def index(request):
    return render(request, 'mastermind/index.html')

def basic_page(request):
    return render(request, 'mastermind/basic_page.html')
