from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from base.models import formdb

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
	if request.method == 'POST':
		fullName = request.POST.get('fullName')
		age = request.POST.get('age')
		gender = request.POST.get('gender')
		country = request.POST.get('country')
		phNo = request.POST.get('phNo')
		address = request.POST.get('address')
		form = formdb(fullName=fullName, age=age, gender=gender, country=country, phNo=phNo, address=address)
		form.save()
	return render(request, "HomePage.html")

def InfoPage(request):
	forms = formdb.objects.all() 
	return render(request, "InfoPage.html",{'forms':forms})

