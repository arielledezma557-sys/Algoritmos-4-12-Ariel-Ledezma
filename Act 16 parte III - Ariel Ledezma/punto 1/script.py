#1. Se desea desarrollar un programa que permita registrar los nombres y las
#calificaciones de 6 estudiantes. Luego de cargar los datos, se debe mostrar el
#nombre del estudiante con la nota más alta, junto con su nota. Al igual que el
#estudiante con la nota más baja. Informar si hay estudiantes con la misma nota
#máxima o mínima.

nombres = []
notas = []

for i in range(6):
    nombre = input("ingrese el nombres del estudiante: ")
    nota = int(input("ingrese la notas: "))
    nombres.append(nombre)
    notas.append(nota)
maxnotas = max(notas)
minnotas = min(notas)
print("Resultados")
print("estudiantes con notas más alta:")

for i in range(6):
    if notas[i] == maxnotas:
        print(nombres[i], " ", notas[i])
        print("estudiantes con notas más baja:")

for i in range(6):
    if notas[i] == minnotas:
        print(nombres[i], " ", notas[i])

if notas.count(maxnotas) > 1:
    print("hay estudiantes con la misma notas máxima.")

if notas.count(minnotas) > 1:
    print("hay estudiantes con la misma notas mínima.")




