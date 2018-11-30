from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Service
from .mixins import FormsUserNeededMixin
from .forms import Form_CreateService

# Create your views here.

class List_Service(generic.ListView):
    template_name = 'services/list_services.html'
    model = Service

    def get_queryset(self, *args, **kwargs):
        qs = Service.objects.all()
        print(self.request.GET)
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(service__icontains=query)          
        return qs


class Create_Service(FormsUserNeededMixin, generic.CreateView):
    template_name = 'services/create_service.html'
    model = Service
    fields = ["user","service","price"]
    success_url = reverse_lazy('Lista_servicios')

    @method_decorator(login_required(login_url='/log'))
    def dispatch(self, *args, **kwargs):
       return super(Create_Service, self).dispatch(*args, **kwargs)

class Order_Service(FormsUserNeededMixin, generic.DetailView):
    template_name = 'services/order_service.html'
    model = Service
    success_url = reverse_lazy('Lista_servicios')


def Pay_Services(request, data):
    services = Service.objects.all()
    return render(request, 'services/pay_service.html',{'services':services,'data':data})

class Update_Service(generic.UpdateView):
    template_name = 'services/update_service.html'
    model = Service
    fields = ["service","price"]
    success_url = reverse_lazy('Lista_servicios')

class Delete_Service(generic.DeleteView):
    template_name = 'services/delete_service.html'
    model = Service
    success_url = reverse_lazy('Lista_servicios')