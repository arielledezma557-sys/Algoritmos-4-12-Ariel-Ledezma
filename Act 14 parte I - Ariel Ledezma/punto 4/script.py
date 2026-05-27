#4. Cargar por teclado y almacenar en una lista las alturas de 5 personas
#(valores float)
#Obtener el promedio de las mismas. Contar cuántas personas son más
#altas que el promedio y cuántas más bajas.

alturas = []
suma = 0

for i in range(5):
    altura = float(input("Ingrese la altura: "))
    alturas.append(altura)
    suma = suma + altura

promedio = suma / 5

masaltas = 0
masbajas = 0

for altura in alturas:
    if altura > promedio:
        masaltas = masaltas + 1
    elif altura < promedio:
        masbajas = masbajas + 1

print("Promedio de alturas:", promedio)
print("Personas más altas que el promedio:", masaltas)
print("Personas más bajas que el promedio:", masbajas)


