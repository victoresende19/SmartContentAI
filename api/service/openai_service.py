from openai import OpenAI
import os
from dotenv import load_dotenv
from utils.prompt_utils import create_dalle_prompt, create_titles_prompt

# Carrega as variáveis de ambiente
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_prompts(transcription: str) -> str:
    prompt = f"Transcription: {transcription}\nElaborate a DALL-E prompt in English."
    
    # Atualize para o método correto de ChatCompletion
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature = 0.1,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message.content

def generate_titles_descriptions(transcription: str):
    prompt = create_titles_prompt(transcription)
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature = 0.3,
        messages=[
            {"role": "system", "content": "You are a creative assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    content = response.choices[0].message.content.split('\n')
    print(prompt)
    filtered_data = [item.strip() for item in content if item.strip() != ""]
    titles_index = filtered_data.index('**Títulos:**')
    descriptions_index = filtered_data.index('**Descrições:**')

    # Extrair títulos e descrições, removendo índices de cabeçalhos
    titles = filtered_data[titles_index + 1:descriptions_index]
    descriptions = filtered_data[descriptions_index + 1:]

    return titles, descriptions
