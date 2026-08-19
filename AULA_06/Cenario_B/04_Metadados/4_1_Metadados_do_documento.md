{
    "document_id": "doc_politica_trocas_01",
    "title": "Política de Trocas e Avarias de Produtos Personalizados",
    "author": "Equipe de Atendimento ao Cliente / Jurídico",
    "source": "politicas/trocas_e_avarias.md",
    "document_type": "politica_comercial",
    "created_at": "2025-01-10",
    "updated_at": "2026-02-15",
    "category": "politicas"
}

Explicação dos campos aplicados:

document_id: Identificador único e padronizado (doc_politica_trocas_01) para rastrear este documento comercial específico dentro da base de dados do e-commerce.

title: O nome oficial da política consultada (Política de Trocas e Avarias de Produtos Personalizados), facilitando a legibilidade humana e o rastreio visual do conteúdo.

author: O departamento ou equipe responsável pela redação e validação do documento (Equipe de Atendimento ao Cliente / Jurídico), garantindo a governança e a origem confiável da diretriz comercial.

source: O caminho do arquivo ou diretório de origem dentro da estrutura do e-commerce (politicas/trocas_e_avarias.md), permitindo localizar fisicamente o arquivo original no repositório.

document_type: Classifica a natureza do arquivo como uma politica_comercial (diferenciando de páginas de FAQ simples, planilhas de preços ou gabaritos de produtos).

created_at e updated_at: Datas essenciais para o controle de vigência. O campo updated_at ("2026-02-15") é criticamente importante no e-commerce para garantir que o pipeline de ingestão saiba se o documento sofreu alterações recentes e evite recuperar regras de troca caducadas.

category: A macrocategoria de diretório (politicas), que agrupa os documentos por área de negócio e agiliza a filtragem lógica na base vetorial.