from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='home'),
    path('user/login/', auth_views.LoginView.as_view(), name='login'),
    path('user/signup/', signup, name='signup'),
]
