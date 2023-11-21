from django.db import models

# Create your models here.

class Patients(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_lenghts=30)
