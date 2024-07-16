# app.py
from flask import Flask, request, render_template, jsonify
import openai

app = Flask(__name__)

# OpenAI API key
openai.api_key = 'your_openai_api_key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_ad', methods=['POST'])
def generate_ad():
    data = request.json
    career_page = data.get('career_page')
    job_description = data.get('job_description')

    prompt = (
        f"Create a detailed and engaging job ad based on the following information:\n\n"
        f"Company Career Page: {career_page}\n"
        f"Job Description: {job_description}\n"
    )

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500
    )
    
    job_ad = response.choices[0].text.strip()
    return jsonify({'job_ad': job_ad})

if __name__ == '__main__':
    app.run(debug=True)
