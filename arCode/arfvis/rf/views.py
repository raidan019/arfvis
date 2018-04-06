from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Signal
from .models import Sensor

# Create your views here.

@csrf_exempt #This allows posting from the client
def index(request):
    if request.method=='PUT':
        dir(request.body)
        print("Received %s" % request.body.decode('utf-8'))
        data = json.loads(request.body.decode('utf-8'))
        print ("Got json: %s" % data)
        newsignal = Signal()
        newsignal.sample_id = data['sample_id']
        newsignal.azimuth = data['azimuth']
        newsignal.signal_strength = data['signal_strength']
        newsignal.sensor_latitude = data['sensor_latitude']
        newsignal.sensor_longitude = data['sensor_longitude']
        newsignal.modulation = data['modulation']
        newsignal.encryption_type = data['encryption_type']
        newsignal.meter_distance = data['meter_distance']
        newsignal.power = data['power']
        newsignal.date_time = data['date_time']
        if (newsignal.save()):
            response="received"
        else:
            response="Oops couldn't save signal"
    else:
        response= "ARFVIS Main"
    return HttpResponse(response)
