# Generated by Django 4.2.7 on 2023-11-22 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0004_alter_doctor_proteges'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='proteges',
            field=models.ManyToManyField(blank=True, related_name='Patients', to='patients.patient'),
        ),
    ]
