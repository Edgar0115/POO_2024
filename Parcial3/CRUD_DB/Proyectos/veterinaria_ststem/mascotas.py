import mysql.connector
from db_config import obtener_conexion

class Mascota:

    @staticmethod
    def registrar_mascota(nombre, especie, raza, edad, dueño_id):
        try:
            conexion = obtener_conexion()
            if conexion is not None:
                cursor = conexion.cursor()
                cursor.execute("INSERT INTO mascotas (nombre, especie, raza, edad, dueño_id) VALUES (%s, %s, %s, %s, %s)",
                            (nombre, especie, raza, edad, dueño_id))
                conexion.commit()
                return True
        except mysql.connector.Error as e:
            print(f"Error al registrar mascota: {e}")
            return False
        finally:
            if conexion is not None and conexion.is_connected():
                conexion.close()

    @staticmethod
    def mostrar_mascotas():
        try:
            conexion = obtener_conexion()
            if conexion is not None:
                cursor = conexion.cursor()
                cursor.execute("SELECT * FROM mascotas")
                mascotas = cursor.fetchall()
                return mascotas
        except mysql.connector.Error as e:
            print(f"Error al mostrar mascotas: {e}")
            return []
        finally:
            if conexion is not None and conexion.is_connected():
                conexion.close()
