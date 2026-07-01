"""""
4. Crear dos listas paralelas. En la primera ingresar los nombres de empleados y
en la segunda los sueldos de cada empleado.
Ingresar por teclado cuando inicia el programa la cantidad de empleados de la
empresa.
Borrar luego todos los empleados que tienen un sueldo mayor a 10000 (tanto el
sueldo como su nombre)
"""""

empleados = []
sueldos = []

cantidad = int(input("Cantidad de empleados: "))

for i in range(cantidad):
    nombre = input("Nombre del empleado: ")
    sueldo = float(input("Sueldo: "))

    empleados.append(nombre)
    sueldos.append(sueldo)

i = 0
while i < len(sueldos):
    if sueldos[i] > 10000:
        del sueldos[i]
        del empleados[i]
    else:
        i += 1

print("Empleados restantes:")
for i in range(len(empleados)):
    print(empleados[i], "-", sueldos[i])

