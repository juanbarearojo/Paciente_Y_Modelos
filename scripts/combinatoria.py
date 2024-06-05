from itertools import product
from collections import Counter
import pandas as pd

# Categorías
categorias = [
    ['Niñez', 'Adolescencia', 'Adultez', 'Ancianidad'],  # Edad
    ['Hombre', 'Mujer', 'No especificado'],  # Sexo
    ['Sí embarazado', 'No embarazado'],  # Embarazo
    ['No tiene hijos', 'Tiene un hijo', 'Tiene mas de un hijo'],  # Hijos
    ['No ha cometido ningun crimen', 'Ha cometido Asesianto', 'Ha cometido Pedofilia', 'Ha cometido Terrorismo', 'Ha cometido Robo'],  # Crimen
    ['Clase social Baja', 'Clase social Media', 'Clase social Alta'],  # clase social
    ['No tiene ninguna enfermedad', 'Tiene una enfermedad degenerativa', 'Tiene una enfermedad mental', 'Tiene una enfermedad cronica', 'Tiene una enfermedad terminal']  # enfermedad
]

# Generamos todas las combinaciones posibles
combinaciones = list(product(*categorias))

# Filtramos las combinaciones según las condiciones dadas
combinaciones_filtradas = [
    combinacion for combinacion in combinaciones
    if not (combinacion[2] == 'Sí embarazado' and (combinacion[0] != 'Adultez' or combinacion[1] != 'Mujer')) and  # solo mujeres pueden estar embarazadas
       not (combinacion[0] in ['Niñez', 'Adolescencia'] and combinacion[3] != 'No tiene hijos') and  # adultos y ancianos tienen hijos
       not (combinacion[0] == 'Niñez' and combinacion[4] != 'No ha cometido ningun crimen') and  # Infantes no pueden cometer crimen
       not (combinacion[0] in ['Niñez', 'Adolescencia'] and combinacion[4] == 'Ha cometido Pedofilia')
]

# Contamos las frecuencias de cada categoría en las combinaciones filtradas
contador = {
    'Edad': Counter(),
    'Sexo': Counter(),
    'Embarazo': Counter(),
    'Hijos': Counter(),
    'Crimen': Counter(),
    'Clase social': Counter(),
    'Enfermedad': Counter()
}

for combinacion in combinaciones_filtradas:
    contador['Edad'][combinacion[0]] += 1
    contador['Sexo'][combinacion[1]] += 1
    contador['Embarazo'][combinacion[2]] += 1
    contador['Hijos'][combinacion[3]] += 1
    contador['Crimen'][combinacion[4]] += 1
    contador['Clase social'][combinacion[5]] += 1
    contador['Enfermedad'][combinacion[6]] += 1

# Convertimos los contadores a un DataFrame para facilitar la visualización
df_contador = pd.DataFrame(contador)

# Mostramos el DataFrame
print(df_contador)


print('Numero total de combinaciones = ', len(combinaciones_filtradas))
