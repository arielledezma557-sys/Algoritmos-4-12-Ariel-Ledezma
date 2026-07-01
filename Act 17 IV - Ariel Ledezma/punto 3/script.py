""""
3. Definir una lista y almacenar los nombres de 3 empleados.
Por otro lado definir otra lista y almacenar en cada elemento una sublista con los
números de días del mes que el empleado faltó.
Imprimir los nombres de empleados y los días que faltó.
Mostrar los empleados con la cantidad de inasistencias.
Finalmente mostrar el nombre o los nombres de empleados que faltan menos
días.
"""""

empleados = []
faltas = []

for i in range(3):
    nombre = input("Nombre del empleado: ")
    empleados.append(nombre)

    cantidad = int(input("Cantidad de faltas: "))
    dias = []

    for j in range(cantidad):
        dia = int(input("Día faltado: "))
        dias.append(dia)

    faltas.append(dias)

print("Empleados y días faltados:")
for i in range(3):
    print(empleados[i], "-", faltas[i])

print("Cantidad de inasistencias:")
menor = len(faltas[0])

for i in range(3):
    cantidad = len(faltas[i])
    print(empleados[i], "-", cantidad)

    if cantidad < menor:
        menor = cantidad

print("Empleado/s con menos faltas:")
for i in range(3):
    if len(faltas[i]) == menor:
        print(empleados[i])
