from django.db import models
from django.db.models import F
from datetime import timedelta, datetime
from django.utils import timezone, dateformat
from django.template.defaultfilters import date as _date
from django.contrib.auth.models import User, Group



class Doctor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    street = models.CharField(max_length=100, null=True)
    code = models.CharField(max_length=6, null=True)
    city = models.CharField(max_length = 40, null=True)
    phone_number = models.IntegerField()
    proteges = models.ManyToManyField('Patient',blank=True, related_name="proteges")
    email = models.EmailField(max_length=254)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor',null=True)
    captcha_score = models.FloatField(default = 0.0)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='doctos', null=True)

    class Meta:
        permissions = [
            ("doctor_permission", "doctor_permission")
            ]
        
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    


class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    street = models.CharField(max_length=100, null=True)
    code = models.CharField(max_length=15, null=True)
    city = models.CharField(max_length = 40, null=True)
    phone_number = models.IntegerField()
    curator = models.ManyToManyField(Doctor, related_name="curator")
    email = models.EmailField(max_length=254)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient', null=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='patients', null=True)
    captcha_score = models.FloatField(default = 0.0)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    



class Meetings(models.Model):
    MEETING_TYPE = (
        ('Biuro', 'Biuro'),
        ('Zdalnie', 'Zdalnie'),
    )

    MEETING_STATUS = (
        ('Zakończone', 'Zakończone'),
        ('W trakcie', 'W trakcie'),
        ('Nierozpoczęte', 'Nierozpoczęte')
    )

    meeting_place = models.CharField(max_length=100, null=True, choices=MEETING_TYPE)
    start_time = models.DateTimeField()
    real_start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    duration = models.DurationField(null=True, blank=True)
    doctor = models.ForeignKey(Doctor, null=True, on_delete=models.SET_NULL)
    patient = models.ForeignKey(Patient, null=True, on_delete=models.SET_NULL)
    progress = models.CharField(max_length=100, null=True, choices = MEETING_STATUS, blank=True)

    def __str__(self):
        return f"ID: {self.id} Doctor: {self.doctor}, Patient: {self.patient}"


    def save(self, *args, **kwargs):
        
        if self.end_time is not None:           
            if self.end_time <= self.start_time:
                raise ValueError("End time must be after the start time")
            
        if self.end_time:
            self.duration = self.end_time - self.start_time


        # Call the status method to update the progress field
        self.status()

        # Now save the object with the updated fields
        super(Meetings, self).save(*args, **kwargs)

    def status(self):
        #now = timezone.now()
        #formatted_now = _date(now, "SHORT_DATETIME_FORMAT")

        if not self.progress:  # Only set progress if it hasn't been set yet
            now = timezone.now()

            if self.start_time > now:
                self.progress = 'Nierozpoczęte'
            elif self.end_time and self.end_time < now:
                self.progress = 'Zakończone'
            else:
                self.progress = 'W trakcie'

            if self.end_time == None and self.progress == 'W trakcie':
                duration = now - self.start_time
                self.duration = duration


class Image(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    image = models.ImageField(upload_to='')


            

    

    