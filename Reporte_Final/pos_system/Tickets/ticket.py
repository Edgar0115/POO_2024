from conexion import create_connection, close_connection

class Ticket:
    def __init__(self, id, fecha, total, tipo_pago, cliente_id=None, empleado_id=None):
        self.id = id
        self.fecha = fecha
        self.total = total
        self.tipo_pago = tipo_pago
        self.cliente_id = cliente_id
        self.empleado_id = empleado_id

    @staticmethod
    def crear_ticket(fecha, total, tipo_pago, cliente_id=None, empleado_id=None):
        cursor, connection = create_connection()
        query = """
        INSERT INTO ticket (fecha, total, tipo_pago, cliente_id, empleado_id)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (fecha, total, tipo_pago, cliente_id, empleado_id))
        connection.commit()
        ticket_id = cursor.lastrowid
        close_connection(connection, cursor)
        return ticket_id

    @staticmethod
    def obtener_ticket_por_id(ticket_id):
        cursor, connection = create_connection()
        query = "SELECT * FROM ticket WHERE id = %s"
        cursor.execute(query, (ticket_id,))
        data = cursor.fetchone()
        close_connection(connection, cursor)
        return Ticket(*data) if data else None

    def actualizar_ticket(self):
        cursor, connection = create_connection()
        query = """
        UPDATE ticket
        SET fecha = %s, total = %s, tipo_pago = %s, cliente_id = %s, empleado_id = %s
        WHERE id = %s
        """
        cursor.execute(query, (self.fecha, self.total, self.tipo_pago, self.cliente_id, self.empleado_id, self.id))
        connection.commit()
        close_connection(connection, cursor)

    def eliminar_ticket(self):
        cursor, connection = create_connection()
        query = "DELETE FROM ticket WHERE id = %s"
        cursor.execute(query, (self.id,))
        connection.commit()
        close_connection(connection, cursor)
