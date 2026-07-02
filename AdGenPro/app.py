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


def generate_job_ad(career_page: str, job_description: str) -> str:
    if not client:
        raise RuntimeError("OPENAI_API_KEY is not set")

    prompt = f"""
    You are an expert recruiter and copywriter. Create an engaging and professional job advertisement
    based on the following information:

    Company Career Page: {career_page}
    Job Description: {job_description}

    The job ad should include:
    1. An attention-grabbing headline
    2. A brief company introduction
    3. Key responsibilities
    4. Requirements and qualifications
    5. Benefits and perks
    6. A compelling call to action

    Make it engaging, professional, and tailored to attract top talent.
    """

    response = client.chat.completions.create(
        model=os.getenv("OPENAI_MODEL", "gpt-3.5-turbo"),
        messages=[
            {"role": "system", "content": "You are an expert recruiter and copywriter specializing in job advertisements."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=800,
        temperature=0.7,
    )
    return response.choices[0].message.content.strip()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate_ad", methods=["POST"])
def generate_ad():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Invalid JSON body"}), 400

    career_page = data.get("career_page", "")
    job_description = data.get("job_description", "")

    if not career_page or not job_description:
        return jsonify({"error": "Both career_page and job_description are required"}), 400

    try:
        job_ad = generate_job_ad(career_page, job_description)
        logger.info("Job ad generated successfully")
        return jsonify({"job_ad": job_ad})
    except RuntimeError as e:
        logger.error(f"Config error: {e}")
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        logger.error(f"Error generating job ad: {e}", exc_info=True)
        return jsonify({"error": "Failed to generate job ad"}), 500


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=os.getenv("DEBUG", "False").lower() == "true")
