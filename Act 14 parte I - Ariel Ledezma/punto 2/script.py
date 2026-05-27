#2. Una empresa tiene dos turnos (mañana y tarde) en los que trabajan 8
#empleados (4 por la mañana y 4 por la tarde) Confeccionar un programa
#que permita almacenar los sueldos de los empleados agrupados en dos
#listas. Imprimir las dos listas de sueldos.

mañana = []
tarde = []

print("Carga de sueldos turno mañana")

for i in range(4):
    sueldo = int(input("Ingrese sueldo: "))
    mañana.append(sueldo)

print("Carga de sueldos turno tarde")

for i in range(4):
    sueldo = int(input("Ingrese sueldo: "))
    tarde.append(sueldo)

print("Lista de sueldos turno mañana:")
print(mañana)

print("Lista de sueldos turno tarde:")
print(tarde)

