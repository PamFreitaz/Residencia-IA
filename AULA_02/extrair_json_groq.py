import os
import json
from dotenv import load_dotenv, find_dotenv
from groq import Groq

# O find_dotenv() varre as pastas para cima até achar o .env na raiz do projeto
load_dotenv(find_dotenv())

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("A chave de API não foi encontrada no arquivo .env!")

# Inicializa o cliente usando a variável GROQ_API_KEY carregada do .env
client = Groq(api_key=api_key)

PASTA_MD = "Arquivos md"

arquivos_md = [
    "bioetica_e_ia.md",
    "escrita_academica_ia.md",
    "twitter_algoritmo.md"
]

resultado_final = []

SYSTEM_PROMPT = """
Você é um assistente especialista em análise de documentos acadêmicos.
Analise o texto fornecido e extraia exatamente as seguintes informações em formato JSON:
- titulo (string): O título principal do artigo.
- autores (lista de strings): Nomes dos autores. Sempre retorne uma lista, mesmo que haja apenas um autor. Ex: ["Nome Autor"]
- ano (string): O ano de publicação no formato "YYYY" ou "Não especificado" caso não encontre no texto.

Responda EXCLUSIVAMENTE com o objeto JSON válido, sem explicações adicionais.
"""

for nome_arquivo in arquivos_md:
    caminho_completo = os.path.join(PASTA_MD, nome_arquivo)

    if not os.path.exists(caminho_completo):
        caminho_completo = nome_arquivo

    if not os.path.exists(caminho_completo):
        print(f"Arquivo {nome_arquivo} não encontrado. Pulando...")
        continue

    print(f"Processando {caminho_completo} com a Groq...")
    
    with open(caminho_completo, "r", encoding="utf-8") as f:
        conteudo_md = f.read()

    trecho_texto = conteudo_md[:4000]

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": f"Arquivo: {nome_arquivo}\n\nTexto:\n{trecho_texto}"}
            ],
            response_format={"type": "json_object"},
            temperature=0.1
        )

        dados_extraidos = json.loads(response.choices[0].message.content)
        dados_extraidos["arquivo"] = nome_arquivo
        resultado_final.append(dados_extraidos)

    except Exception as e:
        print(f"Erro ao processar {nome_arquivo}: {e}")

with open("artigos_estruturados.json", "w", encoding="utf-8") as f:
    json.dump(resultado_final, f, ensure_ascii=False, indent=4)

print("\nSucesso! Arquivo 'artigos_estruturados.json' gerado via Groq.")