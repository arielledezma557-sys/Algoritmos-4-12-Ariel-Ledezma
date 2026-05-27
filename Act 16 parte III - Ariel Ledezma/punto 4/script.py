#4. Se realiza una evaluación a 6 docentes por parte de sus alumnos. Se registran
#sus nombres y puntajes promedio obtenidos (de 1 a 10).
#Cargar sus datos en vectores paralelos, mostrar docente con calificación más
#alta y más baja, ordenar los vectores de mayor a menor de acuerdo con la
#calificación y mostrar en pantalla la cantidad de docentes que aprobaron y
#desaprobaron (tomando como base que se aprueba con una nota mayor o
#igual a 6)

docentes = []
notas = []

aprobados = 0
desaprobados = 0

for i in range(6):
        nombre = input("Ingrese el nombre del docente: ")
        nota = int(input("Ingrese la calificación: "))
        docentes.append(nombre)
        notas.append(nota)
if nota >= 6:
        aprobados += 1
else:
    desaprobados += 1
    maxnota = max(notas)
    minnota = min(notas)
    print("Docentes con mejor calificación:")

for i in range(6):
    if notas[i] == maxnota:
        print(docentes[i], " ", notas[i])
        print("Docentes con peor calificación:")

for i in range(6):
    if notas[i] == minnota:
        print(docentes[i], " ", notas[i])

for i in range(6):
    for j in range(i + 1, 6):
        if notas[i] < notas[j]:
            auxNota = notas[i]
            notas[i] = notas[j]
            notas[j] = auxNota
            auxNombre = docentes[i]
            docentes[i] = docentes[j]
            docentes[j] = auxNombre

print("Docentes Ordenados")

for i in range(6):
    print(docentes[i], " ", notas[i])
print("Cantidad de aprobados:", aprobados)
print("Cantidad de desaprobados:", desaprobados)



