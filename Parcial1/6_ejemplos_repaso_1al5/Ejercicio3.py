# Escribir un programa que muestre los cuadrados 
#(un numero multiplicado por si mismo) de los 60 primeros 
#numeros naturales. Resolverlo con while y for


num = 1

# Usamos un bucle while para recorrer los números del 1 al 60
while num <= 60:
    # Calculamos el cuadrado del número actual
    cuadrado = num * num
    # Mostramos el número y su cuadrado
    print(f"{num}^2 = {cuadrado}")
    # Incrementamos num en 1 para pasar al siguiente número
    num += 1
    
    


# Usamos un bucle for para recorrer los números del 1 al 60
for num in range(1, 61):
    # Calculamos el cuadrado del número actual
    cuadrado = num * num
    # Mostramos el número y su cuadrado
    print(f"{num}^2 = {cuadrado}")