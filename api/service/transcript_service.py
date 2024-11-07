from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
from youtube_transcript_api._errors import NoTranscriptFound, TranscriptsDisabled

def get_transcription(video_url: str, languages=['en', 'pt']) -> str:
    try:
        video_id = video_url.split("v=")[-1]
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages, proxies={"https": "198.23.239.134:6540:kbclugph:whzp3kraonuv"})
        formatter = TextFormatter()
        return formatter.format_transcript(transcript)
    except NoTranscriptFound:
        return f"No transcript found for the requested languages: {languages}. Try another video."
    except TranscriptsDisabled:
        return "Transcripts are disabled for this video."
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"
