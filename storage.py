import json
import os

def save_json(data, file_path):         
    with open(file_path, 'w', encoding='utf-8' , errors='ignore') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def load_json(file_path):
    if not os.path.exists(file_path):
        return None
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        return json.load(f)