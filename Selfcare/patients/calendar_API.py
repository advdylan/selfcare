from decouple import config
from google.oauth2 import service_account
import googleapiclient.discovery
import datetime

CAL_ID = config('https://calendar.google.com/calendar/ical/selfcaresoftware%40gmail.com/private-4c771c33a8dc8f670335d2bafddf8c46/basic.ics')
SCOPES = ['https://www.googleapis.com/auth/calendar']
SERVICE_ACCOUNT_FILE = './credentials.json'



def test_calendar():
    print("RUNNING TEST_CALENDAR()")
    test_event1 = {"start": {"date": "2022-01-01"}, "end": {"date": "2022-01-07"}, "summary":"test event 1"}
    test_event2 = {"start": {"date": "2022-02-01"}, "end": {"date": "2022-02-07"}, "summary":"test event 2"}
    events = [test_event1, test_event2]

    return events