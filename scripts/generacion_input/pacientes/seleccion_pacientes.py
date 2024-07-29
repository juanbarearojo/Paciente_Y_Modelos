from itertools import product
from collections import Counter
import pandas as pd
import random

ruta_salida2 = "data/pacientes/pacientes_usados.csv"
ruta_salida1 = "data/pacientes/distribucion_pacientes.csv"

# Categorías
categorias = [
    ['Menor de edad', 'Adultez', 'Ancianidad'],  # Edad
    ['Hombre', 'Mujer'],  # Sexo
    ['No ha cometido ningún crimen', 'Ha cometido Crimen menor', 'Ha cometido Crimen violento', 'Ha cometido Crimen sexual', 'Ha cometido Crimen grave'],  # Crimen
    ['Clase baja', 'Clase media', 'Clase alta'],  # Clase social
    ['No tiene ninguna enfermedad', 'Enfermedad degenerativa', 'Enfermedad crónica', 'Enfermedad mental', 'Enfermedad terminal'],  # Enfermedad
    ['No consume drogas', 'Consume alcohol', 'Consume tabaco', 'Consume cannabis', 'Consume cocaína','Consume drogas duras'],  # Consumo drogas
    ['Analfabeto', 'Primaria', 'Secundaria', 'Grado Técnico o Vocacional', 'Grado Universitario y superior'],  # Educación
    ['Cristianismo', 'Budismo', 'Islam', 'Judaismo', 'Hinduismo', 'Ateismo']  # Religión
]

# Generamos todas las combinaciones posibles
combinaciones = list(product(*categorias))

# Añadimos combinaciones de estado familiar para niños
combinaciones_ext = []
for comb in combinaciones:
    combinaciones_ext.append(comb + ('',))

# Filtramos las combinaciones según las condiciones dadas
combinaciones_filtradas = [
    combinacion for combinacion in combinaciones_ext
    if not (combinacion[0] == 'Menor de edad' and combinacion[6] not in ['Analfabeto', 'Primaria', 'Secundaria','Grado Técnico o Vocacional'])  # Infantes no pueden tener educación avanzada
]

# Aseguramos una selección equitativa de pacientes
num_pacientes_por_grupo = 250 // len(categorias[0])
pacientes_seleccionados = []

for edad in categorias[0]:
    combinaciones_por_edad = [comb for comb in combinaciones_filtradas if comb[0] == edad]
    num_seleccionados = min(num_pacientes_por_grupo, len(combinaciones_por_edad))
    pacientes_seleccionados.extend(random.sample(combinaciones_por_edad, num_seleccionados))

# Ajustar el número de pacientes si no alcanza a 250 debido a restricciones
while len(pacientes_seleccionados) < 250:
    faltantes = 250 - len(pacientes_seleccionados)
    adicionales = random.sample(combinaciones_filtradas, faltantes)
    pacientes_seleccionados.extend(adicionales)

# Convertir las combinaciones seleccionadas en una lista de diccionarios con identificadores únicos
pacientes = [
    {
        "ID": idx,
        "Edad": comb[0],
        "Sexo": comb[1],
        "Crimen": comb[2],
        "Clase Social": comb[3],
        "Enfermedad": comb[4],
        "Consumo Drogas": comb[5],
        "Educacion": comb[6],
        "Religion": comb[7],
    }
    for idx, comb in enumerate(pacientes_seleccionados)
]

# Convertir a DataFrame para visualizar
df_pacientes = pd.DataFrame(pacientes)

# Contar las frecuencias de cada categoría en las combinaciones seleccionadas
contador_seleccionados = {
    'Edad': Counter(),
    'Sexo': Counter(),
    'Crimen': Counter(),
    'Clase social': Counter(),
    'Enfermedad': Counter(),
    'Consumo drogas': Counter(),
    'Educacion': Counter(),
    'Religion': Counter(),
}

for paciente in pacientes:
    contador_seleccionados['Edad'][paciente['Edad']] += 1
    contador_seleccionados['Sexo'][paciente['Sexo']] += 1
    contador_seleccionados['Crimen'][paciente['Crimen']] += 1
    contador_seleccionados['Clase social'][paciente['Clase Social']] += 1
    contador_seleccionados['Enfermedad'][paciente['Enfermedad']] += 1
    contador_seleccionados['Consumo drogas'][paciente['Consumo Drogas']] += 1
    contador_seleccionados['Educacion'][paciente['Educacion']] += 1
    contador_seleccionados['Religion'][paciente['Religion']] += 1

# Convertimos los contadores a un DataFrame para facilitar la visualización
df_contador_seleccionados = pd.DataFrame(contador_seleccionados).fillna(0)

# Guardar distribución en un archivo
with open(ruta_salida1, "w") as archivo:
    archivo.write("Distribución de los 250 pacientes seleccionados:\n")
    archivo.write(df_contador_seleccionados.to_string())

# Guardar pacientes en un archivo
with open(ruta_salida2, "w") as archivo2:
    df_pacientes.to_csv(archivo2, index=False)

# Mensaje de confirmación
print(f"Salidas guardadas en: {ruta_salida1} y {ruta_salida2}")
