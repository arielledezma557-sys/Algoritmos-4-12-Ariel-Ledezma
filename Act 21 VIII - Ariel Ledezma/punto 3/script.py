"""
3-

Almacenar en una lista 5 empleados, cada elemento de la lista es una sub lista
con el nombre del empleado junto a sus últimos tres sueldos (estos tres valores en
una tupla)
El programa debe tener las siguientes funciones:
1)Carga de los nombres de empleados y sus últimos tres sueldos.
2)Imprimir el monto total cobrado por cada empleado.
3)Imprimir los nombres de empleados que tuvieron un ingreso trimestral mayor a
10000 en los últimos tres meses.
Tener en cuenta que la estructura de datos si se carga por asignación debería ser
similar a:
empleados = [[&quot;juan&quot;,(2000,3000,4233)] , [&quot;ana&quot;,(3444,1000,5333)] , etc. ]
"""

def cargar_empleados():
    empleados = []

    for i in range(5):
        nombre = input("Ingrese nombre del empleado: ")

        sueldo1 = int(input("Sueldo 1: "))
        sueldo2 = int(input("Sueldo 2: "))
        sueldo3 = int(input("Sueldo 3: "))

        sueldos = (sueldo1, sueldo2, sueldo3)
        empleados.append([nombre, sueldos])

    return empleados


def total_cobrado(empleados):
    for empleado in empleados:
        total = sum(empleado[1])
        print(empleado[0], "cobró en total:", total)


def mayores_10000(empleados):
    print("Empleados con ingreso trimestral mayor a 10000:")
    for empleado in empleados:
        total = sum(empleado[1])
        if total > 10000:
            print(empleado[0])

empleados = cargar_empleados()
total_cobrado(empleados)
mayores_10000(empleados)

[
 ["Juan", (2000,3000,4000)],
 ["Ana", (4000,5000,6000)]
]
