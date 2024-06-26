import os
"""
i = True
while i:
    print(f"========== \n Calculadora Básica \n=============")
    print("1.- Suma")
    print("2.- Resta")
    print("3.- Multiplicación")
    print("4.- Divición")
    print("5.- Salir")
    opcion= input("Elige una opción ").upper()

    #====Suma=====
    if opcion=="1" or opcion=="+" or opcion=="SUMA":
        n1=int(input("Número 1: "))
        n2=int(input("Número 2: "))
        suma=n1+n2
        print(f"{n1} + {n2} = {suma}")

    #=====Resta=====
    elif opcion=="2" or opcion=="-" or opcion=="RESTA":
        n1=int(input("Número 1: "))
        n2=int(input("Número 2: "))
        resta=n1-n2
        print(f"{n1} - {n2} = {resta}")

    #=====Multiplicación=====
    elif opcion=="3" or opcion=="x" or opcion=="MULTIPLICACION":
        n1=int(input("Número 1: "))
        n2=int(input("Número 2: "))
        divicion=n1*n2
        print(f"{n1} x {n2} = {divicion}")

    #=====Divición=====
    elif opcion=="4" or opcion=="/" or opcion=="DIVICION":
        n1=int(input("Número 1: "))
        n2=int(input("Número 2: "))
        multiplicacion=n1/n2
        print(f"{n1} / {n2} = {multiplicacion}")

    else:
        print("Saliste")
        i=False

"""

#=====Funciones=====

def SolicitarNumeros():
    global n1,n2
    n1=int(input("Número 1: "))
    n2=int(input("Número 2: "))

def OperacionesArit(n1,n2):
    global i
    #====Suma=====
    if opcion=="1" or opcion=="+" or opcion=="SUMA":
        suma=n1+n2
        return(f"{n1} + {n2} = {suma}")

    #=====Resta=====
    elif opcion=="2" or opcion=="-" or opcion=="RESTA":
        resta=n1-n2
        return(f"{n1} - {n2} = {resta}")

    #=====Multiplicación=====
    elif opcion=="3" or opcion=="x" or opcion=="MULTIPLICACION":
        multiplicacion=n1*n2
        return(f"{n1} x {n2} = {multiplicacion}")

    #=====Divición=====
    elif opcion=="4" or opcion=="/" or opcion=="DIVICION":
        divicion=n1/n2
        return(f"{n1} / {n2} = {divicion}")
    

i=True
while i:
    os.system("Clear")
    print(f"========== \n Calculadora Básica \n=============")
    print("1.- Suma")
    print("2.- Resta")
    print("3.- Multiplicación")
    print("4.- Divición")
    print("5.- Salir")
    opcion= input("Elige una opción ").upper()

    #if opcion!=1 or opcion!=2 or opcion!=3 or opcion!=4:
    if opcion!="5": 
        SolicitarNumeros()
        print(OperacionesArit(n1,n2))
    else:
        print("Saliste")
        
        i=False 