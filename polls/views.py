from django.shortcuts import render
from django.http import HttpResponse # add kele ahe
import datetime

# Create your views here.
def own(request):
    date = datetime.datetime.now()
    s = '<h1>The current date is :' + str(date)+ ' </h1>'

    return HttpResponse(s)
