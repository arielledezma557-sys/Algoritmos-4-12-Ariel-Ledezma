"""
2. En una empresa se almacenaron los sueldos de 10 personas.
Desarrollar las siguientes funciones y llamarlas desde el bloque principal:
1) Carga de los sueldos en una lista.
2) Impresión de todos los sueldos.
3) Cuántos tienen un sueldo superior a $4000.
4) Retornar el promedio de los sueldos.
5) Mostrar todos los sueldos que están por debajo del promedio.
"""

def cargar_sueldos():
    lista = []

    for i in range(10):
        sueldo = float(input(f"Ingrese el sueldo {i + 1}: "))
        lista.append(sueldo)

    return lista


def imprimir_sueldos(lista):
    print("Sueldos:")
    for sueldo in lista:
        print(sueldo)


def mayores_4000(lista):
    contador = 0

    for sueldo in lista:
        if sueldo > 4000:
            contador += 1

    print("Sueldos mayores a $4000:", contador)


def promedio(lista):
    return sum(lista) / len(lista)


def debajo_promedio(lista, prom):
    print("Sueldos debajo del promedio:")
    for sueldo in lista:
        if sueldo < prom:
            print(sueldo)

sueldos = cargar_sueldos()

imprimir_sueldos(sueldos)
mayores_4000(sueldos)
prom = promedio(sueldos)
print("Promedio:", prom)
debajo_promedio(sueldos, prom)


