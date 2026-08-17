Cenário A: Assistente RAG de Suporte Técnico e Especificações de Impressão para um laboratório fotográfico

**Qual é o problema que você deseja resolver?**

O problema é a dificuldade dos operadores de pré-impressão e fotógrafos em consultar rapidamente manuais técnicos densos, guias de conversão de perfis de cores (como ICC) e especificações complexas de materiais, como gramaturas de papéis fine art e restrições de plotters, na hora de fechar um arquivo para produção, o que pode gerar erros e perda de material caro.

**Quem utilizaria a aplicação? Descreva o usuário concretamente:**

- Cargo:
    Operadores de pré-impressão, designers gráficos de laboratório e fotógrafos profissionais parceiros.

- Contexto de uso:
    Chão de produção ou atendimento técnico, onde o profissional está com um arquivo na tela prestes a enviar para impressão e precisa tirar uma dúvida urgente sobre compatibilidade de perfil de cor ou resolução mínima.

- Nível técnico:
    Intermediário a Avançado, eles entendem de termos técnicos de imagem, mas precisam de respostas precisas sem perder tempo folheando manuais de 300 páginas.

**Que tipo de informação o usuário gostaria de consultar?**

Parâmetros exatos de conversão de espaço de cores (ex: conversão de RGB para CMYK para um papel específico), limites de resolução (DPI) para impressões em grandes formatos, informações sobre a impressora ou qualquer equipamento, e soluções de problemas para falhas de jato de tinta em plotters profissionais.

**De onde vêm essas informações?**

De documentos PDF privados e manuais técnicos fornecidos pelos fabricantes de equipamentos (como Epson, Canon, Koda, etc), fichas técnicas de fornecedores de substratos/papéis especiais e guias internos de procedimentos de colorimetria do laboratório.

**Por que utilizar um LLM sozinho não seria suficiente?**

Porque um LLM genérico treinado na internet não conhece os perfis de calibragem proprietários dos equipamentos daquele laboratório específico, tampouco as restrições e fichas técnicas de papéis especializados que acabaram de ser lançados no mercado. Ele daria respostas genéricas ou "alucinaria" parâmetros técnicos que podem estragar a impressão e trazer prejuízo para a loja ou laboratório.

**Como o usuário vai utilizar o sistema?**

Através de uma interface web interna, um painel restrito para a equipe, com separação de roles ou integrado diretamente no fluxo de trabalho via chat corporativo para cada login.

**Três perguntas reais que um usuário faria ao sistema:**

1 - "Qual é o perfil ICC recomendado para imprimir em papel algodão texturizado 310g na plotter Epson SureColor?"

2 - "Qual é o valor de Delta E máximo tolerado na verificação de consistência entre o monitor calibrado da estação de retoque e a prova de cor física (soft proofing)?"

3 - "O que significa o código de erro de cabeçote entupido X5 no manual de manutenção da impressora e qual é o procedimento padrão de limpeza profunda para resolvê-lo?"