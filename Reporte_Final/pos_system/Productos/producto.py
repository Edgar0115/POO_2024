from conexion import create_connection, close_connection

class Producto:
    def __init__(self, id, nombre, precio_venta, precio_compra=None, stock=0, codigo_barras=None, unidad_medida=None):
        self.id = id
        self.nombre = nombre
        self.precio_venta = precio_venta
        self.precio_compra = precio_compra
        self.stock = stock
        self.codigo_barras = codigo_barras
        self.unidad_medida = unidad_medida

    @staticmethod
    def get_all():
        cursor, conn = create_connection()
        if cursor is None or conn is None:
            return []
        
        try:
            query = "SELECT id, nombre, precio_venta, precio_compra, stock, codigo_barras, unidad_medida FROM productos"
            cursor.execute(query)
            rows = cursor.fetchall()
            productos = []
            for row in rows:
                producto = Producto(
                    id=row[0], 
                    nombre=row[1], 
                    precio_venta=row[2], 
                    precio_compra=row[3], 
                    stock=row[4], 
                    codigo_barras=row[5], 
                    unidad_medida=row[6]
                )
                productos.append(producto)
            return productos
        except Exception as e:
            print(f"Error al obtener productos: {e}")
            return []
        finally:
            close_connection(conn, cursor)

    def save(self):
        cursor, conn = create_connection()
        if cursor is None or conn is None:
            return False
        
        try:
            if self.id is None:
                query = """INSERT INTO productos (nombre, precio_venta, precio_compra, stock, codigo_barras, unidad_medida) 
                           VALUES (%s, %s, %s, %s, %s, %s)"""
                cursor.execute(query, (self.nombre, self.precio_venta, self.precio_compra, self.stock, self.codigo_barras, self.unidad_medida))
                self.id = cursor.lastrowid
            else:
                query = """UPDATE productos 
                           SET nombre=%s, precio_venta=%s, precio_compra=%s, stock=%s, codigo_barras=%s, unidad_medida=%s 
                           WHERE id=%s"""
                cursor.execute(query, (self.nombre, self.precio_venta, self.precio_compra, self.stock, self.codigo_barras, self.unidad_medida, self.id))
            conn.commit()
            print(f"all good")
            return True
        except Exception as e:
            print(f"Error al guardar producto: {e}")
            return False
        finally:
            close_connection(conn, cursor)

    @staticmethod
    def eliminar_producto(id):
        cursor, conn = create_connection()
        if cursor is None or conn is None:
            return False
        
        try:
            query = "DELETE FROM productos WHERE id=%s"
            cursor.execute(query, (id,))
            conn.commit()
            return True
        except Exception as e:
            print(f"Error al eliminar producto: {e}")
            return False
        finally:
            close_connection(conn, cursor)

    @staticmethod
    def get_by_id(id):
        cursor, conn = create_connection()
        if cursor is None or conn is None:
            return None
        
        try:
            query = "SELECT id, nombre, precio_venta, precio_compra, stock, codigo_barras, unidad_medida FROM productos WHERE id=%s"
            cursor.execute(query, (id,))
            row = cursor.fetchone()
            if row:
                return Producto(
                    id=row[0], 
                    nombre=row[1], 
                    precio_venta=row[2], 
                    precio_compra=row[3], 
                    stock=row[4], 
                    codigo_barras=row[5], 
                    unidad_medida=row[6]
                )
            return None
        except Exception as e:
            print(f"Error al obtener producto: {e}")
            return None
        finally:
            close_connection(conn, cursor)
    

    @staticmethod
    def buscar_productos_por_nombre(busqueda):
        try:
            cursor, conn = create_connection()
            query = "SELECT id, nombre, precio_venta, stock FROM productos WHERE nombre LIKE %s"
            cursor.execute(query, (f"%{busqueda}%",))
            rows = cursor.fetchall()
            return [Producto(id=row[0], nombre=row[1], precio_venta=row[2], precio_compra=None, stock=row[3], codigo_barras=None, unidad_medida=None) for row in rows]
        except Exception as e:
            print(f"Error al buscar productos por nombre: {e}")
            return []
        finally:
            close_connection(conn, cursor)

    @staticmethod
    def buscar_productos_por_codigo_barras(busqueda):
        try:
            cursor, conn = create_connection()
            query = "SELECT id, nombre, precio_venta, stock FROM productos WHERE codigo_barras = %s"
            cursor.execute(query, (busqueda,))
            row = cursor.fetchone()
            if row:
                return Producto(id=row[0], nombre=row[1], precio_venta=row[2], precio_compra=None, stock=row[3], codigo_barras=None, unidad_medida=None)
            return None
        except Exception as e:
            print(f"Error al buscar producto por código de barras: {e}")
            return None
        finally:
            close_connection(conn, cursor)

 
