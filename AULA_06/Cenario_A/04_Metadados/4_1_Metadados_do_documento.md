JSON
{
    "document_id": "doc_manual_epson_01",
    "title": "Manual de Operação e Perfis de Cor - Epson SureColor",
    "author": "Epson America Inc. / Equipe de Colorimetria Interna",
    "source": "equipamentos/manual_epson_surecolor_v2.pdf",
    "document_type": "manual_tecnico",
    "created_at": "2024-01-15",
    "updated_at": "2026-03-10",
    "category": "equipamentos"
}


Explicação dos campos aplicados:

document_id: Identificador único para rastrear este manual específico no banco de dados.

title: O nome oficial do documento técnico consultado pela equipe.

author: O fabricante do equipamento ou o responsável técnico interno que redigiu o procedimento.

source: O caminho do arquivo dentro da nossa estrutura de pastas (equipamentos/).

document_type: Classifica o documento como um manual_tecnico (diferenciando de planilhas de substratos ou POPs).

created_at e updated_at: Essenciais para garantir que o sistema saiba a vigência do documento e não recupere instruções desatualizadas de anos anteriores.

category: A macrocategoria do diretório (equipamentos), que facilita a filtragem rápida na hora da busca semântica.