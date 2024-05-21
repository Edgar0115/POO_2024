#El for es una estructura de control repetitiva o ciclica que funciona con interaciones x veces deacuerdo a los valosres numericos enteros que contenga

#sintaxis

#for variable in elemento _interables(list,range,etc):
#    bloque instrucciones


#Ejemplo 1 Crear un programa que imprima 5 veces el caracter @


for contador in range (1,6):
    print("@")

#Ejemplo 2 Crear un programa que imprima los numeros del 1 al 5, los suma y los imprima al final

suma=0
for contador in range (1,6):
    print(contador)
    suma+=contador
print(f"la suma es: {suma}")

#Ejamplo 3 crear un programa que solicite un numero entero y 

numero=int(input("Ingrese un numero:"))


multi=0
for i in range(1,11)
   multi=numero*i
   print(f"{numero} x{i} = {multi}")