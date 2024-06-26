from django.db import models

# Create your models here.
class Airport(models.Model):
    city = models.CharField(max_length=65)
    code = models.CharField(max_length=10)

    def __str__(self) -> str:
        return f"{self.city} ({self.code})"


class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departure")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrival")
    duration = models.IntegerField()

    def __str__(self) -> str:
        return f" id: {self.id} {self.origin} to {self.destination}"
