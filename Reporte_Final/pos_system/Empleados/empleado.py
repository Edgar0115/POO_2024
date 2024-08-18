from conexion import create_connection, close_connection

class Empleado:
    def __init__(self, id, usuario_id):
        self.id = id
        self.usuario_id = usuario_id

    @staticmethod
    def agregar_empleado(usuario_id):
        cursor, connection = create_connection()
        if cursor and connection:
            query = "INSERT INTO empleados (usuario_id) VALUES (%s)"
            cursor.execute(query, (usuario_id,))
            connection.commit()

            id_empleado = cursor.lastrowid
            nuevo_empleado = Empleado(id_empleado, usuario_id)
            print("Empleado agregado exitosamente.")
            close_connection(connection, cursor)
            return nuevo_empleado
        else:
            print("No se pudo establecer la conexión con la base de datos.")
            return None

    @staticmethod
    def obtener_empleado_por_id(id_empleado):
        cursor, connection = create_connection()
        if cursor and connection:
            query = "SELECT id, usuario_id FROM empleados WHERE id = %s"
            cursor.execute(query, (id_empleado,))
            empleado_data = cursor.fetchone()
            close_connection(connection, cursor)
            if empleado_data:
                return Empleado(*empleado_data)
            else:
                print("Empleado no encontrado.")
                return None
        else:
            print("No se pudo establecer la conexión con la base de datos.")
            return None
