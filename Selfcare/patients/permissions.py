from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import Doctor, Patient

doctors = Group.objects.get(name="doctors")
ct = ContentType.objects.get_for_model(Doctor)

permission = Permission.objects.create(codename = 'doctor_permission',
                                       name = 'doctor_permission',
                                            content_type = ct)

doctors.permissions.add(permission)