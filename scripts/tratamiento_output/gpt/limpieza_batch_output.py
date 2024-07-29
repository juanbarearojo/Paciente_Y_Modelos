import os
import glob
import json
import re
import pandas as pd

# Ruta al directorio que contiene los archivos JSONL
directory_path = 'data/gpt/lotes_gpt_jsonl/output/jsonl/'

pattern_x = re.compile(r'Paciente\s*(?:&\s*siendo\s*&\s*)?X', re.IGNORECASE)
pattern_y = re.compile(r'Paciente\s*(?:&\s*siendo\s*&\s*)?Y', re.IGNORECASE)

# Lista para almacenar los pacientes encontrados
pacientes = []

# Obtener la lista de archivos .jsonl en el directorio
archivos_jsonl = glob.glob(os.path.join(directory_path, '*.jsonl'))

# Leer cada archivo JSONL y extraer datos
for file_path in archivos_jsonl:
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

# Ruta al archivo CSV de combinaciones
csv_path = 'data/gpt/lotes_gpt_jsonl/output/combinaciones_pacientes_respuesta_gpt.csv'

# Leer el archivo CSV existente
df_combinaciones = pd.read_csv(csv_path)

# Si el número de pacientes es menor que el número de filas en el CSV, rellenar con 'null'
if len(pacientes) < len(df_combinaciones):
    pacientes.extend(['null'] * (len(df_combinaciones) - len(pacientes)))

# Añadir la columna de pacientes
df_combinaciones['Paciente_elegido'] = pacientes

# Guardar el DataFrame actualizado de nuevo en el archivo CSV
df_combinaciones.to_csv(csv_path, index=False)

print("Columna de pacientes añadida y datos guardados en el archivo combinaciones.csv")
