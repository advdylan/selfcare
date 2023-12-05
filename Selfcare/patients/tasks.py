from celery import shared_task
from django.core.mail import send_mail
from celery import shared_task
from sms import send_sms
from django.utils import timezone, dateformat, datetime_safe



@shared_task
def send_sms_to_customer():

    phone_number = "+48501740899"
    message = f"Z tej strony system Selfcare. Dzisiaj masz spotkanie - to jest wiadomość próbna "

    send_sms(phone_number, message)