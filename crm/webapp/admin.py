# admin.py

from django.contrib import admin
from . import models 

# Register your models here

class UserProfileAdmin(admin.ModelAdmin):
    list_display=('user', 'full_name', 'email', 'age', 'gender')
admin.site.register(models.UserProfile,UserProfileAdmin)

class PatientAdmin(admin.ModelAdmin):
    list_display=( 'name', 'age', 'gender','contact_email', 'contact_phone','report' )
admin.site.register(models.Patient,PatientAdmin)

class DoctorAdmin(admin.ModelAdmin):
    list_display=( 'name','contact_email', 'contact_phone' )
admin.site.register(models.Doctor,DoctorAdmin)

class MedicalRecord(admin.ModelAdmin):
    list_display=( 'timestamp','bmi', 'glucose_level','insulin_level' )
admin.site.register(models.MedicalRecord,MedicalRecord)

class Comment(admin.ModelAdmin):
    list_display=( 'patient','author', 'timestamp','text' )
admin.site.register(models.Comment,Comment)

class Record(admin.ModelAdmin):
    list_display=( 'creation_date','first_name', 'last_name','email','phone','address', 'city', 'county', 'country' )
admin.site.register(models.Record,Record)






