**Frequência de ingestão**


O pipeline roda uma vez, sob demanda, ou de forma agendada?

O pipeline opera de forma agendada semanalmente (para capturar automaticamente atualizações nas páginas HTML de FAQ e novas políticas do e-commerce) e também sob demanda (sempre que o setor de marketing ou comercial lança uma nova campanha promocional ou altera regras de frete e prazos).

Com que frequência chegam novos documentos?

Alta frequência: Novos documentos e atualizações de páginas ocorrem com bastante regularidade (semanalmente ou quinzenalmente), impulsionados por safras de campanhas sazonais (como Dia das Mães, Dia dos Namorados, Black Friday), novos produtos de decoração adicionados ao catálogo ou ajustes nas regras logísticas.

Quando um documento é atualizado, você reprocessa só ele ou a base inteira? Como sabe qual reprocessar?

Reprocessamos apenas o documento ou página alterada (e não a base inteira), otimizando o custo e o tempo de processamento.

Como sabemos qual reprocessar? Através de identificadores únicos (document_id) combinados com uma verificação de hash de conteúdo ou a data de atualização (updated_at) extraída das páginas web e arquivos de políticas. Quando o sistema detecta que o hash ou a data de uma página de FAQ mudou em relação à versão armazenada no banco vetorial, ele limpa automaticamente os chunks antigos daquele ID específico e executa o pipeline de ingestão apenas para o conteúdo atualizado.