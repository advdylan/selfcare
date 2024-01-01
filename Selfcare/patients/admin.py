from django.contrib import admin
from.models import Patient, Doctor, Meetings

class MeetingsAdmin(admin.ModelAdmin):
    list_display = ("meeting_place", "duration", "doctor","patient", 'progress')

class PatientsAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name","email")
    #filter_horizontal = ("meetings")

class DoctorAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "email")

admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Patient, PatientsAdmin)
admin.site.register(Meetings, MeetingsAdmin)


