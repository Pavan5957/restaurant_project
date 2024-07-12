import csv
import os
import json
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restaurant_project.settings')
django.setup()

from restaurant_app.models import Recipe

with open('restaurants_small.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        Recipe.objects.create(
       
            name=row['name'],
            location=row['location'],
            items=json.dumps(row['items']),
            lat_long=row['lat_long'],
            full_details=json.dumps(row['full_details'])
        )
