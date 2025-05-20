import json
import os

def load_request_template(request_name):
    template_path = os.path.join("requests", f"{request_name}.json")
    
    if not os.path.exists(template_path):
        raise FileNotFoundError(f"Request template for {request_name} not found.")
    
    with open(template_path, 'r') as file:
        return json.load(file)
