from unittest.mock import patch, MagicMock
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestCustomerServiceChatbot:
    def test_index_route(self):
        from app import app
        with app.test_client() as c:
            res = c.get("/")
            assert res.status_code == 200

    def test_health(self):
        from app import app
        with app.test_client() as c:
            res = c.get("/health")
            assert res.status_code == 200
            assert res.json["status"] == "healthy"

    def test_chat_missing_message(self):
        from app import app
        with app.test_client() as c:
            res = c.post("/chat", json={})
            assert res.status_code == 400

    def test_chat_no_api_key(self):
        from app import app
        with app.test_client() as c:
            with patch("app.client", None):
                res = c.post("/chat", json={"message": "hello"})
                assert res.status_code == 500

    def test_chat_success(self):
        from app import app
        mock_client = MagicMock()
        mock_response = MagicMock()
        mock_response.choices = [MagicMock()]
        mock_response.choices[0].message.content = "Here is your answer."
        mock_client.chat.completions.create.return_value = mock_response

        with app.test_client() as c:
            with patch("app.client", mock_client):
                res = c.post("/chat", json={"message": "What are your hours?"})
                assert res.status_code == 200
                assert "response" in res.json

    def test_chat_empty_message(self):
        from app import app
        with app.test_client() as c:
            res = c.post("/chat", json={"message": ""})
            assert res.status_code == 400
