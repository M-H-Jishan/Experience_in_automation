from unittest.mock import patch, MagicMock
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestEmailGenieBot:
    def test_index_route(self):
        from app import app
        with app.test_client() as c:
            res = c.get("/")
            assert res.status_code == 200

    def test_generate_email_missing_email(self):
        from app import app
        with app.test_client() as c:
            res = c.post("/generate_email", json={})
            assert res.status_code == 400

    def test_generate_email_user_not_found(self):
        from app import app
        with app.test_client() as c:
            with patch("app.session") as mock_session:
                mock_session.query.return_value.filter_by.return_value.first.return_value = None
                res = c.post("/generate_email", json={"email": "nobody@test.com"})
                assert res.status_code == 404

    def test_generate_email_success(self):
        from app import app
        mock_user = MagicMock()
        mock_user.name = "John"
        mock_user.email = "john@test.com"
        mock_user.profile_data = "Software engineer"

        with app.test_client() as c:
            with patch("app.session") as mock_session:
                mock_session.query.return_value.filter_by.return_value.first.return_value = mock_user
                with patch("app.generate_email", return_value="Dear John..."):
                    res = c.post("/generate_email", json={"email": "john@test.com"})
                    assert res.status_code == 200
                    assert "email" in res.json

    def test_create_profile_missing_data(self):
        from app import app
        with app.test_client() as c:
            res = c.post("/create_profile", json={"name": "John"})
            assert res.status_code == 400

    def test_create_profile_success(self):
        from app import app
        mock_user = MagicMock()
        mock_user.id = 1
        with app.test_client() as c:
            with patch("app.session") as mock_session:
                mock_session.query.return_value.filter_by.return_value.first.return_value = None
                res = c.post("/create_profile", json={
                    "name": "John",
                    "email": "john@test.com",
                    "profile_data": "Engineer",
                })
                assert res.status_code == 201
