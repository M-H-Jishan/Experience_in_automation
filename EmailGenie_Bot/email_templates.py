import os
from typing import Optional
from openai import OpenAI

_client: Optional[OpenAI] = None
if os.getenv("OPENAI_API_KEY"):
    _client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_email(user_profile) -> str:
    if not _client:
        raise RuntimeError("OPENAI_API_KEY is not set")

    prompt = (
        f"Create a personalized cold email for the following user profile:\n"
        f"Name: {user_profile.name}\n"
        f"Email: {user_profile.email}\n"
        f"Profile Data: {user_profile.profile_data}\n"
    )

    response = _client.chat.completions.create(
        model=os.getenv("OPENAI_MODEL", "gpt-3.5-turbo"),
        messages=[
            {"role": "system", "content": "You are an expert email copywriter specializing in personalized cold emails."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=300,
        temperature=0.7,
    )
    return response.choices[0].message.content.strip()
