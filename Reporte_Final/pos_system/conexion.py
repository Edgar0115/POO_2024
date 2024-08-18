import mysql.connector

def create_connection():
    config = {
        'user': 'root',
        'password': '',
        'host': 'localhost',
        'database': 'bd_pos'
    }
    
    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        return cursor, connection
    except mysql.connector.Error as err:
        print(f"Error al conectar a la base de datos: {err}")
        return None, None

def close_connection(connection, cursor):
    if cursor:
        cursor.close()
    if connection:
        connection.close()
