from unittest.mock import patch, MagicMock
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestLangSwitch:
    def test_index_route(self):
        from app import app
        with app.test_client() as c:
            res = c.get("/")
            assert res.status_code == 200

    def test_translate_missing_text(self):
        from app import app
        with app.test_client() as c:
            res = c.post("/translate", json={"target_lang": "es"})
            assert res.status_code == 400

    def test_translate_no_api_key(self):
        from app import app
        with app.test_client() as c:
            with patch("app.client", None):
                res = c.post("/translate", json={"text": "hello", "target_lang": "es"})
                assert res.status_code == 500

    def test_translate_success(self):
        from app import app
        mock_client = MagicMock()
        mock_response = MagicMock()
        mock_response.choices = [MagicMock()]
        mock_response.choices[0].message.content = "hola"
        mock_client.chat.completions.create.return_value = mock_response

        with app.test_client() as c:
            with patch("app.client", mock_client):
                res = c.post("/translate", json={"text": "hello", "source_lang": "en", "target_lang": "es"})
                assert res.status_code == 200
                assert res.json["translation"] == "hola"

    def test_translate_empty_text(self):
        from app import app
        with app.test_client() as c:
            res = c.post("/translate", json={"text": "", "target_lang": "es"})
            assert res.status_code == 400
