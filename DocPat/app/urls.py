from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("patient/", views.patient, name="patient"),
    path("patient/new/", views.patient_new, name="patient_new"),
    path("doctor/", views.doctor, name="doctor"),
]