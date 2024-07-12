from django.db import models
import json

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    items = models.TextField()  # Stored as a JSON string
    lat_long = models.CharField(max_length=255)
    full_details = models.TextField()

    def __str__(self):
        return self.name
