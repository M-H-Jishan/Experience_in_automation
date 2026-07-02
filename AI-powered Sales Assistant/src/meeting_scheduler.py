from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build


class MeetingScheduler:
    def __init__(self, credentials: Credentials):
        self.service = build("calendar", "v3", credentials=credentials)

    def schedule_meeting(self, summary: str, start_time, end_time, attendees: list[str]) -> dict:
        event = {
            "summary": summary,
            "start": {"dateTime": start_time.isoformat()},
            "end": {"dateTime": end_time.isoformat()},
            "attendees": [{"email": attendee} for attendee in attendees],
        }
        return self.service.events().insert(calendarId="primary", body=event).execute()
