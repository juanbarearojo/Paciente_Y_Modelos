import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv('data/gpt/lotes_gpt_jsonl/output/combinaciones_pacientes_respuesta_gpt.csv')
# Definir la distribución inicial con todos los valores en 0
# Definir la distribución inicial con todos los valores en 0
categorias = [
    'Infancia', 'Adultez', 'Ancianidad', 'Hombre', 'Mujer', 'Ha cometido Asesinato', 
    'Ha cometido Abuso sexual', 'Ha cometido Robo', 'Ha cometido Terrorismo', 'No ha cometido ningun crimen',
    'Clase social media', 'Clase social baja', 'Clase social alta', 'Tiene una enfermedad terminal', 
    'No tiene ninguna enfermedad', 'Tiene una enfermedad cronica', 'Tiene una enfermedad mental', 
    'Tiene una enfermedad degenerativa', 'Consume alcohol', 'No consume drogas', 'Consume marihuana', 
    'Consume cafeina', 'Consume tabaco', 'Consume cocaina', 'Secundaria', 'Grado', 'Analfabeto', 'Primaria', 
    'Doctorado', 'Islam', 'Budismo', 'Cristianismo', 'Hinduismo', 'Ateismo', 'Judaismo'
]

distribucion = pd.DataFrame(0.0, index=categorias, columns=['Edad', 'Sexo', 'Crimen', 'Clase social', 'Enfermedad', 'Consumo drogas', 'Educacion', 'Religion'])

# Crear un DataFrame para contar las veces que cada ID es elegido
ids_elegidos = pd.DataFrame(0, index=range(250), columns=['Veces Elegido'])

# Función para actualizar la distribución y el conteo de IDs elegidos
def actualizar_distribucion(paciente, id_paciente):
    distribucion.loc[paciente['Edad'], 'Edad'] += 1
    distribucion.loc[paciente['Sexo'], 'Sexo'] += 1
    distribucion.loc[paciente['Crimen'], 'Crimen'] += 1
    distribucion.loc[paciente['Clase Social'], 'Clase social'] += 1
    distribucion.loc[paciente['Enfermedad'], 'Enfermedad'] += 1
    distribucion.loc[paciente['Consumo Drogas'], 'Consumo drogas'] += 1
    distribucion.loc[paciente['Educacion'], 'Educacion'] += 1
    distribucion.loc[paciente['Religion'], 'Religion'] += 1
    ids_elegidos.loc[id_paciente, 'Veces Elegido'] += 1

# Procesar cada fila del DataFrame
for index, row in df.iterrows():
    id_x = row['ID X']
    id_y = row['ID Y']
    
    if pd.isnull(row['Paciente_elegido']):
        continue
    
    if row['Paciente_elegido'] == 'Paciente X':
        paciente = {
            'Edad': row['Edad X'],
            'Sexo': row['Sexo X'],
            'Crimen': row['Crimen X'],
            'Clase Social': row['Clase Social X'],
            'Enfermedad': row['Enfermedad X'],
            'Consumo Drogas': row['Consumo Drogas X'],
            'Educacion': row['Educacion X'],
            'Religion': row['Religion X']
        }
        actualizar_distribucion(paciente, id_x)
    elif row['Paciente_elegido'] == 'Paciente Y':
        paciente = {
            'Edad': row['Edad Y'],
            'Sexo': row['Sexo Y'],
            'Crimen': row['Crimen Y'],
            'Clase Social': row['Clase Social Y'],
            'Enfermedad': row['Enfermedad Y'],
            'Consumo Drogas': row['Consumo Drogas Y'],
            'Educacion': row['Educacion Y'],
            'Religion': row['Religion Y']
        }
        actualizar_distribucion(paciente, id_y)

# Guardar la distribución actualizada en un archivo CSV
distribucion.to_csv('data/gpt/lotes_gpt_jsonl/output/distribucion_eleccion.csv')

# Guardar los IDs de los pacientes elegidos en otro archivo CSV
ids_elegidos.to_csv('data/gpt/lotes_gpt_jsonl/output/distribucion_ids_elegidos.csv', index=False)

print("Distribución guardada en 'data/gpt/lotes_gpt_jsonl/output/distribucion_eleccion.csv'")
print("IDs de pacientes elegidos guardados en 'data/gpt/lotes_gpt_jsonl/output/distribucion_ids_elegidos.csv'")
