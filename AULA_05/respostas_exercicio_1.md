1. Que tipos de dado são aceitos dentro de metadata? Teste colocar uma lista ou um dicionário aninhado e relate o que acontece.

* **O `metadata` aceita textos, números, listas e até dicionários dentro de outros dicionários (dicionários aninhados).** 

* **Quando a gente testa colocar uma lista ou um dicionário aninhado, o Python e o LangChain aceitam tudo normalmente e o código roda sem dar nenhum erro.** 

2. O que acontece se você criar um Document sem passar metadata?

* **O código roda perfeitamente e não dá nenhum erro.** 
* **Por padrão, o próprio LangChain cria um dicionário vazio `{}` automaticamente no lugar do `metadata` para o documento não ficar sem essa estrutura.** 