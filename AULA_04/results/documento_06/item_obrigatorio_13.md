# Análise Comparativa dos 10 Experimentos de Chunking (Documento 06)

### 1. Qual estratégia gerou mais chunks?
O **Teste 1** (Corte Fixo em 200 caracteres), gerando **1.542 chunks**.
Por se tratar de um documento extremamente longo (333.822 caracteres), a divisão rígida em janelas de apenas 200 caracteres resultou na maior quantidade de fragmentos de todo o projeto, fatiando frases, tabelas e parâmetros no meio.

### 2. Qual gerou menos chunks?
O **Teste 10** (Markdown Header Splitter), gerando **57 chunks**, e o **Teste 4** (Corte Fixo em 2000 caracteres), com **167 chunks**.
O Teste 10 agrupou seções inteiras do artigo técnico (como `# 1 Introduction`, `# 2 Approach`, `# 3 Results` e seções do apêndice) sob os respectivos cabeçalhos do Markdown.

### 3. Como o tamanho dos chunks variou?
Nos **Testes 1 a 6**, a variação seguiu limites rígidos pré-fixados de caracteres (200, 500, 1000, 2000) e overlaps fixos (50 e 200). Nos **Testes 7 a 10**, a variação foi altamente dinâmica, adaptando-se à extensão real dos parágrafos, blocos de 3 sentenças e capítulos do artigo.

### 4. Qual estratégia preservou melhor a estrutura dos documentos?
O **Teste 10** (Markdown Splitter) e o **Teste 9** (Recursive Splitter).
O Teste 10 associou a hierarquia de tópicos do artigo aos metadados (identificando trechos como parte de `2.1 Model and Architectures` ou `3.9.1 Arithmetic`). O Teste 9 garantiu que as explicações teóricas e tabelas de hiperparâmetros fossem fatiadas respeitando a sintaxe do texto.

### 5. Como tabelas foram tratadas?
O artigo do GPT-3 contém diversas tabelas extensas (como a Tabela 2.1 com tamanhos de modelos de 125M a 175B parâmetros e tabelas de benchmarks):
* Nos **Testes por Caracteres Fixos (1, 2 e 5)**, as linhas das tabelas em Markdown foram cortadas no meio das colunas e números, corrompendo a leitura dos dados.
* Nos **Testes Estruturados (7, 9 e 10)**, as tabelas foram mantidas em blocos integrados, preservando os alinhamentos e valores numéricos dos modelos.

### 6. Como imagens foram tratadas?
Os gráficos do artigo (como as curvas de aprendizado da Figura 1.2, a comparação de performance em benchmarks da Figura 1.3 e gráficos de scaling laws) foram descartados na conversão do PDF para Markdown e substituídos por marcações indicativas de texto `<!-- image -->`.

### 7. Quais informações foram perdidas durante a conversão PDF → Markdown?
Perdeu-se a diagramação em colunas, a formatação visual de algumas equações complexas de loss/scaling, gráficos de avaliação humana de artigos gerados e a estética original do PDF de 75 páginas. A integridade do texto acadêmico, tabelas convertidas e referências foram preservadas.

### 8. O chunking por caracteres fragmentou conceitos ou estruturas importantes?
Sim, severamente nos **Testes 1 e 2**.
Por não reconhecer a semântica do texto, o algoritmo fatiou ao meio termos fundamentais do GPT-3 (como separar `few-shot`, `zero-shot`, `in-context learning`, nomes de datasets como `SuperGLUE`, `LAMBADA`, `TriviaQA` e números de parâmetros como `175B`), inviabilizando a busca vetorial precisa.

### 9. O chunking por parágrafo produziu chunks muito grandes?
Sim. No **Teste 7** (592 chunks), parágrafos extensos de discussões éticas, apêndices e blocos de tabelas em Markdown geraram chunks muito grandes, chegando a atingir picos de até 40.445 caracteres em seções não formatadas com quebra de linha dupla.

### 10. O chunking por sentença conseguiu preservar melhor o contexto?
Sim. No **Teste 8** (653 chunks), o agrupamento de 3 em 3 sentenças impediu o fatiamento de orações ao meio. No entanto, em um documento técnico extenso, o agrupamento mecânico de 3 sentenças uniu frequentemente o final de uma explicação sobre um benchmark com o início de outro benchmark.

### 11. O Recursive Splitter apresentou vantagens?
Sim, foi a estratégia mais consistente e segura.
Ele tentou dividir prioritariamente por parágrafos (`\n\n`), depois por linhas (`\n`) e palavras, mantendo os blocos controlados em ~500 caracteres com 50 de overlap, evitando fragmentação desordenada em um arquivo de mais de 300 mil caracteres.

### 12. O Markdown Splitter conseguiu preservar a estrutura semântica?
Sim. O splitter identificou todos os cabeçalhos (`#`, `##`) e registrou automaticamente o capítulo e seção do artigo no campo `"metadata"` de cada objeto JSON.

### 13. Qual estratégia parece mais adequada para um sistema de RAG?
O **Teste 9** (Recursive Splitter) e o **Teste 10** (Markdown Splitter).
Ambos preservam o contexto das seções técnicas e evitam a destruição de nomenclaturas de modelos, prompts de poucos exemplos (*few-shot*) e métricas de avaliação.

### 14. Quais estratégias devem ser descartadas?
* **Teste 1 (Fixo 200):** Produz uma quantidade excessiva de fragmentos (1.542 chunks) picotando palavras e conceitos.
* **Teste 2 (Fixo 500 sem overlap):** Alto risco de quebrar explicações acadêmicas e tabelas na borda do limite.
* **Teste 4 (Fixo 2000):** Produz blocos muito extensos que estouram o limite de entrada do modelo de embedding (alerta `539 > 512` no terminal), reduzindo a precisão da busca semântica.

### 15. Quais estratégias você acha que devem ser utilizadas nos próximos experimentos?
O **Recursive Character Splitter (Teste 9)** e o **Markdown Header Splitter (Teste 10)**, utilizando idealmente uma abordagem combinada que mapeia a hierarquia dos capítulos via Markdown e limita o tamanho máximo dos blocos via Recursive Splitter.