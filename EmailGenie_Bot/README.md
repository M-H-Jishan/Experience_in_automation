# EmailGenie Bot

AI-powered personalized email generator with user profiles and OpenAI GPT.

## Features

- Generate personalized cold emails from user profiles
- Create/update user profiles via API
- SQLAlchemy database for profile storage
- Web UI interface
- REST API endpoints

## Quick Start

```bash
cp .env.example .env  # Add your OPENAI_API_KEY
pip install -r requirements.txt
python app.py
```

Visit http://localhost:5000

## API

### POST /create_profile

```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "profile_data": "Software engineer with 5 years experience"
}
```

### POST /generate_email

```json
{"email": "john@example.com"}
```

## Docker

```bash
docker build -t emailgenie-bot .
docker run -p 5000:5000 --env-file .env emailgenie-bot
```

## Testing

```bash
pytest -v
```
