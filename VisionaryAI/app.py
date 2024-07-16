# app.py
from flask import Flask, request, render_template, jsonify
import openai

app = Flask(__name__)

# OpenAI API key
openai.api_key = 'your_openai_api_key'

def generate_image(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    return response['data'][0]['url']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_image', methods=['POST'])
def generate_image_route():
    data = request.json
    description = data.get('description')
    
    pre_prompt = "Create a high-quality, detailed, and visually appealing image based on the following description: "
    prompt = pre_prompt + description

    image_url = generate_image(prompt)
    
    return jsonify({'image_url': image_url})

if __name__ == '__main__':
    app.run(debug=True)
