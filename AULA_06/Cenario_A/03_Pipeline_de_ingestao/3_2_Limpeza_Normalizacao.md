**Limpeza e normalização**

O que precisa ser removido?

Cabeçalhos e rodapés repetidos: Como manuais técnicos de plotters e fichas de papéis costumam repetir o nome do modelo da impressora e o logotipo da fabricante no topo ou rodapé de todas as páginas, isso deve ser removido para não poluir os chunks com repetições inúteis.

Numeração de página e marcas d'água: Números de páginas isolados e textos de fundo (como "Confidencial" ou "Uso Interno") que aparecem cortados no meio do texto.

Sumários e índices remotos: Listas de capítulos iniciais que contêm apenas sumários de páginas, pois não trazem o conteúdo técnico explicativo em si e podem confundir a busca semântica.

O que precisa ser padronizado?

Codificação de caracteres: Garantir que o texto esteja em padrão UTF-8 puro para evitar que símbolos técnicos cruciais (como unidades de medida, porcentagens ou diâmetros) fiquem corrompidos.

Quebras de linha e espaçamentos: Remover quebras de linha artificiais causadas pelo formato do PDF que cortam frases no meio da linha (por exemplo, transformar frases quebradas em parágrafos contínuos e limpos).

Terminologias técnicas e acentuação: Padronizar termos de colorimetria e unidades (ex: padronizar menções a DPI, ICC e gramaturas para que não fiquem com variações de maiúsculas/minúsculas ou erros de acentuação).

Que informação você corre o risco de perder ao limpar demais?

Notas de rodapé técnicas importantes: Às vezes, o rodapé de um manual técnico contém um aviso crítico de segurança (ex: "Atenção: o uso de tinta paralela invalida imediatamente a garantia do cabeçote"). Se o filtro de limpeza eliminar tudo o que está no rodapé de forma automatizada, podemos perder essa restrição vital.

Contextos de referências cruzadas: Remover referências numéricas a outras seções do manual (ex: "consulte a Seção 4.2") pode fazer com que o chunk perca o encadeamento lógico de instruções de manutenção.