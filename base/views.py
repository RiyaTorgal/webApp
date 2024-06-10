from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from base.models import formdb
from django.http import StreamingHttpResponse
import cv2
from ultralytics import YOLO

def LandingPage(request): 
	return render(request, "LandingPage.html") 

model = YOLO("yolov8s.pt")
# model = yolov5.load('yolov5s.pt')
# # model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
# device = select_device('cpu') # 0 for gpu, '' for cpu

# # Get names and colors
# names = model.module.names if hasattr(model, 'module') else model.names
# hide_labels=False
# hide_conf = False

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

def webcam(request):
    return StreamingHttpResponse(stream(), content_type='multipart/x-mixed-replace; boundary=frame')
    return render(request, 'WebCam.html')

def stream():
    result = model.predict(source="0", show=True)
    # cap = cv2.VideoCapture(0)
    # model.conf = 0.25
    # model.iou = 0.5
    # # model.classes = [0,64,39]
    # while True:
    #     ret, frame = cap.read()
    #     if not ret:
    #         print("Error: failed to capture image")
    #         break

    #     results = model(frame, augment=True)
    #     # proccess
    #     annotator = Annotator(frame, line_width=2, pil=not ascii) 
    #     det = results.pred[0]
    #     if det is not None and len(det):  
    #         for *xyxy, conf, cls in reversed(det):
    #             c = int(cls)  # integer class
    #             label = None if hide_labels else (names[c] if hide_conf else f'{names[c]} {conf:.2f}')
    #             annotator.box_label(xyxy, label, color=colors(c, True)) 
    #     im0 = annotator.result() 
    #     image_bytes = cv2.imencode('.jpg', im0)[1].tobytes()
    #     yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + image_bytes + b'\r\n')