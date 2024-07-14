import json
import re

# Ruta al archivo JSONL
file_path = 'data/lotes_gpt_jsonl/output/batch_1.jsonl'

pattern_x = re.compile(r'Paciente\s*(?:&\s*siendo\s*&\s*)?X', re.IGNORECASE)
pattern_y = re.compile(r'Paciente\s*(?:&\s*siendo\s*&\s*)?Y', re.IGNORECASE)

# Leer el archivo JSONL y extraer datos
pacientes = []
with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        entry = json.loads(line.strip())
        response = entry.get("response", {})
        body = response.get("body", {})
        choices = body.get("choices", [])
        for choice in choices:
            message = choice.get("message", {})
            content = message.get("content", "")
            if pattern_x.search(content):
                pacientes.append('Paciente X')
            elif pattern_y.search(content):
                pacientes.append('Paciente Y')

# Mostrar resultados
a = 0
for paciente in pacientes:
    print(a, " ", paciente)
    a+=1
