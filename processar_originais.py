import os
from code.convert_to_md import convert_to_md
from code.clean_md import clean_md

# File type constants
NOTA_ENTRADA = '-E.pdf'    # Notas de entrada
NOTA_ALTA = '-A.pdf'       # Notas de alta
CERT_OBITO = '-O.pdf'      # Certificados de óbito

def check_if_converted(pdf_path):
    """Check if PDF has already been converted to MD"""
    md_path = pdf_path.replace('originais', 'markdown').replace('.pdf', '.md')
    return os.path.exists(md_path)

def process_nota_entrada(input_file, output_file):
    """Process 'nota de entrada' PDF files"""
    print(f"Converting nota de entrada: {input_file}...")
    md_file = convert_to_md(input_file, output_file)
    clean_md(output_file)

def process_nota_alta(input_file, output_file):
    """Process 'nota de alta' PDF files"""
    # TODO: Implement processing for notas de alta
    pass

def process_cert_obito(input_file, output_file):
    """Process 'certificado de óbito' PDF files"""
    # TODO: Implement processing for certificados de óbito
    pass

def main():
    """
    Main function to process different types of medical documents:
    - Notas de entrada (-E.pdf)
    - Notas de alta (-A.pdf)
    - Certificados de óbito (-O.pdf)
    """
    originais_dir = 'originais'
    
    # Get all PDF files in originais directory
    pdf_files = [f for f in os.listdir(originais_dir) if f.endswith('.pdf')]
    
    for pdf_file in pdf_files:
        input_file = os.path.join(originais_dir, pdf_file)
        output_file = os.path.join('markdown', pdf_file.replace('.pdf', '.md'))
        
        if check_if_converted(input_file):
            print(f"File {input_file} has already been converted. Skipping conversion.")
            continue
        
        # Process based on file type
        if pdf_file.endswith(NOTA_ENTRADA):
            process_nota_entrada(input_file, output_file)
        elif pdf_file.endswith(NOTA_ALTA):
            process_nota_alta(input_file, output_file)
        elif pdf_file.endswith(CERT_OBITO):
            process_cert_obito(input_file, output_file)

if __name__ == "__main__":
    main()