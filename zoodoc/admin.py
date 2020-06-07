from django.contrib import admin
from .models import Doctor, Qualification, Office_Location, In_Network_Insurance, Review, Profile, Appointment
# Register your models here.
admin.site.register(Doctor)
admin.site.register(Qualification)
admin.site.register(Office_Location)
admin.site.register(In_Network_Insurance)
admin.site.register(Review)
admin.site.register(Profile)
admin.site.register(Appointment)
