from enum import Enum
import re
import json

class DWR_METHOD_TYPE(Enum):
    SCHEDULE = r'handleCallback\("3","0",(\[.*?\])\);'
    CLASS_DETAILS = r'handleCallback\("4","0",(\{.*?\})\);'
    TEACHER_DETAILS = r'handleCallback\("5","0",(\{.*?\})\);'

# Metodo responsavel pelo parsing das respostas obtidas pelo scrapper
def parse_dwr(content, dwr_method_type: DWR_METHOD_TYPE):
    """
    Parse DWR | Gerado por IA
    """

    if isinstance(content, bytes):
        content = content.decode('utf-8')
    
    match = re.search(dwr_method_type.value, content, re.DOTALL)
    
    if not match:
        print("No valid JSON data found in the response")
        return None
    
    json_str = match.group(1)
    
    json_str = re.sub(r'(?<=\{|,)\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*:', r'"\1":', json_str)
    
    try:
        return json.loads(json_str)
    except json.JSONDecodeError as e:
        print(f"JSON parsing error: {e}")
        print("Raw JSON string:", json_str[:500] + "..." if len(json_str) > 500 else json_str)
        return None