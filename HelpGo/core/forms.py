from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm

class Form_Register(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels = {
            'username':'Nombre de Usuario',
            'first_name':'Nombre',
            'last_name':'Apellidos',
            'email':'Correo',
        }
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise ValidationError(u'Email addresses must be unique.')
        return email