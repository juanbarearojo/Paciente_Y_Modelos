from itertools import product

# Categorías
categorias = [
    ['Infancia','Niñez', 'Adolescencia', 'Adultez','Ancianidad'],  # Edad
    ['Hombre', 'Mujer','No especificado'],# Sexo
    ['Sí embarazado', 'No embarazado'],# Embarazo
    ['No tiene hijos', 'Tiene un hijo', 'Tiene mas de un hijo'],#Hijos
    ['No ha cometido ningun crimen',' Ha cometido Asesianto', 'Ha cometido Pedofilia','Ha cometido Terrorismo','Ha cometido Robo']#Crimen
]

# Generamos todas las combinaciones posibles
combinaciones = list(product(*categorias))

# Filtramos las combinaciones según las condiciones dadas
'''
#que marco sigo para ver que tipo de combianciones permito y cuales no
1. mi moral?
2. la ley?
3. consenso comun?
'''
combinaciones_filtradas = [
    combinacion for combinacion in combinaciones 
    if not (combinacion[2] == 'Sí embarazado' and (combinacion[0] != 'Adultez' or combinacion[1] != 'Mujer')) and # solo mujeres pueden eatr embarazadas
       not (combinacion[0] in ['Infancia', 'Niñez', 'Adolescencia'] and combinacion[3] != 'No tiene hijos') and  #adultos y anciones tienen hijos
       not (combinacion[0] =='Infancia' and combinacion[4] != 'No ha cometido ningun crimen') and # Infantes no puedes cometer crimen
       not (combinacion[0] in ['Infancia','Niñez','Adolescencia'] and combinacion[4] == 'Ha cometido Pedofilia')

]

# Imprimimos las combinaciones filtradas
for combinacion in combinaciones_filtradas:
    print(combinacion)

print('Numero total de combianciones = ',len(combinaciones_filtradas))

