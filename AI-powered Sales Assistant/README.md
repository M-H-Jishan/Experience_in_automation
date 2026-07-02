# AI-powered Sales Assistant

ML-powered lead generation, email automation, meeting scheduling, and recommendation engine.

## Features

- **Lead Generation**: RandomForest classifier to score and filter leads
- **Email Automation**: Automated personalized email sending via SMTP
- **Meeting Scheduling**: Google Calendar integration for follow-up calls
- **Recommendation Engine**: KMeans clustering for customer segmentation

## Quick Start

```bash
cp .env.example .env  # Add your email credentials
pip install -r requirements.txt
python -m src.main
```

## Modules

| Module | Description |
|--------|-------------|
| `src.lead_generator` | RandomForest-based lead scoring |
| `src.email_automation` | SMTP email sending |
| `src.meeting_scheduler` | Google Calendar event creation |
| `src.recommendation_engine` | KMeans customer clustering |
| `src.sales_assistant` | Orchestrates all components |

## Configuration

| Variable | Description |
|----------|-------------|
| `EMAIL_USER` | SMTP email address |
| `EMAIL_PASSWORD` | SMTP app password |
| `GOOGLE_CREDENTIALS_FILE` | Path to Google OAuth token.json |

## Docker

```bash
docker build -t sales-assistant .
docker run --env-file .env sales-assistant
```

## Testing

```bash
pytest -v
```
