from confluent_kafka import Producer
import pandas as pd
import json
import time
from sklearn.preprocessing import LabelEncoder

conf = {
    'bootstrap.servers': 'localhost:9092',  
}

producer = Producer(conf)

df = pd.read_csv('Data\\datos_felicidad_total.csv')

columnas_modelo = ['Country or region', 'Region', 'GDP per capita', 'Social support', 
                   'Healthy life expectancy', 'Freedom to make life choices', 
                   'Perceptions of corruption', 'Generosity', 'Dystopia_Residual']

df_selected = df[columnas_modelo]

label_encoder = LabelEncoder()
df_selected['Country or region'] = label_encoder.fit_transform(df_selected['Country or region'])
df_selected['Region'] = label_encoder.fit_transform(df_selected['Region'])

def delivery_report(err, msg):
    if err is not None:
        print(f"Mensaje fallido: {err}")
    else:
        print(f"Mensaje entregado a {msg.topic()} [{msg.partition()}]")

for index, row in df_selected.iterrows():
    data = row.to_dict()  
    producer.produce('datos_entrada', value=json.dumps(data).encode('utf-8'), callback=delivery_report)  
    print(f"Enviado: {data}")
    time.sleep(0.0) 

producer.flush()
