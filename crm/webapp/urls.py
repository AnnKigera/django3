from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name=""),
    path('register', views.register, name="register"),
    path('my-login', views.my_login, name="my-login"),
    path('dashboard', views.dashboard, name="dashboard"),
    
    path('user-logout', views.user_logout, name="user-logout"),
    

    #CRUD
    path('dashboard', views.dashboard, name="dashboard"),
    path('doctor', views.doctor, name="doctor"),
    path('patient', views.patient, name="patient"),
    path('administrator', views.administrator, name="administrator"),

    path('create-record', views.create_record, name="create-record"),
    path('create-doctor', views.create_doctor, name="create-doctor"),
    path('create-patient', views.create_patient, name="create-patient"),

    path('update-record/<int:pk>', views.update_record, name="update-record"),
    path('update-doctor/<int:pk>', views.update_doctor, name="update-doctor"),
    path('update-patient/<int:pk>', views.update_patient, name="update-patient"),

    path('record/<int:pk>', views.singular_record, name="record"),
    path('doctor/<int:pk>', views.singular_doctor, name="singular_doctor"),
    path('patient/<int:pk>', views.singular_patient, name="patient"),

    path('delete-record/<int:pk>', views.delete_record, name="delete-record"),
    path('delete-doctor/<int:pk>', views.delete_doctor, name="delete-doctor"),
    path('delete-patient/<int:pk>', views.delete_patient, name="delete-patient"),


    
]