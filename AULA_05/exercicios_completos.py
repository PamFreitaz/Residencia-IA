import json
from langchain_core.documents import Document

documentos = [
    Document(
        page_content="Os learned embeddings são usados para converter os tokens de entrada em vetores contínuos de dimensão fixa.",
        metadata={
            "fonte": "attention_is_all_you_need_2.md",
            "pagina": 5,
            "tipo": "conceito",
            "tema": "embeddings",
            "autor": [
                "Ashish Vaswani", "Noam Shazeer", "Llion Jones", 
                "Niki Parmar", "Aidan N. Gomez", "Jakob Uszkoreit", 
                "Łukasz Kaiser", "Illia Polosukhin"
            ]
        }
    ),
    Document(
        page_content="A técnica de tokenização byte-pair encoding (BPE) divide palavras em subunidades para alimentar a rede neural.",
        metadata={
            "fonte": "attention_is_all_you_need_2.md",
            "pagina": 6,
            "tipo": "teoria",
            "tema": "tokenização",
            "autor": [
                "Ashish Vaswani", "Noam Shazeer", "Llion Jones", 
                "Niki Parmar", "Aidan N. Gomez", "Jakob Uszkoreit", 
                "Łukasz Kaiser", "Illia Polosukhin"
            ]
        }
    ),
    Document(
        page_content="O processo de chunking fatia documentos extensos, como artigos da Wikipedia, em pedaços menores de 100 palavras.",
        metadata={
            "fonte": "retrieval_augmented_generation.md",
            "pagina": 4,
            "tipo": "prática",
            "tema": "chunking",
            "autor": [
                "Patrick Lewis", "Ethan Perez", "Aleksandra Piktus", 
                "Fabio Petroni", "Vladimir Karpukhin", "Naman Goyal", 
                "Heinrich Küttler", "Mike Lewis", "Wen-tau Yih", 
                "Tim Rocktäschel", "Sebastian Riedel", "Douwe Kiela"
            ]
        }
    ),
    Document(
        page_content="Modelos RAG combinam a memória paramétrica de um LLM com a memória não-paramétrica de um banco de dados externo.",
        metadata={
            "fonte": "retrieval_augmented_generation.md",
            "pagina": 2,
            "tipo": "arquitetura",
            "tema": "RAG",
            "autor": [
                "Patrick Lewis", "Ethan Perez", "Aleksandra Piktus", 
                "Fabio Petroni", "Vladimir Karpukhin", "Naman Goyal", 
                "Heinrich Küttler", "Mike Lewis", "Wen-tau Yih", 
                "Tim Rocktäschel", "Sebastian Riedel", "Douwe Kiela"
            ]
        }
    ),
    Document(
        page_content="Em sistemas RAG, um modelo codificador computa embeddings densos para cada chunk, permitindo busca semântica eficiente.",
        metadata={
            "fonte": "retrieval_augmented_generation.md",
            "pagina": 3,
            "tipo": "prática",
            "tema": "embeddings",
            "autor": [
                "Patrick Lewis", "Ethan Perez", "Aleksandra Piktus", 
                "Fabio Petroni", "Vladimir Karpukhin", "Naman Goyal", 
                "Heinrich Küttler", "Mike Lewis", "Wen-tau Yih", 
                "Tim Rocktäschel", "Sebastian Riedel", "Douwe Kiela"
            ]
        }
    ),
]

print("--- DETALHES DE CADA DOCUMENTO ---")
for numero, doc in enumerate(documentos, 1):
    print(f"Documento {numero}:")
    print(f"  Conteúdo: {doc.page_content}")
    print("  Metadados:")
    
    # Imprime os metadados de forma organizada sem repetir a linha inteira feia
    for chave, valor in doc.metadata.items():
        print(f"    -> {chave}: {valor}")
        
    print("-" * 60)
    
print(f"\nTotal de documentos gerados: {len(documentos)}")

print("\n--- LISTA COMPLETA ORGANIZADA ---")
lista_organizada = []

for doc in documentos:
    lista_organizada.append({
        "page_content": doc.page_content,
        "metadata": doc.metadata
    })

# O JSON agora vai quebrar os autores linha por linha bonitinho
texto_bonito = json.dumps(lista_organizada, indent=4, ensure_ascii=False)
print(texto_bonito)

"""
EXERCÍCIO 2: SCHEMA DE METADADOS

Tabela do Schema está no arquivo schema_metadados.md

"""

exemplo_schema = {
    "fonte": "retrieval_augmented_generation.md",
    "documento_id": "doc_rag_001",
    "chunk_index": 5,
    "estrategia": "recursive_character",
    "chunk_size": 500,
    "chunk_overlap": 50,
    "n_caracteres": 485,
    "data_criacao": "2026-08-13",
    "nivel_dificuldade": "intermediário",
    "topico_secundario": "busca_semantica"
}

print("\n--- EXEMPLO DO SCHEMA DO EXERCÍCIO 2 ---")
print(json.dumps(exemplo_schema, indent=4, ensure_ascii=False))