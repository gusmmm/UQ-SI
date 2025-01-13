import os
from collections import defaultdict

def get_patient_id(filename):
    """Extract patient ID from filename (only digits)"""
    return ''.join(c for c in filename if c.isdigit())

def get_file_type_header(filename):
    """Return appropriate header based on file type"""
    if filename.endswith('A.md'):
        return ">>> START NOTA DE ALTA <<<"
    elif filename.endswith('E.md'):
        return ">>> START NOTA DE ENTRADA <<<"
    elif filename.endswith('O.md'):
        return ">>> START NOTA DE OBITO <<<"
    elif filename.endswith('BIC.md'):
        return ">>> START NOTA DE BIC <<<"
    return ""

def get_file_type_footer(filename):
    """Return appropriate footer based on file type"""
    if filename.endswith('A.md'):
        return ">>> END NOTA DE ALTA <<<"
    elif filename.endswith('E.md'):
        return ">>> END NOTA DE ENTRADA <<<"
    elif filename.endswith('O.md'):
        return ">>> END NOTA DE OBITO <<<"
    elif filename.endswith('BIC.md'):
        return ">>> END NOTA DE BIC <<<"
    return ""

def get_file_priority(filename):
    """Return priority value for sorting files (E first, then A, then BIC, then O)"""
    if filename.endswith('E.md'):
        return 1
    elif filename.endswith('A.md'):
        return 2
    elif filename.endswith('BIC.md'):
        return 3
    elif filename.endswith('O.md'):
        return 4
    return 5

def merge_patient_files():
    """Merge files by patient ID"""
    # Create output directory
    output_dir = 'markdown_clean/merged'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Group files by patient ID
    patient_files = defaultdict(list)
    clean_dir = 'markdown_clean'
    
    for filename in os.listdir(clean_dir):
        if filename.endswith('.md'):
            patient_id = get_patient_id(filename)
            patient_files[patient_id].append(filename)
    
    # Process each patient's files
    for patient_id, files in patient_files.items():
        merged_content = []
        
        # Sort files by priority (-A first)
        sorted_files = sorted(files, key=get_file_priority)
        
        # Process each file
        for filename in sorted_files:
            file_path = os.path.join(clean_dir, filename)
            header = get_file_type_header(filename)
            footer = get_file_type_footer(filename)
            
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                merged_content.append(f"{header}\n{content}\n{footer}\n")
        
        # Write merged content
        output_file = os.path.join(output_dir, f"{patient_id}_merged.md")
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("\n".join(merged_content))
        
        print(f"Created merged file for patient {patient_id}")

if __name__ == "__main__":
    merge_patient_files()