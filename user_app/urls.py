from django.urls import path
from . import views

app_name='user'

urlpatterns = [
    path('register', views.UserRegisterView, name='register'),
    path('login', views.UserLoginView, name='login'),
    path('logout', views.UserLoginView, name='logout'),
]