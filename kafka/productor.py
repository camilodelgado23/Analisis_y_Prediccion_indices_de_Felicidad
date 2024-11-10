from confluent_kafka import Producer
import pandas as pd
import json
import time
from sklearn.preprocessing import LabelEncoder

# Configuración del productor de Kafka
conf = {
    'bootstrap.servers': 'localhost:9092',  # Dirección del servidor Kafka
}

# Crear el productor
producer = Producer(conf)

# Cargar el DataFrame desde el archivo CSV
df = pd.read_csv('Data\\datos_felicidad_total.csv')

# Lista de las columnas que el modelo espera (sin 'Score')
columnas_modelo = ['Country or region', 'Region', 'GDP per capita', 'Social support', 
                   'Healthy life expectancy', 'Freedom to make life choices', 
                   'Perceptions of corruption', 'Generosity', 'Dystopia_Residual']

# Asegurarse de que df tenga solo las columnas correctas
df_selected = df[columnas_modelo]

# Codificar las columnas categóricas
label_encoder = LabelEncoder()
df_selected['Country or region'] = label_encoder.fit_transform(df_selected['Country or region'])
df_selected['Region'] = label_encoder.fit_transform(df_selected['Region'])

# Función para entregar el mensaje
def delivery_report(err, msg):
    if err is not None:
        print(f"Mensaje fallido: {err}")
    else:
        print(f"Mensaje entregado a {msg.topic()} [{msg.partition()}]")

# Enviar los datos al topic 'datos_entrada'
for index, row in df_selected.iterrows():
    data = row.to_dict()  # Convertir la fila a un diccionario
    producer.produce('datos_entrada', value=json.dumps(data).encode('utf-8'), callback=delivery_report)  # Enviar el dato al topic
    print(f"Enviado: {data}")
    time.sleep(0.0)  # Pausa de 1 segundo entre envíos

# Esperar a que todos los mensajes sean entregados
producer.flush()
