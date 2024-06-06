from django.urls import path 
from base import views 

urlpatterns = [ 
	path("", views.LandingPage, name="LandingPage"), 
	path("login", views.LoginPage, name="LoginPage"), 
	path("home/", views.HomePage, name="HomePage"),
    path("home/info/", views.InfoPage, name="InfoPage"),
    path('webcam', views.webcam, name='webcam'),
]
