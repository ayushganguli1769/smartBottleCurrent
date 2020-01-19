from django.db import models
from rest_framework import serializers
class Person(models.Model):#person is actually patient
    name = models.CharField(max_length= 150)
    ward_id = models.IntegerField(null= True)
    def __str__(self):
        return self.name
class Bottle(models.Model):
    person = models.OneToOneField(Person,on_delete = models.PROTECT, null = True, blank = True)
    channel_id = models.IntegerField()
    threshold = models.FloatField(null= True)
    is_active = models.BooleanField(default= False)
    def __str__(self):
        return "Bottle " + str(self.channel_id)
class Parameter(models.Model):
    bottle = models.ForeignKey(Bottle, on_delete = models.CASCADE)
    field1 = models.CharField(max_length= 100)
    field2 = models.CharField(max_length= 100)
    field3 = models.CharField(max_length= 100)
class Task(models.Model):
    person = models.ForeignKey(Person, on_delete = models.CASCADE)
    prescription = models.CharField(max_length = 200)
    created = models.DateTimeField(auto_now_add=True)
    end = models.DateTimeField()
    def __str__(self):
        return self.person.name + "prescriptions"
class ParameterSerializer(serializers.Serializer):
    #bottle = serializers.StringRelatedField(many=True) #only targets __str__ method of Bottle
    field1 = serializers.CharField(max_length= 100)
    field2 = serializers.CharField(max_length= 100)
    field3 = serializers.CharField(max_length= 100)
class TaskSerializer(serializers.Serializer):
    prescription = serializers.CharField(max_length = 200)
    created = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S", required=False, read_only=True)
    end = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S", required=False, read_only=True)
