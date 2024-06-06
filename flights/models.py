from django.db import models

# Create your models here.


class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    #string representation
    def __str__(self):
        return f"{self.city} ({self.code})"
    

class Flight(models.Model):
    # origin = models.CharField(max_length=64)
    # destination = models.CharField(max_length=64)

    # models.CASCADE means if we ever delete an airport form the airpost table,
    # its going to also delete any of the correspoding flights
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration= models.IntegerField()


    #string representation of the object
    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"

class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flight,  blank=True, related_name="passengers")

    def __str__(self):
        return f"{self.first} {self.last}"