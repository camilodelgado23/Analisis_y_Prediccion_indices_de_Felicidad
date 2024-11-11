from confluent_kafka import Consumer
import json
import joblib
import pandas as pd
import os
from sklearn.preprocessing import LabelEncoder
from feature_selection import seleccionar_caracteristicas

modelo = joblib.load('Model/random_forest_model.pkl')

conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'test-consumer-group',
    'auto.offset.reset': 'earliest'
}

consumer = Consumer(conf)

consumer.subscribe(['datos_entrada'])

csv_path = 'predicciones_resultados.csv'
if not os.path.isfile(csv_path):
    with open(csv_path, 'w') as file:
        file.write("Country or region,Region,GDP per capita,Social support,Healthy life expectancy,Freedom to make life choices,Perceptions of corruption,Generosity,Dystopia_Residual,Prediccion\n")

try:
    while True:
        msg = consumer.poll(timeout=0.2)

        if msg is None:
            continue
        if msg.error():
            print(f"Error en el mensaje: {msg.error()}")
            continue
        
        data = msg.value()
        
        if isinstance(data, bytes):
            data = json.loads(data.decode('utf-8'))

        print("Datos recibidos: ", data)

        datos_seleccionados = seleccionar_caracteristicas(data)

        df_selected = pd.DataFrame([datos_seleccionados], columns=[
            'Country or region', 'Region', 'GDP per capita', 'Social support',
            'Healthy life expectancy', 'Freedom to make life choices',
            'Perceptions of corruption', 'Generosity', 'Dystopia_Residual'
        ])

        prediccion = modelo.predict(df_selected)
        print(f"Predicción: {prediccion[0]}")

        df_selected['Prediccion'] = prediccion[0] 
        df_selected.to_csv(csv_path, mode='a', header=False, index=False)  
finally:
    consumer.close()
