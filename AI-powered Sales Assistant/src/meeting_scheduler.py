from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

class MeetingScheduler:
    def __init__(self, credentials):
        self.service = build('calendar', 'v3', credentials=credentials)

    def schedule_meeting(self, summary, start_time, end_time, attendees):
        event = {
            'summary': summary,
            'start': {'dateTime': start_time.isoformat()},
            'end': {'dateTime': end_time.isoformat()},
            'attendees': [{'email': attendee} for attendee in attendees],
        }
        return self.service.events().insert(calendarId='primary', body=event).execute()

# Usage
credentials = Credentials.from_authorized_user_file('token.json', ['https://www.googleapis.com/auth/calendar'])
scheduler = MeetingScheduler(credentials)
scheduler.schedule_meeting('Sales Call', start_time, end_time, ['lead@example.com'])