# Análise Comparativa dos 10 Experimentos de Chunking (Documento 04)

### 1. Qual estratégia gerou mais chunks?
O **Teste 1** (Corte Fixo em 200 caracteres), gerando **245 chunks**.
Por aplicar uma janela mecânica e muito pequena de 200 caracteres sobre o artigo de 48.957 caracteres, ele fatiou o texto de forma cega, picotando termos técnicos, nomes de autores e fórmulas ao meio.

### 2. Qual gerou menos chunks?
O **Teste 4** (Corte Fixo de 2000 caracteres), com **25 chunks**, e o **Teste 10** (Markdown Header Splitter), com **27 chunks**.
O Teste 4 necessitou de grandes blocos de texto para atingir a meta de corte. O Teste 10 realizou as divisões apenas ao encontrar os títulos e subtítulos do artigo (como `## 3 Model Architecture` ou `## 3.2 Attention`), agrupando seções completas em poucos blocos.

### 3. Como o tamanho dos chunks variou?
Nos **Testes 1 a 6**, o tamanho dos blocos variou de forma estrita dentro dos limites pré-fixados de caracteres (200, 500, 1000, 2000) e seus respectivos overlaps (50 e 200). Nos **Testes 7 a 10**, a variação foi dinâmica e orgânica, acompanhando a extensão real dos parágrafos, agrupamentos de 3 sentenças e seções estruturais do artigo científico.

### 4. Qual estratégia preservou melhor a estrutura dos documentos?
O **Teste 10** (Markdown Splitter) e o **Teste 9** (Recursive Splitter).
O Teste 10 mapeou a hierarquia do artigo diretamente nos metadados de cada chunk (identificando trechos como pertencentes à subseção `3.2.1 Scaled Dot-Product Attention` ou `3.2.2 Multi-Head Attention`). O Teste 9 garantiu que as explicações teóricas e fórmulas fossem divididas respeitando quebras de parágrafo e pontuação humana.

### 5. Como tabelas foram tratadas?
O artigo possui tabelas fundamentais (como a Tabela 1 com a complexidade de camadas, Tabela 2 com pontuações BLEU e Tabela 3 com variações do modelo):
* Nos **Testes por Caracteres Fixos (1, 2 e 5)**, as linhas das tabelas em Markdown foram rasgadas no meio das colunas e valores numéricos, destruindo a estrutura relacional dos dados.
* Nos **Testes Estruturados (7, 9 e 10)**, as tabelas foram mantidas em blocos integrados, preservando a coerência para busca vetorial.

### 6. Como imagens foram tratadas?
Os diagramas do artigo (como o clássico esquema da Arquitetura do Transformer na Figura 1, os mecanismos de atenção na Figura 2 e os mapas de atenção das Figuras 3 a 5) foram descartados na conversão do PDF para Markdown e substituídos pela marcação indicativa em texto `<!-- image -->`.

### 7. Quais informações foram perdidas durante a conversão PDF → Markdown?
Perdeu-se o projeto gráfico do artigo em duas colunas, a formatação visual de algumas equações matemáticas complexas (que foram marcadas no texto como `<!-- formula-not-decoded -->`), os gráficos de atenção e a diagramação das notas de rodapé. O texto corrido, referências bibliográficas e títulos das seções foram 100% preservados.

### 8. O chunking por caracteres fragmentou conceitos ou estruturas importantes?
Sim, de forma crítica nos **Testes 1 e 2**.
Conceitos fundamentais da arquitetura do modelo foram fatiados ao meio (como cortar termos como `Multi-Head Attention`, `Scaled Dot-Product`, hiperparâmetros como `d_model = 512`, nomes de autores e números das referências), o que prejudica diretamente a recuperação semântica em um sistema de RAG.

### 9. O chunking por parágrafo produziu chunks muito grande?
Sim, em pontos específicos. No **Teste 7**, parágrafos explicativos muito longos e a seção final de referências bibliográficas geraram blocos desproporcionais, chegando a ultrapassar 3.000 e 9.000 caracteres em casos isolados.

### 10. O chunking por sentença conseguiu preservar melhor o contexto?
Sim. No **Teste 8** (130 chunks), o agrupamento de 3 em 3 sentenças impediu que orações teóricas fossem cortadas no meio. A limitação é que o agrupamento mecânico de 3 frases pode unir a frase final da introdução com a primeira frase do background sem reconhecer a mudança de capítulo.

### 11. O Recursive Splitter apresentou vantagens?
Sim, demonstrou ser uma das estratégias mais seguras e consistentes.
Ao priorizar quebras por parágrafos (`\n\n`) e depois por linhas (`\n`) e espaços, ele manteve os blocos controlados em ~500 caracteres com 50 de overlap sem fragmentar palavras ou equações.

### 12. O Markdown Splitter conseguiu preservar a estrutura semântica?
Sim. Ele identificou com precisão os cabeçalhos (`#`, `##`) do artigo original e preencheu o campo `"metadata"` do JSON com os títulos exatos das seções do Transformer.

### 13. Qual estratégia parece mais adequada para um sistema de RAG?
O **Teste 9** (Recursive Splitter) e o **Teste 10** (Markdown Splitter).
Ambos mantêm a coesão conceitual do artigo técnico e garantem a qualidade do vetor de embedding para buscas precisas.

### 14. Quais estratégias devem ser descartadas?
* **Teste 1 (Fixo 200):** Fragmentação excessiva e corte de termos técnicos essenciais.
* **Teste 2 (Fixo 500 sem overlap):** Risco de quebra de conceitos nas bordas do bloco.
* **Teste 4 (Fixo 2000):** Blocos gigantescos que estouraram o limite do modelo de embedding (alerta `527 > 512` no terminal) e misturam múltiplos tópicos no mesmo vetor.

### 15. Quais estratégias você acha que devem ser utilizadas nos próximos experimentos?
O **Recursive Character Splitter (Teste 9)** e o **Markdown Header Splitter (Teste 10)**, idealmente utilizando uma abordagem combinada que extrai as seções via Markdown e limita o tamanho máximo dos blocos via Recursive Splitter.