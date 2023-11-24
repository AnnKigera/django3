from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, CreateRecordForm,CreateDoctorForm,CreatePatientForm, UpdateRecordForm,UpdateDoctorForm,UpdatePatientForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import auth
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model

from django.contrib.auth.decorators import login_required

from .models import Record
from .models import Patient
from .models import Doctor
from .models import Comment


from django.contrib import messages

#homepage

def home(request):


    return render(request, 'webapp/index.html')


def doctor(request):


    return render(request, 'webapp/doctor.html')



def patient(request):


    return render(request, 'webapp/patient.html')

#register
def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.user_type = form.cleaned_data['user_type']
            user.save()
            messages.success(request, "Account created successfully!")
            return redirect("my-login")

    # If the form is not valid or it's a GET request, render the registration page.
    context = {'form': form}
    return render(request, 'webapp/register.html', context=context)



            

            

# login a user
def my_login(request):
    if request.method == "POST":
        form = AuthenticationForm()
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user:
            if not user.check_password(password):
                form.add_error(None, "Invalid login credentials")
                return render(request, "webapp/my-login.html", {"form": form})
            
            login(request, user)
            
            # Redirect users based on their type
            if user.user_type == 'admin':
                return redirect("administrator")  # Change "administrator" to your admin page URL
            elif user.user_type == 'patient':
                return redirect("patient")  # Change "patient_dashboard" to your patient page URL
            elif user.user_type == 'doctor':
                return redirect("doctor")  # Change "doctor_dashboard" to your doctor page URL
        
    form = AuthenticationForm()
    return render(request, "webapp/my-login.html", {"form": form})



#dashboard

@login_required(login_url='my-login')

def dashboard(request):

    my_records = Record.objects.all()

    context = {'records': my_records}


    return render(request, 'webapp/dashboard.html', context=context)

#dashboard

@login_required(login_url='my-login')

def doctor(request):

    my_doctor = Doctor.objects.all()

    context = {'doctor': my_doctor}


    return render(request, 'webapp/doctor.html', context=context)

#dashboard

@login_required(login_url='my-login')

def patient(request):

    my_patient = Patient.objects.all()

    context = {'patient': my_patient}


    return render(request, 'webapp/patient.html', context=context)

#dashboard

@login_required(login_url='my-login')

def administrator(request):

    my_administrator = administrator.objects.all()

    context = {'comment': my_administrator}


    return render(request, 'webapp/comment.html', context=context)


#create a record

@login_required(login_url='my-login')

def create_record(request):

    form = CreateRecordForm()

    if request.method == "POST":

        form = CreateRecordForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "Your record has been created!")

            return redirect("dashboard")
        

    context = {'form': form}

    return render(request, 'webapp/create-record.html', context=context)



#cre
@login_required(login_url='my-login')

def create_doctor(request):

    form = CreateDoctorForm()

    if request.method == "POST":

        form = CreateDoctorForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "Your doctor record has been created!")

            return redirect("doctor")
        

    context = {'form': form}

    return render(request, 'webapp/create-doctor.html', context=context)



#cre
@login_required(login_url='my-login')

def create_patient(request):

    form = CreatePatientForm()

    if request.method == "POST":

        form = CreatePatientForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "Your patient record has been created!")

            return redirect("patient")
        

    context = {'form': form}

    return render(request, 'webapp/create-patient.html', context=context)


#update a record

@login_required(login_url='my-login')

def update_record(request, pk):

    record = Record.objects.get(id=pk)

    form = UpdateRecordForm(instance=record)

    if request.method == 'POST':
        form = UpdateRecordForm(request.POST, instance=record)

        if form.is_valid():

            form.save()

            messages.success(request, "Your record was updated!")

            return redirect("dashboard")
        
    context = {'form':form}

    return render(request, 'webapp/update-record.html', context=context)

#upd

@login_required(login_url='my-login')

def update_doctor(request, pk):

    doctor = Doctor.objects.get(id=pk)

    form = UpdateDoctorForm(instance=doctor)

    if request.method == 'POST':
        form = UpdateDoctorForm(request.POST, instance=doctor)

        if form.is_valid():

            form.save()

            messages.success(request, "Your record was updated!")

            return redirect("doctor")
        
    context = {'form':form}

    return render(request, 'webapp/update-doctor.html', context=context)

#upd
@login_required(login_url='my-login')

def update_patient(request, pk):

    patient = Patient.objects.get(id=pk)

    form = UpdatePatientForm(instance=patient)

    if request.method == 'POST':
        form = UpdatePatientForm(request.POST, instance=patient)

        if form.is_valid():

            form.save()

            messages.success(request, "Your record was updated!")

            return redirect("patient")
        
    context = {'form':form}

    return render(request, 'webapp/update-patient.html', context=context)


#read/view a singular record

@login_required(login_url='my-login')

def singular_record(request, pk):

    all_records = Record.objects.get(id=pk)

    context = {'record':all_records}

    return render(request, 'webapp/view-record.html', context=context)

#rea

@login_required(login_url='my-login')
def singular_doctor(request, pk):
    # Retrieve a specific doctor by ID
    selected_doctor = Doctor.objects.get(id=pk)
    
    # Pass the selected doctor as a list to the template
    context = {'my_doctors': [selected_doctor]}

    return render(request, 'webapp/view-doctor.html', context=context)


#rea

@login_required(login_url='my-login')

def singular_patient(request, pk):

    all_patients = Patient.objects.get(id=pk)

    context = {'patient':all_patients}

    return render(request, 'webapp/view-patient.html', context=context)

#delete a record

@login_required(login_url='my-login')

def delete_record(request, pk):

    record = Record.objects.get(id=pk)

    record.delete()

    messages.success(request, "Your record was deleted!")

    return redirect("dashboard")

#del
@login_required(login_url='my-login')

def delete_doctor(request, pk):

    doctor = Doctor.objects.get(id=pk)

    doctor.delete()

    messages.success(request, "Your record was deleted!")

    return redirect("doctor")

#del
@login_required(login_url='my-login')

def delete_patient(request, pk):

    patient = Patient.objects.get(id=pk)

    patient.delete()

    messages.success(request, "Your record was deleted!")

    return redirect("patient")



#user logout
def user_logout(request):

    auth.logout(request)

    messages.success(request, "You have logged out successfully!")

    return redirect("my-login")



