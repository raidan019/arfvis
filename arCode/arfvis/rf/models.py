from django.db import models

# Create your models here.

class Sensor(models.Model):
    antenna_type = models.IntegerField(default=0)
    antenna_direction = models.IntegerField(default=0)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    elevation = models.IntegerField(default=0)

class Signal(models.Model):
    modulation = models.IntegerField(default=0)
    power = models.IntegerField(default = 0)
    bssid = models.CharField(max_length=17) #12 with no colons. Allowing colons
    encryption = models.IntegerField(default = 0)
    channel = models.IntegerField(default = 0)
    essid = models.CharField(max_length=255) 

class Modulation(models.Model):
    modulation_id = models.IntegerField(default=0)
    modulation_name = models.CharField(max_length=100)

class Encryption(models.Model):
    encryption_id = models.IntegerField(default=0)
    encryption_name = models.CharField(max_length=100)

