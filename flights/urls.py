from django.urls import path
 
from . import views

urlpatterns=[
    path("", views.index, name="flights"),
    path("<int:flight_id>", views.flight, name="flight"),
    path("<int:flight_id>/book", views.book, name="book"),
    path("airports", views.airports, name="airports"),
    path("airport/<int:airport_id>", views.airportVIEW, name="airportURL" ),


]