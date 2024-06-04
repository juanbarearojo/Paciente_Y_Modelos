from itertools import product

# Categorías
categorias = [
    ['Infancia','Niñez', 'Adolescente', 'Adultez','Ancianidad'],  # Edad
    ['Hombre', 'Mujer','No especificado'],# Sexo
    ['Sí embarazado', 'No embarazado']                        # Embarazo
]

# Generamos todas las combinaciones posibles
combinaciones = list(product(*categorias))

# Filtramos las combinaciones según las condiciones dadas
combinaciones_filtradas = [
    combinacion for combinacion in combinaciones 
    if not (combinacion[2] == 'Sí embarazado' and (combinacion[0] != 'Adultez' or combinacion[1] != 'Mujer'))
]

# Imprimimos las combinaciones filtradas
for combinacion in combinaciones_filtradas:
    print(combinacion)

