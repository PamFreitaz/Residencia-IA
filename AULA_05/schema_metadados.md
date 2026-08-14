## Schema de Metadados dos Chunks

| Campo | Descrição |
| :--- | :--- |
| `fonte` | Nome do arquivo .md de origem |
| `documento_id` | Identificador único do documento |
| `chunk_index` | Posição do chunk dentro do documento |
| `estrategia` | Qual das 10 estratégias da Aula 04 gerou este chunk |
| `chunk_size` | Configuração usada para o tamanho do pedaço |
| `chunk_overlap` | Configuração usada para a sobreposição |
| `n_caracteres` | Tamanho real do chunk em número de caracteres |
| `data_criacao` | Data em que o arquivo foi processado |
| `nivel_dificuldade` | Se o texto é iniciante, intermediário ou avançado |
| `palavra_chave_principal` | O termo mais importante daquele pedaço de texto |


### Justificativa dos Campos Próprios:

1. **`data_criacao`**
   * "Quais documentos foram processados mais recentemente ou precisam de atualização de versão?"

2. **`nivel_dificuldade`**
   * "Mostre apenas explicações de nível iniciante ou avançado sobre esse tema para o usuário."

3. **`palavra_chave_principal`**
   * "Qual é o foco exato deste parágrafo ou chunk em uma única palavra-chave para melhorar a recuperação?"