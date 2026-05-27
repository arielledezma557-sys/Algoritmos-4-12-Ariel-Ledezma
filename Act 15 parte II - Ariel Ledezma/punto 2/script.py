#2. Realizar un programa que pida la carga de dos listas numéricas enteras
#de 4 elementos cada una. Generar una tercera lista que surja de la suma
#de los elementos de la misma posición de cada lista. Mostrar esta tercera
#lista.


lista1 = []
lista2 = []
lista3 = []

print("Carga de la primera lista")

for i in range(4):
    numero = int(input("Ingrese un número: "))
    lista1.append(numero)

print("Carga de la segunda lista")

for i in range(4):
    numero = int(input("Ingrese un número: "))
    lista2.append(numero)

for i in range(4):
    suma = lista1[i] + lista2[i]
    lista3.append(suma)

print("Tercera lista:")
print(lista3)

