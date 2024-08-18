import tkinter as tk
import datetime
from tkinter import messagebox, ttk, simpledialog
from Usuarios.usuario import Usuario
from Clientes.cliente import Cliente
from Empleados.empleado import Empleado
from Productos.producto import Producto 
from DetalleTicket.detalleticket import DetalleTicket 
from Tickets.ticket import Ticket


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("app-POS-AXOL")

        # Vincular las teclas Ctrl + '+' y Ctrl + '-'
        self.root.bind("<Control-plus>", self.zoom)
        self.root.bind("<Control-minus>", self.backzoom)

        # Vincular Ctrl + Scroll
        self.root.bind("<Control-MouseWheel>", self.zoom_scroll)

        # Crear un contenedor para la pantalla de inicio de sesión
        self.frame = tk.Frame(root)
        self.frame.pack(pady=20, padx=20)

        # Pantalla de inicio de sesión
        self.show_login()

    def zoom_scroll(self, event):
        if event.delta > 0:
            self.zoom(event)
        else:
            self.backzoom(event)

    def zoom(self, event):
        current_scale = self.root.tk.call('tk', 'scaling')
        new_scale = current_scale + 0.1
        self.root.tk.call('tk', 'scaling', new_scale)

    def backzoom(self, event):
        current_scale = self.root.tk.call('tk', 'scaling')
        new_scale = max(0.1, current_scale - 0.1)  # Evitar escala negativa
        self.root.tk.call('tk', 'scaling', new_scale)

    def show_login(self):
        self.clear_content_frame()

        tk.Label(self.frame, text="Username:").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self.frame, text="Contraseña:").grid(row=1, column=0, padx=10, pady=10)

        entry_username = tk.Entry(self.frame)
        entry_password = tk.Entry(self.frame, show="*")

        entry_username.grid(row=0, column=1, padx=10, pady=10)
        entry_password.grid(row=1, column=1, padx=10, pady=10)

        def login():
            username = entry_username.get()
            contrasena = entry_password.get()
            usuario = Usuario.iniciar_sesion(username, contrasena)
            if usuario:
                messagebox.showinfo("Éxito", f"Bienvenido {usuario.nombre}")
                self.show_main_menu()  # Mostrar el menú principal tras iniciar sesión
            else:
                messagebox.showerror("Error", "Usuario o contraseña incorrectos")

        tk.Button(self.frame, text="Iniciar Sesión", command=login).grid(row=2, column=1, padx=10, pady=10)

    def show_main_menu(self):
        self.clear_content_frame()

        # Botones para las diferentes opciones del sistema
        tk.Button(self.frame, text="Gestionar Tickets", command=self.show_ticket_form).pack(pady=10)
        tk.Button(self.frame, text="Gestionar Clientes", command=self.show_client_management).pack(pady=10)
        tk.Button(self.frame, text="Gestionar Productos", command=self.show_product_management).pack(pady=10)
        tk.Button(self.frame, text="Cerrar Sesión", command=self.show_login).pack(pady=10)
    
    
#========== 
#Gestión Clientes
# ========#

    def show_client_management(self):
        self.clear_content_frame()

        # Frame para botones superiores
        button_frame = tk.Frame(self.frame)
        button_frame.pack(fill='x', pady=10)

        def edit_selected_client():
            selected_items = self.tree.selection()
            if len(selected_items) == 1:
                item = self.tree.item(selected_items[0])
                client_id = item['values'][0]  # Assuming the ID is in the first column
                self.show_edit_client(client_id)
            else:
                messagebox.showerror("Error", "Please select exactly one client to edit.")

        # Botones para agregar, editar, y eliminar clientes
        self.edit_button = tk.Button(button_frame, text="Editar Cliente", command=edit_selected_client, state='disabled')
        self.edit_button.pack(side='left', padx=5)

        self.delete_button = tk.Button(button_frame, text="Borrar Cliente", command=self.delete_selected_clients, state='disabled')
        self.delete_button.pack(side='left', padx=5)

        tk.Button(button_frame, text="Agregar Cliente", command=self.show_add_client).pack(side='left', padx=5)

        # Crear un Treeview para mostrar la lista de clientes
        columns = ('ID', 'Domicilio', 'Teléfono', 'Correo', 'RFC')
        self.tree = ttk.Treeview(self.frame, columns=columns, show='headings')

        # Definir los encabezados
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)

        # Agregar una barra de desplazamiento
        scrollbar = ttk.Scrollbar(self.frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Colocar el Treeview y la barra de desplazamiento
        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    # Función para manejar la selección de clientes
        def toggle_buttons(event):
            selected_items = self.tree.selection()
            if len(selected_items) == 1:
                self.edit_button.config(state='normal')
                self.delete_button.config(state='normal')
            elif len(selected_items) > 1:
                self.edit_button.config(state='disabled')
                self.delete_button.config(state='normal')
            else:   
                self.edit_button.config(state='disabled')
                self.delete_button.config(state='disabled')

        # Obtener y mostrar los clientes
        clientes = Cliente.get_all()
        if clientes:
            for cliente in clientes:
                self.tree.insert('', 'end', values=(
                    cliente.id,
                    cliente.domicilio,
                    cliente.telefono,
                    cliente.correo,
                    cliente.rfc
                ))

        # Configurar acción para manejar la selección de clientes
        self.tree.bind('<<TreeviewSelect>>', toggle_buttons)

        # Botón para volver al menú principal
        tk.Button(self.frame, text="Volver al Menú Principal", command=self.show_main_menu).pack(pady=10)



    def show_add_client(self):
        self.clear_content_frame()

        tk.Label(self.frame, text="Domicilio:").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self.frame, text="Teléfono:").grid(row=1, column=0, padx=10, pady=10)
        tk.Label(self.frame, text="Correo:").grid(row=2, column=0, padx=10, pady=10)
        tk.Label(self.frame, text="RFC:").grid(row=3, column=0, padx=10, pady=10)

        entry_domicilio = tk.Entry(self.frame)
        entry_telefono = tk.Entry(self.frame)
        entry_correo = tk.Entry(self.frame)
        entry_rfc = tk.Entry(self.frame)

        entry_domicilio.grid(row=0, column=1, padx=10, pady=10)
        entry_telefono.grid(row=1, column=1, padx=10, pady=10)
        entry_correo.grid(row=2, column=1, padx=10, pady=10)
        entry_rfc.grid(row=3, column=1, padx=10, pady=10)

        def add_client():
            domicilio = entry_domicilio.get()
            telefono = entry_telefono.get()
            correo = entry_correo.get()
            rfc = entry_rfc.get()
            nuevo_cliente = Cliente.create(domicilio, telefono, correo, rfc)
            if nuevo_cliente:
                messagebox.showinfo("Éxito", "Cliente agregado exitosamente")
            else:
                messagebox.showerror("Error", "No se pudo agregar el cliente")

        tk.Button(self.frame, text="Agregar Cliente", command=add_client).grid(row=4, column=1, padx=10, pady=10)
        tk.Button(self.frame, text="Volver", command=self.show_main_menu).grid(row=5, column=1, padx=10, pady=10)



    def delete_selected_clients(self):
        selected_items = self.tree.selection()
        if messagebox.askyesno("Confirmar eliminación", f"¿Estás seguro de que quieres eliminar los clientes seleccionados?"):
            for item in selected_items:
                client = self.tree.item(item, "values")
                cliente = Cliente.read(client[0])
                if cliente:
                    cliente.delete()
                self.tree.delete(item)

    def show_add_client(self):
        self.clear_content_frame()

        tk.Label(self.frame, text="Domicilio:").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self.frame, text="Teléfono:").grid(row=1, column=0, padx=10, pady=10)
        tk.Label(self.frame, text="Correo:").grid(row=2, column=0, padx=10, pady=10)
        tk.Label(self.frame, text="RFC:").grid(row=3, column=0, padx=10, pady=10)

        entry_domicilio = tk.Entry(self.frame)
        entry_telefono = tk.Entry(self.frame)
        entry_correo = tk.Entry(self.frame)
        entry_rfc = tk.Entry(self.frame)

        entry_domicilio.grid(row=0, column=1, padx=10, pady=10)
        entry_telefono.grid(row=1, column=1, padx=10, pady=10)
        entry_correo.grid(row=2, column=1, padx=10, pady=10)
        entry_rfc.grid(row=3, column=1, padx=10, pady=10)

        def add_client():
            domicilio = entry_domicilio.get()
            telefono = entry_telefono.get()
            correo = entry_correo.get()
            rfc = entry_rfc.get()
            nuevo_cliente = Cliente.create(domicilio, telefono, correo, rfc)
            if nuevo_cliente:
                messagebox.showinfo("Éxito", "Cliente agregado exitosamente")
                self.show_client_management()
            else:
                messagebox.showerror("Error", "No se pudo agregar el cliente")

        tk.Button(self.frame, text="Agregar Cliente", command=add_client).grid(row=4, column=1, padx=10, pady=10)
        tk.Button(self.frame, text="Volver", command=self.show_client_management).grid(row=5, column=1, padx=10, pady=10)

    def show_edit_client(self, client_id):
        self.clear_content_frame()

        # Obtener los datos actuales del cliente
        cliente = Cliente.read(client_id)
        if not cliente:
            messagebox.showerror("Error", "Cliente no encontrado")
            return

        tk.Label(self.frame, text="Domicilio:").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self.frame, text="Teléfono:").grid(row=1, column=0, padx=10, pady=10)
        tk.Label(self.frame, text="Correo:").grid(row=2, column=0, padx=10, pady=10)
        tk.Label(self.frame, text="RFC:").grid(row=3, column=0, padx=10, pady=10)

        entry_domicilio = tk.Entry(self.frame)
        entry_domicilio.insert(0, cliente.domicilio)
        entry_telefono = tk.Entry(self.frame)
        entry_telefono.insert(0, cliente.telefono)
        entry_correo = tk.Entry(self.frame)
        entry_correo.insert(0, cliente.correo)
        entry_rfc = tk.Entry(self.frame)
        entry_rfc.insert(0, cliente.rfc)

        entry_domicilio.grid(row=0, column=1, padx=10, pady=10)
        entry_telefono.grid(row=1, column=1, padx=10, pady=10)
        entry_correo.grid(row=2, column=1, padx=10, pady=10)
        entry_rfc.grid(row=3, column=1, padx=10, pady=10)

        def edit_client():
            cliente.domicilio = entry_domicilio.get()
            cliente.telefono = entry_telefono.get()
            cliente.correo = entry_correo.get()
            cliente.rfc = entry_rfc.get()
            cliente.update()
            messagebox.showinfo("Éxito", "Cliente actualizado exitosamente")

        tk.Button(self.frame, text="Guardar Cambios", command=edit_client).grid(row=4, column=1, padx=10, pady=10)
        tk.Button(self.frame, text="Volver", command=self.show_client_management).grid(row=5, column=1, padx=10, pady=10)

    
    #========== 
    #Gestión Productos
    # ========#

    def show_product_management(self):
        self.clear_content_frame()

        # Frame para botones superiores
        button_frame = tk.Frame(self.frame)
        button_frame.pack(fill='x', pady=10)

        def edit_selected_product():
            selected_items = self.tree.selection()
            if len(selected_items) == 1:
                item = self.tree.item(selected_items[0])
                product_id = item['values'][1]  # Assuming the ID is in the second column
                self.show_edit_product(product_id)
            else:
                messagebox.showerror("Error", "Please select exactly one product to edit.")

        # Botones para agregar, editar, e importar productos
        self.edit_button = tk.Button(button_frame, text="Editar Producto", command=edit_selected_product, state='disabled')
        self.edit_button.pack(side='left', padx=5)

        self.delete_button = tk.Button(button_frame, text="Borrar Producto", command=self.delete_selected_products, state='disabled')
        self.delete_button.pack(side='left', padx=5)

        tk.Button(button_frame, text="Agregar Producto", command=self.show_add_product).pack(side='left', padx=5)
        tk.Button(button_frame, text="Importar Productos", command=self.import_products).pack(side='left', padx=5)

        # Crear un Treeview para mostrar la lista de productos
        columns = ('Seleccionar', 'ID', 'Nombre', 'Stock', 'Precio Compra', 'Precio Venta')
        self.tree = ttk.Treeview(self.frame, columns=columns, show='headings')

        # Definir los encabezados
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)

        # Agregar una barra de desplazamiento
        scrollbar = ttk.Scrollbar(self.frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Colocar el Treeview y la barra de desplazamiento
        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Función para manejar la selección de productos
        def toggle_buttons(event):
            selected_items = self.tree.selection()
            if len(selected_items) == 1:
                self.edit_button.config(state='normal')
                self.delete_button.config(state='normal')
            elif len(selected_items) > 1:
                self.edit_button.config(state='disabled')
                self.delete_button.config(state='normal')
            else:
                self.edit_button.config(state='disabled')
                self.delete_button.config(state='disabled')

        # Obtener y mostrar los productos
        productos = Producto.get_all()
        if productos:
            for producto in productos:
                self.tree.insert('', 'end', values=(
                    False,  # Valor inicial para la casilla de selección
                    producto.id,
                    producto.nombre,
                    producto.stock,
                    producto.precio_compra,
                    producto.precio_venta
                ))

        # Configurar acción para manejar la selección de productos
        self.tree.bind('<<TreeviewSelect>>', toggle_buttons)

    # Botón para volver al menú principal
        tk.Button(self.frame, text="Volver al Menú Principal", command=self.show_main_menu).pack(pady=10)

    def show_edit_product(self, product_id):
        self.clear_content_frame()

        # Obtener el producto por su ID
        producto = Producto.get_by_id(product_id)
        if not producto:
            messagebox.showerror("Error", f"No se encontró el producto con ID {product_id}")
            return

        # Etiquetas y campos de entrada con valores actuales del producto
        tk.Label(self.frame, text="Nombre del Producto:").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self.frame, text="Precio de Venta:").grid(row=1, column=0, padx=10, pady=10)
        tk.Label(self.frame, text="Precio de Compra:").grid(row=2, column=0, padx=10, pady=10)
        tk.Label(self.frame, text="Stock:").grid(row=3, column=0, padx=10, pady=10)
        tk.Label(self.frame, text="Código de Barras:").grid(row=4, column=0, padx=10, pady=10)
        tk.Label(self.frame, text="Unidad de Medida:").grid(row=5, column=0, padx=10, pady=10)

        entry_nombre = tk.Entry(self.frame)
        entry_precio_venta = tk.Entry(self.frame)
        entry_precio_compra = tk.Entry(self.frame)
        entry_stock = tk.Entry(self.frame)
        entry_codigo_barras = tk.Entry(self.frame)
        entry_unidad_medida = tk.Entry(self.frame)

        # Insertar los valores actuales del producto en los campos de entrada
        entry_nombre.insert(0, producto.nombre)
        entry_precio_venta.insert(0, producto.precio_venta)
        entry_precio_compra.insert(0, producto.precio_compra if producto.precio_compra is not None else "")
        entry_stock.insert(0, producto.stock)
        entry_codigo_barras.insert(0, producto.codigo_barras if producto.codigo_barras is not None else "")
        entry_unidad_medida.insert(0, producto.unidad_medida if producto.unidad_medida is not None else "")

        entry_nombre.grid(row=0, column=1, padx=10, pady=10)
        entry_precio_venta.grid(row=1, column=1, padx=10, pady=10)
        entry_precio_compra.grid(row=2, column=1, padx=10, pady=10)
        entry_stock.grid(row=3, column=1, padx=10, pady=10)
        entry_codigo_barras.grid(row=4, column=1, padx=10, pady=10)
        entry_unidad_medida.grid(row=5, column=1, padx=10, pady=10)

        def save_product():
            producto.nombre = entry_nombre.get()
            producto.precio_venta = float(entry_precio_venta.get())
            producto.precio_compra = float(entry_precio_compra.get())
            producto.stock = int(entry_stock.get())
            producto.codigo_barras = entry_codigo_barras.get()
            producto.unidad_medida = entry_unidad_medida.get()

            if producto.save():
                messagebox.showinfo("Éxito", "Producto actualizado exitosamente")
                self.show_product_management()  # Actualizar la lista de productos
            else:
                messagebox.showerror("Error", "No se pudo actualizar el producto")

        tk.Button(self.frame, text="Guardar Cambios", command=save_product).grid(row=6, column=1, padx=10, pady=10)
        tk.Button(self.frame, text="Volver", command=self.show_product_management).grid(row=7, column=1, padx=10, pady=10)

    def delete_selected_products(self):
        # Confirmar eliminación y borrar productos seleccionados
        selected_items = self.tree.selection()
        if messagebox.askyesno("Confirmar eliminación", f"¿Estás seguro de que quieres eliminar los productos seleccionados?"):
            for item in selected_items:
                product = self.tree.item(item, "values")
                Producto.eliminar_producto(product[1])
                self.tree.delete(item)


    def show_add_product(self):
        self.clear_content_frame()

        tk.Label(self.frame, text="Nombre del Producto:").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self.frame, text="Precio de Venta:").grid(row=1, column=0, padx=10, pady=10)
        tk.Label(self.frame, text="Precio de Compra:").grid(row=2, column=0, padx=10, pady=10)
        tk.Label(self.frame, text="Stock:").grid(row=3, column=0, padx=10, pady=10)
        tk.Label(self.frame, text="Código de Barras:").grid(row=4, column=0, padx=10, pady=10)
        tk.Label(self.frame, text="Unidad de Medida:").grid(row=5, column=0, padx=10, pady=10)

        entry_nombre = tk.Entry(self.frame)
        entry_precio_venta = tk.Entry(self.frame)
        entry_precio_compra = tk.Entry(self.frame)
        entry_stock = tk.Entry(self.frame)
        entry_codigo_barras = tk.Entry(self.frame)
        entry_unidad_medida = tk.Entry(self.frame)

        entry_nombre.grid(row=0, column=1, padx=10, pady=10)
        entry_precio_venta.grid(row=1, column=1, padx=10, pady=10)
        entry_precio_compra.grid(row=2, column=1, padx=10, pady=10)
        entry_stock.grid(row=3, column=1, padx=10, pady=10)
        entry_codigo_barras.grid(row=4, column=1, padx=10, pady=10)
        entry_unidad_medida.grid(row=5, column=1, padx=10, pady=10)

        def add_product():
            nombre = entry_nombre.get()
            precio_venta = entry_precio_venta.get()
            precio_compra = entry_precio_compra.get()
            stock = entry_stock.get()
            codigo_barras = entry_codigo_barras.get()
            unidad_medida = entry_unidad_medida.get()

            # Validación simple de los campos
            if not nombre or not precio_venta or not stock:
                messagebox.showerror("Error", "Por favor, complete todos los campos obligatorios (Nombre, Precio de Venta, Stock)")
                return

            try:
                # Convertir los campos de precios y stock a números
                precio_venta = float(precio_venta)
                precio_compra = float(precio_compra) if precio_compra else None
                stock = int(stock)

                # Crear un nuevo objeto Producto y guardarlo en la base de datos
                nuevo_producto = Producto(
                    id=None,
                    nombre=nombre,
                    precio_venta=precio_venta,
                    precio_compra=precio_compra,
                    stock=stock,
                    codigo_barras=codigo_barras,
                    unidad_medida=unidad_medida
                )
                if nuevo_producto.save():
                    messagebox.showinfo("Éxito", "Producto agregado exitosamente")
                    self.show_product_management()  # Volver al menú de gestión de productos después de agregar el producto
                else:
                    messagebox.showerror("Error", "Hubo un problema al guardar el producto")

            except ValueError:
                messagebox.showerror("Error", "Por favor, ingrese valores válidos para Precio de Venta, Precio de Compra y Stock")

        tk.Button(self.frame, text="Agregar Producto", command=add_product).grid(row=6, column=1, padx=10, pady=10)
        tk.Button(self.frame, text="Volver", command=self.show_product_management).grid(row=7, column=1, padx=10, pady=10)

    def clear_content_frame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

    


    def import_products(self):
        # Aquí puedes implementar la lógica para importar productos
        messagebox.showinfo("Importar Productos", "Funcionalidad de importación no implementada")



    #=== Ticket===#

    def show_ticket_management(self):
        # Implementar la gestión de tickets aquí
        pass

    def show_ticket_form(self):
        self.clear_content_frame()
        tk.Label(self.frame, text="Formulario para Realizar Ticket").grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        tk.Label(self.frame, text="Buscar producto:").grid(row=1, column=0, padx=10, pady=10)
        entry_busqueda = tk.Entry(self.frame)
        entry_busqueda.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self.frame, text="Tipo de Pago:").grid(row=1, column=2, padx=10, pady=10)
        entry_tipo_pago = tk.Entry(self.frame)
        entry_tipo_pago.grid(row=1, column=3, padx=10, pady=10)

        # Crear un Treeview para mostrar los resultados de la búsqueda
        tree_busqueda = ttk.Treeview(self.frame, columns=('ID', 'Nombre', 'Precio', 'Stock'), show='headings', height=5)
        tree_busqueda.heading('ID', text='ID')
        tree_busqueda.heading('Nombre', text='Nombre')
        tree_busqueda.heading('Precio', text='Precio')
        tree_busqueda.heading('Stock', text='Stock')
        tree_busqueda.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

        # Crear un Treeview para mostrar los productos seleccionados
        tree_seleccionados = ttk.Treeview(self.frame, columns=('ID', 'Nombre', 'Precio', 'Cantidad', 'Subtotal'), show='headings', height=5)
        tree_seleccionados.heading('ID', text='ID')
        tree_seleccionados.heading('Nombre', text='Nombre')
        tree_seleccionados.heading('Precio', text='Precio')
        tree_seleccionados.heading('Cantidad', text='Cantidad')
        tree_seleccionados.heading('Subtotal', text='Subtotal')
        tree_seleccionados.grid(row=3, column=0, columnspan=4, padx=10, pady=10)

        # Label para mostrar el total acumulado
        total_label = tk.Label(self.frame, text="Total: $0.00")
        total_label.grid(row=4, column=0, columnspan=4, padx=10, pady=10)

        def actualizar_total():
            total = sum(float(tree_seleccionados.item(item)['values'][4]) for item in tree_seleccionados.get_children())
            total_label.config(text=f"Total: ${total:.2f}")

        def buscar_producto(event):
            busqueda = entry_busqueda.get()
            if len(busqueda) >= 3:
                # Limpiar resultados anteriores
                for i in tree_busqueda.get_children():
                    tree_busqueda.delete(i)
                
                # Buscar por nombre
                productos = Producto.buscar_productos_por_nombre(busqueda)
                
                # Si no se encuentra por nombre, buscar por código de barras
                if not productos:
                    producto = Producto.buscar_productos_por_codigo_barras(busqueda)
                    if producto:
                        productos = [producto]
                
                # Mostrar resultados en el Treeview
                for producto in productos:
                    tree_busqueda.insert('', 'end', values=(producto.id, producto.nombre, producto.precio_venta, producto.stock))

        entry_busqueda.bind('<KeyRelease>', buscar_producto)

        def seleccionar_producto():
            seleccion = tree_busqueda.selection()
            if not seleccion:
                messagebox.showerror("Error", "Por favor, seleccione un producto")
                return
            
            producto_id, nombre, precio, _ = tree_busqueda.item(seleccion[0])['values']
            
            # Pedir cantidad
            cantidad = simpledialog.askinteger("Cantidad", f"Ingrese la cantidad para {nombre}:", parent=self.frame)
            if cantidad is None or cantidad <= 0:
                return

            subtotal = cantidad * float(precio)
            tree_seleccionados.insert('', 'end', values=(producto_id, nombre, precio, cantidad, subtotal))

            # Actualizar total
            actualizar_total()

        tk.Button(self.frame, text="Seleccionar Producto", command=seleccionar_producto).grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        def realizar_ticket():
            if not tree_seleccionados.get_children():
                messagebox.showerror("Error", "No hay productos seleccionados")
                return

            tipo_pago = entry_tipo_pago.get()
            if not tipo_pago:
                messagebox.showerror("Error", "Por favor, ingrese el tipo de pago")
                return

            total = sum(float(tree_seleccionados.item(item)['values'][4]) for item in tree_seleccionados.get_children())
            ticket_id = Ticket.crear_ticket(fecha=datetime.datetime.now(), total=total, tipo_pago=tipo_pago)

            for item in tree_seleccionados.get_children():
                producto_id, _, precio_unitario, cantidad, _ = tree_seleccionados.item(item)['values']
                DetalleTicket.agregar_detalle_ticket(ticket_id, producto_id, cantidad, float(precio_unitario))

            messagebox.showinfo("Éxito", "Ticket realizado exitosamente")
            self.show_main_menu()  # Volver al menú principal después de crear el ticket

        tk.Button(self.frame, text="Realizar Ticket", command=realizar_ticket).grid(row=4, column=2, padx=10, pady=10)
        tk.Button(self.frame, text="Volver", command=self.show_main_menu).grid(row=4, column=3, padx=10, pady=10)



    
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
