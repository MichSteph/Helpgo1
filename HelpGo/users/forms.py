from django import forms
from .models import User

class Form_CreateProfile(forms.ModelForm):
    class Meta:
        model = User
        fields = ['age','area','active','description','image']