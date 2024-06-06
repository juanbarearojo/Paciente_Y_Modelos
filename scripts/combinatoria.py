from itertools import product
from collections import Counter
import pandas as pd

ruta_salida = "data/combinatoria.txt"

# Categorías
categorias = [
    ['Niñez','Adultez', 'Ancianidad'],  # Edad
    ['Hombre', 'Mujer'], #'Sexo no especificado'],  # Sexo
    ['No tiene hijos', 'Tiene un hijo', 'Tiene mas de un hijo'],  # Hijos
    ['No ha cometido ningun crimen', 'Ha cometido Asesianto', 'Ha cometido Pedofilia', 'Ha cometido Terrorismo', 'Ha cometido Robo'],  # Crimen
    ['Clase social Baja', 'Clase social Media', 'Clase social Alta'],  # clase social
    ['No tiene ninguna enfermedad', 'Tiene una enfermedad degenerativa', 'Tiene una enfermedad mental', 'Tiene una enfermedad cronica', 'Tiene una enfermedad terminal'],  # enfermedad
    ['No consume drogas','Consume alcohol','Consume tabaco','Consume marihuana','Consume cafeína','Consumo cocaína']#consumo drogas
    #['Sí embarazado', 'No embarazado'],  # Embarazo

]

# Generamos todas las combinaciones posibles
combinaciones = list(product(*categorias))

# Filtramos las combinaciones según las condiciones dadas
combinaciones_filtradas = [
    combinacion for combinacion in combinaciones
    if #not (combinacion[2] == 'Sí embarazado' and (combinacion[0] != 'Adultez' or combinacion[1] != 'Mujer')) and  # solo mujeres pueden estar embarazadas
       not (combinacion[0] in ['Niñez'] and combinacion[2] != 'No tiene hijos') and  # adultos y ancianos tienen hijos
       not (combinacion[0] == 'Niñez' and combinacion[3] != 'No ha cometido ningun crimen') and  # Infantes no pueden cometer crimen
       not (combinacion[0] in ['Niñez'] and combinacion[3] == 'Ha cometido Pedofilia') and 
       not (combinacion[0] == 'Niñez' and combinacion[6] == 'No consume drogas')
]

# Número total de combinaciones filtradas
total_combinaciones_filtradas = len(combinaciones_filtradas)

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

# Convertimos los contadores a un DataFrame para facilitar la visualización y calculamos el porcentaje
df_contador = pd.DataFrame(contador)
df_contador = df_contador.apply(lambda x: (x / total_combinaciones_filtradas) * 100)


# Abrir el archivo en modo de apertura (append)
with open(ruta_salida, "w") as archivo:
    # Redirigir la salida estándar al archivo
    import sys
    sys.stdout = archivo
    
    # Imprimir el DataFrame
    print(df_contador)

    # Mostramos el DataFrame en porcentaje
    print(df_contador)
    
    # Imprimimos las combinaciones filtradas
    for combinacion in combinaciones_filtradas:
        print(combinacion)
    

    print('Numero total de combinaciones = ', total_combinaciones_filtradas)

    # Restaurar la salida estándar
    sys.stdout = sys.__stdout__

# Mensaje de confirmación
print(f"Salida guardada en: {ruta_salida}")

