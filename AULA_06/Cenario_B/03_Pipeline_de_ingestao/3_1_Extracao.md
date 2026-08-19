**Extração**

Como o texto seria extraído?

A extração seria feita utilizando bibliotecas e parsers voltados a conteúdos web e documentos comerciais (como Unstructured, WebBaseLoader para páginas HTML de FAQ e carregadores de arquivos Markdown e PDF do Google Drive).

Como você trataria PDFs com texto selecionável?

Utilizaria leitores diretos de fluxo de texto (como PyPDF ou PDFMiner) para extrair de forma limpa as políticas de frete, termos de troca e guias de gabaritos salvos em PDF, preservando a ordem natural dos parágrafos explicativos.

E PDFs digitalizados (imagem escaneada, sem camada de texto)?

Para contratos antigos assinados ou panfletos promocionais físicos escaneados sem camada de texto, aplicaríamos uma ferramenta de OCR integrada (como Tesseract OCR ou processamento via modelos multimodais de visão) para converter o conteúdo visual da imagem em texto legível antes de prosseguir no pipeline.

Como trataria tabelas? (É importante manter?)

Sim, é extremamente importante manter! No nosso cenário de e-commerce, as tabelas contêm dados vitais de precificação, prazos de entrega por região e tabelas de medidas de gabaritos de álbuns e quadros. Elas seriam extraídas preservando a estrutura original (convertidas para formato Markdown estruturado com linhas e colunas) para que o modelo não perca a relação entre o produto e suas especificações numéricas.

Como trataria imagens? (Posso descartar? Quais informações elas têm?)

Não podemos descartar todas. Imagens de banners promocionais antigos ou diagramas visuais explicativos de como medir as margens de sangria de um fotolivro contêm informações úteis. Nesses casos, utilizaríamos um modelo de visão computacional (como LLMs multimodais leves) para gerar uma descrição textual detalhada (captioning) da imagem, transformando o conteúdo visual em texto explicativo indexável.

Como trataria documentos multimodais?

Documentos e páginas de suporte que misturam texto descritivo e infográficos visuais de instruções de montagem de álbuns seriam processados separando os blocos: o texto corrido seria extraído por parsing direto e os infográficos passariam por descrição por IA, unindo ambos em um documento estruturado unificado.

Explique quais problemas podem surgir durante a extração:

1. Poluição por elementos de interface web: Como grande parte da base vem de páginas HTML de FAQs, a extração pode capturar acidentalmente menus de navegação, rodapés institucionais, botões de "Comprar" e links corrompidos, gerando ruído textual.

2. Quebra de tabelas de preços e prazos: Tabelas complexas de frete com múltiplas colunas de CEPs e faixas de peso podem ter suas linhas desalinhadas se extraídas de forma linear, fazendo o modelo associar o valor de frete errado a uma determinada região.

3. Desatualização de formatação em PDFs antigos: Arquivos de políticas comerciais convertidos de versões legadas do Word podem apresentar falhas de codificação em caracteres especiais (como acentuação e símbolos de moeda).