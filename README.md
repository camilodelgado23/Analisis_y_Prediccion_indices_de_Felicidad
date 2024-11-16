# workshop3 :file_folder:

## Por: Camilo Jose Delgado Bolaños - 2225337 

En este workshop se recibieron 5 datasets que contienen informacion relacionadas con la felicidad o bienestar en varios países o regiones. a estos datos se les realizo un E.D.A para limpiar y analizar  su contenido y posterior uso para realizar un modelo de regrecion usando una división de datos del 70-30 (70% para entrenamiento - 30% para pruebas), se transmiten los datos transformados por medio de kafka, y se utiliza el modelo para predecir el índice de felicidad, luego se Almacenaron en una base de datos las predicciones con los respectivos insumos. 

## Estructura del Repositorio :closed_book:

La estructura del repositorio es la siguiente:

- **Data:** Carpeta Donde tendremos los archivos csv proporcionados, y el archivio concatenado.
    - **2015:** Dataset con los datos de indice de felicidad del año 2015 
    - **2016:** Dataset con los datos de indice de felicidad del año 2016 
    - **2017:** Dataset con los datos de indice de felicidad del año 2017 
    - **2018:** Dataset con los datos de indice de felicidad del año 2018 
    - **2019:** Dataset con los datos de indice de felicidad del año 2019 
    - **datos_felicidad_total**: archivo concatenado con los datos de indice de felicidad de los años 2015, 2016, 2017, 2018, 2019.
- **Database:** En esta carpeta tendremos las operaciones que realizamos en nuestra Base de Datos en este caso MySQL
    - **conexion_db.py:** En este archivo tenemos el script que con ayuda de la libreria MySQL connection nos conectamos a la Base de Datos de MySQL.
- **Kafka:** Carpeta donde tendremos las operaciones necesarias para hacer la parte de streaming de datos con la ayuda de kafka.
    - **consumidor:** archivo en donde se reciben los datos enviados por el productor y realiza las predicciones con la ayuda del modelo entrenado, y las almacena en la Base de Datos MySQL.
    - **feature_selection** archivo en donde se encuentran las caracteristicas usadas para el entrenamiento del modelo.
    - **productor:** archivo en donde se envian los mensajes al consumidor. 
- **Model:** En esta carpeta se almacena el modelo predictivo 
    - **random_forest_regressor** El modelo entrenado para predecir el indice de felicidad. 
- **Notebooks**: Carpeta en donde se almacenan todos los jupyter notebooks 
    - **E.D.A_datasets:** Jupyter Notebook en donde se realiza un E.D.A a los 5 archivos csv proporcionados, y en donde se realiza la concatenacion de estos en uno solo 
    - **model_training:** Jupyter Notebook en donde se realiza el entrenamiento del modelo predicctivo. 
- **.gitignore:** Archivo en donde colocamos los archivos que no queremos que se suban a nuestro repositorio de git hub como lo es nuestro entorno virtual o nuestro archivo en donde almacenamos las credenciales.
- **docker-compose.yml:** Archivo que levantara un entorno de Kafka en nuestra maquina local 
- **README.txt:** Archivo donde colocaremos una breve descripción de nuestro proyecto y donde se explica como ejecutar el workshop.
- **requirements.txt:** Archivo en donde colocamos las librerías/bibliotecas que usamos en nuestro entorno para el desarrollo del
workshop.

## Herramientas Usadas :wrench:

- Python: 
    - Python Scripting: Para automatizar tareas como la inserción de datos en bases de datos, y la exportación de archivos.
    - Visual Studio Code (VS Code): Como entorno para escribir y ejecutar código Python.
    - Jupyter Notebook: Para desarrollo interactivo de código, exploración de datos, y ejecución de scripts.
    - Virtual Environment (venv): Para gestionar dependencias y aislar el entorno de desarrollo.

- Docker: Para orquestar y configurar dos servicios relacionados con Apache Kafka
- ZooKeeper: Para configurar el servicio de coordinación que Apache Kafka que utiliza para la gestión de clústeres y la sincronización de datos.
- Kafka: Como broker para procesar y manejar mensajes.

- MySQL:
    - MySQL Workbench: Para gestión y administración de bases de datos MySQL.

- Git: Para control de versiones y seguimiento de cambios en el proyecto.
- GitHub: Para alojar el repositorio del proyecto, gestionar el control de versiones, y colaborar en el desarrollo del proyecto.
- Power BI: Para la visualizacion de Datos.

## Instrucciones para la ejecucion :bookmark_tabs:

### Requerimientos 

- Python: https://www.python.org/downloads/
- MySQL: https://dev.mysql.com/downloads/mysql/
- MySQL Workbench(Opcional): https://dev.mysql.com/downloads/workbench/
- Docker: https://www.docker.com/
- Kafka: https://kafka.apache.org/

Clonamos el repositorio en nuestro entorno 

```bash
  git clone https://github.com/camilodelgado23/workshop_3.git
```
Vamos al repositorio clonado 

```bash
  cd workshop3
```
##### Si desea puede usar un entorno virtual para gestionar dependencias de manera aislada  

Instalamos el entrono virtual 

```bash
  Python -m venv venv 
```
Iniciamos el entorno 

```bash
  .\venv\Scripts\Activate
```
Instalamos las librerias necesarias almacenadas en el archivo requirements.txt

```bash
  pip install -r requirements.txt
```
Creamos la Base de Datos en MySQL 

```bash
  CREATE SCHEMA workshop3;
```
Creamos el archivo credentials.py donde almacenaremos las credenciales para conectarnos a la Base de Datos, puede seguir la siguiente estructura para ese archivo:

```bash
  DB_HOST = 'tu_host'
  DB_USER = 'tu_usuario'
  DB_PASSWORD = 'tu_contraseña'
  DB_NAME = 'tu_Base_Datos'
```
Podemos probar si las credenciales son correctas ejecutando nuestro archivo conexion_db.py.

Para la ejecucion de la transmicion de datos por parte de kafka:

primero creamos un topic del Kafka que vamos a llamar mi_topic el cual se puede utilizar para enviar y recibir mensajes.

```bash
docker-compose exec kafka-test kafka-topics --create --topic mi_topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
```
Luego ejecutamos el docker que levantara los servicios 

```bash
docker-compose up -d
```
Se ejecutara primero el productor.py y luego el consumidor.py como se muestra en el siguiente video:

[![Watch the video](https://imagenes.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2Fb687bcac-6636-49ac-8ce3-1adf66aa571c%2F63584f9f-ed67-4dcf-a97c-d177d19daa3a%2Fimage.png?table=block&id=14038733-ed67-8050-8a00-f2c34df6323a&spaceId=b687bcac-6636-49ac-8ce3-1adf66aa571c&width=1420&userId=&cache=v2)](https://file.notion.so/f/f/b687bcac-6636-49ac-8ce3-1adf66aa571c/47f94739-db7a-4771-ad95-f06e4d630c30/2024-11-15_18-06-55.mkv?table=block&id=14038733-ed67-8079-aeb9-f0a28078a6cd&spaceId=b687bcac-6636-49ac-8ce3-1adf66aa571c&expirationTimestamp=1731816000000&signature=HgKrMUOV4g0PRmHHYYQf8yuI6oHZzqvk1DHBtQ80lNM)

## Para una correcta ejecucion :computer:

Primero puede ejecutar el jupyter notebook E.D.A_datasets para poder entender y comprender de una mejor manera el contenido de los Datasets, ademas de exportar el archivo csv de los 5 datasets concatenados, luego ejecutamos el jupyter notebook model_training donde se importa el dataset concatenado para seleccionar las caracteristicas para realizar  el entrenamiento del modelo dimecional que tiene como objetivo predecir el indice de felicidad, en este se exporta el modelo con mejores resultados, luego se ejecuta el productor.py que se encarga de enviar los mensajes al consumidor el cual realiza las predicciones con el modelo entrenado y los almacena en la Base de Datos MySQL. 

