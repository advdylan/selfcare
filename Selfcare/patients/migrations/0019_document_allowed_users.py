# Generated by Django 4.0 on 2024-02-03 07:27

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('patients', '0018_rename_user_document_user_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='allowed_users',
            field=models.ManyToManyField(related_name='allowed_users', to=settings.AUTH_USER_MODEL),
        ),
    ]
