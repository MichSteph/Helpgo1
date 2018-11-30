from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import Form_Register

# Create your views here.

def Index(request):
    return render(request, 'core/index.html')

def log(request):
    return render(request, 'core/login.html')

class Register_User(CreateView):
    model = User
    template_name = 'registration/register_user.html'
    form_class = Form_Register
    success_url = reverse_lazy('login')