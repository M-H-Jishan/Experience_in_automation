from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os
from inventory import search_products

app = Flask(__name__)
CORS(app)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/generate_gifts', methods=['POST'])
def generate_gifts():
    user_input = request.json
    
    prompt = f"""
    As an expert gift advisor, suggest 3 unique and thoughtful gift ideas based on the following information:
    
    Recipient's Age: {user_input['age']}
    Recipient's Gender: {user_input['gender']}
    Your Relation to Recipient: {user_input['relation']}
    Recipient's Interests: {user_input['interests']}
    Budget: ${user_input['budget']}
    Occasion: {user_input['occasion']}

    For each gift idea, provide:
    1. A creative name for the gift
    2. A brief description (2-3 sentences)
    3. Why it's particularly suitable for this recipient (2-3 sentences)
    4. A general category for the gift (e.g., Electronics, Fashion, Experience, Home Decor)

    Ensure that each gift idea is:
    - Age-appropriate
    - Aligned with the recipient's interests
    - Within the specified budget
    - Suitable for the occasion
    - Considerate of the relationship between the giver and recipient

    Format the response as a JSON object with keys 'gift1', 'gift2', and 'gift3'.
    Each gift should have 'name', 'description', 'reason', and 'category' fields.
    """

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful and creative gift advisor, specializing in personalized gift recommendations."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=800,
            n=1,
            temperature=0.7,
        )

        gift_ideas = response.choices[0].message['content']
        
        import json
        gift_ideas_dict = json.loads(gift_ideas)

        for gift in gift_ideas_dict.values():
            gift['related_products'] = search_products(gift['category'], gift['name'], float(user_input['budget']))

        return jsonify(gift_ideas_dict)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)