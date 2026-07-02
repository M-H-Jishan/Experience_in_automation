import logging
import os
import sys
import json
from typing import Any

import requests
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

SKETCHFAB_API_TOKEN = os.getenv("SKETCHFAB_API_TOKEN", "")


def upload_to_sketchfab(file) -> dict[str, Any]:
    url = "https://api.sketchfab.com/v3/models"
    data = {
        "name": "Generated 3D Model",
        "description": "3D model generated from a 2D image",
        "tags": ["api", "3d-from-image"],
        "isPublished": False,
        "isInspectable": True,
    }
    files = {
        "modelFile": file,
        "name": (None, data["name"]),
        "description": (None, data["description"]),
        "tags": (None, ",".join(data["tags"])),
        "isPublished": (None, json.dumps(data["isPublished"])),
        "isInspectable": (None, json.dumps(data["isInspectable"])),
    }
    headers = {"Authorization": f"Token {SKETCHFAB_API_TOKEN}"}
    response = requests.post(url, files=files, headers=headers, timeout=60)
    response.raise_for_status()
    return response.json()


@app.route("/upload", methods=["POST"])
def upload_image():
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    if not SKETCHFAB_API_TOKEN:
        return jsonify({"error": "SKETCHFAB_API_TOKEN is not set"}), 500

    try:
        result = upload_to_sketchfab(file)
        logger.info("Model uploaded to Sketchfab successfully")
        return jsonify(result), 200
    except requests.exceptions.HTTPError as e:
        logger.error(f"Sketchfab API error: {e}")
        return jsonify({"error": f"Sketchfab API error: {e}"}), 502
    except Exception as e:
        logger.error(f"Upload error: {e}", exc_info=True)
        return jsonify({"error": "Failed to upload model"}), 500


@app.route("/health")
def health():
    return jsonify({"status": "healthy"})


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=os.getenv("DEBUG", "False").lower() == "true")
