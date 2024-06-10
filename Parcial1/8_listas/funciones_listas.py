paises=["Mexico", "USA", "Brasil", "Japon"]
numeros=[23,100, 2.1416,0,100]
varios=["Hola", True, 100,10.22]


#Ordenar la lista

print(paises)
paises.sort()
print(paises)

print(numeros)
numeros.sort()
print(numeros)
#no se pueden ordenar una lista si tiene diferentes tipos de datos


#Agregar elementos a la lista
print(numeros)
numeros.insert(len(numeros),100)
print(numeros)
numeros.append(100)

#Eliminar elementos a la lista
print(numeros)
numeros.pop(2)#poner la posicion que queremos eliminar
print(numeros)
numeros.remove(100)#borra todos los datos que tengan ese valor

#Busca un dato dentro de una lista
encontrar="Brasil" in paises
print(encontrar)

#Dar la vuelta a una lista
print(varios)
varios.reverse()
print(varios)

#Unir listas
print(paises)
paises.extend(numeros)
print(paises)

#Vaciar una lista (borrar contenido)
print(varios)
varios.clear()
print(varios)