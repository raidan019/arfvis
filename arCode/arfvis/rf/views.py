from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Signal, Device
from .models import Sensor, ImageModel
from django.http import HttpResponseRedirect,HttpResponseForbidden
from .forms import ImageUploadForm, SensorForm
from django.template import loader
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
    signal_list = list(Signal.objects.order_by('signal_strength')[:5])
    devices = Device.objects.all()
    context = {'Signal': signal_list, 'devices' : devices} #fill a context with the signal list
    template = loader.get_template('rf/index.html') #Get the template we created    

    #make a template directory (lists top signals[limit approx. 20])
    return HttpResponse(template.render(context, request))

    
def upload_pic(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            m = ImageModel()
            m.model_pic = form.cleaned_data['image']
            m.save()
            return HttpResponse('image upload success')
        else:
            return HttpResponse('oops the form did not work')
    else:
        return HttpResponseForbidden('allowed only via POST')

def upload(request):
	form = ImageUploadForm()
	return render(request, 'rf/upload_pic.html', {'form': form})	

def hololens(request):
    signal_list = list(Signal.objects.order_by('signal_strength'))[:10]
    context = {'signal_list': signal_list} #fill a context with the signal list
    template = loader.get_template('rf/hololens.html') #Get the
    return render(request, 'rf/hololens.html', context)

def addsensor(request):
    if request.method == 'POST':
        form = SensorForm(request.POST)
        if form.is_valid():
            #Add the cadet to the database
            newSensor = form.save()
            #Go back to cadet list
            return HttpResponseRedirect('/')
    else:
        form = SensorForm()
    return render(request, 'rf/add_sensor.html', {'form': form})

def detail(request):
    try: 
        signal = Signal.objects.all
        sensor = Signal.sensor
        context = {'signal': signal, 'sensor' : sensor}
    except Signal.DoesNotExist:
        raise Http404("Signal does not exist")
    return render(request, 'rf/detail.html', context)  


    """def detail(request, cadet_id):
    try:
        cadet = Cadet.objects.get(pk=cadet_id)
        companies = Company.objects.all()
        context = {'cadet':cadet, 'companies': companies}
    except Cadet.DoesNotExist:
        raise Http404("Cadet does not exist")
    return render(request, 'users/detail.html', context)
    """
    #else:
        #return HttpResponseRedirect('/users'
#def handle_uploaded_file(f):
#    with open('some/file/sample.jpg', 'wb+') as destination:
#        for chunk in f.chunks():
#            destination.write(chunk)

