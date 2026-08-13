# Análise Comparativa dos 10 Experimentos de Chunking (Documento 07)

### 1. Qual estratégia gerou mais chunks?
O **Teste 1** (Corte Fixo em 200 caracteres), gerando **1.440 chunks**.
Por ser um documento extenso e complexo contendo o relatório técnico do GPT-4 e o seu System Card, o limite muito apertado de 200 caracteres fragmentou o texto em um número excessivo de pedaços.

### 2. Qual gerou menos chunks?
O **Teste 4** (Corte Fixo de 2000 caracteres), com **145 chunks**, e o **Teste 10** (Markdown Header Splitter), com **195 chunks**.
O Teste 4 necessitou acumular um volume gigante de caracteres para fazer os cortes. Já o Teste 10 agrupou seções inteiras do artigo e do System Card (como `## 4 Capabilities` ou `## 2.2 Hallucinations`) em blocos únicos delimitados pelos cabeçalhos.

### 3. Como o tamanho dos chunks variou?
Nos **Testes 1 a 6**, o tamanho variou estritamente dentro dos limites fixos de caracteres definidos (200, 500, 1000, 2000) com seus overlaps exatos. Nos **Testes 7 a 10**, a variação acompanhou a estrutura natural do relatório técnico, baseando-se em parágrafos, agrupamentos de frases, tabelas de métricas e títulos das seções.

### 4. Qual estratégia preservou melhor a estrutura dos documentos?
O **Teste 10** (Markdown Splitter) e o **Teste 9** (Recursive Splitter).
O Teste 10 foi particularmente brilhante neste artigo por conseguir separar o relatório de pesquisa original do "System Card" (relatório de segurança) presente no final do arquivo, mantendo essa diferenciação no metadado. O Teste 9 garantiu que parágrafos discutindo métricas de segurança não fossem cortados.

### 5. Como tabelas foram tratadas?
O artigo possui tabelas densas, como a **Tabela 1** (desempenho do GPT-4 em exames como Bar Exam e LSAT) e as tabelas com exemplos reais de *prompts* ofensivos/perigosos testados pelo Red Team.
* Nos **Testes por Caracteres Fixos (1, 2 e 5)**, a formatação em Markdown dessas tabelas foi rasgada ao meio, misturando a pontuação do modelo com outras disciplinas.
* Nos **Testes Estruturados (7, 9 e 10)**, as tabelas permaneceram unidas, o que é vital para buscar e recuperar corretamente a precisão do GPT-4 em testes específicos.

### 6. Como imagens foram tratadas?
Os diversos gráficos do relatório (como as curvas de calibração, projeções de Scaling Laws e gráficos de barra de toxicidade) foram descartados na conversão do PDF para Markdown, sendo representados no texto apenas pela tag indicativa `<!-- image -->`.

### 7. Quais informações foram perdidas durante a conversão PDF → Markdown?
A formatação do layout tradicional de artigos científicos, a diagramação de caixas de texto que ilustravam os exemplos de interações (*Prompts* vs *Completions* na seção de Safety), marcações de notas de rodapé e a renderização gráfica das equações de predição de perda (*Loss Prediction*). Todo o conteúdo textual crítico, porém, foi salvo.

### 8. O chunking por caracteres fragmentou conceitos ou estruturas importantes?
Sim, drasticamente nos **Testes 1 e 2**.
Termos fundamentais como `Reinforcement Learning from Human Feedback (RLHF)`, `Rule-based reward models (RBRMs)`, métricas de segurança e os nomes contidos na gigante lista de autores e contribuidores do relatório foram fatiados sem sentido, prejudicando a indexação do RAG.

### 9. O chunking por parágrafo produziu chunks muito grandes?
Sim. No **Teste 7** (1.036 chunks), blocos enormes foram formados nas seções de Referências Bibliográficas (que chegam a mais de 100 itens) e nas extensas listas de colaboradores agrupados por times, onde não existem quebras convencionais de parágrafo (`\n\n`) para interromper o corte.

### 10. O chunking por sentença conseguiu preservar melhor o contexto?
Mais ou menos. O **Teste 8** (956 chunks) ajudou na leitura das explicações contínuas, como as discussões sociológicas no System Card. Porém, ao agrupar 3 sentenças de forma rígida em tabelas de dados brutos ou listas de referência, ele uniu partes que não tinham correlação narrativa lógica.

### 11. O Recursive Splitter apresentou vantagens?
Sim, foi excelente.
O **Teste 9** (846 chunks) conseguiu lidar com as longas listas de autores e referências porque, ao não achar duplo espaço (`\n\n`), desceu para quebrar nas quebras simples de linha (`\n`), mantendo os blocos num tamanho ideal para o modelo vetorial sem destruir o texto.

### 12. O Markdown Splitter conseguiu preservar a estrutura semântica?
Sim. Ele identificou a hierarquia do documento, capturando os capítulos principais do modelo (`# 3 Predictable Scaling`, `# 4 Capabilities`) e as seções de segurança do System Card (`## 2.8 Cybersecurity`, `## 2.2 Hallucinations`), associando o texto aos títulos através do campo `"metadata"`.

### 13. Qual estratégia parece mais adequada para um sistema de RAG?
O **Teste 9** (Recursive Splitter) e o **Teste 10** (Markdown Splitter).
Ambos mantêm a consistência das informações técnicas, das tabelas de *benchmarks* e das amostras de testes do *Red Team*, garantindo que buscas vetoriais no documento do GPT-4 tragam contexto útil.

### 14. Quais estratégias devem ser descartadas?
* **Teste 1 (Fixo 200):** Excesso de fragmentos, fatiando números e conceitos no meio.
* **Teste 2 (Fixo 500 sem overlap):** Possibilidade de perder partes cruciais de um *prompt* de exemplo bem na margem do bloco.
* **Teste 4 (Fixo 2000):** Exigiu blocos gigantes que geraram **erro no terminal** por estourar o limite de tokens do tokenizador (*523 > 512 tokens*), inviabilizando que o embedding seja processado corretamente sem truncar dados.

### 15. Quais estratégias você acha que devem ser utilizadas nos próximos experimentos?
O **Recursive Character Splitter (Teste 9)** e o **Markdown Header Splitter (Teste 10)**. O ideal é combiná-los para dividir o relatório semântico em tópicos (Header) e evitar que blocos da lista de referências passem de 500 caracteres (Recursive).