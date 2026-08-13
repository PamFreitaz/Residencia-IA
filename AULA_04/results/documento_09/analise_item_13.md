# Análise Comparativa dos 10 Experimentos de Chunking (Documento 09)

### 1. Qual estratégia gerou mais chunks?
O **Teste 1** (Corte Fixo em 200 caracteres), gerando **524 chunks**.
Por se tratar de um artigo técnico que detalha a arquitetura e os dados de treinamento do modelo LLaMA, a janela restrita de 200 caracteres fragmentou o texto cegamente em um volume alto de pequenos pedaços.

### 2. Qual gerou menos chunks?
O **Teste 4** (Corte Fixo de 2000 caracteres), com **53 chunks**, seguido de perto pelo **Teste 10** (Markdown Header Splitter), com **54 chunks**.
O Teste 4 atingiu esse número pois exige um acúmulo muito grande de texto para efetuar o corte. O Teste 10 agrupou as seções inteiras do *paper* (como `## 3 Main results` e `## 5 Bias, Toxicity and Misinformation`) através da marcação dos cabeçalhos em poucos blocos coerentes.

### 3. Como o tamanho dos chunks variou?
Nos **Testes 1 a 6**, a variação seguiu limites rígidos de caracteres e *overlaps* previamente fixados no código (200 a 2000 caracteres). Nos **Testes 7 a 10**, a variação se adaptou organicamente à disposição real do documento, acompanhando parágrafos explicativos, tabelas de hiperparâmetros e títulos Markdown das seções do artigo.

### 4. Qual estratégia preservou melhor a estrutura dos documentos?
O **Teste 10** (Markdown Splitter) e o **Teste 9** (Recursive Splitter).
O Teste 10 registrou a hierarquia exata do artigo (ex: agrupando o que pertencia à subseção `## 2.1 Pre-training Data` nos metadados). O Teste 9 garantiu que as sentenças explicativas de *benchmarks* e arquitetura não fossem corrompidas no meio do raciocínio.

### 5. Como tabelas foram tratadas?
O artigo possui 16 tabelas essenciais contendo as fontes dos dados de treino (Tabela 1), hiperparâmetros (Tabela 2) e dezenas de resultados quantitativos de *benchmarks* como MMLU, TriviaQA e HumanEval.
* Nos **Testes por Caracteres Fixos (1, 2 e 5)**, as tabelas em Markdown foram fatiadas ao meio, separando os nomes dos modelos das suas pontuações e colunas.
* Nos **Testes Estruturados (7, 9 e 10)**, a integridade tabular foi respeitada dentro dos blocos, permitindo que a relação estrutural dos dados fosse preservada.

### 6. Como imagens foram tratadas?
Os elementos visuais, como o Gráfico 1 (Training loss over train tokens) e o Gráfico 2 (Evolution of performance), foram ignorados na extração de texto bruto ou substituídos apenas pela tag `<!-- image -->`. Apenas as legendas em texto dessas imagens foram mantidas.

### 7. Quais informações foram perdidas durante a conversão PDF → Markdown?
Perdeu-se o layout de dupla coluna adotado no PDF, bem como a renderização matemática avançada de algumas equações (como as fórmulas de cálculo do *Carbon Footprint*), o estilo de fontes da publicação e logos. O texto técnico e as métricas tabulares, contudo, foram completamente salvos no Markdown.

### 8. O chunking por caracteres fragmentou conceitos ou estruturas importantes?
Sim, drasticamente nos **Testes 1 e 2**.
O algoritmo cego rompeu termos-chave como `Common Sense Reasoning`, `NaturalQuestions`, configurações arquiteturais (`Rotary Embeddings`, `SwiGLU`) e referências de citação, o que destrói a utilidade do vetor semântico gerado.

### 9. O chunking por parágrafo produziu chunks muito grandes?
Sim. No **Teste 7** (281 chunks), o algoritmo produziu vetores desproporcionais e maciços nas seções mais densas do artigo, especialmente em `## 7 Related work` e `## References`, onde a ausência de quebras duplas (`\n\n`) fez com que blocos longos de bibliografia fossem agrupados juntos.

### 10. O chunking por sentença conseguiu preservar melhor o contexto?
Em parte. O **Teste 8** (303 chunks) foi eficiente para manter explicações sobre os modelos coesas, garantindo que frases inteiras fossem preservadas. No entanto, agrupar rigidamente 3 sentenças destruiu a leitura das linhas soltas de tabelas de métricas de avaliação do modelo LLaMA.

### 11. O Recursive Splitter apresentou vantagens?
Sim, o **Teste 9** (309 chunks) foi um dos mais equilibrados.
Ao tentar quebrar o texto por parágrafos duplos e, como *fallback*, quebras simples (`\n`), ele evitou fatiar as densas tabelas de *benchmark* e as listas de referências ao meio, garantindo blocos que ficam dentro do limite do tokenizador.

### 12. O Markdown Splitter conseguiu preservar a estrutura semântica?
Sim. Foi muito eficaz para capturar seções técnicas como `# 4 Instruction Finetuning` e `# 5 Bias, Toxicity and Misinformation`, injetando automaticamente no campo `"metadata"` do JSON de cada *chunk* o título a que aquele trecho de texto se refere.

### 13. Qual estratégia parece mais adequada para um sistema de RAG?
O **Teste 9** (Recursive Splitter) e o **Teste 10** (Markdown Splitter).
Para um sistema responder corretamente "qual é a performance do LLaMA-13B no benchmark HumanEval?", ele precisa das tabelas intactas e da compreensão da seção técnica (metadados), abordagens fornecidas apenas por esses dois testes.

### 14. Quais estratégias devem ser descartadas?
* **Teste 1 (Fixo 200):** Tamanho inútil que gera lixo vetorial, quebrando explicações ao meio.
* **Teste 2 (Fixo 500 sem overlap):** Risco de perder o contexto de uma pontuação na transição entre blocos.
* **Teste 4 (Fixo 2000):** Estourou o tamanho máximo do modelo (gerando o aviso de erro `533 > 512 tokens` na geração dos embeddings). Chunks gigantes resultam em truncamento de informações e perda de dados valiosos na hora de indexar.

### 15. Quais estratégias você acha que devem ser utilizadas nos próximos experimentos?
O **Recursive Character Splitter (Teste 9)** e o **Markdown Header Splitter (Teste 10)**. A união de ambos (fatiar o conteúdo de cada subseção com o limite de tokens recursivo) representaria o melhor dos mundos para indexar *papers* contendo dezenas de tabelas e métricas.