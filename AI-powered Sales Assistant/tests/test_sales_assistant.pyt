import unittest
from unittest.mock import MagicMock
import pandas as pd
from datetime import datetime
from src.sales_assistant import SalesAssistant

class TestSalesAssistant(unittest.TestCase):
    def setUp(self):
        self.lead_gen = MagicMock()
        self.email_automation = MagicMock()
        self.meeting_scheduler = MagicMock()
        self.recommendation_engine = MagicMock()
        self.sales_assistant = SalesAssistant(
            self.lead_gen, 
            self.email_automation, 
            self.meeting_scheduler, 
            self.recommendation_engine
        )

    def test_process_leads(self):
        potential_leads = pd.DataFrame({
            'email': ['test1@example.com', 'test2@example.com'],
            'feature1': [1, 2],
            'feature2': [3, 4]
        })
        self.lead_gen.generate_leads.return_value = potential_leads
        self.recommendation_engine.get_recommendations.return_value = "Test recommendation"

        self.sales_assistant.process_leads(potential_leads)

        self.lead_gen.generate_leads.assert_called_once_with(potential_leads)
        self.assertEqual(self.email_automation.send_email.call_count, 2)
        self.assertEqual(self.recommendation_engine.get_recommendations.call_count, 2)

    def test_schedule_follow_up(self):
        start_time = datetime(2023, 1, 1, 10, 0)
        end_time = datetime(2023, 1, 1, 11, 0)
        self.meeting_scheduler.schedule_meeting.return_value = {'id': 'test_meeting_id'}

        result = self.sales_assistant.schedule_follow_up('test@example.com', start_time, end_time)

        self.meeting_scheduler.schedule_meeting.assert_called_once_with(
            'Follow-up Call', 
            start_time, 
            end_time, 
            ['test@example.com']
        )
        self.assertEqual(result, {'id': 'test_meeting_id'})

if __name__ == '__main__':
    unittest.main()