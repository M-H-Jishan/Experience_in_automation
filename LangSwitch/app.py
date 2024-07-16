from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Replace with your OpenAI API key
openai.api_key = 'your_openai_api_key_here'

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    data = request.json
    message = data['message']
    source_lang = data['source_lang']
    target_lang = data['target_lang']

# Pre-prompt for high-quality translations
    prompt = f"""You are LangSwitch, an advanced AI translator. Your task is to translate the following text from {source_lang} to {target_lang}. Please ensure that the translation is accurate, natural-sounding, and preserves the original meaning and tone. If there are any cultural nuances or idiomatic expressions, please adapt them appropriately for the target language.

Original text: {message}

Translation:"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are LangSwitch, an advanced AI translator."},
            {"role": "user", "content": prompt}
        ]
    )

    translation = response.choices[0].message['content'].strip()

    return jsonify({"translation": translation})

if __name__ == '__main__':
    app.run(debug=True)