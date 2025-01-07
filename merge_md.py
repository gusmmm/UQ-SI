import os
from collections import defaultdict

def get_patient_id(filename):
    """Extract patient ID from filename (first 4 characters)"""
    return filename[:4]

def get_file_type_header(filename):
    """Return appropriate header based on file type"""
    if filename.endswith('-A.md'):
        return ">>> NOTA DE ALTA <<<"
    elif filename.endswith('-E.md'):
        return ">>> NOTA DE ENTRADA <<<"
    elif filename.endswith('-O.md'):
        return ">>> NOTA DE OBITO <<<"
    return ""

def get_file_priority(filename):
    """Return priority value for sorting files (-A first, then -E, then -O)"""
    if filename.endswith('-E.md'):
        return 0
    elif filename.endswith('-A.md'):
        return 1
    elif filename.endswith('-O.md'):
        return 2
    return 3

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
            
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                merged_content.append(f"{header}\n{content}\n")
        
        # Write merged content
        output_file = os.path.join(output_dir, f"{patient_id}_merged.md")
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("\n".join(merged_content))
        
        print(f"Created merged file for patient {patient_id}")

if __name__ == "__main__":
    merge_patient_files()