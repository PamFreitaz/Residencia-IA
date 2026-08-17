documentos/
├── equipamentos/        # Manuais de plotters, impressoras e espectrofotômetros
├── substratos/          # Fichas técnicas de papéis (fine art, canvas, fotográfico) e tintas
├── procedimentos/       # POPs internos de colorimetria, perfis ICC e tratamento de arquivos
├── calibracao/          # Relatórios de calibração, tolerâncias de Delta E e testes de laboratório
└── outros/              # Documentações genéricas e avisos de fabricantes

****************************************************************************************************

*Justificativa da estrutura:*

Essa divisão espelha exatamente a forma como o operador técnico busca a informação no dia a dia. Quando ele quer saber sobre uma máquina, vai em equipamentos/. Se a dúvida é sobre o comportamento de um papel na hora da impressão, ele vai em substratos/. Se o problema é o fluxo de cor, ele recorre a procedimentos/ ou calibracao/. Isso facilita a aplicação de metadados e filtros direcionados no banco de dados vetorial.

****************************************************************************************************

Existe documento que não deve entrar na base? Como você impediria a entrada?

Resposta:
    Sim. Fichas de custo interno de insumos negociados com fornecedores (dados sigilosos financeiros) e versões obsoletas de manuais de máquinas antigas que já foram descartadas pelo laboratório arquivados no banco de dados.

Como impedir:
    Através de uma curadoria humana restrita no pipeline de ingestão (apenas a equipe de engenharia/gerência pode aprovar novos arquivos na pasta raiz) e o uso de regras de exclusão por metadados ou listas de bloqueio (blacklist) no script de indexação.

Como você lidaria com versões do mesmo documento?
Se um manual de perfil de cor mudou em 2026, o sistema pode recuperar a versão de 2024 e responder errado.

Resposta:
    Para evitar que o sistema recupere dados antigos, implementamos duas barreiras principais:

Controle de vigência por metadados:
    Todo documento ingerido recebe obrigatoriamente um campo de metadado de versão e ano de validade (ex: versao: "2.0", ano_vigencia: 2026).

Substituição física e reindexação:
    Quando uma nova versão de um manual é lançada, a versão antiga é imediatamente removida do diretório de ativos e o banco vetorial é atualizado (reindexado) para expurgar os chunks obsoletos, garantindo que o RAG acesse apenas a verdade mais recente.
    