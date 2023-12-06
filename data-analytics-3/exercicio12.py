import json

with open('person.json', encoding='utf-8') as arquivo_json:
    print(json.load(arquivo_json))
