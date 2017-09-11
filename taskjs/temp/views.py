from django.shortcuts import render
from django.http import HttpResponse
from .models import Sensors
# Create your views here.
def index(request):
    return HttpResponse("Hello I am Subhadeep")
def Display(request,sensor1=None,sensor2=None):
    all_sensors = Sensors()
    all_sensors.sensor1=float(sensor1)
    all_sensors.sensor2=float(sensor2)
    print(sensor1)
    print(sensor2)
    all_sensors.save()
    return render(request ,'temp/sensors.html',{'all_sensors':all_sensors})
def new_disp(request):
    all_sensors = Sensors.objects.get(pk=Sensors.objects.count())
    print(all_sensors)
    return render(request ,'temp/sensors.html',{'all_sensors':all_sensors})