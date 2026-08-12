# Roteiro de Apresentação e Explicação Técnica (

## Visão Geral

* **Documento Analisado:** `bioetica_e_ia.pdf` (convertido para `bioetica_e_ia.md` com ~28.415 caracteres).
* **Objetivo:** Testar e comparar **10 estratégias de chunking** (divisão de texto) para avaliar qual delas gera os melhores blocos de contexto para um sistema de **RAG (Retrieval-Augmented Generation)**.
* **Modelo de Embeddings:** `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` (gera vetores semânticos de 384 dimensões).

---

## Como o Código (`main.py`) Foi Estruturado

1. **Leitura e Extração:** O arquivo Markdown é lido do disco em UTF-8.
2. **Execução dos 10 Experimentos:** O texto é submetido aos splitters do LangChain e rotinas customizadas em Python.
3. **Vetorização (Embeddings):** Cada bloco de texto gerado é enviado para o modelo vetorial Multilingual MiniLM.
4. **Contagem Exata de Tokens:** Usei o `AutoTokenizer` oficial do modelo no HuggingFace para contar com precisão os tokens de cada *chunk*, evitando estimativas vagas.
5. **Estrutura de Saída:**
   * Cada teste gera um arquivo `chunks_embeddings.json` na sua respectiva pasta (`teste_01` até `teste_10`).
   * As métricas acumuladas (tamanho mínimo, máximo, média, overlap e total de tokens) são consolidadas no arquivo central `summary.json`.

---

## Os 10 Experimentos Executados

1. **Teste 1 (Fixo 200 / Overlap 0):** Janela pequena e cega. Gerou o maior número de chunks (~181), mas fatiou palavras e rasgou frases ao meio.

2. **Teste 2 (Fixo 500 / Overlap 0):** Janela média. Melhorou a leitura, mas ainda com alto risco de cortar conceitos na borda do bloco.

3. **Teste 3 (Fixo 1000 / Overlap 0):** Bloco grande. Agrupou mais texto, porém misturou diferentes parágrafos
.
4. **Teste 4 (Fixo 2000 / Overlap 0):** Bloco gigante. Poucos chunks (~19), mas juntou múltiplos tópicos em um só vetor, diluindo a precisão da busca.

5. **Teste 5 (Fixo 500 / Overlap 50):** 10% de sobreposição. Criou transição suave entre blocos, reduzindo perda de informação nas bordas
6. **Teste 6 (Fixo 500 / Overlap 200):** 40% de sobreposição. Gerou redundância alta (~120 chunks), inflando o custo de tokens sem ganho semântico proporcional.

7. **Teste 7 (Por Parágrafo):** Usou `CharacterTextSplitter` com separador `\n\n`. Preservou a unidade natural do texto com tamanho médio ideal (300 a 600 letras).

8. **Teste 8 (Agrupamento de 3 Sentenças):** Agrupou frases completas via Expressões Regulares (Regex). Evitou cortes no meio das orações.

9. **Teste 9 (Recursive Character Splitter):** **Uma das melhores estratégias.** Tenta cortar por `\n\n`, depois por `\n`, espaços e letras. Mantém tamanho limite (500 caracteres com 50 de overlap) sem quebrar estruturas humanas.

10. **Teste 10 (Markdown Header Splitter):** **Estratégia mais semântica.** Separou o texto pelos títulos (`## Autonomia`, `## LGPD`) e salvou esses nomes nos metadados (`metadata`).

---

## Destaques e Descobertas Importantes

### A. O Achado Prático do Teste 10 (Estouro de Limite do Modelo)

> *"No Teste 10, o terminal exibiu um alerta informando que um dos chunks gerou 1.525 tokens, superando o limite máximo de 512 tokens do nosso modelo de embedding (MiniLM). Isso comprova que usar apenas o Markdown Splitter pode ser perigoso se um capítulo for muito longo. A solução ideal para a prática de RAG é uma abordagem híbrida: primeiro dividir por títulos com o Markdown Splitter e, em seguida, aplicar o Recursive Splitter para limitar seções longas a 500 caracteres."*

### B. Veredito das Melhores e Piores Estratégias

* **Melhores (Para RAG):** **Teste 9 (Recursive)** e **Teste 10 (Markdown)**. Eles mantêm a coesão do texto, respeitam a leitura humana e entregam contextos ricos para a busca vetorial.
* **A Descartar:** **Teste 1** (muito pequeno e corta palavras), **Teste 2** (risco na borda por falta de overlap)e **Teste 4** (muito grande, mistura múltiplos temas).

### C. Tratamento de Imagens, Tabelas e Perdas da Conversão
* **Imagens:** O arquivo Markdown converteu as fotos em marcações/referências textuais (ex: `<!-- image -->`). O conteúdo puramente visual é descartado porque o Markdown é focado em texto bruto.
* **Tabelas:** Nos testes fixos por caracteres, as tabelas são fatiadas ao meio. Nos testes estruturados (7, 9 e 10), foram mantidas em blocos únicos.
* **Perda do PDF:** Perdeu-se apenas a formatação estética (duas colunas, fontes decorativas, número de página no rodapé). O conteúdo textual foi 100% preservado.

### D. Esclarecimento de Tokens e Arquitetura de API
* A contagem de tokens do relatório é **exata** e foi calculada localmente através do tokenizador da biblioteca `transformers` (HuggingFace).
* "O escopo desta etapa focou na extração, chunking e vetorização local do documento. A estrutura dos arquivos JSON com vetores e metadados foi padronizada para ser consumida por uma LLM (como Groq ou OpenRouter) na próxima fase do pipeline RAG."