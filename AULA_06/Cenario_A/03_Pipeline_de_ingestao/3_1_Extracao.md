**Extração**

Como o texto seria extraído?

A extração seria feita utilizando bibliotecas especializadas do Python (como PyPDFDirectoryLoader ou Unstructured) combinadas com parsers voltados a documentos técnicos e manuais de equipamentos.

Como você trataria PDFs com texto selecionável?

Utilizaria leitores diretos de fluxo de texto (PyPDF ou PDFMiner) para extrair as strings limpas dos manuais de plotters e fichas de especificação de papéis, preservando a ordem natural de leitura dos parágrafos.

E PDFs digitalizados (imagem escaneada, sem camada de texto)?

Para manuais antigos ou documentos físicos escaneados de impressoras descontinuadas, aplicaríamos uma ferramenta de OCR integrada (como Tesseract OCR ou processamento via modelos multimodais de visão) para varrer as páginas em formato de imagem e converter o conteúdo visual em texto legível antes de prosseguir no pipeline.

Como trataria tabelas? (É importante manter?)

Sim, é extremamente importante manter! Nesse cenário, as tabelas contêm dados vitais de conversão (como perfis de cores, gramaturas, tamanhos de mídias e tabelas de compatibilidade de tintas). Elas seriam extraídas preservando a estrutura original (convertidas para formato Markdown estruturado com linhas e colunas) para que o modelo não perca a relação numérica entre os dados.

Como trataria imagens? (Posso descartar? Quais informações elas têm?)

Não podemos descartar todas. Os diagramas de fluxo de manutenção de cabeçotes de impressora ou gráficos de espaço de cor contêm informações cruciais. Nesses casos, utilizaríamos um modelo de visão computacional (como o GPT-4o ou LLMs multimodais leves) para gerar uma descrição textual detalhada (captioning) da imagem, transformando o conteúdo visual em texto explicativo para ser indexado.

Como trataria documentos multimodais?

Documentos que misturam texto e esquemas gráficos de montagem seriam processados dividindo os blocos: o texto corrido seria extraído diretamente por parsing e os diagramas visuais passariam por uma etapa de descrição por IA, unindo ambos em um mesmo documento estruturado.

Explique quais problemas podem surgir durante a extração:

1. Quebra de layout e tabelas corrompidas: Manuais técnicos de equipamentos costumam ter colunas duplas e tabelas densas; se a extração for linear, os dados de uma coluna podem se misturar com a outra, gerando frases sem sentido.

2. Caracteres especiais e símbolos de unidades danificados: Símbolos técnicos (como %, µm para mícrons de espessura de papel, ou DPI) podem vir corrompidos em codificações de PDF antigas.

3. Ruído de OCR: Erros de leitura em letras parecidas (como ler o número 0 como a letra O em códigos de erro de impressoras).