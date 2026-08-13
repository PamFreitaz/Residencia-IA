# Análise Comparativa dos 10 Experimentos de Chunking (Documento 08)

### 1. Qual estratégia gerou mais chunks?
O **Teste 1** (Corte Fixo em 200 caracteres), gerando **1.440 chunks**.
Por ser um artigo acadêmico denso sobre o treinamento do InstructGPT via *Reinforcement Learning from Human Feedback* (RLHF), a janela de apenas 200 caracteres causou uma fragmentação massiva e cega do texto.

### 2. Qual gerou menos chunks?
O **Teste 4** (Corte Fixo de 2000 caracteres), com **145 chunks**, seguido pelo **Teste 10** (Markdown Header Splitter), com **195 chunks**.
O Teste 4 exigiu blocos muito longos para efetuar os cortes. O Teste 10 utilizou os cabeçalhos das seções do artigo para agrupar o conteúdo semanticamente, resultando em menos blocos, porém mais coesos.

### 3. Como o tamanho dos chunks variou?
Nos **Testes 1 a 6**, o tamanho variou estritamente dentro dos limites fixos definidos (200, 500, 1000 e 2000 caracteres) e seus respectivos *overlaps*[. Nos **Testes 7 a 10**, a variação foi flexível, adaptando-se organicamente ao tamanho real dos parágrafos, agrupamentos de sentenças e capítulos do artigo.

### 4. Qual estratégia preservou melhor a estrutura dos documentos?
O **Teste 10** (Markdown Splitter) e o **Teste 9** (Recursive Splitter).
O Teste 10 preservou a divisão lógica do artigo identificando e associando metadados aos capítulos como `## 3 Methods and experimental details` e `## 4 Results`[. O Teste 9 manteve a coesão de parágrafos explicativos e listas de instruções de rotulagem.

### 5. Como tabelas foram tratadas?
O artigo possui tabelas extensas, como a distribuição de categorias de uso da API (Tabela 1), exemplos de *prompts* ilustrativos (Tabela 2) e dados demográficos dos anotadores (Tabela 12).
* Nos **Testes por Caracteres Fixos (1, 2 e 5)**, a estrutura relacional das tabelas foi rasgada ao meio de forma arbitrária.
* Nos **Testes Estruturados (7, 9 e 10)**, as tabelas permaneceram agrupadas no mesmo bloco, preservando a coerência dos dados e exemplos de *prompts* para o modelo vetorial.

### 6. Como imagens foram tratadas?
Os diversos elementos gráficos do documento, como a Figura 1 (avaliações humanas de vários modelos) e a Figura 2 (diagrama das três etapas do método RLHF), foram descartados durante a conversão do PDF para Markdown, sendo substituídos exclusivamente por marcações em texto como `<!-- image -->`.

### 7. Quais informações foram perdidas durante a conversão PDF → Markdown?
Perdeu-se a formatação gráfica das equações matemáticas e fórmulas de perda do modelo de recompensa, o layout tradicional de duas colunas, a formatação visual dos gráficos de barras sobre toxicidade e alinhamento, e os estilos de cabeçalho. O texto corrido, dados tabelados e referências foram integralmente preservados.

### 8. O chunking por caracteres fragmentou conceitos ou estruturas importantes?
Sim, drasticamente nos **Testes 1 e 2**.
Por não analisar a sintaxe, o algoritmo cortou ao meio termos fundamentais como `Reinforcement Learning from Human Feedback`, nomes de modelos (`InstructGPT`, `GPT-3`), siglas de métricas (`ROUGE-L`, `BLEU`) e exemplos vitais de instruções fornecidas aos avaliadores humanos.

### 9. O chunking por parágrafo produziu chunks muito grandes?
Sim. No **Teste 7** (1.036 chunks), seções com blocos densos, como as longas explicações nos Apêndices sobre instruções de rotulagem (*Labeling instructions*) e a extensa lista de Referências Bibliográficas, geraram vetores excessivamente grandes por não conterem quebras de parágrafo convencionais (`\n\n`).

### 10. O chunking por sentença conseguiu preservar melhor o contexto?
Sim. No **Teste 8** (956 chunks), o agrupamento a cada 3 frases evitou que explicações teóricas sobre o comportamento dos modelos fossem cortadas ao meio. A desvantagem ocorreu nas tabelas e listas de referência, onde agrupar mecanicamente 3 sentenças fundiu autores e dados estatísticos não correlacionados de forma sequencial.

### 11. O Recursive Splitter apresentou vantagens?
Sim, provou ser altamente eficaz.
O **Teste 9** (846 chunks) conseguiu lidar perfeitamente com as tabelas de *prompts* e a seção de referências. Ao não encontrar a quebra de parágrafo duplo, ele utilizou a quebra simples de linha (`\n`), dividindo o conteúdo de forma lógica sem ultrapassar o limite de tokens.

### 12. O Markdown Splitter conseguiu preservar a estrutura semântica?
Sim. Ele mapeou a hierarquia do documento com precisão, vinculando o conteúdo de texto aos seus respectivos títulos estruturais, como as subseções do apêndice (`## B.3 Labeler demographic data`) e metodologias (`## 3.1 High-level methodology`), garantindo rastreabilidade através do campo `"metadata"`.

### 13. Qual estratégia parece mais adequada para um sistema de RAG?
O **Teste 9** (Recursive Splitter) e o **Teste 10** (Markdown Splitter).
Ambos mantêm a coesão da terminologia técnica sobre alinhamento de IA, mantêm as métricas e os exemplos de *prompts* intactos e geram *embeddings* de altíssima fidelidade ao contexto original do artigo do InstructGPT.

### 14. Quais estratégias devem ser descartadas?
* **Teste 1 (Fixo 200):** Excesso de fatiamento (1.440 blocos), destruindo conceitos técnicos e métricas de desempenho.
* **Teste 2 (Fixo 500 sem overlap):** Risco de cortar orientações do *prompt* exatamente na borda do limite do bloco.
* **Teste 4 (Fixo 2000):** O limite extenso causou **erro no terminal** pois os blocos estouraram a capacidade máxima do tokenizador HuggingFace (*523 > 512*), prejudicando a indexação e gerando perda de informação.

### 15. Quais estratégias você acha que devem ser utilizadas nos próximos experimentos?
O **Recursive Character Splitter (Teste 9)** e o **Markdown Header Splitter (Teste 10)**. O formato ideal seria uma combinação de ambos: o *Markdown Splitter* para injetar o contexto dos capítulos nos metadados, e o *Recursive Splitter* para garantir que as seções não ultrapassem a capacidade do modelo de *embeddings*.