from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        full_name = models.CharField(max_length=255,primary_key=True)
        email = models.CharField(max_length=255)
        age = models.IntegerField()
        gender = models.CharField(max_length=10)

class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=15)
    

class Doctor(models.Model):
    name = models.CharField(max_length=255)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=15)


class MedicalRecord(models.Model):
        user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
        timestamp = models.DateTimeField(auto_now_add=True)
        bmi = models.FloatField()
        glucose_level = models.FloatField()
        insulin_level = models.FloatField()


class DiabetesPrediction(models.Model):
        user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
        timestamp = models.DateTimeField(auto_now_add=True)
        predicted_diabetes = models.BooleanField()
        prediction_accuracy = models.FloatField()


class Comment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
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
