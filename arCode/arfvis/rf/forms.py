from django import forms
from .models import Sensor, Signal

class CadetForm(forms.ModelForm):
    class Meta:
        model = Sensor
        fields = '__all__'

class ImageUploadForm(forms.Form):
    """Image upload form."""
    image = forms.ImageField()

class SensorForm(forms.ModelForm):
     """Sensor Upload form"""
     class Meta:
          model = Sensor
          fields = '__all__'
	
