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
    location: str = Field(description="The person's location", default="")
    gender: str = Field(description="The person's gender (M/F)", default="")
    birth_date: str = Field(description="The person's date of birth in format dd-mm-yyyy", default="")
    process_number: str = Field(description="The person's process number", default="")

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
    - Process number, if available, usually in the first few lines  of the note, usually mentioned before the expression Nº Processo: .
    If the data is contradictory, use the one in the section between ">>> START NOTA DE ENTRADA <<<" and ">>> END NOTA DE ENTRADA <<<".
    If any field is not found, use an NULL.
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