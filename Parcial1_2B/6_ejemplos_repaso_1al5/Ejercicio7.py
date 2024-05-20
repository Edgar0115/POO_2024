# Hacer un programa que muestre todos los numeros impares entre 2 numeros que decida el usuario

num1=input("Ingrese el primer numero: ")
num2=input("Ingrese el segundo numero: ")



for num in range(num1 + 1, num2):
    # % comprobar
    if num % 2 != 0:
        print(num)