from dueños import Dueño
from mascotas import Mascota
from citas import Cita
import getpass
from funciones import borrarPantalla, esperarTecla
from db_config import crear_base_de_datos

def mostrar_dueños():
    borrarPantalla()
    print("\n \t ..:: Lista de Dueños Registrados ::..")
    dueños = Dueño.mostrar_dueños()
    if len(dueños) > 0:
        for dueño in dueños:
            print(f"ID: {dueño[0]} | Nombre: {dueño[1]} {dueño[2]} | Email: {dueño[4]}")
    else:
        print("No hay dueños registrados.")
    esperarTecla()

def mostrar_mascotas():
    borrarPantalla()
    print("\n \t ..:: Lista de Mascotas Registradas ::..")
    mascotas = Mascota.mostrar_mascotas()
    if len(mascotas) > 0:
        for mascota in mascotas:
            print(f"ID: {mascota[0]} | Nombre: {mascota[1]} | Especie: {mascota[2]} | Raza: {mascota[3]}")
    else:
        print("No hay mascotas registradas.")
    esperarTecla()

def mostrar_dueño_y_cita_de_mascota():
    borrarPantalla()
    print("\n \t ..:: Información del Dueño y Cita de la Mascota ::..")
    mascota_id = input("\t Ingresa el ID de la mascota: ")
    dueño = Dueño.obtener_dueño_por_mascota(mascota_id)
    cita = Cita.obtener_cita_por_mascota(mascota_id)
    if dueño:
        print(f"\nDueño de la Mascota ID: {mascota_id}")
        print(f"ID: {dueño[0]} | Nombre: {dueño[1]} {dueño[2]} | Email: {dueño[4]}")
    else:
        print("\nNo se encontró el dueño de la mascota.")

    if cita:
        print("\nCita de la Mascota:")
        print(f"ID Cita: {cita[0]} | Fecha: {cita[2]} | Hora: {cita[3]}")
    else:
        print("\nNo se encontró una cita para la mascota.")
    esperarTecla()

def menu_principal():
    crear_base_de_datos()  # Crear la base de datos si no existe
    while True:
        borrarPantalla()
        print("""
      .::  Menu Principal ::. 
          1.- Registro de Dueño
          2.- Registro de Mascota
          3.- Agendar Cita
          4.- Mostrar Citas
          5.- Mostrar Dueños y Mascotas
          6.- Mostrar Dueño y Cita de Mascota
          7.- Salir 
          """)
        opcion = input("\t Elige una opción: ").upper()

        if opcion == '1' or opcion == "REGISTRO DUEÑO":
            borrarPantalla()
            print("\n \t ..:: Registro de Dueño ::..")
            nombre = input("\t ¿Cuál es tu nombre?: ")
            apellidos = input("\t ¿Cuáles son tus apellidos?: ")
            telefono = input("\t Ingresa tu teléfono: ")
            email = input("\t Ingresa tu email: ")
            resultado = Dueño.registrar_dueño(nombre, apellidos, telefono, email)
            if resultado:
                print(f"\n\t {nombre} {apellidos}, se registró correctamente.")
            else:
                print(f"\n\t ** Por favor intente de nuevo, no fue posible insertar el registro ** ...")  
            esperarTecla()

        elif opcion == '2' or opcion == "REGISTRO MASCOTA":
            borrarPantalla()
            print("\n \t ..:: Registro de Mascota ::..")
            nombre = input("\t ¿Cuál es el nombre de la mascota?: ")
            especie = input("\t ¿Cuál es la especie (perro/gato/etc.)?: ")
            raza = input("\t ¿Cuál es la raza?: ")
            edad = input("\t ¿Cuál es la edad (en años)?: ")
            dueño_id = input("\t ID del Dueño: ")
            resultado = Mascota.registrar_mascota(nombre, especie, raza, edad, dueño_id)
            if resultado:
                print(f"\n\t {nombre}, se registró correctamente como mascota.")
            else:
                print(f"\n\t ** Por favor intente de nuevo, no fue posible insertar el registro ** ...")  
            esperarTecla()

        elif opcion == '3' or opcion == "AGENDAR CITA":
            borrarPantalla()
            print("\n \t ..:: Agendar Cita ::..")
            mascota_id = input("\t ID de la mascota: ")
            fecha = input("\t Fecha de la cita (YYYY-MM-DD): ")
            hora = input("\t Hora de la cita (HH:MM): ")
            resultado = Cita.agendar_cita(mascota_id, fecha, hora)
            if resultado:
                print(f"\n\t Cita agendada correctamente para la mascota ID: {mascota_id}.")
            else:
                print(f"\n\t ** No fue posible agendar la cita ... vuelva a intentarlo **...")
            esperarTecla()

        elif opcion == '4' or opcion == "MOSTRAR CITAS":
            borrarPantalla()
            citas = Cita.mostrar_citas()
            if len(citas) > 0:
                print(f"\n\t Citas agendadas: ")
                for cita in citas:
                    print(f"\nID: {cita[0]} | Mascota ID: {cita[1]} | Fecha: {cita[2]} | Hora: {cita[3]}")
            else:
                print(f"\n \t \t** No existen citas agendadas ... **...")
            esperarTecla()

        elif opcion == '5' or opcion == "MOSTRAR":
            borrarPantalla()
            print("""
                  .::  Mostrar Información ::. 
                  1.- Mostrar Dueños
                  2.- Mostrar Mascotas
                  3.- Volver al Menú Principal
                  """)
            subopcion = input("\t Elige una opción: ").upper()
            if subopcion == '1' or subopcion == "DUEÑOS":
                mostrar_dueños()
            elif subopcion == '2' or subopcion == "MASCOTAS":
                mostrar_mascotas()
            elif subopcion == '3' or subopcion == "VOLVER":
                continue
            else:
                print("\n \t \t Opción no válida. Intenta de nuevo.")
                esperarTecla()

        elif opcion == '6' or opcion == "MOSTRAR DUEÑO Y CITA":
            mostrar_dueño_y_cita_de_mascota()

        elif opcion == '7' or opcion == "SALIR":
            print("\n\t.. ¡Gracias, adiós! ...")
            break

        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            esperarTecla()

if __name__ == "__main__":
    menu_principal()
