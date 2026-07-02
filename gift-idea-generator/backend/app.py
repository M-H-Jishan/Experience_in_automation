import json
import logging
import os
import sys
from typing import Optional

from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI

from inventory import search_products

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

client: Optional[OpenAI] = None
if os.getenv("OPENAI_API_KEY"):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


@app.route("/generate_gifts", methods=["POST"])
def generate_gifts():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Invalid JSON body"}), 400

    required = ["age", "gender", "relation", "interests", "budget", "occasion"]
    for field in required:
        if field not in data:
            return jsonify({"error": f"{field} is required"}), 400

    if not client:
        return jsonify({"error": "OPENAI_API_KEY is not set"}), 500

    prompt = f"""
    As an expert gift advisor, suggest 3 unique and thoughtful gift ideas based on the following information:

    Recipient's Age: {data['age']}
    Recipient's Gender: {data['gender']}
    Your Relation to Recipient: {data['relation']}
    Recipient's Interests: {data['interests']}
    Budget: ${data['budget']}
    Occasion: {data['occasion']}

    For each gift idea, provide:
    1. A creative name for the gift
    2. A brief description (2-3 sentences)
    3. Why it's particularly suitable for this recipient (2-3 sentences)
    4. A general category for the gift (e.g., Electronics, Fashion, Experience, Home Decor)

    Format the response as a JSON object with keys 'gift1', 'gift2', and 'gift3'.
    Each gift should have 'name', 'description', 'reason', and 'category' fields.
    """

    try:
        response = client.chat.completions.create(
            model=os.getenv("OPENAI_MODEL", "gpt-3.5-turbo"),
            messages=[
                {"role": "system", "content": "You are a helpful and creative gift advisor, specializing in personalized gift recommendations. Always respond with valid JSON."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=800,
            temperature=0.7,
        )

        gift_ideas_raw = response.choices[0].message.content.strip()
        gift_ideas = json.loads(gift_ideas_raw)

        for gift in gift_ideas.values():
            gift["related_products"] = search_products(
                gift["category"], gift["name"], float(data["budget"])
            )

        logger.info("Gift ideas generated successfully")
        return jsonify(gift_ideas)
    except json.JSONDecodeError:
        logger.error("Failed to parse OpenAI response as JSON")
        return jsonify({"error": "Failed to parse gift ideas"}), 500
    except Exception as e:
        logger.error(f"Error generating gifts: {e}", exc_info=True)
        return jsonify({"error": "Failed to generate gift ideas"}), 500


@app.route("/health")
def health():
    return jsonify({"status": "healthy"})


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=os.getenv("DEBUG", "False").lower() == "true")
