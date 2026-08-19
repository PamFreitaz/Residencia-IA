**1.3 Limitações — quando RAG não é a resposta**

Em quais situações RAG não seria a melhor solução?

1. Consulta de status de entrega individual: Saber exatamente onde está o pacote de um pedido específico (melhor resolvido por integração via API com a transportadora e banco relacional).

2. Alteração de dados cadastrais ou senhas: Ações transacionais na conta do usuário (melhor resolvidas por código determinístico e APIs seguras).

3. Verificação de estoque em tempo real: Saber se há unidades físicas de brindes disponíveis no armazém (banco de dados SQL).

****************************************************************************************************

Existe alguma pergunta, dentro do seu próprio cenário, que RAG responderia mal e um banco de dados relacional responderia bem? Qual, e por quê?

Pergunta: "Quantos fotolivros tamanho 20x30 foram vendidos durante a campanha de Dia das Mães do mês passado?"

Por quê? Porque isso exige agregação numérica, contagem exata e cruzamento de tabelas transacionais de vendas, algo que um banco de dados relacional faz instantaneamente via SQL, enquanto o RAG encontraria apenas menções textuais soltas sobre a campanha.

O que aconteceria se a pergunta do usuário exigisse contar, somar ou ordenar informação espalhada por muitos documentos?

O sistema RAG traria apenas trechos fragmentados de texto e falharia em realizar operações matemáticas ou de ordenação global, correndo o risco de gerar uma resposta imprecisa.