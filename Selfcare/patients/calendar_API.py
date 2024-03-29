from dateutil.parser import parse
from decouple import config
from datetime import datetime, timedelta
from google.oauth2 import service_account
from uuid import uuid4
from .models import Doctor, Patient, Meetings
from .helpers import extract
import googleapiclient.discovery
import datetime
import json

#dokończ to jutro. Edytuj dane podane poniżej z Twoich form NewMeeting
#Google Meets works only for Workspace users. I'm not 

CAL_ID = config('CAL_ID')
SCOPES = ['https://www.googleapis.com/auth/calendar']
SERVICE_ACCOUNT_FILE = './google-credentials.json'




def test_calendar():
    print("RUNNING TEST_CALENDAR()")

    credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = googleapiclient.discovery.build('calendar', 'v3', credentials=credentials)

    # CREATE A NEW EVENT
    new_event = {
    'summary': "Ben Hammond Tech's Super Awesome Event",
    'location': 'Denver, CO USA',
    'description': 'https://benhammond.tech',
    'start': {
        'date': f"{datetime.date.today()}",
        'timeZone': 'America/New_York',
    },
    'end': {
        'date': f"{datetime.date.today() + datetime.timedelta(days=3)}",
        'timeZone': 'America/New_York',
    },
    }
    service.events().insert(calendarId=CAL_ID, body=new_event).execute()
    print('Event created')

 # GET ALL EXISTING EVENTS
    events_result = service.events().list(calendarId=CAL_ID, maxResults=2500).execute()
    events = events_result.get('items', [])

    # LOG THEM ALL OUT IN DEV TOOLS CONSOLE
    for e in events:

        #print(e)

    #uncomment the following lines to delete each existing item in the calendar
        event_id = e['id']
        service.events().delete(calendarId=CAL_ID, eventId=event_id).execute()


    return events

def new_event(location, description, start, end, doctor, patient):

    #this function adds a new event into Google Calendar

    credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = googleapiclient.discovery.build('calendar', 'v3', credentials=credentials)
    end = start + timedelta(hours=1)
    doctor_mail = doctor.email
    patient_mail = patient.email

    new_event = {
        
        'summary': f'{doctor} - {location}',
        'location': location,
        'description': description,
        'start': {
            'dateTime': start.isoformat(),
            'timeZone': 'Europe/Warsaw',
        },
        'end': {
            'dateTime': end.isoformat(),
            'timeZone': 'Europe/Warsaw'
        },
        'colorId': '4',     
    }

    try:
        service.events().insert(calendarId=CAL_ID, body=new_event, conferenceDataVersion=1).execute()
    except Exception as e:
        print(f"Error: {e}")


def fetch_calendar():
    credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = googleapiclient.discovery.build('calendar', 'v3', credentials=credentials)

    events = service.events().list(
    calendarId=CAL_ID,  
    maxResults=1000,  # adjust this value as needed
    singleEvents=True,
    orderBy='startTime'
    ).execute()


    return events

def parse_calendar(request,events):

    data_dict = events
    items = data_dict.get('items')
    kind = data_dict.get('kind')
    etag = data_dict.get('etag')
    summary = data_dict.get('summary')
    description = data_dict.get('description')
    updated = data_dict.get('updated')
    timeZone = data_dict.get('timeZone')
    accessRole = data_dict.get('accessRole')
    defaultReminders = data_dict.get('defaultReminders')

    for item in items:
        item_kind = item.get('kind')
        item_etag = item.get('etag')
        item_id = item.get('id')
        item_status = item.get('status')
        item_htmlLink = item.get('htmlLink')
        item_created = item.get('created')
        item_updated = item.get('updated')
        item_summary = item.get('summary')
        item_description = item.get('description')
        item_location = item.get('location')
        item_creator = item.get('creator')
        item_organizer = item.get('organizer')
        item_start = item.get('start')
        item_end = item.get('end')
        item_iCalUID = item.get('iCalUID')
        item_sequence = item.get('sequence')
        item_reminders = item.get('reminders')
        item_eventType = item.get('eventType')

        #print(item_description)
        doctor, patient = extract(request, item_description)
        extract(request, item_description)
        
        start_time = parse(item_start['dateTime'])
        end_time = parse(item_end['dateTime'])
        #print(f"Lekarz id: {doctor}, Pacjent id: {patient}")

        print(start_time, end_time)
       
       
        #add it to the Django Database
        meeting = Meetings.objects.create(
            meeting_place = item_location,
            start_time = start_time,
            end_time = end_time,
            doctor = doctor,
            patient = patient
        )
        meeting.save()
    

    # Return the extracted data
    return kind, etag, summary, description, updated, timeZone, accessRole, defaultReminders, items


def get_settings():

    credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = googleapiclient.discovery.build('calendar', 'v3', credentials=credentials)

    #setting = service.settings().get(setting='conferenceProperties.allowedConferenceSolutionTypes[]').execute()
    #print(setting['id'], setting['value'])

    #calendar = service.calendars().get(calendarId='primary').execute()
    #print(calendar['summary'])

    

    settings = service.settings().list().execute()

    for setting in settings['items']:
        print(setting['id'], setting['value'])
    
