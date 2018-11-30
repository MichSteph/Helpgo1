from django import forms
from .models import Service

class Form_CreateService(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['user','service','price']