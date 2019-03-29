from django.shortcuts import render
from django.http import HttpResponse     #add kele ahe



# Create your views here.

#def index(request):   # add kele for responce
#    return HttpResponse('<h1>This is responce from django application</h1>')

def goodMorning(request):
    return HttpResponse('<h1> Good Morning </h1>')

def goodAfternoon(request):
    return HttpResponse('<h1> Good Afternoon </h1>')

def goodNight(request):
    return HttpResponse('<h1> Good Night </h1>')
