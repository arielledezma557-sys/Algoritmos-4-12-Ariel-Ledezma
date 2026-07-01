"""
2. Desarrollar una aplicación que permita ingresar por teclado los nombres de
5 artículos y sus precios.
Definir las siguientes funciones:
1) Cargar los nombres de artículos y sus precios.
2) Imprimir los nombres y precios.
3) Imprimir el nombre de artículo con un precio mayor
4) Ingresar por teclado un importe y luego mostrar todos los artículos con
un precio menor igual al valor ingresado.
"""

def cargar_articulos():
    nombres = []
    precios = []

    for i in range(5):
        nombre = input(f"Ingrese el nombre del artículo {i+1}: ")
        precio = float(input("Ingrese el precio: "))

        nombres.append(nombre)
        precios.append(precio)

    return nombres, precios


def imprimir_articulos(nombres, precios):
    print("Artículos:")
    for i in range(len(nombres)):
        print(nombres[i], "-", precios[i])


def articulo_mayor(nombres, precios):
    mayor = precios[0]
    posicion = 0

    for i in range(1, len(precios)):
        if precios[i] > mayor:
            mayor = precios[i]
            posicion = i

    print("Artículo más caro:")
    print(nombres[posicion], "-", mayor)


def menor_igual(nombres, precios):
    importe = float(input("Ingrese un importe: "))

    print("Artículos con precio menor o igual:")
    for i in range(len(precios)):
        if precios[i] <= importe:
            print(nombres[i], "-", precios[i])

nombres, precios = cargar_articulos()

imprimir_articulos(nombres, precios)
articulo_mayor(nombres, precios)
menor_igual(nombres, precios)


