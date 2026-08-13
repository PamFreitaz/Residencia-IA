# Análise Comparativa dos 10 Experimentos de Chunking (Documento 11)

### 1. Qual estratégia gerou mais chunks?
O **Teste 1** (Corte Fixo em 200 caracteres), gerando **360 chunks**.
Sendo o artigo clássico que introduz a arquitetura RAG (*Retrieval-Augmented Generation*), a utilização de uma janela de apenas 200 caracteres resultou na fragmentação cega e excessiva do documento.

### 2. Qual gerou menos chunks?
O **Teste 10** (Markdown Header Splitter), com apenas **33 chunks**, seguido de perto pelo **Teste 4** (Corte Fixo de 2000 caracteres), com **36 chunks**.
O Teste 10 reduziu significativamente a quantidade de recortes ao agrupar grandes blocos de conteúdo semanticamente sob os cabeçalhos estruturais do artigo, enquanto o Teste 4 exigiu blocos muito grandes puramente pela contagem de caracteres.

### 3. Como o tamanho dos chunks variou?
Nos **Testes 1 a 6**, o tamanho dos fragmentos obedeceu rigorosamente aos limites preestabelecidos (200, 500, 1000 e 2000 caracteres), com sobreposições (*overlaps*) precisas. Já nos **Testes 7 a 10**, o tamanho foi flexível, variando conforme a extensão real dos parágrafos, agrupamentos de sentenças ou capítulos e seções.

### 4. Qual estratégia preservou melhor a estrutura dos documentos?
O **Teste 10** (Markdown Splitter) e o **Teste 9** (Recursive Splitter).
O Teste 10 incorporou o mapeamento dos capítulos nos metadados, distinguindo seções como `## 2 Methods` e `## 4 Results`. O Teste 9 conseguiu manter a coesão textual ao explicar o funcionamento das abordagens teóricas, sem cortes artificiais.

### 5. Como tabelas foram tratadas?
O artigo contém várias tabelas relatando os *scores* do RAG em diferentes *benchmarks* de *Question Answering* e geração de texto (ex: Tabela 1 e Tabela 2).
* Nos **Testes por Caracteres Fixos (1, 2 e 5)**, a estrutura dessas tabelas em Markdown foi cortada no meio, separando os modelos testados dos seus respectivos resultados.
* Nos **Testes Estruturados (7, 9 e 10)**, as tabelas permaneceram unificadas dentro dos blocos, garantindo a relação correta entre linhas e colunas.

### 6. Como imagens foram tratadas?
A "Figure 1", que detalha graficamente a arquitetura conceitual do RAG, bem como os gráficos de posterior de documentos, foram removidos e substituídos pela marcação de texto `<!-- image -->`. Apenas as legendas descritivas dessas figuras foram preservadas.

### 7. Quais informações foram perdidas durante a conversão PDF → Markdown?
Foram perdidas a formatação em múltiplas colunas típica dos artigos acadêmicos, a renderização gráfica perfeita de equações probabilísticas avançadas e os elementos visuais dos diagramas. A essência do texto, métricas tabulares e bibliografia permaneceram.

### 8. O chunking por caracteres fragmentou conceitos ou estruturas importantes?
Sim, criticamente nos **Testes 1 e 2**.
Fórmulas matemáticas para o cálculo marginal dos modelos, termos técnicos importantes e as citações bibliográficas contidas ao longo do texto foram separadas de maneira ilógica, o que afeta severamente a qualidade da vetorização.

### 9. O chunking por parágrafo produziu chunks muito grandes?
Sim. No **Teste 7** (131 chunks), as extensas listas de referências acadêmicas ao final do artigo, que costumam utilizar apenas quebras de linha simples em vez de parágrafos duplos, acabaram sendo englobadas em blocos gigantescos.

### 10. O chunking por sentença conseguiu preservar melhor o contexto?
De forma parcial. No **Teste 8** (233 chunks), a técnica garantiu a integridade de sentenças discursivas sobre as conclusões da pesquisa. Todavia, agrupar rigidamente de 3 em 3 frases dividiu de forma prejudicial as tabelas de métricas e o apêndice do documento.

### 11. O Recursive Splitter apresentou vantagens?
Sim, exibiu um excelente equilíbrio.
O **Teste 9** (228 chunks) soube lidar bem com a seção de referências e apêndices, pois utilizou a quebra simples de linha (`\n`) para cortar o texto de forma limpa quando as quebras de parágrafos duplos não existiam, evitando blocos monstruosos.

### 12. O Markdown Splitter conseguiu preservar a estrutura semântica?
Sim. Ele mapeou a hierarquia científica original, separando os resultados por tópicos, como `# 3 Experiments` e suas respectivas subseções `# 3.1 Open-domain Question Answering`, utilizando esses títulos como metadados enriquecedores de cada *chunk*.

### 13. Qual estratégia parece mais adequada para um sistema de RAG?
O **Teste 9** (Recursive Splitter) e o **Teste 10** (Markdown Splitter).
Para recuperar informações precisas sobre as métricas e o método de treinamento explicados neste artigo, é essencial que tabelas e explicações matemáticas permaneçam agrupadas de forma semântica, o que só é oferecido por essas duas estratégias.

### 14. Quais estratégias devem ser descartadas?
* **Teste 1 (Fixo 200):** Quebra o texto demasiadamente, gerando ruído e perdendo contexto matemático.
* **Teste 2 (Fixo 500 sem overlap):** Pode fragmentar equações na borda do bloco sem que o próximo *chunk* retome a lógica.
* **Teste 4 (Fixo 2000):** Gerou fragmentos tão extensos que causaram **erro de indexação no tokenizador** (alerta `521 > 512 tokens` visível no terminal), o que leva a truncamento e perda de dados valiosos.

### 15. Quais estratégias você acha que devem ser utilizadas nos próximos experimentos?
O **Recursive Character Splitter (Teste 9)** aliado ao **Markdown Header Splitter (Teste 10)**. O uso coordenado dessas ferramentas garantirá que a hierarquia capitular oriente a divisão semântica, enquanto os limites seguros recursivos impedirão que tabelas e referências estourem a janela de processamento.