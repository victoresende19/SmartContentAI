from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
from youtube_transcript_api._errors import NoTranscriptFound, TranscriptsDisabled

def get_transcription(video_url: str, languages=['en', 'pt']) -> str:
    try:
        video_id = video_url.split("v=")[-1]
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages, proxies = {
            "http": "http://8c5906b99fbd1c0bcd0f916d545c565a75693f0543fe11fc80ea90b6eef64c7d075ea9772e0f84fed81f7579dcfbd6631eb2a669a57dddbd5a802da724eec0c33dcb925f808ce0bc428f24fde369dbae:c003s974u0p3@proxy.toolip.io:31114"
        })
        formatter = TextFormatter()
        return formatter.format_transcript(transcript)
    except NoTranscriptFound:
        return f"No transcript found for the requested languages: {languages}. Try another video."
    except TranscriptsDisabled:
        return "Transcripts are disabled for this video."
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"
