import mysql.connector
from mysql.connector import Error
import sys
import os

# Añadir el directorio raíz al sys.path para permitir importaciones
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importar las credenciales
import credenciales as credenciales

def create_connection():
    """Create a database connection."""
    try:
        print("Attempting to connect to the database...")
        connection = mysql.connector.connect(
            host=credenciales.DB_HOST,
            user=credenciales.DB_USER,
            password=credenciales.DB_PASSWORD,
            database=credenciales.DB_NAME
        )
        if connection.is_connected():
            print('Connection to MySQL database established successfully.')
            return connection
        else:
            print('Failed to connect to MySQL database.')
            return None
    except Error as e:
        print(f'Error: {e}')
        return None

if __name__ == "__main__":
    create_connection()
