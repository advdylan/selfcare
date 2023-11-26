# Generated by Django 4.2.7 on 2023-11-26 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0006_alter_meetings_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetings',
            name='progress',
            field=models.CharField(choices=[('Zakończone', 'Zakończone'), ('W trakcie', 'W trakcie'), ('Nierozpoczęte', 'Nierozpoczęte')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='meetings',
            name='meeting_place',
            field=models.CharField(choices=[('Biuro', 'Biuro'), ('Zdalnie', 'Zdalnie')], max_length=100, null=True),
        ),
    ]
