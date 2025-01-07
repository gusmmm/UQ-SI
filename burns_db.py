from code.extract_burn_data import extract_burn_data
import os
import csv
from pathlib import Path

def flatten_burn_data(burn_data, filename):
    """Flatten nested burn data structure for CSV"""
    flattened_data = []
    
    # Base record with common data
    base_record = {
        'filename': filename,
        'total_body_surface_area': burn_data.total_body_surface_area,
        'mechanism': burn_data.mechanism.value,
        'patient_factors': '; '.join(burn_data.patient_factors),
        'compartment_syndrome': burn_data.compartment_syndrome.compartment_syndrome,
        'compartment_locations': '; '.join(burn_data.compartment_syndrome.locations),
        'compartment_intervention': burn_data.compartment_syndrome.intervention
    }
    
    # Create a record for each burn location
    for burn_loc in burn_data.burn_locations:
        record = base_record.copy()
        record.update({
            'location': burn_loc.location,
            'depth': burn_loc.depth.value,
            'is_circumferential': burn_loc.is_circumferential,
            'laterality': burn_loc.laterality.value
        })
        flattened_data.append(record)
    
    return flattened_data

def process_all_files():
    """Process all merged MD files and save results to CSV"""
    # CSV headers
    headers = [
        'filename', 'location', 'depth', 'is_circumferential', 'laterality',
        'total_body_surface_area', 'mechanism', 'patient_factors',
        'compartment_syndrome', 'compartment_locations', 'compartment_intervention'
    ]
    
    merged_dir = 'markdown_clean/merged'
    
    # Create/open CSV file
    with open('burnDB.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        
        # Process each merged MD file
        for filename in os.listdir(merged_dir):
            if filename.endswith('_merged.md'):
                print(f"Processing {filename}...")
                try:
                    result = extract_burn_data(filename)
                    if result:
                        # Flatten and write data to CSV
                        flattened_data = flatten_burn_data(result, filename)
                        for record in flattened_data:
                            writer.writerow(record)
                    else:
                        print(f"No burn data extracted from {filename}")
                except Exception as e:
                    print(f"Error processing {filename}: {str(e)}")

if __name__ == "__main__":
    process_all_files()
    print("Data extraction complete. Results saved to burnDB.csv")