from django.shortcuts import render, redirect
from . models import Parameter, Bottle, Person,Task
from . models import ParameterSerializer, TaskSerializer
from django.http import HttpResponse
from rest_framework.response import Response
import json
from . forms import taskForm
import datetime
import pytz


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
def todolist(request,person_id):
    person = Person.objects.get(id = person_id)
    return render(request,'person.html', {'person': person})
def test(request):
    return render(request,'person.html')
def task(request,person_id):
    person = Person.objects.get(id = person_id)
    all_task = person.task_set.all()
    all_task_list = []
    for task in all_task:
        ser = TaskSerializer(task, many = False)
        all_task_list.append(ser.data)
    print(all_task_list)
    #return HttpResponse(json.dumps(ser.data))
    return HttpResponse(json.dumps(all_task_list))
def addTask(request,person_id):
    person = Person.objects.get(id = person_id)
    year = int(request.GET['year'])
    month = int(request.GET['month'])
    day = int(request.GET['day'])
    hour = int(request.GET['hour'])
    minute = int(request.GET['minute'])
    prescription = request.GET['prescription']
    timezone =  pytz.timezone("Asia/Calcutta")
    end = datetime.datetime(year,month,day,hour,minute, tzinfo = timezone)
    task = Task(person = person,prescription = prescription, end = end)
    task.save()
    return HttpResponse("saved")


