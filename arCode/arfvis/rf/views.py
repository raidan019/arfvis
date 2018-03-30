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
        newsignal.modulation = data['modulation']
        newsignal.power = data['power']
        newsignal.bssid = data['bssid']
        newsignal.encryption = data['encryption']
        newsignal.channel = data['channel']
        newsignal.essid = data['essid']
        if (newsignal.save()):
            response="received"
        else:
            response="Oops couldn't save signal"
    else:
        response= "ARFVIS Main"
    return HttpResponse(response)
