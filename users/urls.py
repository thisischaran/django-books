from django.urls import path
from . import views

urlpatterns = [
    path('loginuser', views.loginuser, name="loginuser"),
    path('registeruser', views.registeruser, name="registeruser"),
    path('userprofileshow', views.userprofileshow, name="userprofileshow"),
    path('logoutuser', views.logoutuser, name="logoutuser"),
]
