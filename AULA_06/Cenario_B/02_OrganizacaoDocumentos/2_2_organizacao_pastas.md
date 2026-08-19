documentos_ecommerce/
├── faqs/                  # Perguntas frequentes de clientes finais
├── politicas/             # Prazos, termos de troca, avarias e reembolsos
├── gabaritos_produtos/    # Especificações de tamanhos, margens e sangrias de álbuns/quadros
└── promocoes/             # Regras de campanhas ativas, cupons e descontos sazonais

****************************************************************************************************

*Justificativa da estrutura:*

Essa divisão espelha a forma como a equipe de atendimento divide o suporte ao cliente (dúvidas de produto, regras de envio ou campanhas). Facilita a filtragem por metadados direcionados.

****************************************************************************************************

Existe documento que não deve entrar na base? Como você impediria a entrada?

Resposta:
    Sim. Planilhas internas de custos e margens de lucro negociadas com fornecedores (dados financeiros sigilosos) e regras de campanhas promocionais ou cupons de desconto que já expiraram.

Como impedir:
    Através de uma curadoria humana restrita no pipeline de ingestão (apenas a equipe de gestão comercial e marketing pode aprovar novos arquivos na pasta raiz do e-commerce) e o uso de regras de exclusão por metadados ou listas de bloqueio (blacklist) no script de indexação para bloquear arquivos com termos financeiros restritos.

Como você lidaria com versões do mesmo documento? Se uma política de troca ou tabela de prazos mudou em 2026, o sistema pode recuperar a versão de 2024 e responder errado.

Resposta:
    Para evitar que o sistema recupere dados antigos ou regras de campanhas vencidas, implementamos duas barreiras principais:

Controle de vigência por metadados: Todo documento ingerido recebe obrigatoriamente campos de metadados de vigência e ano (ex: document_type: "politica_comercial", updated_at: "2026-02-15").

Substituição física e reindexação: Quando uma nova tabela de prazos de produção ou política de frete é lançada, a versão antiga é imediatamente removida do diretório do e-commerce e o banco vetorial é atualizado (reindexado) para expurgar os chunks obsoletos, garantindo que o RAG acesse estritamente a verdade comercial mais recente.