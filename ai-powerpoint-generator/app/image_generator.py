import os
import requests
from utils.openai_helper import get_client


def generate_image(prompt: str) -> bytes:
    client = get_client()
    response = client.images.generate(
        model=os.getenv("OPENAI_IMAGE_MODEL", "dall-e-3"),
        prompt=prompt,
        n=1,
        size="1024x1024",
    )
    image_url = response.data[0].url
    return requests.get(image_url, timeout=60).content
