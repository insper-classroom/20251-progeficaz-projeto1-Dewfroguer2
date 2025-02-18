import json
import os
def load_data(filename):
    base = os.path.join('static','data', filename)

    try:
        with open(base,'r',encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Erro ao carregar o arquivo: {e}")
        return None
    
def load_template(filename):

    with open(f"static/templates/{filename}", 'r', encoding="utf-8") as file:
        conteudo = file.read()
        return conteudo
    
def add_json(nota):
    with open('static/data/notes.json', 'w', encoding='utf-8') as file:
        json.dump(nota, file, indent=4, ensure_ascii=False)