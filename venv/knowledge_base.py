import json

def load_knowledge_base(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            knowledge_data = json.load(file)
            return knowledge_data
    except FileNotFoundError:
        print("Knowledge base file not found.")
        return []
    except json.JSONDecodeError:
        print("Error decoding the JSON file.")
        return []
