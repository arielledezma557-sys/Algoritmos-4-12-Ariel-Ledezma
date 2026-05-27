#2. Una empresa registra los nombres de sus 5 vendedores y el total de ventas
#realizadas por cada uno en un mes. Cargar los nombres y ventas en dos
#vectores paralelos, ordenar los datos de mayor a menor según las ventas,
#imprimir la lista ordenada con nombre y monto de la venta, e informar quien fue
#el que menos vendió de los 5 empleados.

vendedores = []
ventas = []

for i in range(5):
    nombre = input("Ingrese el nombre del vendedor: ")
    venta = int(input("Ingrese el total vendido: "))
    vendedores.append(nombre)
    ventas.append(venta)

for i in range(5):
    for j in range(i + 1, 5):
        if ventas[i] < ventas[j]:
            auxVenta = ventas[i]
            ventas[i] = ventas[j]
            ventas[j] = auxVenta
            auxNombre = vendedores[i]
            vendedores[i] = vendedores[j]
            vendedores[j] = auxNombre
print("Lista Ordenada")

for i in range(5):
    print(vendedores[i], " ", ventas[i])
print("El vendedor que menos vendió fue:")
print(vendedores[4], " ", ventas[4])




