import os

## This script is used to clean the markdown files generated by the convert_to_md.py script

### Helper functions

def process_file(input_file):
    """Remove blank lines, specific content, and duplicate lines from the file"""
    print(f"Processing {input_file}...")
    # Strings to remove
    remove_strings = [
        "H. SAO JOAO ALAMEDA PROF. HERNANI MONTEIRO PORTO 4200-319 ULS DE SAO JOAO, E.P.E. Email:",
        "Tel. : 225512100",
        "Tel:",
        "Nº SNS (código de barras):",
        "<!-- image -->",
        "Data de Criação :",
        "Data de Bloqueio :",
        "Versão :",
        "ULS DE SAO JOAO, E.P.E."
    ]
    
    # Read input file
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    # Remove blank lines, specific strings, and lines with double underscores
    cleaned_lines = [
        line for line in lines 
        if line.strip() and 
           not any(remove_str in line.strip() for remove_str in remove_strings) and
           '\\_' not in line
    ]
    
    # Remove duplicates while preserving order
    cleaned_lines = list(dict.fromkeys(cleaned_lines))
    
    return cleaned_lines

def save_output(input_file, cleaned_content):
    """Save processed content to clean folder"""
    print(f"Cleaning {input_file}...")
    
    # Create clean directory if it doesn't exist
    clean_dir = 'markdown_clean'
    if not os.path.exists(clean_dir):
        os.makedirs(clean_dir)
    
    # Generate output filename in clean directory
    filename = os.path.basename(input_file)
    output_file = os.path.join(clean_dir, filename)
    
    # Write to output file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.writelines(cleaned_content)
    
    print(f"Cleaned file saved as: {output_file}")

### Main function
def clean_md(input_file_path):
    cleaned_content = process_file(input_file_path)
    save_output(input_file_path, cleaned_content)
