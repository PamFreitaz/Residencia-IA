# Esclarecimento Técnico: Tokens, Uso de APIs e Escolha dos Modelos

## 1. A Diferença Entre os Conceitos de "Token"

Durante o desenvolvimento deste experimento, é importante diferenciar dois conceitos frequentemente associados ao termo **"Token"**:

* **Tokens de Texto (Unidades de Processamento Linguístico):** São pedaços de palavras ou sílabas utilizados pelos modelos de Inteligência Artificial para ler e processar dados. O professor solicitou o registro do número de tokens para avaliar o tamanho de cada *chunk*.
* **Token de API (API Key / Chave de Acesso):** É a chave de autenticação individual (senha) utilizada para se conectar a um serviço pago ou gerenciado na nuvem (como OpenRouter, Groq ou OpenAI).

---

## 2. Como a API e a Contagem de Tokens foram Aplicadas no Projeto

### A. API de Embeddings (OpenRouter / HuggingFace)
No **Item 9 da atividade**, a instrução permitia a escolha entre provedores via API (como OpenRouter) ou modelos abertos de embeddings gerenciados localmente/nuvem via HuggingFace.

Para garantir experimentos reproduzíveis, rápidos e sem custos inesperados, utilizamos o modelo **`paraphrase-multilingual-MiniLM-L12-v2`**. Cada *chunk* de texto foi enviado para este modelo vetorial, retornando um vetor semântico de 384 dimensões salvo na propriedade `"embedding"` de cada objeto no arquivo `chunks_embeddings.json`.

### B. Contagem Precisa de Tokens por Chunk
Em vez de depender de uma chamada externa paga apenas para contar palavras, a contagem de tokens exigida no **Item 4** foi realizada através do **tokenizador oficial do modelo** (`AutoTokenizer` da biblioteca `transformers` / HuggingFace). 

Isso garante que cada vetor gerado corresponda exatamente à quantidade de tokens interpretada pela arquitetura de IA escolhida.

---

## 3. O Papel do Groq (ou OpenRouter) na Arquitetura RAG

Caso o objetivo seja integrar modelos LLM generativos via API externa usando chaves de acesso (como a **API Key do Groq** ou **OpenRouter**), o fluxo da pipeline RAG se divide em duas partes bem definidas:

1. **Etapa Atual (Indexação e Vetorização - Aula 04):**
   * Pega os arquivos em Markdown.
   * Aplica os splitters de *chunking*.
   * Gera os vetores (*embeddings*) de cada trecho de texto.
   * Salva os JSONs com metadados e vetores.

2. **Etapa Seguinte (Recuperação e Geração - RAG):**
   * O usuário faz uma pergunta no sistema.
   * A pergunta é convertida em vetor.
   * O sistema busca os *chunks* mais parecidos no nosso arquivo JSON.
   * **Aqui entra a API do Groq/OpenRouter:** Os *chunks* recuperados são enviados junto da pergunta do usuário para a API da LLM (ex: Llama 3 via Groq) para que a IA escreva uma resposta final baseada no documento.

---

## 4. Segurança de Chaves de API no Código

Quando utilizamos APIs externas que exigem chaves de acesso (`GROQ_API_KEY` ou `OPENROUTER_API_KEY`), a boa prática de engenharia de software aplicada ao projeto exige:

1. Guardar a chave em um arquivo oculto de variáveis de ambiente (`.env`):
   ```env
   GROQ_API_KEY="sua_chave_aqui"


---

### Sobre APR:

* O pipeline foi estruturado para suportar modelos de embeddings via API (como OpenRouter/HuggingFace) e locais. Para a contagem exata de tokens de cada chunk, usamos o tokenizador do próprio modelo de embeddings. E deixamos a estrutura de chave via `.env` pronta para quando formos conectar a LLM de geração de resposta (usando o Groq na etapa final do RAG)."*