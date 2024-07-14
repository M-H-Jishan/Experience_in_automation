import unittest
from unittest.mock import patch, MagicMock
from src.email_automation import EmailAutomation

class TestEmailAutomation(unittest.TestCase):
    def setUp(self):
        self.email_automation = EmailAutomation('test@example.com', 'password')

    def test_generate_email(self):
        message = self.email_automation.generate_email('recipient@example.com', 'Test Subject', 'Test Body')
        self.assertEqual(message['From'], 'test@example.com')
        self.assertEqual(message['To'], 'recipient@example.com')
        self.assertEqual(message['Subject'], 'Test Subject')

    @patch('smtplib.SMTP')
    def test_send_email(self, mock_smtp):
        mock_server = MagicMock()
        mock_smtp.return_value.__enter__.return_value = mock_server

        self.email_automation.send_email('recipient@example.com', 'Test Subject', 'Test Body')

        mock_server.starttls.assert_called_once()
        mock_server.login.assert_called_once_with('test@example.com', 'password')
        mock_server.send_message.assert_called_once()

if __name__ == '__main__':
    unittest.main()