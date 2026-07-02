from unittest.mock import patch, MagicMock
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestIntelliQueryBot:
    def test_index_route(self):
        from app import app
        with app.test_client() as c:
            res = c.get("/")
            assert res.status_code == 200

    def test_chatbot_missing_message(self):
        from app import app
        with app.test_client() as c:
            res = c.post("/chatbot", json={})
            assert res.status_code == 400

    def test_chatbot_no_api_key(self):
        from app import app
        with app.test_client() as c:
            with patch("app.client", None):
                res = c.post("/chatbot", json={"message": "hello"})
                assert res.status_code == 500

    def test_chatbot_success(self):
        from app import app
        mock_client = MagicMock()
        mock_response = MagicMock()
        mock_response.choices = [MagicMock()]
        mock_response.choices[0].message.content = "How can I help?"
        mock_client.chat.completions.create.return_value = mock_response

        with app.test_client() as c:
            with patch("app.client", mock_client):
                with patch("app.session") as mock_session:
                    mock_session.query.return_value.filter_by.return_value.first.return_value = None
                    res = c.post("/chatbot", json={"message": "What services do you offer?"})
                    assert res.status_code == 200
                    assert "response" in res.json

    def test_chatbot_empty_message(self):
        from app import app
        with app.test_client() as c:
            res = c.post("/chatbot", json={"message": ""})
            assert res.status_code == 400

    def test_chatbot_invalid_json(self):
        from app import app
        with app.test_client() as c:
            res = c.post("/chatbot", data="not json", content_type="text/plain")
            assert res.status_code == 400
