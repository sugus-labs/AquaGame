from django.http import HttpResponse

def index(request):
    return HttpResponse("index temporal page.")