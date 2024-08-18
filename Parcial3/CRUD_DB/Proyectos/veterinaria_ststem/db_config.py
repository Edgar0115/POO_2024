import mysql.connector
from mysql.connector import Error

def obtener_conexion():
    try:
        conexion = mysql.connector.connect(
            host='localhost',      
            user='root',
            password='',
            database='veterinaria'
        )
        if conexion.is_connected():
            print("Conexión a la base de datos MySQL exitosa")
            return conexion
    except Error as e:
        print(f"Error al conectar con MySQL: {e}")
        return None

def crear_base_de_datos():
    try:
        conexion = obtener_conexion()
        if conexion is not None:
            cursor = conexion.cursor()

            cursor.execute('''CREATE TABLE IF NOT EXISTS dueños (
                                id INT AUTO_INCREMENT PRIMARY KEY,
                                nombre VARCHAR(100) NOT NULL,
                                apellidos VARCHAR(100) NOT NULL,
                                telefono VARCHAR(20) NOT NULL,
                                email VARCHAR(100) NOT NULL UNIQUE);''')

            cursor.execute('''CREATE TABLE IF NOT EXISTS mascotas (
                                id INT AUTO_INCREMENT PRIMARY KEY,
                                nombre VARCHAR(100) NOT NULL,
                                especie VARCHAR(50) NOT NULL,
                                raza VARCHAR(50) NOT NULL,
                                edad INT NOT NULL,
                                dueño_id INT NOT NULL,
                                FOREIGN KEY (dueño_id) REFERENCES dueños(id));''')

            cursor.execute('''CREATE TABLE IF NOT EXISTS citas (
                                id INT AUTO_INCREMENT PRIMARY KEY,
                                mascota_id INT NOT NULL,
                                fecha DATE NOT NULL,
                                hora TIME NOT NULL,
                                FOREIGN KEY (mascota_id) REFERENCES mascotas(id));''')

            conexion.commit()
    except Error as e:
        print(f"Error al crear la base de datos: {e}")
    finally:
        if conexion is not None and conexion.is_connected():
            conexion.close()
