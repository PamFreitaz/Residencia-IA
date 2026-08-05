import os

# Desativa o PyTorch Dynamo/Inductor para evitar dependência do compilador C++ (cl.exe)
os.environ["TORCH_COMPILE_DISABLE"] = "1"
os.environ["TORCH_LOGS"] = "-dynamo"

from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.datamodel.pipeline_options import PdfPipelineOptions

# Nomes dos arquivos na mesma pasta (AULA_02)
caminho_pdf = "escrita_academica_ia.pdf"
caminho_saida = "escrita_academica_ia.md"

# Configurações do pipeline
pipeline_options = PdfPipelineOptions()
pipeline_options.do_ocr = True  # Mantém OCR ligado como no anterior que funcionou

# Inicializa o conversor com as opções ajustadas
converter = DocumentConverter(
    format_options={
        "pdf": PdfFormatOption(pipeline_options=pipeline_options)
    }
)

print("Iniciando conversão de escrita_academica_ia.pdf...")
result = converter.convert(caminho_pdf)

# Exporta e salva em Markdown
conteudo_md = result.document.export_to_markdown()

with open(caminho_saida, "w", encoding="utf-8") as f:
    f.write(conteudo_md)

print("Sucesso! Arquivo 'escrita_academica_ia.md' gerado na pasta AULA_02.")