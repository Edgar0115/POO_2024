import mysql.connector
from db_config import obtener_conexion

class Dueño:

    @staticmethod
    def registrar_dueño(nombre, apellidos, telefono, email):
        try:
            conexion = obtener_conexion()
            if conexion is not None:
                cursor = conexion.cursor()
                cursor.execute("INSERT INTO dueños (nombre, apellidos, telefono, email) VALUES (%s, %s, %s, %s)",
                            (nombre, apellidos, telefono, email))
                conexion.commit()
                return True
        except mysql.connector.Error as e:
            print(f"Error al registrar dueño: {e}")
            return False
        finally:
            if conexion is not None and conexion.is_connected():
                conexion.close()

    @staticmethod
    def mostrar_dueños():
        try:
            conexion = obtener_conexion()
            if conexion is not None:
                cursor = conexion.cursor()
                cursor.execute("SELECT * FROM dueños")
                dueños = cursor.fetchall()
                return dueños
        except mysql.connector.Error as e:
            print(f"Error al mostrar dueños: {e}")
            return []
        finally:
            if conexion is not None and conexion.is_connected():
                conexion.close()

    @staticmethod
    def obtener_dueño_por_mascota(mascota_id):
        try:
            conexion = obtener_conexion()
            if conexion is not None:
                cursor = conexion.cursor()
                cursor.execute("SELECT dueños.* FROM dueños JOIN mascotas ON dueños.id = mascotas.dueño_id WHERE mascotas.id = %s", (mascota_id,))
                dueño = cursor.fetchone()
                return dueño
        except mysql.connector.Error as e:
            print(f"Error al obtener dueño por mascota: {e}")
            return None
        finally:
            if conexion is not None and conexion.is_connected():
                conexion.close()
