# Generated by Django 5.0.3 on 2024-07-12 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('items', models.TextField()),
                ('lat_long', models.CharField(max_length=255)),
                ('full_details', models.TextField()),
            ],
        ),
    ]
