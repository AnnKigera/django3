from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
      is_admin = models.BooleanField('Is admin', default=False)
      is_doctor = models.BooleanField('Is doctor', default=False)
      is_patient = models.BooleanField('Is patient', default=False)
      is_administrator = models.BooleanField('Is administrator', default=False)
      user_type = models.CharField(max_length=10, choices=[('admin', 'Admin'), ('patient', 'Patient'), ('doctor', 'Doctor')], default='patient')




class UserProfile(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        full_name = models.CharField(max_length=255,unique=True)
        email = models.CharField(max_length=255)
        age = models.IntegerField()
        gender = models.CharField(max_length=10, default=('UserProfile'))

class Patient(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=15)
    report=models.FileField(upload_to="Report/", default="patient_default_report.pdf")
    

class Doctor(models.Model):
    name = models.CharField(max_length=255)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=15)

class Administrator(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=15)
    report=models.FileField(upload_to="Report/", default="patient_default_report.pdf")


class MedicalRecord(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        timestamp = models.DateTimeField(auto_now_add=True)
        bmi = models.FloatField()
        glucose_level = models.FloatField()
        insulin_level = models.FloatField()


class Prediction(models.Model):
    # Choices for categorical fields
    pregnancies = models.IntegerField()
    glucose = models.FloatField()
    blood_pressure = models.FloatField()
    skin_thickness = models.FloatField()
    insulin = models.FloatField()
    bmi = models.FloatField()
    age = models.IntegerField()




class Comment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    timestamp = models.DateTimeField()
    text = models.TextField()


class Record(models.Model):

    creation_date = models.DateTimeField(auto_now_add=True)

    first_name = models.CharField(max_length=100)

    last_name = models.CharField(max_length=100)

    email = models.CharField(max_length=255)

    phone = models.CharField(max_length=20)

    address = models.CharField(max_length=255)

    city = models.CharField(max_length=100)

    county = models.CharField(max_length=200)

    country = models.CharField(max_length=125)


    def __str__(self):
        return f"{self.user.user.username} - {self.timestamp}"
