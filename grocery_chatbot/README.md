# Grocery Chatbot

NLP-powered grocery shopping assistant with cart management and checkout.

## Features

- NLP processing with spaCy for intent detection
- State machine dialogue management (greeting → inquiring → shopping → checkout)
- SQLite database for product inventory
- Cart management (add items, view cart, checkout)
- Stripe payment integration
- Flask web interface

## Quick Start

```bash
cp .env.example .env  # Add your Stripe API key
pip install -r requirements.txt
python -m spacy download en_core_web_sm
python main.py
```

Visit http://localhost:5000

## API

### POST /chat

```json
{"message": "What's the price of milk?"}
```

### GET /health

Returns `{"status": "healthy"}`

## Architecture

| Module | Description |
|--------|-------------|
| `chatbot.bot` | Main chatbot orchestrator |
| `chatbot.nlp_processor` | spaCy-based intent extraction |
| `chatbot.dialogue_manager` | State machine for conversation flow |
| `chatbot.payment_processor` | Stripe payment integration |
| `database.db_manager` | Product inventory CRUD |
| `database.models` | SQLAlchemy Product model |

## Docker

```bash
docker build -t grocery-chatbot .
docker run -p 5000:5000 --env-file .env grocery-chatbot
```

## Testing

```bash
pytest -v
```
