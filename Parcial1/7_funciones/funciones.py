#una funcion es un conjunto de instrucciones agrupadas bajo un nombre en 
#particular como un programa mas pequeño que cumple una funcion especifica. La
#funcion se puede reutilizar con el simple hecho de invocarla es decir
#mandarla llamar

#sintaxis:

#def nombredeMifuncion(parametros):
    #bloque o conjunto de instrucciones
    
 #   nombredeMifuncion(parametros)
    
#Las funciones pueden sr de 4 tipos
#1.- Funcion que no recibe parametros y no regresa valor
#2.- Funcion que no recibe parametros y regresa valor
#3.- Funcion que recibe parametros y no regresa valor
#4.- Funcion que recibe parametros y regresa valor

#Ejemplo 1: Crear una funcion para imprimir nombres de personas 
#1.- Funcion que no recibe parametros y no regresa valor
def solicitarNombres():
    nombre=input("Ingresa el nombre completo: ")
    
    solicitarNombres()
    
    
    #Ejemplo 2: sumar dos numeros 
    def suma():
        n1=int(input("Numero 1: "))
        n2=int(input("Numero 2"))
        suma=n1+n2
        print(f"{n1} + {n2} = {suma}")
        
    suma()
    
    
    #Ejemplo 3 sumar dos numeros 
    
    def suma():
        n1=int(input("Numero 1: "))
        n2=int(input("Numero 2"))
        suma=n1+n2
        return suma
    
    resultado_suma=suma()
    print(f"La suma es: {resultado_suma}")


#Ejemplo 4 sumar dos numeros
#3.-Funcion que recibe parametros y no regresa valor
    def suma(num1,num2):
        suma=num1+num2
        return suma
        
        num1=int(input("Numero 1: "))
        num2=int(input("Numero 2"))
        resultado_suma(n1, n2)
    
    resultado_suma=suma()


#Ejemplo 6 crear un programa que solicite a traves de una funcion la   
#siguiente informacion: Nombre del paciente, Edad, Estatura, Tipo de sangre.
#Utilizar los 4 tipos de funciones  

    def info(Nombre, Edad, Estatura, Tipo):
        Nombre=str(input("Ingrese nombre del paciente: "))
        Edad=int(input("Ingresar edad: "))
        Estatura=float(input("Ingresar estatura: "))
        Tipo=str(input("Ingresar tipoo de sangre: "))
        
        
