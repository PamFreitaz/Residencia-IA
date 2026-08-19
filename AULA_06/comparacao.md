**Comparação entre os Dois Cenários**

Abaixo está a análise comparativa entre o Cenário A (Laboratório Fotográfico - Técnico) e o Cenário B (E-commerce de Produtos Fotográficos - Comercial), avaliando as divergências, convergências e a escolha estratégica de projeto.

1. Em que pontos as decisões foram diferentes? Por quê?

* Tamanho e Estratégia de Chunking:

Cenário A: Utilizou chunks maiores (~600 caracteres) com overlap de 100. Por quê? Manuais técnicos exigem a preservação de sequências lógicas longas, passos de manutenção completos e tabelas de calibração que não podem ser fragmentadas.

Cenário B: Utilizou chunks menores (~350 caracteres) com overlap de 50. Por quê? Páginas de FAQ e políticas comerciais são formadas por perguntas e respostas diretas; blocos menores evitam misturar regras de produtos diferentes.

* Metadados Específicos de Negócio:

Cenário A: Adotou o metadado equipment_model (ex: Epson SureColor). Por quê? Impede que o sistema cruze instruções de plotters de marcas ou modelos diferentes, o que geraria falhas graves de operação na oficina.

Cenário B: Adotou o metadado product_line (ex: fotolivros, quadros). Por quê? Permite filtrar regras comerciais e gabaritos específicos de cada linha de produto do e-commerce.

* Frequência de Atualização e Ingestão:

Cenário A: Possui média frequência de mudanças, pois manuais de equipamentos são estáticos.

Cenário B: Possui alta frequência dinâmica (semanal/quinzenal), exigindo rotinas ágeis para atualizar campanhas promocionais, prazos e fretes.

2. Em que pontos foram iguais? Isso é sinal de boa prática geral ou de você ter repetido a decisão sem pensar?

Modelo de Embeddings (text-embedding-3-small): Ambos os cenários utilizaram o mesmo modelo da OpenAI.

É boa prática ou repetição sem pensar? É um sinal claro de boa prática de engenharia. Esse modelo é um padrão de mercado consolidado porque oferece excelente desempenho multilíngue (suporte robusto ao português), alta capacidade vetorial (1536 dimensões), teto de 8191 tokens e custo extremamente baixo (US$ 0.02 por milhão de tokens). Ele atende com perfeição tanto a termos técnicos complexos (Cenário A) quanto à linguagem informal e coloquial de clientes (Cenário B), tornando redundante a escolha de outro modelo sem justificativa técnica forte.

Arquitetura Base do Pipeline (Extração ➔ Limpeza ➔ Chunking ➔ Vetorização): A estrutura macro de engenharia de dados foi mantida idêntica.

É boa prática: Sim. Trata-se do padrão fundamental de qualquer aplicação RAG madura, garantindo modularidade, rastreabilidade e facilidade de manutenção em ambientes de produção reais.

3. Se você tivesse que construir apenas um dos dois, qual escolheria, e por quê?

Eu escolheria o cenário A pois teria zero margem para erro humano:

 Diferente de um e-commerce onde uma informação trocada no chat pode gerar um reembolso ou um pequeno atrito comercial, no laboratório fotográfico um erro de calibração ou um perfil de cor errado estraga uma tiragem industrial inteira de dezenas de quadros ou álbuns Fine Art. A escolha do Cenário A foca em uma IA de precisão cirúrgica e industrial, onde seguir o manual à risca evita prejuízos financeiros catastróficos de material.

 Enquanto o Cenário B lida com textos comerciais mais simples (FAQs e políticas), o Cenário A lida com engenharia de dados complexa: manuais densos de plotters (Epson, Canon), tabelas numéricas exatas de conversão de perfis ICC, códigos de erro de hardware e fichas de substratos que exigem um nível de compreensão técnica profundo.

O público-alvo não é o cliente final leigo, mas sim operadores de pré-impressão e técnicos especializados. Isso significa que a ferramenta pode e deve utilizar um vocabulário técnico rigoroso, permitindo buscas altamente específicas por modelos de equipamentos sem medo de confundir o usuário.

****************************************************************************************************

4. Como você usou IA para te apoiar nessa atividade? Quais ferramentas? Como você avaliou e verificou a resposta dela?

Fiz toda pesquisa usando Gemini, para todo o aprendizado e elaboração da estrutura