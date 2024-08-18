import mysql.connector
from db_config import obtener_conexion

class Cita:

    @staticmethod
    def agendar_cita(mascota_id, fecha, hora):
        try:
            conexion = obtener_conexion()
            if conexion is not None:
                cursor = conexion.cursor()
                cursor.execute("INSERT INTO citas (mascota_id, fecha, hora) VALUES (%s, %s, %s)",
                               (mascota_id, fecha, hora))
                conexion.commit()
                return True
        except mysql.connector.Error as e:
            print(f"Error al agendar cita: {e}")
            return False
        finally:
            if conexion is not None and conexion.is_connected():
                conexion.close()

    @staticmethod
    def mostrar_citas():
        try:
            conexion = obtener_conexion()
            if conexion is not None:
                cursor = conexion.cursor()
                cursor.execute("SELECT * FROM citas")
                citas = cursor.fetchall()
                return citas
        except mysql.connector.Error as e:
            print(f"Error al mostrar citas: {e}")
            return []
        finally:
            if conexion is not None and conexion.is_connected():
                conexion.close()

    @staticmethod
    def obtener_cita_por_mascota(mascota_id):
        try:
            conexion = obtener_conexion()
            if conexion is not None:
                cursor = conexion.cursor()
                cursor.execute("SELECT * FROM citas WHERE mascota_id = %s", (mascota_id,))
                cita = cursor.fetchone()
                return cita
        except mysql.connector.Error as e:
            print(f"Error al obtener cita por mascota: {e}")
            return None
        finally:
            if conexion is not None and conexion.is_connected():
                conexion.close()
