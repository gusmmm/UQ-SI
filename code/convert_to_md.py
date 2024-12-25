from docling.document_converter import DocumentConverter
import os

def convert_pdf_to_md(input_file_path):
    """Convert PDF to markdown content"""
    print(f"Converting {input_file_path} to markdown...")
    converter = DocumentConverter()
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

