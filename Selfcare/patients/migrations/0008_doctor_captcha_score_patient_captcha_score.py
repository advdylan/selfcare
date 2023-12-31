# Generated by Django 5.0 on 2023-12-20 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0007_alter_doctor_proteges_alter_patient_curator'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='captcha_score',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='patient',
            name='captcha_score',
            field=models.FloatField(default=0.0),
        ),
    ]
