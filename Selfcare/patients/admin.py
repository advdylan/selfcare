from django.contrib import admin
from.models import Patient, Doctor, Meetings

class MeetingsAdmin(admin.ModelAdmin):
    list_display = ("meeting_place", "duration", "doctor","patient")

class PatientsAdmin(admin.ModelAdmin):
    filter_horizontal = ("meetings",)

admin.site.register(Doctors)
admin.site.register(Meetings, MeetingsAdmin)


