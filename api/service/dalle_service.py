from openai import OpenAI
from dotenv import load_dotenv
import os
from utils.prompt_utils import create_dalle3_prompt

# Load environment variables
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_dalle_image(dalle_prompt: str) -> str:
    dalle_request = create_dalle3_prompt(dalle_prompt)
    response = client.images.generate(
        model="dall-e-3",
        prompt=dalle_request,
        size="1024x1024",
        quality="standard",
        n=1,
        )

    return response.data[0].url
