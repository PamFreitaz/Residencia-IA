CENÁRIO B: Assistente de Inteligência Artificial para E-commerce de Produtos Fotográficos Personalizados

**Qual é o problema que você deseja resolver?**

O problema é a dificuldade dos clientes finais na hora da compra e dos atendentes de suporte em consultar rapidamente regras complexas de gabaritos de impressão, prazos de produção de brindes, políticas de troca de álbuns personalizados e custos de frete em um e-commerce de fotografia.

**Quem utilizaria a aplicação? Descreva o usuário concretamente:**

- Cargo/Perfil:
    Clientes finais do e-commerce (consumidores comuns e fotógrafos amadores) e atendentes de suporte de primeiro nível da loja virtual.
  
- Contexto de uso:
    Durante o processo de montagem e fechamento de um pedido na loja virtual ou ao tirar dúvidas rápidas via chat de atendimento, mas principalmente para uma reclamação dos clientes que a RAG vai conseguir responder de uma forma mais satisfatório.

- Nível técnico:
    Iniciante a Intermediário, precisam de respostas claras, sem termos excessivamente técnicos de engenharia, mas com total precisão nas regras comerciais.

**Que tipo de informação o usuário gostaria de consultar?**

Prazos de postagem e produção, políticas de reembolso para produtos personalizados, exigências de gabarito (margens de segurança e sangria para álbuns e quadros) e regras de cupons promocionais.

**De onde vêm essas informações?**

De páginas de FAQ do site corporativo, documentos PDF com políticas internas de troca no Google Drive e manuais comerciais de produtos.

**Por que utilizar um LLM sozinho não seria suficiente?**

Porque os dados de um e-commerce são altamente voláteis e dinâmicos (prazos de entrega mudam, campanhas sazonais entram e saem, regras de frete e tabelas promocionais são atualizadas constantemente). Um LLM pré-treinado puro responderia com base em dados estáticos antigos ou inventaria políticas comerciais inexistentes (alucinação), gerando prejuízo financeiro direto à empresa e insatisfação no cliente.

**Como o usuário vai utilizar o sistema?**

Através de uma interface web interativa, um chat flutuante de atendimento ao cliente integrado à plataforma de e-commerce.

**Três perguntas reais que um usuário faria ao sistema:**

1 - "Qual é o prazo exato de produção e postagem para o fotolivro panorâmico de capa dura após a aprovação final do meu arquivo?"

2 - "Posso enviar arquivos em PNG com fundo transparente para a confecção de quadros canvas ou o sistema exige obrigatoriamente arquivos JPG em perfil sRGB?"

3 - "Comprei um álbum de casamento e ele chegou com a capa amassada por causa do transporte dos Correios; vocês fazem a reimpressão ou o reembolso?"