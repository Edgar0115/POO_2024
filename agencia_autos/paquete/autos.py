from paquete.conexionBD import ConexionDB

class Auto:
    def __init__(self, matricula, marca, modelo, color, nif):
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.nif = nif

    def insertar(self):
        conexion = ConexionDB().conectar()
        try:
            with conexion.cursor() as cursor:
                # Verificar si el nif existe en la tabla clientes
                cursor.execute("SELECT 1 FROM clientes WHERE nif = %s", (self.nif,))
                if cursor.fetchone() is None:
                    # Si el nif no existe, insertarlo en la tabla clientes
                    cursor.execute("INSERT INTO clientes (nif, nombre) VALUES (%s, 'Nuevo Cliente')", (self.nif,))
                
                # Insertar el nuevo auto
                sql = "INSERT INTO autos (matricula, marca, modelo, color, nif) VALUES (%s, %s, %s, %s, %s)"
                valores = (self.matricula, self.marca, self.modelo, self.color, self.nif)
                cursor.execute(sql, valores)
                conexion.commit()
        finally:
            conexion.close()

    @staticmethod
    def consultar():
        conexion = ConexionDB().conectar()
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM autos")
                listaAutos = cursor.fetchall()
                listaFormateada_autos = []
                for auto in listaAutos:
                    matricula, marca, modelo, color, nif = auto
                    auto_str = f"Matrícula: {matricula}\nMarca: {marca}\nModelo: {modelo}\nColor: {color}\nNIF: {nif}\n"
                    listaFormateada_autos.append(auto_str)
        finally:
            conexion.close()
        return listaFormateada_autos

    @staticmethod
    def actualizar(matricula, marca=None, modelo=None, color=None, nif=None):
        set_clause = []
        valores = []

        if marca:
            set_clause.append("marca = %s")
            valores.append(marca)
        if modelo:
            set_clause.append("modelo = %s")
            valores.append(modelo)
        if color:
            set_clause.append("color = %s")
            valores.append(color)
        if nif:
            # Verificar si el nif existe en la tabla clientes
            conexion = ConexionDB().conectar()
            try:
                with conexion.cursor() as cursor:
                    cursor.execute("SELECT 1 FROM clientes WHERE nif = %s", (nif,))
                    if cursor.fetchone() is None:
                        raise ValueError(f"El NIF {nif} no existe en la tabla clientes.")
            finally:
                conexion.close()
            set_clause.append("nif = %s")
            valores.append(nif)

        if not set_clause:
            raise ValueError("No se proporcionaron valores para actualizar.")
        
        set_clause_str = ", ".join(set_clause)
        sql = f"UPDATE autos SET {set_clause_str} WHERE matricula = %s"
        valores.append(matricula)

        conexion = ConexionDB().conectar()
        try:
            with conexion.cursor() as cursor:
                cursor.execute(sql, tuple(valores))
                conexion.commit()
        finally:
            conexion.close()

    @staticmethod
    def eliminar(matricula):
        sql = "DELETE FROM autos WHERE matricula = %s"
        conexion = ConexionDB().conectar()
        try:
            with conexion.cursor() as cursor:
                cursor.execute(sql, (matricula,))
                conexion.commit()
        finally:
            conexion.close()

