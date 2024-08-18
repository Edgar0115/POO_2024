import mysql.connector # type: ignore
from mysql.connector import Error # type: ignore

class ConexionDB:
    def __init__(self):
        
        self.config = {
            'user': 'root',          
            'password': '',          
            'host': 'localhost',
            'database': 'bd_agencia_autos'
        }
    
    def conectar(self):
        try:
            # Establecer la conexión
            conexion = mysql.connector.connect(**self.config)
            if conexion.is_connected():
                #print("Conexión exitosa!")
                return conexion
        except Error as e:
            print(f"Error al conectar a MySQL: {e}")
            raise

    def cerrar_conexion(self, conexion):
        if conexion.is_connected():
            conexion.close()
            print("Conexión cerrada.")
