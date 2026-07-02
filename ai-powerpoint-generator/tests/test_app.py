import os
import sys
from unittest.mock import patch, MagicMock

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestOpenAIHelper:
    def test_get_client_no_key(self):
        from utils.openai_helper import _client
        if _client is None:
            from utils.openai_helper import get_client
            try:
                get_client()
                assert False, "Should have raised"
            except ValueError:
                pass


class TestSlideGenerator:
    def test_generate_slide_titles_mock(self):
        mock_client = MagicMock()
        mock_response = MagicMock()
        mock_response.choices = [MagicMock()]
        mock_response.choices[0].message.content = "1. Introduction\n2. History\n3. Future"
        mock_client.chat.completions.create.return_value = mock_response

        with patch("utils.openai_helper._client", mock_client):
            from app.slide_generator import generate_slide_titles
            titles = generate_slide_titles("AI", 3)
            assert len(titles) == 3

    def test_generate_slide_content_mock(self):
        mock_client = MagicMock()
        mock_response = MagicMock()
        mock_response.choices = [MagicMock()]
        mock_response.choices[0].message.content = "Point 1\nPoint 2\nPoint 3"
        mock_client.chat.completions.create.return_value = mock_response

        with patch("utils.openai_helper._client", mock_client):
            from app.slide_generator import generate_slide_content
            content = generate_slide_content("AI", "Introduction")
            assert len(content) == 3


class TestPresentationBuilder:
    def test_create_presentation_no_template(self):
        mock_titles = ["Slide 1", "Slide 2"]
        mock_content = ["Point A", "Point B"]

        with patch("app.presentation_builder.generate_slide_titles", return_value=mock_titles):
            with patch("app.presentation_builder.generate_slide_content", return_value=mock_content):
                with patch("app.presentation_builder.generate_image", side_effect=Exception("skip")):
                    from app.presentation_builder import create_presentation
                    prs = create_presentation("Test Topic", 2, None)
                    assert len(prs.slides) == 2
