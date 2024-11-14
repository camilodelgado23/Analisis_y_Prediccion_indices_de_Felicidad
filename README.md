# workshop3 :file_folder:

## Por: Camilo Jose Delgado Bolaños - 2225337 

En este workshop se recibieron 5 datasets que contienen informacion relacionadas con la felicidad o bienestar en varios países o regiones. a estos datos se les realizo un E.D.A para limpiar y analizar  su contenido y posterior uso para realizar un modelo de regrecion usando una división de datos del 70-30 (70% para entrenamiento - 30% para pruebas), se transmiten los datos transformados por medio de kafka, y se utiliza el modelo para predecir el índice de felicidad, luego se Almacenaron en una base de datos las predicciones con los respectivos insumos. 

## Herramientas Usadas :wrench:

- Python: 
    - Python Scripting: Para automatizar tareas como la inserción de datos en bases de datos, y la exportación de archivos.
    - Visual Studio Code (VS Code): Como entorno para escribir y ejecutar código Python.
    - Jupyter Notebook: Para desarrollo interactivo de código, exploración de datos, y ejecución de scripts.
    - Virtual Environment (venv): Para gestionar dependencias y aislar el entorno de desarrollo.

- MySQL:
    - MySQL Workbench: Para gestión y administración de bases de datos MySQL.

- Git: Para control de versiones y seguimiento de cambios en el proyecto.
- GitHub: Para alojar el repositorio del proyecto, gestionar el control de versiones, y colaborar en el desarrollo del proyecto.
- Power BI: Para la visualizacion de Datos.

## Instrucciones para la ejecucion :bookmark_tabs:

### Requerimientos 

- Python: https://www.python.org/downloads/
- MySQL: https://dev.mysql.com/downloads/mysql/
- PowerBI: https://www.microsoft.com/es-es/download/details.aspx?id=58494
- MySQL Workbench(Opcional): https://dev.mysql.com/downloads/workbench/

Clonamos el repositorio en nuestro entorno 

```bash
  git clone https://github.com/camilodelgado23/workshop__1.git
```
Vamos al repositorio clonado 

```bash
  cd workshop1
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
  CREATE SCHEMA workshop1;
```
Creamos el archivo credentials.py donde almacenaremos las credenciales para conectarnos a la Base de Datos, puede seguir la siguiente estructura para ese archivo:

```bash
  DB_HOST = 'tu_host'
  DB_USER = 'tu_usuario'
  DB_PASSWORD = 'tu_contraseña'
  DB_NAME = 'tu_Base_Datos'
```
Podemos probar si las credenciales son correctas ejecutando nuestro archivo conexion.py.
