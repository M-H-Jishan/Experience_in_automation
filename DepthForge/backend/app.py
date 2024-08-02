from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os
import json

app = Flask(__name__)
CORS(app)

# Replace with your actual Sketchfab API token
SKETCHFAB_API_TOKEN = 'YOUR_SKETCHFAB_API_TOKEN'

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file:
        # Upload to Sketchfab
        response = upload_to_sketchfab(file)
        return jsonify(response), 200

def upload_to_sketchfab(file):
    url = "https://api.sketchfab.com/v3/models"
    data = {
        "name": "Generated 3D Model",
        "description": "3D model generated from a 2D image",
        "tags": ["api", "3d-from-image"],
        "isPublished": False,
        "isInspectable": True,
    }
    files = {
        'modelFile': file,
        'name': (None, data['name']),
        'description': (None, data['description']),
        'tags': (None, ','.join(data['tags'])),
        'isPublished': (None, json.dumps(data['isPublished'])),
        'isInspectable': (None, json.dumps(data['isInspectable'])),
    }
    headers = {'Authorization': f'Token {SKETCHFAB_API_TOKEN}'}
    response = requests.post(url, files=files, headers=headers)
    return response.json()

if __name__ == '__main__':
    app.run(debug=True)