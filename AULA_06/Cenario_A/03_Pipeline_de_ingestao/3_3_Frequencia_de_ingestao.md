**Frequência de ingestão**


O pipeline roda uma vez, sob demanda, ou de forma agendada?

O pipeline opera principalmente sob demanda. Como os manuais técnicos de plotters, fichas de substratos e guias de calibração do laboratório não mudam todos os dias, a ingestão é acionada manualmente pela equipe de engenharia/gerência sempre que um novo equipamento é adquirido ou um procedimento oficial é atualizado. Opcionalmente, pode rodar de forma agendada mensalmente apenas para verificar se há novos arquivos na pasta raiz.

Com que frequência chegam novos documentos?

Média frequência: Novos documentos chegam geralmente atrelados à incorporação de novas tecnologias de impressão, novos lotes de papéis Fine Art ou revisões de normas internas de colorimetria ou um maquinário novo.

Quando um documento é atualizado, você reprocessa só ele ou a base inteira? Como sabe qual reprocessar?

Reprocessamos apenas o documento alterado (e não a base inteira), pois a base de dados do laboratório é pequena e focada.

Como sabemos qual reprocessar?
Através do controle de versão e do nome do arquivo associado aos metadados. Quando um manual (ex: manual_epson_surecolor_v2.pdf) substitui uma versão anterior (v1), o sistema identifica a mudança do arquivo na pasta de origem, remove os chunks antigos vinculados àquele ID de documento no banco vetorial e executa o pipeline de extração, limpeza e chunking apenas para o novo arquivo atualizado.