from code.person_info import extract_person_info
import os
import csv
from pathlib import Path

def process_all_files():
    """Process all MD files and save results to CSV"""
    # CSV headers based on Person model fields
    headers = ['filename', 'name', 'location', 'gender', 'birth_date', 'process_number']
    
    # Create/open CSV file
    with open('dados_pessoais.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        
        # Process each MD file
        clean_dir = 'markdown_clean'
        for filename in os.listdir(clean_dir):
            if filename.endswith('.md'):
                print(f"Processing {filename}...")
                try:
                    result = extract_person_info(filename)
                    if result:
                        # Write data to CSV
                        writer.writerow({
                            'filename': filename,
                            'name': result.name,
                            'location': result.location,
                            'gender': result.gender,
                            'birth_date': result.birth_date,
                            'process_number': result.process_number
                        })
                    else:
                        print(f"Failed to extract info from {filename}")
                except Exception as e:
                    print(f"Error processing {filename}: {str(e)}")

if __name__ == "__main__":
    process_all_files()
    print("Data extraction complete. Results saved to dados_pessoais.csv")