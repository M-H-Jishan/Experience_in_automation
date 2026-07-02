import logging
import os
import sys
from typing import Optional

from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template
from openai import OpenAI
from sqlalchemy.exc import SQLAlchemyError

from models import User, session, init_db

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger(__name__)

app = Flask(__name__)
init_db()

client: Optional[OpenAI] = None
if os.getenv("OPENAI_API_KEY"):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_response(user_message: str, service_description: str) -> str:
    if not client:
        raise RuntimeError("OPENAI_API_KEY is not set")

    prompt = f"""
    You are an intelligent assistant for a service provider.
    Service Description: {service_description}

    User Question: {user_message}

    Provide a helpful, accurate, and professional response based on the service description.
    If the question is not related to the service, politely redirect the user.
    """

    response = client.chat.completions.create(
        model=os.getenv("OPENAI_MODEL", "gpt-3.5-turbo"),
        messages=[
            {"role": "system", "content": "You are a helpful service assistant chatbot."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=300,
        temperature=0.5,
    )
    return response.choices[0].message.content.strip()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chatbot", methods=["POST"])
def chatbot():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Invalid JSON body"}), 400

    message = data.get("message", "").strip()
    if not message:
        return jsonify({"error": "Message is required"}), 400

    user_email = data.get("email", "guest@example.com")

    try:
        user = session.query(User).filter_by(email=user_email).first()
        service_description = user.service_description if user else "General assistance service."

        response_text = generate_response(message, service_description)
        logger.info(f"Chatbot response generated for {user_email}")
        return jsonify({"response": response_text})
    except RuntimeError as e:
        logger.error(f"Config error: {e}")
        return jsonify({"error": str(e)}), 500
    except SQLAlchemyError as e:
        logger.error(f"Database error: {e}")
        return jsonify({"error": "Database error"}), 500
    except Exception as e:
        logger.error(f"Error generating response: {e}", exc_info=True)
        return jsonify({"error": "Failed to generate response"}), 500


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=os.getenv("DEBUG", "False").lower() == "true")
