from docling.document_converter import DocumentConverter
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.document_converter import DocumentConverter, PdfFormatOption
import os

# Set pipeline options
pipeline_options = PdfPipelineOptions()
pipeline_options.do_ocr = True
pipeline_options.do_table_structure = True
pipeline_options.table_structure_options.do_cell_matching = True
pipeline_options.ocr_options.lang = ["pt"]  # Set OCR language to Portuguese

doc_converter = DocumentConverter(
    format_options={
        InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
    }
)

def convert_pdf_to_md(input_file_path):
    """Convert PDF to markdown content"""
    print(f"Converting {input_file_path} to markdown...")
    #converter = DocumentConverter()
    converter = doc_converter
    result = converter.convert(input_file_path)
    return result.document.export_to_markdown()

def save_output(md_content, output_file_path):
    """Save markdown content to file"""
    print(f"Saving output to {output_file_path}...")
    output_dir = os.path.dirname(output_file_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(output_file_path, 'w', encoding='utf-8') as f:
        f.write(md_content)

### Main function
def convert_to_md(input_file_path, output_file_path):
    """Main function to convert PDF to MD and save"""
    md_content = convert_pdf_to_md(input_file_path)
    save_output(md_content, output_file_path)
    return output_file_path

#convert_to_md('originais/1111-64-O.pdf', 'markdown/1111-64-O.md')
