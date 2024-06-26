# 1.- 

#  Hacer un programa que tenga una lista de 8 numeros enteros y realice lo siguiente: 

#  a.- Recorrer la lista y mostrarla
#  b.- hacer una funcion que recorra la lista de numeros y devuelva un string
#  c.- ordenarla y mostrarla
#  d.- mostrar su longitud
#  e.- buscar algun elemento que el usuario pida por teclado


#Punto A
numeros=[1,4,9,16,44,935,115,18]

# for orden in numeros:
#     print(orden)
    

# #Punto B


# #Punto C
# print(numeros)
# numeros.sort()
# print(numeros)

#Punto D


#Punto E
palabra=input("Ingrese el numero a buscar: ")
for i in palabra:
    if i == numeros:
        print(numeros.index)
        print(f"Encontrado en: {i}")
        
repetir = True
while palabra in palabra:
    print(numeros)

i=0
while i<len(numeros):
    if palabra in palabra:
        print(palabra.index(i))
        repetir=False
        break