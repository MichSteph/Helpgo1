from django.urls import path
from users import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(views.List_Users.as_view()), name='Lista_Usuarios'),
    path('user/<int:pk>', login_required(views.Detail_User.as_view()), name='Detalle_Usuario'),
    path('list_services/<username>', login_required(views.List_Services), name='Lista_servicios_usuario'),
    path('profile', login_required(views.Profile_User), name='Perfil_Usuario'),
    path('edit_profile/<int:pk>', login_required(views.Edit_Profile.as_view()),name='Editar_Perfil'),
]