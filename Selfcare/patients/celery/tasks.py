from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_reminder_email():
    # Fetch the doctors' emails and the meeting details from your database
    # Here's a basic example of how you can send an email in Django
    send_mail(
        'Meeting Reminder',
        'You have a meeting scheduled for today.',
        'from@example.com',
        ['doctor1@example.com', 'doctor2@example.com'],
        fail_silently=False,
    )