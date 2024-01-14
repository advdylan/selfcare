# Generated by Django 5.0 on 2024-01-14 16:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('patients', '0009_doctor_group_patient_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='doctos', to='auth.group'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='patients', to='auth.group'),
        ),
    ]
