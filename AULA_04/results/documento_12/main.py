import os
import json
import re
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer

# Importação dos Splitters do LangChain
from langchain_text_splitters import (
    CharacterTextSplitter,
    RecursiveCharacterTextSplitter,
    MarkdownHeaderTextSplitter
)

# Carrega o tokenizador exato do seu modelo de embeddings
tokenizador = AutoTokenizer.from_pretrained('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')


# LOCALIZAÇÃO DOS ARQUIVOS (USANDO A PASTA ATUAL COMO BASE)
pasta_atual = os.path.dirname(os.path.abspath(__file__))
caminho_md = os.path.join(pasta_atual, "markdown", "scaling_laws_llm.md")

doc_id = "documento_12"
doc_name = "scaling_laws_llm.pdf"

print("Carregando modelo de embeddings...")
modelo_embedding = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')

# Ler o arquivo Markdown existente
with open(caminho_md, "r", encoding="utf-8") as f:
    texto = f.read()

print(f"Arquivo lido com sucesso! Total: {len(texto)} caracteres.\n")

# DEFINIÇÃO DOS 10 EXPERIMENTOS DE CHUNKING
experimentos = {}

# Teste 1: Fixo 200 caracteres, sem overlap
sp1 = CharacterTextSplitter(chunk_size=200, chunk_overlap=0, separator="")
experimentos[1] = ("fixed", 200, 0, sp1.split_text(texto), [])

# Teste 2: Fixo 500 caracteres, sem overlap
sp2 = CharacterTextSplitter(chunk_size=500, chunk_overlap=0, separator="")
experimentos[2] = ("fixed", 500, 0, sp2.split_text(texto), [])

# Teste 3: Fixo 1000 caracteres, sem overlap
sp3 = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0, separator="")
experimentos[3] = ("fixed", 1000, 0, sp3.split_text(texto), [])

# Teste 4: Fixo 2000 caracteres, sem overlap
sp4 = CharacterTextSplitter(chunk_size=2000, chunk_overlap=0, separator="")
experimentos[4] = ("fixed", 2000, 0, sp4.split_text(texto), [])

# Teste 5: Fixo 500 caracteres com overlap de 50 (10%)
sp5 = CharacterTextSplitter(chunk_size=500, chunk_overlap=50, separator="")
experimentos[5] = ("fixed_with_overlap", 500, 50, sp5.split_text(texto), [])

# Teste 6: Fixo 500 caracteres com overlap de 200 (40%)
sp6 = CharacterTextSplitter(chunk_size=500, chunk_overlap=200, separator="")
experimentos[6] = ("fixed_with_overlap", 500, 200, sp6.split_text(texto), [])

# Teste 7: Por Parágrafo usando LangChain
sp7 = CharacterTextSplitter(separator="\n\n", chunk_size=1, chunk_overlap=0)
chunks_p = sp7.split_text(texto)
metadados_p = [{"paragraph_index": i + 1} for i in range(len(chunks_p))]
experimentos[7] = ("paragraph", 0, 0, chunks_p, metadados_p)

# Teste 8: Sentenças agrupadas em 3
sentencas = re.split(r'(?<=[.!?])\s+', texto.replace("\n", " "))
chunks_s = [" ".join(sentencas[i:i+3]).strip() for i in range(0, len(sentencas), 3) if " ".join(sentencas[i:i+3]).strip()]
experimentos[8] = ("grouped_sentences", 0, 0, chunks_s, [])

# Teste 9: Recursive Character Splitter
sp9 = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50, separators=["\n\n", "\n", " ", ""])
experimentos[9] = ("recursive", 500, 50, sp9.split_text(texto), [])

# Teste 10: Markdown Header Splitter
headers = [("#", "Header 1"), ("##", "Header 2"), ("###", "Header 3")]
sp10 = MarkdownHeaderTextSplitter(headers_to_split_on=headers)
docs_md = sp10.split_text(texto)
experimentos[10] = ("markdown_header", 0, 0, [d.page_content for d in docs_md], [d.metadata for d in docs_md])


# GERAR EMBEDDINGS E SALVAR OS JSONS NAS PASTAS EXISTENTES
resumo_experimentos = []

for num_teste, (estrategia, chunk_size, chunk_overlap, chunks, metadados) in experimentos.items():
    pasta_teste = os.path.join(pasta_atual, f"teste_{num_teste:02d}")
    
    # Gera os embeddings para cada chunk
    embeddings = modelo_embedding.encode(chunks, show_progress_bar=False).tolist()
    
    # Monta a estrutura JSON de cada chunk
    lista_json = []
    for i, (txt, emb) in enumerate(zip(chunks, embeddings)):
        meta = metadados[i] if metadados else {}
        item = {
            "chunk_id": f"{doc_id}_test{num_teste:02d}_chunk{i+1:03d}",
            "document_id": doc_id,
            "document_name": doc_name,
            "test_id": num_teste,
            "strategy": estrategia,
            "chunk_size": chunk_size,
            "chunk_overlap": chunk_overlap,
            "text": txt,
            "embedding": emb,
            "metadata": meta
        }
        lista_json.append(item)
        
    # Salva o arquivo chunks_embeddings.json dentro da pasta do teste
    caminho_json = os.path.join(pasta_teste, "chunks_embeddings.json")
    with open(caminho_json, "w", encoding="utf-8") as f:
        json.dump(lista_json, f, ensure_ascii=False, indent=2)
        
    # CÁLCULO DAS MÉTRICAS OBRIGATÓRIAS (Item 4 do Notion)
    tamanhos = [len(c) for c in chunks] if chunks else [0]
    tam_medio = sum(tamanhos) / len(tamanhos) if chunks else 0
    tam_min = min(tamanhos) if chunks else 0
    tam_max = max(tamanhos) if chunks else 0
    
    # Chunks sobrepostos e percentual de overlap
    if chunk_overlap > 0 and len(chunks) > 1:
        qtd_sobrepostos = len(chunks) - 1
        pct_overlap = f"{(chunk_overlap / chunk_size) * 100:.0f}%"
    else:
        qtd_sobrepostos = 0
        pct_overlap = "0%"

    # Contagem EXATA de Tokens usando o tokenizador do HuggingFace
    total_tokens_exatos = sum(len(tokenizador.encode(c)) for c in chunks) if chunks else 0

    resumo_experimentos.append({
        "test_id": num_teste,
        "strategy": estrategia,
        "chunk_size": chunk_size,
        "chunk_overlap": chunk_overlap,
        "num_chunks": len(chunks),
        "avg_chunk_size": round(tam_medio, 1),
        "min_chunk_size": tam_min,
        "max_chunk_size": tam_max,
        "overlapping_chunks": qtd_sobrepostos,
        "overlap_percentage": pct_overlap,
        "total_tokens": total_tokens_exatos,
        "embedding_dimension": len(embeddings[0]) if embeddings else 0
    })
    
    print(f"Teste {num_teste:02d} concluído -> Salvo em: teste_{num_teste:02d}/chunks_embeddings.json ({len(chunks)} chunks)")


# SALVAR O SUMMARY.JSON NO DOCUMENTO_12

summary_doc = {
    "document": doc_name,
    "experiments": resumo_experimentos
}

caminho_summary = os.path.join(pasta_atual, "summary.json")
with open(caminho_summary, "w", encoding="utf-8") as f:
    json.dump(summary_doc, f, ensure_ascii=False, indent=2)

print(f"Sucesso! summary.json gerado em: {caminho_summary}")