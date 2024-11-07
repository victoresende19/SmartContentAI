from langchain_community.document_loaders import YoutubeLoader

def get_transcription(video_url: str, languages=['en', 'pt']) -> str:
    """
    Fetches the transcription for a given YouTube video URL in the specified languages.
    """
    loader = YoutubeLoader.from_youtube_url(
        "https://www.youtube.com/watch?v=QsYGlZkevEg", add_video_info=False
    )

    return loader.load()