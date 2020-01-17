from django.shortcuts import render
from . models import Parameter, Bottle
from . models import ParameterSerializer
from django.http import HttpResponse
from rest_framework.response import Response
import json


def allParameters(request): #for ajax calls
    parameter_list = []
    all_bottles = Bottle.objects.all()# filter by active
    for bt in all_bottles:
        all_parameter = Parameter.objects.filter(bottle = bt)
        parameter = all_parameter.order_by('-pk')[0]
        ser = ParameterSerializer(parameter, many = False)
        print(ser.data)
        parameter_list.append(ser.data)
    return HttpResponse(json.dumps(parameter_list))
def home(request):
    #all_parameter = Parameter.objects.all()
    all_bottles = Bottle.objects.all()# filter by active
    return render(request,'home.html',{'all_bottles':all_bottles})
def test(request):
    return render(request,'base.html')
