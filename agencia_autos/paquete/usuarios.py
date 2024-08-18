from paquete.conexionBD import ConexionDB
import hashlib

class Usuarios:
    def __init__(self, id=None, nombre=None, apellido=None, email=None, password=None):
        self.nif = id
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.password = self.hash_password(password) if password else None

    def hash_password(self, contrasena):
        return hashlib.sha256(contrasena.encode()).hexdigest()

    def insertar(self):
        conexion = ConexionDB().conectar()
        try:
            with conexion.cursor() as cursor:
                sql = "INSERT INTO usuarios (id, nombre, apellido, email, password) VALUES (%s, %s, %s, %s, %s)"
                valores = (self.nif, self.nombre, self.apellido, self.email, self.password)
                cursor.execute(sql, valores)
                conexion.commit()
        finally:
            conexion.close()

    @staticmethod
    def login(email, contrasena):
        conexion = ConexionDB().conectar()
        try:
            with conexion.cursor() as cursor:
                sql = "SELECT id, nombre, apellido, email FROM usuarios WHERE email = %s AND password = %s"
                hashed_password = hashlib.sha256(contrasena.encode()).hexdigest()
                cursor.execute(sql, (email, hashed_password))
                usuario = cursor.fetchone()
                if usuario:
                    print("Login exitoso.")
                    return usuario  # Puedes retornar el usuario si deseas utilizarlo
                else:
                    print("Correo o contraseña incorrectos.")
                    return None
        finally:
            conexion.close()
