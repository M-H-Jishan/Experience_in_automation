from unittest.mock import patch, MagicMock
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "backend"))


class TestGiftIdeaGenerator:
    def test_health(self):
        from app import app
        with app.test_client() as c:
            res = c.get("/health")
            assert res.status_code == 200

    def test_generate_gifts_missing_fields(self):
        from app import app
        with app.test_client() as c:
            res = c.post("/generate_gifts", json={"age": 25})
            assert res.status_code == 400

    def test_generate_gifts_no_api_key(self):
        from app import app
        with app.test_client() as c:
            with patch("app.client", None):
                res = c.post("/generate_gifts", json={
                    "age": 25, "gender": "male", "relation": "friend",
                    "interests": "tech", "budget": 50, "occasion": "birthday",
                })
                assert res.status_code == 500

    def test_generate_gifts_success(self):
        from app import app
        mock_client = MagicMock()
        mock_response = MagicMock()
        mock_response.choices = [MagicMock()]
        mock_response.choices[0].message.content = '{"gift1": {"name": "Widget", "description": "Cool", "reason": "Fun", "category": "Electronics"}}'
        mock_client.chat.completions.create.return_value = mock_response

        with app.test_client() as c:
            with patch("app.client", mock_client):
                res = c.post("/generate_gifts", json={
                    "age": 25, "gender": "male", "relation": "friend",
                    "interests": "tech", "budget": 50, "occasion": "birthday",
                })
                assert res.status_code == 200
                assert "gift1" in res.json

    def test_search_products(self):
        from inventory import search_products
        results = search_products("Electronics", "Widget", 50.0)
        assert len(results) == 3
        assert all("name" in r and "price" in r for r in results)
