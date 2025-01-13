from pydantic import BaseModel, Field
from pydantic_ai import Agent
from typing import Optional
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key from environment
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in environment variables")

class Person(BaseModel):
    name: str = Field(description="The person's full name")
    location: str = Field(description="The person's location", default="NULL")
    gender: str = Field(description="The person's gender (M/F)", default="NULL")
    birth_date: str = Field(description="The person's birth date (dd-mm-yyyy)", default="NULL")
    process_number: str = Field(description="The person's process number", default="NULL")
    admission_date: str = Field(description="The admission date to burn unit (dd-mm-yyyy)", default="NULL")
    origin: str = Field(description="Where patient came from before burn unit admission", default="NULL")
    data_alta: str = Field(description="The discharge date from burn unit (dd-mm-yyyy)", default="NULL")
    destination: str = Field(description="Where patient was discharged to", default="NULL")

def read_md_file(filename):
    """Read content from a markdown file in the clean folder"""
    #file_path = os.path.join('markdown_clean', filename)
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File {filename} not found")
        return None

# Create Gemini agent
agent = Agent(
    'gemini-2.0-flash-exp',
    result_type=Person,
    system_prompt="""
    Extract the following information from the Portuguese text:
    - Full name of the person
    - Location if mentioned, extract just the name of the city or region
    - The person's gender (M/F), if present
    - Date of birth in format dd-mm-yyyy, if available it is usually mentioned before "Data Nasc:". If it is not there it is before the patient's name.
    - Process number, if available, usually in the first few lines of the note, usually mentioned before the expression Nº Processo: .
    - Admission date in format dd-mm-yyyy, usually in the first few lines of the admission note (between ">>> START NOTA DE ENTRADA <<<" and ">>> END NOTA DE ENTRADA <<<")
    - Origin: where the patient came from before admission to burn unit. Look for:
      * Hospital services (urgência, internamento, etc)
      * Other hospitals (usually mentioned with 'transferido de' or 'proveniente de')
      * Transport services (VMER, HELI, INEM)
      * Look in the section between ">>> START NOTA DE ENTRADA <<<" and ">>> END NOTA DE ENTRADA <<<")
    - Data Alta: discharge date in format dd-mm-yyyy (look between ">>> START NOTA DE ALTA <<<" and ">>> END NOTA DE ALTA <<<")
    - Destination: where patient was discharged to. Look for:
      * Hospital services (enfermaria, consulta externa, etc)
      * Other hospitals (mentioned with 'transferido para' or 'enviado para'). In case of another hospital, try and be specific about the hospital name.
      * Home (domicílio, casa, residência)
      * Institutions (lar, centro de reabilitação)
      * deceased (óbito)
      * Look in the section between ">>> START NOTA DE ALTA <<<" and ">>> END NOTA DE ALTA <<<")
    If the data is contradictory, use the one in the appropriate section (ENTRADA or ALTA).
    If any field is not found, use NULL.
    """
)

def extract_person_info(filename):
    md_content = read_md_file(filename)
    if md_content:
        try:
            result = agent.run_sync(md_content)
            return result.data if result else None
        except Exception as e:
            print(f"Extraction error: {str(e)}")
            return None
    return None

#print(extract_person_info('1102-55-E.md'))