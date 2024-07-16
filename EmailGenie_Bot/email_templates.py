# email_templates.py
import openai

def generate_email(user_profile):
    prompt = (
        f"Create a personalized cold email for the following user profile:\n"
        f"Name: {user_profile.name}\n"
        f"Email: {user_profile.email}\n"
        f"Profile Data: {user_profile.profile_data}\n"
    )
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=250
    )
    return response.choices[0].text.strip()
