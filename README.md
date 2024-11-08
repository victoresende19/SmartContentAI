# SmartContentAI
<hr>

A agente de IA SmartContentAI tem como objetivo fornecer uma aplicação que utiliza técnicas de inteligência artificial para transcrever vídeos do YouTube e, a partir da transcrição, gerar títulos e descrições otimizados, além de criar imagens de thumbnail atrativas para os vídeos. Dessa forma, a API foca em simplificar e automatizar o processo de otimização de vídeos para a plataforma YouTube, auxiliando criadores de conteúdo a economizar tempo e melhorar a qualidade de seus uploads.

## Acesse 
Para facilitar o teste do SmartContentAI, foi desenvolvido um website que realiza consultas à API criada. A API foi criada através das bibliotecas FastAPI, LangChain e OpenAI, em linguagem Python, e é necessário obter uma API_KEY da OpenAI, a qual você pode criar gratuitamente, basta [clicar aqui](https://openai.com/index/openai-api/). Além disso, visando a acessibilidade, criou-se a plataforma SmartContentAI por meio do framework React, em linguagem JavaScript. 

O deploy da API foi realizado utilizando o [Render](https://dashboard.render.com/), sob o plano gratuito. Devido às limitações deste plano, como o uso de máquinas menos robustas, o tempo de resposta pode ser maior em comparação ao uso local da API. Por fim, o frontend da plataforma teve o deploy através do [Vercel](https://vercel.com/). Para acessar e testar o aplicativo, visite: [https://smart-content-br.vercel.app/](https://smart-content-br.vercel.app/).

<hr>

## Tecnologias
O agente foi criado a partir das seguintes tecnologias:
- Langflow: Interface para criação de fluxos de IA low code. O Langflow foi utilizado principalmente para estudo e prototipagem, o qual posteriormente fez-se a implementação via Python com LangChain.
- Python 3.11 (com as respectivas bibliotecas): 
  - Langflow: criação dos fluxos para agentes de IA no Code para prototipagem;
  - LangChain: biblioteca para utilização modular de códigos voltados a agentes de IA;
  - OpenAI (além do OpenAI Key): utilização dos modelos LLM OpenAI para a criação das descrições e títulos. Além disso, utilização do modelo DallE 3 para criação da thumbnail;
  - TikToken: identificação da quantidade de tokens, visando a limitação de determinados modelos;
  - Youtube-transcript-api: extração da transcrição dos vídeos oriundos aos links do YouTube.
  - Poetry: pacote para o controle de versões das bibiliotecas

<hr>

# Teste a Aplicação

## API
A API foi escrita em FastAPI através da lingugem Python e as devidas bibliotecas contidas no arquivo requirements.txt.

### Configurações - localmente
Instalação da biblioteca Poetry:
```
pip install poetry
```

Inicialização do Poetry:
```
poetry init
```

Instalação das bibliotecas necessárias:
```
poetry install
```

Ativação da API:
```
poetry run uvicorn main:app --reload
```

Para executar a API localmente, os seguintes métodos estarão disponíveis. Utilize ferramentas como o Postman ou Insomnia para realizar as requisições:
- Gerar conteúdo:
  - ``` (POST): http://127.0.0.1:8000/generate-video-details/```
  - Corpo da Requisição JSON: ```{ "video_url": "https://www.youtube.com/watch?v=BjC0KUxiMhc" }```

## Frontend
O frontend foi escrito em React através da linguagem Typescript.

### Configurações - localmente
Instalação das bibliotecas:
```
npm install
```

Ativação da interface:
```
npm start
```

<hr>

## Arquitetura
O agente SmartContentAI foi criado seguindo a arquitetura abaixo:
![image](https://github.com/user-attachments/assets/2cf43b43-30af-4b1e-8a0d-d436372b065b)

<hr>

# Langflow
O fluxo está disponível para download através do arquivo SmartContentAI.json, o qual pode ser importado via interface Langflow para testes. Recomendações: o projeto foi criado localmente, dessa forma, para testar o fluxo faça as devidas instalações das bibliotecas.
