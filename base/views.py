from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

def LandingPage(request): 
	return render(request, "LandingPage.html") 

def LoginPage(request):
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user is not None:
			return redirect("home/")
		else:
			return render(request, "LoginPage.html")
	return render(request, "LoginPage.html") 

def HomePage(request): 
	return render(request, "HomePage.html")

def InfoPage(request):
	return render(request, "InfoPage.html")

