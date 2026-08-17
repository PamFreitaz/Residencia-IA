JSON
{
  "document_id": "doc_manual_epson_01",
  "chunk_id": "doc_manual_epson_01-05",
  "page": 5,
  "section": "Procedimento de Calibração de Cores e Perfis ICC",
  "document_type": "manual_tecnico",
  "category": "equipamentos",
  "equipment_model": "Epson SureColor",
  "text": "..."
}


Justificativa de cada metadado escolhido, por que cada um é importante?

document_id: Essencial para rastrear e vincular o pedaço de texto (chunk) ao documento de origem. Se uma nova versão do manual for lançada, conseguimos remover em lote todos os chunks associados a esse ID.

chunk_id: Identificador único e sequencial do fragmento (ex: documento 01, chunk 05). É fundamental para localizar a posição exata do trecho e permitir a recuperação programática do chunk seguinte (chunk_id + 1) caso a explicação esteja cortada.

page: Indica o número exato da página de onde o texto foi extraído. É indispensável para permitir que o operador do laboratório consulte o documento físico ou PDF original rapidamente.

section: Identifica o título da seção ou capítulo do manual. Ajuda o modelo a entender o contexto macro daquele trecho específico.

document_type: Classifica a natureza do arquivo (manual_tecnico, ficha_tecnica, pop), permitindo restringir buscas apenas a documentos de homologação oficial.

category: Define a macro pasta de origem (equipamentos, substratos, procedimentos), facilitando a segmentação da base vetorial.

equipment_model: Metadado próprio e crítico para o laboratório. Como existem diferentes plotters e impressoras na oficina, esse campo garante que o sistema saiba exatamente a qual maquinário (ex: Epson SureColor) aquela instrução pertence.