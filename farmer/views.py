from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from farmer.models import Sensor 

def sensor(request, sid):
    sensor_data = Sensor.objects.filter(sensor_id=sid)
    context = {}
    context['sid'] = sid
    context['data'] = sensor_data
    return render(request, 'farmer/sensor.html', context)


def sensor_api(request, sid):
    sensor_data = Sensor.objects.filter(sensor_id=sid)
    context = {}
    context['sid'] = sid
    context['data'] = list(sensor_data.values())
    return JsonResponse(context)


def farmer(request):
    return render(request, 'farmer/farmer.html')