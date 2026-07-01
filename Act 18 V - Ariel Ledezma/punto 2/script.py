"""""
2. Confeccionar una función que reciba tres enteros y los muestre ordenados
de menor a mayor. En otra función solicitar la carga de 3 enteros por
teclado y proceder a llamar a la primer función definida.
"""""

def ordenar_mostrar(a, b, c):
    lista = [a, b, c]
    lista.sort()

    print("Números ordenados:")
    for numero in lista:
        print(numero)

def cargar_datos():
    numero1 = int(input("Ingrese el primer número: "))
    numero2 = int(input("Ingrese el segundo número: "))
    numero3 = int(input("Ingrese el tercer número: "))

    ordenar_mostrar(numero1, numero2, numero3)
    cargar_datos()

