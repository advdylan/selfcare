from django.db import models

# Create your models here.

class Doctors(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    proteges = models.ForeignKey('Patients', on_delete=models.CASCADE, related_name="Patients")

class Patients(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    curator = models.ForeignKey(Doctors, on_delete=models.CASCADE, related_name="Doctor")


    def __str__(self):
        return f"{self.first_name} {self.last_name}, address: {self.address}, phone_number: {self.phone_number}"



