# Customer Service Chatbot

RAG-based customer support chatbot using OpenAI GPT and a knowledge base.

## Features

- Knowledge base-powered responses (RAG pattern)
- OpenAI GPT integration
- Web UI chat interface
- Health check endpoint
- Configurable knowledge base path

## Quick Start

```bash
cp .env.example .env  # Add your OPENAI_API_KEY
pip install -r requirements.txt
python app.py
```

Visit http://localhost:5000

## API

### POST /chat

```json
{"message": "What are your business hours?"}
```

### GET /health

Returns `{"status": "healthy"}`

## Knowledge Base

Edit `knowledge_base/Data.txt` with your business information. The chatbot uses this as context for answering questions.

## Docker

```bash
docker build -t customer-service-chatbot .
docker run -p 5000:5000 --env-file .env customer-service-chatbot
```

## Testing

```bash
pytest -v
```
