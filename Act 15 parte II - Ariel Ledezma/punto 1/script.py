#1. En un curso de 4 alumnos se registraron las notas de sus exámenes y se deben procesar de acuerdo a lo siguiente:
#a. Ingresar nombre y nota de cada alumno (almacenar los datos en dos listas paralelas)
#b. Realizar un listado que muestre los nombres, notas y condición del
#alumno. En la condición, colocar "Muy Bueno" si la nota es mayor o
#igual a 8, "Bueno" si la nota está entre 4 y 7, y colocar "Insuficiente"
#si la nota es inferior a 4.
#c. Imprimir cuántos alumnos tienen la leyenda “Muy Bueno”.

nombres = []
notas = []

for i in range(4):
    nombre = input("Ingrese el nombre del alumno: ")
    nombres.append(nombre)
    nota = int(input("Ingrese la nota del alumno: "))
    notas.append(nota)
muybueno = 0
print("Listado de alumnos:")

for i in range(4):
    if notas[i] >= 8:
        condicion = "Muy Bueno"
        muybueno += 1
    elif notas[i] >= 4:
        condicion = "Bueno"
    else:
        condicion = "Insuficiente"
    print("Nombre:", nombres[i],
          "Nota:", notas[i],
          "Condición:", condicion)
print("Cantidad de alumnos con condición 'Muy Bueno':", muybueno)



