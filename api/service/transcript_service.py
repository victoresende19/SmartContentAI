from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
from youtube_transcript_api._errors import NoTranscriptFound, TranscriptsDisabled
from pytube import YouTube

# def get_transcription(video_url: str, languages=['en', 'pt']) -> str:
#     proxies = {
#         "http": "http://150.230.72.171:80",
#         "https": "http://150.230.72.171:80",
#     }
#     try:
#         video_id = video_url.split("v=")[-1]
#         transcript = YouTubeTranscriptApi.get_transcript(video_id, languages, proxies=proxies)
#         formatter = TextFormatter()
#         return formatter.format_transcript(transcript)
#     except NoTranscriptFound:
#         return f"No transcript found for the requested languages: {languages}. Try another video."
#     except TranscriptsDisabled:
#         return "Transcripts are disabled for this video."
#     except Exception as e:
#         return f"An unexpected error occurred: {str(e)}"

def get_transcription(video_url: str, languages=['en', 'pt']) -> str:
    try:
        yt = YouTube(video_url)
        for language in languages:
            caption = yt.captions.get_by_language_code(language)
            if caption:
                return caption.generate_srt_captions()
        return f"Nenhuma legenda encontrada para as linguagens solicitadas: {languages}. Tente outro vídeo."
    except Exception as e:
        return f"Ocorreu um erro: {str(e)}"

