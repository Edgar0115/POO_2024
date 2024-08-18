from conexion import create_connection, close_connection

class Cliente:
    def __init__(self, id, domicilio, telefono, correo, rfc):
        self.id = id
        self.domicilio = domicilio
        self.telefono = telefono
        self.correo = correo
        self.rfc = rfc

    @classmethod
    def create(cls, domicilio, telefono, correo, rfc):
        try:
            cursor, conn = create_connection()  # Cambiado a cursor, conn
            query = """
                INSERT INTO clientes (domicilio, telefono, correo, rfc)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (domicilio, telefono, correo, rfc))
            conn.commit()
            new_id = cursor.lastrowid
            return cls(new_id, domicilio, telefono, correo, rfc)
        except Exception as e:
            print(f"Error al crear cliente: {e}")
        finally:
            close_connection(conn, cursor)

    @classmethod
    def read(cls, id):
        try:
            cursor, conn = create_connection()  # Cambiado a cursor, conn
            query = "SELECT * FROM clientes WHERE id = %s"
            cursor.execute(query, (id,))
            row = cursor.fetchone()
            if row:
                return cls(*row)
            else:
                print(f"Cliente con ID {id} no encontrado.")
        except Exception as e:
            print(f"Error al leer cliente: {e}")
        finally:
            close_connection(conn, cursor)

    def update(self):
        try:
            cursor, conn = create_connection()  # Cambiado a cursor, conn
            query = """
                UPDATE clientes
                SET domicilio = %s, telefono = %s, correo = %s, rfc = %s
                WHERE id = %s
            """
            cursor.execute(query, (self.domicilio, self.telefono, self.correo, self.rfc, self.id))
            conn.commit()
        except Exception as e:
            print(f"Error al actualizar cliente: {e}")
        finally:
            close_connection(conn, cursor)

    def delete(self):
        try:
            cursor, conn = create_connection()  # Cambiado a cursor, conn
            query = "DELETE FROM clientes WHERE id = %s"
            cursor.execute(query, (self.id,))
            conn.commit()
        except Exception as e:
            print(f"Error al eliminar cliente: {e}")
        finally:
            close_connection(conn, cursor)

    @staticmethod
    def get_all():
        cursor, conn = create_connection()
        if cursor is None or conn is None:
            return []
        
        try:
            query = "SELECT id, domicilio, telefono, correo, rfc FROM clientes"
            cursor.execute(query)
            rows = cursor.fetchall()
            clientes = []
            for row in rows:
                cliente = Cliente(
                    id=row[0], 
                    domicilio=row[1], 
                    telefono=row[2], 
                    correo=row[3], 
                    rfc=row[4]
                )
                clientes.append(cliente)
            return clientes
        except Exception as e:
            print(f"Error al obtener clientes: {e}")
            return []
        finally:
            close_connection(conn, cursor)
        
    
    

