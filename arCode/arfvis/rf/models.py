from django.db import models
from datetime import datetime

# Create your models here.

class Sensor(models.Model):
    antenna_type = models.IntegerField(default=0)
    antenna_direction = models.IntegerField(default=0)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    elevation = models.IntegerField(default=0)
    ssid = models.IntegerField(default=0)
    encryption = models.ForeignKey(Encryption, on_delete=models.CASCADE, default=1)
    modulation = models.IntegerField(default=0)

class Device(models.Model):
    device_name = models.CharField(max_length=100)
    pictureFileName = models.CharField(max_length=100)
    three_dimensional_Object = models.CharField(max_length=100)
    default_username = models.CharField(max_length=100)
    default_password = models.CharField(max_length=100)
    vendor_id = models.CharField(max_length=100)

class Signal(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, default=1)
    device = models.ForeignKey(Device, on_delete=models.CASCADE, default=1)
    azimuth = models.FloatField(default=0.0)
    signal_strength = models.IntegerField(default = 0)
    sensor_latitude = models.FloatField(default=0.0)
    sensor_longitude = models.FloatField(default=0.0)
    modulation = models.ForeignKey(Modulation, on_delete=models.CASCADE, default=1)
    encryption = models.ForeignKey(Encryption, on_delete=models.CASCADE, default=1)
    meter_distance = models.IntegerField(default = 0)
    power = models.IntegerField(default = 0)
    bssid = models.CharField(max_length=100)
    essid = models.CharField(max_length=100)
    apmode = models.CharField(max_length=100)
    date_time = models.DateTimeField(default=datetime.now, blank=True) 

class Modulation(models.Model):
    modulation_name = models.CharField(max_length=100)

class Encryption(models.Model):
    encryption_name = models.CharField(max_length=100)
    key_size = models.IntegerField(default = 0)


