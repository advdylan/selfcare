from django.db import models
from django.db.models import F
from datetime import timedelta

# Create your models here.

class Doctor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    proteges = models.ManyToManyField('Patient',blank=True, related_name="Patients")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    curator = models.ManyToManyField(Doctor, related_name="Doctor")


    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Meetings(models.Model):
    MEETING_TYPE = (
        ('Office', 'Office'),
        ('Remote', ' Remote'),
    )

    meeting_place = models.CharField(max_length=100, null=True, choices=MEETING_TYPE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    duration = models.DurationField(null=True, blank=True)
    doctor = models.ForeignKey(Doctor, null=True, on_delete=models.SET_NULL)
    patient = models.ForeignKey(Patient, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"ID: {self.id} Doctor: {self.doctor}, Patient: {self.patient}"


    def save(self,*args, **kwargs):
        if self.end_time <= self.start_time:
            raise ValueError("End time must be after the start time")
        
        self.duration = self.end_time - self.start_time
        super(Meetings,self).save(*args,**kwargs)

    

    