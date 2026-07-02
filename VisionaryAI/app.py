import logging
import os
import sys
from typing import Optional

from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template
from openai import OpenAI

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

client: Optional[OpenAI] = None
if os.getenv("OPENAI_API_KEY"):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_image(prompt: str) -> str:
    if not client:
        raise RuntimeError("OPENAI_API_KEY is not set")

    response = client.images.generate(
        model=os.getenv("OPENAI_IMAGE_MODEL", "dall-e-3"),
        prompt=prompt,
        n=1,
        size="1024x1024",
    )
    return response.data[0].url


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate_image", methods=["POST"])
def generate_image_route():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Invalid JSON body"}), 400

    description = data.get("description", "").strip()
    if not description:
        return jsonify({"error": "Description is required"}), 400

    prompt = f"Create a high-quality, detailed, and visually appealing image based on the following description: {description}"

    try:
        image_url = generate_image(prompt)
        logger.info("Image generated successfully")
        return jsonify({"image_url": image_url})
    except RuntimeError as e:
        logger.error(f"Config error: {e}")
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        logger.error(f"Error generating image: {e}", exc_info=True)
        return jsonify({"error": "Failed to generate image"}), 500


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=os.getenv("DEBUG", "False").lower() == "true")
