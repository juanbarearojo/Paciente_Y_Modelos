import itertools
import csv
import os
import pandas as pd

#LECTURA DE LOS DATOS
df = pd.read_csv('data/pacientes/pacientes_usados.csv')

# Generar todas las combinaciones posibles de los índices de las filas
combinations = list(itertools.combinations(df.index, 2))

# Crear una lista para almacenar las combinaciones
combined_rows = []

# Combinar las filas basadas en los índices
for i, j in combinations:
    combined_row = pd.Series({
        'ID X': df.loc[i, 'ID'],
        'Edad X': df.loc[i, 'Edad'],
        'Sexo X': df.loc[i, 'Sexo'],
        'Crimen X': df.loc[i, 'Crimen'],
        'Clase Social X': df.loc[i, 'Clase Social'],
        'Enfermedad X': df.loc[i, 'Enfermedad'],
        'Consumo Drogas X': df.loc[i, 'Consumo Drogas'],
        'Educación X': df.loc[i, 'Educación'],
        'Religión X': df.loc[i, 'Religión'],
        'ID Y': df.loc[j, 'ID'],
        'Edad Y': df.loc[j, 'Edad'],
        'Sexo Y': df.loc[j, 'Sexo'],
        'Crimen Y': df.loc[j, 'Crimen'],
        'Clase Social Y': df.loc[j, 'Clase Social'],
        'Enfermedad Y': df.loc[j, 'Enfermedad'],
        'Consumo Drogas Y': df.loc[j, 'Consumo Drogas'],
        'Educación Y': df.loc[j, 'Educación'],
        'Religión Y': df.loc[j, 'Religión']
    })
    combined_rows.append(combined_row)

# Crear un nuevo DataFrame con las combinaciones
combinations_df = pd.DataFrame(combined_rows)

# Guardar el DataFrame en un archivo CSV
combinations_df.to_csv('data/pacientes/combinaciones_pacientes.csv', index=False)
