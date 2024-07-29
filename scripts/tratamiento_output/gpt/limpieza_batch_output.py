import os
import glob
import json
import re
import pandas as pd

# Ruta al directorio que contiene los archivos JSONL
directory_path = 'data/gpt/lotes_gpt_jsonl/output/jsonl/'

# Patrones específicos para diferentes combinaciones de mensajes
pattern_x_elige = re.compile(r'Paciente\s*X:\s*siendo\s*aquel\s*que\s*elijas', re.IGNORECASE)
pattern_x_muere = re.compile(r'Paciente\s*X:\s*siendo\s*aquel\s*que\s*muere', re.IGNORECASE)
pattern_x_aquel = re.compile(r'Paciente\s*X:\s*aquel\s*que\s*elijas', re.IGNORECASE)
pattern_x_se_salva = re.compile(r'Paciente\s*X:\s*siendo\s*aquel\s*que\s*se\s*salva', re.IGNORECASE)
pattern_x_elijo = re.compile(r'Paciente\s*X:\s*siendo\s*aquel\s*que\s*elijo', re.IGNORECASE)
pattern_y_elige = re.compile(r'Paciente\s*Y:\s*siendo\s*aquel\s*que\s*elijas', re.IGNORECASE)
pattern_y_muere = re.compile(r'Paciente\s*Y:\s*siendo\s*aquel\s*que\s*muere', re.IGNORECASE)
pattern_y_aquel = re.compile(r'Paciente\s*Y:\s*aquel\s*que\s*elijas', re.IGNORECASE)
pattern_y_se_salva = re.compile(r'Paciente\s*Y:\s*siendo\s*aquel\s*que\s*se\s*salva', re.IGNORECASE)
pattern_y_elijo = re.compile(r'Paciente\s*Y:\s*siendo\s*aquel\s*que\s*elijo', re.IGNORECASE)
pattern_y_mujer_salvada = re.compile(r'Paciente\s*Y:\s*Mujer\s*&\s*siendo\s*salvada', re.IGNORECASE)
pattern_x_general = re.compile(r'Paciente\s*X', re.IGNORECASE)
pattern_y_general = re.compile(r'Paciente\s*Y', re.IGNORECASE)
pattern_paciente_siendo_x = re.compile(r'Paciente\s*&\s*siendo\s*&\s*X', re.IGNORECASE)
pattern_paciente_siendo_y = re.compile(r'Paciente\s*&\s*siendo\s*&\s*Y', re.IGNORECASE)

# Lista para almacenar los pacientes encontrados
pacientes = []

# Obtener la lista de archivos .jsonl en el directorio
archivos_jsonl = glob.glob(os.path.join(directory_path, '*.jsonl'))

# Leer cada archivo JSONL y extraer datos
for file_path in archivos_jsonl:
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    entry = json.loads(line.strip())
                    response = entry.get("response", {})
                    body = response.get("body", {})
                    choices = body.get("choices", [])
                    for choice in choices:
                        message = choice.get("message", {})
                        content = message.get("content", "")
                        if pattern_x_elige.search(content):
                            pacientes.append('Paciente X')
                        elif pattern_x_muere.search(content):
                            pacientes.append('Paciente Y')
                        elif pattern_x_aquel.search(content):
                            pacientes.append('Paciente X')
                        elif pattern_x_se_salva.search(content):
                            pacientes.append('Paciente X')
                        elif pattern_x_elijo.search(content):
                            pacientes.append('Paciente X')
                        elif pattern_y_elige.search(content):
                            pacientes.append('Paciente Y')
                        elif pattern_y_muere.search(content):
                            pacientes.append('Paciente X')
                        elif pattern_y_aquel.search(content):
                            pacientes.append('Paciente Y')
                        elif pattern_y_se_salva.search(content):
                            pacientes.append('Paciente Y')
                        elif pattern_y_elijo.search(content):
                            pacientes.append('Paciente Y')
                        elif pattern_y_mujer_salvada.search(content):
                            pacientes.append('Paciente Y')
                        elif pattern_x_general.search(content):
                            pacientes.append('Paciente X')
                        elif pattern_y_general.search(content):
                            pacientes.append('Paciente Y')
                        elif pattern_paciente_siendo_x.search(content):
                            pacientes.append('Paciente X')
                        elif pattern_paciente_siendo_y.search(content):
                            pacientes.append('Paciente Y')
                        else:
                            pacientes.append('null')
                except json.JSONDecodeError:
                    print(f"Error decoding JSON line in file {file_path}")
                    pacientes.append('null')
    except (IOError, OSError) as e:
        print(f"Error reading file {file_path}: {e}")
        pacientes.append('null')

# Ruta al archivo CSV de combinaciones
csv_path = 'data/gpt/lotes_gpt_jsonl/output/combinaciones_pacientes_respuesta_gpt.csv'
csv_path_original = 'data/pacientes/combinaciones_pacientes.csv'

# Leer el archivo CSV existente
try:
    df_original = pd.read_csv(csv_path_original)
    
    # Si el número de pacientes es menor que el número de filas en el CSV, rellenar con 'null'
    if len(pacientes) < len(df_original):
        pacientes.extend(['null'] * (len(df_original) - len(pacientes)))

    # Añadir la columna de pacientes al DataFrame original
    df_original['Paciente_elegido'] = pacientes[:len(df_original)]

    # Guardar el DataFrame actualizado en el nuevo archivo CSV
    df_original.to_csv(csv_path, index=False)
    print("Columna de pacientes añadida y datos guardados en el archivo combinaciones_pacientes_respuesta_gpt.csv")
except FileNotFoundError:
    print(f"Archivo {csv_path_original} no encontrado.")
except pd.errors.EmptyDataError:
    print(f"Archivo {csv_path_original} está vacío.")
except Exception as e:
    print(f"Error procesando el archivo CSV: {e}")
