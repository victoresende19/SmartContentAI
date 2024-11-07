def create_dalle_prompt(transcription: str) -> str:
    return f"""{transcription}

    Baseado na transcrição anterior, elabore um prompt para geração de imagem utilizando a ferramenta DallE, sua resposta deve conter apenas o prompt e nada mais, nem uma palavra introdução. O prompt deve ser em inglês.
    """

def create_dalle3_prompt(dalle_content: str) -> str:
    return f"Create an image with a minimalistic style and realistic, without any text with the following context: {dalle_content}"

def create_titles_prompt(transcription: str) -> str:
    return f"""Transcription: {transcription}
    Baseado na transcrição acima, crie inicialmente três títulos, após isso, crie 3 descrições envolventes e informativas para vídeos do YouTube. Cada título deve ser cativante e otimizado para mecanismos de busca, enquanto as descrições devem ser detalhadas, incluindo palavras-chave relevantes, um breve resumo do conteúdo do vídeo e um chamado para ação.

    O resultado deve seguir o formato do exemplo abaixo:
    **Títulos:**
    1. "Título 1"
    2. "Título 2"
    3. "Título 3"

    **Descrições:**
    1. Descrição 1.
    2. Descrição 2.
    3. Descrição 3.

    Se a transcrição for: Transcripts are disabled for this video. Retorne o prompt como: 
    **Títulos:**
    1. "A transcrição desse vídeo está desabilitada ou seu IP foi barrado pelo YouTube."
    2. "A transcrição desse vídeo está desabilitada ou seu IP foi barrado pelo YouTube."
    3. "A transcrição desse vídeo está desabilitada ou seu IP foi barrado pelo YouTube."

    **Descrições:**
    1. A transcrição desse vídeo está desabilitada ou seu IP foi barrado pelo YouTube..
    2. A transcrição desse vídeo está desabilitada ou seu IP foi barrado pelo YouTube..
    3. A transcrição desse vídeo está desabilitada ou seu IP foi barrado pelo YouTube..
    """
