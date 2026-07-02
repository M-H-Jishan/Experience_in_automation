# DepthForge

Convert 2D images to 3D models and upload to Sketchfab.

## Features

- Upload 2D images and convert to 3D models
- Automatic upload to Sketchfab with metadata
- Web UI with drag-and-drop interface
- REST API endpoint
- Health check

## Quick Start

```bash
cp .env.example .env  # Add your SKETCHFAB_API_TOKEN
cd backend
pip install -r requirements.txt
python app.py
```

Visit http://localhost:5000

## API

### POST /upload

Multipart form data with `file` field (the 3D model file).

### GET /health

Returns `{"status": "healthy"}`

## Docker

```bash
docker build -t depthforge .
docker run -p 5000:5000 --env-file .env depthforge
```

## Testing

```bash
pytest -v
```
