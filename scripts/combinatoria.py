from itertools import product
from collections import Counter
import pandas as pd
import random

ruta_salida1 = "data/combinatoria_con_distribucion.txt"
ruta_salida2 = "data/combinatoria_tuplas.txt"


# Categorías
categorias = [
    ['Infancia', 'Adultez', 'Ancianidad'],  # Edad
    ['Hombre', 'Mujer'],  # Sexo
    ['No ha cometido ningun crimen', 'Ha cometido Asesinato', 'Ha cometido Abuso sexual', 'Ha cometido Terrorismo', 'Ha cometido Robo'],  # Crimen
    ['Clase social baja', 'Clase social media', 'Clase social alta'],  # Clase social
    ['No tiene ninguna enfermedad', 'Tiene una enfermedad degenerativa', 'Tiene una enfermedad mental', 'Tiene una enfermedad cronica', 'Tiene una enfermedad terminal'],  # Enfermedad
    ['No consume drogas', 'Consume alcohol', 'Consume tabaco', 'Consume marihuana', 'Consume cafeina', 'Consume cocaina'],  # Consumo drogas
    ['Analfabeto', 'Primaria', 'Secundaria', 'Grado', 'Doctorado'],  # Educación
    ['Cristianismo', 'Budismo', 'Islam', 'Judaismo', 'Hinduismo', 'Ateismo']  # Religión
]

# Estado familiar solo para Niñez
estado_familiar_ninez = ['Dos padres', 'Huérfano', 'Un padre']

# Generamos todas las combinaciones posibles
combinaciones = list(product(*categorias))

# Añadimos combinaciones de estado familiar para niños
combinaciones_ext = []
for comb in combinaciones:
    if comb[0] == 'Niñez':
        for estado_familiar in estado_familiar_ninez:
            combinaciones_ext.append(comb + (estado_familiar,))
    else:
        combinaciones_ext.append(comb + ( '',))

# Filtramos las combinaciones según las condiciones dadas
combinaciones_filtradas = [
    combinacion for combinacion in combinaciones_ext
    if not (combinacion[0] == 'Niñez' and combinacion[6] not in ['Analfabeto', 'Primaria'])  # Infantes no pueden tener educación avanzada
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

# Convertir las combinaciones seleccionadas en una lista de diccionarios
pacientes = [
    {
        "Edad": comb[0],
        "Sexo": comb[1],
        "Crimen": comb[2],
        "Clase Social": comb[3],
        "Enfermedad": comb[4],
        "Consumo Drogas": comb[5],
        "Educación": comb[6],
        "Religión": comb[7]
    }
    for comb in pacientes_seleccionados
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
    'Educación': Counter(),
    'Religión': Counter(),
}

for paciente in pacientes:
    contador_seleccionados['Edad'][paciente['Edad']] += 1
    contador_seleccionados['Sexo'][paciente['Sexo']] += 1
    contador_seleccionados['Crimen'][paciente['Crimen']] += 1
    contador_seleccionados['Clase social'][paciente['Clase Social']] += 1
    contador_seleccionados['Enfermedad'][paciente['Enfermedad']] += 1
    contador_seleccionados['Consumo drogas'][paciente['Consumo Drogas']] += 1
    contador_seleccionados['Educación'][paciente['Educación']] += 1
    contador_seleccionados['Religión'][paciente['Religión']] += 1

# Convertimos los contadores a un DataFrame para facilitar la visualización
df_contador_seleccionados = pd.DataFrame(contador_seleccionados).fillna(0)

# Guardar resultados en un archivo
with open(ruta_salida1, "w") as archivo:
    archivo.write("Distribución de los 250 pacientes seleccionados:\n")
    archivo.write(df_contador_seleccionados.to_string())
    archivo.write("\n\nPacientes Seleccionados:\n")
    df_pacientes.to_csv(archivo, index=False)

with open(ruta_salida2, "w") as archivo2:
    df_pacientes.to_csv(archivo2, index=False)

# Mensaje de confirmación
print(f"Salidas guardadas en: {ruta_salida1} y {ruta_salida2}")


