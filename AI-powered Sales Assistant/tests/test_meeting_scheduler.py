import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime
from src.meeting_scheduler import MeetingScheduler

class TestMeetingScheduler(unittest.TestCase):
    def setUp(self):
        self.credentials = MagicMock()
        self.scheduler = MeetingScheduler(self.credentials)

    @patch('googleapiclient.discovery.build')
    def test_schedule_meeting(self, mock_build):
        mock_service = MagicMock()
        mock_build.return_value = mock_service

        start_time = datetime(2023, 1, 1, 10, 0)
        end_time = datetime(2023, 1, 1, 11, 0)
        attendees = ['attendee@example.com']

        self.scheduler.schedule_meeting('Test Meeting', start_time, end_time, attendees)

        mock_service.events().insert.assert_called_once()
        call_args = mock_service.events().insert.call_args[1]
        self.assertEqual(call_args['calendarId'], 'primary')
        self.assertEqual(call_args['body']['summary'], 'Test Meeting')
        self.assertEqual(call_args['body']['attendees'], [{'email': 'attendee@example.com'}])

if __name__ == '__main__':
    unittest.main()