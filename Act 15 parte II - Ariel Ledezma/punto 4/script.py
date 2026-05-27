#4. Cargar una lista con 5 elementos enteros. Ordenar de menor a mayor y
#mostrarla por pantalla, luego ordenar de mayor a menor e imprimir
#nuevamente.

numeros = []

for i in range(5):
    numero = int(input("Ingrese un número: "))
    numeros.append(numero)

numeros.sort()

print("Lista ordenada de menor a mayor:")
print(numeros)

numeros.sort(reverse=True)

print("Lista ordenada de mayor a menor:")
print(numeros)




