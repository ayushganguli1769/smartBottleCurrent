from django.db import models
from rest_framework import serializers
class Bottle(models.Model):
    channel_id = models.IntegerField()
    is_active = models.BooleanField(default= False)
    def __str__(self):
        return "Bottle " + str(self.channel_id)
class Parameter(models.Model):
    bottle = models.ForeignKey(Bottle, on_delete = models.CASCADE)
    field1 = models.CharField(max_length= 100)
    field2 = models.CharField(max_length= 100)
    field3 = models.CharField(max_length= 100)

class ParameterSerializer(serializers.Serializer):
    #bottle = serializers.StringRelatedField(many=True) #only targets __str__ method of Bottle
    field1 = serializers.CharField(max_length= 100)
    field2 = serializers.CharField(max_length= 100)
    field3 = serializers.CharField(max_length= 100)
