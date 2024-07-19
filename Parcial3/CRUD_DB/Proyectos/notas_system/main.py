from usuarios.usuario import Usuario
from notas.nota import Nota
import getpass
from funciones import *

import getpass


def menu_principal():
    while True:
        borrarPantalla()
        print("""
      .::  Menu Principal ::. 
          1.- Registro
          2.- Login
          3.- Salir 
          """)
        opcion = input("\t Elige una opción: ")

        if opcion == '1':
            borrarPantalla()
            print("\n \t ..:: Registro en el Sistema ::..")
            nombre = input("\t ¿Cual es tu nombre?: ")
            apellidos = input("\t ¿Cuales son tus apellidos?: ")
            email = input("\t Ingresa tu email: ")
            password = getpass.getpass("\t Ingresa tu contraseña: ")
            
            # Crear un nuevo usuario
            nuevo_usuario = Usuario(nombre, apellidos, email, password, "2024-01-01")
            Usuario.crear_usuario(nuevo_usuario)
            
            print("\n\tUsuario registrado exitosamente.")
            esperarTecla()

        elif opcion == '2':
            borrarPantalla()
            print("\n \t ..:: Inicio de Sesión ::..")     
            email = input("\t Ingresa tu E-mail: ")
            password = getpass.getpass("\t Ingresa tu Contraseña: ")

            # Verificar el login
            usuario = Usuario.obtener_usuario_por_email(email)
            if usuario and usuario['password'] == password:
                print("\n\tInicio de sesión exitoso.")
                usuario_id = usuario['id']
                nombre = usuario['nombre']
                apellidos = usuario['apellidos']
                esperarTecla()
                menu_notas(usuario_id, nombre, apellidos)
            else:
                print("\n\tCorreo electrónico o contraseña incorrectos.")
                esperarTecla()

        elif opcion == '3':
            print("\n\t.. ¡Gracias Bye! ...")
            break
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            esperarTecla()



def menu_notas(usuario_id, nombre, apellidos):
    while True:
        borrarPantalla()
        print(f"\n \t \t \t Bienvenido {nombre} {apellidos}, has iniciado sesión ...")
        print("""
                  \n \t 
                      .::  Menu Notas ::. 
                  1.- Crear 
                  2.- Mostrar
                  3.- Cambiar
                  4.- Eliminar
                  5.- Salir 
                  """)
        opcion = input("\t\t Elige una opción: ")

        if opcion == '1':
            borrarPantalla()
            print(f"\n \t .:: Crear Nota ::. ")
            titulo = input("\tTitulo: ")
            descripcion = input("\tDescripción: ")
            # Crear una nueva nota
            nueva_nota = Nota(usuario_id, titulo, descripcion, "2024-01-01")
            Nota.crear_nota(nueva_nota)
            print("\n\tNota creada exitosamente.")
            esperarTecla()

        elif opcion == '2':
            borrarPantalla()
            print(f"\n \t .:: Mostrar Notas ::. ")
            id = input("\t \t ID de la nota a mostrar: ")
            nota = Nota.obtener_nota(id)
            if nota:
                print(f"\nID: {nota['id']}\nUsuario ID: {nota['usuario_id']}\nTítulo: {nota['titulo']}\nDescripción: {nota['descripcion']}\nFecha: {nota['fecha']}")
            else:
                print("\n\tNo se encontró ninguna nota con ese ID.")
            esperarTecla()

        elif opcion == '3':
            borrarPantalla()
            print(f"\n \t .:: {nombre} {apellidos}, vamos a modificar una Nota ::. \n")
            id = input("\t \t ID de la nota a actualizar: ")
            titulo = input("\t Nuevo título: ")
            descripcion = input("\t Nueva descripción: ")
            nota_actualizada = Nota(usuario_id, titulo, descripcion, "2024-01-01")
            Nota.actualizar_nota(id, nota_actualizada)
            print("\n\tNota actualizada exitosamente.")
            esperarTecla()

        elif opcion == '4':
            borrarPantalla()
            print(f"\n \t .:: {nombre} {apellidos}, vamos a borrar una Nota ::. \n")
            id = input("\t \t ID de la nota a eliminar: ")
            Nota.eliminar_nota(id)
            print("\n\tNota eliminada exitosamente.")
            esperarTecla()

        elif opcion == '5':
            break

        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            esperarTecla()

if __name__ == "_main_":
    menu_principal()