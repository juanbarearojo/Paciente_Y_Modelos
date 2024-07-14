import itertools
import csv
import os
import pandas as pd

#LECTURA DE LOS DATOS
df = pd.read_csv('data/pacientes/pacientes_usados.csv')

## Generar todas las combinaciones posibles de las filas
combinations = list(itertools.combinations(df, 2))

# Crear un nuevo DataFrame con las combinaciones
combinations_df = pd.DataFrame(combinations)

print(combinations_df.head())

