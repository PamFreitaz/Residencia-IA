Estratégia de divisão de documentos

Qual estratégia de splitting você utilizaria?

Utilizaria o RecursiveCharacterTextSplitter (divisor de texto recursivo), pois ele é ideal para documentos técnicos estruturados, tentando primeiro quebrar nos limites de parágrafos, depois em frases e, por fim, em caracteres, preservando ao máximo a integridade semântica das explicações.

Qual tamanho aproximado dos chunks?

Um tamanho aproximado de 500 a 800 caracteres por chunk. Esse tamanho garante que haja contexto suficiente para explicar um parâmetro técnico ou passo de manutenção sem ser tão longo a ponto de misturar tópicos diferentes.

Utilizaria overlap? Quanto?

Sim. Utilizaríamos um overlap (sobreposição) de aproximadamente 100 caracteres. Isso é vital em manuais técnicos para evitar que uma instrução de configuração de perfil ICC ou um passo de código de erro seja cortado bruscamente na transição entre um chunk e o seguinte.

A divisão seria por caracteres, palavras, sentenças, parágrafos ou seções?

Uma abordagem hierárquica mista: priorizamos a divisão baseada em seções lógicas e parágrafos do manual, utilizando contagem de caracteres como limite máximo de corte do splitter recursivo.

Utilizaria um splitter recursivo?

Sim. O RecursiveCharacterTextSplitter é indispensável aqui porque ele respeita os separadores naturais do texto (como quebras de linha duplas de parágrafos \n\n e simples \n), evitando fatiar termos técnicos ou frases no meio.

Utilizaria uma estratégia específica para cada tipo de documento? Um contrato e uma transcrição de call center pedem o mesmo tratamento?

Não, os tratamentos são totalmente diferentes. Um contrato exige divisões baseadas em cláusulas e artigos legais, enquanto uma transcrição de call center pede divisões baseadas em turnos de fala. No nosso cenário de laboratório, manuais densos de equipamentos exigem um splitter sensível a títulos e blocos de instruções passo a passo, enquanto planilhas de conversão exigem tratamento tabular isolado para não corromper os dados.


****************************************************************************************************

Respostas às questões analíticas:


O que pode acontecer se os chunks forem muito pequenos?

O contexto fica fragmentado. Se o chunk tiver apenas uma frase solta (ex: "Ajuste o valor para"), a IA perde o restante da instrução técnica e não consegue responder com precisão qual valor deve ser inserido no software de impressão.

O que pode acontecer se os chunks forem muito grandes?

O modelo de embeddings perde a especificidade do trecho, e o modelo gerador (LLM) pode se perder em meio a excesso de informações irrelevantes na mesma janela de contexto, além de aumentar o risco de alucinação.

Como você trataria uma tabela na hora de dividir? Uma tabela cortada ao meio ainda significa alguma coisa? E uma imagem?

Tabelas: Tabelas nunca devem ser cortadas ao meio por um splitter de texto comum. Elas devem ser tratadas como blocos atômicos (mantidas inteiras dentro de um único chunk ou convertidas para estruturas markdown completas) para que a relação entre cabeçalhos e colunas numéricas não seja destruída. Uma tabela cortada perde totalmente o sentido e gera dados errados.

Imagens: Diagramas técnicos e gráficos de fluxo não passam pelo splitter de texto comum; eles são processados previamente por modelos de visão para gerar um texto descritivo (captioning), e esse texto descritivo é que é indexado como um chunk de texto comum.

Como saber se a sua escolha de chunking foi boa? Que evidência você juntaria para provar isso?

Evidências de qualidade:

Testes de recuperação (Hit Rate): Fazer um conjunto de perguntas reais de teste (como as nossas perguntas sobre perfil ICC e Delta E) e medir se os chunks retornados contêm exatamente a resposta esperada sem cortes.

Inspeção visual dos chunks gerados: Verificar se os passos de manutenção e as tabelas de conversão permaneceram íntegros dentro dos blocos salvos no banco vetorial.