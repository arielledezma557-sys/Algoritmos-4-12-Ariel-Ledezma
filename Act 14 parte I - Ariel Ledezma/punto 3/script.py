#3. Cargar una lista con 5 elementos enteros. Imprimir el mayor y un mensaje
#si se repite dentro de la lista (es decir si dicho valor se encuentra en 2 o
#más posiciones en la lista)

numeros = []

for i in range(5):
    num = int(input("Ingrese un número entero: "))
    numeros.append(num)

mayor = numeros[0]

for i in range(1, 5):
    if numeros[i] > mayor:
        mayor = numeros[i]

print("El número mayor es:", mayor)

cantidad = numeros.count(mayor)


if cantidad >= 2:
    print("El numeros mayor se repiten en la lista")

else:
    print("El número mayor no se repite")


