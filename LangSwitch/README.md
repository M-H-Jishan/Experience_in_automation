# LangSwitch

AI-powered language translator using OpenAI GPT.

## Features

- Translate text between multiple languages
- Auto-detect source language
- Web UI with language selectors
- REST API endpoint

## Quick Start

```bash
cp .env.example .env  # Add your OPENAI_API_KEY
pip install -r requirements.txt
python app.py
```

Visit http://localhost:5000

## API

### POST /translate

```json
{
  "text": "Hello, how are you?",
  "source_lang": "auto",
  "target_lang": "es"
}
```

## Docker

```bash
docker build -t langswitch .
docker run -p 5000:5000 --env-file .env langswitch
```

## Testing

```bash
pytest -v
```
