from django.urls import path
from . import views, helpers

urlpatterns = [
    path("", views.index, name="index"),
    path("meetings", views.meetings, name="meetings"),
    path("patients", views.patients, name="patients"),
    path("patient/<str:pk>", views.patient, name="patient"),
    path("newpatient", views.newpatient, name="newpatient"),
    path("newmeeting", views.newmeeting, name="newmeeting"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("meeting/<str:pk>", views.meeting, name="meeting"),
    path('newdoctor', views.newdoctor, name="newdoctor"),
    path('doctors', views.doctors, name="doctors"),
    path("doctor/<str:pk>", views.doctor, name="doctor"),
    path('calendar', views.calendar, name="calendar"),
    path('synchro', views.synchro, name="synchro"),
    path('apisettings', views.apisettings, name="apisettings"),
    path('permissions', views.permissions, name="permissions"),
    path('doctors_meetings', views.doctors_meetings, name="doctors_meetings"),
    path('end_meeting', views.end_meeting, name="end_meeting"),
    path('start_meeting', views.start_meeting, name="start_meeting"),
    path('upload_images', views.upload_images, name="upload_images"),
    path('upload_files', views.upload_files, name='upload_files'),
    path('add_permission', helpers.add_permission, name="add_permission")
]
