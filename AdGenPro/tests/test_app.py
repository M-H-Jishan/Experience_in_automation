from unittest.mock import patch, MagicMock
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestAdGenPro:
    def test_index_route(self):
        from app import app
        with app.test_client() as c:
            res = c.get("/")
            assert res.status_code == 200

    def test_generate_ad_missing_data(self):
        from app import app
        with app.test_client() as c:
            res = c.post("/generate_ad", json={})
            assert res.status_code == 400

    def test_generate_ad_no_api_key(self):
        from app import app, client
        with app.test_client() as c:
            with patch("app.client", None):
                res = c.post("/generate_ad", json={
                    "career_page": "https://example.com",
                    "job_description": "Software Engineer",
                })
                assert res.status_code == 500

    def test_generate_ad_success(self):
        from app import app
        mock_client = MagicMock()
        mock_response = MagicMock()
        mock_response.choices = [MagicMock()]
        mock_response.choices[0].message.content = "Great Job Ad!"
        mock_client.chat.completions.create.return_value = mock_response

        with app.test_client() as c:
            with patch("app.client", mock_client):
                res = c.post("/generate_ad", json={
                    "career_page": "https://example.com",
                    "job_description": "Software Engineer",
                })
                assert res.status_code == 200
                assert "job_ad" in res.json
                assert res.json["job_ad"] == "Great Job Ad!"

    def test_generate_ad_invalid_json(self):
        from app import app
        with app.test_client() as c:
            res = c.post("/generate_ad", data="not json", content_type="text/plain")
            assert res.status_code == 400
