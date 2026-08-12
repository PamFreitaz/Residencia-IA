# Análise Comparativa dos 10 Experimentos de Chunking (Documento 02)

### 1. Qual estratégia gerou mais chunks?
O **Teste 1** (Corte Fixo em 200 caracteres).
Por utilizar uma janela extremamente reduzida (200 caracteres), o programa fatiou o artigo sobre Escrita Acadêmica em uma grande quantidade de pequenos blocos, picotando frases e conceitos ao meio.

### 2. Qual gerou menos chunks?
O **Teste 4** (Corte Fixo de 2000 caracteres) e o **Teste 10** (Markdown Header Splitter).
O Teste 4 exigia blocos extensos para realizar o corte. Já o Teste 10 realizou a divisão apenas ao encontrar os cabeçalhos das seções (como `## I. Introdução` ou `## II.1. Fase 1: planejamento humano`), agrupando seções inteiras em poucos blocos.

### 3. Como o tamanho dos chunks variou?
Nos **Testes 1 a 6**, a variação seguiu limites rígidos definidos em caracteres (200, 500, 1000, 2000) e overlaps fixos (50 e 200). Nos **Testes 7 a 10**, o tamanho variou de forma dinâmica e flexível, adaptando-se às quebras naturais do texto, como parágrafos, agrupamentos de sentenças e seções do documento.

### 4. Qual estratégia preservou melhor a estrutura dos documentos?
O **Teste 10** (Markdown Splitter) e o **Teste 9** (Recursive Splitter).
O Teste 10 manteve a hierarquia do texto ligada aos metadados (ex: identificando que as orientações de prompts pertenciam à `Fase 1` ou `Fase 2`). O Teste 9 garantiu que parágrafos e frases da discussão fossem mantidos sem cortes abruptos.

### 5. Como tabelas foram tratadas?
O artigo possui o **Quadro 1** (Etapas para uso ético, responsável e humano da IA). Nos **Testes por Caracteres Fixos (1, 2 e 5)**, as linhas da tabela em Markdown (`| Fase | Foco | Objetivo |`) foram rasgadas no meio das colunas. Nos **Testes Estruturados (7, 9 e 10)**, a estrutura de tabela foi preservada intacta dentro de blocos coesos, mantendo a legibilidade para o modelo vetorial.

### 6. Como imagens foram tratadas?
O artigo continha elementos visuais e badges de identificação (como o ícone de e-mail do autor e selos da revista). Na conversão para Markdown, as imagens físicas foram descartadas e substituídas por tags de texto indicativas (ex: `<!-- image -->`). Apenas o conteúdo em texto puro do artigo foi mantido.

### 7. Quais informações foram perdidas durante a conversão PDF → Markdown?
Perdeu-se a formatação e a diagramação estética do PDF original: o layout de duas colunas, o estilo visual dos cabeçalhos e rodapés da *Revista de Sociologia e Política*, numeração gráfica de páginas e elementos decorativos. A integridade do texto acadêmico foi 100% preservada.

### 8. O chunking por caracteres fragmentou conceitos ou estruturas importantes?
Sim, severamente nos **Testes 1 e 2**.
Por contar apenas letras sem considerar o significado, o algoritmo cortou termos acadêmicos essenciais ao meio e separou citações bibliográficas (como citar `(Sampaio et al., 2024)` em um bloco e o conceito de `descarregamento cognitivo` no bloco seguinte), prejudicando a recuperação semântica.

### 9. O chunking por parágrafo produziu chunks muito grandes?
Não. Neste artigo, os parágrafos explicativos das 5 Fases metodológicas possuem um tamanho médio ideal para leitura (entre 400 e 900 caracteres), resultando em unidades de contexto bem delimitadas.

### 10. O chunking por sentença conseguiu preservar melhor o contexto?
Sim. No **Teste 8**, ao agrupar as frases de 3 em 3, nenhuma oração foi cortada no meio. A principal limitação é que o agrupamento fixo de 3 frases não reconhece a mudança de assunto, podendo fundir o final da explicação de uma fase com o início da fase seguinte.

### 11. O Recursive Splitter apresentou vantagens?
Sim, demonstrou ser a estratégia mais equilibrada.
Ele busca realizar as quebras respeitando primeiro os parágrafos (`\n\n`), depois as linhas (`\n`), frases e palavras. Isso garantiu que as recomendações do guia fossem mantidas organizadas, sem estourar o limite de 500 caracteres.

### 12. O Markdown Splitter conseguiu preservar a estrutura semântica?
Sim, com alta precisão. O splitter utilizou as marcações do artigo (como `## II.1. Fase 1: planejamento humano` e `## II.2. Fase 2: geração de insumos`) para criar os blocos e associou esses títulos automaticamente no campo `"metadata"` de cada registro JSON.

### 13. Qual estratégia parece mais adequada para um sistema de RAG?
O **Teste 9** (Recursive Splitter) e o **Teste 10** (Markdown Splitter).
Eles fornecem fragmentos contextualizados com início, meio e fim, sem interromper argumentos científicos e garantindo excelente qualidade nos vetores de busca (*embeddings*).

### 14. Quais estratégias devem ser descartadas?
* **Teste 1 (Fixo 200):** Fragmenta excessivamente o texto e corta palavras.
* **Teste 2 (Fixo 500 sem overlap):** Apresenta alto risco de quebrar citações e conceitos na borda do bloco.
* **Teste 4 (Fixo 2000):** Bloco excessivamente grande que mistura múltiplos conceitos e fases no mesmo vetor, prejudicando a precisão da busca RAG.

### 15. Quais estratégias você acha que devem ser utilizadas nos próximos experimentos?
O **Recursive Character Splitter (Teste 9)** e o **Markdown Header Splitter (Teste 10)**, ou uma abordagem combinada entre ambas.