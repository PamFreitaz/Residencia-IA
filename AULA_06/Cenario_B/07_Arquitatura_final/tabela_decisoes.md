[Documentos Originais: FAQs, Políticas Web e PDFs]
│
▼
[3.1 Extração] ──► (Parsers de texto/HTML + Preservação de Tabelas de Frete/Preços)
│
▼
[3.2 Limpeza / Normalização] ──► (Remoção de menus e rodapés web, padronização UTF-8)
│
▼
[4. Metadados e Chunking] ──► (RecursiveCharacterTextSplitter, ~350 chars, Overlap 50)
│
▼
[6. Embeddings] ──► (Modelo: text-embedding-3-small via API OpenAI)
│
▼
[Banco Vetorial] ──► (Armazenamento com metadados estruturados: product_line, section, etc.)
│
▼
[Consulta do Cliente / Suporte] ──► (Ex: "Qual a regra de sangria para quadros canvas?")
│
▼
[Busca Semântica + Filtro] ──► (Filtro por linha de produto + Recuperação de Chunks de FAQ)
│
▼
[Geração da Resposta pelo LLM] ──► (Resposta Comercial + Citação da Fonte + Handoff Humano se necessário)


****************************************************************************************************

### Tabela de Decisões Resumida

| Etapa | Decisão | Justificativa em uma linha |
| :--- | :--- | :--- |
| **Extração** | Uso de parsers HTML/texto + preservação de tabelas de prazos e preços. | Garante a captura limpa de páginas de FAQ e tabelas comerciais sem corromper valores e regiões de frete. |
| **Limpeza** | Remoção de menus de navegação web, rodapés repetidos e padronização para UTF-8. | Elimina poluição visual e de layout de páginas de internet, mantendo ressalvas e prazos intactos. |
| **Chunking** | RecursiveCharacterTextSplitter (tamanho ~350 caracteres, overlap de 50). | Gera blocos curtos e focados, ideais para isolar regras de FAQ e políticas de atendimento de cada produto. |
| **Metadados** | Inclusão de ID, tipo, seção e metadado comercial próprio (product_line). | Permite filtrar a busca por linha de produto específica, evitando misturar regras de álbuns com quadros. |
| **Embeddings** | text-embedding-3-small (OpenAI). | Oferece excelente desempenho semântico para capturar a linguagem informal, gírias e sinônimos dos clientes. |


****************************************************************************************************

Riscos e limitações da sua própria proposta (O que essa arquitetura não resolve bem?)

1. Dados transacionais em tempo real: A arquitetura baseada em RAG não consegue consultar o status de entrega de um pedido específico ou o estoque em tempo real de um brinde, exigindo integrações ativas com o banco de dados transacional e APIs de transportadoras.

2. Cálculos analíticos globais: O sistema não responde bem a perguntas gerenciais de volume (ex: "Qual foi o produto mais vendido com desconto no mês passado?"), pois o RAG busca trechos de texto em políticas e FAQs, e não realiza somas ou contagens em tabelas SQL.

3. Linguagem excessivamente ambígua ou incompleta: Se o cliente fizer uma pergunta muito vaga sem citar o contexto (ex: "Quanto tempo demora?" sem especificar se é produção, frete ou postagem), o sistema pode recuperar chunks incorretos ou exigir uma nova pergunta de esclarecimento.

****************************************************************************************************

Diagrama em Mermaid:

graph TD
    A[FAQs e Políticas Web / PDFs] --> B[3.1 Extração: Parsers de Texto / HTML / Tabelas]
    B --> C[3.2 Limpeza / Normalização: UTF-8 / Remoção de Menus Web]
    C --> D[4. Metadados e Chunking: RecursiveCharacterTextSplitter]
    D --> E[6. Embeddings: text-embedding-3-small]
    E --> F[Banco Vetorial: Armazenamento com metadados product_line]
    G[Consulta do Cliente / Suporte] --> H[Busca Semântica + Filtro por Linha de Produto]
    F --> H
    H --> I[Geração da Resposta Comercial pelo LLM + Citação da Fonte + Handoff]