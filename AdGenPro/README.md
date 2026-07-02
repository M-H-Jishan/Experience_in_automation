# AdGenPro

AI-powered job advertisement generator using OpenAI GPT.

## Features

- Generate professional job ads from company career page + job description
- Web UI with real-time generation
- REST API endpoint for integration

## Quick Start

```bash
cp .env.example .env  # Add your OPENAI_API_KEY
pip install -r requirements.txt
python app.py
```

Visit http://localhost:5000

## API

### POST /generate_ad

```json
{
  "career_page": "https://company.com/careers",
  "job_description": "Senior Software Engineer with 5+ years..."
}
```

## Docker

```bash
docker build -t adgenpro .
docker run -p 5000:5000 --env-file .env adgenpro
```

## Testing

```bash
pytest -v
```
