import os

# Desativa o PyTorch Dynamo/Inductor para evitar dependência do compilador C++ (cl.exe)
os.environ["TORCH_COMPILE_DISABLE"] = "1"
os.environ["TORCH_LOGS"] = "-dynamo"

from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.datamodel.pipeline_options import PdfPipelineOptions

caminho_pdf = r"C:\Users\Usuario\Documents\Curso IA Puc\Aula2\bioetica_e_ia.pdf"

# Configurações do pipeline
pipeline_options = PdfPipelineOptions()
pipeline_options.do_ocr = True  # Mantém OCR se necessário

# Inicializa o conversor com as opções ajustadas
converter = DocumentConverter(
    format_options={
        "pdf": PdfFormatOption(pipeline_options=pipeline_options)
    }
)

print("Iniciando conversão...")
result = converter.convert(caminho_pdf)

# Exporta e salva em Markdown
conteudo_md = result.document.export_to_markdown()

with open("bioetica_e_ia.md", "w", encoding="utf-8") as f:
    f.write(conteudo_md)

print("Sucesso! Arquivo 'bioetica_e_ia.md' gerado com sucesso.")