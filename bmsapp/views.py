from django.shortcuts import render, redirect
from .forms import RegistraionForm
from django.http import HttpResponse
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json
import requests

from .models import Movie
from .models import Theatre
from .models import Seat
from .models import Tickets

# Create your views here.

def index(response):
    return render(response, "home/homepage.html", {})

def register(response):
	if response.method == 'POST':
		form = RegistraionForm(response.POST)
		if form.is_valid():
			form.save()

		return redirect("/")
	else:
		form = RegistraionForm()

	return render(response, "bmsapp/register.html", {"form" : form})

def all_movies_citywise(request):
    if request.method == 'GET':
    	lol = []
    	data = request.GET['city_name']
    	print (data)
    	movies = Movie.objects.all().filter(city = data)
    	lol.append(movies)
    return HttpResponse(lol)

def all_theatre_movie(request):
    if request.method == 'GET':
    	lol = []
    	data = request.GET['movie_name']
    	theatres = Theatre.objects.all().filter(movie_name = data)
    	print (theatres)
    	showtime = Movie.objects.order_by('show_time')
    	print (showtime)
    	lol.append(theatres)
    	lol.append(showtime)
    return HttpResponse(lol)

@login_required
def bookticket(request):
	if request.method == 'GET':
		data1 = request.GET['theatre_name']
		print (data1)
		data2 = request.GET['movie_name']
		print (data2)
		seatbooking = Seat.objects.filter(movie = data2 , show = data1)[0:1].get()
		print(seatbooking)
		# seatid = seatbooking.seat_id
		ticketid = Tickets.objects.create(seat = seatbooking)
		print (ticketid)
	return HttpResponse(ticketid)



