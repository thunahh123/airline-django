from django.shortcuts import render
from .models import Flight, Passenger, Airport
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, "flights/index.html",{
        "flights" : Flight.objects.all()
    })

def airports(request):
    return render(request, "flights/airports.html",{
        "airports" : Airport.objects.all()
    })

def airportVIEW(request, airport_id):
    airport = Airport.objects.get(pk=airport_id)
    return  render(request, "flights/singleairport.html",{
        "airport": airport,
        "departures": airport.departures.all(),
        "arrivals": airport.arrivals.all()
    })

def flight(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)
    return render(request, "flights/flight.html",{
        "flight": flight,
        #passengers is the related_name
        "passengers" : flight.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flights=flight).all(),
        #
        # "origin": flight.origin,
        # "destination": flight.destination
    })

def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
        passenger = Passenger.objects.get(pk= int(request.POST["passenger"]))
        # take this passenger, take their set of flights, and go ahead and add a new flight
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flight",args=(flight_id,)))