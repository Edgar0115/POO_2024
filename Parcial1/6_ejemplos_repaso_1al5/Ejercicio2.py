#Crear un script que muestre en pantalla todos los numeros
# pares del 1 al 20 
# 

for num in range(1, 21, 4): #al agregar un tercer valor significa lo que va a hacer
    #el for se utiliza con numeros enteros
    #el while se utiliza para numeros reales
    # % comprobar
    if num % 2 == 0:
        print(num)