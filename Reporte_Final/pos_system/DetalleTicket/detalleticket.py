from conexion import create_connection, close_connection

class DetalleTicket:
    def __init__(self, id, ticket_id, producto_id, cantidad, precio_unitario, subtotal):
        self.id = id
        self.ticket_id = ticket_id
        self.producto_id = producto_id
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.subtotal = subtotal

    @staticmethod
    def agregar_detalle_ticket(ticket_id, producto_id, cantidad, precio_unitario):
        subtotal = cantidad * precio_unitario
        cursor, connection = create_connection()
        query = """
        INSERT INTO detalleTicket (ticket_id, producto_id, cantidad, precio_unitario, subtotal)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (ticket_id, producto_id, cantidad, precio_unitario, subtotal))
        connection.commit()
        detalle_id = cursor.lastrowid
        close_connection(connection, cursor)
        return detalle_id
