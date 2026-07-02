# AI PowerPoint Generator

Automated presentation generator using OpenAI GPT and DALL-E, with Streamlit UI.

## Features

- AI-generated slide titles and content (GPT-4)
- AI-generated images for each slide (DALL-E 3)
- Configurable number of slides and templates
- Download generated `.pptx` files
- Streamlit web interface

## Quick Start

```bash
cp .env.example .env  # Add your OPENAI_API_KEY
pip install -r requirements.txt
streamlit run run.py
```

Visit http://localhost:8501

## Configuration

| Variable | Default | Description |
|----------|---------|-------------|
| `OPENAI_API_KEY` | — | OpenAI API key |
| `OPENAI_MODEL` | `gpt-4` | Chat model for titles/content |
| `OPENAI_IMAGE_MODEL` | `dall-e-3` | Image generation model |

## Docker

```bash
docker build -t ai-ppt-generator .
docker run -p 8501:8501 --env-file .env ai-ppt-generator
```

## Testing

```bash
pytest -v
```
