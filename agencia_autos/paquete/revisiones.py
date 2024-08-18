from paquete.conexionBD import ConexionDB

class Revision:
    def __init__(self, no_revision, cambiofiltro=None, cambioaceite=None, cambiofrenos=None, otros=None, matricula=None):
        self.no_revision = no_revision
        self.cambiofiltro = cambiofiltro
        self.cambioaceite = cambioaceite
        self.cambiofrenos = cambiofrenos
        self.otros = otros
        self.matricula = matricula

    def insertar(self):
        conexion = ConexionDB().conectar()
        try:
            with conexion.cursor() as cursor:
                sql = "INSERT INTO revisiones (no_revision, cambiofiltro, cambioaceite, cambiofrenos, otros, matricula) VALUES (%s, %s, %s, %s, %s, %s)"
                valores = (self.no_revision, self.cambiofiltro, self.cambioaceite, self.cambiofrenos, self.otros, self.matricula)
                cursor.execute(sql, valores)
                conexion.commit()
        finally:
            conexion.close()

    @staticmethod
    def consultar():
        conexion = ConexionDB().conectar()
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM revisiones")
                listaRevisiones = cursor.fetchall()
                listaFormateada_revisiones = []
                for revision in listaRevisiones:
                    no_revision, cambiofiltro, cambioaceite, cambiofrenos, otros, matricula = revision
                    revision_str = f"Numero de Revision: {no_revision}\nCambio de filtro: {cambiofiltro}\nCambio de aceite : {cambioaceite}\nCambio de frenos: {cambiofrenos}\nOtros: {otros}\nMatricula: {matricula}\n"
                    listaFormateada_revisiones.append(revision_str)
        finally:
            conexion.close()
        return listaFormateada_revisiones

    @staticmethod
    def actualizar(no_revision, cambiofiltro=None, cambioaceite=None, cambiofrenos=None, otros=None, matricula=None):
        set_clause = []
        valores = []

        if cambiofiltro:
            set_clause.append("cambiofiltro = %s")
            valores.append(cambiofiltro)
        if cambioaceite:
            set_clause.append("cambioaceite = %s")
            valores.append(cambioaceite)
        if cambiofrenos:
            set_clause.append("cambiofrenos = %s")
            valores.append(cambiofrenos)
        if otros:
            set_clause.append("otros = %s")
            valores.append(otros)
        if matricula:
            set_clause.append("matricula = %s")
            valores.append(matricula)

        if not set_clause:
            raise ValueError("No se proporcionaron valores para actualizar.")

        set_clause_str = ", ".join(set_clause)
        sql = f"UPDATE revisiones SET {set_clause_str} WHERE no_revision = %s"
        valores.append(no_revision)

        conexion = ConexionDB().conectar()
        try:
            with conexion.cursor() as cursor:
                cursor.execute(sql, tuple(valores))
                conexion.commit()
        finally:
            conexion.close()

    @staticmethod
    def eliminar(no_revision):
        sql = "DELETE FROM revisiones WHERE no_revision = %s"
        conexion = ConexionDB().conectar()
        try:
            with conexion.cursor() as cursor:
                cursor.execute(sql, (no_revision,))
                conexion.commit()
        finally:
            conexion.close()
