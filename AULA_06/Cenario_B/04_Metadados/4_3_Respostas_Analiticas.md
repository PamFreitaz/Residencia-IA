Quais metadados você usaria para filtrar a busca? Dê um exemplo de pergunta em que o filtro é indispensável.
Usaria os metadados product_line e document_type.

Exemplo de pergunta: "Qual é a regra de margem de sangria para a confecção de quadros canvas?"

Por que o filtro é indispensável?
Sem filtrar por product_line: "quadros", a busca vetorial poderia puxar instruções de margens de álbuns ou fotolivros, que possuem tamanhos de sangria totalmente diferentes, fazendo o chat dar uma resposta errada que estragaria o produto do cliente.

Quais metadados você usaria para citar a fonte ao usuário?
O que exatamente apareceria na tela junto da resposta?
Usaria os metadados title (do documento), section e updated_at.

O que apareceria na tela: Junto da resposta gerada pela IA, apareceria um rodapé de citação estruturado assim:
"Fonte: Política de Trocas e Avarias — Seção: Avarias de Transporte (Atualizado em Fev/2026)."

Que metadado seria caríssimo de acrescentar depois que a base já estivesse indexada? Por quê?
O metadado product_line (ou qualquer classificação comercial específica de produtos).

Por quê? Porque se a base de FAQs e políticas já estivesse totalmente indexada sem essa etiqueta de qual produto o texto se refere, adicionar esse campo depois exigiria reabrir centenas de arquivos de texto, reclassificar manualmente cada regra (ou gastar tempo e dinheiro rodando chamadas de LLM para inferir o produto) e reconstruir todos os vetores no banco de dados do zero.

Como você vai extrair esses metadados?
Os metadados estruturais globais (document_id, title, source, created_at, updated_at) serão extraídos automaticamente no momento da ingestão, mapeados direto da estrutura de pastas do e-commerce (politicas/, gabaritos_produtos/) e do cabeçalho dos arquivos Markdown. Já os metadados contextuais do chunk (chunk_id, page, section, product_line) serão extraídos programaticamente pelos parsers durante o fatiamento e a leitura estruturada dos blocos.