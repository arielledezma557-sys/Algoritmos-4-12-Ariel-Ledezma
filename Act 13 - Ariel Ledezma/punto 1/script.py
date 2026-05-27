#1. En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500,
#realizar un programa que lea los sueldos que cobra cada empleado e informe cuántos
#empleados cobran entre $100 y $300 y cuántos cobran más de $300. Además el
#programa deberá informar el importe que gasta la empresa en sueldos al personal.

cantidaddeempleados = int(input("Ingrese la cantidad de empleados: "))

entre100y300 = 0
mayor300 = 0
totaldesueldos = 0

for i in range(cantidaddeempleados):
    sueldo = int(input(f"Ingrese el sueldo del empleado {i + 1}: "))

    if sueldo >= 100 and sueldo <= 300:
        entre100y300 += 1
    elif sueldo > 300:
        mayor300 += 1

    totaldesueldos += sueldo

print("Empleados que cobran entre $100 y $300:", entre100y300)
print("Empleados que cobran más de $300:", mayor300)
print("Total gastado en sueldos:", totaldesueldos)


