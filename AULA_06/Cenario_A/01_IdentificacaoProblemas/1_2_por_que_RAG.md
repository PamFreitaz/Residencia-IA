1. Por que RAG é adequado para esse problema?

A escolha pelo RAG se dá pela necessidade de precisão. Ele combina a capacidade de compreensão de linguagem natural de um LLM com uma base de dados documental estrita e privada. Isso permite que a IA consulte manuais específicos antes de responder, garantindo que ela forneça dados técnicos validados em vez de "adivinhar" parâmetros ou alucinar informações críticas.

2. Que tipo de conhecimento precisa ser fornecido ao modelo?

Para que o sistema seja funcional, a base de conhecimento deve conter:

- Manuais de operação dos equipamentos.

- Fichas técnicas de substratos e papéis.

- Guias de colorimetria e perfis de cor.

- Procedimentos Operacionais Padrão (POPs) internos do laboratório.

3. Esse conhecimento muda com que frequência?

A frequência de atualização é média, as alterações do conteúdo apenas ocorrem em eventos específicos, como:

- Atualização de firmware das máquinas.

- Troca de fornecedores de suprimentos ou papéis.

- Implementação de novos padrões de processo (novos POPs).

4. Existe necessidade de utilizar documentos privados?

Sim. A exclusividade do sistema reside justamente na utilização de:

- Manuais internos de calibragem.

- Guias de procedimentos exclusivos, criados e validados pelo próprio laboratório, que não existem em bases de conhecimento públicas.

5. Que problemas poderiam ocorrer se o LLM respondesse apenas com seu conhecimento pré-treinado?

O LLM daria uma resposta genérica ou inventaria (alucinaria) códigos de erro e valores de Delta E ou perfis ICC que não correspondem à realidade daquele maquinário.
Exemplo de erro: Indicar um procedimento padrão de limpeza de cabeçote de uma impressora genérica que, na plotter específica do laboratório, danifique permanentemente o injetor de tinta.

