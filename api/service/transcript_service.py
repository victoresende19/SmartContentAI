from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
from youtube_transcript_api._errors import NoTranscriptFound, TranscriptsDisabled
from urllib.parse import urlparse, parse_qs

def extract_video_id(video_url: str) -> str:
    """
    Extracts the YouTube video ID from a URL.
    Supports various YouTube URL formats.
    """
    try:
        parsed_url = urlparse(video_url)
        hostname = parsed_url.hostname or ""
        if hostname in ["www.youtube.com", "youtube.com"]:
            query_params = parse_qs(parsed_url.query)
            return query_params.get("v", [None])[0]
        elif hostname in ["youtu.be"]:
            return parsed_url.path.lstrip("/")
        else:
            raise ValueError("Invalid YouTube URL format")
    except Exception as e:
        raise ValueError(f"Error extracting video ID: {str(e)}")

def get_available_languages(video_id: str) -> list:
    """
    Lists available transcript languages for a given YouTube video.
    """
    try:
        transcripts = YouTubeTranscriptApi.list_transcripts(video_id)
        return [trans.language for trans in transcripts]
    except Exception as e:
        raise RuntimeError(f"Could not list available languages: {str(e)}")

def get_transcription(video_url: str, languages=['en', 'pt']) -> str:
    """
    Fetches the transcription for a given YouTube video URL in the specified languages.
    """
    try:
        video_id = extract_video_id(video_url)
        if not video_id:
            return "Invalid or missing video ID."
        
        available_languages = get_available_languages(video_id)
        
        for lang in languages:
            if lang in available_languages:
                transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[lang])
                formatter = TextFormatter()
                return formatter.format_transcript(transcript)
        
        return f"No transcript found for the requested languages: {languages}. Available: {available_languages}."
    except NoTranscriptFound:
        return f"No transcript found for the requested languages: {languages}."
    except TranscriptsDisabled:
        return "Transcripts are disabled for this video."
    except ValueError as ve:
        return f"Error: {str(ve)}"
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"

# Exemplo de uso
if __name__ == "__main__":
    youtube_link = input("Enter YouTube URL: ")
    result = get_transcription(youtube_link, languages=['en', 'pt'])
    print(result)
