from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from base.models import formdb
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.views.decorators import gzip
from django.http import StreamingHttpResponse
import cv2
import threading

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

@gzip.gzip_page
def webcam(request):
    try:
        cam = VideoCamera()
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except:
        pass
    return render(request, 'WebCam.html')

#to capture video class
class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = self.frame
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
    	b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')