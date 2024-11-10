from confluent_kafka import Consumer
import json
import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from feature_selection import seleccionar_caracteristicas

# Cargar el modelo entrenado
modelo = joblib.load('Model/random_forest_model.pkl')

# Configura el consumidor
conf = {
    'bootstrap.servers': 'localhost:9092',  # Dirección del servidor Kafka
    'group.id': 'test-consumer-group',  # ID del grupo del consumidor
    'auto.offset.reset': 'earliest'  # Empezar desde el principio
}

consumer = Consumer(conf)

# Suscribirse al topic 'datos_entrada'
consumer.subscribe(['datos_entrada'])

# Procesar los datos recibidos, seleccionar características y hacer la predicción
try:
    while True:
        msg = consumer.poll(timeout=0.2)  # Obtener mensaje con tiempo de espera de 1 segundo

        if msg is None:  # Si no se recibió ningún mensaje, continuar
            continue
        if msg.error():  # Si hay un error en el mensaje, imprimir y continuar
            print(f"Error en el mensaje: {msg.error()}")
            continue
        
        # Obtener los datos del mensaje
        data = msg.value()
        
        # Verifica el tipo de datos
        if isinstance(data, bytes):
            data = json.loads(data.decode('utf-8'))

        print("Datos recibidos: ", data)

        # Selección de características (solo las que el modelo necesita)
        datos_seleccionados = seleccionar_caracteristicas(data)

        # Crear el DataFrame para hacer la predicción
        df_selected = pd.DataFrame([datos_seleccionados], columns=['Country or region', 'Region', 'GDP per capita', 'Social support', 
                                                                   'Healthy life expectancy', 'Freedom to make life choices', 
                                                                   'Perceptions of corruption', 'Generosity', 'Dystopia_Residual'])

        # Codificar las columnas categóricas como durante el entrenamiento
        label_encoder = LabelEncoder()
        df_selected['Country or region'] = label_encoder.fit_transform(df_selected['Country or region'])
        df_selected['Region'] = label_encoder.fit_transform(df_selected['Region'])

        # Hacer la predicción
        prediccion = modelo.predict(df_selected)
        print(f"Predicción: {prediccion[0]}")
finally:
    # Asegurarse de cerrar el consumidor al finalizar
    consumer.close()
