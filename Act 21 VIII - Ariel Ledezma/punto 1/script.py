"""
1-
Confeccionar un programa con las siguientes funciones:
1)Cargar una lista de 5 enteros.
2)Retornar el mayor y menor valor de la lista mediante una tupla.
Desempaquetar la tupla en el bloque principal y mostrar el mayor y menor.
"""
def cargar_lista():
    lista = []
    for i in range(5):
        num = int(input("Ingrese un número entero: "))
        lista.append(num)
    return lista


def mayor_menor(lista):
    mayor = max(lista)
    menor = min(lista)
    return (mayor, menor)  

numeros = cargar_lista()
mayor, menor = mayor_menor(numeros)  
print("Mayor:", mayor)
print("Menor:", menor)