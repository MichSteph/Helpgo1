from django.urls import path
from services import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("list_services/", views.List_Service.as_view(), name="Lista_servicios"),
    path("create_service/", views.Create_Service.as_view(), name="Crear_servicio"),
    path("update_service/<int:pk>", views.Update_Service.as_view(), name="Actualizar_servicio"),
    path("delete_service/<int:pk>", views.Delete_Service.as_view(), name="Eliminar_servicio"),
    path("order_service/<int:pk>",views.Order_Service.as_view(), name="Pagar_servicio"),
    path("pay_services/<int:data>",views.Pay_Services, name="Pagar_servicios"),
]