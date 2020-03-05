from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='home'),
    path('logs/', delivery_logs, name='logs'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/',  logout_request, name="logout"),
    path('accounts/signup/', signup, name='signup'),
]
