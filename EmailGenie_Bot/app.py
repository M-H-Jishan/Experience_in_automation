import logging
import os
import sys
from typing import Optional

from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template
from openai import OpenAI
from sqlalchemy.exc import SQLAlchemyError

from models import UserProfile, session, init_db
from email_templates import generate_email

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


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate_email", methods=["POST"])
def generate_email_route():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Invalid JSON body"}), 400

    email = data.get("email", "").strip()
    if not email:
        return jsonify({"error": "Email is required"}), 400

    try:
        user = session.query(UserProfile).filter_by(email=email).first()
        if not user:
            return jsonify({"error": "User profile not found"}), 404

        email_content = generate_email(user)
        logger.info(f"Email generated for {email}")
        return jsonify({"email": email_content})
    except RuntimeError as e:
        logger.error(f"Config error: {e}")
        return jsonify({"error": str(e)}), 500
    except SQLAlchemyError as e:
        logger.error(f"Database error: {e}")
        return jsonify({"error": "Database error"}), 500
    except Exception as e:
        logger.error(f"Error generating email: {e}", exc_info=True)
        return jsonify({"error": "Failed to generate email"}), 500


@app.route("/create_profile", methods=["POST"])
def create_profile():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Invalid JSON body"}), 400

    name = data.get("name", "").strip()
    email = data.get("email", "").strip()
    profile_data = data.get("profile_data", "").strip()

    if not name or not email:
        return jsonify({"error": "Name and email are required"}), 400

    try:
        existing = session.query(UserProfile).filter_by(email=email).first()
        if existing:
            existing.name = name
            existing.profile_data = profile_data
            session.commit()
            logger.info(f"Updated profile for {email}")
            return jsonify({"message": "Profile updated", "id": existing.id})

        user = UserProfile(name=name, email=email, profile_data=profile_data)
        session.add(user)
        session.commit()
        logger.info(f"Created profile for {email}")
        return jsonify({"message": "Profile created", "id": user.id}), 201
    except SQLAlchemyError as e:
        session.rollback()
        logger.error(f"Database error: {e}")
        return jsonify({"error": "Database error"}), 500
    except Exception as e:
        logger.error(f"Error creating profile: {e}", exc_info=True)
        return jsonify({"error": "Failed to create profile"}), 500


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=os.getenv("DEBUG", "False").lower() == "true")
