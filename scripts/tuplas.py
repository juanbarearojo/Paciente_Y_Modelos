import pandas as pd
import itertools

# Leer el archivo combinatoria.txt
df = pd.read_csv('data/combinatoria.txt', skiprows=40)

# Filtrar las filas relevantes (eliminar la primera fila de descripción)
df = df.iloc[40:]

# Generar todas las combinaciones de índices de filas
indices = df.index.tolist()
combinations = list(itertools.combinations(indices, 2))

# Añadir la frase "elige uno 'fila x' o 'fila y'" delante de cada combinación
combinations_with_phrase = [f"elige uno 'fila {comb[0]}' o 'fila {comb[1]}'" for comb in combinations]

# Guardar las combinaciones en un archivo de texto
with open('combinaciones_posibles.txt', 'w') as file:
    for line in combinations_with_phrase:
        file.write(line + '\n')

print("Combinaciones generadas y guardadas en combinaciones_posibles.txt")
