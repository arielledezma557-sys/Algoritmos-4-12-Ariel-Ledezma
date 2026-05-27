#3. Realizar un programa que permita cargar dos listas de 
#15 valores cada una. Informar con un mensaje cuál de las 
#dos listas tiene un valor acumulado mayor 
#(mensajes "Lista 1 mayor", "Lista 2 mayor", "Listas iguales") 
#Tener en cuenta que puede haber dos o más estructuras 
#repetitivas en un algoritmo. 

lista1 = []
lista2 = []

suma1 = 0
suma2 = 0

print("Carga de la lista 1")
for i in range(15):
    valor = int(input(f"Ingrese valor {i + 1}: "))
    lista1.append(valor)
    suma1 += valor

print("Carga de la lista 2")
for i in range(15):
    valor = int(input(f"Ingrese valor {i + 1}: "))
    lista2.append(valor)
    suma2 += valor

if suma1 > suma2:
    print("Lista 1 mayor")
elif suma2 > suma1:
    print("Lista 2 mayor")
else:
    print("Listas iguales")


