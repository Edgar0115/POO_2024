#una función es un conjunto de instrucciones agrupadas bao un nombre en particulas como un programa más pqueño que comple una función especifica, la función se puede reutilizar con el simple hecho de incovarla es decir mandarla a llamar

#Sintaxis:
def nombredeMiFuncion():
    #bloque o conjunto de intrucciónes
    print("bloque o conjunto de intrucciónes")

nombredeMiFuncion()

#las funciones puedes ser de 4 tipos
#1.- Funciones que no reciben parametros y no regresa valor
#2.- funciones que no recibe parametro y regresa valor
#3.- funciones que no recibe parametro y NO regresa valor
#4.- funciones que recibe parametro y regresa valor

#Ejemplo 1 - crear una función para imprimir nombres de personas
def solicitarNombre():
    nombre=input("Ingresa el nombre completo: ")

solicitarNombre()

#Ejemplo 2 - Realizar sumatoria (No recibe parametro pero regresa valor)
def suma():
    n1=int(input("Número #1: "))
    n2=int(input("Número #2: "))
    suma = n1+n2
    print(f"La suma de los números es {suma}")

suma()


#Ejemplo 3 - Sumar números (No recibe parametro pero regresa valor)

def suma():
    n1=int(input("Número #1: "))
    n2=int(input("Número #2: "))
    suma = n1+n2
    return suma

resultado_suma=suma()
print(f"La suma de los números es {suma()}")
print(f"La suma de los números es {resultado_suma}")


#Ejmplo 4 - Realizar suma
#funciones que recibe parametro y NO regresa valor

def suma(n1,n2):
    suma = n1+n2
    print(suma)

n1=int(input("Número #1: "))
n2=int(input("Número #2: "))
suma(n1,n2)


#Ejmplo 5 - Realizar suma
#funciones que recibe parametro y regresa valor

def suma(n1,n2):
    suma = n1+n2
    return suma

n1=int(input("Número #1: "))
n2=int(input("Número #2: "))
suma(n1,n2)



#Ejemplo - Tarea
#Crear un programa que solicite a traves de una función la siguiente información
#Nombre de paciente
#Edad
#Estatura
#Tipo de sangre
#Utilzar los 4 tipos de funciónes

def infoPaciente():
    nombre = input("Escribe el nombre del paciente")
    edad = input("Escribe la edad del paciente")
    eatatura = input("Escribe la  estatura del paciente")
    tipoSangre = input("Escribe el tipo de sangre del paciente")
    return(f"Nombre: ")


valor= infoPaciente()
#Recibe parametros pero no regresa valor
def infoPaciente2(nom, edad, est, sandre):
    return