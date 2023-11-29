from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name=""),
    path('register', views.register, name="register"),
    path('my-login', views.my_login, name="my-login"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('medical-record', views.MedicalRecord, name="medical-record"),
    path('comment', views.Comment, name="comment"),
    path('prediction', views.Prediction, name="prediction"),
    
    
    path('user-logout', views.user_logout, name="user-logout"),
    

    #CRUD
    path('dashboard', views.dashboard, name="dashboard"),
    path('doctor', views.doctor, name="doctor"),
    path('patient', views.patient, name="patient"),
    path('administrator/', views.administrators, name="administrator"),
    path('medical-record/', views.medical_record, name="medical-record"),
    path('comment', views.Comment, name="comment"),

    path('create-record/', views.create_record, name="create-record"),
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

    path('create-medical-record/', views.create_medical_record, name='create-medical-record'),
    path('update-medical-record/<int:record_id>/', views.update_medical_record, name='update-medical-record'),
    path('delete-medical-record/<int:record_id>/', views.delete_medical_record, name='delete-medical-record'),

    path('create-comment/', views.create_comment, name='create-comment'),
    path('update-comment/<int:comment_id>/', views.update_comment, name='update-comment'),
    path('delete-comment/<int:comment_id>/', views.delete_comment, name='delete-comment'),



    



    
]