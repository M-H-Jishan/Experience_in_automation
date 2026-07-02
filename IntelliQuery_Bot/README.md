# IntelliQuery Bot

Intelligent query chatbot with user profiles and OpenAI GPT integration.

## Features

- AI-powered chatbot for service providers
- User profiles with service descriptions (SQLAlchemy)
- Context-aware responses based on user's service
- Web UI chat interface
- REST API endpoint

## Quick Start

```bash
cp .env.example .env  # Add your OPENAI_API_KEY
pip install -r requirements.txt
python app.py
```

Visit http://localhost:5000

## API

### POST /chatbot

```json
{
  "message": "What services do you offer?",
  "email": "user@example.com"
}
```

## Docker

```bash
docker build -t intelliquery-bot .
docker run -p 5000:5000 --env-file .env intelliquery-bot
```

## Testing

```bash
pytest -v
```
