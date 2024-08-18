from paquete.conexionBD import ConexionDB

class Cliente:
    def __init__(self, nif, nombre=None, direccion=None, ciudad=None, tel=None):
        self.nif = nif
        self.nombre = nombre
        self.direccion = direccion
        self.ciudad = ciudad
        self.tel = tel

    def insertar(self):
        conexion = ConexionDB().conectar()
        try:
            with conexion.cursor() as cursor:
                sql = "INSERT INTO clientes (nif, nombre, direccion, ciudad, tel) VALUES (%s, %s, %s, %s, %s)"
                valores = (self.nif, self.nombre, self.direccion, self.ciudad, self.tel)
                cursor.execute(sql, valores)
                conexion.commit()
        finally:
            conexion.close()

    @staticmethod
    def consultar():
        conexion = ConexionDB().conectar()
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM clientes")
                listaClientes = cursor.fetchall()
                listaFormateada_clientes = []
                for cliente in listaClientes:
                    nif, nombre, direccion, ciudad, tel = cliente
                    cliente_str = f"Nif: {nif}\nNombre: {nombre}\nDireccion: {direccion}\nCiudad: {ciudad}\nTelefono: {tel}\n"
                    listaFormateada_clientes.append(cliente_str)
        finally:
            conexion.close()
        return listaFormateada_clientes

    @staticmethod
    def actualizar(nif, nombre=None, direccion=None, ciudad=None, tel=None):
        set_clause = []
        valores = []

        if nombre:
            set_clause.append("nombre = %s")
            valores.append(nombre)
        if direccion:
            set_clause.append("direccion = %s")
            valores.append(direccion)
        if ciudad:
            set_clause.append("ciudad = %s")
            valores.append(ciudad)
        if tel:
            set_clause.append("tel = %s")
            valores.append(tel)
        if not set_clause:
            raise ValueError("No se proporcionaron valores para actualizar.")

        set_clause_str = ", ".join(set_clause)
        sql = f"UPDATE clientes SET {set_clause_str} WHERE nif = %s"
        valores.append(nif)

        conexion = ConexionDB().conectar()
        try:
            with conexion.cursor() as cursor:
                cursor.execute(sql, tuple(valores))
                conexion.commit()
        finally:
            conexion.close()

    @staticmethod
    def eliminar(nif):
        sql = "DELETE FROM clientes WHERE nif = %s"
        conexion = ConexionDB().conectar()
        try:
            with conexion.cursor() as cursor:
                cursor.execute(sql, (nif,))
                conexion.commit()
        finally:
            conexion.close()
