from django.contrib import admin
from . models import Parameter, Bottle, Person,Task 
# Register your models here.
admin.site.register(Parameter)
admin.site.register(Bottle)
admin.site.register(Person)
admin.site.register(Task)
