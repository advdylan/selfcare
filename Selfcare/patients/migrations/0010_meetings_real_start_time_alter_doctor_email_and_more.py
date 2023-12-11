# Generated by Django 4.2.7 on 2023-12-05 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0009_doctor_email_patient_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetings',
            name='real_start_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='patient',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]