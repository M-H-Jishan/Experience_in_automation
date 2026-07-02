from unittest.mock import patch, MagicMock
import io
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "backend"))


class TestDepthForge:
    def test_health(self):
        from app import app
        with app.test_client() as c:
            res = c.get("/health")
            assert res.status_code == 200

    def test_upload_no_file(self):
        from app import app
        with app.test_client() as c:
            res = c.post("/upload", data={})
            assert res.status_code == 400

    def test_upload_empty_filename(self):
        from app import app
        with app.test_client() as c:
            data = {"file": (io.BytesIO(b""), "")}
            res = c.post("/upload", data=data, content_type="multipart/form-data")
            assert res.status_code == 400

    def test_upload_no_token(self):
        from app import app
        with app.test_client() as c:
            with patch("app.SKETCHFAB_API_TOKEN", ""):
                data = {"file": (io.BytesIO(b"fake"), "model.obj")}
                res = c.post("/upload", data=data, content_type="multipart/form-data")
                assert res.status_code == 500

    def test_upload_success(self):
        from app import app
        with app.test_client() as c:
            with patch("app.SKETCHFAB_API_TOKEN", "fake_token"):
                with patch("app.upload_to_sketchfab", return_value={"uid": "abc123"}):
                    data = {"file": (io.BytesIO(b"fake"), "model.obj")}
                    res = c.post("/upload", data=data, content_type="multipart/form-data")
                    assert res.status_code == 200
