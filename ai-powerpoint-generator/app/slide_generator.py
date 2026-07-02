import os
from utils.openai_helper import get_client


def generate_slide_titles(topic: str, num_slides: int) -> list[str]:
    client = get_client()
    prompt = f"Generate {num_slides} engaging slide titles for a presentation on '{topic}'. Provide them as a numbered list."
    response = client.chat.completions.create(
        model=os.getenv("OPENAI_MODEL", "gpt-4"),
        messages=[
            {"role": "system", "content": "You are a helpful assistant that generates slide titles."},
            {"role": "user", "content": prompt},
        ],
    )
    titles = response.choices[0].message.content.split("\n")
    return [title.strip().split(". ", 1)[1] for title in titles if title.strip()]


def generate_slide_content(topic: str, title: str) -> list[str]:
    client = get_client()
    prompt = f"Generate concise bullet points for a slide titled '{title}' in a presentation about '{topic}'. Provide 3-5 bullet points."
    response = client.chat.completions.create(
        model=os.getenv("OPENAI_MODEL", "gpt-4"),
        messages=[
            {"role": "system", "content": "You are a helpful assistant that generates slide content."},
            {"role": "user", "content": prompt},
        ],
    )
    return response.choices[0].message.content.split("\n")
