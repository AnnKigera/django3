from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.contrib.auth import get_user_model
from .models import Record
from .models import Doctor
from .models import Patient


from django import forms

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

#register a user

class CreateUserForm(UserCreationForm):
     USER_TYPE_CHOICES = (
        ('patient', 'Patient'),
        ('doctor', 'Doctor'),
        ('admin', 'Admin'),
    )
     user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES)

    #email = forms.EmailField(required=True)
     class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2', 'user_type']

    #def save(self, commit=True):
     #   user = super().save(commit=False)
      #  user.is_active = False
       # user.save()
        #verification_token = get_random_string(length=40)
        #user.profile.verification_token = verification_token
        #user.profile.save()

        #return user

#login a user

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


# create a record
class CreateRecordForm(forms.ModelForm):

     class Meta:
        model = Record
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'county', 'country']

class CreateDoctorForm(forms.ModelForm):

     class Meta:
        model = Doctor
        fields = ['name',  'contact_email', 'contact_phone']

class CreatePatientForm(forms.ModelForm):

     class Meta:
        model = Patient
        fields = ['name', 'age', 'gender', 'contact_email', 'contact_phone', 'report']

# update a record
class UpdateRecordForm(forms.ModelForm):

     class Meta:
        model = Record
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'county', 'country']

class UpdateDoctorForm(forms.ModelForm):

     class Meta:
        model = Doctor
        fields = ['name',  'contact_email', 'contact_phone']

class UpdatePatientForm(forms.ModelForm):

     class Meta:
        model = Patient
        fields = ['name', 'age', 'gender', 'contact_email', 'contact_phone', 'report']