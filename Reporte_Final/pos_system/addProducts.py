from Productos.producto import Producto  # Asegúrate de que la ruta de importación es correcta

def agregar_productos_papeleria():
    productos = [
        ("Cuaderno", 50.00, 30.00, 100, "1234567890123", "Unidad"),
        ("Bolígrafo", 10.00, 5.00, 200, "2345678901234", "Unidad"),
        ("Lápiz", 5.00, 2.00, 150, "3456789012345", "Unidad"),
        ("Marcador", 20.00, 12.00, 80, "4567890123456", "Unidad"),
        ("Goma", 7.00, 3.50, 120, "5678901234567", "Unidad"),
        ("Tijeras", 15.00, 8.00, 50, "6789012345678", "Unidad"),
        ("Regla", 12.00, 6.00, 70, "7890123456789", "Unidad"),
        ("Carpeta", 25.00, 15.00, 90, "8901234567890", "Unidad"),
        ("Pegamento", 8.00, 4.00, 110, "9012345678901", "Unidad"),
        ("Calculadora", 35.00, 20.00, 40, "0123456789012", "Unidad"),
        ("Archivo", 18.00, 10.00, 60, "1234567890124", "Unidad"),
        ("Papel A4", 50.00, 25.00, 200, "2345678901235", "Paquete"),
        ("Cuaderno Espiral", 60.00, 35.00, 90, "3456789012346", "Unidad"),
        ("Rotulador", 22.00, 14.00, 70, "4567890123457", "Unidad"),
        ("Pegatinas", 5.00, 2.50, 150, "5678901234568", "Paquete"),
        ("Cinta Adhesiva", 10.00, 6.00, 100, "6789012345679", "Unidad"),
        ("Clip", 3.00, 1.50, 200, "7890123456790", "Paquete"),
        ("Engrapadora", 30.00, 18.00, 60, "8901234567891", "Unidad"),
        ("Pinceles", 12.00, 7.00, 80, "9012345678902", "Juego"),
        ("Estuche", 25.00, 15.00, 40, "0123456789013", "Unidad"),
        ("Cartera de Notas", 20.00, 12.00, 50, "1234567890125", "Unidad")
    ]

    for nombre, precio_venta, precio_compra, stock, codigo_barras, unidad_medida in productos:
        producto = Producto(
            id=None,  # El ID será asignado automáticamente en la base de datos
            nombre=nombre,
            precio_venta=precio_venta,
            precio_compra=precio_compra,
            stock=stock,
            codigo_barras=codigo_barras,
            unidad_medida=unidad_medida
        )
        if producto.save():
            print(f"Producto '{nombre}' agregado exitosamente.")
        else:
            print(f"Error al agregar el producto '{nombre}'.")

if __name__ == "__main__":
    agregar_productos_papeleria()
