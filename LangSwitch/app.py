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


def translate_text(text: str, source_lang: str, target_lang: str) -> str:
    if not client:
        raise RuntimeError("OPENAI_API_KEY is not set")

    prompt = f"Translate the following text from {source_lang} to {target_lang}:\n\n{text}"
    response = client.chat.completions.create(
        model=os.getenv("OPENAI_MODEL", "gpt-3.5-turbo"),
        messages=[
            {"role": "system", "content": "You are a professional translator. Translate accurately and naturally."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=500,
        temperature=0.3,
    )
    return response.choices[0].message.content.strip()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/translate", methods=["POST"])
def translate():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Invalid JSON body"}), 400

    text = data.get("text", "").strip()
    source_lang = data.get("source_lang", "auto")
    target_lang = data.get("target_lang", "en")

    if not text:
        return jsonify({"error": "Text is required"}), 400
    if not target_lang:
        return jsonify({"error": "Target language is required"}), 400

    try:
        translation = translate_text(text, source_lang, target_lang)
        logger.info(f"Translated from {source_lang} to {target_lang}")
        return jsonify({"translation": translation})
    except RuntimeError as e:
        logger.error(f"Config error: {e}")
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        logger.error(f"Error translating: {e}", exc_info=True)
        return jsonify({"error": "Failed to translate text"}), 500


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=os.getenv("DEBUG", "False").lower() == "true")
