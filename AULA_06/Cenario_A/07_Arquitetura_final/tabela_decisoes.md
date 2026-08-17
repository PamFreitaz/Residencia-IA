[Documentos Originais: PDFs / Manuais]
                  │
                  ▼
         [3.1 Extração] ──► (PyPDF / OCR para digitalizados + Preservação de Tabelas)
                  │
                  ▼
     [3.2 Limpeza / Normalização] ──► (Remoção de rodapés repetidos, padronização UTF-8)
                  │
                  ▼
       [4. Metadados e Chunking] ──► (RecursiveCharacterTextSplitter, ~600 chars, Overlap 100)
                  │
                  ▼
         [6. Embeddings] ──► (Modelo: text-embedding-3-small via API OpenAI)
                  │
                  ▼
        [Banco Vetorial] ──► (Armazenamento com metadados estruturados: equipment_model, page, etc.)
                  │
                  ▼
     [Consulta do Usuário] ──► (Ex: "Qual perfil ICC usar na Epson SureColor?")
                  │
                  ▼
      [Busca Semântica + Filtro] ──► (Filtro por modelo de equipamento + Recuperação de Chunks)
                  │
                  ▼
    [Geração da Resposta pelo LLM] ──► (Resposta + Citação da Fonte e Página)


****************************************************************************************************


    ### Tabela de Decisões Resumida

| Etapa | Decisão | Justificativa em uma linha |
| :--- | :--- | :--- |
| **Extração** | Uso de leitores diretos de texto (PyPDF) + OCR e preservação de tabelas. | Garante a captura íntegra de dados textuais e tabelas numéricas de conversão de cores sem corromper o layout. |
| **Limpeza** | Remoção de cabeçalhos/rodapés repetidos e padronização para UTF-8. | Elimina poluição textual mantendo avisos técnicos essenciais e integridade de símbolos de unidades de medida. |
| **Chunking** | RecursiveCharacterTextSplitter (tamanho ~600 caracteres, overlap de 100). | Respeita os limites lógicos dos parágrafos e seções, mantendo o contexto de manuais técnicos coeso. |
| **Metadados** | Inclusão de ID, página, tipo e metadado próprio (equipment_model). | Permite filtrar a busca por plotter específica, evitando cruzar instruções de equipamentos diferentes. |
| **Embeddings** | text-embedding-3-small (OpenAI). | Oferece alta performance em múltiplos idiomas e captura excelente proximidade semântica para termos técnicos e de colorimetria. |


****************************************************************************************************

Riscos e limitações da sua própria proposta (O que essa arquitetura não resolve bem?)

1. Agregações e Consultas Numéricas Globais: A arquitetura baseada puramente em RAG não consegue responder bem a perguntas analíticas de grande volume (ex: "Qual foi o total de metros quadrados de papel fosco consumidos no último trimestre?"), pois o sistema recupera fragmentos de texto e não calcula somas de bancos relacionais.

2. Mudanças dinâmicas em tempo real: Se um parâmetro de calibração for alterado urgentemente na oficina, a resposta do RAG continuará baseada no documento estático até que o novo arquivo seja ingerido e a base seja reindexada.

3. Interpretação de imagens complexas sem OCR avançado: Embora tratemos diagramas via descrição textual, esquemas gráficos muito complexos de circuitos de impressoras podem perder detalhes cruciais na conversão para texto puro.

****************************************************************************************************

diagrama em Mermaid:

graph TD
    A[Documentos Originais: Manuais PDF] --> B[3.1 Extração: PyPDF / OCR / Tabelas]
    B --> C[3.2 Limpeza / Normalização: UTF-8 / Remoção de Rodapés]
    C --> D[4. Metadados e Chunking: RecursiveCharacterTextSplitter]
    D --> E[6. Embeddings: text-embedding-3-small]
    E --> F[Banco Vetorial: Armazenamento com metadados]
    G[Consulta do Usuário] --> H[Busca Semântica + Filtro por Equipamento]
    F --> H
    H --> I[Geração da Resposta pelo LLM + Citação da Fonte]