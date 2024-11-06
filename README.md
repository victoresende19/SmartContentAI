# SmartContentAI
<hr>

A agente de IA SmartContentAI tem como objetivo fornecer uma aplicação que utiliza técnicas de inteligência artificial para transcrever vídeos do YouTube e, a partir da transcrição, gerar títulos e descrições otimizados, além de criar imagens de thumbnail atrativas para os vídeos. Dessa forma, a API foca em simplificar e automatizar o processo de otimização de vídeos para a plataforma YouTube, auxiliando criadores de conteúdo a economizar tempo e melhorar a qualidade de seus uploads.

## Tecnologias
O agente foi criado a partir das seguintes tecnologias:
- Langflow:
- Python 3.11 (com as respectivas bibliotecas): 
  - Langflow: criação dos fluxos para agentes de IA;
  - OpenAI (além do OpenAI Key): utilização dos modelos LLM OpenAI para a criação das descrições e títulos. Além disso, utilização do modelo DallE 3 para criação da thumbnail;
  - TikToken: identificação da quantidade de tokens, visando a limitação de determinados modelos;
  - Youtube-transcript-api: extração da transcrição dos vídeos oriundos aos links do YouTube.

## Arquitetura
O agente SmartContentAI foi criado seguindo a arquitetura abaixo:
![image](https://github.com/user-attachments/assets/9234600d-9811-4c20-b243-ad62f85e3f35)


## Acesse o fluxo
O fluxo está disponível para download através do arquivo SmartContentAI.json, o qual pode ser importado via interface Langflow para testes.

## Recomendações
O projeto foi criado localmente, dessa forma, para testar o fluxo faça as devidas instalações das bibliotecas.
