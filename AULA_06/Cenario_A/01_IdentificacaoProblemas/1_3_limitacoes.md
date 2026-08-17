**1.3 Limitações — quando RAG não é a resposta**

Em quais situações RAG não seria a melhor solução?

1. Consulta de estoque em tempo real: Saber quantas folhas de papel Fine Art restam no estoque físico (melhor resolvido por um banco de dados relacional e SQL).

2. Regras determinísticas de tamanho: Impedir o upload de arquivos abaixo de 300 DPI (melhor resolvido por código de validação determinístico/regras fixas).

3. Monitoramento de status de hardware: Saber se a impressora da ponta da sala está ligada ou com erro físico de conexão (melhor resolvido por integração via API/IoT com o equipamento).

****************************************************************************************************

*Existe alguma pergunta, dentro do seu próprio cenário, que RAG responderia mal e um banco de dados relacional responderia bem?*

Sim.

*Qual, e por quê?*

Pergunta:
    "Quantos metros quadrados de papel fosco 240g nós utilizamos no mês passado para atender aos pedidos dos fotógrafos parceiros?"

Por quê?
    Porque isso exige agregação numérica, soma exata e cruzamento de dados de pedidos transacionais, algo que um banco de dados relacional faz com facilidade via SQL, enquanto o RAG encontraria apenas trechos soltos de texto em relatórios antigos.

*O que aconteceria se a pergunta do usuário exigisse contar, somar ou ordenar informação espalhada por muitos documentos?*

O sistema RAG tradicional cortaria os documentos em vários chunks (pedaços) e poderia perder a visão global, trazendo apenas fragmentos parciais e falhando em fornecer uma contagem ou ordenação precisa, a menos que estivesse integrado a ferramentas de execução de código (como agentes estruturados).