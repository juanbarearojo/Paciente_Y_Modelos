import json
import os

# Ruta de los archivos
archivo_entrada = 'data/gpt/prompt_gpt_usado.txt'  # Reemplazar con el nombre de tu archivo de datos
directorio_salida = 'data/gpt/lotes_gpt_jsonl/input/'  # Asegúrate de que este directorio exista

# Leer las líneas del archivo
with open(archivo_entrada, 'r', encoding='utf-8') as file:
    datos = file.readlines()

# Eliminar los saltos de línea
datos = [linea.strip() for linea in datos]

# Dividir las combinaciones en lotes de 100
lotes = [datos[i:i + 100] for i in range(0, len(datos), 100)]

# Asegurar que el directorio de salida exista
os.makedirs(directorio_salida, exist_ok=True)

# Función para crear un archivo jsonl
def crear_archivo_jsonl(lote, indice_lote):
    archivo_salida = f'{directorio_salida}lote_{indice_lote + 1}.jsonl'
    with open(archivo_salida, 'w', encoding='utf-8') as file:
        for index, combinacion in enumerate(lote):
            json_data = {
                "custom_id": f"request-{indice_lote}-{index}",
                "method": "POST",
                "url": "/v1/chat/completions",
                "body": {
                    "model": "gpt-3.5-turbo-0125",
                    "messages": [
                        {
                            "role": "user",
                            "content": combinacion
                        }
                    ],
                    "max_tokens": 1000
                }
            }
            file.write(json.dumps(json_data) + '\n')

# Crear los archivos jsonl para cada lote
for indice, lote in enumerate(lotes):
    crear_archivo_jsonl(lote, indice)

print(f"Se han generado {len(lotes)} archivos jsonl en {directorio_salida}")

