from django.urls import path

from . import views

urlpatterns = [
#    path('',views.index, name ='index' ),
    path('goodMorning/',views.goodMorning, name = 'goodMorning'),
    path('goodAfternoon/',views.goodAfternoon, name='goodAfternoon'),
    path('goodNight/',views.goodNight, name='goodNight' )# by default this page will be open index and in which called function whos name is infdex
]
