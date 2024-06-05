from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .forms import UserForm

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
		print("Form submission received")
		form = UserForm(request.POST)
		if form.is_valid():
			form.save()
			form_data = form.cleaned_data
			request.session['form_data'] = form.cleaned_data
			print("Form data saved to session:", form_data)
			return redirect('home/info/')
	else:
		form = UserForm()
	return render(request, "HomePage.html", {'form': form})

def InfoPage(request):
	form_data = request.session.get('form_data', {})
	print("Form data retrieved from session:", form_data) 
	return render(request, "InfoPage.html", {'form_data': form_data})

