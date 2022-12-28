from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Airport, Flight
# Create your views here.
def index(request):
    flights = Flight.objects.all()
    return render(request, "flights/index.html", {
        "flights":flights
    })

def addFlight(request):
    if request.method == 'GET':
        return render(request, "flights/add_flight.html", {
            "departures": Airport.objects.all(),
            "destinations": Airport.objects.all()
        })
    else:
        flight = Flight()
        destination = request.POST.get("destination")
        flight.destination = Airport.objects.get(city=destination)
        flight.origin = Airport.objects.get(city=request.POST.get('departure'))
        flight.duration = int(request.POST.get('duration'))
        if (flight.is_valid_flight()):
            flight.save()
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "flights/add_flight.html", {
                "message":"Invalid flight.",
                "departures": Airport.objects.all(),
                "destinations": Airport.objects.all()
            })
def flight(request, flightId):
    f = Flight.objects.get(pk=flightId)
    return render(request, "flights/flight.html", {
        "flight":f
    })