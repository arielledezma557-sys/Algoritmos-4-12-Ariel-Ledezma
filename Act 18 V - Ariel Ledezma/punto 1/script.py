"""""
1. Desarrollar un programa que solicite la carga de tres valores y muestre el
menor. Desde el bloque principal del programa llamar 2 veces a dicha
función (sin utilizar una estructura repetitiva)
"""""

def mostrar_menor():
    num1 = int(input("Ingrese el primer valor: "))
    num2 = int(input("Ingrese el segundo valor: "))
    num3 = int(input("Ingrese el tercer valor: "))

    menor = num1

    if num2 < menor:
        menor = num2

    if num3 < menor:
        menor = num3

    print("El menor valor es:", menor)

mostrar_menor()
mostrar_menor()



