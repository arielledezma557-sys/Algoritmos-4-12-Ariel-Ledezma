#3. Solicitar por teclado la cantidad de empleados que tiene la empresa. Crear
#y cargar una lista con todos los sueldos de dichos empleados. Imprimir la
#lista de sueldos ordenamos de menor a mayor.

sueldos = []

cantidad = int(input("Ingrese la cantidad de empleados: "))

for i in range(cantidad):
    sueldo = int(input("Ingrese el sueldo: "))
    sueldos.append(sueldo)

sueldos.sort()

print("Lista de sueldos ordenada de menor a mayor:")
print(sueldos)


