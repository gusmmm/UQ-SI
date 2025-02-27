from code.person_info import extract_person_info
import os
import csv
from pathlib import Path

def get_patient_id(filename):
    """Extract patient ID from filename (only digits)"""
    return ''.join(c for c in filename if c.isdigit())

def process_all_files():
    """Process all MD files and save results to CSV"""
    # CSV headers based on Person model fields
    headers = [
        'patient_id', 'process_number', 'name', 'location', 'gender', 
        'birth_date', 'admission_date', 'origin', 'data_alta', 'destination',
        'tbsa', 'burn_mechanism', 'burn_etiology'
    ]
    
    # Create/open CSV file
    with open('dados_pessoais.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        
        # Process each MD file
        clean_dir = 'markdown_clean/merged'
        for filename in os.listdir(clean_dir):
            if filename.endswith('.md'):
                print(f"Processing {filename}...")
                try:
                    result = extract_person_info(os.path.join(clean_dir, filename))
                    if result:
                        # Write data to CSV
                        writer.writerow({
                            'patient_id': get_patient_id(filename),
                            'process_number': result.process_number,
                            'name': result.name,
                            'location': result.location,
                            'gender': result.gender,
                            'birth_date': result.birth_date,
                            'admission_date': result.admission_date,
                            'origin': result.origin,
                            'data_alta': result.data_alta,
                            'destination': result.destination,
                            'tbsa': result.tbsa,
                            'burn_mechanism': result.burn_mechanism,
                            'burn_etiology': result.burn_etiology
                        })
                    else:
                        print(f"Failed to extract info from {filename}")
                except Exception as e:
                    print(f"Error processing {filename}: {str(e)}")

if __name__ == "__main__":
    process_all_files()
    print("Data extraction complete. Results saved to dados_pessoais.csv")