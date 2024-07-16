# app.py
from flask import Flask, request, jsonify, render_template
from sqlalchemy.exc import SQLAlchemyError
import openai
from models import UserProfile, session, init_db
from email_templates import generate_email

app = Flask(__name__)

# Initialize database
init_db()

# OpenAI API key
openai.api_key = 'your_openai_api_key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_email', methods=['POST'])
def generate_email_route():
    data = request.json
    if not all(key in data for key in ('name', 'email', 'profile_data')):
        return jsonify({'message': 'Missing data'}), 400

    try:
        user_profile = UserProfile(name=data['name'], email=data['email'], profile_data=data['profile_data'])
        session.add(user_profile)
        session.commit()

        email_content = generate_email(user_profile)
        return jsonify({'email_content': email_content})
    except SQLAlchemyError as e:
        return jsonify({'message': 'Database error'}), 500
    except Exception as e:
        return jsonify({'message': 'Error generating email'}), 500

if __name__ == '__main__':
    app.run(debug=True)
