import os
from code.convert_to_md import convert_to_md
from code.clean_md_E import clean_md_E
from code.clean_md_A import clean_md_A
from code.clean_md_O import clean_md_O

# File type constants
NOTA_ENTRADA = 'E.pdf'      # Notas de entrada
NOTA_ALTA = 'A.pdf'         # Notas de alta
CERT_OBITO = ['O.pdf', 'BIC.pdf']    # Certificados de óbito

def check_if_converted(pdf_path):
    """Check if PDF has already been converted to MD"""
    md_path = pdf_path.replace('originais', 'markdown').replace('.pdf', '.md')
    return os.path.exists(md_path)

def process_nota_entrada(input_file, output_file):
    """Process 'nota de entrada' PDF files"""
    print(f"Converting nota de entrada: {input_file}...")
    md_file = convert_to_md(input_file, output_file)
    clean_md_E(output_file)

def process_nota_alta(input_file, output_file):
    """Process 'nota de alta' PDF files"""
    print(f"Converting nota de alta: {input_file}...")
    md_file = convert_to_md(input_file, output_file)
    clean_md_A(output_file)

def process_cert_obito(input_file, output_file):
    print(f"Converting nota de obito: {input_file}...")
    md_file = convert_to_md(input_file, output_file)
    clean_md_O(output_file)

def is_death_certificate(pdf_file):
    """Check if the file is a death certificate"""
    return any(pdf_file.endswith(cert) for cert in CERT_OBITO)

def main():
    """
    Main function to process different types of medical documents:
    - Notas de entrada (E.pdf)
    - Notas de alta (A.pdf)
    - Certificados de óbito (O.pdf or BIC.pdf)
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
        elif is_death_certificate(pdf_file):
            process_cert_obito(input_file, output_file)

if __name__ == "__main__":
    main()