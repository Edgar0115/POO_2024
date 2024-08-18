from conexion import create_connection, close_connection
from funciones import hash_password

class Usuario:
    def __init__(self, id, nombre, username, contrasena=None):
        self.id = id
        self.nombre = nombre
        self.username = username
        self.contrasena = hash_password(contrasena) if contrasena else None

    @staticmethod
    def iniciar_sesion(username, contrasena):
        cursor, connection = create_connection()
        if cursor and connection:
            query = "SELECT id, nombre, username, contrasena FROM usuarios WHERE username = %s"
            cursor.execute(query, (username,))
            usuario_data = cursor.fetchone()
            close_connection(connection, cursor)
            
            if usuario_data and usuario_data[3] == hash_password(contrasena):
                return Usuario(*usuario_data[:3])
            else:
                print("Username o contraseña incorrectos.")
                return None
        else:
            print("No se pudo establecer la conexión con la base de datos.")
            return None

    @staticmethod
    def registrarse(nombre, username, contrasena):
        cursor, connection = create_connection()
        if cursor and connection:
            # Verificar si el username ya está registrado
            query = "SELECT username FROM usuarios WHERE username = %s"
            cursor.execute(query, (username,))
            if cursor.fetchone():
                print("El username ya está registrado.")
                close_connection(connection, cursor)
                return None
            
            # Insertar el nuevo usuario en la base de datos
            query = """
            INSERT INTO usuarios (nombre, username, contrasena)
            VALUES (%s, %s, %s)
            """
            hashed_password = hash_password(contrasena)
            cursor.execute(query, (nombre, username, hashed_password))
            connection.commit()

            # Obtener el ID del nuevo usuario
            id_usuario = cursor.lastrowid

            # Crear una instancia de Usuario
            nuevo_usuario = Usuario(id_usuario, nombre, username, hashed_password)
            print("Registro exitoso.")
            close_connection(connection, cursor)
            return nuevo_usuario
        else:
            print("No se pudo establecer la conexión con la base de datos.")
            return None
