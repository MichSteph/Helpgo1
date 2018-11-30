from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .models import User
from services.models import Service
from .forms import Form_CreateProfile
from .mixins import FormsUserNeededMixin
from django.contrib.auth.models import User as User_model


# Create your views here.

class List_Users(generic.ListView):
    template_name = 'users/list_users.html'
    model = User_model

    def get_queryset(self, *args, **kwargs):
        qs = User_model.objects.all()
        print(self.request.GET)
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(username__icontains=query)          
        return qs


class Detail_User(generic.DetailView):
    template_name = 'users/detail_user.html'
    model = User_model


def Profile_User(request, pk=None):
    if pk:
        user = User_model.objects.get(pk=pk)
    else:
        user = request.user
        id = User_model._get_pk_val(request.user)
        user = User_model.objects.get(id=id)
    args = {'user': user, 'id': id}
    return render(request, 'users/profile_user.html', args)


class Edit_Profile(FormsUserNeededMixin, generic.UpdateView):
    template_name = 'users/edit_profile.html'
    model = User
    form_class = Form_CreateProfile
    success_url = reverse_lazy('Perfil_Usuario')


    def get_context_data(self, *args, **kwargs):
        context = super(Edit_Profile, self).get_context_data(*args, **kwargs)
        context["create_form"] = Form_CreateProfile()
        return context

class List_Service(generic.ListView):
    template_name = 'users/list_services.html'
    model = Service

    def get_queryset(self, *args, **kwargs):
        qs = Service.objects.all()
        print(self.request.GET)
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(service__icontains=query)          
        return qs

def List_Services(request, username):
    services = Service.objects.all()
    return render(request, 'users/list_services.html',{'services':services,'username':username})