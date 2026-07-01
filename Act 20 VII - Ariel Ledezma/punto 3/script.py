"""
3. Confeccionar un programa que permita:
1) Cargar una lista de 10 elementos enteros.
2) Generar dos listas a partir de la primera. En una guardar los valores
positivos y en otra los negativos.
3) Imprimir las dos listas generadas.
"""
def cargar_lista():
    lista = []

    for i in range(10):
        numero = int(input(f"Ingrese el número {i+1}: "))
        lista.append(numero)

    return lista


def separar(lista):
    positivos = []
    negativos = []

    for numero in lista:
        if numero >= 0:
            positivos.append(numero)
        else:
            negativos.append(numero)

    return positivos, negativos


def imprimir(lista):
    for elemento in lista:
        print(elemento)

numeros = cargar_lista()

positivos, negativos = separar(numeros)

print("Positivos:")
imprimir(positivos)

print("Negativos:")
imprimir(negativos)
