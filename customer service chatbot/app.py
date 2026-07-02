import logging
import os
import sys
from typing import Optional

from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template
from openai import OpenAI

from constants import OPENAI_API_KEY, OPENAI_MODEL, KNOWLEDGE_BASE_PATH, PORT, DEBUG

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

client: Optional[OpenAI] = None
if OPENAI_API_KEY:
    client = OpenAI(api_key=OPENAI_API_KEY)


def load_knowledge_base() -> str:
    try:
        with open(KNOWLEDGE_BASE_PATH, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        logger.warning(f"Knowledge base file not found at {KNOWLEDGE_BASE_PATH}")
        return ""
    except Exception as e:
        logger.error(f"Error loading knowledge base: {e}")
        return ""


def generate_response(user_message: str, knowledge_base: str) -> str:
    if not client:
        raise RuntimeError("OPENAI_API_KEY is not set")

    prompt = f"""
    You are a helpful customer service assistant. Use the following knowledge base to answer questions.
    If the answer is not in the knowledge base, say you don't have that information.

    Knowledge Base:
    {knowledge_base}

    User Question: {user_message}
    """

    response = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[
            {"role": "system", "content": "You are a helpful customer service chatbot."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=300,
        temperature=0.5,
    )
    return response.choices[0].message.content.strip()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Invalid JSON body"}), 400

    message = data.get("message", "").strip()
    if not message:
        return jsonify({"error": "Message is required"}), 400

    try:
        knowledge_base = load_knowledge_base()
        response_text = generate_response(message, knowledge_base)
        logger.info("Chat response generated")
        return jsonify({"response": response_text})
    except RuntimeError as e:
        logger.error(f"Config error: {e}")
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        logger.error(f"Error generating response: {e}", exc_info=True)
        return jsonify({"error": "Failed to generate response"}), 500


@app.route("/health")
def health():
    return jsonify({"status": "healthy"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT, debug=DEBUG)
