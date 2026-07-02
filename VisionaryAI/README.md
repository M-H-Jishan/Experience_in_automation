# VisionaryAI

AI-powered text-to-image generator using OpenAI DALL-E.

## Features

- Generate high-quality images from text descriptions
- Web UI with real-time generation
- REST API endpoint

## Quick Start

```bash
cp .env.example .env  # Add your OPENAI_API_KEY
pip install -r requirements.txt
python app.py
```

Visit http://localhost:5000

## API

### POST /generate_image

```json
{"description": "A beautiful sunset over the ocean"}
```

## Docker

```bash
docker build -t visionaryai .
docker run -p 5000:5000 --env-file .env visionaryai
```

## Testing

```bash
pytest -v
```
