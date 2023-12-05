from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("meetings", views.meetings, name="meetings"),
    path("patients", views.patients, name="patients"),
    path("patient/<str:pk>", views.patient, name="patient"),
    path("newpatient", views.newpatient, name="newpatient"),
    path("newmeeting", views.newmeeting, name="newmeeting"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("meeting/<str:pk>", views.meeting, name="meeting")
]
