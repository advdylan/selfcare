from decouple import config
from datetime import datetime, timedelta
from google.oauth2 import service_account
import googleapiclient.discovery
import datetime
#dokończ to jutro. Edytuj dane podane poniżej z Twoich form NewMeeting

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

def new_event(location, description, start, end, doctor):

    credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = googleapiclient.discovery.build('calendar', 'v3', credentials=credentials)
    end = start + timedelta(hours=1)

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
        'colorId': '5'
    }


    service.events().insert(calendarId=CAL_ID, body=new_event).execute()

    def sync(request):
    # Fetch all meetings from your database
    meetings = Meetings.objects.all()

    # Fetch all events from the Google Calendar
    events = fetch_events()

    # For each meeting in the database, check if it exists in the Google Calendar
    for meeting in meetings:
        if not event_exists(meeting, events):
            # If the meeting does not exist in the Google Calendar, add it
            add_event(meeting)

    # For each event in the Google Calendar, check if it exists in the database
    for event in events:
        if not meeting_exists(event, meetings):
            # If the event does not exist in the database, add it
            add_meeting(event)