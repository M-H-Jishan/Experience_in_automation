# app.py
from flask import Flask, request, jsonify, render_template
from sqlalchemy.exc import SQLAlchemyError
import openai
from models import User, session, init_db

app = Flask(__name__)

# Initialize database
init_db()

# OpenAI API key
openai.api_key = 'your_openai_api_key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_message = request.json.get('message')
    if not user_message:
        return jsonify({'response': 'Please provide a message.'}), 400

    try:
        response = get_ai_response(user_message)
        return jsonify({'response': response})
    except Exception as e:
        return jsonify({'response': 'An error occurred while processing your request.'}), 500

def get_ai_response(message):
    prompt = f"User: {message}\nBot:"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

@app.route('/add_user', methods=['POST'])
def add_user_route():
    data = request.json
    if not all(key in data for key in ('name', 'email', 'service_description')):
        return jsonify({'message': 'Missing data'}), 400

    try:
        add_user(data['name'], data['email'], data['service_description'])
        return jsonify({'message': 'User added successfully'})
    except SQLAlchemyError as e:
        return jsonify({'message': 'Database error'}), 500

def add_user(name, email, service_description):
    new_user = User(name=name, email=email, service_description=service_description)
    session.add(new_user)
    session.commit()

if __name__ == '__main__':
    app.run(debug=True)
