import os
import sys
from unittest.mock import patch, MagicMock

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestGroceryChatbot:
    def test_health(self):
        from main import app
        with app.test_client() as c:
            res = c.get("/health")
            assert res.status_code == 200

    def test_index(self):
        from main import app
        with app.test_client() as c:
            res = c.get("/")
            assert res.status_code == 200

    def test_chat_missing_message(self):
        from main import app
        with app.test_client() as c:
            res = c.post("/chat", json={})
            assert res.status_code == 400

    def test_chat_success(self):
        from main import app
        mock_bot = MagicMock()
        mock_bot.respond.return_value = "Hello!"
        with app.test_client() as c:
            with patch("main.get_chatbot", return_value=mock_bot):
                res = c.post("/chat", json={"message": "hi"})
                assert res.status_code == 200
                assert res.json["response"] == "Hello!"

    def test_chat_empty_message(self):
        from main import app
        with app.test_client() as c:
            res = c.post("/chat", json={"message": ""})
            assert res.status_code == 400
