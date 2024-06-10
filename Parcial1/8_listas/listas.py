# """
# List (Array)Son colecciones o conjunto de datos/valores bajo un mismo nombre, para acceder a los valores se hace con un indice numerico

# Nota: sus valores si son modificables

# La lista es una colección ordenada y modificable.
# Permite miembres duplicados
# """

# """
# #Ejemplo 1: Crear una lista de números e imprimir el contenido
# list=["a","b","c"]
# for i in list:
#     print(i)


# i=0
# cont=len(list)-1
# while i <= cont:
#     print(list[i])
#     i+=1
# """

# #Ejemplo 2: Crear una lista de palabras y posteriormente buscar la coincidencia de una palabra en 

# palabras=["Edgar", "Jair", "Garcia", "Santillan"]
# palabra=input("Ingrese la palabra: ")
# # for i in palabras:
# #     if i == palabra:
# #         print(palabras.index)
# #         #print(f"Encontrado en: {i}")

# repetir = True
# # while palabra in palabras:
# #     print(palabra)

# i=o
# while i<len(palabras):
#     if palabra in palabras:
#         print(palabras.index(i))
#         repetir=False


# """Investigar todo sobre Listas


# #ejemplo 3: agregar y eliminar elementos de una lista
# #os.system("clear")

# numeros=[23,24,25]
# print(numeros)

# #agregar elementos

# numeros.append(100)
# print(numeros)
# numeros.insert(3,200)
# print(numeros)

# #eliminar un elementos
# numeros.remove(100) #Indica el elemento
# print(numeros)
# numeros.pop(2) #Indica la posición
# print(numeros)


# """


# #Ejemplo 4: Lista Multilinea o Multidimencional (Matriz) con nombres y números

agenda=[
    ["Lucas", 8171178455],
    ["Ernesto", 5555171717],
    ["Erik", 6181234567],
    ["Antonio", 6181212121]
]

print(agenda)

for i in agenda:
    print(f"{agenda.index(i)+1} .-{i}")