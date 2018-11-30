from django.urls import path
from core import views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(views.Index), name='index'),
    path('log', LoginView.as_view(),name='login'),
    path('register', views.Register_User.as_view(), name='register'),
    path('logout', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
]