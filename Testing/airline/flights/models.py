from django.db import models

# Create your models here.
class Airport(models.Model):
    city= models.CharField(max_length=64)
    code = models.CharField(max_length=3)

    def __str__(self):
        return f"{self.city}"
class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrivals')
    duration = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.id} : {self.origin} to {self.destination}"

    def is_valid_flight(self):
        return self.origin != self.destination or self.duration > 0