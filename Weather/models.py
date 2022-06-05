from django.db import models

class WeatherModel(models.Model):

    city = models.CharField(max_length=50)

    def __str__(self):
        return self.city
