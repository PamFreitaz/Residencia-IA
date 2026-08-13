# Análise Comparativa dos 10 Experimentos de Chunking (Documento 10)

### 1. Qual estratégia gerou mais chunks?
O **Teste 1** (Corte Fixo em 200 caracteres), gerando **499 chunks**.
Por se tratar de um *paper* técnico denso sobre a arquitetura LoRA (Low-Rank Adaptation) e o ajuste de matrizes em redes neurais, o corte rígido de 200 caracteres fragmentou severamente equações, tabelas e parágrafos teóricos.

### 2. Qual gerou menos chunks?
O **Teste 10** (Markdown Header Splitter), com apenas **38 chunks**, seguido pelo **Teste 4** (Corte Fixo de 2000 caracteres), com **50 chunks**.
O Teste 10 agrupou seções inteiras do artigo sob seus cabeçalhos originais (ex: `## 4 OUR METHOD` ou `## 5 EMPIRICAL EXPERIMENTS`), criando blocos contínuos e reduzindo o número total de *chunks*. 

### 3. Como o tamanho dos chunks variou?
Nos **Testes 1 a 6**, a variação seguiu limites rígidos de caracteres e *overlaps* matemáticos (200 a 2000 caracteres). Nos **Testes 7 a 10**, a divisão adaptou-se de forma inteligente e dinâmica à estrutura do documento, acompanhando parágrafos descritivos, quebras de seções e agrupamentos de 3 frases.

### 4. Qual estratégia preservou melhor a estrutura dos documentos?
O **Teste 10** (Markdown Splitter) e o **Teste 9** (Recursive Splitter).
O Teste 10 manteve a hierarquia acadêmica perfeita, separando a introdução das análises empíricas e apêndices de hiperparâmetros, guardando isso nos metadados. O Teste 9 evitou que as explicações das funções matemáticas fossem divididas de forma abrupta.

### 5. Como tabelas foram tratadas?
O artigo possui tabelas enormes e cruciais, como a Tabela 2 de resultados do *GLUE benchmark* e as extensas tabelas de hiperparâmetros no apêndice (Tabelas 9 a 18).
* Nos **Testes por Caracteres Fixos (1, 2 e 5)**, a estrutura relacional do Markdown foi destruída, separando os nomes dos modelos (ex: `RoB large (LoRA)`) das suas respectivas pontuações.
* Nos **Testes Estruturados (7, 9 e 10)**, as tabelas permaneceram unidas dentro do mesmo bloco, o que é vital para buscar e comparar os resultados dos modelos corretamente.

### 6. Como imagens foram tratadas?
Elementos visuais importantes do artigo, como a "Figura 1: Our reparametrization" e a "Figura 2: GPT-3 175B validation accuracy", não foram processados como imagens gráficas na conversão e foram substituídos apenas pela *tag* indicativa `<!-- image -->`. 

### 7. Quais informações foram perdidas durante a conversão PDF → Markdown?
Perdeu-se a formatação gráfica de equações matemáticas avançadas (marcadas ocasionalmente como `<!-- formula-not-decoded -->`), o formato de texto em duas colunas típico de conferências científicas, logotipos e o layout exato dos gráficos de similaridade de subespaço vetorial. Todo o texto essencial e dados de tabelas foram preservados.

### 8. O chunking por caracteres fragmentou conceitos ou estruturas importantes?
Sim, drasticamente nos **Testes 1 e 2**.
O algoritmo cego interrompeu termos técnicos no meio, como a separação das matrizes `W0 + BA`, bem como fatiou nomes de métricas, equações de ranqueamento e as citações bibliográficas, arruinando a qualidade semântica dos embeddings.

### 9. O chunking por parágrafo produziu chunks muito grandes?
Sim. No **Teste 7** (223 chunks), seções contendo longas listas de referências acadêmicas ou tabelas massivas de hiperparâmetros (que não contêm quebra dupla de linha `\n\n`) foram aglutinadas em blocos gigantescos.

### 10. O chunking por sentença conseguiu preservar melhor o contexto?
Em parte. O **Teste 8** (271 chunks) foi bom para a parte dissertativa, impedindo que a explicação sobre *inference latency* ou adaptações *low-rank* fosse rasgada no meio. No entanto, agrupar de 3 em 3 frases destrói a coesão das tabelas técnicas e listas pontuadas de hiperparâmetros.

### 11. O Recursive Splitter apresentou vantagens?
Sim, foi excelente.
O **Teste 9** (296 chunks) contornou a limitação das tabelas e blocos grandes. Quando a quebra por parágrafo duplo não era viável nas seções de anexos ou código matemático, ele fez o corte pelas quebras simples (`\n`), mantendo os blocos dentro do limite seguro sem perder a coesão.

### 12. O Markdown Splitter conseguiu preservar a estrutura semântica?
Sim. O algoritmo mapeou perfeitamente as seções do documento (ex: `# 1 INTRODUCTION`, `# 4 OUR METHOD`, `# 7 UNDERSTANDING THE LOW-RANK UPDATES`) e transformou esses títulos em metadados injetados em cada registro JSON.

### 13. Qual estratégia parece mais adequada para um sistema de RAG?
O **Teste 9** (Recursive Splitter) e o **Teste 10** (Markdown Splitter).
Para um RAG técnico que precisa responder "Como o LoRA afeta a latência de inferência no GPT-3?", o sistema depende dos metadados extraídos pelo Teste 10 e da divisão respeitosa de tabelas e equações propiciada pelo Teste 9.

### 14. Quais estratégias devem ser descartadas?
* **Teste 1 (Fixo 200):** Fragmenta equações matemáticas e tabelas até que percam o sentido.
* **Teste 2 (Fixo 500 sem overlap):** Pode cortar explicações de fórmulas ou matrizes de peso na borda do limite.
* **Teste 4 (Fixo 2000):** Produziu um **erro de estouro de tokens** (`521 > 512`), gerando vetores imensos que confundem a representação matemática do *embedding* e truncam dados no RAG.

### 15. Quais estratégias você acha que devem ser utilizadas nos próximos experimentos?
A combinação do **Recursive Character Splitter (Teste 9)** com o **Markdown Header Splitter (Teste 10)**. O uso em conjunto garante que a estrutura em árvore do *paper* guie os vetores, enquanto o *Recursive Splitter* garante que tabelas gigantes não estourem a janela de tokens.