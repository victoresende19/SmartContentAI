from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from service.transcript_service import get_transcription
from service.openai_service import generate_prompts, generate_titles_descriptions
from service.dalle_service import generate_dalle_image

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir apenas a origem do React
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos os métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permitir todos os cabeçalhos
)

@app.post("/generate-video-details/")
async def generate_video_details(request: Request):
    data = await request.json()
    video_url = data.get("video_url")

    if not video_url:
        raise HTTPException(status_code=400, detail="Video URL is required")

    # Step 1: Get transcription
    transcription = get_transcription(video_url)

    # Step 2: Generate DALL-E prompt
    dalle_prompt = generate_prompts(transcription)

    # Step 3: Generate DALL-E image URL
    dalle_image_url = generate_dalle_image(dalle_prompt)

    # Step 4: Generate titles and descriptions
    titles, descriptions = generate_titles_descriptions(transcription)

    return {
        "transcription": transcription,
        "dalle_image_url": dalle_image_url,
        "titles": titles,
        "descriptions": descriptions,
    }
