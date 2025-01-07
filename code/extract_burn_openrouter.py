from pydantic import BaseModel, Field
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from typing import Optional, List
from enum import Enum
import os
from dotenv import load_dotenv

# Load environment variables and context
load_dotenv()
with open('contextos/context_burn_classification.md', 'r') as f:
    BURN_CONTEXT = f.read()

OPENROUTER_API_KEY = os.getenv('OPENROUTER_API_KEY')
if not OPENROUTER_API_KEY:
    raise ValueError("OPENROUTER_API_KEY not found in environment variables")

model = OpenAIModel(
    'deepseek/deepseek-chat',
    #'google/gemini-2.0-flash-thinking-exp:free',   # or any other OpenRouter model
    base_url='https://openrouter.ai/api/v1',
    api_key=OPENROUTER_API_KEY,
)

class BurnDepth(str, Enum):
    FIRST_DEGREE = "first-degree"
    SECOND_DEGREE_SUPERFICIAL = "second-degree-superficial"
    SECOND_DEGREE_DEEP = "second-degree-deep"
    THIRD_DEGREE = "third-degree"
    FOURTH_DEGREE = "fourth-degree"

class BurnMechanism(str, Enum):
    THERMAL_FLAME = "thermal-flame"
    THERMAL_SCALD = "thermal-scald"
    THERMAL_CONTACT = "thermal-contact"
    ELECTRICAL_HIGH = "electrical-high"
    ELECTRICAL_LOW = "electrical-low"
    CHEMICAL = "chemical"
    RADIATION = "radiation"
    INHALATION = "inhalation"

class BurnLocation(BaseModel):
    location: str = Field(description="Body part affected")
    depth: BurnDepth = Field(description="Burn depth for this location")
    is_critical: bool = Field(description="Whether it's a critical location")
    is_circumferential: bool = Field(description="Whether the burn is circumferential")

class BurnData(BaseModel):
    burn_locations: List[BurnLocation] = Field(
        description="List of burn locations with their depths",
        default_factory=list
    )
    total_body_surface_area: float = Field(description="Total body surface area affected (%)")
    mechanism: BurnMechanism = Field(description="Mechanism of injury")
    patient_factors: List[str] = Field(
        description="List of patient factors including age, conditions, and injuries",
        default_factory=list
    )

def read_md_file(filename):
    """Read content from a markdown file in the clean folder"""
    file_path = os.path.join('markdown_clean', filename)
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File {file_path} not found")
        return None

agent = Agent(
    model=model,
    result_type=BurnData,
    system_prompt=f"""
    Using this burn classification context:
    
    {BURN_CONTEXT}
    
    Extract burn injury information from Portuguese medical notes into structured data.
    Each burn location should include both the body part and its burn depth.
    Patient factors should be listed individually.
    
    Return data according to the BurnData model structure.
    If information is not found, use empty lists or default values.
    """
)

def extract_burn_data(filename):
    """Extract burn data from markdown file"""
    md_content = read_md_file(filename)
    if md_content:
        try:
            result = agent.run_sync(md_content)
            return result.data if result else None
        except Exception as e:
            print(f"Extraction error: {str(e)}")
            return None
    return None

if __name__ == "__main__":
    result = extract_burn_data('1107-60-E.md')
    if result:
        print(result.model_dump_json(indent=2))