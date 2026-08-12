1. Qual estratégia gerou mais chunks?
O Teste 1 (Corte Fixo em 200 caracteres).
Como o tamanho definido foi muito pequeno (apenas 200 letras por bloco), o programa precisou picotar o artigo em uma quantidade enorme de pedacinhos.

2. Qual gerou menos chunks?
O Teste 4 (Corte Fixo de 2000 caracteres) e o Teste 10 (Markdown Splitter).
O Teste 4 exigia blocos gigantescos para poder cortar. Já o Teste 10 só cortava quando encontrava um título principal (como ## Introdução ou ## Discussão), então juntou páginas inteiras de texto em poucos blocos.  

3. Como o tamanho dos chunks variou?
Nos Testes 1 a 6, o tamanho foi rígido e cego definido por números de caracteres como 200, 500, 1000. Nos Testes 7 a 10, o tamanho variou sozinho de forma dinâmica, adaptando-se ao tamanho real das frases, parágrafos e seções.

4. Qual estratégia preservou melhor a estrutura dos documentos?
O Teste 10 (Markdown Splitter) e o Teste 9 (Recursive Splitter).
O Teste 10 manteve os trechos ligados aos seus títulos originais (ex: guardou que o trecho sobre "LGPD" estava dentro da seção de "Confidencialidade"). O Teste 9 garantiu que parágrafos e frases não fossem quebrados no meio.  

5. Como tabelas foram tratadas?
Nos testes por Caracteres Fixos (1, 2, 5), a estrutura foi rasgada, cortando linhas de tabelas pela metade.Nos Testes Estruturados (7, 9 e 10), caso houvesse tabelas em Markdown (| Coluna A | Coluna B |), elas seriam mantidas inteiras dentro de um único bloco, preservando a leitura da IA.

6. Como imagens foram tratadas?
Arquivos em Markdown guardam apenas texto puro, sem salvar fotos reais. O artigo possui uma indicação visual de imagem na primeira página. Na conversão para Markdown, a foto em si é ignorada ou vira apenas um texto explicativo/legenda. Se a imagem não tiver texto ou legenda no PDF, ela é descartada. 

 7. Quais informações foram perdidas durante a conversão PDF → Markdown?
 A diagramação visual original. Perdeu-se o alinhamento de duas colunas, cores de fundo, o formato exato dos cabeçalhos das folhas, o número da página no rodapé e o estilo visual do artigo. Todo o conteúdo em texto bruto foi mantido. 
 
  8. O chunking por caracteres fragmentou conceitos ou estruturas importantes?
  Sim, e muito especialmente nos estes 1 e 2.
  O programa contava letras sem ler o sentido. Com isso, ele cortou palavras no meio (ex: separando "bioé-" de "tica") e separou Leis importantes (como citar a "Lei 13.709/2018" em um bloco e o nome "LGPD" no bloco seguinte), estragando o sentido do texto. 
  
   9. O chunking por parágrafo produziu chunks muito grandes?
   Não. Neste artigo de bioética, os parágrafos têm um tamanho médio ideal para leitura (entre 300 e 600 caracteres). Não gerou blocos gigantescos e perigosos. 
   
   10. O chunking por sentença conseguiu preservar melhor o contexto?
   Sim, no teste 8 ao juntar as frases de 3 em 3 , nenhuma oração foi cortada no meio. A única falha é que essa estratégia não percebe quando um assunto acaba e outro começa, misturando às vezes o final de uma seção com o início de outra.  
   
   11. O Recursive Splitter apresentou vantagens?
   Sim, foi a estratégia mais inteligente.
   Ele tenta primeiro cortar por parágrafos completos (\n\n). Se o parágrafo for grande demais, ele tenta cortar por linhas, depois por frases e só em último caso por letras. Isso evita quebras feias e mantém tudo organizado.  
   
   12. O Markdown Splitter conseguiu preservar a estrutura semântica?
   Sim, perfeitamente. Ele usou os títulos do artigo (como ## Autonomia e opacidade algorítmica ou ## Beneficência e risco de viés algorítmico) para separar os blocos e salvou o nome desses títulos dentro do campo "metadata" do nosso arquivo JSON.  
   
   13. Qual estratégia parece mais adequada para um sistema de RAG?
   O Teste 9 (Recursive Splitter) e o Teste 10 (Markdown Splitter).
   Eles entregam blocos de texto com começo, meio e fim, sem cortar frases ao meio e mantendo o contexto ideal para o modelo de embeddings transformar em vetores e a IA responder com precisão.
   
   14. Quais estratégias devem ser descartadas?
   Teste 1 (Fixo 200): Bloco pequeno demais que esmaga o texto e corta palavras no meio.
   Teste 2 (Fixo 500 sem overlap): Risco alto de cortar um conceito no meio na transição de um bloco para o outro.
   Teste 4 (Fixo 2000): Bloco grande demais que mistura assuntos diferentes (ex: junta LGPD, Hipócrates e viés algorítmico no mesmo lugar), confundindo a busca da IA.  
   
   15. Quais estratégias você acha que devem ser utilizadas nos próximos experimentos?
   O Recursive Splitter (Teste 9) e o Markdown Header Splitter (Teste 10).