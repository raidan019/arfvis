from django.db import models
from datetime import datetime

# Create your models here.

class Modulation(models.Model):
    modulation_name = models.CharField(max_length=100)
    def __str__(self):
        return (self.modulation_name)

class Encryption(models.Model):
    encryption_name = models.CharField(max_length=100)
    key_size = models.IntegerField(default = 0)
    def __str__(self):
        return (self.encryption_name)

class Sensor(models.Model):
    antenna_type = models.CharField(max_length = 100)
    antenna_direction = models.IntegerField(default=0)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    elevation = models.IntegerField(default=0)
    ssid = models.CharField(max_length = 100)
    encryption = models.ForeignKey(Encryption, on_delete=models.CASCADE, default=1)
    modulation = models.ForeignKey(Modulation, on_delete=models.CASCADE, default=1)

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

class ImageModel(models.Model):
    model_pic = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')

