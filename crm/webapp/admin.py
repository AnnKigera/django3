# admin.py

from django.contrib import admin
from .models import UserProfile, Patient, Doctor, MedicalRecord, DiabetesPrediction, Comment, Record

# Register your models here

admin.site.register(UserProfile)
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(MedicalRecord)
admin.site.register(DiabetesPrediction)
admin.site.register(Comment)
admin.site.register(Record)
