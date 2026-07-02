# Gift Idea Generator

AI-powered personalized gift recommendation engine using OpenAI GPT.

## Features

- Generate 3 personalized gift ideas based on recipient profile
- Related product suggestions from inventory
- Web UI with form input
- REST API endpoint
- Health check

## Quick Start

```bash
cp .env.example .env  # Add your OPENAI_API_KEY
cd backend
pip install -r requirements.txt
python app.py
```

Visit http://localhost:5000

## API

### POST /generate_gifts

```json
{
  "age": 30,
  "gender": "female",
  "relation": "sister",
  "interests": "reading, cooking",
  "budget": 50,
  "occasion": "birthday"
}
```

### GET /health

Returns `{"status": "healthy"}`

## Docker

```bash
docker build -t gift-idea-generator .
docker run -p 5000:5000 --env-file .env gift-idea-generator
```

## Testing

```bash
pytest -v
```
