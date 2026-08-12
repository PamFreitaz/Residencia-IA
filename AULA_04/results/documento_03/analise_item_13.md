# Análise Comparativa dos 10 Experimentos de Chunking (Documento 03)

### 1. Qual estratégia gerou mais chunks?
O **Teste 1** (Corte Fixo em 200 caracteres).
Por utilizar uma janela muito pequena de caracteres sem considerar a estrutura do texto, ele fatiou o documento sobre o algoritmo do Twitter em um volume muito alto de pequenos fragmentos.

### 2. Qual gerou menos chunks?
O **Teste 4** (Corte Fixo de 2000 caracteres) e o **Teste 10** (Markdown Header Splitter).
O Teste 4 exigia blocos imensos de texto para realizar o corte. Já o Teste 10 dividiu o documento apenas nos títulos das seções principais (como `# Candidate Sources`, `## Heavy Ranker`, `## Visibility Filtering`), gerando poucos blocos contendo seções inteiras.

### 3. Como o tamanho dos chunks variou?
Nos **Testes 1 a 6**, o tamanho variou estritamente dentro dos limites fixos de caracteres definidos (200, 500, 1000, 2000) e seus respectivos overlaps (50 e 200). Nos **Testes 7 a 10**, a variação foi dinâmica, acompanhando a extensão natural dos parágrafos, blocos de 3 sentenças e tópicos técnicos do documento.

### 4. Qual estratégia preservou melhor a estrutura dos documentos?
O **Teste 10** (Markdown Splitter) e o **Teste 9** (Recursive Splitter).
O Teste 10 manteve a hierarquia de tópicos registrada nos metadados (identificando quais explicações pertenciam a qual fase da timeline do Twitter). O Teste 9 garantiu que as etapas técnicas fossem divididas respeitando quebras lógicas.

### 5. Como tabelas foram tratadas?
Nas seções que descrevem métricas e pesos de engajamento (como pesos para Likes, Retweets, Replies):
* Nos **Testes por Caracteres Fixos (1, 2 e 5)**, as linhas e colunas em Markdown foram cortadas ao meio de forma cega.
* Nos **Testes Estruturados (7, 9 e 10)**, as tabelas foram mantidas inteiras dentro dos blocos, preservando a relação de dados para busca vetorial.

### 6. Como imagens foram tratadas?
Os diagramas de arquitetura e fluxogramas da pipeline de recomendação do Twitter (como a transição entre Candidate Generation, Ranking e Filtering) foram descartados na conversão do PDF para Markdown ou substituídos por marcações de texto indicativas (ex: `<!-- image -->`).

### 7. Quais informações foram perdidas durante a conversão PDF → Markdown?
Perdeu-se o projeto gráfico original: diagramação visual, gráficos de fluxo do sistema, layout de colunas, cabeçalhos da empresa e numeração de páginas. Contudo, todo o conteúdo conceitual e técnico em texto foi 100% preservado.

### 8. O chunking por caracteres fragmentou conceitos ou estruturas importantes?
Sim, principalmente nos **Testes 1 e 2**.
O algoritmo cortou ao meio nomes de componentes e termos técnicos cruciais do algoritmo (como separar `Sim` e `Clusters`, `Heavy` e `Ranker`, ou cortar nomes de modelos de grafos como `GraphJet`), o que prejudica diretamente a busca semântica no RAG.

### 9. O chunking por parágrafo produziu chunks muito grandes?
Não. Como os parágrafos deste documento técnico são objetivos e focados em explicar etapas específicas, a divisão por parágrafo (Teste 7) gerou blocos bem equilibrados (entre 300 e 800 caracteres).

### 10. O chunking por sentença conseguiu preservar melhor o contexto?
Sim. No **Teste 8**, o agrupamento de 3 em 3 frases evitou que orações fossem cortadas pela metade. A única limitação é que o agrupamento fixo de 3 frases pode unir a última frase da explicação de "Candidate Retrieval" com a primeira frase de "Heavy Ranking", sem perceber a mudança de assunto.

### 11. O Recursive Splitter apresentou vantagens?
Sim, foi uma das estratégias mais eficientes.
Ele tentou quebrar primeiro por parágrafos (`\n\n`), depois por linhas (`\n`) e espaços. Isso evitou a fragmentação de termos técnicos e manteve os blocos abaixo do limite de 500 caracteres com 50 de overlap.

### 12. O Markdown Splitter conseguiu preservar a estrutura semântica?
Sim, com excelente resultado. Ele utilizou os cabeçalhos do documento para separar os módulos do algoritmo e injetou o nome de cada seção dentro do campo `"metadata"` do JSON.

### 13. Qual estratégia parece mais adequada para um sistema de RAG?
O **Teste 9** (Recursive Splitter) e o **Teste 10** (Markdown Splitter).
Ambos mantêm a coesão técnica do texto e evitam que a busca vetorial perda o contexto das etapas da pipeline de recomendação.

### 14. Quais estratégias devem ser descartadas?
* **Teste 1 (Fixo 200):** Muito pequeno e corta nomes de componentes técnicos.
* **Teste 2 (Fixo 500 sem overlap):** Risco de cortar conceitos na borda do bloco.
* **Teste 4 (Fixo 2000):** Bloco grande demais que mistura diferentes fases do algoritmo no mesmo vetor.

### 15. Quais estratégias você acha que devem ser utilizadas nos próximos experimentos?
O **Recursive Character Splitter (Teste 9)** e o **Markdown Header Splitter (Teste 10)**, idealmente combinando a divisão por seções do Markdown com o limite de tamanho do Recursive Splitter.