"""smartBottle URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include, re_path
from . import views
urlpatterns = [
    path('home/',views.home, name= "home"),
    path('all_parameters/', views.allParameters, name= "all_parameters"),
    path('test',views.test),
    re_path(r'person/(?P<person_id>[0-9]+)/',views.todolist, name= "todolist"),
    re_path(r'person/task/(?P<person_id>[0-9]+)/', views.task, name= "task"),
    re_path(r'person/task/add/(?P<person_id>[0-9]+)', views.addTask, name= "addTask"),
    re_path(r'bottle/message/(?P<bottle_id>[0-9]+)/(?P<string>[\w\-]+)/$',views.bottleMessage, name= "bottleMessage"),#can take person todo list task also
    re_path(r'^live/(?P<person_id>[0-9]+)/$', views.live, name="live"),
    #re_path(r'prescription/(?P<person_id>[0-9]+)/', views.prescription, name= "task"),

]
