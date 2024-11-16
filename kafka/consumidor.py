import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from socket import create_connection
from confluent_kafka import Consumer
import json
import joblib
import pandas as pd
import mysql.connector
from feature_selection import seleccionar_caracteristicas
from Database.conexion_db import create_connection


modelo = joblib.load('Model/random_forest_regressor.pkl')

conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'test-consumer-group',
    'auto.offset.reset': 'earliest'
}

consumer = Consumer(conf)
consumer.subscribe(['datos_entrada'])


connection = create_connection()
cursor = connection.cursor()

tabla_sql = '''
CREATE TABLE IF NOT EXISTS predicciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    country_or_region VARCHAR(255),
    region VARCHAR(255),
    gdp_per_capita FLOAT,
    social_support FLOAT,
    healthy_life_expectancy FLOAT,
    freedom_to_make_life_choices FLOAT,
    perceptions_of_corruption FLOAT,
    generosity FLOAT,
    dystopia_residual FLOAT,
    score FLOAT,
    prediccion FLOAT
)
'''
cursor.execute(tabla_sql)
connection.commit()

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

        df_selected['Score'] = data['Score']

        df_input = df_selected.drop(columns=['Score']) 
        prediccion = modelo.predict(df_input)
        print(f"Predicción: {prediccion[0]}")

        df_selected['Prediccion'] = prediccion[0]

        insert_query = '''
        INSERT INTO predicciones (
            country_or_region, region, gdp_per_capita, social_support, 
            healthy_life_expectancy, freedom_to_make_life_choices, 
            perceptions_of_corruption, generosity, dystopia_residual, score, prediccion
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        '''
        
        row_values = tuple(df_selected.iloc[0].values)
        cursor.execute(insert_query, row_values)
        connection.commit()
        
finally:
    consumer.close()
    cursor.close()
    connection.close()
