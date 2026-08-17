Respostas questões analíticas

Quais metadados você usaria para filtrar a busca? Dê um exemplo de pergunta em que o filtro é indispensável:
Usaria os metadados equipment_model e document_type.

Exemplo de pergunta:
"Qual é o procedimento de limpeza de cabeçote da impressora Epson SureColor?"

Por que o filtro é indispensável? Sem filtrar por equipment_model: "Epson SureColor", o banco vetorial poderia puxar trechos de manuais de outras plotters de marcas diferentes (como Canon ou HP), misturando comandos de manutenção e gerando um erro grave de operação.

Quais metadados você usaria para citar a fonte ao usuário? O que exatamente apareceria na tela junto da resposta?
Usaria os metadados title (do documento), equipment_model e page.

O que apareceria na tela junto da resposta gerada pela IA:
apareceria um rodapé de citação estruturado exatamente assim:
Ex: Fonte: Manual de Operação - Epson SureColor (Página 5, Seção: Procedimento de Calibração).

Que metadado seria caríssimo de acrescentar depois que a base já estivesse indexada? Por quê?
O metadado equipment_model (ou qualquer classificação semântica/contextual profunda que exija categorizar o equipamento ao qual o texto se refere).

Por quê?
Porque se a base já estiver totalmente indexada sem essa etiqueta, adicionar esse campo depois exigiria reabrir todos os PDFs originais, reclassificar manualmente centenas de fragmentos de texto (ou reexecutar chamadas caras a LLMs para inferir o modelo do equipamento de cada parágrafo) e reescrever todos os vetores no banco de dados.

Como você vai extrair esses metadados?
Os metadados estruturais globais (document_id, title, source, created_at, equipment_model) serão extraídos de forma programática no momento da ingestão, mapeados diretamente do nome do arquivo, da pasta de origem ou lidos do cabeçalho do documento PDF. Já os metadados contextuais do chunk (page, section, chunk_id) serão extraídos automaticamente pelo parser do LangChain durante a quebra do texto.