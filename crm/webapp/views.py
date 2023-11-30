import pickle
from django.shortcuts import render, redirect
from django.http import HttpResponse
from sklearn.preprocessing import StandardScaler
from .forms import CreateUserForm, LoginForm, CreateRecordForm,CreateDoctorForm,CreatePatientForm, UpdateRecordForm,UpdateDoctorForm,UpdatePatientForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import auth
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from .forms import MedicalRecordForm,CommentForm ,UserPredictionForm
from django.contrib.auth.decorators import login_required
from .models import Administrator
from .models import Record
from .models import MedicalRecord
from .models import Patient
from .models import Doctor
from .models import Comment
from .models import Prediction
from django.contrib import messages
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

#homepage

def home(request):


    return render(request, 'webapp/index.html')

def prediction1(request):


    return render(request, 'webapp/prediction1.html')

def predict(request):


    return render(request, 'webapp/predict.html')
def result(request):
    data=pd.read_csv(r"static\diabetes.csv")
    X = data.drop('Outcome', axis=1)  # Replace 'target_column_name' with your actual target column
    Y = data['Outcome']
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.2, stratify=Y, random_state=2)
    classifier = svm.SVC(kernel='linear')
    classifier.fit(X_train, Y_train)
    val1 = float(request.GET['n1'])
    val2 = float(request.GET['n2'])
    val3 = float(request.GET['n3'])
    val4 = float(request.GET['n4'])
    val5 = float(request.GET['n5'])
    val6 = float(request.GET['n6'])
    val7 = float(request.GET['n7'])
    val8 = float(request.GET['n8'])


    pred = classifier.predict([[val1,val2,val3,val4,val5,val6,val7,val8]])
    result1 = ""
    if pred ==[1]:
        result1 = "Positive"
    else:
        result1 = "Negative"


    return render(request, 'webapp/predict.html', {"result2":result1})



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

    context = {'my_doctor': my_doctor}


    return render(request, 'webapp/doctor.html', context=context)

#dashboard

@login_required(login_url='my-login')

def patient(request):

    my_patient = Patient.objects.all()

    context = {'patient': my_patient}


    return render(request, 'webapp/patient.html', context=context)

#dashboard

@login_required(login_url='my-login')

def administrators(request):

    my_administrators = Administrator.objects.all()

    context = {'administrators': my_administrators}


    return render(request, 'webapp/administrator.html', context=context)

#dashboard

@login_required(login_url='my-login')

def medical_record(request):

    my_MedicalRecord = MedicalRecord.objects.all()

    context = {'my_MedicalRecord': my_MedicalRecord}


    return render(request, 'webapp/medical-record.html', context=context)

@login_required(login_url='my-login')

def Comment(request):

    my_Comment = Comment.objects.all()

    context = {'my_Comment': my_Comment}


    return render(request, 'webapp/medical-record.html', context=context)


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

#cre
@login_required(login_url='my-login')
def create_medical_record(request):
    form = MedicalRecordForm()

    if request.method == 'POST':
        form = MedicalRecordForm(request.POST)
        if form.is_valid():
            medical_record = form.save(commit=False)
            medical_record.user = request.user  # Assuming you are using Django's built-in User model
            medical_record.save()
            messages.success(request, "Medical record created successfully!")
            return redirect("medical-record")

    context = {'form': form}
    return render(request, 'webapp/create-medical-record.html', context=context)


@login_required(login_url='my-login')
def update_medical_record(request, pk):
    medical_record = MedicalRecord.objects.get(id=pk)
    form = MedicalRecordForm(instance=medical_record)

    if request.method == 'POST':
        form = MedicalRecordForm(request.POST, instance=medical_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Medical record updated successfully!")
            return redirect("medical-record")

    context = {'form': form}
    return render(request, 'webapp/update-medical-record.html', context=context)


@login_required(login_url='my-login')
def delete_medical_record(request, pk):
    medical_record = MedicalRecord.objects.get(id=pk)

    if request.method == 'POST':
        medical_record.delete()
        messages.success(request, "Medical record deleted successfully!")
        return redirect("medical-record")

    context = {'medical_record': medical_record}
    return render(request, 'webapp/delete-medical-record.html', context=context)




# Similar views for create, update, and delete comment and diabetes prediction

#cre
@login_required(login_url='my-login')
def create_comment(request):
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Comment created successfully!")
            return redirect("comment")

    context = {'form': form}
    return render(request, 'webapp/create-comment.html', context=context)


@login_required(login_url='my-login')
def update_comment(request, pk):
    comment = Comment.objects.get(id=pk)
    form = CommentForm(instance=comment)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, "Comment updated successfully!")
            return redirect("comment")

    context = {'form': form}
    return render(request, 'webapp/update-comment.html', context=context)


@login_required(login_url='my-login')
def delete_comment(request, pk):
    comment = Comment.objects.get(id=pk)

    if request.method == 'POST':
        comment.delete()
        messages.success(request, "Comment deleted successfully!")
        return redirect("comment")

    context = {'comment': comment}
    return render(request, 'webapp/delete-comment.html', context=context)






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
    context = {'doctor': [selected_doctor]}

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


with open('C:/Users/annwa/AI/model_pickle', 'rb') as model_file:

    model_pickle = pickle.load(model_file)

def make_prediction(data):
    try:
        # Create a DataFrame from the form data
        features_df = pd.DataFrame(data, index=[0])

        # Apply the scaler to the features
        features_scaled = ScalarType.transform(features_df)

        # Make predictions using the loaded model
        prediction = model_pickle.predict(features_scaled)[0]

        return prediction

    except Exception as e:
        print(f"Error in make_prediction: {e}")
        return None


def prediction(request):
    prediction_result = None

    if request.method == 'POST':
        form = UserPredictionForm(request.POST)
        if form.is_valid():
            try:
                # Get the form data and make predictions
                data = {
                    'Pregnancies': form.cleaned_data['pregnancies'],
                    'Glucose': form.cleaned_data['glucose'],
                    'BloodPressure': form.cleaned_data['blood_pressure'],
                    'SkinThickness': form.cleaned_data['skin_thickness'],
                    'Insulin': form.cleaned_data['insulin'],
                    'BMI': form.cleaned_data['bmi'],
                    
                    'Age': form.cleaned_data['age'],
                    'Outcome': form.cleaned_data['outcome'],
                }

                # Make predictions
                raw_prediction = make_prediction(data)

                # Map raw prediction to human-readable labels
                prediction_result = "Presence of Diabetes" if raw_prediction == 1 else "Absence of Diabetes"

                # Save the prediction result in the database
                # patient = form.cleaned_data['patient']
                # user_prediction = Prediction(
                #     patient=patient, 
                #     doctor=request.user,
                #     name=f"{patient.first_name} {patient.last_name}", 
                #     **data
                # )
                # user_prediction.save()

                # Add a success message with the prediction result
                messages.success(request, f'The prediction result is: {prediction_result}')

            except Exception as e:
                print(f"Error during prediction: {e}")
                messages.error(request, 'An error occurred during prediction. Please try again.')

            # Redirect to the same page after form submission
            return redirect('prediction')

    else:
        form = UserPredictionForm()

    return render(request, 'webapp/prediction.html', {'form': form, 'prediction': prediction_result})

def prediction_view(request):
    prediction_instance = Prediction.objects.get(id=1)
    result = prediction_instance.outcome  # Replace 'outcome' with the actual attribute name
    return render(request, 'webapp/prediction.html', {'result': result})







#user logout
def user_logout(request):

    auth.logout(request)

    messages.success(request, "You have logged out successfully!")

    return redirect("my-login")



