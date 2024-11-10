import pandas as pd
from sklearn.preprocessing import LabelEncoder
import joblib  # Para cargar el modelo

# Cargar el modelo entrenado
modelo = joblib.load('Model/random_forest_model.pkl')

# Suponiendo que df es el DataFrame que contiene los datos para predecir
df = pd.read_csv('Data\\datos_felicidad_total.csv')  # Usar \\ en la ruta

# Lista de las columnas que el modelo espera (sin 'Score')
columnas_modelo = ['Country or region', 'Region', 'GDP per capita', 'Social support', 
                   'Healthy life expectancy', 'Freedom to make life choices', 
                   'Perceptions of corruption', 'Generosity', 'Dystopia_Residual']

# Asegurarse de que df tenga solo las columnas correctas
df_selected = df[columnas_modelo]

# Si hay columnas categóricas, codificar (como se hizo durante el entrenamiento)
label_encoder = LabelEncoder()
df_selected.loc[:, 'Country or region'] = label_encoder.fit_transform(df_selected['Country or region'])
df_selected.loc[:, 'Region'] = label_encoder.fit_transform(df_selected['Region'])

# Hacer la predicción
prediccion = modelo.predict(df_selected)

# Imprimir o guardar la predicción
print(f"Predicción: {prediccion}")
