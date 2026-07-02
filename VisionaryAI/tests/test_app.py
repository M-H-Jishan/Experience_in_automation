from unittest.mock import patch, MagicMock
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestVisionaryAI:
    def test_index_route(self):
        from app import app
        with app.test_client() as c:
            res = c.get("/")
            assert res.status_code == 200

    def test_generate_image_missing_description(self):
        from app import app
        with app.test_client() as c:
            res = c.post("/generate_image", json={})
            assert res.status_code == 400

    def test_generate_image_no_api_key(self):
        from app import app
        with app.test_client() as c:
            with patch("app.client", None):
                res = c.post("/generate_image", json={"description": "a cat"})
                assert res.status_code == 500

    def test_generate_image_success(self):
        from app import app
        mock_client = MagicMock()
        mock_response = MagicMock()
        mock_response.data = [MagicMock()]
        mock_response.data[0].url = "https://example.com/image.png"
        mock_client.images.generate.return_value = mock_response

        with app.test_client() as c:
            with patch("app.client", mock_client):
                res = c.post("/generate_image", json={"description": "a beautiful sunset"})
                assert res.status_code == 200
                assert "image_url" in res.json

    def test_generate_image_empty_description(self):
        from app import app
        with app.test_client() as c:
            res = c.post("/generate_image", json={"description": ""})
            assert res.status_code == 400
