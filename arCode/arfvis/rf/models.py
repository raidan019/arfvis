from django.db import models

# Create your models here.

class Sensor(models.Model):
    sensor_id = models.IntegerField(default=0)
    antenna_type = models.IntegerField(default=0)
    antenna_direction = models.IntegerField(default=0)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    elevation = models.IntegerField(default=0)
    ssid = models.IntegerField(default=0)
    encryption_type = models.IntegerField(default=0)
    modulation = models.IntegerField(default=0)

class Signal(models.Model):
    sample_id = models.ForeignKey(sensor_id)
    azimuth = models.FloatField(default=0.0)
    signal_strength = models.IntegerField(default = 0)
    sensor_latitude = models.FloatField(default=0.0)
    sensor_longitude = models.FloatField(default=0.0)
    modulation = models.IntegerField(default = 0)
    encryption_type = models.IntegerField(default = 0)
    meter_distance = models.IntegerField(default = 0)
    power = models.IntegerField(default = 0)
    date_time = models.DateTimeField(auto_now_add=True, blank=True) 

class Modulation(models.Model):
    modulation_id = models.ForeignKey(modulation)
    modulation_name = models.CharField(max_length=100)

class Encryption(models.Model):
    encryption_id = models.ForeignKey(encryption_type)
    encryption_name = models.CharField(max_length=100)
    key_size = models.IntegerField(default = 0)

