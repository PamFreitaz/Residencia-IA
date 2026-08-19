Qual estratégia de splitting você utilizaria?

Utilizaríamos o RecursiveCharacterTextSplitter (divisor de texto recursivo), pois ele é excelente para fatiar FAQs, páginas de ajuda e políticas comerciais, respeitando a estrutura natural dos parágrafos e subtópicos.

Qual tamanho aproximado dos chunks?

Um tamanho aproximado de 300 a 450 caracteres por chunk. Esse tamanho menor é ideal para e-commerce, pois garante que cada bloco contenha uma regra comercial específica, uma pergunta de FAQ e sua respectiva resposta de forma isolada e direta.

Utilizaria overlap? Quanto?

Sim. Utilizaríamos um overlap (sobreposição) curto de aproximadamente 50 caracteres. Isso garante que o contexto não seja cortado abruptamente na transição entre o final de uma regra de troca e o início de outra.

A divisão seria por caracteres, palavras, sentenças, parágrafos ou seções?

Uma abordagem baseada em seções lógicas, blocos de perguntas/respostas de FAQ e parágrafos, utilizando a contagem de caracteres como limite máximo de corte do fatiador.

Utilizaria um splitter recursivo?

Sim. O RecursiveCharacterTextSplitter é fundamental porque ele tenta primeiro quebrar nos separadores mais naturais do texto (como quebras de linha duplas \n\n de parágrafos ou divisões de tópicos) antes de recorrer a cortes arbitrários de caracteres.

Utilizaria uma estratégia específica para cada tipo de documento? Um contrato e uma transcrição de call center pedem o mesmo tratamento?

Não, os tratamentos são totalmente diferentes. Documentos de FAQ e políticas de e-commerce pedem blocos curtos e focados em perguntas e respostas; já um contrato jurídico completo exige fatiamento baseado em cláusulas e artigos legais, enquanto uma transcrição de call center exigiria cortes baseados em turnos de fala entre atendente e cliente.

****************************************************************************************************

Respostas questões analíticas

O que pode acontecer se os chunks forem muito pequenos?
O contexto fica fragmentado. Se o chunk tiver apenas meia frase (ex: "O prazo para trocas é de"), a IA perde a condição ou o número de dias especificado e não consegue responder com precisão ao cliente.

O que pode acontecer se os chunks forem muito grandes?
O modelo de embeddings perde a especificidade do trecho e o LLM pode se confundir misturando regras de produtos diferentes (por exemplo, misturando as regras de reembolso de álbuns com as regras de brindes corporativos no mesmo bloco).

Como você trataria uma tabela na hora de dividir? Uma tabela cortada ao meio ainda significa alguma coisa? E uma imagem?

Tabelas: Tabelas de frete ou de gabaritos nunca devem ser cortadas ao meio por um fatiador comum. Elas devem ser mantidas inteiras (atômicas) em um único chunk estruturado em Markdown para preservar a relação exata entre colunas e linhas. Uma tabela cortada ao meio perde totalmente o sentido lógico e numérico.

Imagens: Banners ou infográficos explicativos de como medir as margens de um álbum são processados previamente por IA para gerar uma descrição textual (captioning), e é essa descrição que entra na base como texto.

Como saber se a sua escolha de chunking foi boa? Que evidência você juntaria para provar isso?

Evidências de qualidade:

Testes de recuperação de FAQ: Criar um conjunto de perguntas reais feitas por clientes (ex: "Como peço reembolso se o produto vier amassado?") e verificar se o chunk recuperado traz exatamente a resposta correta sem cortes.

Inspeção visual dos blocos: Conferir se as perguntas e respostas das FAQs permaneceram inteiras e coesas dentro de cada chunk gerado.