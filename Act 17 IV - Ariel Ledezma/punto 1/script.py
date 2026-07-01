"""""
1. Se tiene la siguiente lista:
lista=[[100,7,85,8], [4,8,56,25], [67,89,23,1], [78,56]]
Imprimir la lista. Luego cambiar de elemento todos los enteros mayores a 50 del
primer elemento de "lista". El resto de enteros menores a 50 deben encontrarse
en una nueva posición dentro de la lista.
Volver a imprimir la lista.
"""""

lista = [[100, 7, 85, 8], [4, 8, 56, 25], [67, 89, 23, 1], [78, 56]]

print("Lista original:")
print(lista)

nuevasublista = []
primerelemento = []

for num in lista[0]:
    if num > 50:
        primerelemento.append(num)
    else:
        nuevasublista.append(num)

lista[0] = primerelemento
lista.append(nuevasublista)

print("Lista modificada:")
print(lista)

[[100, 7, 85, 8], [4, 8, 56, 25], [67, 89, 23, 1], [78, 56]]


[[100, 89], [4, 8, 56, 25], [67, 89, 23, 1], [78, 56], [7, 8]]



