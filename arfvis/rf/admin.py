from django.contrib import admin

# Register your models here.

from .models import Sensor
from .models import Signal
from .models import Modulation
from .models import Encryption
from .models import Device
admin.site.register(Sensor)
admin.site.register(Signal)
admin.site.register(Modulation)
admin.site.register(Encryption)
admin.site.register(Device)

