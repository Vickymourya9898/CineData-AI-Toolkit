import json
import re

# CineData-AI-Toolkit: Unstructured Casting Data Parser
# Purpose: Standardizes raw talent submission text into structured format.

def parse_talent_data(raw_text):
    data_schema = {
        "name": None,
        "contact": None,
        "availability": "Pan-India"
    }
    
    # Basic Regex extraction for contact info (Phone numbers)
    phone_pattern = re.compile(r'(\+91[\-\s]?)?[0-9]{10}')
    phone_match = phone_pattern.search(raw_text)
    if phone_match:
        data_schema["contact"] = phone_match.group()
        
    # TODO: Integrate Codex/OpenAI API for accurate entity extraction
    
    return json.dumps(data_schema, indent=4)

if __name__ == "__main__":
    sample_text = "Actor Rahul, 9876543210, Pune. Ready to travel."
    print("Standardized Output:")
    print(parse_talent_data(sample_text))
