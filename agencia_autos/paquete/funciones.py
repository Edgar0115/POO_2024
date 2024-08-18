import os
import platform

def borrarPantalla():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def esperarTecla():
    input("\nPresiona Enter para continuar...")
