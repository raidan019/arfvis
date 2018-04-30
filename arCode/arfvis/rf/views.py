from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Signal
from .models import Sensor
from django.http import HttpResponseRedirect
from .forms import ImageUploadForm
#from somewhere import handle_uploaded_file
# Create your views here.

@csrf_exempt #This allows posting from the client
def index(request):
    if request.method=='PUT':
        dir(request.body)
        print("Received %s" % request.body.decode('utf-8'))
        data = json.loads(request.body.decode('utf-8'))
        print ("Got json: %s" % data)
        newsignal = Signal()
        newsignal.sensor = data['sensor']
        newsignal.device = data['device']
        newsignal.azimuth = data['azimuth']
        newsignal.signal_strength = data['signal_strength']
        newsignal.sensor_latitude = data['sensor_latitude']
        newsignal.sensor_longitude = data['sensor_longitude']
        newsignal.modulation = data['modulation']
        newsignal.encryption_type = data['encryption']
        newsignal.meter_distance = data['meter_distance']
        newsignal.power = data['power']
        newsignal.bssid = data['bssid']
        newsignal.essid = data['essid']
        newsignal.apmode = data['apmode']
        newsignal.date_time = data['date_time']
        #ensure var names match
        if (newsignal.save()):
            response="received"
        else:
            response="Oops couldn't save signal"
    else:
        response= "ARFVIS Main"
    signal_list = list(Signal.objects.order_by('signal_strength')[LIMIT:20])
    context = {'Signal': signal_list} #fill a context with the signal list
    template = loader.get_template('rf/templates/rf/index.html') #Get the template we created    

    #make a template directory (lists top signals[limit approx. 20])
    return HttpResponse(template.render(context, request))

    
def upload_pic(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            m = ExampleModel.objects.get(pk=course_id)
            m.model_pic = form.cleaned_data['image']
            m.save()
            return HttpResponse('image upload success')
    return HttpResponseForbidden('allowed only via POST')



#def handle_uploaded_file(f):
#    with open('some/file/sample.jpg', 'wb+') as destination:
#        for chunk in f.chunks():
#            destination.write(chunk)
