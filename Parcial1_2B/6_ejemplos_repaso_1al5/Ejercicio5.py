#Hacer un programa que muestre todos los numeros entre 2 numeros que diga el usuario

num1= int(input("Ingresa el primer numero:"))
num2= int(input("Ingresa el segundo numero:"))

if num1 < num2:
    
    print("Los números entre", num1, "y", num2, "son:")
    for i in range(num1, num2 + 1):
        print(i, end=" ")
    print()  
else:
    print("El primer número debe ser menor que el segundo número.")