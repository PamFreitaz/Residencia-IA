import os
from dotenv import load_dotenv
from openai import OpenAI

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Instancia o cliente apontando para a API do OpenRouter
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

# Pega o modelo configurado no .env (ou usa o DeepSeek R1 gratuito como padrão)
modelo = os.getenv("OPENAI_MODEL", "deepseek/deepseek-r1:free")

# Faz a chamada para a IA
response = client.chat.completions.create(
    model=modelo,
    messages=[
        {"role": "user", "content": "Qual a capital do Brasil?"}
    ]
)

# Imprime a resposta no terminal
print(response.choices[0].message.content)