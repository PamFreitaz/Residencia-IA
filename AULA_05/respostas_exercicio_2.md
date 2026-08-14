## Respostas do Exercício 2 

**1. Qual campo você incluiria se precisasse citar a fonte na resposta final do RAG, informando ao usuário exatamente de onde veio a informação?**
* O campo **`fonte`** (junto com o campo de página ou `documento_id`), pois ele armazena o nome exato do arquivo `.md` de onde o texto foi extraído, permitindo que a inteligência artificial informe a referência correta ao usuário.

**2. Por que chunk_index é útil? Pense no caso em que o trecho recuperado está cortado no meio de uma explicação.**
* O **`chunk_index`** é útil porque indica a posição exata daquele pedaço dentro do documento original. Se o texto recuperado estiver cortado no meio de uma frase ou explicação, saber o índice permite buscar programaticamente o chunk seguinte (por exemplo, `chunk_index + 1`) para garantir a leitura completa do contexto sem perder a continuação.