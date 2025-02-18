from utils import load_data, load_template, add_json
import json

def index():   
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title=dados['titulo'], details=dados['detalhes'])
        for dados in load_data('notes.json')
        ]
    notes = '\n'.join(notes_li)

    return load_template('index.html').format(notes=notes)

def submit(titulo,detalhes):
    # carrega o conteudo do json
    with open('static/data/notes.json', 'r', encoding='utf-8') as file:
        notas = json.load(file)
    
    # adiciona o novo conteudo na lista
    nova_nota = {'titulo': titulo, 'detalhes':detalhes}
    notas.append(nova_nota)

    add_json(notas)